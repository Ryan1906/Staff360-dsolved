from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.user_model import user_model
from utils.utils import generate_hash
from controllers.auth_general_controller import check_user_exists
from utils.logger_config import setup_logger
from flask import jsonify

logger = setup_logger(__name__)

def register_user(
        db: Session, 
        username: str, 
        nombres: str,
        apellidos: str,
        password: str, 
        email: str, 
        direccion: str, 
        telefono: str, 
        role:str
    ):
    try:
        if check_user_exists(db, username):
            logger.warning("User already exists")
            return jsonify({ "message": "El usuario ya existe"}), 409

        hashed_password = generate_hash(password)
        new_user = user_model(
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            password=hashed_password,
            email=email,
            direccion=direccion,
            telefono=telefono,
            rol=role,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logger.info(f"Usuario {username} registrado exitosamente")

        return jsonify({ "message": "Usuario creado", "user_id": new_user.id }), 201
    except SQLAlchemyError as err:
        db.rollback()
        logger.error("Error registrando usuario", exc_info=err)

        return jsonify({ "message": "Error interno" }), 500
