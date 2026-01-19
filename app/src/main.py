"""
Secure CI/CD Pipeline Demo Application
A simple Flask API demonstrating security best practices
"""

import os
import logging
from flask import Flask, jsonify, request
from pythonjsonlogger import jsonlogger
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

# Configure structured logging
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

app = Flask(__name__)

# Prometheus metrics
request_counter = Counter('app_requests_total', 'Total requests', ['method', 'endpoint', 'status'])

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for ALB target group"""
    request_counter.labels(method='GET', endpoint='/health', status=200).inc()
    return jsonify({
        'status': 'healthy',
        'service': 'secure-cicd-demo',
        'version': os.getenv('APP_VERSION', '1.0.0')
    }), 200

@app.route('/api/info', methods=['GET'])
def get_info():
    """Return application information"""
    request_counter.labels(method='GET', endpoint='/api/info', status=200).inc()
    
    info = {
        'application': 'Secure CI/CD Pipeline Demo',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'security_features': [
            'Container vulnerability scanning',
            'SAST analysis',
            'Dependency checking',
            'IaC security scanning',
            'Secret detection'
        ]
    }
    
    logger.info('Info endpoint accessed', extra={'endpoint': '/api/info'})
    return jsonify(info), 200

@app.route('/api/secure-data', methods=['GET'])
def get_secure_data():
    """Demonstrate secure data handling"""
    # Example: No hardcoded secrets, use environment variables
    api_key = os.getenv('API_KEY')  # Would come from AWS Secrets Manager in production
    
    if not api_key:
        request_counter.labels(method='GET', endpoint='/api/secure-data', status=500).inc()
        logger.error('API key not configured')
        return jsonify({'error': 'Configuration error'}), 500
    
    request_counter.labels(method='GET', endpoint='/api/secure-data', status=200).inc()
    
    # Don't log sensitive data
    logger.info('Secure data accessed', extra={'endpoint': '/api/secure-data'})
    
    return jsonify({
        'message': 'Secure data access successful',
        'timestamp': request.headers.get('X-Request-Time')
    }), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.errorhandler(404)
def not_found(error):
    request_counter.labels(method=request.method, endpoint=request.path, status=404).inc()
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    request_counter.labels(method=request.method, endpoint=request.path, status=500).inc()
    logger.error('Internal server error', extra={'error': str(error)})
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Don't use debug mode in production
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 8080)),
        debug=False
    )