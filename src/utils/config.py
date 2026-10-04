import json


def load_config(path="config/config.json"):
    """Read settings from the config file, using defaults if it's missing."""
    defaults = {
        "data_file": "data/students.json",
        "log_file": "logs/student_system.log",
    }

    try:
        with open(path) as f:
            return {**defaults, **json.load(f)}
    except FileNotFoundError:
        return defaults