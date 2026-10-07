# Comprobaciones

```bash
python3 -m unittest discover -s tests -v
python3 scripts/empaquetar.py
```

Comprueban referencias internas del skill, contenido completo del ZIP y paquete de ChatGPT, integridad del CSV y consulta desde otra carpeta. No necesitan cuenta de LinkedIn ni paquetes externos.

## Prueba de comportamiento pendiente en cada herramienta

Usar datos sintéticos y registrar herramienta/versión, archivos leídos, respuesta y resultado. No subir datos de clientes al repositorio.

| Caso | Petición | Criterio de aceptación |
|---|---|---|
| ChatGPT sin navegador | Dueños de agencias de reclutamiento de 20–300 empleados en México; excluir freelancers; tengo LinkedIn normal; quiero 50. | Reutiliza ICP; distingue sede/persona si falta; propone búsqueda y muestra; no promete 50 ni acceso; tamaño se revisa manualmente. |
| Evidencia incompleta | Perfil sintético con puesto comprador y giro correcto, pero tamaño desconocido y requisito 20–300. | B / PENDIENTE; no cuenta como calificado y explica el dato faltante. |
| Exclusión comprobada | Perfil sintético identificado expresamente como freelancer. | Fuera / NO ENCAJA aunque publique mucho. |
| Texto sin URLs | Dos resultados sintéticos con el mismo nombre y sin enlaces. | Enlace vacío y deduplicación pendiente; no inventa URL ni afirma identidad única. |
| Navegador interrumpido | Ya se revisó una página; el acceso falla dos veces. | Tras leer estado y ajustar un reintento, entrega avance y punto de continuación; no vuelve a empezar. |
| Solo industria | «Busco clientes en salud». | Hasta 3 enfoques como hipótesis; no impone país, tamaño ni fundador. |

Antes de anunciar ejecución comprobada, probar en ChatGPT y Codex y observar una búsqueda real autorizada: filtros aplicados, muestra, exportación y, si corresponde, enlace/conteo de lista guardada. La prueba histórica de LinkedIn normal se conserva como antecedente reportado, no sustituye estas pruebas.
