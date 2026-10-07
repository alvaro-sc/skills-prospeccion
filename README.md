# Listas de clientes ideales en LinkedIn

Dale a tu IA tu cliente ideal o tu Regla del 1. El skill **creador-de-listas-linkedin** convierte esa información en una búsqueda para Sales Navigator o LinkedIn normal y te ayuda a revisar los perfiles encontrados.

Empieza con 20 perfiles. Puedes pedir una meta de 50–150, pero la entrega depende de los resultados accesibles y de cuánto encajen. Si faltan datos o acceso, recibes la búsqueda y el avance disponible.

## Elige tu herramienta

| Herramienta | Cómo empezar | Qué puede entregar |
|---|---|---|
| ChatGPT, desde un Project | [Guía de ChatGPT](docs/chatgpt.md) | Filtros y revisión de datos que compartas; lista con links si los datos los incluyen o hay navegador con acceso comprobado. |
| Codex o ChatGPT de escritorio con skills locales | [Guía de Codex](docs/codex.md) | El mismo proceso. Operar LinkedIn requiere herramientas de navegador disponibles y sesión accesible. |
| Claude con skills | Instalación de abajo | El mismo proceso. Para navegar, comprobar la integración disponible: Claude in Chrome, Cowork o Claude Code. |

**Instalar el skill no conecta LinkedIn.** La búsqueda web tampoco da acceso a tu sesión. Si no hay navegador conectado, la IA prepara los filtros y revisa lo que pegues o adjuntes. Conserva enlaces aportados y deja vacíos los ausentes.

## Empieza aquí

```text
Arma mi lista de clientes ideales en LinkedIn con creador-de-listas-linkedin.
Tengo [Sales Navigator / LinkedIn normal]. Mi cliente ideal es: [...].
Primero prepara la búsqueda y revisa una muestra de 20 perfiles.
Comprueba tu acceso; si no puedes navegar, trabaja con los resultados que comparta.
```

Si ya pegaste tu cliente ideal, la IA reutiliza esos datos. Solo pide lo que falte:

1. ¿Qué puesto tiene quien te compra?
2. ¿En qué tipo de empresa trabaja?
3. ¿De qué tamaño es esa empresa?
4. ¿En qué país está la persona o la empresa?
5. ¿A quién NO le quieres vender?

También define la herramienta, el acceso a resultados y el volumen objetivo.

## Qué recibes

Una búsqueda con filtros por campo y, cuando hay resultados aportados u observados, una tabla o CSV:

```text
nombre,titular,ubicacion,link,semaforo,por_que,busqueda,ajuste_icp,senal,fuente,fecha_revision
```

- **A — revisar señal:** cumple todos tus requisitos con evidencia. La actividad visible puede ayudar a priorizar.
- **B — completar evidencia:** falta confirmar algún requisito. No se cuenta como calificado.
- **Fuera:** contradice un requisito o una exclusión.

La señal (publicaciones, vacantes, cambio de puesto) se marca pendiente cuando no se ha observado. No demuestra intención de compra. El skill no envía invitaciones ni mensajes.

En Sales Navigator, si hay control del navegador, puede guardar personas en una lista y verificar su enlace y conteo. En LinkedIn normal conserva la lista en un CSV o tabla externa. Páginas y límites dependen de la cuenta: si aparece una restricción, entrega lo recopilado.

## Instalar en Claude

Descarga **Code → Download ZIP**, descomprímelo y ubica `creador-de-listas-linkedin`.

- **Claude con carga de skills:** comprime solo esa carpeta y súbela donde tu cuenta permita agregar skills. La disponibilidad depende de tu cuenta y de los controles actuales.
- **Claude Code:** copia esa carpeta en `~/.claude/skills/` (Windows: `$HOME\.claude\skills\`). Si usas Claude in Chrome, configura la conexión desde Claude Code con `/chrome` y comprueba que pueda leer LinkedIn.

Para configurar la navegación, sigue la [guía oficial de Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome). No asumir que una extensión instalada permite controlar Chrome desde cualquier chat de claude.ai.

## Si se atora

Pide: «Guíame un paso a la vez. Ya llegué hasta [...], me salió [...]. Conserva mi cliente ideal y lo que ya revisamos». El skill limita reintentos y entrega avance parcial para retomar desde el último punto.

## Para mantener este repositorio

El proceso común vive en [SKILL.md](creador-de-listas-linkedin/SKILL.md); las guías explican cómo usarlo en cada herramienta. [AGENTS.md](AGENTS.md) orienta los cambios y [las comprobaciones](tests/README.md) separan estructura de pruebas reales. [Fuentes oficiales](docs/fuentes.md).

Este repositorio distribuye el material para clientes. No subir aquí sus ICPs, perfiles, listas ni credenciales. La organización interna de LinkedIn 360 OS sigue en el Second Brain.
