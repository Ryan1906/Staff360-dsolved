from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta, timezone
from models import user_model
import jwt
import sys
from utils.logger_config import setup_logger

logger = setup_logger(__name__)

private_key_path = "keys/private.pem"
public_key_path = "keys/public.pem"

try:
    with open(private_key_path, "rb") as file:
        PRIVATE_KEY = file.read()
except FileNotFoundError:
    logger.error(f"Private key file is not present at {private_key_path}")
    sys.exit(3)

try:
    with open(public_key_path, "rb") as file:
        PUBLIC_KEY = file.read()
except FileNotFoundError:
    logger.error(f"Public key file is not present at {public_key_path}")
    sys.exit(3)

# CONSTANTES
ALGORITHM = "ES256"
ACCESS_TOKEN_VALIDITY = timedelta(minutes=10)
REFRESH_TOKEN_VALIDITY = timedelta(days=7)

def check_user_exists(db: Session, username: str):
    try:
        user = db.query(user_model).filter(user_model.username == username).first()
        return user if user is not None else None
    except SQLAlchemyError as err:
        logger.error("Error retrieving user while checking its existence check_user_exists", exc_info=err)
        return False

def generate_tokens(user_id: str, username: str, role: str) -> str:
    now = datetime.now(timezone.utc)

    access_payload = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "exp": now + ACCESS_TOKEN_VALIDITY,
        "iat": now
    }

    refresh_payload = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "exp": now + REFRESH_TOKEN_VALIDITY,
        "iat": now
    }

    access_token = jwt.encode(access_payload, PRIVATE_KEY, algorithm=ALGORITHM)
    refres_token = jwt.encode(refresh_payload, PRIVATE_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refres_token
    }
