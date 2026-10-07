"""Consulta acotada del catálogo local. Usa etiquetas inglesas o IDs oficiales."""
import argparse, csv, json
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('terminos', nargs='+', help='Coincidencia OR en etiqueta/jerarquía, o ID exacto')
p.add_argument('--descripciones', action='store_true', help='Buscar y mostrar también la definición')
p.add_argument('--incluir-inactivas', action='store_true')
p.add_argument('--limite', type=int, default=20)
a=p.parse_args()
if a.limite < 1 or a.limite > 100: p.error('--limite debe estar entre 1 y 100')
with Path(__file__).with_name('industrias-linkedin-v2.csv').open(encoding='utf-8-sig', newline='') as f:
    rows=list(csv.DictReader(f))
fields=['label','hierarchy'] + (['description'] if a.descripciones else [])
hits=[]
for r in rows:
    if r['status'] != 'active' and not a.incluir_inactivas: continue
    corpus=' '.join(r[k] for k in fields).casefold()
    if any((t == r['industry_id']) if t.isdigit() else (t.casefold() in corpus) for t in a.terminos):
        hits.append(r if a.descripciones else {k:v for k,v in r.items() if k != 'description'})
print(json.dumps({'total':len(hits),'mostrados':min(len(hits),a.limite),'resultados':hits[:a.limite]},ensure_ascii=False,indent=2))
