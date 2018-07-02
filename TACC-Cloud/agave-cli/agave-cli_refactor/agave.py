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
