# AWS -> Teams Alerts

**Flow:** CloudWatch Alarm → SNS Topic → Lambda → Teams Incoming Webhook (Adaptive Card).

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
