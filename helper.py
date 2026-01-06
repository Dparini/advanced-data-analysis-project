"""Helper functions and variables."""

from pathlib import Path


def get_project_root() -> Path:
    """Return the root directory of the project."""
    start_dir = Path.cwd()

    markers = [".git", "pyproject.toml", "uv.lock"]

    # Traverse parents looking for markers
    for path in [start_dir] + list(start_dir.parents):
        for marker in markers:
            if (path / marker).exists():
                return path

    # Fallback: Return current dir if no root found
    return start_dir
