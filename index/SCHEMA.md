# SCHEMA.md — Esquema de Metadatos Normativo

Define la estructura completa de registros en los índices JSON y documentos normativos del repositorio.

---

## Campos de Documento Normativo

Todo documento en `normativa/` debe llevar estos campos en su frontmatter/metadata:

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `id` | string | ✅ | ID único y estable: formato `{NORMA}_{ARTICULO}` ej. `LIR_art31-4`, `CT_art4-ter` |
| `norma` | string | ✅ | Identificación exacta: "Ley N°17.063", "DL N°824", etc. (verificado contra fuente oficial) |
| `articulos` | array[string] | ✅ | Lista de artículos contenidos: `["1", "17", "21"]` |
| `fuente_oficial_url` | string (URL) | ✅ | URL completa a leychile.cl, bcn.cl o sii.cl del texto vigente |
| `fecha_publicacion_diario_oficial` | date (YYYY-MM-DD) | ✅ | Fecha de publicación en Diario Oficial (fuente oficial) |
| `vigente` | boolean | ✅ | `true` si la norma está actualmente en vigor; `false` si histórica/derogada |
| `fecha_verificacion` | date (YYYY-MM-DD) | ✅ | Fecha en que se verificó el contenido contra fuente oficial |
| `texto_verificado` | boolean | ✅ | `true` si el extracto de texto coincide con fuente oficial consultada; `false` si pendiente o no verificado |
| `reemplazado_por` | string | ❌ | (Solo en histórico/) ID de la norma que reemplaza este contenido |
| `vigencia_estimada_fin` | date (YYYY-MM-DD) | ❌ | Fecha esperada de derogación (si aplica) |

### Ejemplo de documento normativo correcto

```markdown
---
id: LIR_art1
norma: "Decreto Ley N°824 de 1974 (DL N°824)"
articulos: ["1"]
fuente_oficial_url: "https://www.leychile.cl/Navegar/idNorma/5597"
fecha_publicacion_diario_oficial: 1974-01-01
vigente: true
fecha_verificacion: 2026-10-07
texto_verificado: true
---

# Artículo 1 — Concepto de Renta

[Texto verificado del artículo]
```

---

## Esquema de Índices JSON

### `index/por-tributo.json`

Organización de normas por tipo de tributo.

```json
{
  "impuesto-renta": [
    {
      "id": "LIR_vigente",
      "norma": "Decreto Ley N°824 de 1974",
      "articulos": ["1", "17", "21"],
      "fuente_oficial_url": "https://www.leychile.cl/Navegar/idNorma/5597",
      "fecha_publicacion_diario_oficial": "1974-01-01",
      "vigente": true,
      "fecha_verificacion": "2026-10-07",
      "texto_verificado": true,
      "path": "normativa/impuesto-renta/leyes/dl-824-lir/vigente.md",
      "descripcion": "[descripción breve]"
    }
  ],
  "iva": [...],
  "cumplimiento": [...]
}
```

### `index/cross-references.json`

Referencias cruzadas entre normas.

```json
{
  "LIR_art1": {
    "referencias_a": ["DL825_art1"],
    "referenced_by": ["CT_art4ter"]
  }
}
```

### `index/metadata-completo.json`

Registro completo con todos los campos (usado para auditoría).

```json
{
  "LIR_vigente": {
    "id": "LIR_vigente",
    "norma": "Decreto Ley N°824 de 1974",
    "articulos": ["1", "17", "21", ...],
    "fuente_oficial_url": "https://www.leychile.cl/Navegar/idNorma/5597",
    "fecha_publicacion_diario_oficial": "1974-01-01",
    "vigente": true,
    "fecha_verificacion": "2026-10-07",
    "texto_verificado": true,
    "path": "normativa/impuesto-renta/leyes/dl-824-lir/vigente.md",
    "descripcion": "...",
    "historico": false,
    "reemplazado_por": null
  }
}
```

---

## Validación y Auditoría

- `texto_verificado: true` → el extracto en el documento fue cotejado línea a línea contra fuente oficial en la `fecha_verificacion`
- `texto_verificado: false` → campo aún sin verificar; se registra en `monitoring/pendientes-verificacion.md` con motivo
- Todos los campos requeridos (✅) deben estar presentes o con valor null + `texto_verificado: false` si el dato no se puede obtener

---

## Nombrado de Archivos Históricos

Cuando se reemplaza contenido (R3):

1. Original permanece en su ruta
2. Se crea copia en `normativa/historico/{nombre-original}/`
3. Copia lleva metadata adicional: `reemplazado_por: {nuevo_id}`
4. Se registra en un changelog

