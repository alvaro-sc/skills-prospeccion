# Taxonomía de industrias de LinkedIn

Consulta comprobada: 2026-10-02. Fuente: [Industry Codes V2](https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/industry-codes-v2). V2 significa versión 2.

El catálogo cubre todas las industrias publicadas por LinkedIn, incluyendo servicios, tecnología, educación, salud, comercio y manufactura. La copia contiene 487 registros: 434 activos y 53 inactivos. La disponibilidad y traducción de cada opción se comprueban en el menú del producto utilizado.

## Archivos

- [CSV completo](industrias-linkedin-v2.csv): ID, etiqueta original, jerarquía, definición y estado. Exportación local de las tablas oficiales, no un CSV publicado por LinkedIn. UTF-8 con BOM, compatible con Excel.
- [Procedencia y controles](industrias-linkedin-v2.meta.json): URL, fecha de descarga, recuentos y huellas de integridad. La fecha editorial publicada no equivale a la fecha de descarga.
- [Consulta breve](consultar-industrias.py): devuelve hasta 20 coincidencias activas por defecto; no requiere paquetes adicionales.

## Uso en el skill

1. Traducir el ICP a actividades observables: qué vende, a quién, fabricante/distribuidor/servicio.
2. Buscar términos ingleses probables en el CSV local. Son claves de búsqueda, no etiquetas oficiales confirmadas. Consultar solo coincidencias; no cargar el CSV entero en el contexto.
3. Leer definición y jerarquía de los IDs candidatos. Clasificar núcleo, adyacente, excluido o pendiente. No usar códigos inactivos como filtros nuevos.
4. Verificar etiqueta visible y filtros aplicados en Sales Navigator o LinkedIn. El ID del catálogo no demuestra por sí mismo disponibilidad en un menú.
5. Revisar 15–25 empresas, o todas si hay menos, antes de ampliar. Registrar aceptadas, rechazadas, motivos, consulta y filtros realmente usados. Después revisar cargos actuales de personas de las cuentas elegidas. La revisión no acredita presupuesto.
6. Usar keywords complementarias si la clasificación de las empresas es imperfecta. No llamar auditoría taxonómica a una revisión hecha solo por palabras clave.

Desde esta carpeta:

```sh
python3 consultar-industrias.py chemical cleaning wholesale
python3 consultar-industrias.py 1257 727 54 --descripciones
```

Los términos se combinan con OR. Un ID busca exactamente ese registro; una palabra busca en etiqueta y jerarquía. Con `--descripciones` también busca en la definición y la muestra. La búsqueda textual local no interpreta sinónimos ni traduce automáticamente. Sin coincidencias, probar sinónimos ingleses y definiciones antes de consultar la web.

## Fuentes complementarias

- [Filtros de Sales Navigator](https://www.linkedin.com/help/sales-navigator/answer/a1461507): Industry de cuentas incluye categorías hijas; distinguir Geography de la persona y Headquarters de empresa.
- [Boolean de LinkedIn](https://www.linkedin.com/help/lms/answer/a524335): AND, OR, NOT, comillas y paréntesis. Esta sintaxis es distinta del catálogo de industrias.
- [Referencias del skill](../plataformas.md): capacidades por campo y producto. No trasladar capacidades de Sales Navigator a LinkedIn normal.

## Vigencia

Usar la copia local para consultas rutinarias. Volver a la fuente oficial si falta una categoría tras probar sinónimos, el menú contradice el CSV o el usuario pide comprobar vigencia. Como regla de mantenimiento de este proyecto, comprobar la fuente al iniciar una campaña si la copia supera 90 días; no es un plazo fijado por LinkedIn. Al actualizar, comparar altas, bajas y cambios por ID, validar recuentos/estados y actualizar metadatos. Conservar las selecciones documentadas de campañas anteriores.

