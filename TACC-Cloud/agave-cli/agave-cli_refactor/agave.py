#!/usr/bin/env python
"""Agave CLI

Refactoring of agave-cli in python.
"""
from __future__ import print_function
import argparse
import sys
import tenants

# Parser and subparsers definition.
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument(
    "-H",
    "--hosturl",
    default="https://api.tacc.utexas.edu/tenants",
    help="URL of Agave central service")

main_parser = argparse.ArgumentParser()

commands_subparsers = main_parser.add_subparsers(
    title="Commands", dest="commands_cmd")

###############################################################################
#                                                                             #
#                        Tenant Command Line Option                           #
#                                                                             #
###############################################################################
command_parser = commands_subparsers.add_parser(
    "tenant", help="Manage Agave tenants", parents=[parent_parser])

action_subparser = command_parser.add_subparsers(
    title="action", dest="action_cmd")

# Tenant init command.
tenant_init_parser = action_subparser.add_parser(
    "init",
    help="Configure the context for a given tenant",
    parents=[parent_parser])
tenant_init_parser.add_argument(
    "tenant_name", help="Name of agave tenant to use")

# Tenant ls command.
tenant_ls_parser = action_subparser.add_parser(
    "ls",
    help="List all available tenants from the Agave central database",
    parents=[parent_parser])
tenant_ls_parser.set_defaults(func=tenants.tenant_list)



if __name__ == "__main__":
    args = main_parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args.func(args)
