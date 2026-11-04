#import "common.typ": cd, edge, node
#import "../main-defs.typ": *

// Section 4.1, Example: the quiver of the four subspace problem, four arrows
// from the outer vertices into the central one.
#let four-subspace-quiver = {
  let centre = (0, 0)
  // Above, on the left, on the right and below the central vertex.
  let outer = ((0, -1), (-1, 0), (1, 0), (0, 1))
  cd(
    spacing: 5mm,
    node(centre, $bullet$),
    ..outer.map(vertex => node(vertex, $bullet$)),
    ..outer.map(vertex => edge(vertex, centre, "->")),
  )
}
