"""Comprobaciones de portabilidad e integridad, sin acceso a LinkedIn."""
import csv
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package', ROOT / 'scripts/empaquetar.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)
TAX = package.SKILL / 'references/taxonomia'


class PackageTests(unittest.TestCase):
    def test_portable_package(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive, chat = package.build(tmp)
            with zipfile.ZipFile(archive) as z:
                self.assertIsNone(z.testzip())
                expected = {str(p.relative_to(package.SKILL.parent))
                            for p in package.SKILL.rglob('*') if p.is_file()
                            and '__pycache__' not in p.parts and p.name != '.DS_Store'}
                self.assertEqual(set(z.namelist()), expected)
                # Cada archivo distribuido debe coincidir con su fuente.
                for name in expected:
                    self.assertEqual(z.read(name), (ROOT / name).read_bytes())
            self.assertEqual((chat / 'industrias-linkedin-v2.csv').read_bytes(),
                             (TAX / 'industrias-linkedin-v2.csv').read_bytes())
            text = (chat / 'proceso-listas-chatgpt.md').read_text()
            for p in [package.SKILL / 'SKILL.md'] + list((package.SKILL / 'references').rglob('*.md')):
                self.assertIn(f'## Archivo: {p.relative_to(package.SKILL).as_posix()}', text)
            self.assertIn('csv_sha256', text)

    def test_taxonomy_integrity(self):
        raw = (TAX / 'industrias-linkedin-v2.csv').read_bytes()
        meta = json.loads((TAX / 'industrias-linkedin-v2.meta.json').read_text())
        self.assertEqual(hashlib.sha256(raw).hexdigest(), meta['csv_sha256'])
        with (TAX / 'industrias-linkedin-v2.csv').open(encoding='utf-8-sig', newline='') as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), meta['rows'])
        self.assertEqual(len({r['industry_id'] for r in rows}), len(rows))
        for status, count in meta['by_status'].items():
            self.assertEqual(sum(r['status'] == status for r in rows), count)

    def test_query_from_other_directory(self):
        script = TAX / 'consultar-industrias.py'
        with tempfile.TemporaryDirectory() as tmp:
            def run(*args):
                return subprocess.run([sys.executable, str(script), *args], cwd=tmp,
                                      text=True, capture_output=True)
            exact = json.loads(run('118', '--descripciones').stdout)
            self.assertEqual(exact['total'], 1)
            self.assertEqual(exact['resultados'][0]['industry_id'], '118')
            self.assertEqual(exact['resultados'][0]['status'], 'active')
            limited = json.loads(run('services', '--limite', '1').stdout)
            self.assertGreater(limited['total'], 1)
            self.assertEqual(len(limited['resultados']), 1)
            self.assertNotEqual(run('118', '--limite', '0').returncode, 0)
            self.assertEqual(json.loads(run('impossible-category-xyz').stdout)['total'], 0)


if __name__ == '__main__':
    unittest.main()
