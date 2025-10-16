![CI](https://github.com/berkeleyo/aws-teams-alerts/actions/workflows/python-ci.yml/badge.svg)
![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# AWS -> Teams Alerts

**Flow:** CloudWatch Alarm â†’ SNS Topic â†’ Lambda â†’ Teams Incoming Webhook (Adaptive Card).

## Deploy (CloudFormation)
```bash
aws cloudformation deploy \
  --stack-name teams-alerts \
  --template-file template.yaml \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides TeamsWebhookUrl="https://outlook.office.com/webhook/..." LambdaName="teams-alerts-lambda"
```

## Wire CloudWatch
- In your Alarm action, choose **SNS** and select the created topic `cloudwatch-alarms-to-teams`.

