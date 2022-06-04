from typing import List

import argparse
import sys

SUCCESS = 1
FAILURE = 0


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser()

    args = parser.parse_args(argv)

    return SUCCESS


if __name__ == "__main__":
    result = main(sys.argv[1:])
    sys.exit(result)
