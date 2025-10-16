# AWS → Microsoft Teams Alerts
EventBridge → Lambda → Teams webhook with Adaptive Cards.

## Architecture
```mermaid
flowchart LR
  EVT[AWS Event] --> L[Lambda]
  L --> T[Teams Webhook]
```

## Deploy
```bash
sam build && sam deploy --guided
```

## Outcome
- Alerts delivered to Teams channels with context (service, severity)
