from __future__ import annotations

from pathlib import Path
from typing import Union

from .paths import repo_path

PathInput = Union[str, Path]

DEFAULT_LEARNING_SUBDIR = Path("learning") / "data"
DEFAULT_LEARNING_PATH = repo_path(DEFAULT_LEARNING_SUBDIR)


def _to_path(value: PathInput | None) -> Path:
    if value is None:
        return DEFAULT_LEARNING_PATH
    return value if isinstance(value, Path) else Path(value)


class LearningStorage:
    """Lightweight storage helper that defaults to ``learning/data``."""

    def __init__(self, base_dir: PathInput | None = None):
        self.base_dir = _to_path(base_dir)

    def ensure_base(self) -> Path:
        self.base_dir.mkdir(parents=True, exist_ok=True)
        return self.base_dir

    def path_for(self, relative: PathInput) -> Path:
        relative_path = relative if isinstance(relative, Path) else Path(relative)
        return self.base_dir / relative_path

    def write_text(self, relative: PathInput, content: str, encoding: str = "utf-8") -> Path:
        target = self.path_for(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding=encoding)
        return target

    def write_bytes(self, relative: PathInput, content: bytes) -> Path:
        target = self.path_for(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        return target

    def read_text(self, relative: PathInput, encoding: str = "utf-8") -> str:
        return self.path_for(relative).read_text(encoding=encoding)

    def read_bytes(self, relative: PathInput) -> bytes:
        return self.path_for(relative).read_bytes()
