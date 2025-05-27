# STAFF360

Convenciones para el uso de commits (no es necesario, aporta mayor legibilidad).

### Tipos validos para commits

| Tipo       | Descripcion                                           |
|------------|--------------------------------------------------------|
| `feat`     | Agregar una nueva funcionalidad                        |
| `fix`      | Corregir un error o bug                                |
| `refactor` | Reestructurar codigo sin cambiar su comportamiento     |
| `docs`     | Cambios relacionados con documentacion                 |
| `test`     | Agregar o modificar pruebas                            |
| `chore`    | Tareas generales (build, configuración, limpieza, etc) |
| `perf`     | Mejoras de rendimiento                                 |
| `ci`       | Cambios en integracion continua                        |
| `build`    | Cambios en el sistema de build o dependencias          |

Formato: `<tipo>/<servicio> - <descripcion corta con verbo en infinitivo>`


### 📌 Ejemplos

```bash
feat/auth - agregar soporte para tokens JWT
fix/orders - corregir error al cancelar ordenes pendientes
refactor/payments - simplificar logica de redondeo
docs/common-libs - documentar funciones reutilizables
test/auth - agregar pruebas unitarias al endpoint de login
chore/ci - configurar validacion de convenciones de commits
```