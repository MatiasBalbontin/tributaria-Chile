# AGENTS.md — Lineamientos operativos para agentes

Todo agente que trabaje en este repositorio opera bajo estas reglas.
Son invariables para toda tarea. El prompt de tarea solo define el QUÉ;
este documento define el CÓMO y los LÍMITES.

## R0 — Rol y límites

- Eres un agente de producción. Tus outputs son INSUMOS DE TRABAJO para  
  revisión humana. Nunca material entregable final.
- Este repositorio es un insumo de investigación para profesionales  
  tributarios. Ningún contenido que produzcas constituye dictamen,  
  asesoría ni opinión profesional.
- No redactes texto prescriptivo hacia usuarios ("debe", "conviene",  
  "se recomienda"). El repositorio describe normativa; no aconseja.

## R1 — Verdad normativa (regla principal)

- PROHIBIDO escribir identificaciones, números, fechas o contenido de  
  normas desde memoria interna. Todo dato legal se verifica contra  
  fuente oficial (leychile.cl / BCN, sii.cl) antes de escribirse.
- Si no puedes verificar un dato: lo marcas `texto_verificado: false`  
  y lo registras en monitoring/pendientes-verificacion.md. Nunca lo  
  inventas ni sustituyes por fuentes secundarias.
- Si una instrucción de tarea contradice la fuente oficial verificada,  
  prevalece la fuente, y registras la discrepancia en el resumen.  
  Prohibida la corrección silenciosa en cualquier dirección.

## R2 — Datos personales

- PROHIBIDO incluir datos de personas naturales o jurídicas: RUTs,  
  declaraciones, balances, cartolas, nombres de clientes, cualquier  
  dato identificable, ni "anonimizado". Este repo es público y el  
  historial de git no se purga.

## R3 — Gestión del repositorio

- Nada se borra. Contenido reemplazado migra a normativa/historico/  
  con campo `reemplazado_por` en su metadata.
- IDs de normas: formato estable {NORMA}_{ARTICULO} (ej. LIR_art31-4,  
  CT_art4-ter, IVA_art11). Los commits del monitor conservan su  
  numeración secuencial propia (esa numeración es de commits, no de  
  normas).
- Todo documento normativo lleva en su metadata: fuente_oficial_url,  
  fecha_publicacion_diario_oficial, fecha_verificacion,  
  texto_verificado.
- Trabajas SIEMPRE en branch dedicado. Nunca push a main. El flujo  
  termina en Pull Request con resumen de: cambios aplicados,  
  verificaciones pendientes (con motivo), discrepancias encontradas.

## R4 — Estilo

- Español. Markdown. Frontmatter según index/SCHEMA.md cuando aplique.
- Precisión sobre completitud: mejor un stub bien referenciado que un  
  documento extenso no verificado.

## Conflictos

Si dos reglas chocan: R1 > R2 > R0 > resto. Ante duda no resuelta por
este documento: no actúes, consulta.
