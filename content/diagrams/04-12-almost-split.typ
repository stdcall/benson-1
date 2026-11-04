#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// A short exact sequence 0 → M → E → N → 0 with σ on its last map but one,
// and a map ρ from N′ above N; the dotted arrow from N′ to E is the
// factorisation of ρ through σ. Also for the sequence ending in N in the
// proof of Proposition 4.13.3, with the factorisation μ.
#let factorisation(sub, down, through: []) = grid-diagram(
  (
    (none, none, none, $N'$, none),
    ($0$, sub, $E$, $N$, $0$),
  ),
  across: (none, ("->", "->", (label: $sigma$), "->")),
  down: ((none, none, none, (label: down), none),),
  extra: (edge((3, 0), (2, 1), through, "..>", label-side: right),),
  gap: 7mm,
  row: 12mm,
)

// Definition 4.12.1: ρ factors through σ.
#let almost-split-factorisation = factorisation($M$, $rho$)

// The rows of an almost split sequence and its comparison with another one
// terminating in N: the last two columns are N and 0.
#let sequence-row(sub, middle, over: []) = (
  ($0$, sub, middle, $N$, $0$),
  ("->", (label: over), "->", "->"),
)
// Rows joined by maps down the columns, the identity on N.
#let comparison(rows, labels) = grid-diagram(
  rows.map(row => row.first()),
  across: rows.map(row => row.last()),
  down: labels.map(label => (
    none,
    (label: label),
    "->",
    "=",
    none,
  )),
  gap: 7mm,
  row: 10mm,
)

// Proof of Lemma 4.12.3: the two almost split sequences terminating in N
// mapped to each other and back.
#let almost-split-comparison = comparison(
  (
    sequence-row($M$, $E$),
    sequence-row($M'$, $E'$),
    sequence-row($M$, $E$),
  ),
  ([], []),
)

// Proof of Proposition 4.12.4: the pushout along ρ.
#let almost-split-pushout = comparison(
  (
    sequence-row($M$, $E$, over: $sigma'$),
    sequence-row($M'$, $E'$),
  ),
  ($rho$,),
)

// Proof of Proposition 4.12.4: the pushout completed back to the almost split
// sequence by ρ′.
#let almost-split-pushout-back = comparison(
  (
    sequence-row($M$, $E$, over: $sigma'$),
    sequence-row($M'$, $E'$),
    sequence-row($M$, $E$),
  ),
  ($rho$, $rho'$),
)

// Proof of Theorem 4.12.11: the Nakayama relations between the homomorphisms
// from N into the induced sequence and from N restricted to H into the
// almost split sequence terminating in f(M), in smaller type, as printed.
#let induced-almost-split = {
  let modules = ($Omega^2 f(M)$, $E$, $f(M)$)
  text(size: 0.7em, grid-diagram(
    (
      ($0$, ..modules.map(X => $Hom_(k G) (N, #X up^G)$)),
      (
        $0$,
        ..modules.map(X => $Hom_(k H) (N down_H, #X)$),
        $S_(f(M)) (N down_H)$,
        $0.$,
      ),
    ),
    down: ((none, ..modules.map(_ => (label: $tilde.equiv$))),),
    gap: 3mm,
    row: 9mm,
  ))
}
