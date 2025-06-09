# AutoBudgetViewer
AutoBudgetViewer - An interactive interface to monitor and visualize personal household income and expenses over time.  

### Devs: [Lior Gazit](https://github.com/LiorGazit), and GPT4.1  
*Hours spent in total on this project so far: `2.5 hours`  

## (This README is to be addressed later)

    My comments for things to have here:   
    1. The full documentation  
    2. Setting up the venv  
    3. Setting up the ability to run the streamlit command in powershell     
  



## AutoBudgetView – Codebase Structure  

AutoBudgetView/  
│  
├── CHANGELOG.md        # High-level release notes — top-level, visible to all contributors  
├── devlog.md           # Developer diary/log — top-level, close to where day-to-day dev happens  
├── app.py                       # Main Streamlit entry point  
├── requirements.txt             # Python dependencies  
├── config/  
│   └── tabs_config.json         # Tab/category config file  
├── data/  
│   └── Main AutoBudget File (mocked).xlsx  # (Git-ignored, but this is the input file location)  
├── autobudget/  
│   ├── \_\_init\_\_.py  
│   ├── loader.py                # Excel loading, validation, and parsing logic  
│   ├── config_loader.py         # Config file reader and validator  
│   ├── state.py                 # (Optional) Session state handling for Streamlit  
│   └── viz.py                   # Plotting and visualization functions  
├── tests/  
│   ├── test_loader.py  
│   ├── test_config_loader.py  
│   └── test_viz.py  
└── .gitignore  

Key Points

-   app.py: Streamlit UI, ties everything together.

-   autobudget/: Core logic for data I/O, validation, and plotting.

-   config/: Tab definitions (tabs_config.json), easily edited.

-    data/: Input Excel file(s)—won’t be versioned in git, just for local use.

-    tests/: Unit tests for core components (expand as the codebase matures).

-    requirements.txt: Includes streamlit, pandas, openpyxl, and other essentials.

-    state.py: For Streamlit session state, if we need it for advanced UI.