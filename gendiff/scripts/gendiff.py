#!usr/bin/env python3

from argparse import Namespace, ArgumentParser
from gendiff import generate_diff


def get_args() -> Namespace:
    parser = ArgumentParser(description="Compares two files and shows a diff.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    difference = generate_diff(args.first_file, args.second_file)
    print(difference)


if "__name__" == "__main__":
    main()
