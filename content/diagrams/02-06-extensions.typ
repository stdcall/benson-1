#import "common.typ": edge, grid-diagram, ladder
#import "../main-defs.typ": *

// A map of n-fold extensions: the identity at both ends.
#let extension-map = grid-diagram(
  (
    ($0$, $M'$, $M_(n-1)$, $dots.c$, $M_0$, $M$, $0$),
    ($0$, $M'$, $M'_(n-1)$, $dots.c$, $M'_0$, $M$, $0.$),
  ),
  down: ((none, "=", "->", none, "->", "=", none),),
)

// The element of Ext determined by an n-fold extension: the projective
// resolution of M mapped to the extension.
#let resolution-to-extension = grid-diagram(
  (
    (
      $dots.c$,
      $P_(n+1)$,
      $P_n$,
      $P_(n-1)$,
      $dots.c$,
      $P_0$,
      $M$,
      $0$,
    ),
    (none, $0$, $M'$, $M_(n-1)$, $dots.c$, $M_0$, $M$, $0$),
  ),
  across: (
    ("->", "->", (label: $partial_n$), "->", "->", "->", "->"),
    "->",
  ),
  down: (
    (none, none, (label: $phi.alt$), "->", none, "->", "=", none),
  ),
)

// Two n-fold extensions defining the same element of Ext are equivalent.
#let equivalent-extensions = {
  let maps(style) = (none, "=", style, style, none, style, "=", none)
  grid-diagram(
    (
      ($0$, $M'$, $M_(n-1)$, $M_(n-2)$, $dots.c$, $M_0$, $M$, $0$),
      (
        $0$,
        $M'$,
        $P_(n-1) slash partial_n (Ker phi.alt)$,
        $P_(n-2)$,
        $dots.c$,
        $P_0$,
        $M$,
        $0$,
      ),
      ($0$, $M'$, $M'_(n-1)$, $M'_(n-2)$, $dots.c$, $M'_0$, $M$, $0$),
    ),
    down: (maps("<-"), maps("->")),
  )
}

// The kernel L_ζ of the map representing ζ, and the n-fold extension
// representing ζ in the bottom row.
#let kernel-extension = {
  let ends = (none, "->", "->", none, none, none, none, none)
  grid-diagram(
    (
      (none, $0$, $0$),
      (none, $L_zeta$, $L_zeta$),
      (
        $0$,
        $tilde(Omega)^n (M)$,
        $P_(n-1)$,
        $P_(n-2)$,
        $dots.c$,
        $P_0$,
        $M$,
        $0$,
      ),
      (
        $0$,
        $M'$,
        $P_(n-1) slash L_zeta$,
        $P_(n-2)$,
        $dots.c$,
        $P_0$,
        $M$,
        $0$,
      ),
      (none, $0$, $0$),
    ),
    across: (none, "=", "->", "->", none),
    down: (
      ends,
      ends,
      (none, "->", "->", "->", none, "->", "=", none),
      ends,
    ),
  )
}

// The Yoneda splice of two extensions: M′ below the composite
// M′₀ → M_(n−1), with the zeros of the two short exact sequences through it.
#let yoneda-splice = grid-diagram(
  (
    (
      $0$,
      $M''$,
      $M'_(m-1)$,
      $dots.c$,
      $M'_0$,
      none,
      $M_(n-1)$,
      $dots.c$,
      $M_0$,
      $M$,
      $0$,
    ),
    (none, none, none, none, none, $M'$),
    (none, none, none, none, $0$, none, $0$),
  ),
  across: ("->", none, none),
  extra: (
    edge((4, 0), (6, 0), "->"),
    edge((4, 0), (5, 1), "->"),
    edge((5, 1), (6, 0), "->"),
    edge((4, 2), (5, 1), "->"),
    edge((5, 1), (6, 2), "->"),
  ),
  gap: 3mm,
  row: 2mm,
)

// Exercise 2: the direct sum of two extensions pushed out along the sum
// map M″ ⊕ M″ → M″; in smaller type, as printed.
#let pushout-sum = text(size: 0.8em, grid-diagram(
  (
    (
      $0$,
      $M'' plus.o M''$,
      $M_(n-1) plus.o M'_(n-1)$,
      $M_(n-2) plus.o M'_(n-2)$,
      $dots.c$,
      $M_0 plus.o M'_0$,
      $M plus.o M'$,
      $0$,
    ),
    (
      $0$,
      $M''$,
      $X$,
      $M_(n-2) plus.o M'_(n-2)$,
      $dots.c$,
      $M_0 plus.o M'_0$,
      $M plus.o M'$,
      $0.$,
    ),
  ),
  down: ((none, "->", "->", "=", none, "=", "=", none),),
  gap: 3mm,
))

// Exercise 5: the diagram for the snake lemma.
#let snake-diagram = ladder(
  ($0$, $Ker phi.alt$, $Omega M$, $S$, $0$),
  ($0$, $P_M$, $P_M$, $0$, $0$),
  (none, [], [], [], none),
  top-maps: ([], [], $phi.alt$, []),
)
