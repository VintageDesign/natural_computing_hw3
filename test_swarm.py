#!/usr/bin/env python3
import argparse
from swarming import Particle_Swarm

def parse_args():
    parser = argparse.ArgumentParser(description="Swarm Optimization of f(x) = (2^(-2((x-.01)/.9)^2) * (sin(5*pi*x))^6")

    parser.add_argument(
        "--quiet",
        action="store_true",
        default=False,
        help="Quiet all output.")
    parser.add_argument(
        "--population",
        "-p",
        type=int,
        default=25,
        help="The population size.")
    parser.add_argument(
        "--it_max",
        "-i",
        type=int,
        default=30,
        help="maximum iterations")
    parser.add_argument(
        "--v_max",
        type=int,
        default=.5,
        help="maximum velocity")
    parser.add_argument(
        "--v_min",
        type=int,
        default=.01,
        help="minimum velocity")

    return parser.parse_args()


def main(args):
    print(args)
    swarm = Particle_Swarm(
        args.population,
        args.it_max,
        args.v_min,
        args.v_max
    )

    swarm.run()


if __name__ == "__main__":
    main(parse_args())
