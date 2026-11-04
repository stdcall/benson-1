#import "common.typ": cd, edge, node

// Projectivity relative to H (Definition 3.6.1): M maps down to M_1, the
// bottom row M_2 -> M_1 -> 0 is exact, and the dotted map nu lifts lambda
// to M_2.
#let relative-projective-lifting = cd(
  spacing: (9mm, 8mm),
  node((1, 0), $M$),
  node((0, 1), $M_2$),
  node((1, 1), $M_1$),
  node((2, 1), $0$),
  edge((1, 0), (1, 1), $lambda$, "->", label-side: left),
  edge((1, 0), (0, 1), $nu$, "..>", label-side: right),
  edge((0, 1), (1, 1), $mu$, "->"),
  edge((1, 1), (2, 1), "->"),
)

// Injectivity relative to H (Definition 3.6.1): the top row
// 0 -> M_1 -> M_2 is exact, M_1 maps down to M, and the dotted map nu
// extends lambda to M_2.
#let relative-injective-extension = cd(
  spacing: (9mm, 8mm),
  node((0, 0), $0$),
  node((1, 0), $M_1$),
  node((2, 0), $M_2$),
  node((1, 1), $M$),
  edge((0, 0), (1, 0), "->"),
  edge((1, 0), (2, 0), $mu$, "->"),
  edge((1, 0), (1, 1), $lambda$, "->", label-side: right),
  edge((2, 0), (1, 1), $nu$, "..>", label-side: left),
)
