#import "main-defs.typ": *
#import "statements.typ": *

== The Jordan–Hölder theorem <sec:jordan-holder>

#definition[
  A *composition series*#idx("composition", "series")#idx(
    "series",
    "composition",
  ) for a $Lambda$-module $M$ is a series of submodules
  $ 0 = M_0 < M_1 < dots.c < M_n = M $
  with $M_i slash M_(i-1)$ irreducible.
] <def:composition-series>

A module $M$ is said to satisfy the descending chain condition#idx(
  "descending chain condition",
)#idx("D.C.C.")#idx("chain", "condition") (D.C.C.) on submodules if every
descending chain of submodules eventually stops, and the ascending chain
condition#idx(
  "ascending chain condition",
)#idx("A.C.C.") (A.C.C.) if every ascending chain of submodules eventually
stops. A module satisfying A.C.C. on submodules is said to be *Noetherian*#idx(
  "Noetherian",
  "module",
)#idx("module", "Noetherian").

#lemma(title: [Modular law])[
  If $A$ and $B supset.eq C$ are submodules of $M$ then
  $ (C + A) inter B = C + (A inter B). $
] <lem:modular-law>
#idx("modular", "law", target: [@lem:modular-law])#idx(
  "law, modular",
  target: [@lem:modular-law],
)

#proof[
  Clearly $C + (A inter B) subset.eq (C + A) inter B$. Conversely if
  $b = c + a in (C + A) inter B$ then $a = b - c in A inter B$ and so
  $b in C + (A inter B)$.
]

#theorem(title: [Zassenhaus isomorphism theorem])[
  If $U supset.eq V$ and $U' supset.eq V'$ are submodules of $M$ then
  $
    ((U + V') inter U') / ((V + V') inter U')
    tilde.equiv (U inter U') / ((U' inter V) + (U inter V'))
    tilde.equiv ((U' + V) inter U) / ((V' + V) inter U).
  $
] <th:zassenhaus>
#idx("Zassenhaus isomorphism theorem", target: [@th:zassenhaus])#idx(
  "theorem",
  "Zassenhaus isomorphism",
  target: [@th:zassenhaus],
)#idx(
  "isomorphism",
  "theorem, Zassenhaus",
  target: [@th:zassenhaus],
)

#proof[
  It suffices to prove the first isomorphism. The kernel of the composite map
  $
    U inter U' arrow.hook ((U + V') inter U') arrow.twohead
    ((U + V') inter U') slash ((V + V') inter U')
  $
  #source(14)is
  $
    (U inter U') inter ((V + V') inter U') = U' inter (V + V') inter U
    = (U' inter V) + (U inter V')
  $
  by two applications of the modular law.
]

#theorem(title: [Jordan–Hölder])[
  Given any two series of submodules
  $
    0 = M_0 lt.eq dots.c lt.eq M_r = M \
    0 = M'_0 lt.eq dots.c lt.eq M'_s = M
  $
  of a $Lambda$-module $M$, we may refine them (i.e., stick in extra terms) to
  series of equal length
  $
    0 = L_0 lt.eq dots.c lt.eq L_n = M \
    0 = L'_0 lt.eq dots.c lt.eq L'_n = M
  $
  so that the factors $L_i slash L_(i-1)$ are a permutation of the factors
  $L'_j slash L'_(j-1)$ (up to isomorphism). Thus the following conditions on
  $M$ are equivalent.
  + $M$ has a composition series.
  + Every series of submodules of $M$ can be refined to a composition series.
  + $M$ satisfies A.C.C. and D.C.C. on submodules.
] <th:jordan-holder>
#idx("Jordan–Hölder theorem", target: [@th:jordan-holder])#idx(
  "theorem",
  "Jordan–Hölder",
  target: [@th:jordan-holder],
)

#proof[
  Between $M_i$ and $M_(i+1)$ we insert the terms $(M'_j + M_i) inter
  M_(i+1)$, and between $M'_j$ and $M'_(j+1)$ we insert the terms
  $(M_i + M'_j) inter M'_(j+1)$. Now use the Zassenhaus isomorphism theorem.
]

#remark[
  It follows that the length of a composition series, if one exists, is an
  invariant of the module. It is called the *composition length*#idx(
    "composition",
    "length",
  )#idx("length", "composition") of the module.
]

A module $M$ is said to be *uniserial*#idx("uniserial module")#idx(
  "module",
  "uniserial",
) if it has a unique composition series. This is the same as saying that $M$ has
a unique minimal submodule $M_0$, $M slash M_0$ has a unique minimal submodule
$M_1 slash M_0$, and so on.

#exercise[
  Suppose that $M$ is a module of finite composition length. Show that the
  submodules of $M$ satisfy the distributive laws#idx("distributive law")
  $
    (A + B) inter C & = (A inter C) + (B inter C) \
    (A inter B) + C & = (A + C) inter (B + C)
  $
  if and only if $M$ has no subquotient isomorphic to a direct sum of two
  isomorphic simple modules.
]

Read about Birkhoff's theorem for distributive lattices of finite length in
Aigner [@bib:Aigner1979]. In effect, this says that for a module with the above
property, one can draw a diagram, whose vertices represent the composition
factors, and whose edges describe how they are "glued together." In fact, there
is a generalisation of Birkhoff's diagrams to modular lattices of finite length
(Benson and Conway [@bib:Benson1985]), but this method quickly becomes
cumbersome, #source(15)as there are usually many more vertices than composition
factors. For further discussions of diagrams for modules#idx(
  "diagrams for modules",
), see Alperin [@bib:Alperin1980a] and Benson and Carlson [@bib:Benson1987].
