# Changelog

## [v0.1.0] - 2025-06-07
### Added
- Initial project structure with modular folder layout.
- Excel loader to read category vs. month data from the first sheet.
- Streamlit UI with multi-tab support based on `tabs_config.json`.
- Category selection via checkboxes, grouped per tab.
- Dynamic plotting of selected categories with line charts.
- "Sum of Categories" graph added to plots for chosen items.
- Layout improvements (e.g., checkbox positioning, minimized category list view).

## [Unreleased]
- `Main AutoBudget File (mocked).xlsx` committed once to the repo for public reference.
- `CHANGELOG.md` and `devlog.md` files initialized for structured development tracking.

### Added
- Smoothing feature with causal moving average on all plotted lines.
  - Users can input window size M (M ≥ 1) below each graph.
  - Graph titles update to reflect smoothing status.
