#import "common.typ": cd, edge, ladder, node
#import "../main-defs.typ": *

// The kernel of a natural transformation F₁ ⇝ F₂ at a homomorphism M → M′:
// the kernels V, V′ with the maps of F₁ and F₂ down the columns.
#let kernel-ladder = ladder(
  ($0$, $V$, $F_1 (M)$, $F_2 (M)$),
  ($0$, $V'$, $F_1 (M')$, $F_2 (M')$),
  (none, [], [], []),
)

// Theorem 4.8.2: the natural transformation λ from (M, −) lifted through the
// epimorphism μ: F₁ ⇝ F₂ to ν; all maps are natural transformations, drawn
// as wavy arrows.
#let representable-lift = {
  let natural(from, to, ..label) = edge(
    from,
    to,
    ..label,
    "->",
    decorations: "wave",
  )
  cd(
    spacing: (9mm, 9mm),
    node((1, 0), $(M, -)$),
    node((0, 1), $F_1$),
    node((1, 1), $F_2$),
    node((2, 1), $0$),
    natural((1, 0), (0, 1), $nu$, label-side: right),
    natural((1, 0), (1, 1), $lambda$, label-side: left),
    natural((0, 1), (1, 1), $mu$, label-side: left),
    natural((1, 1), (2, 1)),
  )
}
