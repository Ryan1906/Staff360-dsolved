FROM python:3.11-slim

WORKDIR /app

# Instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos del proyecto
COPY . .

# Puerto como argumento
ARG PORT

# Exponemos el puerto (cambiar puerto segun microservicio)
EXPOSE ${PORT}

# Ejecutamos el servidor
CMD ["python", "src/server.py"]
