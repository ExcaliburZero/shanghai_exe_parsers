import os.path
import unittest

import shanghai_exe_parser as sep


class TestTranslationTable(unittest.TestCase):
    def test_load_from_xml(self) -> None:
        input_filepath = os.path.join("examples", "GenNet2.xml")

        table = sep.TranslationTable.new()

        with open(input_filepath, "r") as input_stream:
            table.load_from_xml(input_stream)

        actual = table["Map.GenNet2Name"]
        expected = "Genso Area 2"

        self.assertEqual(expected, actual)
