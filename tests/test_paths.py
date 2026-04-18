from pathlib import Path
import sys
import unittest

from upl.paths import PROJECT_ROOT, discover_project_root, repo_path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class PathsTests(unittest.TestCase):
    def test_discover_project_root_finds_repo_root(self):
        expected = Path(__file__).resolve().parent.parent
        self.assertEqual(discover_project_root(__file__), expected)

    def test_repo_path_joins_with_project_root(self):
        target = repo_path("learning", "data")
        self.assertEqual(target, PROJECT_ROOT / "learning" / "data")


if __name__ == "__main__":
    unittest.main()
