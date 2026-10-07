# Referencias y URLs en leychile.cl - Guía de Verificación Futura

**Preparado:** 2026-10-07  
**Estado:** Pendiente de acceso a leychile.cl  
**Propósito:** Facilitar verificación exhaustiva una vez se obtenga acceso de red

---

## ACCESO ACTUAL A leychile.cl

**Estado:** BLOQUEADO  
**Error:** HTTP 403 Forbidden (proxy tunnel refused)  
**Solución:** Agregar www.leychile.cl a dominios permitidos en configuración de red

---

## NORMAS A VERIFICAR - URLS Y DATOS ESPERADOS

### 1. DECRETO LEY N°824 DE 1974 - LEY SOBRE IMPUESTO A LA RENTA (LIR BASE)

**URL Esperada:**
```
https://www.leychile.cl/Navegar?idNorma=824&tipo_norma=DL
```

**Datos a Verificar:**
- [ ] Fecha de publicación en Diario Oficial
- [ ] Número de Diario Oficial
- [ ] Título oficial exacto
- [ ] Estado: Vigente o Histórico
- [ ] Último refundidor/refundición
- [ ] Número de refundición (DFL) vigente
- [ ] Enlace a texto completo refundido

**Hipótesis:** Esta es la norma base de la LIR chilena  
**Notas:** Tiene múltiples refundiciones. La más reciente importante es DFL N°1/2015

---

### 2. LEY N°17.063 DE 1980 - ESTATUTO TRIBUTARIO

**URL Esperada:**
```
https://www.leychile.cl/Navegar?idNorma=17063
```

**Datos a Verificar:**
- [ ] Fecha de publicación en Diario Oficial
- [ ] Número de Diario Oficial
- [ ] Título oficial exacto
- [ ] Estado: Vigente o Histórico
- [ ] Naturaleza: ¿Complementaria a DL N°824? ¿Modificatoria?
- [ ] Última modificación
- [ ] Relación explícita con DL N°824

**Hipótesis:** Es ley complementaria a DL N°824, NO la ley base de LIR  
**Notas:** La documentación local la llama "Estatuto Tributario"

---

### 3. DECRETO LEY N°830 DE 1974 - CÓDIGO TRIBUTARIO (HISTÓRICO)

**URL Esperada:**
```
https://www.leychile.cl/Navegar?idNorma=830&tipo_norma=DL
```

**Datos a Verificar:**
- [ ] Confirmar que es Código Tributario de 1974
- [ ] Número de Diario Oficial
- [ ] Estado: Derogado o Histórico
- [ ] Fecha de derogación (debería ser 1982 con Ley 18.038)
- [ ] Enlace a norma que la reemplazó

**Hipótesis:** Fue reemplazado por Ley 18.038 en 1982  
**Notas:** Será documento histórico

---

### 4. LEY N°18.038 - CÓDIGO TRIBUTARIO (VIGENTE)

**URL Esperada:**
```
https://www.leychile.cl/Navegar?idNorma=18038
```

**Datos a Verificar:**
- [ ] Fecha de publicación en Diario Oficial (esperado: 1982)
- [ ] Número de Diario Oficial
- [ ] Título oficial exacto
- [ ] Estado: Vigente
- [ ] Últimas modificaciones importantes
- [ ] Ultimo refundidor vigente
- [ ] Enlaces a refundiciones

**Hipótesis:** Es el Código Tributario vigente desde 1982  
**Notas:** Reemplazó a DL N°830; tiene múltiples refundiciones

---

### 5. DECRETO LEY N°825 DE 1974 - LEY SOBRE IMPUESTO A LAS VENTAS Y SERVICIOS (IVA)

**URL Esperada:**
```
https://www.leychile.cl/Navegar?idNorma=825&tipo_norma=DL
```

**Datos a Verificar:**
- [ ] Fecha de publicación en Diario Oficial
- [ ] Número de Diario Oficial
- [ ] Título oficial exacto
- [ ] Estado: Vigente
- [ ] Tasa general de IVA (esperado: 19%)
- [ ] Últimas modificaciones (especialmente 2023-2024)
- [ ] Refundidor vigente
- [ ] Circulares/resoluciones SII relacionadas

