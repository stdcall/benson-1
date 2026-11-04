#import "common.typ": cd, edge, node

// The square of a natural transformation φ: F ⇝ F′ at a morphism α: X → Y
// (Definition 2.1.1): the maps φ_X, φ_Y along the rows, labelled above
// them; F(α) and F′(α) down the columns, labelled on the outer sides.
#let naturality-square = cd(
  spacing: (8mm, 8mm),
  node((0, 0), $F(X)$),
  node((1, 0), $F'(X)$),
  node((0, 1), $F(Y)$),
  node((1, 1), $F'(Y)$),
  edge((0, 0), (1, 0), $phi.alt_X$, "->"),
  edge((0, 1), (1, 1), $phi.alt_Y$, "->"),
  edge((0, 0), (0, 1), $F(alpha)$, "->", label-side: right),
  edge((1, 0), (1, 1), $F'(alpha)$, "->", label-side: left),
)
