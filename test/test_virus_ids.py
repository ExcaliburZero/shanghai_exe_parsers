import os.path
import unittest

import shanghai_exe_parser as sep


class TestVirusIds(unittest.TestCase):
    def test_from_csv(self) -> None:
        input_filepath = os.path.join("data", "virus_ids.csv")

        with open(input_filepath, "r") as input_stream:
            table = sep.VirusIds.from_csv(input_stream)

        self.assertEqual("BibitBat", table[13])
