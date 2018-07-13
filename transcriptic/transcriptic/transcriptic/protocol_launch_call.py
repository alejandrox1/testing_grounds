#!/usr/bin/env python
"""
   protocol_launch_call.py

Following example from https://developers.transcriptic.com/docs/protocolsprotocol_idlaunch
"""
import json
import requests
from transcriptic.protocol_launch_request import request as body

def make_transcriptic_request():
    headers = {
        "X-User-Email" : "exaple@organization.com",
        "X-User-Token" : "someaccesstoken",
        "Content-Type" : "application/json",
        "Accept"       : "application/json"
    }

    url = "https://secure.transcriptic.com//:organization/protocols/:protocol_id/launch"

    response = requests.post(url, body, headers=headers)

    return response

if __name__ == "__main__":
    resp = make_transcriptic_request()
