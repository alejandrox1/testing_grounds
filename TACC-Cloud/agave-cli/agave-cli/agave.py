#!/usr/bin/env python
"""Agave CLI

Refactoring of agave-cli in python.
"""
from __future__ import print_function
import argparse


def greet(arguments):
    """Greet

    greet takes arguments parsed from argparse and creates a greeting.

    PARAMETERS
    ----------
    arguments: object
    """
    output = "{0}, {1}!".format(arguments.greeting, arguments.name)
    if arguments.caps:
        output = output.upper()
    print(output)


parser = argparse.ArgumentParser()
parser.add_argument("--version", action="version", version="0.0.1")
subparsers = parser.add_subparsers()

hello_parser = subparsers.add_parser("hello")
hello_parser.add_argument("name", help="name of person to greet")
hello_parser.add_argument("--greeting", default="Hello", help="greeting to use")
hello_parser.add_argument(
    "--caps", action="store_true", help="uppercase output")
hello_parser.set_defaults(func=greet)

goodbye_parser = subparsers.add_parser("goodbye")
goodbye_parser.add_argument("name", help="name of person to greet")
goodbye_parser.add_argument("--greeting", default="Bye", help="greeting to use")
goodbye_parser.add_argument(
    "--caps", action="store_true", help="uppercase greeting")
goodbye_parser.set_defaults(func=greet)

if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)
