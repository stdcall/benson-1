#import "common.typ": cd, edge, maps-grid, node
#import "../main-defs.typ": Im

// A map of modules M → M′ extended to a map of projective resolutions
// (Theorem 2.4.2).
#let comparison = maps-grid(
  (
    ($dots.c$, $P_2$, $P_1$, $P_0$, $M$, $0$),
    ($dots.c$, $Q_2$, $Q_1$, $Q_0$, $M'$, $0$),
  ),
  (
    ([], $partial_2$, $partial_1$, [], []),
    ([], $partial'_2$, $partial'_1$, [], []),
  ),
  ((none, $f_2$, $f_1$, $f_0$, [], none),),
)

// The lift of f_(n-1) ∘ ∂_n through ∂′_n in the proof of Theorem 2.4.2:
// P_n is projective, the row is exact, and the dotted map is the lift.
#let lifting = cd(
  spacing: (12mm, 12mm),
  node((1, 0), $P_n$),
  node((0, 1), $Q_n$),
  node((1, 1), $Im(partial'_n)$),
  node((2, 1), $0$),
  edge((1, 0), (1, 1), $f_(n-1) compose partial_n$, "->", label-side: left),
  edge((1, 0), (0, 1), "..>"),
  edge((0, 1), (1, 1), $partial'_n$, "->"),
  edge((1, 1), (2, 1), "->"),
)
