---
document: Deployment
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 1.0
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o responsable]
related_documents:
  - operations/01_operational_spec.md
  - operations/02_setup_guide.md
  - architecture/02_technical_design.md
---

# Deployment

## 1. Introducción

Este documento define la **estrategia de despliegue del sistema**, incluyendo:

- entornos de despliegue
- procedimientos de release
- gestión de versiones
- estrategias de rollback

Su objetivo es garantizar:

- despliegues reproducibles y controlados
- trazabilidad entre versiones y cambios
- capacidad de recuperación ante fallos de despliegue

Este documento no define:

- instalación inicial del entorno (ver `02_setup_guide.md`)
- operación continua (ver `01_operational_spec.md`)
- procedimientos de incidencia (ver `03_runbook.md`)

---

### Ejemplo

> El sistema se despliega en un entorno local controlado mediante un proceso manual versionado, con capacidad de rollback a la versión anterior.

---

## 2. Entornos

Definir los entornos en los que se despliega el sistema.

---

### 2.1 [Nombre del entorno]

- propósito:
- acceso:
- características:
- responsable:

---

### Ejemplo

### 2.1 Local (desarrollo)

- propósito: desarrollo y pruebas del desarrollador
- acceso: solo desarrollador
- características: datos sintéticos, sin restricciones de recursos
- responsable: desarrollador

### 2.2 Staging

- propósito: validación previa a producción
- acceso: equipo técnico
- características: datos reales anonimizados, restricciones similares a producción
- responsable: equipo técnico

### 2.3 Producción

- propósito: operación real del sistema
- acceso: restringido
- características: datos reales, configuración optimizada
- responsable: responsable de operaciones

---

## 3. Estrategia de Despliegue

Definir el enfoque general de despliegue del sistema.

---

### Tipos de despliegue

- despliegue completo
- despliegue incremental
- despliegue con feature flags

---

### Estrategia seleccionada

- tipo:
- justificación:
- restricciones:

---

### Ejemplo

- tipo: despliegue completo con parada del servicio
- justificación: sistema sin alta disponibilidad requerida
- restricciones: ventana de mantenimiento necesaria

---

## 4. Gestión de Versiones

Definir cómo se versionan y rastrean los despliegues.

---

### Formato de versión

- esquema:
- ejemplo:

---

### Ejemplo

- esquema: `MAJOR.MINOR.PATCH` (semver)
- ejemplo: `1.2.3`

---

### Relación versión — cambios

- dónde se documentan los cambios:
- criterios para incremento de versión:

---

### Ejemplo

| Incremento | Criterio |
| ---------- | -------- |
| MAJOR | cambios incompatibles en API o datos |
| MINOR | nuevas funcionalidades compatibles |
| PATCH | correcciones de errores |

---

### Artefactos de despliegue

- qué se despliega:
- cómo se empaqueta:
- dónde se almacena:

---

### Ejemplo

- código fuente versionado en git
- dependencias declaradas en `requirements.txt`
- configuración en archivos `.env` versionados por entorno

---

## 5. Procedimiento de Despliegue

Pasos para realizar un despliegue en cada entorno.

---

### 5.1 Pre-despliegue

Verificaciones obligatorias antes de desplegar.

- [ ] tests pasando en el entorno origen
- [ ] versión etiquetada en el repositorio
- [ ] backup del entorno destino realizado
- [ ] ventana de mantenimiento comunicada (si aplica)

---

### Ejemplo

```bash
# Verificar tests
run tests --all

# Etiquetar versión
git tag v1.2.3
git push origin v1.2.3
```

---

### 5.2 Despliegue

Pasos de ejecución del despliegue.

1. ...
2. ...
3. ...

---

### Ejemplo

```bash
# Parar sistema actual
run system --stop --graceful

# Actualizar código
git pull origin main

# Actualizar dependencias
pip install -r requirements.txt

# Aplicar migraciones (si aplica)
run system --migrate

# Arrancar sistema
run system --start
```

---

### 5.3 Post-despliegue

Verificaciones obligatorias tras el despliegue.

