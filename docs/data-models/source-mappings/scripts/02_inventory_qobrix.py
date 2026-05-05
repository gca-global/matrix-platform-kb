#!/usr/bin/env python3
"""
Inventory the Qobrix OpenAPI 3.0 schemas relevant to Sharp Matrix.

Reads:
  ../../../../raw/qobrix/qobrix_openapi.yaml

Writes:
  raw/qobrix_inventory.csv

Phase: Inventory (mechanical, deterministic).
Owner: scripts/02_inventory_qobrix.py - do NOT hand-edit raw/qobrix_inventory.csv.

In-scope schemas (Sharp Matrix's six target RESO resources):
  - Property            -> RESO Property
  - Contact             -> RESO Contacts
  - Agent, User         -> RESO Member (Qobrix splits brokerage staff)
  - Group               -> RESO Teams (Qobrix has no Branch/Office schema;
                          office data lives on Property/Agent flat fields)
  - Media               -> RESO Media

Determinism:
  - Sorted by (schema, property_path).
  - csv.QUOTE_MINIMAL.
  - Enum values are stored sorted then JSON-serialized for stable diff.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any

import yaml

KB_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = KB_ROOT.parent.parent.parent
SPEC_PATH = REPO_ROOT / "raw" / "qobrix" / "qobrix_openapi.yaml"
OUT_CSV = KB_ROOT / "raw" / "qobrix_inventory.csv"

IN_SCOPE_SCHEMAS = [
    "Property",
    "PropertyCoordinates",
    "Contact",
    "Agent",
    "User",
    "Group",
    "Media",
    "MediaResponse",
    "MediaFile",
    "MediaRequest",
]

MAX_DEPTH = 3


def first_sentence(text: str | None) -> str:
    if not text:
        return ""
    text = text.strip().replace("\n", " ").replace("\r", " ")
    text = " ".join(text.split())
    if "." in text:
        return text.split(".", 1)[0] + "."
    return text


def walk_schema(
    schemas: dict[str, Any],
    schema_name: str,
    schema: dict[str, Any],
    prefix: str = "",
    depth: int = 0,
    visited: tuple[str, ...] = (),
) -> list[dict]:
    """Walk one schema; emit one row per leaf (non-object) property and one
    row per object property (parents are useful for navigation)."""
    rows: list[dict] = []
    if depth > MAX_DEPTH:
        return rows
    if schema.get("type") != "object" and "properties" not in schema:
        return rows

    for prop_name, prop in (schema.get("properties") or {}).items():
        path = f"{prefix}/{prop_name}" if prefix else prop_name
        ref = prop.get("$ref")
        prop_type = prop.get("type")
        prop_format = prop.get("format", "")
        description = first_sentence(prop.get("description"))
        required_yn = "yes" if prop_name in (schema.get("required") or []) else "no"
        nullable_yn = "yes" if prop.get("nullable") else "no"

        enum_values = prop.get("enum")
        items = prop.get("items") or {}

        # Resolve $ref if present (only one level deep, for nested type info).
        if ref and isinstance(ref, str) and ref.startswith("#/components/schemas/"):
            target_name = ref.split("/")[-1]
            if target_name not in visited:
                target = schemas.get(target_name)
                if target and target.get("type") == "object":
                    rows.append(
                        {
                            "schema": schema_name,
                            "property_path": path,
                            "type": "object",
                            "format": "",
                            "ref": target_name,
                            "items_type": "",
                            "required_yn": required_yn,
                            "nullable_yn": nullable_yn,
                            "description": description,
                            "enum_values_json": "",
                        }
                    )
                    rows.extend(
                        walk_schema(
                            schemas,
                            schema_name,
                            target,
                            prefix=path,
                            depth=depth + 1,
                            visited=visited + (target_name,),
                        )
                    )
                    continue

        # Array items: capture the item type or ref name.
        items_type = ""
        if prop_type == "array" and items:
            if items.get("$ref"):
                items_type = items["$ref"].split("/")[-1]
            else:
                items_type = items.get("type", "")
            # If items.enum is present, treat as enum at this level.
            if items.get("enum") and not enum_values:
                enum_values = items["enum"]

        rows.append(
            {
                "schema": schema_name,
                "property_path": path,
                "type": prop_type or ("ref" if ref else ""),
                "format": prop_format,
                "ref": (ref.split("/")[-1] if ref else ""),
                "items_type": items_type,
                "required_yn": required_yn,
                "nullable_yn": nullable_yn,
                "description": description,
                "enum_values_json": (
                    json.dumps(sorted(enum_values), ensure_ascii=False)
                    if enum_values
                    else ""
                ),
            }
        )

    return rows


def main() -> int:
    if not SPEC_PATH.is_file():
        print(f"ERROR: Qobrix spec not found: {SPEC_PATH}", file=sys.stderr)
        return 2

    with SPEC_PATH.open("r", encoding="utf-8") as fh:
        spec = yaml.safe_load(fh)

    schemas = spec.get("components", {}).get("schemas", {})
    if not schemas:
        print("ERROR: no components.schemas in spec", file=sys.stderr)
        return 2

    rows: list[dict] = []
    for schema_name in IN_SCOPE_SCHEMAS:
        schema = schemas.get(schema_name)
        if not schema:
            print(f"WARN: in-scope schema '{schema_name}' not found in spec", file=sys.stderr)
            continue
        rows.extend(
            walk_schema(
                schemas,
                schema_name,
                schema,
                visited=(schema_name,),
            )
        )

    rows.sort(key=lambda r: (r["schema"], r["property_path"]))

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "schema",
                "property_path",
                "type",
                "format",
                "ref",
                "items_type",
                "required_yn",
                "nullable_yn",
                "description",
                "enum_values_json",
            ],
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    for row in rows:
        counts[row["schema"]] = counts.get(row["schema"], 0) + 1
    parts = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    print(f"[02] wrote {OUT_CSV.relative_to(KB_ROOT)}: {len(rows)} rows ({parts})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
