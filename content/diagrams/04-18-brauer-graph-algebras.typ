#import "common.typ": cd, edge, node
#import "../main-defs.typ": *

// The Brauer graph of the example in Section 4.18 and what it determines.
// The graph is given by the places of its vertices, their multiplicities
// and its edges, each with the two vertices at its ends; the cyclic ordering
// of the edges round a vertex is anticlockwise in the picture, as in the
// text, and is computed from the places. From it follow the projective
// indecomposable modules of a Brauer graph algebra (Definition 4.18.1) and
// its Ext-quiver.

#let brauer-graph = (
  // Places on a grid, the rows counted downwards.
  vertices: (u: (-1, 0), v: (1, 0), w: (0, 1), x: (0, 2)),
  multiplicity: (u: 3),
  // An edge: the simple module, its ends and the side of its label.
  edges: (
    (name: "1", ends: ("u", "v"), side: left),
    (name: "2", ends: ("u", "w"), side: right),
    (name: "3", ends: ("v", "w"), side: left),
    (name: "4", ends: ("w", "x"), side: right),
  ),
)

#let simple(name) = $S_#name$

// The edges at a vertex, in anticlockwise order of their directions in the
// picture (rows are counted downwards).
#let edges-around(graph, vertex) = {
  let (x0, y0) = graph.vertices.at(vertex)
  graph
    .edges
    .filter(e => vertex in e.ends)
    .map(e => {
      let other = e.ends.find(end => end != vertex)
      let (x1, y1) = graph.vertices.at(other)
      (e.name, calc.atan2(x1 - x0, y0 - y1))
    })
    .sorted(key: ((_, angle)) => angle.deg())
    .map(((name, _)) => name)
}

// The uniserial module of Definition 4.18.1 for the edge j at the vertex u:
// the edges after j in the cyclic order round u, then j, the whole e_u
// times, without the last j.
#let uniserial(graph, vertex, j) = {
  let order = edges-around(graph, vertex)
  let start = order.position(name => name == j)
  let turn = order.slice(start + 1) + order.slice(0, start + 1)
  let e = graph.multiplicity.at(vertex, default: 1)
  (turn * e).slice(0, -1)
}

// The Brauer graph: dots joined by its edges, labelled by the simple
// modules; a multiplicity greater than one stands to the left of its vertex.
#let brauer-graph-picture = {
  let g = brauer-graph
  cd(
    spacing: 0pt,
    cell-size: 11mm,
    node-inset: 0pt,
    node-outset: 1.2mm,
    ..g
      .vertices
      .pairs()
      .map(((name, place)) => node(
        place,
        [],
        shape: circle,
        radius: 0.6mm,
        fill: black,
      )),
    ..g
      .multiplicity
      .pairs()
      .map(((name, e)) => {
        let (x, y) = g.vertices.at(name)
        node((x - 0.35, y), $#e$, outset: 0pt)
      }),
    ..g.edges.map(e => edge(
      g.vertices.at(e.ends.first()),
      g.vertices.at(e.ends.last()),
      simple(e.name),
      "-",
      label-side: e.side,
    )),
  )
}

// The projective indecomposable module P_j: S_j at the top and at the
// bottom, and between them the uniserial modules for the two ends of the
// edge j side by side (the first end on the left). A column of m factors
// in a module of height h (the longer column) stands at the heights
// i(h + 1)/(m + 1), and every height met is one row of the picture, as
// printed.
#let projective-diagram(graph, j) = {
  let e = graph.edges.find(e => e.name == j)
  let columns = e
    .ends
    .map(vertex => uniserial(graph, vertex, j))
    .filter(c => c.len() > 0)
  let h = calc.max(..columns.map(c => c.len()))
  let placed = columns
    .enumerate()
    .map(((side, c)) => c
      .enumerate()
      .map(((i, name)) => (
        level: (i + 1) * (h + 1) / (c.len() + 1),
        side: side,
        name: name,
      )))
    .join()
  let levels = placed.map(p => p.level).dedup().sorted()
  let cells = (grid.cell(colspan: columns.len(), align(center, simple(j))),)
  for level in levels {
    for side in range(columns.len()) {
      let here = placed.find(p => p.level == level and p.side == side)
      cells.push(if here == none { [] } else { simple(here.name) })
    }
  }
  cells.push(grid.cell(colspan: columns.len(), align(center, simple(j))))
  grid(
    columns: columns.len(),
    column-gutter: 1.2em,
    row-gutter: 0.6em,
    ..cells,
  )
}

// The projective modules of the example, side by side, centred on a common
// line.
#let projective-modules = grid(
  columns: brauer-graph.edges.len(),
  column-gutter: 12mm,
  align: horizon,
  ..brauer-graph.edges.map(e => projective-diagram(brauer-graph, e.name)),
)

// The Ext-quiver: a vertex for each edge of the Brauer graph and, round each
// vertex of the graph of valency or multiplicity greater than one, the
// cycle of arrows from each edge to the next in the cyclic order. Each of
// two opposite arrows bends to its right. `places` gives the place of each
// vertex, `names` the name of each arrow and the side of its label.
#let ext-quiver = {
  let g = brauer-graph
  let places = ("1": (0, 0), "2": (-1, 1), "3": (1, 1), "4": (0, 2))
  let names = (
    "1-2": ($alpha$, right),
    "2-1": ($beta$, right),
    "3-1": ($gamma$, right),
    "1-3": ($delta$, right),
    "3-2": ($epsilon$, left),
    "2-4": ($zeta$, right),
    "4-3": ($eta$, right),
  )
  let arrows = ()
  for vertex in g.vertices.keys() {
    let order = edges-around(g, vertex)
    if order.len() > 1 or g.multiplicity.at(vertex, default: 1) > 1 {
      assert(order.len() > 1, message: "no loops in this example")
      for (i, from) in order.enumerate() {
        arrows.push((from, order.at(calc.rem(i + 1, order.len()))))
      }
    }
  }
  let keys = arrows.map(((from, to)) => from + "-" + to)
  assert(
    keys.sorted() == names.keys().sorted(),
    message: "every arrow is named",
  )
  cd(
    spacing: 0pt,
    cell-size: 14mm,
    node-inset: 0pt,
    node-outset: 1mm,
    ..places
      .values()
      .map(place => node(
        place,
        [],
        shape: circle,
        radius: 0.6mm,
        fill: black,
      )),
    ..arrows.map(((from, to)) => {
      let (name, side) = names.at(from + "-" + to)
      let opposite = (to + "-" + from) in keys
      edge(
        places.at(from),
        places.at(to),
        name,
        "->",
        bend: if opposite { -22deg } else { 0deg },
        label-side: side,
      )
    }),
  )
}
