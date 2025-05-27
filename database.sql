CREATE DATABASE IF NOT EXISTS staff360;
USE staff360;

-- Tabla: empleados
CREATE TABLE empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    puesto VARCHAR(100),
    departamento VARCHAR(100),
    fecha_contratacion DATE,
    fecha_nacimiento DATE,
    estado ENUM('activo', 'suspendido', 'inactivo') DEFAULT 'activo',
    usuario VARCHAR(50) UNIQUE,
    contraseña VARCHAR(255)
);

-- Tabla: asistencia
CREATE TABLE asistencia (
    id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    fecha DATE,
    hora_entrada TIME,
    hora_salida TIME,
    tipo_registro VARCHAR(50),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE
);

-- Tabla: vacaciones
CREATE TABLE vacaciones (
    id_vacacion INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    estado ENUM('pendiente', 'aprobada', 'rechazada') DEFAULT 'pendiente',
    motivo TEXT,
    fecha_solicitud DATE,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE
);

-- Tabla: incapacidades
CREATE TABLE incapacidades (
    id_incapacidad INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    motivo TEXT,
    estado ENUM('pendiente', 'aprobada', 'rechazada') DEFAULT 'pendiente',
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE
);

-- Tabla: permisos
CREATE TABLE permisos (
    id_permiso INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    motivo TEXT,
    tipo VARCHAR(50),
    estado ENUM('pendiente', 'aprobado', 'rechazado') DEFAULT 'pendiente',
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE
);

-- Tabla: evaluaciones
CREATE TABLE evaluaciones (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    fecha DATE,
    evaluador VARCHAR(100),
    puntaje DECIMAL(5,2),
    comentarios TEXT,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE
);

-- Tabla: bonos
CREATE TABLE bonos (
    id_bono INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    tipo VARCHAR(50),
    monto DECIMAL(10,2),
    fecha_generado DATE,
    justificacion TEXT,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE
);

-- Tabla: contratos
CREATE TABLE contratos (
    id_contrato INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    tipo_contrato VARCHAR(50),
    fecha_inicio DATE,
    fecha_fin DATE,
    estado ENUM('activo', 'por vencer', 'renovado', 'vencido') DEFAULT 'activo',
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE
);

-- Tabla: usuarios
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE,
    contraseña VARCHAR(255),
    rol ENUM('admin', 'gerente', 'rrhh', 'empleado') DEFAULT 'empleado'
);

-- Tabla: logs (auditoría)
CREATE TABLE logs (
    id_log INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    accion VARCHAR(100),
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    descripcion TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE SET NULL
);
