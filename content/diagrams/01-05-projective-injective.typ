#import "common.typ": cd, edge, node

// Definition of a projective module: P maps down to M, the bottom row
// M' -> M -> 0 is exact, and the dotted map nu lifts lambda to M'.
#let projective-lifting = cd(
  spacing: (9mm, 8mm),
  node((1, 0), $P$),
  node((0, 1), $M'$),
  node((1, 1), $M$),
  node((2, 1), $0$),
  edge((1, 0), (1, 1), $lambda$, "->", label-side: left),
  edge((1, 0), (0, 1), $nu$, "..>", label-side: right),
  edge((0, 1), (1, 1), $mu$, "->"),
  edge((1, 1), (2, 1), "->"),
)

// Definition of an injective module: the top row 0 -> M -> M' is exact, M
// maps down to I, and the dotted map nu extends lambda to M'.
#let injective-extension = cd(
  spacing: (9mm, 8mm),
  node((0, 0), $0$),
  node((1, 0), $M$),
  node((2, 0), $M'$),
  node((1, 1), $I$),
  edge((0, 0), (1, 0), "->"),
  edge((1, 0), (2, 0), $mu$, "->"),
  edge((1, 0), (1, 1), $lambda$, "->", label-side: right),
  edge((2, 0), (1, 1), $nu$, "..>", label-side: left),
)

// Two minimal projective modules mapping onto M, and the dotted maps
// between them in both directions.
#let minimal-projectives = cd(
  spacing: (9mm, 4mm),
  node((0, 0), $P_1$),
  node((1, 1), $M$),
  node((0, 2), $P_2$),
  edge((0, 0), (1, 1), "->"),
  edge((0, 2), (1, 1), "->"),
  edge((0, 0), (0, 2), "..>", shift: -2pt),
  edge((0, 2), (0, 0), "..>", shift: -2pt),
)

// Schanuel's lemma: the pullback X of P_1 -> M and P_2 -> M, with exact rows
// and columns. Each row lists its objects by column (`none`: no object);
// consecutive objects of the two middle rows and of the two middle columns
// are joined by arrows.
#let schanuel-pullback = {
  let rows = (
    (none, none, $0$, $0$, none),
    (none, none, $M_2$, $M_2$, none),
    ($0$, $M_1$, $X$, $P_2$, $0$),
    ($0$, $M_1$, $P_1$, $M$, $0$),
    (none, none, $0$, $0$, none),
  )
  let items = ()
  for (y, row) in rows.enumerate() {
    for (x, object) in row.enumerate() {
      if object != none { items.push(node((x, y), object)) }
    }
  }
  for y in (2, 3) {
    for x in range(4) { items.push(edge((x, y), (x + 1, y), "->")) }
  }
  for x in (2, 3) {
    for y in range(4) { items.push(edge((x, y), (x, y + 1), "->")) }
  }
  items.push(edge((2, 1), (3, 1), "="))
  items.push(edge((1, 2), (1, 3), "="))
  cd(spacing: (8mm, 7mm), ..items)
}
