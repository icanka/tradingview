"""
This module contains utility functions for the project.
"""
import json

def dump_json(data, filename):
    """Place holder docstring"""
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)
