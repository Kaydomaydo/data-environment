# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    env = os.getenv("FLASK_ENV", "empty")
    if env is None or env == "":
        return "Starting in empty mode..."
    else:
        return f"Starting in {env} mode..."

if __name__ == "__main__":
    print(start())
