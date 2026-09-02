# Tributaria-Chile | Base de Conocimiento Normativa Tributaria Chilena

**Repositorio centralizado de normativa tributaria chilena** para asesoría tributaria, cumplimiento normativo y análisis regulatorio empresarial.

Integrado con skill `tributario-marco` para análisis de marcos normativos de empresas reales.

---

## 📋 Contenido

### Leyes Fundamentales (2021-2026 + Forward-looking)
- **Ley N°17.063** - Estatuto Tributario (Impuesto a la Renta)
- **Ley N°18.038** - Código Tributario (Procedimientos)
- **DL N°825** - IVA (Impuesto a Ventas y Servicios)
- **Leyes N°18.045-18.046** - Sociedades Anónimas

### Jurisprudencia & Tratados (En construcción)
- Jurisprudencia Administrativa (Oficios SII, Circulares)
- Jurisprudencia Judicial (Sentencias TTA, Corte Suprema)
- Tratados Internacionales (CDIs, OCDE)
- Estudios Especializados (CET U. Chile, CEPET)
- Procedimientos Operativos (Matrices DDJJ, Formulario 22)

---

## 🤖 Monitoreo Automático

**Tarea recurrente:** Lunes 9 AM (America/Santiago)
- Script detecta cambios normativos en SII/BCN/Leyes.cl
- Genera commit automático con código secuencial (001, 002, 003...)
- Notifica cambios detectados
- Usuario valida y solicita push en Claude

**Próximas vigencias (2026-2027):** Forward-looking monitoring incluido

---

## 📖 Uso

### Para Asesoría Tributaria
1. Consultar normativa vigente por tributo
2. Revisar jurisprudencia relacionada
3. Verificar procedimientos operativos

### Para Agentes IA (skill tributario-marco)
1. Acceder índices JSON (`index/por-tributo.json`)
2. Buscar normativas aplicables por tributo
3. Integrar en análisis profesional
4. Citar fuentes con referencias precisas

---

## 📁 Estructura

```
tributaria-Chile/
├── README.md (este archivo)
├── LICENSE (CC BY-NC-SA)
├── normativa/
│   ├── impuesto-renta/
│   ├── iva/
│   ├── cumplimiento/
│   ├── jurisprudencia-administrativa/
│   ├── jurisprudencia-judicial/
│   ├── tratados-internacionales/
│   ├── estudios-especializados/
│   └── procedimientos-operativos/
├── index/
│   ├── por-tributo.json
│   ├── cross-references.json
│   └── metadata-completo.json
├── monitoring/
│   ├── vigencias-2024.md
│   ├── vigencias-2025.md
│   └── vigencias-proximas-2026-2027.md
└── scripts/
    └── monitor-normativa.py
```

---

## ⚖️ Licencia

**Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)**

- ✅ **Permitido:** Uso educativo, investigación, asesoría no comercial
- ✅ **Permitido:** Compartir con atribución
- ✅ **Permitido:** Modificar y adaptar bajo misma licencia
- ❌ **No permitido:** Usos comerciales (venta, consultorías pagadas, etc.)

Ver archivo `LICENSE` para términos completos.

---

## 🔄 Contribuciones & Actualizaciones

Cambios detectados automáticamente cada lunes. Para contribuciones manuales:
1. Fork del repositorio
2. Branch para cambios
3. Pull request con descripción

---

## 📧 Contacto & Feedback

Usuario: MatiasBalbontin  
Email: matiasrbalbontin@gmail.com

---

**Última actualización:** 2026-09-02  
**Estado:** Base inicial (4 leyes). Estructura lista para expansión.

*Base de conocimiento tributario en construcción continua.*
