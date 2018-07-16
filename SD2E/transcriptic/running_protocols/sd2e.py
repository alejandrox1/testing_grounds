from transcriptic import Connection
import json
import time 

params = {
  "parameters": {
    "items": [
      {
        "name": "10X TBS with 0.5 Tween 20.",
        "cont_type": "micro-1.5",
        "res_id": "rs19ktpq4z7teg",
        "vol": "100:microliter",
        "dead_vol": False,
        "storage_condition": "cold_20"
      }
    ]
  }
}

def _create_launch_request(params, bsl=1, test_mode=False):
    """Creates launch_request from input params"""
    params_dict = dict()
    params_dict["launch_request"] = params
    params_dict["launch_request"]["bsl"] = bsl
    params_dict["launch_request"]["test_mode"] = test_mode
    return json.dumps(params_dict)


api = Connection.from_file("/home/jochoa/.transcriptic")


launch_request = _create_launch_request(params, test_mode=False)
launch_protocol = api.launch_protocol(launch_request, protocol_id="pr1bjexfxj424v")

time.sleep(6)

launch_request_id = launch_protocol["id"]
api.submit_launch_request(
    launch_request_id, 
    protocol_id="pr1bjexfxj424v",
    project_id="p1bqm3ehqzgum", 
    title="py test", 
    test_mode=False,
)
