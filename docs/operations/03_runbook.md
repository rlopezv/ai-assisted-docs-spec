---
document: Runbook
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

# Runbook

## 1. Introducción

Este documento define los **procedimientos operativos del sistema** para su operación continua y gestión de incidencias.

Su objetivo es:

- centralizar los procedimientos de operación rutinaria
- definir la respuesta ante incidencias conocidas
- permitir operación sin conocimiento previo del sistema

Este documento no define:

- requisitos del entorno (ver `01_operational_spec.md`)
- instalación inicial (ver `02_setup_guide.md`)
- diseño técnico (ver `02_technical_design.md`)

---

### Ejemplo

> Este runbook permite a cualquier operador arrancar, detener y recuperar el sistema ante las incidencias más comunes sin necesidad de consultar al equipo de desarrollo.

---

## 2. Procedimientos de Operación Rutinaria

Definir las operaciones habituales del sistema en producción.

---

### 2.1 Arranque del sistema

Pasos para iniciar el sistema desde cero.

- verificaciones previas al arranque:
- comando de inicio:
- verificación de arranque correcto:

---

### Ejemplo

```bash
# Verificar dependencias
check-dependencies

# Arrancar sistema
run system --start

# Verificar estado
run system --status
```

Resultado esperado:

- sistema en estado `running`
- logs de arranque sin errores

---

### 2.2 Parada controlada del sistema

Pasos para detener el sistema de forma segura.

- condiciones previas a la parada:
- comando de parada:
- verificación de parada correcta:

---

### Ejemplo

```bash
run system --stop --graceful
```

- esperar finalización de operaciones en curso
- verificar que no quedan procesos activos

---

### 2.3 Reinicio del sistema

Pasos para reiniciar el sistema.

- cuándo reiniciar:
- procedimiento:
- verificación post-reinicio:

---

### Ejemplo

- reinicio tras actualización de configuración
- reinicio ante degradación de rendimiento sostenida

---

### 2.4 Verificación de estado

Comprobaciones periódicas del estado del sistema.

- checks de salud:
- métricas a revisar:
- frecuencia recomendada:

---

### Ejemplo

```bash
run system --health
```

| Check | Valor esperado |
| ----- | -------------- |
| Estado general | `ok` |
| Cola de procesamiento | < 100 elementos |
| Tasa de error | < 1% |

---

## 3. Gestión de Incidencias

Definir la respuesta ante situaciones de error o degradación.

---

### 3.1 Clasificación de incidencias

| Severidad | Descripción | Tiempo de respuesta |
| --------- | ----------- | ------------------- |
| Crítica | sistema detenido o datos comprometidos | inmediato |
| Alta | degradación severa del servicio | < 1h |
| Media | degradación parcial o errores recurrentes | < 4h |
| Baja | comportamiento anómalo sin impacto directo | planificado |

---

### 3.2 Procedimiento general ante incidencia

1. Detectar y clasificar la incidencia
2. Registrar en el log de incidencias
3. Aplicar procedimiento específico (ver sección 4)
4. Verificar resolución
5. Documentar causa y solución

---

## 4. Procedimientos de Resolución

### 4.1 [Nombre de la incidencia]

Descripción:

- síntomas:
- causa probable:
- impacto:

Procedimiento:

1. ...
2. ...
3. ...

Verificación:

- ...

---

### Ejemplo

### 4.1 Saturación de recursos

Descripción:

- síntomas: latencia elevada, timeout en operaciones
- causa probable: concurrencia excesiva o fuga de memoria
- impacto: degradación del servicio

Procedimiento:

1. Verificar uso de recursos: `check-resources`
2. Reducir concurrencia activa
3. Reiniciar procesos afectados si persiste

Verificación:

- métricas de recursos vuelven a valores normales
- latencia recuperada

---

### 4.2 [Nombre de la incidencia]

(Repetir estructura)

---

## 5. Procedimientos de Escalado

Definir cuándo y cómo escalar una incidencia.

---

### Criterios de escalado

- incidencia no resuelta en el tiempo de respuesta definido
- impacto en datos o integridad del sistema
- causa desconocida

