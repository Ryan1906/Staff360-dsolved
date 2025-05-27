from flask import jsonify
from src.models.vacaciones_model import Vacacion
from sqlalchemy.orm import Session
from datetime import date

def solicitar_vacacion(db: Session, id_empleado: int, fecha_inicio, fecha_fin, motivo):
    nueva_vacacion = Vacacion(
        id_empleado=id_empleado,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        motivo=motivo,
        fecha_solicitud=date.today()
    )
    db.add(nueva_vacacion)
    db.commit()
    db.refresh(nueva_vacacion)
    return jsonify({"mensaje": "Solicitud de vacaciones registrada", "id_vacacion": nueva_vacacion.id_vacacion}), 201