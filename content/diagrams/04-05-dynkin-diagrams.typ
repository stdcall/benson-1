// The labelled graphs of Section 4.5 in CeTZ: the Dynkin and Euclidean
// diagrams of Definition 4.5.1 and the pictures of the proofs.
//
// A labelled graph (Definition 4.1.9) is given by its edges (x, y, a, b):
// the vertices x and y, numbered from 0, and the values a = _x d_y and
// b = _y d_x. An edge valued (1, 1) is a line; (2, 1) and (3, 1) are the
// double and triple arrows from x to y of the text after Definition 4.5.1,
// (1, 2) and (1, 3) those from y to x; other values are printed over the
// line. The Cartan matrix
// c_xy = 2δ_xy - Σ _x d_y (Definition 4.5.3) is computed from the edges, and
// the numbers attached to the vertices are checked to form an additive
// function, Σ_x n_x c_xy = 0, at every vertex all of whose neighbours are
// drawn (Lemma 4.5.5 (i), Proposition 4.5.7). The finite Dynkin diagrams are
// checked to have a positive definite symmetrised Cartan matrix
// (Proposition 4.6.3 (i)).
//
// The layout comes from the structure. The vertices of the path (by default
// the longest path from the vertex 0) stand in a row one unit apart;
// `hidden` ones are left out, a run of them leaving a gap "— ··· —", and an
// `open` end trails off "— ···". A vertex off the path joined to two path
// vertices closes a cycle above the middle of the row (Ã_n); a leaf at the
// second vertex from an end of the path forms a fork with the end vertex
// (D_n); every other vertex hangs above its neighbour (E_n). A series is
// drawn from one of its members, in which each gap hides two vertices.
#import "@preview/cetz:0.5.2"

// The measures of the book: the distance of neighbouring vertices and the
// radius of a vertex; in units, the half height of a fork and the height of
// the top of a cycle (that of a step of an arm is given with each graph).
#let unit = 6mm
#let radius = 0.6mm
#let fork = 0.6
#let apex = 1.15
// Lines of a multiple edge are this far apart; its arrowhead is so long and
// so wide on each side of the axis.
#let spacing = ("2": 0.63mm, "3": 0.68mm)
#let head = (length: 1.35mm, half: ("2": 0.8mm, "3": 0.93mm))

// The row x_0 — x_1 — … of edges with the given values, from the vertex
// `from`.
#let chain(..values, from: 0) = {
  let pairs = values.pos().enumerate()
  pairs.map(((k, (a, b))) => (from + k, from + k + 1, a, b))
}
#let line-edge = (1, 1)

// The Cartan matrix c_xy = 2δ_xy - Σ _x d_y of the edges (Definition 4.5.3).
#let cartan(edges) = {
  let n = calc.max(..edges.map(((x, y, ..)) => calc.max(x, y))) + 1
  let c = range(n).map(x => range(n).map(y => if x == y { 2 } else { 0 }))
  for (x, y, a, b) in edges {
    c.at(x).at(y) -= a
    c.at(y).at(x) -= b
  }
  c
}

// The longest path from the vertex 0 in a graph without cycles; of two
// equally long ones the first by the numbering.
#let longest-path(n, neighbours) = {
  let walk(v, previous) = {
    let best = ()
    for w in neighbours.at(v) {
      if w != previous {
        let tail = walk(w, v)
        if tail.len() > best.len() { best = tail }
      }
    }
    (v,) + best
  }
  walk(0, none)
}

