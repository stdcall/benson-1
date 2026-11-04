"""Compile bibliography fixtures with the production reader and renderer."""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import fitz

ROOT = Path(__file__).resolve().parents[2]
BIB_KEY = re.compile(r'(?m)^@[A-Za-z]+\{([^,]+),')
HEADER = (
    '#import "content/book-style.typ": book-style\n'
    '#import "content/statements.typ": bib-item\n'
    '#import "content/bibliography-style.typ": bib-description, bib-part\n'
    '#show: book-style\n'
    '#set page(header: none, footer: none, numbering: "1")\n')


def bib_keys():
    return BIB_KEY.findall((ROOT / 'references.bib').read_text())


def items(*keys):
    return ''.join(f'#bib-item[#bib-description("{key}")] <bib:{key}>\n'
                   for key in keys)


def replace_in_record(bib, key, old, new):
    """Replace a field value inside one record of the .bib text."""
    match = re.search(r'(?ms)^@[A-Za-z]+\{' + key + r',\n.*?^\}\n', bib)
    assert match, key
    record = match[0]
    assert record.count(old) == 1, (key, old)
    return bib[:match.start()] + record.replace(old, new) + bib[match.end():]


class Bibliography(unittest.TestCase):
    def fixture(self, root, body):
        shutil.copytree(ROOT / 'content', root / 'content')
        shutil.copytree(ROOT / 'assets/fonts', root / 'assets/fonts')
        shutil.copyfile(ROOT / 'references.bib', root / 'references.bib')
        shutil.copyfile(ROOT / 'editorial.bib', root / 'editorial.bib')
        (root / 'sample.typ').write_text(HEADER + body)

    def run_typst(self, root, command, *extra):
        result = subprocess.run([
            'typst', command, '--root', str(root), '--ignore-system-fonts',
            '--font-path', str(root / 'assets/fonts'),
            *(['--in', str(root / 'sample.typ'), *extra]
              if command == 'eval' else [str(root / 'sample.typ'), *extra])],
            text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, '')
        return result.stdout

    def compile(self, root, name):
        self.run_typst(root, 'compile', str(root / name))
        with fitz.open(root / name) as doc:
            # Word joiners keep an en dash with its neighbours; in a DOI they
            # follow the hyphens, and zero-width spaces follow the slashes.
            text = ' '.join(
                ' '.join(p.get_text().replace('\u2060', '')
                         .replace('\u200b', '').split())
                for p in doc)
            # A DOI may break after a slash.
            text = text.replace('/ ', '/')
            links = [link for page in doc for link in page.get_links()]
        return text, links

    def mutate(self, root, *changes):
        bib = (root / 'references.bib').read_text()
        for key, old, new in changes:
            bib = replace_in_record(bib, key, old, new)
        (root / 'references.bib').write_text(bib)

    def test_bib_fields_control_printed_descriptions_and_doi_links(self):
        with tempfile.TemporaryDirectory(prefix='bib-test-', dir='/tmp') as tmp:
            root = Path(tmp)
            self.fixture(root, items('Aigner1979', 'Alperin1980a',
                                     'Kratzer1984'))
            before, links = self.compile(root, 'before.pdf')
            self.assertIn(
                'M. Aigner. Combinatorial theory. Grundlehren der Mat. Wiss. '
                '234, Springer-Verlag, Berlin/New York, 1979.', before)
            self.assertIn('J. L. Alperin. Diagrams for modules. J. Pure Appl. '
                          'Algebra 16 (1980), 111–119.', before)
            self.assertIn('C. Kratzer et J. Thévenaz.', before)
            uris = {x.get('uri') for x in links}
            self.assertIn('https://doi.org/10.1016/0022-4049(80)90010-9', uris)
            self.assertIn('DOI: 10.1007/978-1-4615-6666-3', before)
            self.assertNotIn('doi.org/10.1234', ' '.join(map(str, uris)))
            self.mutate(
                root,
                ('Aigner1979', 'title = {Combinatorial theory}',
                 'title = {Bibliography mutation probe}'),
                ('Aigner1979', 'author = {Aigner, M.}',
                 'author = {Changedauthor, I. and Second, J.}'),
                ('Aigner1979', 'publisher = {Springer-Verlag}',
                 'publisher = {Changed publisher}'),
                ('Aigner1979', 'doi = {10.1007/978-1-4615-6666-3}',
                 'doi = {10.1234/mutation-probe}'),
                ('Kratzer1984', 'usera = {et}', 'usera = {und}'))
            after, links = self.compile(root, 'after.pdf')
            self.assertIn('I. Changedauthor and J. Second. Bibliography '
                          'mutation probe. Grundlehren der Mat. Wiss. 234, '
                          'Changed publisher, Berlin/New York, 1979.', after)
            self.assertNotIn('Combinatorial theory', after)
            self.assertIn('C. Kratzer und J. Thévenaz.', after)
            self.assertIn('DOI: 10.1234/mutation-probe', after)
            self.assertIn('https://doi.org/10.1234/mutation-probe',
                          {x.get('uri') for x in links})

    def test_journal_language_and_related_components_reach_pdf(self):
        with tempfile.TemporaryDirectory(prefix='bib-test-', dir='/tmp') as tmp:
            root = Path(tmp)
            self.fixture(root, items('Bondarenko1975', 'Bessenrodt1982b',
                                     'Bessenrodt1982a', 'Drozd1977',
                                     'Dress1971a', 'Burnside1911'))
            before, links = self.compile(root, 'before.pdf')
            self.assertIn(
                'characteristic 2. (Russian), Mat. Sbornik 96 (1975), 63–74; '
                'translation: Math. USSR Sbornik 25 (1975), 58–68.', before)
            self.assertIn('DOI (translation): '
                          '10.1070/SM1975v025n01ABEH002197', before)
            self.assertIn('Comm. in Algebra 10 (2) (1982), 135–170.', before)
            self.assertIn('Proc. Amer. Math. Soc. 85 (1982), 520–522.', before)
            self.assertIn('104–114 (in Russian).', before)
            self.assertIn('Lecture notes, Bielefeld, Dec. 1971.', before)
            self.assertIn('ed., Cambridge Univ. Press, 1911.', before)
            uris = {x.get('uri') for x in links}
            self.assertIn(
                'https://doi.org/10.1070/SM1975v025n01ABEH002197', uris)
            # A field of a related component, the book's spelling of a
            # journal (userb), the verified abbreviation where the book's
            # spelling agrees with it, the language and a month.
            self.mutate(
                root,
                ('Bondarenko1975t', 'pages = {58--68}',
                 'pages = {9001--9002}'),
                ('Bessenrodt1982b', '  userb = {Comm. in Algebra},\n', ''),
                ('Bessenrodt1982a', 'shortjournal = {Proc. Amer. Math. Soc.}',
                 'shortjournal = {Journal mutation probe}'),
                ('Drozd1977', 'language = {russian}',
                 'language = {ukrainian}'),
                ('Dress1971a', 'month = {12}', 'month = {9}'))
            after, _ = self.compile(root, 'after.pdf')
            self.assertIn('Math. USSR Sbornik 25 (1975), 9001–9002.', after)
            self.assertIn('Comm. Algebra 10 (2) (1982), 135–170.', after)
            self.assertIn('Journal mutation probe 85 (1982)', after)
            self.assertIn('104–114 (in Ukrainian).', after)
            self.assertIn('Lecture notes, Bielefeld, Sept. 1971.', after)

    def test_backlinks_are_distinct_pages_and_exclude_internal_references(self):
        with tempfile.TemporaryDirectory(prefix='bib-test-', dir='/tmp') as tmp:
            root = Path(tmp)
            self.fixture(root, (
                'Mention [@bib:Aigner1979] and again [@bib:Aigner1979].\n'
                '#footnote[Another mention [@bib:Aigner1979].]\n'
                '#pagebreak()\nSecond page [@bib:Aigner1979].\n'
                '#pagebreak()\n'
                '#metadata((kind: "bibliography-boundary", enter: true))\n'
                + items('Aigner1979') +
                'Internal reference [@bib:Aigner1979].\n'
                '#metadata((kind: "bibliography-boundary", enter: false))\n'))
            text, links = self.compile(root, 'book.pdf')
            self.assertIn('[1] M. Aigner.', text)
            data = json.loads(self.run_typst(root, 'eval',
                'query(metadata).map(it => (value: '
                'if type(it.value) == dictionary { '
                '(..it.value, position: it.location().position()) '
                '} else { it.value }))'))
            backlinks = [x['value'] for x in data
                         if isinstance(x['value'], dict)
                         and x['value'].get('kind') == 'page-reference']
            self.assertEqual([x['description'] for x in backlinks], ['1', '2'])
            self.assertEqual([x['target-position']['page'] for x in backlinks],
                             [1, 2])
            page_links = [x for x in links
                          if x.get('kind') == fitz.LINK_GOTO
                          and x.get('page') in (0, 1)]
            self.assertGreaterEqual(len(page_links), 2)
            from pypdf import PdfWriter
            sys.path.insert(0, str(ROOT / 'scripts'))
            from check_links import check_links, set_link_descriptions
            writer = PdfWriter(root / 'book.pdf', incremental=True)
            set_link_descriptions(writer, backlinks)
            writer.write(root / 'described.pdf')
            report = check_links(root / 'described.pdf', backlinks)
            self.assertEqual(report['semantic_references_checked'], 2)
            self.assertTrue(all(x['destination-offset-pt'] == 18
                                for x in backlinks))
            wrong = [{k: v for k, v in x.items()
                      if k != 'destination-offset-pt'} for x in backlinks]
            with self.assertRaisesRegex(AssertionError, 'wrong target height'):
                check_links(root / 'described.pdf', wrong)

    def test_numbering_runs_through_the_further_references(self):
        with tempfile.TemporaryDirectory(prefix='bib-test-', dir='/tmp') as tmp:
            root = Path(tmp)
            self.fixture(root, (
                items('Aigner1979', 'Alperin1980a')
                + '#bib-part[Further references (added since the first '
                'edition):]\n' + items('Alperin1988')))
            text, _ = self.compile(root, 'book.pdf')
            data = json.loads(self.run_typst(root, 'eval', 'query(metadata)'))
            numbers = [x['value']['number'] for x in data
                       if isinstance(x['value'], dict)
                       and x['value'].get('family') == 'bib']
            self.assertEqual(numbers, [[1], [2], [3]])
            self.assertIn('[3] J. L. Alperin. Loewy structure', text)

    def test_keys_are_surname_and_year(self):
        sys.path.insert(0, str(ROOT / 'scripts'))
        from lint_typst import label_problem
        for key in bib_keys():
            self.assertRegex(key, r'^[A-Z][A-Za-z]*[0-9]{4}[a-z]?$')
            self.assertIsNone(label_problem('bib:' + key), key)

    def test_entry_file_contains_structure_and_keys_only(self):
        source = (ROOT / 'content/80-bibliography.typ').read_text()
        allowed = {
            '#heading(level: 1, numbering: none)[Bibliography]',
            '#bib-part[Further references (added since the first '
            'edition):]'}
        keys = []
        for line in source.splitlines():
            line = line.strip()
            if (not line or line.startswith(('#import', '//', '#metadata'))
                    or line in allowed):
                continue
            match = re.fullmatch(
                r'#bib-item(?:\(tag: "[0-9]+[a-z]?"\))?'
                r'\[#bib-description\("([A-Za-z][A-Za-z0-9]*)"\)\]'
                r' <bib:\1>', line)
            self.assertIsNotNone(match, line)
            keys.append(match[1])
        # The printed list: [1]-[210] and the further references [211]-[282].
        self.assertEqual(len(keys), 282)
        self.assertEqual(len(keys), len(set(keys)))
        self.assertLess(source.index('#bib-part'),
                        source.index('"Alperin1988"'))
        self.assertLess(source.index('"Zemanek1973"'),
                        source.index('#bib-part'))
        db_keys = bib_keys()
        self.assertEqual(len(db_keys), len(set(db_keys)))
        related = {key.strip()
                   for group in re.findall(
                       r'(?m)^  related = \{([^}]+)\}',
                       (ROOT / 'references.bib').read_text())
                   for key in group.split(',')}
        self.assertEqual(set(db_keys), set(keys) | related,
                         'Every data record is printed or a related component')
        self.assertFalse(set(keys) & related)
        cited = {key
                 for path in (ROOT / 'content').rglob('*.typ')
                 for key in re.findall(r'@bib:([A-Za-z0-9]+)',
                                       path.read_text())}
        editorial = set(BIB_KEY.findall((ROOT / 'editorial.bib').read_text()))
        self.assertFalse(editorial & set(db_keys))
        self.assertTrue(cited <= set(keys) | editorial,
                        cited - set(keys) - editorial)

    def test_editorial_references_print_every_editorial_record(self):
        source = (ROOT / 'content/81-editorial-references.typ').read_text()
        printed = re.findall(
            r'#editorial-bib-item\[\s*#bib-description\("([A-Za-z0-9]+)", '
            r'editorial: true\)\s*\] <bib:\1>', source)
        editorial = BIB_KEY.findall((ROOT / 'editorial.bib').read_text())
        self.assertEqual(printed, sorted(editorial))
        cited = {key
                 for path in (ROOT / 'content').rglob('*.typ')
                 if path.name != '81-editorial-references.typ'
                 for key in re.findall(r'@bib:([A-Za-z0-9]+)',
                                       path.read_text())}
        self.assertTrue(set(editorial) <= cited, set(editorial) - cited)


if __name__ == '__main__':
    unittest.main()
