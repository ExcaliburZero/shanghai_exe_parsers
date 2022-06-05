from dataclasses import dataclass
from typing import IO, List


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
    @staticmethod
    def from_shd(line: str) -> "Battle":
        pass
