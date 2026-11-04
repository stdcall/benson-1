#import "common.typ": grid-diagram, maps-grid
#import "../main-defs.typ": *

// A map of modules M → M′ extended to a map of relatively H-projective
// resolutions (Theorem 3.9.3).
#let relative-comparison = maps-grid(
  (
    ($dots.c$, $X_2$, $X_1$, $X_0$, $M$, $0$),
    ($dots.c$, $Y_2$, $Y_1$, $Y_0$, $M'$, $0$),
  ),
  (
    ([], $partial_2$, $partial_1$, [], []),
    ([], $partial'_2$, $partial'_1$, [], []),
  ),
  ((none, $f_2$, $f_1$, $f_0$, [], none),),
)

// Lemma 3.9.4: the relatively H-projective resolutions of M′ and M″
// completed to a short exact sequence of chain complexes.
#let relative-horseshoe = {
  let zeros = (none, $0$, $0$, $0$, $0$, none)
  let maps = (none, "->", "->", "->", "->", none)
  grid-diagram(
    (
      zeros,
      ($dots.c$, $X'_2$, $X'_1$, $X'_0$, $M'$, $0$),
      (
        $dots.c$,
        $X'_2 plus.o X''_2$,
        $X'_1 plus.o X''_1$,
        $X'_0 plus.o X''_0$,
        $M$,
        $0$,
      ),
      ($dots.c$, $X''_2$, $X''_1$, $X''_0$, $M''$, $0$),
      zeros,
    ),
    across: (none, "->", "->", "->", none),
    down: (maps, maps, maps, maps),
  )
}
