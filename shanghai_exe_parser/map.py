from dataclasses import dataclass
from typing import IO, List, Optional

NULL_VIRUS_ID = 0


@dataclass
class Map:
    grid: "Grid"
    battles: List["Battle"]

    @staticmethod
    def from_shd(input_stream: IO[str]) -> "Map":
        line = next(input_stream)

        parts = line.split(",")

        assert len(parts) == 14

        [
            x_len,
            y_len,
            rend_x,
            rend_y,
            rect_1,
            rect_2,
            save_plase,
            height,
            z_len,
            back_no,
            ecncount_cap_1,
            encount_cap_2,
            str1,
            _,
        ] = parts

        grid = Grid.from_shd(input_stream, int(x_len), int(y_len), int(z_len))

        battles = Map.__parse_battles(input_stream)

        return Map(grid=grid, battles=battles)

    @staticmethod
    def __parse_battles(input_stream: IO[str]) -> List["Battle"]:
        battles = []
        line = next(input_stream).strip()
        while line != "":
            battles.append(Battle.from_shd(line))

            line = next(input_stream).strip()

        return battles


@dataclass
class Grid:
    # z, x, y
    tiles: List[List[List[int]]]

    def width(self) -> int:
        return len(self.tiles[0][0])

    def height(self) -> int:
        return len(self.tiles[0])

    def depth(self) -> int:
        return len(self.tiles)

    @staticmethod
    def from_shd(input_stream: IO[str], x_len: int, y_len: int, z_len: int) -> "Grid":
        tiles = []
        for current_z in range(0, z_len):
            floor = []
            for current_y in range(0, y_len):
                row = []

                line = next(input_stream).strip()

                assert line != ""
                assert len(line.split(",")) == x_len

                for tile in line.split(","):
                    row.append(int(tile))

                floor.append(row)
            tiles.append(floor)

            line = next(input_stream).strip()
            assert line == ""

        return Grid(tiles)


@dataclass
class Battle:
    viruses: List["VirusEntry"]
    panel_1: int
    panel_2: int
    type: int
    count: bool
    result: bool
    escape: bool
    gameover: bool
    bgm: str
    back: int

    @staticmethod
    def from_shd(line: str) -> "Battle":
        parts = line.split(":")

        viruses = []

        if len(parts) >= 20:
            for i in range(0, 3):
                j = 1 + i * 9

                virus_id = int(parts[j])
                if virus_id == NULL_VIRUS_ID:
                    continue

                viruses.extend(
                    [
                        VirusEntry(
                            int(parts[j]),
                            int(parts[j + 1]),
                            int(parts[j + 2]),
                            int(parts[j + 3]),
                            int(parts[j + 4]),
                            int(parts[j + 5]),
                            int(parts[j + 6]),
                            int(parts[j + 7]),
                            parts[j + 8] or None,
                        )
                    ]
                )

            panel_1 = int(parts[28])
            panel_2 = int(parts[29])
            type = int(parts[30])
            count = parts[31] == "True"
            result = parts[32] == "True"
            escape = parts[33] == "True"
            gameover = parts[34] == "True"
            bgm = parts[35]
            back = int(parts[36])
        else:
            raise NotImplementedError("Small battle entries not yet supported")

        return Battle(
            viruses=viruses,
            panel_1=panel_1,
            panel_2=panel_2,
            type=type,
            count=count,
            result=result,
            escape=escape,
            gameover=gameover,
            bgm=bgm,
            back=back,
        )


@dataclass
class VirusEntry:
    virus_id: int
    lank: int
    x: int
    y: int
    chip_1: Optional[int]
    chip_2: Optional[int]
    chip_3: Optional[int]
    hp: Optional[int]
    name: Optional[str]
