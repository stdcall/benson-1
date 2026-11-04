#import "main-defs.typ": *
#import "statements.typ": *

== Trivial source modules <sec:trivial-source>

As we shall see in Chapter~@ch:representation-rings, trivial source modules
control quite a lot of the structure of representation rings.

Throughout this section, $R$ is an arbitrary commutative ring of coefficients
such that the Krull–Schmidt theorem holds for finitely generated $R G$-modules,
and $(K, cal(O), k)$ is a $p$-modular system.

#definition[
  An $R G$-module $M$ is a *trivial source module*#idx(
    "module",
    "trivial",
    "source",
  )#idx("source", "trivial")#idx("trivial", "source module") if each
  indecomposable summand of $M$ has the trivial module $R$ as its source.
] <def:trivial-source>

#lemma[
  An indecomposable $R G$-module $M$ has trivial source if and only if it is a
  direct summand of a permutation module.
] <lem:trivial-source-permutation>

#proof[
  Suppose $M$ is a summand of $R_H up^G$. Let $D$ be a vertex of $M$, and $M_0$
  be a source. Then by the Mackey decomposition theorem, $M_0$ is a summand of
  $
    R_H up^G down_D = plus.o.big_(D g H) R_(D inter lconj(g, H)) up^D .
  $
  Since $D$ is a vertex, $M_0 tilde.equiv R_D$.
]

One of the principal properties of trivial source modules is that they lift from
characteristic $p$ to characteristic zero.

#theorem(title: [Scott])[
  Let $M_1$ and $M_2$ be the $cal(O) G$-permutation modules on the cosets of
  $H_1$ and $H_2$ respectively. Then the natural homomorphism from
  $Hom_(cal(O) G) (M_1, M_2)$ to $Hom_(k G) (macron(M)_1, macron(M)_2)$ given by
  reduction modulo $frak(p)$ is surjective.
] <th:scott-lifting>
#idx("Scott's lifting theorem", target: [@th:scott-lifting])#idx(
  "lifting theorem",
  "Scott's",
  target: [@th:scott-lifting],
)#idx("theorem", "Scott's lifting", target: [@th:scott-lifting])

#proof[
  By the Mackey decomposition theorem, the free $cal(O)$-module
  $Hom_(cal(O) G) (M_1, M_2)$ and the $k$-vector space
  $Hom_(k G) (macron(M)_1, macron(M)_2)$ have the same rank, namely the number
  of double cosets $H_2 g H_1$.
]

#corollary[
  + Every trivial source $k G$-module lifts to a trivial source
    $cal(O) G$-module, unique up to isomorphism.
  + If $M_1$ and $M_2$ are trivial source $cal(O) G$-modules, then the natural
    map
    $ Hom_(cal(O) G) (M_1, M_2) -> Hom_(k G) (macron(M)_1, macron(M)_2) $
    given by reduction modulo $frak(p)$ is surjective.
] <cor:trivial-source-lift>

#proof[
  By the theorem, reduction modulo $frak(p)$ is surjective on endomorphism rings
  of permutation modules. A trivial source module corresponds to an idempotent
  in such an endomorphism ring, and so by the Idempotent Refinement
  Theorem~@th:idempotent-refinement-p-adic, trivial source modules lift.

  Applying the theorem again, we see that homomorphisms between trivial source
  modules lift. Uniqueness of the lifts follows from the conjugacy statement in
  Theorem~@th:idempotent-refinement-p-adic.
]
