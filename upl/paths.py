from __future__ import annotations

from pathlib import Path
from typing import Iterable


def _has_marker(directory: Path, markers: Iterable[str]) -> bool:
    return any((directory / marker).exists() for marker in markers)


def discover_project_root(start: Path | str | None = None) -> Path:
    """
    Walk upward from ``start`` until a repo marker is found.

    Markers include a VCS directory or top-level project files so clones can be
    relocated without breaking imports.
    """
    markers = (".git", ".hg", "README.md", "pyproject.toml", "learning")
    start_path = Path(start or __file__).resolve()
    current = start_path if start_path.is_dir() else start_path.parent

    for directory in (current, *current.parents):
        if _has_marker(directory, markers):
            return directory

    return current


PROJECT_ROOT = discover_project_root()


def repo_path(*parts: str | Path) -> Path:
    """Join paths relative to the discovered project root."""
    return PROJECT_ROOT.joinpath(*map(Path, parts))
