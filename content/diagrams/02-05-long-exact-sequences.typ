#import "common.typ": cd, edge, grid-diagram, node
#import "../main-defs.typ": *

// Lemma 2.5.1: the projective resolutions of M′ and M″ completed to a short
// exact sequence of chain complexes.
#let horseshoe = {
  let zeros = (none, $0$, $0$, $0$, $0$, none)
  let maps = (none, "->", "->", "->", "->", none)
  grid-diagram(
    (
      zeros,
      ($dots.c$, $P'_2$, $P'_1$, $P'_0$, $M'$, $0$),
      (
        $dots.c$,
        $P'_2 plus.o P''_2$,
        $P'_1 plus.o P''_1$,
        $P'_0 plus.o P''_0$,
        $M$,
        $0$,
      ),
      ($dots.c$, $P''_2$, $P''_1$, $P''_0$, $M''$, $0$),
      zeros,
    ),
    across: (none, "->", "->", "->", none),
    down: (maps, maps, maps, maps),
  )
}

// Proposition 2.5.3 (i): a short exact sequence of right modules tensored
// with a projective resolution of M′.
#let tensored-resolution = {
  let zeros = (none, $0$, $0$, $0$)
  let maps = (none, "->", "->", "->")
  let row(i) = (
    $dots.c$,
    $M_#i times.o P'_2$,
    $M_#i times.o P'_1$,
    $M_#i times.o P'_0$,
  )
  grid-diagram(
    (zeros, row(0), row(1), row(2), zeros),
    across: (none, "->", "->", "->", none),
    down: (maps, maps, maps, maps),
  )
}

// Proposition 2.5.3 (ii): homomorphisms from a projective resolution of M′
// to a short exact sequence of left modules.
#let hom-resolution = {
  let zeros = ($0$, $0$, $0$, none)
  let maps = ("->", "->", "->", none)
  let row(i) = (
    $Hom_Lambda (P'_0, M_#i)$,
    $Hom_Lambda (P'_1, M_#i)$,
    $Hom_Lambda (P'_2, M_#i)$,
    $dots.c$,
  )
  grid-diagram(
    (zeros, row(0), row(1), row(2), zeros),
    across: (none, "->", "->", "->", none),
    down: (maps, maps, maps, maps),
  )
}

// Proof of Proposition 2.5.5: the case n = 1, in smaller type, as printed.
#let first-extension = text(size: 0.8em, grid-diagram(
  (
    (
      $0$,
      $Hom_Lambda (M, M')$,
      $Hom_Lambda (P, M')$,
      $Hom_Lambda (M_1, M')$,
      $Ext^1_Lambda (M, M')$,
      $0$,
    ),
    (
      $0$,
      $Hom_Lambda (M, M')$,
      $Hom_Lambda (P, M')$,
      $Hom_Lambda (M_1, M')$,
      $cal(E X T)^1_Lambda (M, M')$,
      $0.$,
    ),
  ),
  down: ((none, "=", "=", "=", none, none),),
  gap: 3mm,
))
