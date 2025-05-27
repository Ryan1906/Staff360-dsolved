from flask import Flask
from src.routes.vacaciones_route import vacaciones_bp

app = Flask(__name__)
app.register_blueprint(vacaciones_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)