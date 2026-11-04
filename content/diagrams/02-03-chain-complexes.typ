#import "common.typ": cd, edge, ladder, maps-grid, node

// A chain map and a cochain map (Definition 2.3.3): the two commuting
// squares side by side, the second one in parentheses.
#let chain-map-squares = maps-grid(
  (
    ($C_n$, $C_(n-1)$, [(resp.], $C^n$, $C^(n+1)$, [).]),
    ($D_n$, $D_(n-1)$, none, $D^n$, $D^(n+1)$, none),
  ),
  (
    ($partial_n$, none, none, $delta^n$, none),
    ($partial_n$, none, none, $delta^n$, none),
  ),
  (($f_n$, $f_(n-1)$, none, $f_n$, $f_(n+1)$, none),),
)

// A chain homotopy h between chain maps f, f′: C → D (Definition 2.3.4):
// the maps h_n go from C_n down to D_(n+1).
#let chain-homotopy = maps-grid(
  (
    ($dots.c$, $C_(n+1)$, $C_n$, $C_(n-1)$, $dots.c$),
    ($dots.c$, $D_(n+1)$, $D_n$, $D_(n-1)$, $dots.c$),
  ),
  (
    ([], $partial_(n+1)$, $partial_n$, []),
    ([], $partial_(n+1)$, $partial_n$, []),
  ),
  ((none, $f_(n+1)$, $f_n$, $f_(n-1)$, none),),
  diagonal: ((none, $h_(n+1)$, $h_n$, $h_(n-1)$, []),),
  down-side: left,
  gap: 14mm,
  row: 18mm,
)

// A short exact sequence 0 → C′ → C → C″ → 0 of chain complexes
// (Definition 2.3.6), degree by degree.
#let short-exact-complexes = {
  let zeros = (none, $0$, $0$, $0$, none)
  maps-grid(
    (
      zeros,
      ($dots.c$, $C'_(n+1)$, $C'_n$, $C'_(n-1)$, $dots.c$),
      ($dots.c$, $C_(n+1)$, $C_n$, $C_(n-1)$, $dots.c$),
      ($dots.c$, $C''_(n+1)$, $C''_n$, $C''_(n-1)$, $dots.c$),
      zeros,
    ),
    (
      (none, none, none, none),
      ([], $partial'_(n+1)$, $partial'_n$, []),
      ([], $partial_(n+1)$, $partial_n$, []),
      ([], $partial''_(n+1)$, $partial''_n$, []),
    ),
    (
      (none, [], [], [], none),
      (none, $phi.alt_(n+1)$, $phi.alt_n$, $phi.alt_(n-1)$, none),
      (none, $psi_(n+1)$, $psi_n$, $psi_(n-1)$, none),
      (none, [], [], [], none),
    ),
  )
}

// The commutative diagram of short exact sequences of the snake lemma
// (Lemma 2.3.9).
#let snake = ladder(
  ($0$, $C'_1$, $C_1$, $C''_1$, $0$),
  ($0$, $C'_0$, $C_0$, $C''_0$, $0$),
  (none, $alpha$, $beta$, $gamma$, none),
  down-side: right,
)
