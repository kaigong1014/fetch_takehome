# ETL Pipeline Project

## Overview
This project reads JSON data from an AWS SQS Queue, masks PII fields, and writes the data to a Postgres database.

## Setup
1. Clone the repository.
2. Ensure Docker and Docker Compose are installed.
3. Run the following command to start the services:
   ```bash
   docker-compose up

##How would you deploy this application in production?
Deploy using Docker containers for the ETL application, AWS SQS, and AWS RDS for Postgres. Utilize Kubernetes for orchestration to manage scaling, health checks, and deployments. Implement a CI/CD pipeline to automate testing, building, and deployment. Use environment variables and secrets management tools like AWS Secrets Manager for secure configuration. Ensure proper monitoring and logging with AWS CloudWatch or similar tools.

##What other components would you want to add to make this production ready?
Add logging (CloudWatch, ELK stack) and monitoring (Prometheus, Grafana) for visibility. Implement robust error handling and retry mechanisms. Include health checks using readiness and liveness probes. Set up automated backups for the database and ensure secure data handling through IAM roles and encryption. Validate input data and optimize performance for high throughput and large datasets.

##How can this application scale with a growing dataset?
Scale horizontally by adding more ETL instances to process SQS messages in parallel. Use AWS RDS Read Replicas to handle increased read traffic. Implement batch processing for SQS messages to reduce interaction frequency. Consider database partitioning or sharding if necessary. Archive old data to AWS S3 to manage storage costs and improve database performance.

##How can PII be recovered later on?
Use encryption (e.g., AES-256) instead of hashing for PII fields to allow for reversible masking. Store and manage encryption keys securely using AWS KMS. Rotate keys regularly and maintain audit logs for key usage and access to encrypted PII. Ensure compliance with data protection regulations by controlling and monitoring access to encryption keys.

##What are the assumptions you made?
Assume JSON messages from SQS follow a consistent schema. The provided user_logins table schema is sufficient. PII masking does not require reversibility for this use case; hashing is acceptable for deduplication. SQS and Postgres are reliable and can handle the expected load. Development and production environments are similar, minimizing deployment discrepancies.






