import json
import os

class ConfigFormatError(Exception):
    pass

def load_tab_config(config_path, all_categories):
    """
    Loads tab config from a JSON file.
    - config_path: path to config/tabs_config.json
    - all_categories: list of all category names (from Excel)
    Returns: dict {tab_name: [list of checked category names]}
    """
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Tab config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    if not isinstance(config, dict):
        raise ConfigFormatError("Tab config must be a dictionary.")

    # Validate that all checked categories actually exist in the loaded data
    for tab, categories in config.items():
        if not isinstance(categories, list):
            raise ConfigFormatError(f"Categories for tab '{tab}' must be a list.")
        unknown = set(categories) - set(all_categories)
        if unknown:
            raise ConfigFormatError(
                f"Tab '{tab}' has unknown categories: {unknown}. "
                "Update config or Excel data."
            )
    return config
