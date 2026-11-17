import os
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from main import run

class ProjectTests(unittest.TestCase):
    def setUp(self):
        os.chdir(ROOT)

    def test_representative_sample(self):
        result=run()
        expected={'total_rows': 5, 'partition_rows': 2, 'rows_avoided': 3, 'customers_in_partition': 1}
        for key,value in expected.items():
            self.assertEqual(result[key],value, f'Mismatch on {key}')

    def test_replay_consistency(self):
        self.assertEqual(run(),run())

if __name__=='__main__':
    unittest.main()
