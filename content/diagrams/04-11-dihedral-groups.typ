#import "common.typ": cd, edge, node
#import "../main-defs.typ": *

// The schema of a module of the second kind M(C, φ): the copies V₀, …, Vₙ₋₁
// of V in a row, the letter ℓᵢ acting from Vᵢ to Vᵢ₋₁, and the last letter
// ℓₙ from V₀ back round to Vₙ₋₁ under the row. `labels` gives the label of
// the arrow into each object of the row from its right neighbour (`[]`
// unlabelled).
#let band-schema = {
  let objects = ($V_0$, $V_1$, $V_2$, $dots.c$, $V_(n-2)$, $V_(n-1)$)
  let labels = ($ell_1 = phi.alt$, $ell_2 = id$, [], [], $ell_(n-1) = id$)
  let last = objects.len() - 1
  cd(
    spacing: (11mm, 5mm),
    ..objects.enumerate().map(((x, object)) => node((x, 0), object)),
    ..labels
      .enumerate()
      .map(((x, label)) => edge(
        (x + 1, 0),
        (x, 0),
        label,
        "->",
        label-side: right,
      )),
    edge(
      (0, 0),
      (0, 1),
      (last, 1),
      (last, 0),
      $ell_n = id$,
      "->",
      label-pos: (1, 50%),
      label-side: right,
      corner-radius: 3mm,
    ),
  )
}
