#import "common.typ": cd, edge, node
#import "../main-defs.typ": *

// The Ext-quiver in the proof of Theorem 6.6.2: a vertex for each of the
// three simple modules, at the corners of a triangle, and an arrow each way
// between any two of them. Each arrow bends to its left and carries its
// name on that side, as printed: the outer arrows α and δ, the inner arrows
// β and γ, and ε above ζ along the bottom.
#let klein-four-quiver = (
  // Places on a grid, the rows counted downwards.
  places: (top: (1, 0), left: (0, 1), right: (2, 1)),
  arrows: (
    (from: "left", to: "top", name: $alpha$),
    (from: "top", to: "left", name: $beta$),
    (from: "right", to: "top", name: $gamma$),
    (from: "top", to: "right", name: $delta$),
    (from: "left", to: "right", name: $epsilon$),
    (from: "right", to: "left", name: $zeta$),
  ),
)

#let ext-quiver = {
  let q = klein-four-quiver
  for a in q.arrows {
    assert(
      q.arrows.any(b => b.from == a.to and b.to == a.from),
      message: "every arrow has an opposite arrow",
    )
  }
  cd(
    spacing: 0pt,
    cell-size: 17mm,
    node-inset: 0pt,
    node-outset: 1mm,
    ..q
      .places
      .values()
      .map(place => node(
        place,
        [],
        shape: circle,
        radius: 0.6mm,
        fill: black,
      )),
    ..q.arrows.map(a => edge(
      q.places.at(a.from),
      q.places.at(a.to),
      a.name,
      "->",
      bend: 15deg,
      label-side: left,
    )),
  )
}
