from sqlalchemy import Column, Integer, Date, Enum, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vacacion(Base):
    __tablename__ = "vacaciones"
    id_vacacion = Column(Integer, primary_key=True, autoincrement=True)
    id_empleado = Column(Integer, ForeignKey("empleados.id_empleado", ondelete="CASCADE"))
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    estado = Column(Enum("pendiente", "aprobada", "rechazada"), default="pendiente")
    motivo = Column(Text)
    fecha_solicitud = Column(Date)
