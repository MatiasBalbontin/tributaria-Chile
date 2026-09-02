# NORMA-CHILE | Repositorio de Normativa Tributaria Chilena

**Base de conocimiento centralizada** de normativa tributaria chilena (2021-2026 + forward-looking) para asesoría, cumplimiento y análisis regulatorio.

Integrado con skill `tributario-marco` para análisis de marcos normativos empresariales.

---

## Estructura

- **`normativa/`** — Documentos parseados organizados por tributo (impuesto-renta, deducciones, IVA, etc.)
- **`_sources/`** — PDFs originals descargados de SII/BCN/Leyes.cl (sin procesar)
- **`index/`** — Índices JSON queryables para agente IA
- **`monitoring/`** — Tracking de cambios semanales
- **`scripts/`** — Script Python de monitoreo automático
- **`docs/`** — Guías de uso

---

## Fuentes Oficiales

1. **SII** (Servicio de Impuestos Internos)
2. **BCN** (Biblioteca del Congreso Nacional)
3. **Leyes.cl**
4. **Sentencias/Circulares SII**
5. **Doctrina oficial** (SII/BCN)

---

## Monitoreo Automático

**Tarea Cowork:** Lunes 9 AM (semanal)
- Script detecta cambios en SII/BCN/Leyes.cl
- Genera commit con código
- Envía email con resumen

**Tu acción:** Pides en Claude "push commit 003" → ejecuta automáticamente

---

## Usar NORMA-CHILE

### Para Agentes IA (skill tributario-marco)

```python
import json

# Cargar índice por tributo
with open('index/por-tributo.json', 'r', encoding='utf-8') as f:
    tributos = json.load(f)

# Buscar leyes sobre renta
renta_docs = tributos['impuesto-renta']

# Acceder a documentos
for doc in renta_docs:
    print(f"{doc['nombre']} - {doc['fuente']}")
    print(f"Path: {doc['path']}")
```

### Cross-references

```python
# Encontrar artículos relacionados
with open('index/cross-references.json', 'r', encoding='utf-8') as f:
    referencias = json.load(f)

art_17 = referencias['articulo-17-lir']
print(f"Artículo 17 está relacionado con: {art_17['relacionado-con']}")
```

---

## Metadata de Documentos

Cada documento Markdown incluye:

```markdown
# Ley N°17.063 - Estatuto Tributario

**Fuente:** SII (oficial)
**Vigencia:** 1980 (múltiples modificaciones)
**Última actualización:** 2024
**URL Original:** https://...

## Artículo X
[contenido]

**Cambios recientes (2024):** [refs]
```

---

## Próximas Acciones

- [ ] Descargar leyes 2021-2026 de SII/BCN
- [ ] Parsear a Markdown
- [ ] Generar índices JSON
- [ ] Configurar Cowork tarea
- [ ] Validar con skill tributario-marco
