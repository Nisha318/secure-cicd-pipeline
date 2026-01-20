# Secure CI/CD Pipeline for Web Applications

[![Terraform](https://img.shields.io/badge/Terraform-1.0+-623CE4?logo=terraform&logoColor=white)](https://www.terraform.io/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Security](https://img.shields.io/badge/Security-First-green)](https://github.com/YOUR_USERNAME/secure-cicd-pipeline)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> A production-grade demonstration of security-first DevOps practices, implementing automated security scanning at every stage of the software delivery pipeline.

## 🎯 Project Overview

This project showcases end-to-end pipeline security with a Python Flask application deployed to AWS ECS Fargate through a fully automated CI/CD pipeline with integrated security controls.

**Live Demo:** [View Application](http://your-alb-url.amazonaws.com/api/info) *(infrastructure can be spun up on demand)*

## 🔒 Security Features

- **Secret Detection**: Pre-commit hooks with TruffleHog and git-secrets
- **SAST Analysis**: Bandit for Python security vulnerabilities
- **Dependency Scanning**: OWASP Dependency-Check for vulnerable libraries
- **Container Scanning**: Trivy for image vulnerability analysis
- **Infrastructure Scanning**: Checkov for Terraform security validation
- **Runtime Security**: Non-root containers, minimal attack surface, defense-in-depth networking

## 🏗️ Architecture
```
Developer → Pre-commit Hooks → GitHub Actions Pipeline
                                      ↓
                    [5 Security Scanning Stages]
                                      ↓
              AWS ECR → ECS Fargate → Application Load Balancer
                   ↓
            CloudWatch Logs & Metrics
```

### Infrastructure Components (46 AWS Resources)

- **Network**: Multi-AZ VPC with public/private subnet segmentation
- **Compute**: ECS Fargate with auto-scaling (CPU/Memory based)
- **Load Balancing**: Application Load Balancer with health checks
- **Container Registry**: ECR with image scanning enabled
- **Security**: IAM roles (least privilege), Security Groups, VPC Flow Logs
- **Monitoring**: CloudWatch Logs, Metrics, Alarms, and Dashboard

## 🚀 Quick Start

### Prerequisites

- Docker Desktop
- Python 3.11+
- AWS CLI configured
- Terraform 1.0+

### Local Development
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/secure-cicd-pipeline.git
cd secure-cicd-pipeline

# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Build and test locally
cd app
docker build -t secure-cicd-demo:local .
docker run -d --name test-app -p 8080:8080 -e ENVIRONMENT=development secure-cicd-demo:local

# Test endpoints
curl http://localhost:8080/health
curl http://localhost:8080/api/info

# Cleanup
docker stop test-app && docker rm test-app
```

### Deploy to AWS
```bash
# Navigate to terraform directory
cd terraform

# Initialize Terraform
terraform init

# Review planned changes
terraform plan

# Deploy infrastructure
terraform apply

# Get outputs (ECR URL, ALB URL, etc.)
terraform output
```

### Push Container to ECR
```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 

# Tag and push
docker tag secure-cicd-demo:local :latest
docker push :latest

# Update ECS service
aws ecs update-service --cluster secure-cicd-pipeline-cluster \
  --service secure-cicd-pipeline-service \
  --force-new-deployment
```

## 📊 Project Status

- [x] Application development with security best practices
- [x] Docker containerization with multi-stage builds
- [x] Pre-commit security hooks
- [x] Terraform infrastructure (46 resources)
- [x] AWS deployment and verification
- [ ] GitHub Actions pipeline (Phase 3 - In Progress)
- [ ] Automated security scanning
- [ ] Automated rollback on security findings

## 🛠️ Technology Stack

**Application**: Python 3.11, Flask 3.0, Gunicorn  
**Security Tools**: Trivy, Bandit, TruffleHog, OWASP Dependency-Check, Checkov  
**Infrastructure**: Terraform, AWS (VPC, ECS Fargate, ECR, ALB, CloudWatch)  
**CI/CD**: GitHub Actions *(coming in Phase 3)*  
**Monitoring**: CloudWatch Logs, Metrics, Alarms, Dashboards


## 🎓 Learning Outcomes

This project demonstrates:

1. **Security-First Design**: Defense-in-depth with multiple security layers
2. **Infrastructure as Code**: 100% Terraform, reproducible, version-controlled
3. **Cloud Architecture**: Multi-AZ, auto-scaling, high availability
4. **DevOps Practices**: CI/CD automation, containerization, monitoring
5. **Compliance**: VPC Flow Logs, CloudWatch monitoring, audit trails

## 📈 Key Metrics

- **46** AWS resources deployed via Terraform
- **5** security scanning stages in pipeline
- **2** availability zones for high availability
- **<100ms** application response time
- **Zero** hardcoded secrets in code

## 🔐 Security Highlights

- ✅ Non-root container execution
- ✅ Private subnets for application tier
- ✅ Security groups with least privilege
- ✅ IAM roles with minimal permissions
- ✅ VPC Flow Logs enabled
- ✅ CloudWatch monitoring and alarms
- ✅ Multi-layer vulnerability scanning
- ✅ Automated secret detection

## 📝 Blog Post

Read the detailed walkthrough: [Building a Secure CI/CD Pipeline](https://nishacloud.com/blog/secure-cicd-pipeline) *(coming soon)*

## 🤝 Contributing

This is a portfolio project, but suggestions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Nisha** - Cloud Security Engineer | GRC Engineer 
- LinkedIn: [linkedin.com/in/nishapmcd](https://linkedin.com/in/nishapmcd)
- Portfolio: [nishacloud.com](https://nishacloud.com)
- GitHub: [@nisha318](https://github.com/nisha318)


---

⭐ **If you find this project helpful, please consider giving it a star!**