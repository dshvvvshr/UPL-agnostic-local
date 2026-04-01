from pathlib import Path
import sys
import tempfile
import unittest

from upl.paths import PROJECT_ROOT
from upl.storage import DEFAULT_LEARNING_PATH, LearningStorage

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class LearningStorageTests(unittest.TestCase):
    def test_default_base_dir_points_into_learning_data(self):
        expected = PROJECT_ROOT / "learning" / "data"
        self.assertEqual(DEFAULT_LEARNING_PATH, expected)
        storage = LearningStorage()
        self.assertEqual(storage.base_dir, expected)

    def test_accepts_path_inputs_and_round_trips_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_base = Path(tmp) / "store-root"
            storage = LearningStorage(tmp_base)
            written = storage.write_text(Path("notes/info.txt"), "hello world")
            self.assertTrue(written.exists())
            self.assertEqual(written.parent, tmp_base / "notes")
            self.assertEqual(storage.read_text("notes/info.txt"), "hello world")

    def test_write_bytes_creates_missing_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            storage = LearningStorage(tmp)
            target = storage.write_bytes("bin/model.bin", b"\x00\x01")
            self.assertTrue(target.exists())
            self.assertEqual(target.read_bytes(), b"\x00\x01")


if __name__ == "__main__":
    unittest.main()
