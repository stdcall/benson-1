#import "main-defs.typ": *
#import "statements.typ": *

== Rojter's theorem <sec:rojter>
#idx("Rojter's theorem", target: [@sec:rojter])#idx(
  "theorem",
  "Rojter's",
  target: [@sec:rojter],
)

The main theorem of this section (@th:rojter) was conjectured by Brauer and
Thrall, and first proved by Rojter. The proof we give is due to Auslander. We
refer to Ringel [@bib:Ringel1980], Bautista [@bib:Bautista1985], and Nazarova
and Rojter [@bib:Nazarova1973] for more information on this and another
conjecture of Brauer and Thrall, solved by Nazarova and Rojter.

We begin with a lemma.

#lemma(title: [Harada, Sai [@bib:Harada1970]])[
  Let $M_0, dots, M_(2^n - 1)$ be indecomposable modules, each having at most
  $n$ composition factors, and suppose $f_i : M_(i-1) -> M_i$ is a homomorphism
  which is not an isomorphism. Then
  $f_(2^n - 1) compose dots.c compose f_2 compose f_1 = 0$.
] <lem:harada-sai>
#idx("Harada–Sai lemma", target: [@lem:harada-sai])#idx(
  "lemma",
  "Harada–Sai",
  target: [@lem:harada-sai],
)

#proof[
  We show by induction on $m$ that the image of
  $f_(2^m - 1) compose dots.c compose f_1$ has at most $n - m$ composition
  factors. The assertion is clear for $m = 1$, since $f_1$ is not an
  isomorphism. Let $f = f_(2^(m-1) - 1) compose dots.c compose f_1$,
  $g = f_(2^(m-1))$ and
  $h = f_(2^m - 1) compose dots.c compose f_(2^(m-1) + 1)$. By the inductive
  hypothesis, the images of $f$ and $h$ each have at most $n - m + 1$
  composition factors. If either has strictly less, we are done, so suppose the
  images of $f$, $h$ and $h compose g compose f$ each has exactly $n - m + 1$
  #source(166)composition factors. Then $Ker(h compose g) inter Im(f) = 0$ and
  $Ker(h) inter Im(g compose f) = 0$, and so by counting composition factors we
  have $M_(2^(m-1) - 1) tilde.equiv Ker(h compose g) plus.o Im(f)$ and
  $M_(2^(m-1)) tilde.equiv Ker(h) plus.o Im(g compose f)$. Since each is
  indecomposable, $h compose g$ is injective and $g compose f$ is surjective.
  Thus $g$ is an isomorphism, contrary to hypothesis.
]

#theorem(title: [Auslander [@bib:Auslander1978]])[
  Suppose $Lambda$ is a finite dimensional algebra and $Q$ is an infinite
  connected component of the Auslander–Reiten quiver of $Lambda$-modules. Then
  $Q$ has modules with an arbitrarily large number of composition factors.
] <th:auslander-infinite-component>
#idx("Auslander", "'s theorem", target: [@th:auslander-infinite-component])#idx(
  "theorem",
  "Auslander's",
  target: [@th:auslander-infinite-component],
)

#proof[
  Suppose to the contrary that all modules in $Q$ have at most $n$ composition
  factors. Suppose $M$ is an indecomposable $Lambda$-module in $Q$. For some
  projective indecomposable $Lambda$-module $P$ we have a non-zero homomorphism
  $phi.alt : P -> M$ (for example, take for $P$ the projective cover of a simple
  submodule of $M$). If $P$ is not in the component $Q$, then by
  Proposition~@prop:irreducible-chains there is a chain of irreducible maps
  $
    M_0 limits(->)^(f_1) M_1 limits(->)^(f_2) dots.c
    limits(arrow.r.long)^(f_(2^n - 1)) M_(2^n - 1) = M
  $
  and $f : P -> M_0$ such that
  $f_(2^n - 1) compose dots.c compose f_2 compose f_1 compose f != 0$,
  contradicting the lemma. It follows that $P$ is in $Q$, and $P$ is connected
  to $M$ by a chain of irreducible maps of length at most $2^n - 1$. Since $Q$
  has finite valence, and there are only finitely many projective
  $Lambda$-modules, this forces $Q$ to have only finitely many vertices,
  contrary to assumption.
]

#theorem(title: [Rojter [@bib:Rojter1968]])[
  Suppose $Lambda$ is a finite dimensional algebra of infinite representation
  type. Then there are finitely generated indecomposable $Lambda$-modules with
  an arbitrarily large number of composition factors.
] <th:rojter>

#proof[
  (Auslander) By Proposition~@prop:finite-component the Auslander–Reiten quiver
  of finitely generated $Lambda$-modules has an infinite connected component.
  Now apply the above theorem.
]

#remark[
  Almost split sequences exist for an arbitrary Artin algebra, and so
  Auslander's proof of Rojter's theorem works in this generality.
]
