"""
    tenants.py
"""
from __future__ import print_function
import json
import requests
import sys
from os import path



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
        print("Bad GET request to {0}, status code {1}".format(
                hosturl, resp.status_code),
                file=sys.stderr)
        sys.exit(1)

    return resp.json()



def tenant_init(arguments):
    """ Initiate an Agave Tenant

    Create or switch the current context to a specified Agave tenant.
    The current context along with all previous used are stored in a 
    local database.

    PARAMETERS
    ----------
    arguments: object (argparse.Namespace)
        tenant_name: pecify the name of the Agave tenant to work with.
        hosturl: url of Agave system.
    """
    # Get a json of all Agave tenants.
    tenants = get_tenants(arguments.hosturl)

    list_of_tenants = [ x["code"] for x in tenants["result"] ]
    
    # Check if the given tenant is part of the specified Agave system.
    if arguments.tenant_name not in list_of_tenants:
        print("{0} is not a tenant in {1}".format(
                arguments.tenant_name, arguments.hosturl), 
                file=sys.stderr)
        sys.exit(1)

    # Organize metadata for tenant context.
    tenant_context = dict()
    tenant_index = list_of_tenants.index(arguments.tenant_name)
    tenant_info = tenants["result"][tenant_index]

    tenant_context["tenantid"]      = tenant_info["code"]
    tenant_context["baseurl"]       = tenant_info["baseUrl"]
    tenant_context["devurl"]        = ""
    tenant_context["apisecret"]     = ""
    tenant_context["apikey"]        = ""
    tenant_context["username"]      = "" 
    tenant_context["access_token"]  = "" 
    tenant_context["refresh_token"] = "" 
    tenant_context["created_at"]    = "" 
    tenant_context["expires_in"]    = ""
    tenant_context["expires_at"]    = ""

    # Read in Agave database if it doesn't already exist, else create one.
    if path.isfile("agave.json"):                                               
        with open("agave.json", "r") as f:                                           
            agave_context = json.load(f)                                        
    else:                                                                       
        agave_context  = dict()

    # Set the current context.
    agave_context["current"] = tenant_info["code"]

    # Append current context if contexts array is empty.
    if "tenants" not in agave_context:
        agave_context.setdefault("tenants", []).append(tenant_context)
    # Append current context if it doesn't already exit.
    elif agave_context["current"] not in [ x["tenantid"] for x in agave_context["tenants"] ]:
        agave_context["tenants"].append(tenant_context)

    # Save data to Agave database.
    with open("agave.json", "w") as f:
        json.dump(agave_context, f, sort_keys=True, indent=4)
    



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
