# Sharp Matrix Financial Management — 1st Line Support Knowledge Base

> **App name:** Matrix Financial Management (Matrix FM)
> **URL:** [https://intranet.sharpsir.group/matrix-fm/](https://intranet.sharpsir.group/matrix-fm/)
> **Purpose:** Group financial reporting, budgeting, annual planning, CORE cost allocation, and financial analytics across all Sharp Group entities.
> **Users:** Finance Team, Entity Managers, Senior Management, CFO/Board

---

## What Is Matrix Financial Management?

Matrix Financial Management is the financial reporting and planning app for Sharp Group. It allows finance teams and entity managers to submit monthly and annual financial data (actuals, budgets, estimations, forecasts), perform multi-year annual planning, allocate CORE (central overhead) costs across entities, track submission deadlines, and view analytics. It provides a centralized view of financial health across all group entities.

---

## How to Access Matrix Financial Management

1. Open your browser and go to [https://intranet.sharpsir.group/matrix-fm/](https://intranet.sharpsir.group/matrix-fm/).
2. You will be redirected to the Sharp Matrix SSO login page.
3. Sign in with your company email and password, or use "Sign in with Microsoft".
4. After login you land on the **Home Dashboard**.

If you cannot log in, your account may not have access to Matrix FM. Contact your Admin or IT department.

---

## User Roles and What They Can Do

| Role | What They Can Do |
|------|-----------------|
| **Entity Finance User** | Enter and submit financial data for their entity, view own submissions, track deadlines |
| **Country Manager** | View financial data across entities in their country, monitor submission progress |
| **Group Finance** | View all entities, manage CORE allocation, set deadlines, run analytics, export reports |
| **Admin** | Full access: all capabilities plus permissions, settings, data layer configuration, test data management |

---

## Main Features

### Home Dashboard

The home page shows:
- **Submission Progress** — summary cards: Total Business Units, Submitted This Month, In Progress, Overdue
- **Key Performance Indicators** — KPI cards: YTD Actual, YTD Budget Variance, Gross Margin, Budget Utilization
- **Upcoming Deadlines** — next submission deadlines (deadlines within 7 days are highlighted)
- **Recent Updates** — latest changes across all entities

### Monthly Reporting

Enter and review monthly financial data for each entity.

1. Click **Monthly Reporting** in the sidebar.
2. Select an **entity** and a **month/year**.
3. View and edit four financial statement types:
   - **P&L** (Profit & Loss) — revenue and expense line items
   - **Cash Flow** — cash inflows and outflows
   - **Balance Sheet** — assets, liabilities, equity
   - **Working Capital** — short-term financial position
4. For each line item, enter values in the four data type columns:
   - **Budget** — the approved budget figure (labeled with the budget cycle year)
   - **Actual** — the real figure for the period
   - **Estimation** — estimated figures (used before actuals are finalized)
   - **Forecast** — updated forward-looking forecast
5. Each line item also has a **Notes** column for adding context.
6. Click **Save Changes** to save your progress (data remains in Draft status).
7. Click **Submit** when all data is complete (locks the data from further editing).

**Clipboard paste:** You can copy data from Excel and paste it into the monthly reporting grid using Ctrl+V. The system matches column headers and line items automatically. A confirmation dialog shows matched data before applying. Paste is available in Monthly Reporting mode.

### Annual Reporting

View and submit full-year actual financial data.

1. Click **Annual Reporting** in the sidebar.
2. Select an entity and year.
3. Review annual **Actual** figures across all statement types (P&L, Cash Flow, Balance Sheet, Working Capital).
4. Enter annual actuals and submit when complete.

### Annual Planning

Create multi-year financial plans.

1. Click **Annual Planning** in the sidebar. Subtitle: "Plan budgets for the next three fiscal years."
2. Select a **Budget Cycle** year. The planning header shows "Planning: {Y+1} – {Y+3}."
3. View a five-column model (where `Y` is the selected budget cycle year):
   - **{Y-1} Actual** — last year's actual figures (read-only reference)
   - **{Y} Budget** — current year approved budget (read-only reference)
   - **{Y+1} Budget** — next year plan (editable, expandable to monthly breakdown)
   - **{Y+2} Budget** — two-year plan (editable, expandable to monthly breakdown)
   - **{Y+3} Budget** — three-year plan (editable, expandable to monthly breakdown)
4. Enter planned figures for future years.
5. Save and submit.

### CORE Allocation

Manage how central overhead costs are distributed across business units.

1. Click **CORE Allocation** in the sidebar. Subtitle: "Distribute CORE costs across Business Units by percentage."
2. Select a year (2023–2026 available).
3. View **Yearly Distribution** — allocation percentages for each business unit (entities with code "CORE" are excluded from the list as they are the source of costs).
4. Edit allocation percentages (must total 100% across all business units).
5. Use **Distribute Evenly** to split costs equally, or set custom percentages.
6. Click **Save Allocations**.

### Data Entry Progress

Track which business units have submitted their financial data.

1. Click **Data Entry Progress** in the sidebar. Subtitle: "Track submission status and completion across all business units."
2. View stats: **Total BUs**, **Fields per BU/Month**, **Submitted This Year**, **Overdue**.
3. View a progress matrix showing submission status by entity and month, color-coded: **Submitted** (green), **In Progress** (yellow), **Not Started** (gray), **Overdue** (red).
4. Click **Manage Deadlines** to set or adjust submission deadlines per entity and month.
5. Identify outstanding submissions and follow up with responsible users.

### Analytics & Reports

View financial analytics and comparisons.

1. Click **Analytics** in the sidebar. Page title: "Analytics & Reports."
2. Select a statement type (P&L, Cash Flow, Balance Sheet, Working Capital) and data type to filter.
3. Browse multiple analysis views:
   - **Full Year Summary** — 12-month view with quarterly and annual totals
   - **YTD Analysis** — year-to-date performance with run-rate projections
   - **YoY Comparison** — year-over-year variance and trend analysis
   - **CAGR Analysis** — compound annual growth rates over 2–5 years
   - **Budget vs Actual** — budget utilization and variance tracking
   - **Actual vs Estimation** — forecast accuracy with MAPE and bias metrics
   - **Trend Charts** — visual monthly trends with interactive charts
   - **KPI & Ratios** — margin ratios, cost structure, and efficiency metrics
4. Select **Consolidated (All Entities)** in the entity selector to view group-wide analytics.

### Audit Log

View a record of all changes made in the system.

1. Click **Audit Log** in the sidebar. Subtitle: "Track all changes to financial data across the system."
2. Filter by user, entity, date range, or action type.
3. The log tracks changes to: **Financial Entries**, **Submissions**, **CORE Allocations**, and **Deadlines**.
4. Actions logged: **Created**, **Updated**, **Deleted** — with before/after data for each change.
5. Export the audit log as CSV for compliance purposes.

### Documentation (In-App Help)

Access built-in help and process documentation.

1. Click **Documentation** in the sidebar.
2. Browse topics including budgeting process, statement types, roles, entity hierarchy, and CORE allocation rules.
3. Documentation is available in English and Russian.

### Settings (Admin)

Admins can configure:

- **App Permissions** — role-based page and action access
- **Data Layer** — data source configuration
- **MLS Integration** — MLS settings (shared platform component)
- **AI Providers** — AI settings
- **Agency Hub URL** — return URL for the Back to Agency Hub link
- **Test Data** — generate or delete test financial data for testing purposes

---

## Use Cases: Common Finance Scenarios

### Scenario 1: Monthly Financial Reporting
It's the 5th of the month — time to submit last month's actuals.
1. Open Matrix FM → **Monthly Reporting**.
2. Select your entity and the previous month.
3. Open the **P&L** tab first — enter revenue and expense actuals for each line item.
4. Switch to **Cash Flow** — enter cash movements.
5. Complete **Balance Sheet** and **Working Capital** tabs.
6. For any line items where actuals aren't final yet, enter an **Estimation** instead.
7. Click **Save** after completing each statement type.
8. Review all four tabs. When everything is correct, click **Submit**.
9. Your submission appears in the Data Entry Progress dashboard as "Submitted."

**Tip:** You can copy your data from an Excel spreadsheet and paste it directly into the grid. The system matches headers and line items automatically.

### Scenario 2: Correcting a Submitted Month
You discover an error after submitting.
1. Contact your Group Finance lead or an Admin.
2. They will **withdraw** the submission, unlocking the month for editing.
3. Open Monthly Reporting → select the entity and month.
4. Make your corrections.
5. Click **Save**, then **Submit** again.

### Scenario 3: Annual Budget Planning
The CFO requests next year's budget and a 3-year outlook.
1. Open Matrix FM → **Annual Planning**.
2. Select your entity.
3. Select the budget cycle year. Review the **{Y-1} Actual** column (last year's figures) and the **{Y} Budget** column (current year budget) — both are read-only reference points.
4. Enter your planned figures in **{Y+1} Budget** (next year). You can expand this column to a monthly breakdown.
5. Extend the plan to **{Y+2}** and **{Y+3}** Budget columns for the 3-year outlook.
6. Save and submit when complete.

### Scenario 4: CORE Allocation Review
Group finance needs to update how central overhead is split across entities.
1. Open Matrix FM → **CORE Allocation**.
2. Select the year.
3. Review current allocation percentages for each entity.
4. Adjust percentages based on the new agreed split (must total 100%).
5. Save. The updated allocations will be reflected in financial reports.

### Scenario 5: Tracking Team Submission Progress
As Group Finance lead, you need to ensure all entities submit on time.
1. Open **Data Entry Progress**.
2. See a matrix: entities as rows, months as columns, submission status color-coded.
3. Identify entities that haven't submitted yet (red/blank cells).
4. Follow up with responsible finance users in those entities.
5. Check the Home Dashboard for the overall progress percentage and upcoming deadlines.

---

## Best Practices for Financial Reporting

### Data Entry
- **Enter data monthly, not quarterly** — submitting monthly actuals promptly keeps forecasts accurate and leadership informed.
- **Use the Excel paste feature** (Monthly Reporting) — prepare your data in Excel first, then use Ctrl+V to paste into the grid. The system shows a confirmation dialog with matched data. This is faster and reduces manual entry errors.
- **Save after each statement type** — don't fill all four tabs without saving. If you navigate away, unsaved changes are lost.
- **Double-check before submitting** — once submitted, data is locked. Review all line items carefully.
- **Add variance notes** — when actual figures differ significantly from budget, add a note explaining why. This saves time during review.

### Deadlines and Submissions
- **Know your deadlines** — check the Home Dashboard at the start of each month. Deadlines are displayed with countdown timers.
- **Submit early, not on the deadline** — late submissions delay group-level reporting. Aim to submit 2-3 days before the deadline.
- **Monitor Data Entry Progress** — group finance leads should check this daily during reporting windows to catch missing submissions.

### Annual Planning
- **Start with last year's actuals** — use the Y-1 Actual column as your baseline, then adjust for known changes.
- **Be realistic with forecasts** — overoptimistic budgets lead to negative variances every month. Base your plan on achievable targets.
- **Document assumptions** — when building Y+1 to Y+3 plans, keep notes about key assumptions (growth rates, new hires, capital investments).

### CORE Allocation
- **Review allocations annually** — as the business grows and entities change, CORE percentages should be updated.
- **Ensure totals equal 100%** — the system enforces this. If you're adjusting one entity, remember to reduce another.

---

## Key Concepts

### Financial Statement Types

| Code | Name | What It Shows |
|------|------|---------------|
| **P&L** | Profit & Loss | Revenue, expenses, and net income |
| **CF** | Cash Flow | Cash inflows, outflows, and net cash position |
| **BS** | Balance Sheet | Assets, liabilities, and equity at a point in time |
| **WC** | Working Capital | Short-term assets minus short-term liabilities |

### Data Types (Column Types)

| Type | Meaning |
|------|---------|
| **Budget** | Approved budget figure for the period |
| **Actual** | Real recorded figure |
| **Estimation** | Estimated figure (used before actuals are available) |
| **Forecast** | Updated forward-looking forecast |

### Submission Workflow

| Step | What Happens |
|------|-------------|
| **Draft** | Data is entered and saved but not yet submitted; can still be edited |
| **Submitted** | Data is locked and visible to group finance; no further edits allowed |

To correct submitted data, an Admin or Group Finance user can **Withdraw** the submission, which returns it to **Draft** status so corrections can be made and the data resubmitted.

### Entities

Entities represent the individual companies and cost centers within the Sharp Group. Each entity submits its own financial data. CORE entities represent central overhead functions whose costs are allocated to operating entities.

---

## Languages

Matrix FM has a language toggle (globe icon) in the sidebar footer with **English** and **Russian** options. The built-in **Documentation** section is fully bilingual (EN/RU). The rest of the app interface is primarily in English; full i18n is being expanded progressively.

---

## Frequently Asked Questions

### General

**Q: What is Matrix Financial Management?**
A: It is the Sharp Matrix app for group financial reporting, budgeting, annual planning, and analytics. Finance teams and entity managers use it to submit and track financial data.

**Q: Who can see my financial data?**
A: Entity finance users see their own entity's data. Country managers see data for their country. Group finance and admins can see all entities.

**Q: Is my data saved automatically?**
A: No. You must click Save to save your work. Save frequently to avoid losing changes.

### Monthly Reporting

**Q: I submitted data but found an error. Can I edit it?**
A: Once submitted, data is locked. Contact group finance or an admin to withdraw the submission so you can make corrections.

**Q: What is the difference between Budget, Actual, and Estimation?**
A: Budget is the approved plan, Actual is the real figure, and Estimation is a projected figure used before actuals are finalized.

**Q: Can I paste data from Excel?**
A: Yes, in Monthly Reporting. Copy the data in Excel (including headers) and press Ctrl+V when the financial grid is active. The system shows a confirmation dialog with matched items before applying. You need to allow clipboard permissions in your browser.

**Q: I pasted data but nothing appeared.**
A: Check that your clipboard is not empty, the column headers match the expected format, and line item names match those in the system. If you see "No matching line items found," the pasted data format may not align. Also ensure you have clipboard permissions enabled in your browser.

### Annual Planning

**Q: Why are some columns read-only?**
A: Y-1 Actual and Y Budget columns are historical/approved figures and cannot be edited. Only future year plans (Y+1, Y+2, Y+3) are editable.

**Q: How do I plan for multiple years?**
A: Enter figures in the Y+1, Y+2, and Y+3 columns for each line item in the Annual Planning view.

### CORE Allocation

**Q: What is CORE allocation?**
A: CORE allocation distributes central overhead costs (like HQ, IT, shared services) across operating entities based on agreed percentages.

**Q: The allocation percentages don't add up to 100%.**
A: Allocation percentages across all entities for a given year must total 100%. Adjust the percentages and save again.

### Deadlines and Submissions

**Q: How do I know when my submission is due?**
A: Check the Home Dashboard for upcoming deadlines, or ask your finance lead for the reporting calendar.

**Q: What happens if I miss a deadline?**
A: The submission deadline is tracked in the system. Late submissions are flagged for group finance visibility. Submit as soon as possible.

---

## Troubleshooting

### Login and Access

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot log in** | Wrong credentials or no account | Check email/password. Contact Admin if you don't have an account. |
| **"Access Denied" on a page** | Your role doesn't have permission | Contact your Admin to check your role and permissions. |
| **Session expired unexpectedly** | Your login session timed out | Log in again. This is normal after periods of inactivity. |

### Data Entry

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot edit financial data** | Month already submitted or you lack write permission | Check if the month is submitted (locked). If you need to edit, ask finance to withdraw. |
| **Save fails with an error** | Permission issue or server error | Verify you have write access. If the error persists, note the message and contact support. |
| **Paste from Excel doesn't work** | Mismatched headers or empty clipboard | Verify column headers match. Copy the data again and try pasting. |
| **Data not appearing after save** | Page needs to be refreshed | Refresh the page (press F5 or click the refresh button in your browser). |

### Reports and Exports

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Export fails** | Large dataset or server timeout | Try a smaller date range or fewer entities. If it persists, contact support. |
| **Analytics charts show no data** | No submissions for the selected period | Verify that financial data has been submitted for the entity and period you selected. |

### General

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Page loads slowly** | Large dataset | Wait a moment and refresh. Try narrowing your filters. |
| **Audit log is empty** | No activity in the selected date range | Broaden the date filter. |
| **Notifications not appearing** | Browser or app issue | Refresh the page. |

---

## Known Issues and Workarounds

| Issue | Workaround | Status |
|-------|-----------|--------|
| Full UI translation to Russian is not yet complete for all screens | Use the Documentation section (fully bilingual) for reference. Most financial terms are standard. | In progress |
| Some pages may be visible even without full access | Admin should configure role permissions in Settings to control access properly. | By design |

---

## When to Escalate — Incident Reporting

If you cannot resolve the issue using the troubleshooting steps above, submit an incident to the 2nd Line Support team.

Report the issue using the standard incident template — see [How to Report an Incident](incident-reporting.md). Mention **Matrix Financial Management** as the app name and include the **entity name** and **reporting period** if relevant.

---

## Quick Reference Card

| Task | Where to Go |
|------|-------------|
| View dashboard and deadlines | Sidebar → Home |
| Enter monthly financial data | Sidebar → Monthly Reporting |
| Submit annual actuals | Sidebar → Annual Reporting |
| Create multi-year plans | Sidebar → Annual Planning |
| View analytics and comparisons | Sidebar → Analytics (page title: "Analytics & Reports") |
| Manage CORE cost allocation | Sidebar → CORE Allocation |
| Track submission progress | Sidebar → Data Entry Progress |
| View change history | Sidebar → Audit Log |
| Read help documentation | Sidebar → Documentation |
| Configure settings (admin) | Sidebar → Settings |
| Switch language | Sidebar footer → Globe icon |
| Switch theme (light/dark) | Sidebar footer → Theme toggle |
| Return to Agency Hub | Sidebar footer → Back to Agency Hub |
