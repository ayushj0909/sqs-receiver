# sqs-receiver

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.0.1](https://img.shields.io/badge/AppVersion-0.0.1-informational?style=flat-square)

A Helm chart for deploying an SQS Message Receiver

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Ayush | <ayush@amnic.com> |  |

## Source Code

* <https://github.com/ayushj0909/sqs-receiver>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| awsKeyID | string | `nil` |  |
| awsSecretKey | string | `nil` |  |
| image | string | `"ayushj0909/sqs-receiver:0.0.1"` |  |
| replicas | int | `4` |  |
| sqsQueueURL | string | `nil` |  |

## Installation

```
helm upgrade -i . --set awsKeyID=<> --set awsSecretKey=<> --set sqsQueueURL=<>
```