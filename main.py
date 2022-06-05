from typing import List

import argparse
import os.path
import sys

import shanghai_exe_parser as sep

SUCCESS = 1
FAILURE = 0


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument("--virus_ids", default=os.path.join("data", "virus_ids.csv"))

    subparsers = parser.add_subparsers(dest="command")

    map_parser = subparsers.add_parser("map")
    map_parser.add_argument("map_shd")

    args = parser.parse_args(argv)

    result = SUCCESS
    if args.command == "map":
        result = run_map(args.map_shd, args.virus_ids)
    else:
        result = FAILURE

        parser.print_usage()

    return result


def run_map(map_shd: str, virus_ids_filepath: str) -> int:
    with open(map_shd, "r") as input_stream:
        map = sep.Map.from_shd(input_stream)

    with open(virus_ids_filepath, "r") as input_stream:
        virus_ids = sep.VirusIds.from_csv(input_stream)

    print("Battles:")
    for i, b in enumerate(map.battles):
        print(f"\t{i}:")
        for virus in b.viruses:
            print(f"\t\t{virus_ids[virus.virus_id]}")

    return SUCCESS


if __name__ == "__main__":
    result = main(sys.argv[1:])
    sys.exit(result)
