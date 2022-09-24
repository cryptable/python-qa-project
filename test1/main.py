import argparse
from .fibonacci import Fibonacci

parser = argparse.ArgumentParser()
parent_subparser = parser.add_subparsers()
fibo = Fibonacci(parent_subparser)


def get_argument_parser():
    return parser


def main():
    parser = get_argument_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        exit(args.func(args))
    else:
        parser.print_help()
        exit(-1)


if __name__ == "__main__":
    main()