---

### Ejemplo

- escalar a equipo técnico si la incidencia es crítica y no se resuelve en 30 minutos
- escalar a responsable de producto si afecta a datos del cliente

---

## 6. Tareas de Mantenimiento Programado

Definir operaciones periódicas necesarias para la salud del sistema.

---

### Tareas periódicas

| Tarea | Frecuencia | Responsable |
| ----- | ---------- | ----------- |
| Limpieza de logs | semanal | [Rol] |
| Limpieza de temporales | diaria | [Rol] |
| Verificación de integridad | semanal | [Rol] |
| Revisión de métricas | diaria | [Rol] |

---

### Ejemplo

```bash
# Limpieza de archivos temporales
run system --cleanup --temp

# Compactación de base de datos
run system --maintenance --db
```

---

## 7. Gestión de Logs

Definir cómo consultar y gestionar los logs del sistema.

---

### Ubicación de logs

- logs de sistema:
- logs de errores:
- logs de operaciones:

---

### Consulta de logs

- cómo filtrar por nivel:
- cómo filtrar por fecha:
- cómo filtrar por componente:

---

### Ejemplo

```bash
# Ver últimos errores
tail -100 /logs/error.log

# Filtrar por nivel
grep "ERROR" /logs/system.log
```

---

### Rotación y retención

- política de retención:
- rotación automática:

---

## 8. Procedimientos de Backup y Recuperación

Definir cómo proteger y recuperar datos del sistema.

---

### Backup

- qué se respalda:
- frecuencia:
- ubicación:
- verificación:

---

### Ejemplo

```bash
run system --backup --output /backups/$(date +%Y%m%d)
```

---

### Recuperación

- procedimiento de restauración:
- verificación post-restauración:

---

### Ejemplo

```bash
run system --restore --from /backups/20260101
```

---

## 9. En el caso de utilizar IA / LLM (opcional)

Procedimientos específicos para sistemas con modelos de lenguaje.

---

### Gestión del modelo

- carga y descarga del modelo:
- verificación de disponibilidad:
- actualización del modelo:

---

### Incidencias específicas de LLM

| Incidencia | Síntoma | Procedimiento |
| ---------- | ------- | ------------- |
| Modelo no disponible | error en inferencia | recargar modelo |
| Outputs inválidos recurrentes | alta tasa de schema errors | revisar prompt y reiniciar |
| Saturación de VRAM | OOM en inferencia | reducir batch size o reiniciar |

---

## 10. Registro de Incidencias

Mantener un registro estructurado de incidencias para análisis posterior.

---

### Estructura del registro

| Campo | Descripción |
| ----- | ----------- |
| `fecha` | timestamp de detección |
| `severidad` | crítica / alta / media / baja |
| `descripción` | resumen del problema |
| `causa` | causa identificada |
| `solución` | procedimiento aplicado |
| `duración` | tiempo hasta resolución |

---

### Ejemplo

| Fecha | Severidad | Descripción | Causa | Solución | Duración |
| ----- | --------- | ----------- | ----- | -------- | -------- |
| 2026-01-15 | Alta | Saturación de memoria | fuga en módulo X | reinicio + fix | 45 min |

---

## 11. Trazabilidad

| Elemento | Documento Relacionado |
| -------- | --------------------- |
| Entorno y requisitos | Operational Spec |
| Instalación | Setup Guide |
| Diseño técnico | Technical Design |

---

## Anexo. Notas de Coworking (IA Assistant)

### Contexto

Este documento centraliza los procedimientos operativos del sistema.

---

### Instrucciones

- no duplicar información de la Operational Spec
- no incluir lógica de implementación
- mantener procedimientos reproducibles y verificables
- cada procedimiento debe tener criterio de verificación

---

### Riesgos

- procedimientos desactualizados respecto al sistema real
- falta de cobertura de incidencias comunes
- ausencia de criterios de escalado claros

---

### Dudas abiertas

- niveles de severidad y tiempos de respuesta aceptables
- propietario de cada procedimiento
- política de retención de logs

### Inputs utilizados

- ...


### Insights clave

- ...

