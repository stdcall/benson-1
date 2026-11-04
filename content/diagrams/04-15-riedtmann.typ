#import "common.typ": cd, edge, node
#import "../main-defs.typ": *

// The quivers of Section 4.15 are built from a directed tree B, given by the
// row in which each of its vertices is drawn and by its arrows x → y. Each
// arrow leads one column to the right, which fixes the column of every
// vertex. The vertex (n, x) of ℤB stands in the row of x, 2n columns to the
// left of x: both arrows (n, x) → (n, y) and (n, y) → (n − 1, x) of ℤB then
// lead one column to the right, and the translation τ(n, x) = (n + 1, x)
// two columns to the left.

// A vertex is a dot. A picture of a quiver is drawn on a square grid of the
// given unit, its arrows stopping short of the dots, as printed; set in a
// line of text or of a formula, it is centred on the axis of the formula,
// or, if `axis` is given, that row of the picture is: rows are counted
// upwards from the lowest one, a row of dots, at whose foot the picture
// ends.
#let dot-radius = 0.6mm
#let dot(position, outset: auto) = node(
  position,
  [],
  shape: circle,
  radius: dot-radius,
  fill: black,
  outset: outset,
)
#let quiver-picture(unit, axis: none, ..items) = {
  let height = if axis == none { 50% } else { axis * unit + dot-radius }
  box(baseline: height - 0.25em, cd(
    spacing: 0pt,
    cell-size: unit,
    node-inset: 0pt,
    node-outset: 0.4mm,
    mark-scale: 140%,
    ..items,
  ))
}

// The column of each vertex of a directed tree, counted from its first
// vertex.
#let tree-columns(tree) = {
  let vertices = tree.rows.keys()
  assert(
    tree.arrows.len() == vertices.len() - 1,
    message: "a tree has one arrow fewer than vertices",
  )
  let column = ((vertices.first()): 0)
  for _ in vertices {
    for (x, y) in tree.arrows {
      if x in column and y not in column {
        column.insert(y, column.at(x) + 1)
      } else if y in column and x not in column {
        column.insert(x, column.at(y) - 1)
      }
    }
  }
  assert(column.len() == vertices.len(), message: "a tree is connected")
  column
}

// The place of a vertex in a picture: rows are counted upwards.
#let place-at(column, row) = (column, -row)

// The directed tree B itself.
#let tree-quiver(tree, unit: 4.75mm) = {
  let column = tree-columns(tree)
  let at(x) = place-at(column.at(x), tree.rows.at(x))
  quiver-picture(
    unit,
    ..tree.rows.keys().map(x => dot(at(x))),
    ..tree.arrows.map(((x, y)) => edge(at(x), at(y), "->")),
  )
}

// The graph B̄ of a directed tree: its vertices in their rows, each shifted
// to the left by its row, so that a path upwards becomes a vertical line,
// joined by undirected edges, which meet the dots.
#let tree-graph(tree, unit: 4.75mm) = {
  let column = tree-columns(tree)
  let at(x) = place-at(column.at(x) - tree.rows.at(x), tree.rows.at(x))
  quiver-picture(
    unit,
    ..tree.rows.keys().map(x => dot(at(x), outset: 0pt)),
    ..tree.arrows.map(((x, y)) => edge(at(x), at(y), "-")),
  )
}

// The stable representation quiver ℤB, drawn for the integers n in
// `copies` and, if `window` is given, only in the columns between its two
// ends; `marks` are further labels (dots for the parts left out) at given
// places; `axis` is the row of B set on the axis of the formula.
#let zb-quiver(
  tree,
  copies,
  window: none,
  marks: (),
  axis: none,
  unit: 4.75mm,
) = {
  let column = tree-columns(tree)
  let at(n, x) = place-at(column.at(x) - 2 * n, tree.rows.at(x))
  let shown(n, x) = (
    n in copies
      and (
        window == none
          or (
            window.first() <= at(n, x).first()
              and at(n, x).first() <= window.last()
          )
      )
  )
  let vertices = ()
  let arrows = ()
  for n in copies {
    for x in tree.rows.keys() {
      if shown(n, x) { vertices.push(dot(at(n, x))) }
    }
    for (x, y) in tree.arrows {
      if shown(n, x) and shown(n, y) {
        arrows.push(edge(at(n, x), at(n, y), "->"))
      }
      if shown(n, y) and shown(n - 1, x) {
        arrows.push(edge(at(n, y), at(n - 1, x), "->"))
      }
    }
  }
  let lowest = calc.min(..tree.rows.values())
  assert(
    marks.all(((position, _)) => -position.last() >= lowest),
    message: "the lowest row of a picture is a row of vertices",
  )
  quiver-picture(
    unit,
    axis: if axis != none { axis - lowest },
    ..vertices,
    ..arrows,
    ..marks.map(((position, label)) => node(position, label)),
  )
}

// The examples after Definition 4.15.1: a tree with a branch at its third
// vertex, drawn as printed, and a second tree with the same graph. ℤB is
// drawn for four copies of B.
#let example-tree = (
  rows: (a: 0, b: 1, c: 2, d: 3, e: 2),
  arrows: (("a", "b"), ("b", "c"), ("c", "d"), ("c", "e")),
)
#let other-tree = (
  rows: (b: 1, c: 2, d: 3, e: 2, a: 0),
  arrows: (("b", "c"), ("c", "d"), ("c", "e"), ("b", "a")),
)
#let example-copies = range(-3, 1)

// The Example after Definition 4.15.4: ℤA∞, of which the five lowest rows
// are drawn in twelve columns, with dots for the parts left out; "ℤB = ⋯"
// stands on the level of the fourth row.
#let a-infinity-rows = 5
#let a-infinity = (
  rows: range(a-infinity-rows).map(i => (str(i), i)).to-dict(),
  arrows: range(a-infinity-rows - 1).map(i => (str(i), str(i + 1))),
)
#let a-infinity-quiver = zb-quiver(
  a-infinity,
  range(-6, 3),
  window: (0, 11),
  marks: (
    ((2, -a-infinity-rows), $dots.v$),
    ((6, -a-infinity-rows), $dots.v$),
    ((-0.2, -3), $dots.c$),
    ((-0.7, -1), $dots.c$),
    ((12, -2), $dots.c$),
  ),
  axis: 3,
  unit: 7mm,
)

// Lemma 4.15.5: the lift ψ of π through the covering φ, dotted.
#let covering-lift = cd(
  spacing: (9mm, 9mm),
  node((1, 0), $ZZ B$),
  node((0, 1), $Q'$),
  node((1, 1), $Q$),
  edge((1, 0), (1, 1), $pi$, "->", label-side: left),
  edge((0, 1), (1, 1), $phi.alt$, "->", label-side: left),
  edge((1, 0), (0, 1), $psi$, "..>", label-side: right),
)
