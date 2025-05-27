from flask import Blueprint, request, jsonify
from services.db_service import SessionLocal
from controllers.auth_login_controller import login_user
from controllers.auth_register_controller import register_user
from controllers.auth_session_controller import test_token, refresh_token
from datetime import datetime, timezone
import jwt

prefix = '/auth'
auth_bp = Blueprint('auth_blueprint', __name__, url_prefix=prefix)

@auth_bp.route('/register', methods=['POST'])
def register_user_route():
    db = SessionLocal()
    try:
        data = request.json
        username = data.get("username")
        nombres = data.get("nombres")
        apellidos = data.get("apellidos")
        password = data.get("password")
        email = data.get("email")
        direccion = data.get("direccion")
        telefono = data.get("telefono")
        rol = data.get("rol")
        return register_user(
            db,
            username,
            nombres,
            apellidos,
            password,
            email,
            direccion,
            telefono,
            rol
        )

    finally:
        db.close()

@auth_bp.route('/login', methods=['POST'])
def login_user_route():
    db = SessionLocal()
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")
        
        if not username or not password:
            return { "error": "Se requieren username y password" }, 400
        
        return login_user(db, username, password)
    finally:
        db.close()

@auth_bp.route('/test_token', methods=['POST'])
def test_token_route():
    return test_token()

@auth_bp.route('/refresh_token', methods=['POST'])
def refresh_token_route():
    return refresh_token()
