from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone
import os

# Importacion de blueprints
from routes.template_route import template_bp

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_env()

# Tiempo en que el microservicio se inicio
start_time = datetime.now(timezone.utc)

# Variables de entorno
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
PORT = int(os.getenv('PORT', 5000))
FLASK_ENV = os.getenv('FLASK_ENV', 'production').lower()

app = Flask(__name__)

CORS(app, origins='*')

# Indica si el servicio esta vivo (servicios que lo pueden utilizar: Kubernetes, Docker Swarm y ECS)
@app.route('/healthz', methods=['GET'])
def healthz():
    return jsonify({ "status": "alive"}), 200

# Devuelve un healthcheck basico 'pong' (servicios que lo pueden utilizar: Load Balancers, API Gateways, health checks)
@app.route('/ping', methods=['GET'])
def ping():
    return "pong", 200

# Devuelve la version del servicio (servicios que lo pueden utilizar: sistemas CI/CD, interfaces de monitoreo)
@app.route('/version', methods=['GET'])
def version():
    return jsonify({
        "version": APP_VERSION
    }), 200

# Indica el estado del microservicio (servicios que lo pueden utilizar: Azure App Service, Heroku, GCP AppEngine)
@app.route('/status', methods=['GET'])
def status():
    now = datetime.now(timezone.utc)
    uptime = now - start_time

    return jsonify({
        "status": "OK",
        "message": "service is running",
        "uptime": str(uptime),
        "started_at": start_time.isoformat() + "Z"
    }), 200



# En este espacio van los registros de los blueprints creados
app.register_blueprint(template_bp)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    print(f"Microservice running on port {port}")
    app.run(
        host='0.0.0.0',
        port=port, 
        debug=FLASK_ENV == 'development'
    )