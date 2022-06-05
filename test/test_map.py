import os.path
import unittest

import shanghai_exe_parser as sep


class TestMap(unittest.TestCase):
    def test_from_shd(self) -> None:
        input_filepath = os.path.join("examples", "genNet2.shd")

        with open(input_filepath, "r") as input_stream:
            map = sep.Map.from_shd(input_stream)

        self.assertEqual(58, map.grid.width())
        self.assertEqual(65, map.grid.height())
        self.assertEqual(2, map.grid.depth())

        self.assertEqual(9, len(map.battles))

        self.assertEqual(3, len(map.battles[0].viruses))
