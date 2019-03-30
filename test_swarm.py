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
        default=100,
        help="maximum iterations")
    parser.add_argument(
        "--v_max",
        type=int,
        default=.3,
        help="maximum velocity")
    parser.add_argument(
        "--v_min",
        type=int,
        default=.1,
        help="minimum velocity")

    return parser.parse_args()


def main(args):
    print(args)
    j = 0
    avg_it = 0
    swarm = None
    while j < 100: 
        swarm = Particle_Swarm(
            args.population,
            args.it_max,
            args.v_min,
            args.v_max
        )

        x, y, it = swarm.pso()
        avg_it += it
        j += 1
    print("Average iterations: %f" % (avg_it/100))
    swarm.save_plot()


if __name__ == "__main__":
    main(parse_args())