- [ ] sistema arrancado correctamente
- [ ] health checks pasando
- [ ] logs sin errores críticos
- [ ] smoke tests ejecutados

---

### Ejemplo

```bash
# Verificar estado
run system --health

# Ejecutar smoke tests
run tests --smoke
```

---

## 6. Estrategia de Rollback

Definir cómo revertir un despliegue fallido.

---

### Criterios de rollback

Condiciones que activan un rollback:

- ...

---

### Ejemplo

- health checks fallando tras despliegue
- tasa de errores superior al umbral definido
- pérdida de funcionalidad crítica detectada en smoke tests

---

### Procedimiento de rollback

1. ...
2. ...
3. ...

---

### Ejemplo

```bash
# Parar sistema actual
run system --stop

# Revertir a versión anterior
git checkout v1.2.2

# Restaurar dependencias
pip install -r requirements.txt

# Restaurar datos si aplica
run system --restore --from /backups/pre-deploy

# Arrancar sistema
run system --start
```

---

### Tiempo máximo de decisión

Definir en cuánto tiempo se debe decidir si hacer rollback:

- tiempo máximo tras despliegue para evaluar:
- responsable de la decisión:

---

### Ejemplo

- tiempo máximo: 30 minutos tras despliegue
- responsable: responsable técnico del despliegue

---

## 7. Configuración por Entorno

Definir cómo varía la configuración entre entornos.

---

### Variables de entorno por entorno

| Variable | Local | Staging | Producción |
| -------- | ----- | ------- | ---------- |
| `ENV` | `local` | `staging` | `production` |
| `LOG_LEVEL` | `debug` | `info` | `warning` |

---

### Gestión de secretos

- cómo se gestionan las credenciales:
- dónde se almacenan:
- quién tiene acceso:

---

### Ejemplo

- variables sensibles no versionadas en git
- almacenadas en archivo `.env` local no compartido
- acceso restringido al responsable del entorno

---

## 8. En el caso de utilizar IA / LLM (opcional)

Consideraciones específicas de despliegue para sistemas con modelos.

---

### Gestión de modelos

- cómo se versionan los modelos:
- cómo se despliegan:
- compatibilidad modelo — código:

---

### Ejemplo

- modelos versionados junto con el código que los consume
- verificación de compatibilidad antes del despliegue
- rollback del modelo junto con el código si falla

---

### Gestión de prompts

- los prompts forman parte del artefacto desplegable
- cambios de prompts siguen el mismo proceso de versioning que el código
- impacto de cambio de prompt debe evaluarse antes del despliegue

---

## 9. Trazabilidad de Despliegues

Mantener un registro de despliegues realizados.

---

### Registro de despliegues

| Versión | Fecha | Entorno | Responsable | Resultado | Notas |
| ------- | ----- | ------- | ----------- | --------- | ----- |
| 1.0.0 | [YYYY-MM-DD] | producción | [Rol] | ✅ OK | despliegue inicial |

---

## 10. Trazabilidad

| Elemento | Documento Relacionado |
| -------- | --------------------- |
| Requisitos del entorno | Operational Spec |
| Instalación inicial | Setup Guide |
| Procedimientos de incidencia | Runbook |
| Diseño técnico | Technical Design |

---

## Anexo. Notas de Coworking (IA Assistant)

### Contexto

Este documento define la estrategia y procedimientos de despliegue del sistema.

---

### Instrucciones

- no duplicar procedimientos de instalación inicial (ver Setup Guide)
- mantener procedimientos de rollback siempre actualizados
- cada despliegue debe quedar registrado en la sección 9
- los cambios de entorno deben reflejarse en la sección 7

---

### Riesgos

- procedimientos de rollback no probados
- configuración de entorno desincronizada
- despliegue sin backup previo
- falta de criterios claros de decisión de rollback

---

### Dudas abiertas

- ventanas de mantenimiento aceptables
- responsable de autorizar despliegues en producción
- estrategia de gestión de secretos a largo plazo

### Inputs utilizados

- ...


### Insights clave

- ...

