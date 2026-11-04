# Checks kept with the edition

Independent checks of statements from D. J. Benson, *Representations and
Cohomology I: Basic representation theory of finite groups and associative
algebras* (Cambridge Studies in Advanced Mathematics 30, second edition,
1998). They supplement, and never replace, reading the text against the
printed book: none of them establishes that our text matches the book.

* `tests/` — `just test` (and `just check`, and CI): the schema of
  `corrections.json`; the label forms; the bibliography (`references.bib`
  and the printed list of `content/80-bibliography.typ` have the same keys,
  the numbers [1]–[282] are counted in the printed order and run on through
  the further references of the second edition, every citation names an
  entry, `editorial.bib` is printed in full in the Editorial references and
  every one of its works is cited); the numbering (an inserted statement
  renumbers the following ones and every reference to them); the layout of
  statements, lists and proofs; the index; the passage labels of
  `lean-proofs.json`; and unit tests of the lint.
* `sage/` — `just check-sage` runs every script here with `sage -python`, so
  each script is plain Python that imports `sage.all` (last run with
  SageMath 10.9; CI uses the official SageMath container). One script per
  chapter or half chapter (`chapter-1.py` … `chapter-6.py`), exact
  computations over finite fields, the integers and number fields, with
  GAP through `libgap` (MeatAxe, character tables, tables of marks): for
  example radicals, socles and Loewy series, Wedderburn and block
  decompositions, Cartan and decomposition matrices, Ext and Tor from
  minimal resolutions, the Künneth formulas, Mackey decompositions,
  vertices, sources and Green correspondents, Jennings bases, quiver
  representations and the Dynkin and Euclidean diagrams, almost split
  sequences and Auslander–Reiten quivers of small algebras, string and band
  modules for dihedral groups, Burnside rings and tables of marks,
  induction theorems, the forms on representation rings, Brauer trees and
  the blocks with Klein four defect groups. Each docstring states what is
  checked, where each expected value comes from (printed page and label of
  this edition) and what the script does not establish. Expected values are
  the book's; where the book is wrong, the printed reading is kept as a
  refuted check beside the corrected one. Every script fails on a false
  check and ends with `ok chapter-…: N checks`.
* `lean/` — a Lake project (Lean 4, mathlib pinned in `lakefile.toml`) with
  formalizations of important bounded steps of the book, one file per
  claim; the header of each file names the place in the book, maps the
  book's notation and lists what is not covered. `lean-proofs.json` records
  each file's declarations, the claim and its limits, and the labels of the
  passages it checks (`passages`); `just check-lean` and `just test` fail
  if one of these labels is missing from `content/`. When such a passage or
  proof changes, review their correspondence. `just check-lean`
  (`lean/check_axioms.py`) compiles every file, rejects errors, warnings
  and `sorry`, and allows only the axioms propext, Classical.choice and
  Quot.sound. By default it runs in `checks/lean` after `lake build` there,
  as the `lean` job of CI does; with `LEAN_MATHLIB` (or `--mathlib`) set to
  a prebuilt mathlib checkout of the pinned commit it compiles there
  instead, building and fetching nothing.
* `harper-dictionary.txt` — vocabulary for `just check-prose` (Harper). The
  prose check is advisory and never fails a build.

`corrections.json` at the top of the repository is the journal of the
corrections: for each entry the printed page and place, the printed reading,
the correction, the reason and how it was verified (`verified_by`: the
printed text and its context, the author's list of corrections, a script or
Lean file of this directory, or a book or article of the literature).
`just corrections` builds the reader's list from it.