// A labelled graph and its view. `marks` are the numbers attached to the
// vertices (an additive function, checked), `labels` other labels; `arm` is
// the height of a step of an arm; `finite: true` checks a finite Dynkin
// diagram; `values: true` prints the values of every edge over a line.
#let graph(
  edges,
  path: none,
  hidden: (),
  open: (),
  marks: none,
  labels: none,
  arm: 1,
  finite: false,
  values: false,
) = {
  let n = calc.max(..edges.map(((x, y, ..)) => calc.max(x, y))) + 1
  let neighbours = range(n).map(v => edges
    .filter(((x, y, ..)) => x == v or y == v)
    .map(((x, y, ..)) => if x == v { y } else { x })
    .sorted())
  let c = cartan(edges)
  let path = if path == none { longest-path(n, neighbours) } else { path }
  if marks != none {
    assert(marks.len() == n, message: "a mark for every vertex")
    let ends = (
      (if "start" in open { path.first() }),
      (if "end" in open { path.last() }),
    )
    for y in range(n).filter(y => y not in ends) {
      assert(
        range(n).map(x => marks.at(x) * c.at(x).at(y)).sum() == 0,
        message: "the marks are not an additive function",
      )
    }
  }
  if finite {
    // The symmetrised Cartan matrix c_xy f_y, with _x d_y f_y = _y d_x f_x
    // (a tree), has positive leading principal minors.
    let f = (1,) + range(n - 1).map(_ => none)
    for _ in range(n) {
      for (x, y, a, b) in edges {
        if f.at(x) != none and f.at(y) == none { f.at(y) = f.at(x) * b / a }
        if f.at(y) != none and f.at(x) == none { f.at(x) = f.at(y) * a / b }
      }
    }
    let m = range(n).map(x => range(n).map(y => c.at(x).at(y) * f.at(y)))
    assert(
      range(n).all(x => range(n).all(y => (
        calc.abs(m.at(x).at(y) - m.at(y).at(x)) < 1e-9
      ))),
      message: "not a valued graph",
    )
    for k in range(n) {
      let pivot = m.at(k).at(k)
      assert(pivot > 1e-9, message: "not positive definite")
      for i in range(k + 1, n) {
        let q = m.at(i).at(k) / pivot
        for j in range(k, n) { m.at(i).at(j) -= q * m.at(k).at(j) }
      }
    }
  }
  // Positions in units, and the side of each label.
  let at = (:)
  let side = (:)
  for (k, v) in path.enumerate() {
    at.insert(str(v), (k, 0))
    side.insert(str(v), "below")
  }
  let placed = path
  while placed.len() < n {
    let v = range(n).find(v => (
      v not in placed and neighbours.at(v).any(w => w in placed)
    ))
    let next = neighbours.at(v).filter(w => w in placed)
    let (px, py) = at.at(str(next.first()))
    if next.len() == 2 {
      // The top of a cycle, above the middle of the row.
      let (qx, _) = at.at(str(next.last()))
      at.insert(str(v), ((px + qx) / 2, apex))
      side.insert(str(v), "super-left")
    } else {
      let k = path.position(w => w == next.first())
      let end = if k == 1 { path.first() } else if k == path.len() - 2 {
        path.last()
      }
      if (
        k != none
          and end != none
          and neighbours.at(v).len() == 1
          and neighbours.at(end).len() == 1
      ) {
        // A fork: the end vertex and the leaf, one unit outwards.
        let (ex, _) = at.at(str(end))
        at.insert(str(end), (ex, fork))
        at.insert(str(v), (ex, -fork))
        let inwards = ex < px
        side.insert(str(end), if inwards { "super" } else { "super-left" })
        side.insert(str(v), if inwards { "below" } else { "below-left" })
        if not inwards { side.insert(str(next.first()), "below-left") }
      } else {
        at.insert(str(v), (px, py + arm))
        side.insert(str(v), "sub")
      }
    }
    placed.push(v)
  }
  let labels = if labels != none { labels } else if marks != none {
    marks.map(m => [$#m$])
  }
  (
    edges: edges,
    path: path,
    hidden: hidden,
    open: open,
    at: at,
    side: side,
    labels: labels,
    values: values,
  )
}

// A label in the script style of the formulas: `$n_0+n'_0$` as printed,
// without the spaces of the text style.
#let small(body) = {
  let body = if body.func() == math.equation { body.body } else { body }
  $script(#body)$
}

// The drawing.
// The drawing commands of a labelled graph, its row on the x-axis.
#let strokes(g) = {
  import cetz.draw: circle, content, line, set-style
  let u = unit / 1mm
  let r = radius / 1mm
  set-style(stroke: 0.4pt, content: (padding: 0.35))
  let shown(v) = v not in g.hidden
  let point(v) = {
    let (x, y) = g.at.at(str(v))
    (x * u, y * u)
  }
  // Direction, normal and length of the segment between two vertices.
  let frame(p, q) = {
    let (x1, y1) = p
    let (x2, y2) = q
    let length = calc.sqrt(calc.pow(x2 - x1, 2) + calc.pow(y2 - y1, 2))
    let d = ((x2 - x1) / length, (y2 - y1) / length)
    (from: p, d: d, n: (-d.at(1), d.at(0)), length: length)
  }
  // The point at distance s along the segment, t along the normal.
  let along(f, s, t) = (
    f.from.at(0) + s * f.d.at(0) + t * f.n.at(0),
    f.from.at(1) + s * f.d.at(1) + t * f.n.at(1),
  )
  // Three dots centred at distance s along a row.
  let dots(f, s) = for k in (-1, 0, 1) {
    circle(
      along(f, s + k * 0.24 * u, 0),
      radius: 0.2,
      fill: black,
      stroke: none,
    )
  }
  for (x, y, a, b) in g.edges {
    if not (shown(x) and shown(y)) { continue }
    let arrow = (
      not g.values and calc.min(a, b) == 1 and calc.max(a, b) in (2, 3)
    )
    if not arrow {
      line(point(x), point(y))
      if g.values or (a, b) != line-edge {
        let f = frame(point(x), point(y))
        let label = small([(#a,#b)])
        content(along(f, f.length / 2, 0.3), label, anchor: "south")
      }
    } else {
      // The arrow from x to y (a > b): `a` lines from the dot of x into the
      // head, whose tip touches the dot of y.
      let (x, y, a) = if a > b { (x, y, a) } else { (y, x, b) }
      let f = frame(point(x), point(y))
      let tip = f.length - r - 0.1
      let back = tip - head.length / 1mm
      let half = head.half.at(str(a)) / 1mm
      for i in range(a) {
        let t = (i - (a - 1) / 2) * spacing.at(str(a)) / 1mm
        let end = back + (tip - back) * (half - calc.abs(t)) / half
        line(along(f, r + 0.1, t), along(f, end, t))
      }
      line(along(f, back, half), along(f, tip, 0), along(f, back, -half))
    }
  }
  // Gaps in the row and open ends.
  let row = g.path
  let drawn = row.enumerate().filter(((_, v)) => shown(v))
  for ((i, v), (j, w)) in drawn.zip(drawn.slice(1)) {
    if j > i + 1 {
      let f = frame(point(v), point(w))
      line(point(v), along(f, 0.85 * u, 0))
      line(along(f, f.length - 0.85 * u, 0), point(w))
      dots(f, f.length / 2)
    }
  }
  for (end, before) in (("start", row.at(1)), ("end", row.at(-2))) {
    if end in g.open {
      // Away from the neighbour in the row.
      let v = point(if end == "start" { row.first() } else { row.last() })
      let w = point(before)
      let f = frame(v, (2 * v.at(0) - w.at(0), 2 * v.at(1) - w.at(1)))
      line(v, along(f, 0.85 * u, 0))
      dots(f, 1.5 * u)
    }
  }
  // The vertices and their labels: below and to the right like a subscript,
  // or to the left if an edge leaves there; beside the vertices of an arm;
  // above the upper leaf of a fork and the top of a cycle.
  for v in g.at.keys().map(int).filter(shown) {
    circle(point(v), radius: r, fill: black, stroke: none, name: "v")
    if g.labels != none and g.labels.at(v) != none {
      let body = small(g.labels.at(v))
      let (x, y) = point(v)
      let s = g.side.at(str(v))
      if s == "below" {
        content((x + r, y - r), body, anchor: "north")
      } else if s == "below-left" {
        content((x - r, y - r), body, anchor: "north")
      } else if s == "sub" {
        content("v.east", body, anchor: "north-west")
      } else if s == "super" {
        content("v.north-east", body, anchor: "south-west")
      } else {
        content("v.north-west", body, anchor: "south-east")
      }
    }
  }
}
#let draw(g) = cetz.canvas(length: 1mm, strokes(g))

#let s = line-edge

// Definition 4.5.1 (i): the finite Dynkin diagrams (n vertices); a series is
// drawn from a member with as many vertices on either side of its gap as
// printed.
#let dynkin = (
  (
    A: graph(chain(s, s, s, s, s, s), hidden: (3, 4), finite: true),
    B: graph(chain((1, 2), s, s, s, s, s), hidden: (3, 4), finite: true),
    C: graph(chain((2, 1), s, s, s, s, s), hidden: (3, 4), finite: true),
    D: graph(
      chain(s, s, s, s, s, s) + ((1, 7, 1, 1),),
      hidden: (3, 4),
      finite: true,
    ),
    E6: graph(chain(s, s, s, s) + ((2, 5, 1, 1),), finite: true),
    E7: graph(chain(s, s, s, s, s) + ((2, 6, 1, 1),), finite: true),
    E8: graph(chain(s, s, s, s, s, s) + ((2, 7, 1, 1),), finite: true),
    F4: graph(chain(s, (2, 1), s), finite: true),
    G2: graph(chain((3, 1)), finite: true),
  )
    .pairs()
    .map(((name, g)) => (name, draw(g)))
    .to-dict()
)

// The Cartan matrix of F_4 printed after Definition 4.5.3.
#assert(
  cartan(chain(s, (2, 1), s))
    == ((2, -1, 0, 0), (-1, 2, -2, 0), (0, -1, 2, -1), (0, 0, -1, 2)),
  message: "not the Cartan matrix of F4 of Definition 4.5.3",
)

// Definition 4.5.1 (ii): the infinite Dynkin diagrams, with their additive
// functions.
#let infinite-dynkin = (
  (
    A: graph(chain(s, s), open: ("end",), marks: (1, 2, 3)),
    B: graph(chain((1, 2), s), open: ("end",), marks: (1, 1, 1)),
    C: graph(chain((2, 1), s), open: ("end",), marks: (1, 2, 2)),
    D: graph(
      chain(s, s) + ((1, 3, 1, 1),),
      open: ("end",),
      marks: (1, 2, 2, 1),
    ),
    A2: graph(chain(s, s), open: ("start", "end"), marks: (1, 1, 1)),
  )
    .pairs()
    .map(((name, g)) => (name, draw(g)))
    .to-dict()
)

// Definition 4.5.1 (iii): the Euclidean diagrams (n + 1 vertices), with
// their additive functions; a series is drawn from a member with as many
// vertices on either side of its gap as printed.
#let euclidean = (
  (
    A: graph(
      chain(s, s, s, s, s, s, s) + ((0, 8, 1, 1), (7, 8, 1, 1)),
      path: range(8),
      hidden: (3, 4),
      marks: (1,) * 9,
    ),
    A11: graph(((0, 1, 1, 4),), marks: (2, 1)),
    A12: graph(((0, 1, 2, 2),), marks: (1, 1)),
    B: graph(
      chain((1, 2), s, s, s, s, s, (2, 1)),
      hidden: (3, 4),
      marks: (1,) * 8,
    ),
    C: graph(
      chain((2, 1), s, s, s, s, s, (1, 2)),
      hidden: (3, 4),
      marks: (1, 2, 2, 2, 2, 2, 2, 1),
    ),
    D: graph(
      chain(s, s, s, s, s, s, s) + ((1, 8, 1, 1), (6, 9, 1, 1)),
      hidden: (3, 4),
      marks: (1, 2, 2, 2, 2, 2, 2, 1, 1, 1),
    ),
    BC: graph(
      chain((1, 2), s, s, s, s, s, (1, 2)),
      hidden: (3, 4),
      marks: (2, 2, 2, 2, 2, 2, 2, 1),
    ),
    BD: graph(
      chain((1, 2), s, s, s, s, s, s) + ((6, 8, 1, 1),),
      hidden: (3, 4),
      marks: (2, 2, 2, 2, 2, 2, 2, 1, 1),
    ),
    CD: graph(
      chain((2, 1), s, s, s, s, s, s) + ((6, 8, 1, 1),),
      hidden: (3, 4),
      marks: (1, 2, 2, 2, 2, 2, 2, 1, 1),
    ),
    E6: graph(
      chain(s, s, s, s) + ((2, 5, 1, 1), (5, 6, 1, 1)),
      marks: (1, 2, 3, 2, 1, 2, 1),
      arm: 1.3,
    ),
    E7: graph(
      chain(s, s, s, s, s, s) + ((3, 7, 1, 1),),
      marks: (1, 2, 3, 4, 3, 2, 1, 2),
      arm: 1.3,
    ),
    E8: graph(
      chain(s, s, s, s, s, s, s) + ((5, 8, 1, 1),),
      marks: (1, 2, 3, 4, 5, 6, 4, 2, 3),
      arm: 1.3,
    ),
    F41: graph(chain(s, s, (1, 2), s), marks: (1, 2, 3, 2, 1)),
    F42: graph(chain(s, s, (2, 1), s), marks: (1, 2, 3, 4, 2)),
    G21: graph(chain(s, (1, 3)), marks: (1, 2, 1)),
    G22: graph(chain(s, (3, 1)), marks: (1, 2, 3)),
  )
    .pairs()
    .map(((name, g)) => (name, draw(g)))
    .to-dict()
)

