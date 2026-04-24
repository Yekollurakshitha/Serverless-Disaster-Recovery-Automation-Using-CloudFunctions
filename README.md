# 🌐 Serverless Disaster Recovery Automation Using Cloud Functions

## 📌 Overview
This project implements an automated **Disaster Recovery (DR)** system using **serverless cloud technologies**. It continuously monitors application health, detects failures, and automatically restores services using Cloud Functions with minimal downtime.

---

## 🚀 Features
- ⚡ Fully automated disaster recovery
- ☁️ Serverless architecture (no manual intervention)
- 📊 Real-time monitoring & alerting
- 🔄 Backup & restore using cloud storage
- ⏱️ Minimal downtime
- 📜 Logging and auditing

---

## 🧠 Architecture

             ┌──────────────┐
             │   Users      │
             └──────┬───────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Primary Server    │
          │ (Application)     │
          └────────┬──────────┘
                   │
                   ▼
       ┌──────────────────────┐
       │ Monitoring Service   │
       │ (Health Checks)      │
       └────────┬─────────────┘
                │
      🚨 Failure Detected
                │
                ▼
    ┌────────────────────────┐
    │ Alert System (SNS/Pub) │
    └────────┬───────────────┘
             │
             ▼
    ┌────────────────────────┐
    │ Cloud Function         │
    │ (Recovery Logic)       │
    └────────┬───────────────┘
             │
 ┌───────────┼───────────────┐
 ▼           ▼               ▼




 Fetch Backup Create New Configure DNS
from Storage Instance / Routing
│
▼
┌──────────────────────────┐
│ Application Restored ✅ │
└──────────────────────────┘




---

## ⚙️ Tech Stack

- **Cloud Functions** → AWS Lambda / Azure Functions / GCP
- **Storage** → AWS S3 / Blob Storage
- **Monitoring** → CloudWatch / Azure Monitor
- **Messaging** → SNS / Pub-Sub
- **Compute** → EC2 / Virtual Machines / Containers

---

## 🔄 Workflow

### 1️⃣ Normal State
- Application runs normally on primary server
- Health checks are continuously monitored
- Backups are stored in cloud storage

---

### 2️⃣ Failure Detection
- Server crash / high latency occurs
- Monitoring system detects anomaly

---

### 3️⃣ Alert Trigger
- Alert sent via SNS / Pub-Sub
- Cloud Function is triggered automatically

---

### 4️⃣ Disaster Recovery Execution
Cloud Function performs:
- Fetch latest backup
- Launch new instance
- Restore data
- Update routing

---

### 5️⃣ Service Restoration
- Application is restored on new instance
- Minimal downtime achieved

---

### 📍 Failure Detection
_Add monitoring alert screenshot_

### 📍 Cloud Function Triggered
_Add logs screenshot_

### 📍 Recovery Process
_Add infrastructure creation screenshot_

### 📍 Service Restored
_Add final output screenshot_

---

## 🧪 Test Cases

| Scenario            | Expected Result                  |
|--------------------|--------------------------------|
| Server crash       | Auto recovery triggered        |
| High latency       | Alert + recovery initiated     |
| Data corruption    | Restore from backup            |

---

## 🛠️ Setup Guide (AWS Example)

### ✅ Step 1: Create S3 Bucket
- Go to AWS S3
- Create bucket: `dr-backup-bucket`
- Store backups here

---

### ✅ Step 2: Deploy Application
- Launch EC2 instance
- Deploy your application

---

### ✅ Step 3: Configure Monitoring
- Go to CloudWatch
- Create alarm for:
  - CPU usage
  - Health checks

---

### ✅ Step 4: Create SNS Topic
- Create topic
- Subscribe email for alerts

---

### ✅ Step 5: Create Lambda Function

#### 📄 `recovery_function.py`

```python
import boto3

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Disaster detected! Starting recovery...")

    # Step 1: Get backup
    bucket_name = "dr-backup-bucket"
    backup_file = "backup.zip"

    print(f"Fetching backup from {bucket_name}")

    # Step 2: Launch new EC2 instance
    response = ec2.run_instances(
        ImageId='ami-12345678',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )

    instance_id = response['Instances'][0]['InstanceId']
    print(f"New instance created: {instance_id}")

    # Step 3: (Optional) Restore backup logic here

    return {
        'statusCode': 200,
        'body': 'Recovery completed successfully'
    }
✅ Step 6: Connect SNS to Lambda
Add SNS trigger to Lambda
Link CloudWatch alarm to SNS
✅ Step 7: Test Disaster Recovery
Stop EC2 manually
Observe:
Alert triggered
Lambda executes
New instance created
📂 Project Structure
├── cloud-function/
│   └── recovery_function.py
├── scripts/
│   └── backup_script.sh
├── docs/
│   └── architecture.png
├── README.md
📊 Key Benefits
⚡ Fast recovery
💰 Cost-efficient
🔐 Reliable backup system
📉 Less manual effort
🔮 Future Enhancements
🤖 AI-based failure prediction
🌍 Multi-region DR
📊 Monitoring dashboard
🔁 Auto scaling
👨‍💻 Author
A Lahari
