import os.path
import unittest

import shanghai_exe_parser as sep


class TestMap(unittest.TestCase):
    def test_from_shd(self) -> None:
        # input_filepath = os.path.join("examples", "airCleaner1.shd")
        input_filepath = os.path.join("examples", "genNet2.shd")
        with open(input_filepath, "r") as input_stream:
            map = sep.Map.from_shd(input_stream)
