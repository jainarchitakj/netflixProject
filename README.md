# 🚀 ISS Tracker – AWS Lambda + RDS PostgreSQL (Serverless VPC Project)
A secure, serverless data pipeline that tracks the real-time location of the International Space Station (ISS) every minute using AWS Lambda and stores the data in a PostgreSQL database hosted on Amazon RDS. All components run inside a private network using AWS VPC with NAT Gateway and subnet routing.

---

## ✨ Features
- Fetches real-time ISS coordinates from a public API

- Stores latitude, longitude, timestamp, and message into PostgreSQL table

- Triggered automatically every 1 minute using Amazon EventBridge

- Lambda is deployed inside a private subnet (no public access)

- Internet access enabled via NAT Gateway (secure outbound only)

- End-to-end setup follows real-world VPC architecture and IAM security

---

## 🎯 Objective
To build a production-like, serverless architecture in AWS that:

- Collects real-time data from a public API

- Runs on automation without any manual trigger

- Stores data in a private PostgreSQL database (Amazon RDS)

- Uses secure networking practices with private subnets and NAT

---

## 🏗️ Architecture Overview

![aws lambda architecture](https://github.com/user-attachments/assets/464e90bc-2a1b-4b8a-aa7d-169e0af4a75c)


- Custom VPC with 3 subnets (2 public, 1 private)

- Internet Gateway (IGW) is attached to the VPC

- NAT Gateway is deployed in a public subnet

Route Tables are created:

- Public subnet → Internet Gateway

- Private subnet → NAT Gateway

- Amazon RDS (PostgreSQL) is launched inside the private subnet

- AWS Lambda is deployed in the private subnet (no public IP)

- Amazon EventBridge triggers the Lambda every 1 minute

- Lambda function fetches ISS data and stores it into PostgreSQL

--

## 🛠️ Tech Stack

| Tool/Service    | Purpose                                            |
|-----------------|----------------------------------------------------|
| AWS Lambda      | Executes Python code to fetch & store data         |
| Amazon RDS      | PostgreSQL database to store ISS coordinates       |
| Amazon VPC      | Custom network with public/private subnets         |
| NAT Gateway     | Allows secure internet access for private Lambda   |
| Internet Gateway| Enables internet access for public subnets         |
| EventBridge     | Scheduled trigger every 1 minute                   |
| urllib          | Fetches data from public ISS tracking API          |
| psycopg2        | Python PostgreSQL connector                        |
	
--

## 🧱 Database Schema
CREATE TABLE IF NOT EXISTS iss_position (
  id SERIAL PRIMARY KEY,
  latitude INTEGER,
  longitude INTEGER,
  timestamp INTEGER,
  message VARCHAR(255)
);

--

## 📂 Project Structure
iss-tracker-lambda/
│
- ├── lambda_function.py       # Main Lambda logic
- ├── README.md                # Project documentation
- ├── screenshots/             # (Optional) Architecture diagrams and logs

--

## 🔁 Data Flow

### 📥 Extract
- EventBridge triggers the Lambda function every 1 minute
- Lambda uses urllib to call the public ISS API:
- http://api.open-notify.org/iss-now.json

### 🔧 Transform
- Extracts fields: latitude, longitude, timestamp, message
- Ensures table exists in RDS before inserting

### 📤 Load
- Inserts each new row into the iss_position table in RDS PostgreSQL

--- 

## 🔐 VPC & Network Design

| Component        | Purpose / Configuration                                             |
| ---------------- | ------------------------------------------------------------------- |
| VPC              | Custom VPC created in ap-south-1 (Mumbai) region                    |
| Subnets          | 2 Public subnets and 1 Private subnet                               |
| Internet Gateway | Attached to VPC for public subnet internet access                   |
| NAT Gateway      | In public subnet to allow private subnet to access the internet     |
| Route Tables     | Public subnets → IGW<br>Private subnet → NAT Gateway                |
| Lambda           | Deployed inside private subnet (no public IP)                       |
| RDS PostgreSQL   | Hosted inside private subnet (not publicly exposed to the internet) |
| Security Groups  | Allows Lambda to access RDS on port 5432                            |


### ⚙️ Deployment Steps
### Create a custom VPC with 3 subnets
- 2 Public subnets
- 1 Private subnet

### Attach an Internet Gateway to the VPC
- Enables public subnet connectivity to the internet.

### Create a NAT Gateway in one of the public subnets
- Allows private subnet resources (Lambda) to make outbound internet calls.

### Create 2 Route Tables
- Public subnets → 0.0.0.0/0 via Internet Gateway
- Private subnet → 0.0.0.0/0 via NAT Gateway

### Launch Amazon RDS PostgreSQL in the private subnet
- Disable public access.

### Deploy the Lambda function in the private subnet
- Attach to the same VPC as the RDS instance.

### Create an IAM Role with permissions for
- VPC access
- RDS connectivity
- CloudWatch logs

### Create an EventBridge rule to trigger Lambda every 1 minute
- Schedule expression: `rate(1 minute)`

### Monitor data
- Use pgAdmin, DBeaver, or any SQL client.

---

### 📊 Screenshots / Diagram
- **Folder:** `screenshots/`

---

### 🧪 Learnings / Highlights
- Built a fully secure VPC-based serverless app in AWS.
- Used Lambda in a private subnet with NAT Gateway for outbound access.
- Practiced IAM role assignment, NAT Gateway, and route table configuration.
- Implemented automated ETL workflow using EventBridge + Lambda.
- Gained hands-on experience in API integration with RDS PostgreSQL.



