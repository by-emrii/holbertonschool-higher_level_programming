#!/usr/bin/env python3
"""
This is the "task_02_csv.py" module.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to a JSON file
    """
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            read = list(csv.DictReader(csv_file))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(read, json_file)

        return True
    except Exception:
        return False
