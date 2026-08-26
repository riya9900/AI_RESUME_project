"""
Application Entrypoint Launcher
Delegates to modular application package in src/app/main.py
"""
import sys
from pathlib import Path

# Ensure root is in sys.path
root_dir = Path(__file__).resolve().parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from src.app.main import main

if __name__ == "__main__":
    main()
