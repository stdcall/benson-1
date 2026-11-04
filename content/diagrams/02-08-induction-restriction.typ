#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// The pushout of an induced extension along the natural map onto M.
#let induced-pushout = grid-diagram(
  (
    (
      $M down_Gamma up^Lambda$,
      $N_(n-1) up^Lambda$,
    ),
    ($M$, $X$),
  ),
  down: (("->", "->"),),
  gap: 8mm,
)

// The pullback of a restricted extension along the natural map from N.
#let restricted-pullback = grid-diagram(
  (
    ($Y$, $N$),
    (
      $M_0 down_Gamma$,
      $N up^Lambda down_Gamma$,
    ),
  ),
  down: (("->", "->"),),
  gap: 8mm,
)

// The exercise: a map of Ext groups, its composite with the Eckmann–Shapiro
// isomorphism, and restriction.
#let restriction-triangle(top-left, top-right, bottom, top-map) = {
  grid-diagram(
    (
      (top-left, top-right),
      (none, bottom),
    ),
    across: ((label: top-map), none),
    down: ((none, (label: $tilde.equiv$)),),
    extra: (
      edge((0, 0), (1, 1), $res_(Lambda, Gamma)$, "->", label-side: right),
    ),
    gap: 5mm,
  )
}

// Side by side, apart and on a common bottom row.
#let restriction-triangles = grid(
  columns: 2,
  column-gutter: 6mm,
  align: bottom,
  restriction-triangle(
    $Ext^n_Lambda (N, M)$,
    $Ext^n_Lambda (N, M down_Gamma Up^Lambda)$,
    $Ext^n_Gamma (N down_Gamma, M down_Gamma)$,
    $eta_*$,
  ),
  restriction-triangle(
    $Ext^n_Lambda (M, N)$,
    $Ext^n_Lambda (M down_Gamma up^Lambda, N)$,
    $Ext^n_Gamma (M down_Gamma, N down_Gamma)$,
    $(eta')^*$,
  ),
)
