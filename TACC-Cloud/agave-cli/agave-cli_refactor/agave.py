#!/usr/bin/env python
"""Agave CLI

Refactoring of agave-cli in python.
"""
from __future__ import print_function
import argparse
import sys
import tenants


# Parser and subparsers definition.
parser = argparse.ArgumentParser()
parser.add_argument("--version", action="version", version="0.0.1")
subparsers = parser.add_subparsers()

###############################################################################
#                                                                             #
#                        Tenant Command Line Option                           #
#                                                                             #
###############################################################################
tenant_parser = subparsers.add_parser("tenant")

# tenant init argument.
tenant_parser.add_argument(
        "init", help="Configure the context for a given tenant.")
tenant_parser.add_argument(
    "-H",
    "--hosturl",
    default="https://api.tacc.utexas.edu/tenants",
    help="URL of Agave central service")


# tenant ls argument.
tenant_parser.add_argument(
    "ls", help="List all available tenants from the Agave central database")
tenant_parser.add_argument(
    "-H",
    "--hosturl",
    default="https://api.tacc.utexas.edu/tenants",
    help="URL of Agave central service")


# Tenant entrypoint.
tenant_parser.set_defaults(func=tenants.tenants_cmd)


if __name__ == "__main__":
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args.func(args)
