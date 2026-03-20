# utils/file_handler.py
"""
Handles:
1. export to JSON
"""
import json

def export_to_json(data, filepath):
    """
    Export data to a JSON file.

    Args:
        data: list/dict
        filepath: destination file path
    """
    try:
        with open(filepath, mode="w") as file:
            json.dump(data, file, indent=4)
            print(f"Data successfully exported to {filepath}")
    except FileNotFoundError:
        print("Error: Directory does not exist")

    except PermissionError:
        print("Error: Permission denied")

    except Exception as e:
        print(f"Error: Failed to export data - {e}")
    