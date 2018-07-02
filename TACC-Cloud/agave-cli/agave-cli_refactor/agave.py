#!/usr/bin/env python
"""Agave CLI

Refactoring of agave-cli in python.
"""
from __future__ import print_function
import argparse
import sys
import tenants


def greet(arguments):
    """Greet

    greet takes arguments parsed from argparse and creates a greeting.

    PARAMETERS
    ----------
    arguments: object (argparse.Namespace)
    """
    output = "{0}, {1}!".format(arguments.greeting, arguments.name)
    if arguments.caps:
        output = output.upper()
    print(output)


# Parser and subparsers definition.
parser = argparse.ArgumentParser()
parser.add_argument("--version", action="version", version="0.0.1")
subparsers = parser.add_subparsers()

# Example command line option.
hello_parser = subparsers.add_parser("hello")
hello_parser.add_argument("name", help="name of person to greet")
hello_parser.add_argument(
    "-g", "--greeting", default="Hello", help="greeting to use")
hello_parser.add_argument(
    "-c", "--caps", action="store_true", help="uppercase output")
hello_parser.set_defaults(func=greet)

# Tenant command line option.
tenant_parser = subparsers.add_parser("tenant")
tenant_parser.add_argument(
    "ls", help="List all available tenants from the Agave central database")
tenant_parser.add_argument(
    "-H",
    "--hosturl",
    default="https://api.tacc.utexas.edu/tenants",
    help="URL of Agave central service")
tenant_parser.set_defaults(func=tenants.tenants_list)

if __name__ == "__main__":
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args.func(args)
