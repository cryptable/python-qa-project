"""Main code for test1 CLI.

This module is the basis of the CLI. It only parser arguments and
execute the connected function to the parser. The parameters and
function connection  is done in the submodules.

"""
import argparse
from .fibonacci import Fibonacci

parser = argparse.ArgumentParser()
parent_subparser = parser.add_subparsers()
fibo = Fibonacci(parent_subparser)


def get_argument_parser():
    """get parser for the arguments.

    Mainly used for testing purposes (see tests)

    :return: The argument parser

    """
    return parser


def main():
    """main function to execute.

    Run the app, all logic and business functions are located in submodules.

    :return: depends on the submodules.

    """
    args = parser.parse_args()
    if hasattr(args, "func"):
        exit(args.func(args))
    else:
        parser.print_help()
        exit(-1)


if __name__ == "__main__":
    main()
