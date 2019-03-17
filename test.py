#!/usr/bin/env python3
import argparse

import numpy as np

from clustering import Cluster


def parse_args():
    parser = argparse.ArgumentParser(description="Cluster objects via the ACA")

    parser.add_argument(
            "--quiet",
            action="store_true",
            default=False,
            help="Quiet all output.")
    parser.add_argument(
            "--population",
            "-p",
            type=int,
            default=10,
            help="The population size.")
    parser.add_argument(
            "--colors",
            "-c",
            type=int,
            default=2,
            help="The number of object types")
    parser.add_argument(
        "--objects",
        "-o",
        type=int,
        default=20,
        help="The number of objects to cluster." )
    parser.add_argument(
        "--x_size",
        "-x",
        type=int,
        default=200,
        help="The column count of the board" )
    parser.add_argument(
        "--y_size",
        "-y",
        type=int,
        default=200,
        help="The row count of the board" )
    parser.add_argument(
        "--ticks", "-t",
        type=int,
        default=200,
        help="The ticks that that the cluster will run for" )

    return parser.parse_args()


def main(args):
    print(args)
    cluster = Cluster(args.population, args.objects, args.colors, args.x_size, args.y_size, args.ticks)
    cluster.print_board(0)
    cluster.run_algorithm()




if __name__ == "__main__":
    main(parse_args())
