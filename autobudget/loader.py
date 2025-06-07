import pandas as pd
import os

class ExcelFormatError(Exception):
    pass

def load_budget_table(filepath):
    """
    Loads and validates the budget table from the first sheet of the Excel file.
    - First column: category names (must be non-empty, unique)
    - First row: month headers in YYYY-MM format
    - All cells must be non-empty (raise if any are missing)
    Returns: DataFrame (index=category, columns=YYYY-MM strings, values=floats)
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    df = pd.read_excel(filepath, sheet_name=0, header=0, engine="openpyxl")
    # Basic structural check: at least two columns and two rows
    if df.shape[1] < 2 or df.shape[0] < 1:
        raise ExcelFormatError("The table must have at least one category and one month column.")
    
    # Rename first column to 'Category' for consistency
    df = df.rename(columns={df.columns[0]: "Category"})
    df.set_index("Category", inplace=True)
    
    # Check column headers: all except 'Category' must be YYYY-MM
    month_cols = df.columns
    for col in month_cols:
        if not isinstance(col, str) or not col[:4].isdigit() or col[4] != '-' or not col[5:7].isdigit():
            raise ExcelFormatError(f"Column header '{col}' does not match YYYY-MM format.")
    
    # Check for missing (empty or NaN) values
    if df.isnull().values.any():
        missing = df.isnull().sum().sum()
        raise ExcelFormatError(f"Found {missing} missing values in the table. Please complete all cells.")
    
    # Optional: convert values to float
    df = df.astype(float)
    return df
