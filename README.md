# Secure Container Infrastructure with Automated Deployment Pipeline

[![Terraform](https://img.shields.io/badge/Terraform-1.0+-623CE4?logo=terraform&logoColor=white)](https://www.terraform.io/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Security](https://img.shields.io/badge/Security-First-green)](https://github.com/YOUR_USERNAME/secure-cicd-pipeline)

> Production-grade AWS infrastructure and automated deployment pipeline implementing security-first DevOps practices with multi-stage vulnerability scanning.

## 🎯 Overview

This project implements a complete secure deployment workflow for containerized applications on AWS ECS Fargate. The infrastructure follows AWS Well-Architected Framework principles with defense-in-depth security controls, while the CI/CD pipeline enforces security gates at every stage of the software delivery lifecycle.

## 🔒 Security Features

### Infrastructure Security
- **Network Segmentation**: Multi-AZ VPC with isolated public/private subnets
- **Defense in Depth**: Security groups, NACLs, VPC Flow Logs
- **Least Privilege IAM**: Separate execution and task roles with minimal permissions
- **Container Security**: Non-root execution, minimal base images, image scanning
- **Monitoring**: CloudWatch Logs, Metrics, Alarms, and VPC Flow Logs

### Pipeline Security (Phase 3 - In Development)
- **Secret Detection**: Pre-commit hooks and pipeline scanning with TruffleHog
- **SAST Analysis**: Bandit for Python vulnerability detection
- **Dependency Scanning**: OWASP Dependency-Check for vulnerable libraries
- **Container Scanning**: Trivy for image vulnerability analysis
- **IaC Security**: Checkov for Terraform misconfigurations
- **Automated Rollback**: Deployment fails on security findings

## 🏗️ Architecture
```
Developer → Security Hooks → GitHub Actions Pipeline
                                      ↓
                        [Security Scanning Gates]
                                      ↓
                  AWS ECR → ECS Fargate → ALB
                       ↓
              CloudWatch Monitoring
```

### Infrastructure Components

**Deployed Resources: 46 AWS components managed via Terraform**

- **Network Layer**: Multi-AZ VPC, public/private subnets, NAT Gateways, Internet Gateway
- **Compute Layer**: ECS Fargate cluster with auto-scaling (CPU/Memory thresholds)
- **Load Balancing**: Application Load Balancer with health checks and target groups
- **Container Registry**: ECR with lifecycle policies and scan-on-push enabled
- **Identity & Access**: IAM roles and policies following least privilege
- **Observability**: CloudWatch log groups, metric alarms, dashboards, VPC Flow Logs
- **Security**: Security groups restricting traffic flows, VPC Flow Logs for audit

## 🚀 Deployment

### Prerequisites

- AWS CLI configured with appropriate credentials
- Terraform 1.0+
- Docker Desktop
- Python 3.11+

### Infrastructure Deployment
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/secure-cicd-pipeline.git
cd secure-cicd-pipeline

# Deploy infrastructure
cd terraform
terraform init
terraform plan
terraform apply

# Capture outputs
terraform output
```

### Application Deployment
```bash
# Build container
cd app
docker build --platform linux/amd64 -t secure-cicd-demo:latest .

# Authenticate to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin 

# Tag and push
docker tag secure-cicd-demo:latest :latest
docker push :latest

# Deploy to ECS
aws ecs update-service \
  --cluster secure-cicd-pipeline-cluster \
  --service secure-cicd-pipeline-service \
  --force-new-deployment
```

### Local Development
```bash
# Install security hooks
pip install pre-commit
pre-commit install

# Build and test locally
cd app
docker build --platform linux/amd64 -t secure-cicd-demo:local .
docker run -d --name test-app -p 8080:8080 \
  -e ENVIRONMENT=development \
  secure-cicd-demo:local

# Test endpoints
curl http://localhost:8080/health
curl http://localhost:8080/api/info
curl http://localhost:8080/metrics

# Cleanup
docker stop test-app && docker rm test-app
```

## 📊 Implementation Status

- [x] Security-hardened Flask application
- [x] Multi-stage Docker containerization
- [x] Pre-commit security hooks (TruffleHog, Bandit, git-secrets)
- [x] Terraform infrastructure (46 resources)
- [x] Multi-AZ VPC with network segmentation
- [x] ECS Fargate with auto-scaling
- [x] Application Load Balancer
- [x] CloudWatch monitoring and alarms
- [ ] GitHub Actions CI/CD pipeline (In Development)
- [ ] Automated security scanning gates
- [ ] Integration testing suite


## 🛠️ Technology Stack

**Application**: Python 3.11, Flask 3.0, Gunicorn, prometheus-client  
**Infrastructure**: Terraform, AWS (VPC, ECS Fargate, ECR, ALB, CloudWatch)  
**Security**: Trivy, Bandit, TruffleHog, OWASP Dependency-Check, Checkov  
**CI/CD**: GitHub Actions (In Development)  
**Monitoring**: CloudWatch Logs, Metrics, Alarms, Dashboards

## 📈 Key Metrics

- **46** AWS resources deployed via Infrastructure as Code
- **Multi-AZ** deployment across 2 availability zones
- **Auto-scaling** based on CPU and memory utilization
- **5-layer** security scanning in pipeline
- **Zero** hardcoded credentials or secrets

## 🔐 Security Implementations

✅ Container runs as non-root user (UID 1000)  
✅ Application tier in private subnets with NAT Gateway egress  
✅ Security groups enforce least-privilege network access  
✅ IAM roles scoped to minimal required permissions  
✅ VPC Flow Logs enabled for network monitoring  
✅ CloudWatch alarms on resource utilization thresholds  
✅ Secrets managed via environment variables (production: AWS Secrets Manager)  
✅ Multi-stage Docker builds minimize attack surface  

## 📝 API Endpoints

- `GET /health` - Health check for load balancer target groups
- `GET /api/info` - Application information and security features
- `GET /api/secure-data` - Demonstrates secure data handling patterns
- `GET /metrics` - Prometheus-compatible metrics endpoint


## 👤 Contact

**Nisha** - Senior Cybersecurity Engineer/ISSE  
[LinkedIn](https://linkedin.com/in/nishapmcd) • [Portfolio](https://nishacloud.com) • [GitHub](https://github.com/nisha318)

---

*Enterprise-grade infrastructure implementing AWS Well-Architected Framework security principles*