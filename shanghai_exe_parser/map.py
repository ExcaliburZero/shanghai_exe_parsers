from dataclasses import dataclass
from typing import IO, List


@dataclass
class Map:
    grid: "Grid"

    @staticmethod
    def from_shd(input_stream: IO[str]) -> "Map":
        line = next(input_stream)

        print(line)

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

        return Map(grid=grid)


@dataclass
class Grid:
    # z, x, y
    tiles: List[List[List[int]]]

    @staticmethod
    def from_shd(input_stream: IO[str], x_len: int, y_len: int, z_len: int) -> "Grid":
        tiles = []
        for current_z in range(0, z_len):
            floor = []
            for current_y in range(0, y_len):
                row = []

                line = next(input_stream).strip()
                while line == "":
                    assert current_y == 0
                    line = next(input_stream).strip()

                assert len(line.split(",")) == x_len

                for tile in line.split(","):
                    row.append(int(tile))

                floor.append(row)
            tiles.append(floor)

        return Grid(tiles)