// A list of pictures, centred and set off from the text by a line's space.
#let displayed(body) = block(
  width: 100%,
  above: 1.2em,
  below: 1.2em,
  align(center, body),
)

// A list of diagrams in two columns, each a name and its picture, given by
// rows: `diagram-table((name, picture, name, picture), …)`. The gaps are
// those of the book, so that the widest list, of the Euclidean diagrams,
// keeps within the measure.
#let diagram-table(..rows) = displayed(grid(
  columns: 4,
  column-gutter: (3mm, 5mm, 3mm),
  row-gutter: 3.5mm,
  align: (right + horizon, left + horizon, right + horizon, left + horizon),
  ..rows.pos().flatten(),
))

// The two vertices joined by a double or triple arrow, and by the line with
// its values, in the text after Definition 4.5.1.
#let inline(g) = box(baseline: 50% - 0.25em, draw(g))
#let bond(a, b) = inline(graph(((0, 1, a, b),)))
#let valued-bond(a, b) = box(
  baseline: radius - 0.25em,
  draw(graph(((0, 1, a, b),), values: true)),
)

// The labelled graph of the proof of Lemma 4.5.2 with an edge (2, 1).
#let double-edge-chain = draw(graph(chain(s, (2, 1), s), open: (
  "start",
  "end",
)))

