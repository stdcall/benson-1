#import "common.typ": maps-grid
#import "../main-defs.typ": *

// The proof of Proposition 5.9.4: the decomposition map d and the sums of
// the ring homomorphisms t_g to the direct sums of copies of ℂ.
#let copies(index) = $display(plus.o.big_#index CC)$
#let brauer-lift-square = maps-grid(
  (
    ($cal(R)(K G)$, copies($g in_G G$)),
    ($cal(R)(k G)$, copies($p'"-elements" \ g in_G G$)),
  ),
  (($sum t_g$,), ($sum t_g$,)),
  (($d$, []),),
  gap: 10mm,
)
