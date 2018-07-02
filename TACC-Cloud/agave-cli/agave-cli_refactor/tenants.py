"""
    tenants.py
"""
from __future__ import print_function
import sys
import requests

AGAVE_DB = "agave.jsonl"


def get_tenants(hosturl):
    """ Get Agave tenants

    Get all Agave tenants for a given Agave host.

    PARAMETERS
    ----------
    hosturl: string
        URL to send GET request to. This resource should list all Agave
        tenants.
    """
    # Make request.
    try:
        resp = requests.get(hosturl)
    except requests.exceptions.MissingSchema as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    # Handle bad status code.
    if resp.status_code >= 400:
        print(
            "Bad GET request to {0}, status code {1}".format(
                hosturl, resp.status_code),
            file=sys.stderr)
        sys.exit(1)

    return resp.json()


def tenant_init(arguments):
    """ Initiate an Agave Tenant

    PARAMETERS
    ----------
    arguments: object (argparse.Namespace)
    """
    # Get a json of all AGave tenants.
    tenants = get_tenants(arguments)

    tenant_context = dict()

    #if arguments. in [ x["code"] for x in resp.json()["result"] ]


def tenant_list(arguments):
    """ List Agave tenants

    List all Agave tenants for a given Agave host. Information listed is the
    name and the code of the tenant.

    PARAMETERS
    ----------
    arguments: object (argparse.Namespace)
        This object may contain the following attributes:
        - hosturl: string representing a url (optional).
    """
    # Get a json of all AGave tenants.
    tenants = get_tenants(arguments.hosturl)

    # Print results.
    print("{0:<20} {1:<40}".format("CODE", "NAME"))
    for tenant in tenants["result"]:
        print("{0:<20} {1:<40}".format(tenant["code"], tenant["name"]))