**Hipótesis:** Es la ley de IVA vigente desde 1974  
**Notas:** La documentación local es correcta; tasa 19% confirmada

---

### 6. LEY N°18.045 - SOCIEDADES ANÓNIMAS

**URL Esperada:**
```
https://www.leychile.cl/Navegar?idNorma=18045
```

**Datos a Verificar:**
- [ ] Fecha de publicación en Diario Oficial (esperado: 1981)
- [ ] Número de Diario Oficial
- [ ] Título oficial exacto
- [ ] Estado: Vigente
- [ ] Ámbito: ¿Regula SA? ¿NO regula bancos?
- [ ] Últimas modificaciones
- [ ] Refundidor vigente
- [ ] Distinción clara con Ley 18.046 y 18.010

**Hipótesis:** Ley de Sociedades Anónimas (NO de bancos; NO debe confundirse con 18.046)  
**Notas:** Aplica a todas las SA (abiertas y cerradas)

---

### 7. LEY N°18.046 - MERCADO DE VALORES / OPERACIONES CON VALORES

**URL Esperada:**
```
https://www.leychile.cl/Navegar?idNorma=18046
```

**Datos a Verificar:**
- [ ] Fecha de publicación en Diario Oficial (esperado: 1981-1982)
- [ ] Número de Diario Oficial
- [ ] Título oficial exacto
- [ ] Estado: Vigente
- [ ] Ámbito: ¿Mercado de valores? ¿NO es ley de SA?
- [ ] Últimas modificaciones
- [ ] Refundidor vigente
- [ ] Relación con Ley 18.045 (complementaria, no equivalente)

**Hipótesis:** Regula mercado de valores y operaciones de valores (NO es ley de SA)  
**Notas:** Aplica a SA abiertas; completa a Ley 18.045

---

### 8. LEY N°18.010 - GENERAL DE BANCOS (REFERENCIA)

**URL Esperada:**
```
https://www.leychile.cl/Navegar?idNorma=18010
```

**Datos a Verificar:**
- [ ] Confirmar que regula instituciones bancarias
- [ ] Distinta de Leyes 18.045 y 18.046
- [ ] Verificar NO está vinculada a SA genéricamente

**Hipótesis:** Es ley de bancos; completamente distinta de 18.045/18.046  
**Notas:** Fuera del alcance de hipótesis original, pero necesaria para aclaración

---

## MATRIZ DE VERIFICACIÓN EXHAUSTIVA

| ID | Norma | Tipo | Año | URL esperada | Estado Esperado | Verificado |
|---|---|---|---|---|---|---|
| 1 | DL N°824 | DL | 1974 | ?idNorma=824&tipo_norma=DL | Vigente (refundido) | ☐ |
| 2 | Ley 17.063 | Ley | 1980 | ?idNorma=17063 | Vigente/Complementaria | ☐ |
| 3 | DL N°830 | DL | 1974 | ?idNorma=830&tipo_norma=DL | Histórico/Derogado | ☐ |
| 4 | Ley 18.038 | Ley | 1982 | ?idNorma=18038 | Vigente | ☐ |
| 5 | DL N°825 | DL | 1974 | ?idNorma=825&tipo_norma=DL | Vigente | ☐ |
| 6 | Ley 18.045 | Ley | 1981 | ?idNorma=18045 | Vigente | ☐ |
| 7 | Ley 18.046 | Ley | 1981-82 | ?idNorma=18046 | Vigente | ☐ |
| 8 | Ley 18.010 | Ley | 1981 | ?idNorma=18010 | Vigente | ☐ |

---

## INFORMACIÓN ESPECÍFICA A CAPTURAR

Para cada norma, cuando se logre acceso a leychile.cl, capturar y documentar:

### Plantilla de Captura

