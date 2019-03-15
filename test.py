import argparse

import numpy as np

from clustering import Cluster


def parse_args():
    parser = argparse.ArgumentParser(description="Cluster objects via the ACA")

    parser.add_argument("--quiet", action="store_true", default=False, help="Quiet all output.")
    parser.add_argument("--population", "-p", type=int, default=10, help="The population size.")
    parser.add_argument("--colors", "-c", type=int, default=2, help="The number of object types")
    parser.add_argument(
        "--objects",
        "-o",
        type=int,
        default=20,
        help="The number of objects to cluster.",
    )
    parser.add_argument(
        "--x_size", "-x", type=int, default=200, help="The column count of the board"
    )
    parser.add_argument(
        "--y_size", "-y", type=int, default=200, help="The row count of the board"
    )

    return parser.parse_args()


def main(args):




if __name__ == "__main__":
    main(parse_args())
