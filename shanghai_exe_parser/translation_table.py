from dataclasses import dataclass
from typing import Dict, IO, List, Optional

import xml.etree.ElementTree as ET


@dataclass
class TranslationTable:
    entries: Dict[str, str]

    def __getitem__(self, key: str) -> str:
        return self.entries[key]

    def load_from_xml(
        self, input_stream: IO[str], types: Optional[List[str]] = None
    ) -> None:
        if types is None:
            types = ["Text", "Dialogue"]

        tree = ET.parse(input_stream)

        root = tree.getroot()
        for t in types:
            for item in root.findall(t):
                key = item.attrib["Key"]
                value = item.attrib["Value"]

                self.entries[key] = value

    @staticmethod
    def new(entries: Optional[Dict[str, str]] = None) -> "TranslationTable":
        if entries is None:
            entries = {}

        return TranslationTable(entries)
