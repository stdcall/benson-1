#import "main-defs.typ": *
#import "statements.typ": *

== The Wedderburn structure theorem <sec:wedderburn-structure>
#idx("Wedderburn structure theorem", target: [@sec:wedderburn-structure])#idx(
  "structure theorem, Wedderburn",
  target: [@sec:wedderburn-structure],
)#idx("theorem", "Wedderburn", "structure", target: [@sec:wedderburn-structure])

#lemma(title: [Schur])[
  If $M_1$ and $M_2$ are irreducible $Lambda$-modules, then for
  $M_1 tilde.equiv.not M_2$, $Hom_Lambda (M_1, M_2) = 0$, while
  $Hom_Lambda (M_1, M_1) = End_Lambda (M_1)$ is a division ring.
] <lem:schur>
#idx("Schur's lemma", target: [@lem:schur])#idx(
  "lemma",
  "Schur's",
  target: [@lem:schur],
)

#proof[
  Clear.
]

#definition[
  An *idempotent*#idx("idempotent") in $Lambda$ is a non-zero element $e$ with
  $e^2 = e$.
] <def:idempotent>

Note that if $e != 1$ is an idempotent then so is $1 - e$, and we have
$lmodule(Lambda, Lambda) = Lambda e plus.o Lambda(1 - e)$.

#lemma[
  + If $M$ is a $Lambda$-module and $e$ is an idempotent in $Lambda$ then
    $ e M tilde.equiv Hom_Lambda (Lambda e, M). $
  + We have an isomorphism of rings
    $e Lambda e tilde.equiv End_Lambda (Lambda e)^op$ ($Lambda^op$ denotes the
    opposite ring to $Lambda$, where the order of multiplication has been
    reversed).
] <lem:idempotent-hom>

#proof[
  + #source(18)Define maps $f_1 : e M -> Hom_Lambda (Lambda e, M)$ by
    $f_1(e m) : a e |-> a e m$ and $f_2 : Hom_Lambda (Lambda e, M) -> e M$ by
    $f_2 : alpha |-> alpha(e)$. It is easy to check that $f_1$ and $f_2$ are
    mutually inverse.
  + This follows by applying (i) with $M = Lambda e$. It is easy to check that
    $f_1$ and $f_2$ reverse the order of multiplication.
]

#theorem[
  Let $M$ be a finite direct sum of irreducible $Lambda$-modules, say
  $M = M_1 plus.o dots.c plus.o M_r$, with each $M_i$ a direct sum of $n_i$
  modules $M_(i,1) plus.o dots.c plus.o M_(i,n_i)$ isomorphic to a simple module
  $S_i$, and $S_i tilde.equiv.not S_j$ if $i != j$. Let
  $Delta_i = End_Lambda (S_i)$. Then $Delta_i$ is a division ring#idx(
    "division ring",
  )#idx("ring", "division"), $End_Lambda (M_i) tilde.equiv Mat_(n_i) (Delta_i)$,
  and $End_Lambda (M) = plus.o.big_i End_Lambda (M_i)$ is semisimple.
] <th:semisimple-endomorphisms>

#proof[
  By Lemma~@lem:schur, $Delta_i$ is a division ring. Choose once and for all
  isomorphisms $theta_(i j) : M_(i j) -> S_i$. Now given
  $lambda in End_Lambda (M_i)$, we define $lambda_(j k) in Delta_i$ as the
  composite map
  $
    S_i limits(tilde.equiv)^(theta_(i k)^(-1)) M_(i k) arrow.hook M_i
    limits(->)^lambda M_i arrow.twohead M_(i j)
    limits(tilde.equiv)^(theta_(i j)) S_i.
  $

  The map $lambda |-> (lambda_(j k))$ is then an injective homomorphism
  $End_Lambda (M_i) -> Mat_(n_i) (Delta_i)$. Conversely, given $(lambda_(j k))$,
  we can construct $lambda$ as the sum of the composite endomorphisms
  $
    M_i arrow.twohead M_(i k) limits(tilde.equiv)^(theta_(i k)) S_i
    limits(arrow.r.long)^(lambda_(j k)) S_i
    limits(tilde.equiv)^(theta_(i j)^(-1)) M_(i j) arrow.hook M_i.
  $

  Finally, $End_Lambda (M) = plus.o.big_i End_Lambda (M_i)$ since if $i != j$,
  Lemma~@lem:schur implies that $Hom_Lambda (S_i, S_j) = 0$.
]

#theorem(title: [Wedderburn–Artin])[
  Let $Lambda$ be a semisimple Artinian ring. Then
  $Lambda = plus.o.big_(i=1)^r Lambda_i$,
  $Lambda_i tilde.equiv Mat_(n_i) (Delta_i)$, $Delta_i$ is a division ring, and
  the $Lambda_i$ are uniquely determined. The ring $Lambda$ has exactly $r$
  isomorphism classes of irreducible modules $M_i$, $i = 1, dots, r$,
  $End_Lambda (M_i) tilde.equiv Delta_i^op$, and $dim_(Delta_i^op)(M_i) = n_i$.
  If $Lambda$ is simple then $Lambda tilde.equiv Mat_n (Delta)$.
] <th:wedderburn-artin>

#proof[
  By Lemma~@lem:semisimple-ring, $lmodule(Lambda, Lambda)$ is completely
  reducible. By Lemma~@lem:idempotent-hom with $e = 1$,
  $Lambda tilde.equiv End_Lambda (lmodule(Lambda, Lambda))^op$. The result now
  follows by applying Theorem~@th:semisimple-endomorphisms to
  $lmodule(Lambda, Lambda)$. Note that the opposite ring of a complete matrix
  ring is again a complete matrix ring, over the opposite division ring.
]

#remark(kind: "Remarks")[
  + Wedderburn#idx("theorem", "Wedderburn", "on finite division rings") has
    shown that every division ring with a finite number of elements is a field.
  + If $Lambda$ is a finite dimensional algebra over a field $k$, then each
    $Delta_i$ for $Lambda slash J(Lambda)$ in the above theorem has $k$ in its
    centre. If for each $i$ we have $Delta_i = k$, then $k$ is called a
    *splitting field*#idx("splitting", "field")#idx("field", "splitting") for
    $Lambda$. This is true, for example, if $k$ is algebraically closed, since
    in this case there are no finite dimensional division rings over $k$ (apart
    from $k$ itself).
]

Finally, the following special case of the Skolem–Noether theorem#idx(
  "Skolem–Noether theorem",
)#idx("theorem", "Skolem–Noether") is often useful.

#proposition[
  #source(19)Suppose that $V$ is a finite dimensional vector space over a field
  $k$. Then every $k$-linear automorphism of $End_k (V)$ is inner (i.e.,
  effected by a conjugation in $End_k (V)$).
] <prop:skolem-noether>

#proof[
  Since the regular representation of $End_k (V)$ is a direct sum of copies of
  $V$, it follows that $End_k (V)$ has only one isomorphism class of simple
  modules. Thus if $f : End_k (V) -> End_k (V)$ is an automorphism, then $f$
  defines a new representation of $End_k (V)$ on $V$, which is therefore
  conjugate to the old one. Thus $f$ is conjugate to the identity map.
]

#exercise[
  If $Lambda$ is a finite dimensional algebra over $k$, show that some finite
  extension $k'$ of $k$ is a splitting field for $Lambda$ (i.e., for
  $k' times.o_k Lambda$). If $k$ is algebraically closed, then $k$ is a
  splitting field for $Lambda$.
]
