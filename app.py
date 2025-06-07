import streamlit as st
from autobudget.loader import load_budget_table, ExcelFormatError
from autobudget.config_loader import load_tab_config, ConfigFormatError
from autobudget.viz import plot_time_series

st.set_page_config(page_title="AutoBudgetView", layout="wide")
st.title("AutoBudgetView_v01")

DATA_PATH = "data/Main AutoBudget File.xlsx"
CONFIG_PATH = "config/tabs_config.json"

# --- Data Loading ---
try:
    df = load_budget_table(DATA_PATH)
    all_categories = df.index.tolist()
except Exception as e:
    st.error(str(e))
    st.stop()

# --- Config Loading ---
try:
    tab_config = load_tab_config(CONFIG_PATH, all_categories)
except Exception as e:
    st.error(str(e))
    st.stop()

st.success(f"Loaded {df.shape[0]} categories and {df.shape[1]} month columns.")
st.info("Tabs reflect your config. Try editing tabs_config.json and restart to see changes.")

# --- Tabs UI ---
tabs = list(tab_config.keys())
tab_objs = st.tabs(tabs)

for tab_name, tab_obj in zip(tabs, tab_objs):
    with tab_obj:
        st.markdown(f"### {tab_name}")

        # Columns: left for checkboxes, right for future charts or other content
        col_left, col_right = st.columns([1, 3], gap="large")

        # Use session state to store the checkboxes for each tab
        state_key = f"selected_{tab_name}"
        if state_key not in st.session_state:
            # Initialize with defaults from config
            st.session_state[state_key] = set(tab_config[tab_name])

        # Button handlers
        with col_left:
            select_all = st.button("Select All", key=f"select_all_{tab_name}")
            unselect_all = st.button("Unselect All", key=f"unselect_all_{tab_name}")

            if select_all:
                st.session_state[state_key] = set(all_categories)
            if unselect_all:
                st.session_state[state_key] = set()

            # Checkboxes, tight and compact
            selected = set()
            for cat in all_categories:
                is_checked = cat in st.session_state[state_key]
                # Each checkbox's value is based on the session state
                checked = st.checkbox(cat, value=is_checked, key=f"{tab_name}_{cat}")
                if checked:
                    selected.add(cat)
            # Update the session state for next rerun
            st.session_state[state_key] = selected

        with col_right:
            # Visualization
            plot_time_series(df, sorted(list(st.session_state[state_key])),
                            title=f"{tab_name} – Time Series")

            # Minimal, collapsed "Selected categories" below the chart
            with st.expander("Show selected categories", expanded=False):
                st.caption(
                    "For validation only: currently selected categories in this tab:"
                )
                st.write(
                    ", ".join(sorted(list(st.session_state[state_key]))) or "(none selected)"
                )

