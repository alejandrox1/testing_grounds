""" 
    tenants.py
"""
from __future__ import print_function
import requests
import sys



def tenant_init(arguments):
    """ Initiate an Agave Tenant 

    PARAMETERS
    ----------
    arguments: object (argparse.Namespace)
    """
    pass



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
    # Set hosturl.
    if not arguments.hosturl:
        hosturl = "https://api.tacc.utexas.edu/tenants"
    else:
        hosturl = arguments.hosturl

    # Make request.
    try:
        resp = requests.get(hosturl)
    except requests.exceptions.MissingSchema as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    # Handle Errors.
    # Handle bad status code.
    if resp.status_code >= 400:
        print(
            "Bad GET request to {0}, status code {1}".format(
                hosturl, resp.status_code),
            file=sys.stderr)
        sys.exit(1)

    # Print results.
    print("{0:<20} {1:<40}".format("CODE", "NAME"))
    for tenant in resp.json()["result"]:
        print("{0:<20} {1:<40}".format(tenant["code"], tenant["name"]))



def tenants_cmd(arguments):
    """ Tenants Command

    PARAMETERS
    ----------
    arguments: object (argparse.Namespace)
    """
    if (arguments.init):
        # Use an agave tenant.
        tenant_init(arguments)
    elif (arguments.ls):
        # List agave tenants.
        tenant_list(arguments)
