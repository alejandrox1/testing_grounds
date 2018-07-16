request = {
  "title": "My ligation run",
  "parameters": {
    "inputs": {
      "reaction_setup": {
        "inputs": {
          "total_reaction_volume": "20:microliter",
          "ligase_type": "thermo",
          "ligase_vol": "1:microliter",
          "gel": True
        }
      },
      "reactions": {
        "inputs": {
          "fragments": {
            "inputs": {
              "fragment": "ctxxxxxxxxx/A1",
              "volume": "5:microliter"
            }
          }
        }
      },
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
      ]
    },
    "deact": {
      "type": "thermocycle",
      "label": "deactivation conditions",
      "default": [
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
    },
    "test_mode": False
  },
  "test_mode": False
}
