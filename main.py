from typing import List

import argparse
import sys

import shanghai_exe_parser as sep

SUCCESS = 1
FAILURE = 0


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    map_parser = subparsers.add_parser("map")
    map_parser.add_argument("map_shd")

    args = parser.parse_args(argv)

    result = SUCCESS
    if args.command == "map":
        result = run_map(args.map_shd)
    else:
        result = FAILURE

        parser.print_usage()

    return result


def run_map(map_shd: str) -> int:
    with open(map_shd, "r") as input_stream:
        map = sep.Map.from_shd(input_stream)

    print("Battles:")
    for i, b in enumerate(map.battles):
        print(f"\t{i}:")
        for virus in b.viruses:
            print(f"\t\t{virus}")

    return SUCCESS


if __name__ == "__main__":
    result = main(sys.argv[1:])
    sys.exit(result)
