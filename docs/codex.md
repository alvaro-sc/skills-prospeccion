# Usar en Codex

El skill usa el formato SKILL.md compartido. La carpeta fuente es `creador-de-listas-linkedin`; no hace falta mantener una segunda versión del proceso para GPT.

## Instalar

Pide a Codex:

```text
Usa skill-installer para instalar creador-de-listas-linkedin desde
https://github.com/alvaro-sc/skills-prospeccion,
carpeta creador-de-listas-linkedin. Comprueba que se pueda invocar.
```

También puedes descargar el repositorio y copiar solo la carpeta del skill a `~/.agents/skills/` para uso personal, o a `.agents/skills/` dentro de tu proyecto para uso de ese proyecto. Si ya existe, compara versiones antes de reemplazarla. No instales duplicados del mismo skill en varias ubicaciones.

Ejemplo en Mac, después de descomprimir el ZIP en Descargas y comprobar el nombre de carpeta:

```bash
mkdir -p ~/.agents/skills
cp -R ~/Downloads/skills-prospeccion-main/creador-de-listas-linkedin ~/.agents/skills/
```

En PowerShell, ajustando la ruta si tu carpeta Descargas tiene otro nombre:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills"
Copy-Item "$HOME\Downloads\skills-prospeccion-main\creador-de-listas-linkedin" "$HOME\.agents\skills\" -Recurse
```

En Codex CLI o IDE, invoca `$creador-de-listas-linkedin` o selecciónalo con `/skills`. Si no aparece tras instalarlo, reinicia Codex. En interfaces con selector `@`, elige el skill disponible. Si trabajas sobre el repositorio sin instalarlo, pide explícitamente que lea `creador-de-listas-linkedin/SKILL.md`; la carpeta en la raíz no se descubre como skill local por sí sola.

## Comprobar acceso y empezar

```text
Usa creador-de-listas-linkedin. Mi ICP es [...]. Tengo Sales Navigator.
Prepara la búsqueda y revisa primero 20 perfiles.
Comprueba si tienes navegador con acceso a mi LinkedIn.
Si no lo tienes, entrega los filtros y trabaja con los resultados que aporte.
```

Codex puede preparar búsquedas y archivos con este skill. Recorrer LinkedIn exige herramientas de navegador y sesión disponibles en esa ejecución; instalarlo no las añade. Si puede navegar, debe comprobar filtros y resultados, conservar avances y verificar cualquier lista guardada. No basta un clic para declarar el guardado.

Al mantener este repositorio, Codex lee [AGENTS.md](../AGENTS.md). Es una guía de mantenimiento; no sustituye las instrucciones del Project de ChatGPT ni el proceso del skill.
