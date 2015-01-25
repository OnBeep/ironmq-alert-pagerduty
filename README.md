# ironmq-alert-pagerduty
Basic IronWorker to translate from IronMQ Alerts to PagerDuty Incidents

# Config
This worker expects two values are configured for it, in the HUD Dashboard:
```yaml
pagerduty_api_key: EXAMPLEKEY
pagerduty_service_key: ANOTHEREXAMPLEKEY
```

# Payload
This worker expects the standard IronMQ Alert message as payload:
```json
{
    "alert_direction": "asc",
    "alert_id": "54c548fc7fae9a32210f5782",
    "alert_trigger": 1,
    "alert_type": "fixed",
    "created_at": "2015-01-25T19:52:39Z",
    "queue_size": 1,
    "source_queue": "example_queue_name"
}
```

# Result
This will create/update a PagerDuty Incident. The "incident key" will be the
value of the ```source_queue``` in the payload. The incident name look like
"Queue [example_queue_name] is at size [1]".
