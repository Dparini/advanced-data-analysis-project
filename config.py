"""Configuration file for the notebooks."""

from pathlib import Path

from helper import get_project_root

# Paths
PROJECT_ROOT: Path = get_project_root()
DATA_DIR: Path = PROJECT_ROOT / "data"
RAW_DIR: Path = DATA_DIR / "raw"
PROCESSED_PATH: Path = DATA_DIR / "processed"
FINAL_PATH: Path = PROCESSED_PATH / "final"
OUTPUT_PATH: Path = PROJECT_ROOT / "models"
RITTER_PATH: Path = RAW_DIR / "IPO-age.xlsx"
RITTER_URL: str = "https://site.warrington.ufl.edu/ritter/files/IPO-age.xlsx"


if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    FINAL_PATH.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)