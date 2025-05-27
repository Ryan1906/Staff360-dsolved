from sqlalchemy import Column, Integer, String, Text
from services.db_service import Base

class user_model(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    password = Column(Text, nullable=False)
    email = Column(String(100))
    direccion = Column(String(255))
    telefono = Column(String(15))
    rol = Column(String(50))
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "email": self.email,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "role": self.rol
        }