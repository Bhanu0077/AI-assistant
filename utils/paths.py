import os

# Project root = folder containing main.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def project_path(*paths):
    return os.path.join(BASE_DIR, *paths)
