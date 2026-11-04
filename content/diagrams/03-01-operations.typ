#import "common.typ": cd, edge, grid-diagram, node
#import "../main-defs.typ": *

// Definition 3.1.4: co-associativity of the comultiplication.
#let coassociativity = cd(
  spacing: (14mm, 9mm),
  node((0, 0), $Lambda$),
  node((1, 0), $Lambda times.o_R Lambda$),
  node((0, 1), $Lambda times.o_R Lambda$),
  node((1, 1), $Lambda times.o Lambda times.o_R Lambda$),
  edge((0, 0), (1, 0), $Delta$, "->", label-side: left),
  edge((0, 0), (0, 1), $Delta$, "->", label-side: right),
  edge((1, 0), (1, 1), $Delta times.o 1$, "->", label-side: left),
  edge((0, 1), (1, 1), $1 times.o Delta$, "->", label-side: left),
)

// Definition 3.1.4: the co-unitary property; the maps from Λ to the two
// outer corners are the natural isomorphisms.
#let counit-triangles = cd(
  spacing: (12mm, 11mm),
  node((1, 0), $Lambda$),
  node((0, 1), $R times.o_R Lambda$),
  node((1, 1), $Lambda times.o_R Lambda$),
  node((2, 1), $Lambda times.o_R R$),
  edge((1, 0), (0, 1), $tilde.equiv$, "->", label-side: right),
  edge((1, 0), (2, 1), $tilde.equiv$, "->", label-side: left),
  edge((1, 0), (1, 1), $Delta$, "->", label-side: left),
  edge((1, 1), (0, 1), $epsilon times.o 1$, "->", label-side: right),
  edge((1, 1), (2, 1), $1 times.o epsilon$, "->", label-side: left),
)

// Definition 3.1.4: cocommutativity, the twist map τ composed with Δ.
#let cocommutativity = cd(
  spacing: (12mm, 9mm),
  node((0, 0), $Lambda$),
  node((0, 1), $Lambda times.o_R Lambda$),
  node((1, 1), $Lambda times.o_R Lambda$),
  edge((0, 0), (0, 1), $Delta$, "->", label-side: right),
  edge((0, 0), (1, 1), $Delta$, "->", label-side: left),
  edge((0, 1), (1, 1), $tau$, "->", label-side: left),
)

// Proof of Proposition 3.1.10: the maps M -> M ⊗ M* ⊗ M -> M and their
// effect on an element m, in smaller type, as printed.
#let summand-maps = text(size: 0.75em, grid-diagram(
  (
    (
      $M$,
      $tilde.equiv$,
      $k times.o_k M$,
      $(M times.o_k M^*) times.o_k M$,
      $tilde.equiv$,
      $M times.o_k (M^* times.o_k M)$,
      $M times.o_k k$,
      $tilde.equiv$,
      $M$,
    ),
    (
      $m$,
      $=$,
      $1 times.o m$,
      $(sum m_i times.o m'_i) times.o m$,
      $=$,
      $sum m_i times.o (m'_i times.o m)$,
      $sum m_i times.o m'_i (m)$,
      $=$,
      $m.$,
    ),
  ),
  across: (
    (none, none, "->", none, none, "->", none, none),
    (none, none, "|->", none, none, "|->", none, none),
  ),
  gap: 2mm,
  row: 9mm,
))
