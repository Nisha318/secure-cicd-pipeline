# Secure CI/CD Pipeline for Web Applications

A production-grade demonstration of security-first DevOps practices, implementing automated security scanning at every stage of the software delivery pipeline.

## 🎯 Project Overview

This project showcases end-to-end pipeline security with a Python Flask application deployed to AWS ECS Fargate through a fully automated CI/CD pipeline with integrated security controls.

## 🔒 Security Features

- **Secret Detection**: Pre-commit hooks with TruffleHog and git-secrets
- **SAST Analysis**: Bandit for Python security scanning
- **Dependency Scanning**: OWASP Dependency-Check for vulnerable libraries
- **Container Scanning**: Trivy for image vulnerability analysis
- **Infrastructure Scanning**: Checkov for Terraform security validation
- **Runtime Security**: Non-root containers, minimal attack surface

## 🏗️ Architecture
```
Developer → Pre-commit Hooks → GitHub Actions Pipeline
                                      ↓
                    [Security Scanning Stages]
                                      ↓
                    AWS ECR → ECS Fargate → ALB
```

## 🚀 Quick Start

### Prerequisites
- Docker Desktop
- Python 3.11+
- AWS CLI configured
- Terraform

### Local Testing
```bash
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

## 📊 Project Status

- [x] Application development with security best practices
- [x] Docker containerization with multi-stage builds
- [x] Pre-commit security hooks
- [ ] Terraform infrastructure (In Progress)
- [ ] GitHub Actions pipeline
- [ ] AWS deployment

## 🛠️ Technology Stack

**Application**: Python, Flask, Gunicorn  
**Security**: Trivy, Bandit, TruffleHog, OWASP Dependency-Check, Checkov  
**Infrastructure**: Terraform, AWS (VPC, ECS Fargate, ECR, ALB)  
**CI/CD**: GitHub Actions  

## 📝 License

This is a portfolio project for demonstration purposes.

## 👤 Author

Nisha - Cloud Security Engineer 
[LinkedIn](https://linkedin.com/in/nishapmcd) | [Portfolio](https://nishacloud.com)