// The proof of Proposition 4.5.7: a subadditive function on B_∞, C_∞ and
// D_∞ gives one on A_∞^∞, its value at the middle vertex given.
#let folding-scheme = {
  let (n0, n1, n2) = ($n_0$, $n_1$, $n_2$)
  let infinite(edges, ..labels) = graph(
    edges,
    open: ("end",),
    labels: labels.pos(),
  )
  let row(middle) = graph(
    chain(s, s, s, s),
    open: ("start", "end"),
    labels: (n2, n1, middle, n1, n2),
  )
  let rows = (
    (infinite(chain((1, 2), s), n0, n1, n2), row(n0)),
    (infinite(chain((2, 1), s), n0, n1, n2), row($2 n_0$)),
    (
      infinite(chain(s, s) + ((1, 3, 1, 1),), n0, n1, n2, $n'_0$),
      row($n_0 + n'_0$),
    ),
  )
  // Each row in one picture, the arrow on the line of the graphs: the image
  // begins 9.5 units after the graph, the arrow between them.
  let u = unit / 1mm
  displayed(grid(row-gutter: 3.5mm, align: left, ..rows.map(((from, to)) => {
      cetz.canvas(length: 1mm, {
        import cetz.draw: content, group, translate
        strokes(from)
        content((5.75 * u, 0), $|->$)
        group({
          translate((9.5 * u, 0))
          strokes(to)
        })
      })
    })))
}
