# Development Log

## 2025-06-08
- Committed the Excel file used for prototyping (`Main AutoBudget File (mocked).xlsx`) to the repo despite `.gitignore`, for transparency and reproducibility.
- Created and committed `CHANGELOG.md` and `devlog.md` to track development milestones and ongoing work.


## 2025-06-07
- First commit pushed to main branch.
- Core functionality implemented with:
  - `loader.py` for Excel ingestion.
  - `viz.py` for plotting monthly category trends.
  - `config_loader.py` for tab/category setup via JSON config.
  - Streamlit interface with tabbed views, category checkboxes.
- Improved UX:
  - Category selection displayed at the bottom of each tab.
  - "Sum of Categories" curve added, with thicker line.
  - "Select All" / "Unselect All" functionality added.
  - Checkbox section condensed and aligned to the left.
- Repo structured for maintainability:
  - `autobudget/` for business logic
  - `tests/` for unit testing
  - `data/` for Excel file input (git-ignored)
  - `config/` for tab configurations

> Paired programming with GPT-4.1. Initial development took about 2 hours including iterations and refinement. Working PoC is live.
