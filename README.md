# NOMBRE DEL MICROSERVICIO
Manera en la que se estara trabajando el ejecutar los contenedores.

**Correr contenedor**: nombre del microservicio
```bash
docker run -d \
  -p 5000:5000 \
  -e APP_VERSION="X.X.X" \
  -e PORT=5000 \
  -e FLASK_ENV=development \
  --name <nombre-imagen>-container \
  <nombre-imagen>
```
**Ejemplo**
```bash
docker run -d \
 -p 5001:5001
 -e APP_VERSION="1.0.0" \
 -e PORT=5001 \
 -e FLASK_ENV=development \
 --name template-backend-container \
 template-backend
 ```
