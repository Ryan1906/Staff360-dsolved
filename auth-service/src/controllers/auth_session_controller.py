from controllers.auth_general_controller import PUBLIC_KEY, PRIVATE_KEY, ACCESS_TOKEN_VALIDITY, ALGORITHM
from flask import request, jsonify
from datetime import datetime, timezone
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

def validate_token(token: str, token_type: str):
    try:
        decoded = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
        return { "is_valid": True, "data": decoded }
    except ExpiredSignatureError:
        return { "is_valid": False, "error": f"{token_type} token has expired" }
    except InvalidTokenError:
        return { "is_valid": False, "error": f"Invalid {token_type} token" }

def decode_token(token_type: str):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None, jsonify({ "code": 401, "message": f"{token_type} token is missing or malformed"}), 401
    
    token = auth_header.split(" ")[1]
    validation = validate_token(token, token_type)

    if not validation["is_valid"]:
        return None, jsonify({ "code": 401, "message": validation["error"]}), 401

    return validation["data"], None, None

def test_token():
    token_data, error_response, status = decode_token("Access")
    if error_response:
        return error_response, status

    return jsonify({
        "message": "Acces token is valid",
        "token_data": token_data
    }), 200


def refresh_token():
    token_data, error_response, status = decode_token("Refresh")
    if error_response:
        return error_response, status

    now = datetime.now(timezone.utc)
    new_acces_token = jwt.encode({
        "user_id": token_data["user_id"],
        "username": token_data["username"],
        "role": token_data["role"],
        "iat": now,
        "exp": now + ACCESS_TOKEN_VALIDITY,
    }, PRIVATE_KEY, algorithm=ALGORITHM)

    return jsonify({
        "code": 0,
        "access_token": new_acces_token,
        "message": "New access token generated"
    }), 200