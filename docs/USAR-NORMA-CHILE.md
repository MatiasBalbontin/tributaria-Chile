# Guía de Uso NORMA-CHILE para Skills y Agentes

**NORMA-CHILE** es una base de datos centralizada de normativa tributaria chilena diseñada para ser consultada por skills de IA (como `tributario-marco`) y agentes de análisis.

---

## Acceso Rápido a Normativa

### 1. Búsqueda por Tributo

**Archivo:** `index/por-tributo.json`

```python
import json

# Cargar catálogo por tributo
with open('index/por-tributo.json', 'r') as f:
    tributos = json.load(f)

# Acceder a documentos sobre impuesto a la renta
renta_docs = tributos['impuesto-renta']

for doc in renta_docs:
    print(f"{doc['nombre']}")
    print(f"  Fuente: {doc['fuente']}")
    print(f"  Path: {doc['path']}")
    print(f"  Artículos: {', '.join(doc['articulos'])}")
```

### 2. Buscar Artículos Relacionados

**Archivo:** `index/cross-references.json`

```python
# Encontrar qué artículos están relacionados
with open('index/cross-references.json', 'r') as f:
    referencias = json.load(f)

# Ejemplo: ¿Qué está relacionado con Art. 17 (Renta Líquida)?
art_17 = referencias['articulo-17-lir']

print(f"Artículo: {art_17['nombre']}")
print(f"Relacionado con: {art_17['relacionado-con']}")
print(f"Tributos afectados: {art_17['tributos']}")
print(f"Path al documento: {art_17['path']}")
```

### 3. Catálogo Completo

**Archivo:** `index/metadata-completo.json`

Contiene estadísticas globales, total de documentos, y metadata consolidada.

```python
# Estadísticas generales
with open('index/metadata-completo.json', 'r') as f:
    metadata = json.load(f)

print(f"Total documentos: {metadata['total_documentos']}")
print(f"Documentos por tributo:")
for tributo, cantidad in metadata['estadisticas']['por_tributo'].items():
    print(f"  - {tributo}: {cantidad}")
```

---

## Estructura de Documentos Markdown

Cada documento está en `normativa/[tributo]/[tipo]/[nombre]/vigente.md`

**Estructura esperada:**

```markdown
# Ley N°XXX - [Nombre]

**Fuente:** SII/BCN
**Vigencia:** [Año]
**Última actualización:** [Año]
**URL Oficial:** https://...

## Artículos Clave

### Artículo X - [Título]

[Contenido parseado]

**Aplicación:** [Casos de uso]
**Relacionado con:** [Referencias cruzadas]
**Referencia:** [Cita formal]

## Cambios Recientes

[Actualizaciones por año]

## Conexiones Cruzadas

| Tema | Artículo | Documento |
|------|----------|-----------|
| ... | ... | ... |
```

---

## Uso en Skill tributario-marco

La skill `tributario-marco` consulta NORMA-CHILE así:

### Paso 1: Identificar tributos aplicables

```python
# Basado en rubro de empresa
rubro = "empresa_tecnologica"  # ejemplo

# Cargar índice
tributos_aplicables = [
    'impuesto-renta',
    'deducciones-beneficios',
    'iva',
    'normativa-laboral'
]
```

### Paso 2: Obtener documentos

```python
with open('index/por-tributo.json', 'r') as f:
    tributos = json.load(f)

leyes_aplicables = []
for tributo in tributos_aplicables:
    leyes_aplicables.extend(tributos[tributo])
```

### Paso 3: Leer documentos Markdown

```python
import os

for doc in leyes_aplicables:
    doc_path = os.path.join(REPO_ROOT, doc['path'])
    
    with open(doc_path, 'r') as f:
        contenido = f.read()
    
    # Usar contenido para generar análisis
    # Crear referencias en documento Word
    # Incluir en infografía
```

### Paso 4: Investigación Complementaria

Si hay gaps o se necesita mayor detalle:

```python
# NORMA-CHILE es punto de partida, no límite
# Si necesitas:
# - Sentencias específicas
# - Doctrina más reciente
# - Casos particulares

# Buscar en internet documentando SIEMPRE la fuente
# Usar solo fuentes oficiales (SII, BCN, jurisprudencia)
```

---

## Monitoreo de Cambios

### Recibir Notificaciones

Tarea Cowork automática cada **lunes 9 AM**:
- Detecta cambios en SII/BCN/Leyes.cl
- Genera commit con código (001, 002, 003...)
- Envía email con resumen

### Revisar Cambios Recientes

```markdown
Archivo: `monitoring/vigencias-AAAA.md`

Listar cambios por año
```

### Histórico de Commits

```
Archivo: `monitoring/changelog-commits.log`

Log de todos los commits de monitoreo
```

---

## Best Practices para Agentes

### ✓ Hacer

- **Consultar NORMA-CHILE primero** para normativa base
- **Documentar fuentes** en todos los análisis
- **Usar cross-references.json** para conexiones
- **Validar vigencia** checando fecha_ultima_actualizacion
- **Citar artículos específicos** (Art. X, Ley N°Y)

### ✗ Evitar

- No asumir normativa desactualizada
- No saltarse referencias cruzadas
- No usar solo títulos sin leer artículos
- No mezclar leyes diferentes sin validar
- No inventar normas

---

## Actualizar NORMA-CHILE

### Para Agregar Nueva Normativa

1. **Descargar PDF** de SII/BCN/Leyes.cl
2. **Guardar en:** `_sources/[fuente]/`
3. **Parsear a Markdown:** `normativa/[tributo]/[tipo]/[nombre]/vigente.md`
4. **Crear meta.json** con metadata
5. **Actualizar índices JSON**
6. **Hacer commit:** `git commit -m "Add: Ley N°XXX - [descripción]"`

### Cuando se Detecten Cambios (Automático)

- Sistema genera commit con código
- Email notifica cambios
- Pedir "push commit 003" en Claude
- Sistema ejecuta push automáticamente

---

## Preguntas Frecuentes

**P: ¿Qué versión de ley debo usar?**  
R: Siempre `vigente.md`. Es la versión actualizada con todas las modificaciones.

**P: ¿Qué hago si encuentro error en documento?**  
R: Reportar al usuario. Los documentos son parseados de fuentes oficiales pero pueden tener inconsistencias.

**P: ¿Puedo complementar con internet?**  
R: Sí, si NORMA-CHILE no cubre un caso específico. Pero documenta siempre la fuente complementaria.

**P: ¿Cómo cito una ley?**  
R: Usar formato oficial: "Art. X de Ley N°YYYYY" con link a documento en NORMA-CHILE.

---

**Última actualización:** 2026-09-01  
**Mantenedor:** NORMA-CHILE Monitor System
