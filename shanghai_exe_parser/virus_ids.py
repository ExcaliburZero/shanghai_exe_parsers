from dataclasses import dataclass
from typing import Dict, IO

import csv


@dataclass
class VirusIds:
    id_table: Dict[int, str]

    def __getitem__(self, key: int) -> str:
        return self.id_table[key]

    @staticmethod
    def from_csv(input_stream: IO[str]) -> "VirusIds":
        id_table = {}
        for entry in csv.DictReader(input_stream):
            id_table[int(entry["id"])] = entry["name"]

        return VirusIds(id_table)
