#import "main-defs.typ": *
#import "statements.typ": *

== The Krull–Schmidt theorem <sec:krull-schmidt>
#idx("Krull–Schmidt theorem", target: [@sec:krull-schmidt])#idx(
  "theorem",
  "Krull–Schmidt",
  target: [@sec:krull-schmidt],
)

#definition[
  A (not necessarily commutative) ring $E$ is said to be a *local ring*#idx(
    "local ring",
  )#idx("ring", "local") if it has a unique maximal left ideal, or equivalently
  a unique maximal right ideal. This maximal ideal is automatically two-sided
  (see the remarks in Section~@sec:jacobson-radical) and consists of the
  non-invertible elements of $E$. The quotient by the unique maximal ideal is a
  division ring.

  It is easy to see that $E$ is local if and only if the non-invertible elements
  form a left ideal.
] <def:local-ring>

#definition[
  A $Lambda$-module $M$ has the *unique decomposition property*#idx(
    "unique decomposition property",
  ) if
  + $M$ is a finite direct sum of indecomposable modules, and
  + Whenever $M = plus.o.big_(i=1)^m M_i = plus.o.big_(i=1)^n M'_i$ with each
    $M_i$ and each $M'_i$ non-zero indecomposable, then $m = n$, and after
    reordering if necessary, $M_i tilde.equiv M'_i$.

  A ring $Lambda$ is said to have the unique decomposition property if every
  finitely generated $Lambda$-module does.
] <def:unique-decomposition>

#theorem[
  Suppose that $M$ is a finite sum of indecomposable $Lambda$-modules $M_i$ with
  the property that the endomorphism ring of each $M_i$ is a local ring. Then
  $M$ has the unique decomposition property.
] <th:local-endomorphisms-unique-decomposition>

#proof[
  Let $M = plus.o.big_(i=1)^m M_i = plus.o.big_(i=1)^n M'_i$ and work by
  induction on $m$. Assume $m > 1$. Let $alpha_i$ and $beta_i$ be the composites
  $ alpha_i : M'_i arrow.hook M arrow.twohead M_1 $
  and
  $ beta_i : M_1 arrow.hook M arrow.twohead M'_i. $
  Then $id_(M_1) = sum alpha_i compose beta_i : M_1 -> M_1$. Since
  $End_Lambda (M_1)$ is a local ring, some $alpha_i compose beta_i$ must be a
  unit. Renumber so that $alpha_1 compose beta_1$ is a unit. Then
  $M_1 tilde.equiv M'_1$.

  Consider the map $mu = 1 - theta$, where $theta$ is the composite
  $
    theta : M arrow.twohead M_1 limits(arrow.r.long)^(alpha_1^(-1)) M'_1
    arrow.hook M arrow.twohead plus.o.big_(i=2)^m M_i arrow.hook M.
  $
  #source(20)Then $mu M'_1 = M_1$, and
  $mu(plus.o.big_(i=2)^m M_i) = plus.o.big_(i=2)^m M_i$, so $mu$ is onto. If
  $mu(w) = 0$, then $w = theta(w)$ and so $w in plus.o.big_(i=2)^m M_i$. But
  then $theta(w) = 0$.

  Thus $mu$ is an automorphism of $M$ with $mu M'_1 = M_1$, and so
  $
    plus.o.big_(i=2)^n M'_i = M slash M'_1 tilde.equiv M slash M_1
    = plus.o.big_(i=2)^m M_i.
  $
]

#lemma(title: [Fitting])[
  Suppose that $M$ has a composition series (i.e., satisfies A.C.C. and D.C.C.
  on submodules, see Theorem~@th:jordan-holder) and $f in End_Lambda (M)$. Then
  for large enough $n$, $M = Im(f^n) plus.o Ker(f^n)$.
] <lem:fitting>
#idx("Fitting's lemma", target: [@lem:fitting])#idx(
  "lemma",
  "Fitting's",
  target: [@lem:fitting],
)

#proof[
  By A.C.C. and D.C.C. on submodules of $M$, there is a positive integer $n$
  such that for all $k gt.eq 0$ we have $Ker(f^n) = Ker(f^(n+k))$ and
  $Im(f^n) = Im(f^(n+k))$. If $x in M$, write $f^n (x) = f^(2n) (y)$. Then
  $x = f^n (y) + (x - f^n (y)) in Im(f^n) + Ker(f^n)$. If
  $f^n (x) in Im(f^n) inter Ker(f^n)$ then $f^(2n) (x) = 0$, and so
  $f^n (x) = 0$.
]

#lemma[
  Suppose that $M$ is an indecomposable module with a composition series. Then
  $End_Lambda (M)$ is a local ring.
] <lem:indecomposable-local>

#proof[
  Let $E = End_Lambda (M)$, and choose $I$ a maximal left ideal of $E$. Suppose
  that $a in.not I$. Then $E = E a + I$. Write $1 = lambda a + mu$ with
  $lambda in E$, and $mu in I$. Since $mu$ is not an isomorphism,
  Lemma~@lem:fitting implies that $mu^n = 0$ for some $n$. Thus
  $(1 + mu + dots.c + mu^(n-1)) lambda a = (1 + dots.c + mu^(n-1))(1 - mu) = 1$,
  and so $a$ is invertible.
]

#theorem(title: [Krull–Schmidt])[
  Suppose that $Lambda$ is Artinian. Then $Lambda$ has the unique decomposition
  property.
] <th:krull-schmidt>

#proof[
  Suppose that $M$ is a finitely generated indecomposable $Lambda$-module. Then
  by Theorem~@th:artinian-ring $M$ has a composition series, and so by
  Lemma~@lem:indecomposable-local, $End_Lambda (M)$ is a local ring. The result
  now follows from Theorem~@th:local-endomorphisms-unique-decomposition.
]

#exercise[
  Suppose that $cal(O)$ is the ring of integers in an algebraic number field.
  Show that the Krull–Schmidt theorem holds for finitely generated
  $cal(O)$-modules if and only if $cal(O)$ has class number one.
]
