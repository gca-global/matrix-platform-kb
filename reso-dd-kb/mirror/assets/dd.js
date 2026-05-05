    document.addEventListener('DOMContentLoaded', function() {
      // ── Heading anchor links ──────────────────────────────────
      // Auto-generate id attributes and insert a link icon on every
      // h1, h2, h3, h4 inside the main content area. Clicking the
      // icon copies the permalink to the clipboard.
      var contentArea = document.querySelector('.dd-content') || document.querySelector('main') || document.body;
      var headings = contentArea.querySelectorAll('h1, h2, h3, h4');
      var slugCounts = {};
      headings.forEach(function(h) {
        // Skip headings inside nav, header, cards, or sidebar
        if (h.closest('.site-header, .dd-sidebar, .dd-resource-card, .dd-nav-resource')) return;
        var text = h.textContent.trim();
        var slug = text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
        if (!slug) return;
        if (slugCounts[slug]) { slugCounts[slug]++; slug += '-' + slugCounts[slug]; }
        else { slugCounts[slug] = 1; }
        if (!h.id) h.id = slug;
        var anchor = document.createElement('a');
        anchor.className = 'dd-heading-anchor';
        anchor.href = '#' + h.id;
        anchor.innerHTML = '#';
        anchor.title = 'Copy link';
        anchor.addEventListener('click', function(e) {
          e.preventDefault();
          var url = window.location.origin + window.location.pathname + '#' + h.id;
          navigator.clipboard.writeText(url).then(function() {
            history.replaceState(null, '', '#' + h.id);
            anchor.innerHTML = '\u2713';
            setTimeout(function() { anchor.innerHTML = '#'; }, 1200);
          });
        });
        h.appendChild(anchor);
      });

      // ── Code block copy buttons ───────────────────────────────
      // Wrap every <pre> in a .dd-code-wrapper and add a copy button.
      var pres = document.querySelectorAll('pre');
      pres.forEach(function(pre) {
        if (pre.parentElement.classList.contains('dd-code-wrapper')) return;
        var wrapper = document.createElement('div');
        wrapper.className = 'dd-code-wrapper';
        pre.parentElement.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        var btn = document.createElement('button');
        btn.className = 'dd-code-copy';
        btn.textContent = 'Copy';
        btn.type = 'button';
        btn.addEventListener('click', function() {
          var code = pre.querySelector('code') || pre;
          navigator.clipboard.writeText(code.textContent).then(function() {
            btn.textContent = 'Copied!';
            btn.classList.add('copied');
            setTimeout(function() { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1200);
          });
        });
        wrapper.appendChild(btn);
      });

      var currentVersion = document.body.dataset.version;
      var activeFilter = currentVersion;
      var pfUI = null;
      var searchEl = document.getElementById('search');
      var modalEl = document.getElementById('searchModal');
      var countEl = null;
      var filtersEl = null;
      var ddCustomInput = null;

      var observer = null;

      function initPagefind() {
        pfUI = new PagefindUI({
          element: '#search', showSubResults: false, showImages: false, resetStyles: false,
          processResult: function(result) {
            var parts = [];
            if (result.meta && result.meta.description) parts.push(result.meta.description);
            if (result.meta && result.meta.date) parts.push(result.meta.date);
            var line1 = parts.join(' &middot; ');
            var def = (result.meta && result.meta.definition) ? result.meta.definition : '';
            result.excerpt = (line1 && def) ? line1 + '<br>' + def : (line1 || def || result.excerpt);
            return result;
          }
        });

        // Inject filter pills before the drawer
        var form = searchEl.querySelector('.pagefind-ui__form');
        if (form) {
          var tpl = document.getElementById('searchFiltersTemplate');
          var clone = tpl.content.cloneNode(true);
          var drawer = form.querySelector('.pagefind-ui__drawer');
          if (drawer) form.insertBefore(clone, drawer);
          else form.appendChild(clone);
          filtersEl = form.querySelector('.dd-search-filters');
          countEl = form.querySelector('.dd-search-count');

          if (filtersEl) {
            filtersEl.querySelectorAll('.dd-search-filter-pill').forEach(function(b) {
              b.classList.toggle('active', b.dataset.version === activeFilter);
            });
            filtersEl.addEventListener('click', function(e) {
              var btn = e.target.closest('.dd-search-filter-pill');
              if (!btn) return;
              filtersEl.querySelectorAll('.dd-search-filter-pill').forEach(function(b) { b.classList.remove('active'); });
              btn.classList.add('active');
              activeFilter = btn.dataset.version;
              applyFilter(activeFilter);
              var welcomeText = document.getElementById('ddSearchWelcomeText');
              if (welcomeText) {
                welcomeText.textContent = activeFilter
                  ? 'Search across Data Dictionary ' + activeFilter + ' resources, fields and lookup values.'
                  : 'Search across all Data Dictionary resources, fields and lookup values.';
              }
            });
          }
        }

        // Custom input overlay: user types here, we normalize and proxy to Pagefind
        var pfInput = searchEl.querySelector('.pagefind-ui__search-input');
        if (pfInput) {
          pfInput.style.position = 'absolute';
          pfInput.style.opacity = '0';
          pfInput.style.pointerEvents = 'none';
          var customInput = document.createElement('input');
          customInput.type = 'text';
          customInput.placeholder = 'Search...';
          customInput.className = 'dd-search-input';
          pfInput.parentNode.insertBefore(customInput, pfInput);
          ddCustomInput = customInput;

          function clearSearch() {
            customInput.value = '';
            var welcomeEl = document.getElementById('ddSearchWelcome');
            var emptyEl = document.getElementById('ddSearchEmpty');
            var drawerEl = searchEl.querySelector('.pagefind-ui__drawer');
            if (welcomeEl) welcomeEl.classList.add('visible');
            if (emptyEl) emptyEl.classList.remove('visible');
            if (drawerEl) drawerEl.style.display = 'none';
            if (countEl) countEl.textContent = '';
            pfUI.triggerSearch('');
          }

          var normDebounce = null;
          customInput.addEventListener('input', function() {
            var raw = customInput.value;
            var hasQuery = raw.trim().length > 0;
            if (!hasQuery) { clearSearch(); return; }
            var welcomeEl = document.getElementById('ddSearchWelcome');
            var emptyEl = document.getElementById('ddSearchEmpty');
            var drawerEl = searchEl.querySelector('.pagefind-ui__drawer');
            if (welcomeEl) welcomeEl.classList.remove('visible');
            if (emptyEl) emptyEl.classList.remove('visible');
            if (drawerEl) drawerEl.style.display = '';
            clearTimeout(normDebounce);
            normDebounce = setTimeout(function() {
              var normalized = customInput.value.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
              if (normalized) pfUI.triggerSearch(normalized);
            }, 150);
          });

          // Sync Pagefind's Clear button with our custom input
          var clearBtn = searchEl.querySelector('.pagefind-ui__search-clear');
          if (clearBtn) {
            clearBtn.addEventListener('click', function() { clearSearch(); customInput.focus(); });
          }
        }

        // Attach infinite scroll on the drawer
        var drawerEl = searchEl.querySelector('.pagefind-ui__drawer');
        if (drawerEl) {
          drawerEl.addEventListener('scroll', function() {
            if (drawerEl.scrollTop + drawerEl.clientHeight >= drawerEl.scrollHeight - 300) {
              var btn = searchEl.querySelector('.pagefind-ui__button');
              if (btn) btn.click();
            }
          });
        }

        // Observe for version badges, result count, and auto-load
        var processing = false;
        observer = new MutationObserver(function() {
          if (processing) return;
          processing = true;
          requestAnimationFrame(function() {
            searchEl.querySelectorAll('.pagefind-ui__result-link:not([data-badge])').forEach(function(link) {
              link.setAttribute('data-badge', '1');
              var url = link.getAttribute('href') || '';
              var m = url.match(/\/DD(\d+\.\d+)\//);
              if (m) {
                var badge = document.createElement('span');
                badge.className = 'dd-result-version';
                badge.textContent = 'DD ' + m[1];
                link.appendChild(badge);
              }
            });
            // Re-sort: exact title matches go first
            var query = ddCustomInput ? ddCustomInput.value.replace(/[^a-zA-Z0-9]/g, '').toLowerCase() : '';
            if (query) {
              var resultsList = searchEl.querySelector('.pagefind-ui__results');
              if (resultsList) {
                var items = Array.from(resultsList.querySelectorAll('.pagefind-ui__result'));
                var needsSort = items.some(function(item) {
                  var link = item.querySelector('.pagefind-ui__result-link');
                  if (!link) return false;
                  var title = (link.textContent || '').replace(/DD\s*\d+\.\d+$/, '').trim();
                  return title.replace(/[^a-zA-Z0-9]/g, '').toLowerCase() === query;
                });
                if (needsSort) {
                  observer.disconnect();
                  items.forEach(function(item) {
                    var link = item.querySelector('.pagefind-ui__result-link');
                    if (!link) return;
                    var title = (link.textContent || '').replace(/DD\s*\d+\.\d+$/, '').trim();
                    var normTitle = title.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
                    if (normTitle === query) {
                      resultsList.insertBefore(item, resultsList.firstChild);
                    }
                  });
                  observer.observe(searchEl, { childList: true, subtree: true });
                }
              }
            }
            var hasQuery = ddCustomInput && ddCustomInput.value.trim().length > 0;
            var msg = searchEl.querySelector('.pagefind-ui__message');
            var emptyEl = document.getElementById('ddSearchEmpty');
            if (msg && countEl) {
              if (!hasQuery) {
                countEl.textContent = '';
                if (emptyEl) emptyEl.classList.remove('visible');
              } else {
                var txt = msg.textContent || '';
                var cm = txt.match(/(\d+)\s+result/);
                var count = cm ? parseInt(cm[1], 10) : -1;
                var newCount = count > 0 ? count + ' results' : '';
                if (countEl.textContent !== newCount) countEl.textContent = newCount;
                if (emptyEl) emptyEl.classList.toggle('visible', count === 0);
              }
            }
            var dEl = searchEl.querySelector('.pagefind-ui__drawer');
            var loadBtn = searchEl.querySelector('.pagefind-ui__button');
            if (dEl && loadBtn && dEl.scrollHeight <= dEl.clientHeight) {
              setTimeout(function() { loadBtn.click(); }, 50);
            }
            processing = false;
          });
        });
        observer.observe(searchEl, { childList: true, subtree: true });

        // Apply initial filter and set welcome text
        if (activeFilter) {
          pfUI.triggerFilters({ 'dd-version': [activeFilter] });
          var welcomeText = document.getElementById('ddSearchWelcomeText');
          if (welcomeText) {
            welcomeText.textContent = 'Search across Data Dictionary ' + activeFilter + ' resources, fields and lookup values.';
          }
        }
      }

      function applyFilter(version) {
        if (!pfUI) return;
        if (version) {
          pfUI.triggerFilters({ 'dd-version': [version] });
        } else {
          pfUI.triggerFilters({});
        }
        // Re-trigger current search term (normalized) so results update
        var raw = ddCustomInput ? ddCustomInput.value : '';
        if (raw) {
          pfUI.triggerSearch(raw.replace(/[^a-zA-Z0-9]/g, '').toLowerCase());
        }
      }

      // Load Pagefind
      var s = document.createElement('script');
      s.src = '/pagefind/pagefind-ui.js';
      s.onload = function() { if (typeof PagefindUI !== 'undefined') initPagefind(); };
      document.head.appendChild(s);

      // Header hamburger
      document.getElementById('menuToggle').addEventListener('click', function() {
        document.getElementById('headerNav').classList.toggle('open');
      });

      // Search modal
      var overlay = document.getElementById('searchOverlay');
      function openSearch() {
        overlay.classList.add('active');
        document.body.classList.add('search-open');
        setTimeout(function() {
          if (ddCustomInput) {
            ddCustomInput.focus();
            var hasQuery = ddCustomInput.value.trim().length > 0;
            var welcomeEl = document.getElementById('ddSearchWelcome');
            var drawerEl = searchEl.querySelector('.pagefind-ui__drawer');
            if (welcomeEl) welcomeEl.classList.toggle('visible', !hasQuery);
            if (drawerEl) drawerEl.style.display = hasQuery ? '' : 'none';
            if (!hasQuery && countEl) countEl.textContent = '';
          }
        }, 100);
      }
      function closeSearch() {
        overlay.classList.remove('active');
        document.body.classList.remove('search-open');
      }
      // Sidebar accordion — one open at a time
      document.querySelectorAll('.dd-sidebar-section-title').forEach(function(title) {
        title.addEventListener('click', function() {
          var section = title.parentElement;
          var wasExpanded = section.classList.contains('expanded');
          document.querySelectorAll('.dd-sidebar-section').forEach(function(s) {
            s.classList.remove('expanded');
          });
          if (!wasExpanded) section.classList.add('expanded');
        });
      });

      // Scroll the active sidebar item into view so the selected
      // resource/lookup stays visible instead of jumping to top (#4).
      // Only on desktop — mobile sidebar is a slide-over, not visible on load.
      if (window.innerWidth >= 768) {
        var activeLink = document.querySelector('.dd-nav-resource-link.active');
        if (activeLink) {
          activeLink.scrollIntoView({ block: 'center', behavior: 'instant' });
        }
      }

      document.getElementById('searchTrigger').addEventListener('click', openSearch);
      var sidebarSearchEl = document.getElementById('sidebarSearch');
      if (sidebarSearchEl) sidebarSearchEl.addEventListener('click', openSearch);
      overlay.addEventListener('click', function(e) { if (e.target === overlay) closeSearch(); });
      document.addEventListener('keydown', function(e) {
        if (e.key === '/' && !e.ctrlKey && !e.metaKey && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
          e.preventDefault();
          openSearch();
        }
        if (e.key === 'Escape') closeSearch();
      });

      // Sidebar toggle (mobile)
      var sidebar = document.getElementById('ddSidebar');
      var sidebarOverlay = document.getElementById('ddSidebarOverlay');
      function toggleSidebar() { sidebar.classList.toggle('open'); sidebarOverlay.classList.toggle('active'); }
      document.getElementById('ddSidebarToggle').addEventListener('click', toggleSidebar);
      sidebarOverlay.addEventListener('click', toggleSidebar);

      // Expand active resource in sidebar
      document.querySelectorAll('.dd-nav-resource-link.active').forEach(function(link) {
        link.closest('.dd-nav-resource').classList.add('expanded');
      });

      // Toggle resource groups
      document.querySelectorAll('.dd-nav-resource-link').forEach(function(link) {
        link.addEventListener('click', function(e) {
          var li = link.closest('.dd-nav-resource');
          if (li.querySelector('.dd-nav-groups')) {
            li.classList.toggle('expanded');
          }
        });
      });

      // Toggle subgroup visibility in sidebar
      document.querySelectorAll('.dd-nav-group.has-children > .dd-nav-group-link').forEach(function(link) {
        link.addEventListener('click', function(e) {
          var li = link.closest('.dd-nav-group');
          if (li.classList.contains('expanded')) {
            e.preventDefault();
            li.classList.remove('expanded');
          } else {
            li.classList.add('expanded');
          }
        });
      });

      // Theme toggle
      document.getElementById('themeToggle').addEventListener('click', function() {
        var isDark = document.documentElement.classList.toggle('dark');
        localStorage.setItem('dd-theme', isDark ? 'dark' : 'light');
      });

      // Copy-to-clipboard buttons
      document.querySelectorAll('.dd-copy-btn').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
          e.preventDefault();
          var text = btn.getAttribute('data-copy');
          if (!text) return;
          navigator.clipboard.writeText(text).then(function() {
            var svg = btn.querySelector('svg');
            var origHTML = svg.outerHTML;
            var w = svg.getAttribute('width') || '18';
            var h = svg.getAttribute('height') || '18';
            svg.outerHTML = '<svg viewBox="0 0 24 24" width="' + w + '" height="' + h + '" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>';
            btn.classList.add('copied');
            setTimeout(function() {
              btn.innerHTML = origHTML;
              btn.classList.remove('copied');
            }, 1500);
          });
        });
      });

      // Table filter — filters rows by text content
      document.querySelectorAll('.dd-table-filter input').forEach(function(input) {
        var wrapper = input.closest('.dd-resource-sticky') || input.parentElement;
        var tableWrapper = wrapper.nextElementSibling;
        // Skip the sticky column headers div (contains a header-only table)
        while (tableWrapper && (tableWrapper.classList.contains('dd-sticky-col-headers') || !tableWrapper.querySelector('table'))) {
          tableWrapper = tableWrapper.nextElementSibling;
        }
        if (!tableWrapper) return;
        var countEl = input.parentElement.querySelector('.dd-table-filter-count');
        var rows = Array.from(tableWrapper.querySelectorAll('table tbody tr'));
        var totalCount = rows.length;

        function applyFilter(query) {
          var allRows = Array.from(tableWrapper.querySelectorAll('table tbody tr'));
          var visible = 0;
          allRows.forEach(function(row) {
            var text = row.textContent.toLowerCase();
            var show = !query || text.indexOf(query) !== -1;
            row.style.display = show ? '' : 'none';
            if (show) visible++;
          });
          // Hide group headings + their tables when no rows match
          var headings = Array.from(tableWrapper.querySelectorAll('.dd-group-heading'));
          headings.forEach(function(h) {
            var table = h.nextElementSibling;
            while (table && table.tagName !== 'TABLE') table = table.nextElementSibling;
            if (!table) return;
            var visibleRows = Array.from(table.querySelectorAll('tbody tr')).filter(function(r) { return r.style.display !== 'none'; });
            var empty = visibleRows.length === 0 && !!query;
            h.style.display = empty ? 'none' : '';
            table.style.display = empty ? 'none' : '';
          });
          // Repaint zebra stripes on visible rows only
          var visibleIdx = 0;
          allRows.forEach(function(row) {
            if (row.style.display !== 'none') {
              row.style.background = (visibleIdx % 2 === 1) ? 'rgba(0, 0, 0, 0.04)' : '';
              visibleIdx++;
            } else {
              row.style.background = '';
            }
          });
          if (countEl) {
            countEl.textContent = query ? visible + ' of ' + allRows.length : '';
          }
        }
        // Expose applyFilter so the group toggle can re-apply after restoring HTML
        tableWrapper._applyFilter = applyFilter;
        input.addEventListener('input', function() {
          applyFilter(input.value.toLowerCase().trim());
        });
      });

      // Collapsible panels
      document.querySelectorAll('.dd-collapsible-toggle').forEach(function(btn) {
        btn.addEventListener('click', function() {
          btn.parentElement.classList.toggle('open');
        });
      });

      // Definition callout toggle — only show button when text is actually clamped
      document.querySelectorAll('.dd-definition-callout').forEach(function(callout) {
        var textEl = callout.querySelector('.dd-callout-text');
        var btn = callout.querySelector('.dd-callout-toggle');
        if (!textEl || !btn) return;
        function checkOverflow() {
          if (window.innerWidth > 768) { callout.classList.remove('needs-toggle'); return; }
          callout.classList.remove('expanded');
          btn.textContent = '... more';
          var isOverflowing = textEl.scrollHeight > textEl.clientHeight + 1;
          callout.classList.toggle('needs-toggle', isOverflowing);
        }
        btn.addEventListener('click', function() {
          var expanded = callout.classList.toggle('expanded');
          btn.textContent = expanded ? 'less' : '... more';
        });
        checkOverflow();
        window.addEventListener('resize', checkOverflow);
      });

      // Pill-based sort helper — returns a reset function
      function initSortPills(container, onSort) {
        if (!container) return function() {};
        var pills = Array.from(container.querySelectorAll('.dd-sort-pill'));
        var currentField = pills.length ? pills[0].dataset.sort : '';
        var ascending = true;
        pills.forEach(function(pill) {
          pill.addEventListener('click', function() {
            var sf = pill.dataset.sort;
            if (sf === currentField) {
              ascending = !ascending;
            } else {
              currentField = sf;
              ascending = true;
              pills.forEach(function(p) { p.classList.remove('active'); });
              pill.classList.add('active');
            }
            var arrow = pill.querySelector('.dd-sort-arrow');
            pills.forEach(function(p) {
              var a = p.querySelector('.dd-sort-arrow');
              if (a) a.innerHTML = '&#9650;';
            });
            if (arrow) arrow.innerHTML = ascending ? '&#9650;' : '&#9660;';
            onSort(currentField, ascending);
          });
        });
        return function resetPills() {
          currentField = pills.length ? pills[0].dataset.sort : '';
          ascending = true;
          pills.forEach(function(p) {
            p.classList.remove('active');
            var a = p.querySelector('.dd-sort-arrow');
            if (a) a.innerHTML = '&#9650;';
          });
          if (pills.length) pills[0].classList.add('active');
        };
      }

      // Sort + filter controls for version landing (resource grid)
      var resGrid = document.getElementById('ddResourceGrid');
      if (resGrid) {
        var resToolbar = resGrid.previousElementSibling;
        initSortPills(resToolbar, function(field, asc) {
          var cards = Array.from(resGrid.querySelectorAll('.dd-resource-card'));
          cards.sort(function(a, b) {
            if (field === 'name') {
              return asc ? a.dataset.name.localeCompare(b.dataset.name) : b.dataset.name.localeCompare(a.dataset.name);
            } else if (field === 'fields') {
              var fa = parseInt(a.dataset.fields), fb = parseInt(b.dataset.fields);
              return asc ? fb - fa : fa - fb;
            }
            return 0;
          });
          cards.forEach(function(c) { resGrid.appendChild(c); });
        });
        var resFilterInput = resToolbar.querySelector('.dd-table-filter input');
        var resFilterCount = resToolbar.querySelector('.dd-table-filter-count');
        if (resFilterInput) {
          var allCards = Array.from(resGrid.querySelectorAll('.dd-resource-card'));
          resFilterInput.addEventListener('input', function() {
            var q = resFilterInput.value.toLowerCase().trim();
            var visible = 0;
            allCards.forEach(function(card) {
              var name = (card.dataset.name || '').toLowerCase();
              var desc = (card.querySelector('.dd-resource-desc') || {}).textContent || '';
              var match = !q || name.indexOf(q) !== -1 || desc.toLowerCase().indexOf(q) !== -1;
              card.style.display = match ? '' : 'none';
              if (match) visible++;
            });
            resFilterCount.textContent = q ? visible + ' of ' + allCards.length : '';
          });
        }
      }

      // Sort controls for resource pages
      var wrapper = document.querySelector('.dd-fields-table-wrapper');
      if (wrapper) {
        var groupToggle = document.getElementById('ddGroupToggle');
        var originalHTML = wrapper.innerHTML;
        var groupsVisible = !!groupToggle;

        // Calculate sticky offset from resource sticky header
        var stickyColHeaders = document.querySelector('.dd-sticky-col-headers');
        function updateStickyOffset() {
          var stickyHeader = document.querySelector('.dd-resource-sticky');
          if (stickyHeader) {
            // After collapse, offsetHeight may not reflect the final
            // animated size. Use scrollHeight when collapsed to get
            // the true rendered height post-transition.
            var height = stickyHeader.offsetHeight;
            var top = height + 64;
            if (stickyColHeaders) stickyColHeaders.style.setProperty('--sticky-thead-top', top + 'px');
            wrapper.style.setProperty('--sticky-thead-top', top + 'px');
          }
        }
        updateStickyOffset();
        window.addEventListener('resize', updateStickyOffset);

        function flatSort(field, ascending) {
          var headings = wrapper.querySelectorAll('.dd-group-heading');
          var tables = wrapper.querySelectorAll('.dd-fields-table');
          headings.forEach(function(h) { h.style.display = 'none'; });
          var allRows = [];
          tables.forEach(function(t) {
            Array.from(t.querySelectorAll('tbody tr')).forEach(function(r) { allRows.push(r); });
          });
          allRows.sort(function(a, b) {
            var va, vb;
            if (field === 'name') {
              va = a.dataset.name || ''; vb = b.dataset.name || '';
              return ascending ? va.localeCompare(vb) : vb.localeCompare(va);
            } else if (field === 'usage') {
              va = parseFloat(a.dataset.usage) || -1; vb = parseFloat(b.dataset.usage) || -1;
              return ascending ? vb - va : va - vb;
            } else if (field === 'added') {
              va = a.dataset.added || ''; vb = b.dataset.added || '';
              return ascending ? va.localeCompare(vb) : vb.localeCompare(va);
            } else if (field === 'type') {
              va = a.dataset.type || ''; vb = b.dataset.type || '';
              return ascending ? va.localeCompare(vb) : vb.localeCompare(va);
            } else if (field === 'revised') {
              va = a.dataset.revised || ''; vb = b.dataset.revised || '';
              return ascending ? vb.localeCompare(va) : va.localeCompare(vb);
            }
            return 0;
          });
          if (tables.length > 0) {
            var mainTbody = tables[0].querySelector('tbody');
            allRows.forEach(function(r) { mainTbody.appendChild(r); });
            for (var i = 1; i < tables.length; i++) tables[i].style.display = 'none';
          }
          wrapper.classList.remove('dd-grouped');
        }

        // Sidebar group tree for the active resource
        var sidebarGroups = document.querySelector('.dd-nav-resource.expanded > .dd-nav-groups');

        var fieldSortContainer = document.querySelector('.dd-sort-controls');
        var mobileSortAscending = true;
        var mobileSortSelect = fieldSortContainer ? fieldSortContainer.querySelector('.dd-sort-select') : null;
        var mobileSortDirBtn = fieldSortContainer ? fieldSortContainer.querySelector('.dd-sort-dir-btn') : null;

        function reapplyFilter() {
          var filterInput = document.querySelector('.dd-table-filter input');
          if (filterInput && filterInput.value.trim()) {
            filterInput.dispatchEvent(new Event('input'));
          }
        }

        function doSort(field, ascending) {
          if (groupToggle && groupsVisible) {
            groupsVisible = false;
            groupToggle.classList.remove('active');
          }
          flatSort(field, ascending);
          reapplyFilter();
          updateStickyOffset();
          if (sidebarGroups) sidebarGroups.style.display = 'none';
        }

        var resetPills = initSortPills(fieldSortContainer, function(field, ascending) {
          doSort(field, ascending);
          // Sync mobile select
          if (mobileSortSelect) mobileSortSelect.value = field;
          mobileSortAscending = ascending;
          if (mobileSortDirBtn) mobileSortDirBtn.innerHTML = ascending ? '&#9650;' : '&#9660;';
        });

        // Mobile sort dropdown
        if (mobileSortSelect) {
          mobileSortSelect.addEventListener('change', function() {
            mobileSortAscending = true;
            if (mobileSortDirBtn) mobileSortDirBtn.innerHTML = '&#9650;';
            doSort(mobileSortSelect.value, true);
            // Sync desktop pills
            var pills = fieldSortContainer.querySelectorAll('.dd-sort-pill');
            pills.forEach(function(p) { p.classList.remove('active'); var a = p.querySelector('.dd-sort-arrow'); if (a) a.innerHTML = '&#9650;'; });
            var matchPill = fieldSortContainer.querySelector('.dd-sort-pill[data-sort="' + mobileSortSelect.value + '"]');
            if (matchPill) matchPill.classList.add('active');
          });
        }
        if (mobileSortDirBtn) {
          mobileSortDirBtn.addEventListener('click', function() {
            mobileSortAscending = !mobileSortAscending;
            mobileSortDirBtn.innerHTML = mobileSortAscending ? '&#9650;' : '&#9660;';
            doSort(mobileSortSelect ? mobileSortSelect.value : 'name', mobileSortAscending);
          });
        }

        function resetMobileSort() {
          mobileSortAscending = true;
          if (mobileSortSelect) mobileSortSelect.value = 'name';
          if (mobileSortDirBtn) mobileSortDirBtn.innerHTML = '&#9650;';
        }

        if (groupToggle) {
          groupToggle.addEventListener('click', function() {
            if (groupsVisible) {
              groupsVisible = false;
              groupToggle.classList.remove('active');
              flatSort('name', true);
              reapplyFilter();
              resetPills();
              resetMobileSort();
              updateStickyOffset();
              if (sidebarGroups) sidebarGroups.style.display = 'none';
            } else {
              groupsVisible = true;
              groupToggle.classList.add('active');
              wrapper.classList.add('dd-grouped');
              wrapper.innerHTML = originalHTML;
              resetPills();
              resetMobileSort();
              updateStickyOffset();
              initScrollSpy();
              if (sidebarGroups) sidebarGroups.style.display = '';
              // Re-apply active filter after restoring groups
              var filterInput = document.querySelector('.dd-table-filter input');
              if (filterInput && filterInput.value.trim()) {
                filterInput.dispatchEvent(new Event('input'));
              }
            }
          });
        }
      }

      // Sort controls for xref/browse-by value pages
      var xrefSortContainer = document.querySelector('.dd-xref-sort');
      var xrefTable = document.querySelector('.dd-xref-table');
      if (xrefSortContainer && xrefTable) {
        var xrefMobileSortAsc = true;
        var xrefMobileSelect = xrefSortContainer.querySelector('.dd-sort-select');
        var xrefMobileDirBtn = xrefSortContainer.querySelector('.dd-sort-dir-btn');

        function xrefSort(field, ascending) {
          var tbody = xrefTable.querySelector('tbody');
          var rows = Array.from(tbody.querySelectorAll('tr'));
          rows.sort(function(a, b) {
            var va, vb;
            if (field === 'name') {
              va = a.dataset.name || ''; vb = b.dataset.name || '';
              return ascending ? va.localeCompare(vb) : vb.localeCompare(va);
            } else if (field === 'resource') {
              va = a.dataset.resource || ''; vb = b.dataset.resource || '';
              return ascending ? va.localeCompare(vb) : vb.localeCompare(va);
            } else if (field === 'type') {
              va = a.dataset.type || ''; vb = b.dataset.type || '';
              return ascending ? va.localeCompare(vb) : vb.localeCompare(va);
            } else if (field === 'usage') {
              va = parseFloat(a.dataset.usage) || -1; vb = parseFloat(b.dataset.usage) || -1;
              return ascending ? vb - va : va - vb;
            }
            return 0;
          });
          rows.forEach(function(r) { tbody.appendChild(r); });
        }

        initSortPills(xrefSortContainer, function(field, ascending) {
          xrefSort(field, ascending);
          if (xrefMobileSelect) xrefMobileSelect.value = field;
          xrefMobileSortAsc = ascending;
          if (xrefMobileDirBtn) xrefMobileDirBtn.innerHTML = ascending ? '&#9650;' : '&#9660;';
        });

        if (xrefMobileSelect) {
          xrefMobileSelect.addEventListener('change', function() {
            xrefMobileSortAsc = true;
            if (xrefMobileDirBtn) xrefMobileDirBtn.innerHTML = '&#9650;';
            xrefSort(xrefMobileSelect.value, true);
          });
        }
        if (xrefMobileDirBtn) {
          xrefMobileDirBtn.addEventListener('click', function() {
            xrefMobileSortAsc = !xrefMobileSortAsc;
            xrefMobileDirBtn.innerHTML = xrefMobileSortAsc ? '&#9650;' : '&#9660;';
            var field = xrefMobileSelect ? xrefMobileSelect.value : 'name';
            xrefSort(field, xrefMobileSortAsc);
          });
        }

        // Set sticky offset for xref column headers
        var xrefColHeaders = document.querySelector('.dd-xref-col-headers');
        if (xrefColHeaders) {
          var xrefSticky = document.querySelector('.dd-resource-sticky');
          if (xrefSticky) {
            var xrefTop = xrefSticky.offsetHeight + 64;
            xrefColHeaders.style.setProperty('--sticky-thead-top', xrefTop + 'px');
          }
          window.addEventListener('resize', function() {
            if (xrefSticky) {
              xrefColHeaders.style.setProperty('--sticky-thead-top', (xrefSticky.offsetHeight + 64) + 'px');
            }
          });
        }
      }

      // Progressive collapse: only on resource/lookup/xref field pages (not version landing).
      // Uses a fixed threshold (initial header height captured once) to avoid flickering
      // from the header height changing when collapsed.
      if (window.innerWidth < 768 && !document.getElementById('ddResourceGrid')) {
        var resourceSticky = document.querySelector('.dd-resource-sticky');
        if (resourceSticky) {
          var collapseThreshold = resourceSticky.offsetHeight;
          var isCollapsed = false;
          var onScroll = function() {
            var scrollY = window.scrollY || window.pageYOffset || 0;
            // Collapse when scrolled past the initial header. Uncollapse
            // only when scrolled back near the very top (hysteresis).
            if (!isCollapsed && scrollY > collapseThreshold) {
              isCollapsed = true;
              resourceSticky.classList.add('scrolled');
              updateStickyOffset();
            } else if (isCollapsed && scrollY < 20) {
              isCollapsed = false;
              resourceSticky.classList.remove('scrolled');
              updateStickyOffset();
            }
          };
          window.addEventListener('scroll', onScroll, { passive: true });
        }
      }

      // Scroll-spy: sync sidebar tree with visible group headings
      var groupLinks = document.querySelectorAll('.dd-nav-group-link');
      var activeGroupLink = null;
      var currentObserver = null;

      function initScrollSpy() {
        var groupHeadings = document.querySelectorAll('.dd-group-heading');
        if (groupHeadings.length === 0) return;
        var mobileGroupLabel = document.getElementById('ddMobileGroupLabel');

        if (currentObserver) currentObserver.disconnect();

        currentObserver = new IntersectionObserver(function(entries) {
          var topEntry = null;
          entries.forEach(function(entry) {
            if (entry.isIntersecting) {
              if (!topEntry || entry.boundingClientRect.top < topEntry.boundingClientRect.top) {
                topEntry = entry;
              }
            }
          });
          if (topEntry) activateGroupLink(topEntry.target.id, mobileGroupLabel);
        }, { rootMargin: '-80px 0px -60% 0px' });

        groupHeadings.forEach(function(h) { currentObserver.observe(h); });
      }

      function activateGroupLink(id, mobileGroupLabel) {
        if (activeGroupLink) activeGroupLink.classList.remove('active');
        var link = null;
        for (var i = 0; i < groupLinks.length; i++) {
          if (groupLinks[i].getAttribute('href') === '#' + id) {
            link = groupLinks[i];
            break;
          }
        }
        if (!link) return;
        activeGroupLink = link;
        link.classList.add('active');
        // Update mobile group indicator
        if (mobileGroupLabel) {
          mobileGroupLabel.textContent = link.textContent.trim();
        }
        // Expand this group and all ancestor group nodes
        var group = link.closest('.dd-nav-group');
        while (group) {
          group.classList.add('expanded');
          group = group.parentElement.closest('.dd-nav-group');
        }
        // Scroll sidebar to keep active link visible
        var sidebar = document.getElementById('ddSidebar');
        if (sidebar && link.offsetParent) {
          var linkRect = link.getBoundingClientRect();
          var sidebarRect = sidebar.getBoundingClientRect();
          if (linkRect.top < sidebarRect.top || linkRect.bottom > sidebarRect.bottom) {
            link.scrollIntoView({ block: 'center', behavior: 'smooth' });
          }
        }
      }

      initScrollSpy();
    });