```markdown
## [NOMBRE DE LA LEY]

### Identificadores
- **URL leychile.cl:** [copiar URL exacta]
- **Número de Ley/DL:** [copiar número exacto]
- **Fecha de Publicación:** [YYYY-MM-DD]
- **Número de Diario Oficial:** [número y año]
- **Página DO:** [página]

### Estado Vigencia
- **Estado:** [Vigente/Derogada/Histórica]
- **Última Modificación:** [fecha]
- **Tipo de Modificación:** [nombre de ley modificatoria]
- **Refundición Vigente:** [DFL/Número]

### Contenido
- **Título Oficial:** [copiar exacto]
- **Descripción breve:** [párrafo del sitio]
- **Artículos principales:** [lista]

### Relaciones Normativas
- **Modifica a:** [leyes/decretos que modifica]
- **Modificada por:** [leyes/decretos que la modifican]
- **Complementa a:** [leyes conexas]
- **Reemplaza a:** [si aplica]
- **Reemplazada por:** [si aplica]

### Referencias Cruzadas
- **Enlaces en leychile.cl:** [capturar]
- **Circulares SII:** [si existen]
- **Resoluciones CMF:** [si existen]
```

---

## CHECKLIST DE VERIFICACIÓN COMPLETADA

Una vez acceso esté disponible, marcar items conforme se verifiquen:

**Fase 1: Acceso y Búsqueda**
- [ ] Acceso a leychile.cl confirmado
- [ ] Todas las URLs esperadas responden
- [ ] Se puede descargar texto completo de cada norma

**Fase 2: Verificación de Hipótesis**
- [ ] Ley 17.063: Confirmar naturaleza (base o complementaria)
- [ ] Ley 18.038: Confirmar que reemplazó DL N°830
- [ ] DL N°825: Confirmar vigencia y tasa de IVA
- [ ] Ley 18.045: Confirmar que es SA, NO bancos
- [ ] Ley 18.046: Confirmar que es valores, NO SA
- [ ] Ley 18.010: Confirmar que es bancos, distinta de anteriores

**Fase 3: Datos Exactos**
- [ ] Capturar todos los Diarios Oficiales
- [ ] Capturar todas las fechas de publicación
- [ ] Capturar refundidores vigentes
- [ ] Documentar últimas modificaciones 2023-2024

**Fase 4: Documentación**
- [ ] Actualizar investigacion-normas.md con datos exactos
- [ ] Actualizar archivos locales con información verificada
- [ ] Crear archivo de "Números de Referencia Exactos"

---

## INSTRUCCIONES PARA ACCESO FUTURO

### Paso 1: Solicitar Acceso
1. Ir a configuración de ambiente Claude Code (icono de nube en barra superior)
2. Seleccionar "Edit"
3. Buscar "Network access"
4. Cambiar a "Limited" o agregar www.leychile.cl a dominios permitidos

### Paso 2: Verificar Acceso
```bash
curl -I https://www.leychile.cl
# Esperar HTTP 200, NO 403
```

### Paso 3: Ejecutar Búsquedas
- Abrir en navegador cada URL del listado anterior
- Capturar información usando herramienta WebFetch
- Documentar resultados en archivo especial

### Paso 4: Actualizar Documentación
- Reemplazar URLs esperadas por URLs verificadas
- Documentar cualquier discrepancia
- Actualizar archivos locales del repositorio

---

## ARCHIVOS DE SEGUIMIENTO

Cuando acceso esté disponible, crear:

1. **verificacion-leychile-resultados.md**
   - URLs verificadas
   - Datos exactos capturados
   - Comparación hipótesis vs realidad

2. **actualizacion-base-datos-normas.md**
   - Cambios necesarios en documentación local
   - Nuevos archivos a crear
   - Inconsistencias a resolver

3. **números-referencia-oficiales.md**
   - Tabla con IDs exactos de cada norma
   - Diarios Oficiales exactos
   - Fechas de publicación verificadas
   - URLs leychile.cl definitivas

---

**Este documento será actualizado conforme se obtenga acceso a leychile.cl**

*Preparado como parte de investigación de normas tributarias fundamentales*  
*Última actualización: 2026-10-07*
