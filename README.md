# Skills de prospección en LinkedIn

Por ahora hay 1: **creador-de-listas-linkedin**.

Le das tu cliente ideal y te regresa una lista de 50 a 150 personas en un CSV,
con nombre, titular, link al perfil y un semáforo que te dice con quién
conectar primero.

> **¿Se te atora la instalación?** Pásale el link de esta página a ChatGPT o a
> Claude y pídele: *"llévame paso a paso, uno a la vez, y espera a que te diga
> que ya lo hice antes de darme el siguiente"*. Dile qué computadora tienes
> (Mac o Windows) y qué te salió en pantalla cuando se atoró.

---

## Qué necesitas

**Para que la lista salga con links, la IA tiene que poder ver tu LinkedIn.**
Eso se logra con un navegador conectado. Cualquiera de estas sirve:

| Herramienta | Qué hace con este skill |
|---|---|
| **Claude Code + extensión Claude in Chrome** | Abre tu búsqueda, recorre las páginas y te entrega el CSV con links. |
| **Claude (app o claude.ai) + extensión Claude in Chrome** | Lo mismo, desde el chat. |
| **Solo el chat, sin navegador** | Te arma la búsqueda. Tú abres cada página, copias todo y lo pegas. Te regresa el CSV con semáforo, **pero sin links**: al copiar texto, los links no viajan. |

Funciona con LinkedIn normal y con Sales Navigator. En Sales Navigator puede
guardar la lista dentro de tu cuenta, y si quieres también te da el CSV.

---

## Instalación

### Opción A. En Claude (app o claude.ai)

1. Arriba de esta página, botón verde **Code** → **Download ZIP**.
2. Descomprímelo. Adentro está la carpeta `creador-de-listas-linkedin`.
3. Comprime **solo esa carpeta** en un ZIP.
4. En Claude: **Configuración → Capacidades → Skills → Subir skill** y elige
   ese ZIP.
5. Instala la extensión **Claude in Chrome** desde la Chrome Web Store e inicia
   sesión con tu cuenta de Claude.

### Opción B. En Claude Code

**B.1. Instala Claude Code.** Abre la terminal (Mac: "Terminal". Windows:
"PowerShell"), pega esto y dale enter:

```bash
npm install -g @anthropic-ai/claude-code
```

Si te dice que `npm` no existe, instala Node.js primero desde
[nodejs.org](https://nodejs.org) (el botón grande, versión LTS) y repite.

**B.2. Descarga el skill.** Arriba de esta página, botón verde **Code** →
**Download ZIP**. Doble clic para descomprimirlo. Se crea la carpeta
`skills-prospeccion-main` en tu carpeta de Descargas. Déjala ahí.

**B.3. Cópialo a su carpeta.** Pega el bloque que te toca en la terminal:

Mac:

```bash
mkdir -p ~/.claude/skills
cp -R ~/Downloads/skills-prospeccion-main/creador-de-listas-linkedin ~/.claude/skills/
```

Windows:

```powershell
mkdir "$HOME\.claude\skills" -Force
Copy-Item "$HOME\Downloads\skills-prospeccion-main\creador-de-listas-linkedin" "$HOME\.claude\skills\" -Recurse
```

**B.4. Conecta Chrome.** Instala la extensión **Claude in Chrome**, abre
LinkedIn en Chrome con tu sesión iniciada, y en la terminal escribe:

```bash
claude
```

Dentro de Claude Code escribe `/chrome` para conectarlo.

---

## Cómo se usa

Escribe:

```
arma mi lista de clientes ideales en LinkedIn
```

Te va a pedir 5 respuestas. Si ya tienes tu Regla del 1 o tu perfil de cliente
ideal, pégalo y las saca de ahí:

1. ¿Qué puesto tiene quien te compra?
2. ¿En qué tipo de empresa trabaja?
3. ¿De qué tamaño es esa empresa?
4. ¿En qué país?
5. ¿A quién NO le quieres vender?

Y 3 datos más: si tienes Sales Navigator o LinkedIn normal, si hay navegador
conectado y cuántas personas quieres.

---

## Qué vas a ver en el resultado

Un CSV con estas columnas:

```
nombre, titular, ubicacion, link, semaforo, por_que, busqueda
```

**El semáforo:**

- **A (revisar señal):** decide la compra y su empresa encaja. Abre su perfil:
  si publica, está contratando o cambió de puesto hace poco, conecta esta semana.
- **B:** cumple 1 de las 2. Espera.
- **Fuera:** no cumple o cae en tu "a quién NO".

El semáforo sale de lo que se ve en los resultados de búsqueda. La señal solo
se confirma abriendo el perfil, y el skill te lo marca como pendiente si no lo
abrió.

---

## Lo que ya sabemos de LinkedIn normal

- Una búsqueda muestra hasta 10 páginas, unos 100 perfiles. Para 150, el skill
  corre 2 o 3 búsquedas con distinto puesto y quita duplicados.
- El filtro de Sector toma la industria del perfil de la persona, no de su
  empresa. Por eso se cuelan perfiles de otros giros, y por eso existe el
  semáforo.
- Las cuentas gratis tienen un tope mensual de búsquedas. Si aparece el aviso,
  el skill te entrega lo que lleva.

---

## Qué NO hace este skill

- No manda solicitudes de conexión ni mensajes. Conectar lo haces tú, empezando
  por los A.
- No califica a nadie sin evidencia. Si falta un dato, lo marca como pendiente.
- No inventa perfiles para llegar al número.
