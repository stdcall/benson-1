#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// The central extension of G pulled back from the extension of G/N
// (Section 3.13 and Theorem 3.13.4).
#let central-pullback = grid-diagram(
  (
    ($1$, $Z$, $hat(G)$, $G$, $1$),
    ($1$, $Z$, $hat(G slash N)$, $G slash N$, $1$),
  ),
  down: ((none, "=", "->", "->", none),),
  row: 7mm,
)

// The group of pairs (g, φ_g) extending G by the units of End_kN(M)^op.
#let units-extension = {
  let ends = (none, none, $1$, $1$, none)
  let units = $(End_(k N) (M)^op)^times$
  grid-diagram(
    (
      ends,
      (none, none, $N$, $N$, none),
      ($1$, units, $tilde(G)$, $G$, $1$),
      ($1$, units, $tilde(G) slash N$, $G slash N$, $1$),
      ends,
    ),
    across: (none, "=", "->", "->", none),
    down: (
      (none, none, "->", "->", none),
      (none, none, "->", "->", none),
      (none, "=", "->", "->", none),
      (none, none, "->", "->", none),
    ),
  )
}

// The quotient by the kernel K of the determinant map.
#let determinant-kernel = {
  let ends = (none, none, $1$, $1$, none)
  grid-diagram(
    (
      ends,
      ($1$, $K$, $(End_(k N) (M)^op)^times$, $k^times$, $1$),
      ($1$, $K$, $tilde(G) slash N$, $hat(G) slash N$, $1$),
      (none, none, $G slash N$, $G slash N$, none),
      ends,
    ),
    across: (none, "->", "->", "=", none),
    down: (
      (none, none, "->", "->", none),
      (none, "=", "->", "->", none),
      (none, none, "->", "->", none),
      (none, none, "->", "->", none),
    ),
  )
}
