from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Cloud Portfolio Project',
        'hostname': socket.gethostname(),
        'version': '1.0'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/info')
def info():
    return jsonify({
        'app': 'Portfolio Web API',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'region': os.getenv('AWS_REGION', 'unknown')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
