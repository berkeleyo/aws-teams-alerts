import json, os, urllib.request

TEAMS_WEBHOOK_URL = os.environ.get("TEAMS_WEBHOOK_URL", "")

def post_to_teams(card):
    if not TEAMS_WEBHOOK_URL:
        raise RuntimeError("TEAMS_WEBHOOK_URL not set")
    data = json.dumps(card).encode("utf-8")
    req = urllib.request.Request(TEAMS_WEBHOOK_URL, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode()

def build_card(title, severity, description, link=None):
    return {
        "type": "message",
        "attachments": [{
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "type": "AdaptiveCard",
                "version": "1.4",
                "body": [
                    {"type": "TextBlock", "size": "Large", "weight": "Bolder", "text": title},
                    {"type": "TextBlock", "text": f"Severity: {severity}"},
                    {"type": "TextBlock", "wrap": True, "text": description or "No description"}
                ],
                "actions": ([{"type":"Action.OpenUrl","title":"Open in AWS Console","url":link}] if link else [])
            }
        }]
    }

def lambda_handler(event, context):
    # Event from SNS -> records list
    records = event.get("Records", [])
    for rec in records:
        if rec.get("EventSource") == "aws:sns":
            msg = rec["Sns"]["Message"]
            try:
                payload = json.loads(msg)
            except json.JSONDecodeError:
                payload = {"AlarmText": msg}

            title = payload.get("AlarmName") or payload.get("AlarmDescription") or "CloudWatch Alarm"
            severity = payload.get("NewStateValue") or payload.get("Severity", "N/A")
            desc = payload.get("NewStateReason") or payload.get("StateChangeTime") or "Alarm notification"
            link = payload.get("AlarmArn")
            post_to_teams(build_card(title, severity, desc, link))
    return {"status": "ok"}
