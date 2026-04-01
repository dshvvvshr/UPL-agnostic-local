# UPL (location-agnostic)

This repository is trimmed down to focus on making UPL runnable from any clone location with no hardcoded absolute paths. Project paths are discovered relative to the repository root so modules and tests work when the repo is moved, symlinked, or vendored.

## Project root discovery

`upl.paths.discover_project_root` walks upward from the calling file until it finds a repo marker (such as `.git` or `README.md`). `upl.paths.PROJECT_ROOT` caches that location and `upl.paths.repo_path(*parts)` builds paths relative to it.

## Learning storage defaults

`upl.storage.LearningStorage` defaults to `learning/data/` under the project root. It accepts either `str` or `pathlib.Path` inputs and creates any missing directories on write. This keeps local learning artifacts contained in the repo regardless of where it is cloned.

## Prime Directive Zero + UPL

UPL code and Prime Directive Zero assets can coexist as long as they both resolve paths relative to `PROJECT_ROOT` and write transient data under `learning/data/`. Keep long-lived documents and specs in the repo; keep generated artifacts under `learning/data/` so they can be cleaned or ignored safely.

## Running tests

```bash
python -m unittest
```
