#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Proof of Proposition 3.2.1: the map of (m + n)-fold extensions from the
// tensor product of the complexes to the Yoneda composite, in smaller type,
// as printed.
#let cup-yoneda-map = text(size: 0.8em, grid-diagram(
  (
    (
      $0$,
      $M' times.o_R N'$,
      $(bold(M) times.o_R bold(N))_(m+n-1)$,
      $dots.c$,
      $dots.c$,
      $(bold(M) times.o_R bold(N))_0$,
      $M times.o_R N$,
      $0$,
    ),
    (
      $0$,
      $M' times.o_R N'$,
      $M_(m-1)$,
      $M_0$,
      $N_(n-1)$,
      $N_0$,
      $M times.o_R N$,
      $0$,
    ),
  ),
  across: (
    ("->", "->", "->", none, "->", "->", "->"),
    ("->", "->", "..>", "->", "..>", "->", "->"),
  ),
  down: (
    (
      none,
      "=",
      (label: $phi.alt_(m+n-1)$),
      none,
      none,
      (label: $phi.alt_0$),
      "=",
      none,
    ),
  ),
  gap: 4mm,
  row: 7mm,
))

// Graded commutativity of the cup product: the twist of the factors.
#let cup-twist = grid-diagram(
  (
    (
      $Ext^m_Lambda (bold(C), bold(D))
      times.o_R Ext^n_Lambda (bold(C)', bold(D)')$,
      $Ext^(m+n)_Lambda
      (bold(C) times.o_R bold(C)', bold(D) times.o_R bold(D)')$,
    ),
    (
      $Ext^n_Lambda (bold(C)', bold(D)')
      times.o_R Ext^m_Lambda (bold(C), bold(D))$,
      $Ext^(m+n)_Lambda
      (bold(C)' times.o_R bold(C), bold(D)' times.o_R bold(D))$,
    ),
  ),
  down: (((label: $tilde.equiv$), (label: $tilde.equiv$)),),
  gap: 7mm,
  row: 9mm,
)
