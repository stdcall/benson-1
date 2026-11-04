#import "common.typ": cd, edge, node
#import "../main-defs.typ": *

// Section 4.3: the Ext-quiver of kV₄, one vertex with the two loops a and b,
// drawn on its left and on its right; each runs from the top of the vertex
// round to the bottom.
#let klein-four-ext-quiver = {
  let vertex = (0, 0)
  // A loop and its side: -1 on the left, 1 on the right.
  let loops = (($a$, -1), ($b$, 1))
  cd(
    node(vertex, $bullet$, inset: 2mm),
    ..loops.map(((caption, side)) => edge(
      vertex,
      vertex,
      caption,
      "->",
      bend: side * 130deg,
      loop-angle: 0deg,
    )),
  )
}

// Definition 4.3.1: the Kronecker quiver, two arrows a and b from x₁ to x₂,
// a bending above and b below.
#let kronecker-quiver = {
  let (tail, head) = ((0, 0), (1, 0))
  let arrows = (($a$, 1), ($b$, -1))
  cd(
    spacing: 7mm,
    node(tail, $x_1 bullet$),
    node(head, $bullet x_2$),
    ..arrows.map(((caption, side)) => edge(
      tail,
      head,
      caption,
      "->",
      bend: side * 20deg,
      label-side: if side > 0 { left } else { right },
    )),
  )
}
