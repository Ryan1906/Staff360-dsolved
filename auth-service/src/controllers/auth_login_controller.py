from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.user_model import user_model
from utils.utils import verify_hash
from controllers.auth_general_controller import generate_tokens
from utils.logger_config import setup_logger
from flask import jsonify

logger = setup_logger(__name__)

def login_user(db: Session, username: str, password: str):
    try:
        user = db.query(user_model).filter_by(username=username).first()

        if not user:
            logger.warning(f"Intento de login con usuario inexistente: {username}")
            return jsonify({ "error": "Usuario no encontrado"}), 404

        if not verify_hash(password, user.password):
            logger.warning(f"Password incorrecto para usuario: {username}")
            return jsonify({ "error": "Credenciales invalidas"}), 401

        tokens = generate_tokens(str(user.id), user.username, user.rol)

        logger.info(f"Usuario {username} inicio sesion correctamente")

        return jsonify({
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
            "user": {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "role": user.rol,
            }
        }), 200
    except Exception as e:
        logger.error("Error al iniciar sesion", exc_info=True)
        return jsonify({ "error": "Error interno del servidor" }), 500


