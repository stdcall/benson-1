#import "common.typ": maps-grid
#import "../main-defs.typ": *

// The squares of Section 5.6: a Burnside ring, or its q-local version, mapped
// by φ to a representation ring, each with the sum of its ring
// homomorphisms to ℂ along the rows and the map λ between the direct sums
// of copies of ℂ, as printed.
#let copies(index) = $display(plus.o.big_#index CC)$
#let induction-square(top, bottom, top-index, bottom-index) = maps-grid(
  (
    (top, copies(top-index)),
    (bottom, copies(bottom-index)),
  ),
  (([],), ([],)),
  (($phi.alt$, $lambda$),),
  gap: 10mm,
)

// Artin's induction theorem (Theorem 5.6.1).
#let artin-square = induction-square(
  $B(G)$,
  $CC times.o_ZZ cal(R)(G)$,
  $H lt.eq_G G$,
  $g in_G G$,
)

// Brauer's induction theorem, with q-local coefficients.
#let brauer-square = induction-square(
  $b(G)_((q))$,
  $cal(R)(G)_((q))$,
  $H lt.eq_G G$,
  $g in_G G$,
)

// Conlon's induction theorem (Theorem 5.6.8).
#let conlon-square = induction-square(
  $B(G)$,
  $A(G, Triv)$,
  $H lt.eq_G G$,
  $"ccl’s of" \ "pairs" (H, g)$,
)

// Dress' induction theorem (Theorem 5.6.11).
#let dress-square = induction-square(
  $b(G)_((q))$,
  $a(G, Triv)_((q))$,
  $H lt.eq_G G$,
  $"ccl’s of" \ "pairs" (H, g)$,
)
