"""Helper functions for YouTube2FreshRSS."""

import json


def read_config_file():
    """Read secrets JSON file."""
    with open("config.json", "rb") as config_file:
        data = json.load(config_file)

    return data
