import argparse
import json
import pprint
import pygerduty
import time
import yaml

parser = argparse.ArgumentParser(description="Simple argument parser")
parser.add_argument("-config", type=str, required=False,
        help="The location of a file containing a JSON payload.")
parser.add_argument("-payload", type=str, required=False,
        help="The location of a file containing a JSON payload.")
parser.add_argument("-d", type=str, required=False,
        help="Directory")
parser.add_argument("-e", type=str, required=False,
        help="Environment")
parser.add_argument("-id", type=str, required=False,
        help="Task id")
args = parser.parse_args()

config = {}
if args.config is not None:
    config = yaml.load(open(args.config).read())
pdapi = config['pagerduty_api_key']
pdsvc = config['pagerduty_service_key']
pdsub = config['pagerduty_subdomain']

payload = {}
if args.payload is not None:
    payload = json.loads(open(args.payload).read())

# Alert payloads are expected to look like the following:
# {
#     "alert_direction": "asc",
#     "alert_id": "54c548fc7fae9a32210f5782",
#     "alert_trigger": 1,
#     "alert_type": "fixed",
#     "created_at": "2015-01-25T19:52:39Z",
#     "queue_size": 1,
#     "source_queue": "example_queue_name"
# }
queue_name = payload['source_queue']
queue_size = payload['queue_size']

desc = 'Queue [%s] is at size [%s]' % (queue_name, queue_size)
pagerduty = pygerduty.PagerDuty(pdsub, api_token=pdapi)
pagerduty.trigger_incident(
    pdsvc,
    desc,
    incident_key=queue_name,
    details=payload)
