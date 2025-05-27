from flask import Blueprint, request
from src.controllers.vacaciones_controller import solicitar_vacacion
from src.services.db_service import get_db

vacaciones_bp = Blueprint("vacaciones", __name__)

@vacaciones_bp.route("/vacaciones", methods=["POST"])
def crear_vacacion():
    db = next(get_db()) 
    data = request.json
    return solicitar_vacacion(
        db,
        data["id_empleado"],
        data["fecha_inicio"],
        data["fecha_fin"],
        data.get("motivo", "")
    )

