# Usar en ChatGPT

## Ruta sencilla: un Project

Esta ruta usa archivos e instrucciones de proyecto; no requiere una instalación de skill nativo.

1. Descarga **Code → Download ZIP** y descomprímelo.
2. Crea un Project de ChatGPT para tu prospección, preferiblemente uno por cliente.
3. Adjunta los archivos Markdown de `creador-de-listas-linkedin` y su CSV de industrias. Incluye las referencias y los metadatos de la taxonomía. No basta con adjuntar solo SKILL.md: necesita sus referencias. Si te resulta más cómodo, pide a Codex que genere el paquete compacto con `python3 scripts/empaquetar.py`; adjunta los dos archivos de `dist/chatgpt/`.
4. Copia el bloque siguiente en las instrucciones del Project.
5. Abre un chat dentro del Project y pega tu cliente ideal o Regla del 1 junto con el mensaje de inicio del README.

No hace falta adjuntar el script de consulta si tu ChatGPT no puede ejecutar código. Puede consultar las filas relevantes del CSV; si no logra leerlo, deberá solicitar el fragmento necesario, sin inventar categorías.

## Instrucciones para copiar

```text
Ayúdame a construir y revisar listas de clientes ideales en LinkedIn.
Usa el proceso de creador-de-listas-linkedin adjunto: SKILL.md y sus referencias,
o el paquete consolidado proceso-listas-chatgpt.md. Ambos contienen el mismo proceso.
Lee las secciones necesarias para la fase actual y consulta solo las filas relevantes
del CSV de industrias. Si falta una referencia necesaria o no puedes leerla, di cuál;
continúa únicamente con lo que sí puedes verificar.
Reutiliza el cliente ideal ya aportado. Pregunta en un bloque solo lo que falte.
Distingue confirmado, hipótesis y pendiente. Separa ubicación de persona y sede de empresa.
Comprueba tus herramientas: búsqueda web o acceso a GitHub no es control de mi LinkedIn.
Si no puedes leer la sesión, entrega filtros y revisa resultados, capturas o archivos que aporte.
Conserva los enlaces aportados; no inventes los ausentes ni perfiles para cumplir volumen.
Empieza con 20 perfiles, o todos si hay menos. A requiere evidencia de todos los requisitos;
B es pendiente de evidencia; Fuera requiere una contradicción comprobada.
No cuentes B como calificado. Una señal no demuestra necesidad ni presupuesto.
Trabaja con un agente. Si falla una acción, revisa el estado y ajusta antes de un único reintento.
Si sigue fallando o aparece un límite, entrega avance parcial y el paso para retomarlo.
Al cerrar, deja ICP, búsqueda/filtros, muestra, perfiles/links disponibles, conteos,
pendientes y último punto revisado. No envíes invitaciones ni mensajes.
```

## Comprobar que quedó listo

Escribe: «Dime qué archivos puedes leer y prepara una búsqueda con mi ICP. Si no tienes navegador, entrega solo filtros y una plantilla para los resultados». La IA debe identificar los archivos usados, reutilizar tu información y declarar el acceso real. Mencionar un nombre de archivo no prueba su lectura: pide un criterio concreto extraído de la referencia.

Si tu aplicación permite skills nativos, puedes usar el mismo directorio como skill siguiendo los controles que tenga disponibles. No asumir que subir archivos al Project lo instala globalmente. Para Codex, usa [su guía](codex.md).

Si falta acceso al navegador, copia resultados con sus URLs o adjunta un CSV. El texto copiado puede perder enlaces. Puedes pegar los enlaces por separado. Ninguna instalación ni conexión de GitHub garantiza acceso a tu cuenta de LinkedIn.
