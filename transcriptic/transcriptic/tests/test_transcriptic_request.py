#!/usr/bin/env python
import json
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from unittest.mock import Mock, patch
from transcriptic.protocol_launch_call import make_transcriptic_request



sample_response = json.dumps(
"""{
  "id": "lr18wrhb23k54vk",
  "user_id": "u16r234n2393m",
  "protocol_id": "pr18v9bpcsjn4p",
  "inputs": {
    "refs": {
      "o397_10uM": {
        "id": "ctl84ud9p7se2ug",
        "label": "plasmid_dna",
        "type": "micro-1.5",
        "store": "cold_20",
        "cover": null,
        "aliquots": {
          "0": {
            "name": "plasmid_dna",
            "volume": "94.8:microliter",
            "properties": {
              "Concentration": "10.00uM",
              "Sequence": "actcgactagatcaggatcagagctagcatcgatcagct"
            }
          }
        }
      }
    },
    "parameters": {
      "reaction_setup": {
        "total_reaction_volume": "20:microliter",
        "ligase_type": "thermo",
        "ligase_vol": "1:microliter",
        "gel": true
      },
      "reactions": [
        {
          "fragments": [
            {
              "fragment": "plasmid_dna/0",
              "volume": "3:microliter"
            }
          ]
        }
      ],
      "lig": [
        {
          "cycles": 1,
          "steps": [
            {
              "temperature": "22:celsius",
              "duration": "30:minute"
            }
          ]
        }
      ],
      "deact": [
        {
          "cycles": 1,
          "steps": [
            {
              "temperature": "65:celsius",
              "duration": "10:minute"
            }
          ]
        }
      ]
    }
  },
  "autoprotocol": null,
  "generation_errors": [],
  "progress": 0,
  "created_at": "2016-04-21T17:20:44.839-07:00",
  "updated_at": "2016-04-21T17:20:44.839-07:00",
  "validated_at": null,
  "test_mode": false
}""")


def get_free_port():
    """ Find a free port to bind to
    """
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(("localhost", 0))
    addr, port = s.getsockname()
    s.close()
    return port


class MockServer(BaseHTTPRequestHandler):
    """ Mock transcriptic 
    
    Mock /protocols/:protocol_id/launch endpoint.
    """
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        with open("protocol-launch-response.json", "r") as resp:
            resp = json.load(resp)
            resp = json.dump(resp).encode()
            self.wfile.write(resp)


class TestMockServer:
    """ Test transcriptic API calls
    """
    @classmethod
    def setup_class(cls):
        """ Setup the MockServer and run it as a daemon
        """
        cls.mock_server_port = get_free_port()
        cls.mock_server = HTTPServer(("localhost", cls.mock_server_port), MockServer)

        cls.mock_server_thread = Thread(target=cls.mock_server.serve_forever)
        cls.mock_server_thread.setDaemon(True)
        cls.mock_server_thread.start()
    
    @patch("transcriptic.protocol_launch_call.requests.post")
    def test_auth_create(self, mock_post, capfd):
        mock_post.return_value = Mock(ok=True)
        mock_post.return_value.json.return_value = sample_response

        response = make_transcriptic_request()
        
        assert response.json()
        assert response.json() == sample_response
