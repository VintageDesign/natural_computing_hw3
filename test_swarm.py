#!/usr/bin/env python3
import argparse
from swarming import Swarm

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
        default=5,
        help="The population size.")
    parser.add_argument(
        "--cities",
        "-c",
        type=int,
        default=5,
        help="The number of cities to organize.")

    return parser.parse_args()

def main(args):
    print(args)
    swarm = Swarm(
        args.population,
        args.cities
    )

if __name__ == "__main__":
    main(parse_args())