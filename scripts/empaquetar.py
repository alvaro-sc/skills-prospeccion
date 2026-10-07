"""Genera entregables desde el skill fuente; no requiere dependencias externas."""
import argparse
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'creador-de-listas-linkedin'


def build(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    texts = [SKILL / 'SKILL.md'] + sorted((SKILL / 'references').rglob('*.md'))
    # Comprobar referencias antes de generar un paquete que las deje inaccesibles.
    for path in texts:
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' not in target and not target.startswith('#'):
                if not (path.parent / target.split('#')[0]).is_file():
                    raise ValueError(f'Referencia ausente: {path.name}: {target}')
    parts = ['# Proceso de listas para ChatGPT\n\n'
             'Archivo generado. Editar el skill fuente y regenerar, no esta copia.\n'
             'Las referencias están incluidas por sección; leer solo lo necesario.\n'
             'El CSV de industrias se adjunta por separado. El script de consulta\n'
             'es opcional si el entorno permite ejecutar Python.\n']
    for path in texts:
        body = path.read_text()
        # Mantener enlaces web; convertir rutas relativas en nombres localizables
        # dentro del documento consolidado, sin enlaces rotos entre adjuntos.
        body = re.sub(r'\[([^]]+)\]\(([^)]+)\)',
                      lambda m: m.group(0) if '://' in m[2] or m[2].startswith('#')
                      else f'{m[1]} (referencia: {m[2]})', body)
        parts.append(f'\n---\n\n## Archivo: {path.relative_to(SKILL).as_posix()}\n\n{body}')
    meta = SKILL / 'references/taxonomia/industrias-linkedin-v2.meta.json'
    parts.append('\n---\n\n## Procedencia del CSV\n\n```json\n' + meta.read_text() + '\n```\n')
    chat = output / 'chatgpt'
    chat.mkdir(exist_ok=True)
    (chat / 'proceso-listas-chatgpt.md').write_text('\n'.join(parts))
    shutil.copyfile(SKILL / 'references/taxonomia/industrias-linkedin-v2.csv',
                    chat / 'industrias-linkedin-v2.csv')
    archive = output / 'creador-de-listas-linkedin.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for path in sorted(SKILL.rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and path.name != '.DS_Store':
                z.write(path, path.relative_to(SKILL.parent))
    return archive, chat


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    archive, chat = build(args.output)
    print(f'Skill: {archive}\nChatGPT: {chat}')
