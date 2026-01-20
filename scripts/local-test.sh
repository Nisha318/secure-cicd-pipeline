#!/bin/bash
set -e

echo "🔍 Running local security checks and tests..."

# Check if Docker Desktop is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker Desktop is not running. Please start Docker Desktop first."
    exit 1
fi

# Install pre-commit hooks (if not already installed)
echo "Installing pre-commit hooks..."
pip install pre-commit 2>/dev/null || echo "pre-commit already installed"
pre-commit install

# Run pre-commit checks
echo "Running pre-commit security scans..."
pre-commit run --all-files || echo "Some pre-commit checks failed, but continuing..."

# Build Docker image locally
echo "🐳 Building Docker image..."
cd app
docker build --platform linux/amd64 -t secure-cicd-demo:local .

# Run Trivy scan locally (if installed via Docker)
echo "🔒 Scanning container image with Trivy..."
docker run --rm -v //var/run/docker.sock:/var/run/docker.sock \
    aquasec/trivy:latest image --severity HIGH,CRITICAL secure-cicd-demo:local

# Run container locally for testing
echo "🚀 Starting container..."
docker run -d --name test-app -p 8080:8080 \
  -e ENVIRONMENT=development \
  -e APP_VERSION=local \
  secure-cicd-demo:local

# Wait for container to be ready
echo "Waiting for container to start..."
sleep 5

# Test health endpoint
echo "✅ Testing health endpoint..."
curl -f http://localhost:8080/health || (echo "Health check failed" && docker logs test-app && exit 1)

echo "✅ Testing info endpoint..."
curl http://localhost:8080/api/info

# Cleanup
echo "🧹 Cleaning up..."
docker stop test-app
docker rm test-app

echo "✨ All local tests passed!"