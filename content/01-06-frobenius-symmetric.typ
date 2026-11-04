#import "main-defs.typ": *
#import "statements.typ": *

== Frobenius and symmetric algebras <sec:frobenius-symmetric>

Suppose that $Lambda$ is an algebra over a field $k$. If $M$ is a left
$Lambda$-module, then the vector space dual $M^* = Hom_k (M, k)$ has a natural
structure as a right $Lambda$-module, and vice-versa. If $M$ is finite
dimensional as a vector space, which it usually is because we are normally
interested in finitely generated modules, then there is a natural isomorphism
$(M^*)^* tilde.equiv M$. If $M$ is injective then $M^*$ is projective, and
vice-versa, since duality reverses all arrows.

In general, projective and injective modules for a ring are very different.
However, there is a special situation under which they are the same.

#definition[
  We say a finite dimensional algebra $Lambda$ over a field $k$ is
  *Frobenius*#idx("Frobenius", "algebra")#idx("algebra", "Frobenius") if there
  is a linear map $lambda : Lambda -> k$ such that
  + $Ker(lambda)$ contains no non-zero left or right ideal.
  We say that $Lambda$ is *symmetric*#idx("symmetric", "algebra")#idx(
    "algebra",
    "symmetric",
  ) if it satisfies (i) together with
  #enum(start: 2)[For all $a, b in Lambda$, $lambda(a b) = lambda(b a)$.]

  We say that a ring $Lambda$ is *self injective*#idx(
    "self injective ring",
  )#idx("ring", "self injective") if the regular representation
  $lmodule(Lambda, Lambda)$ is an injective $Lambda$-module.
] <def:frobenius-symmetric>

#proposition[
  + If $Lambda$ be a Frobenius algebra over $k$, then
    $(Lambda_Lambda)^* tilde.equiv lmodule(Lambda, Lambda)$. In particular
    $Lambda$ is self injective.
  + Suppose that $Lambda$ is self injective. Then the following conditions on a
    finitely generated $Lambda$-module $M$ are equivalent:
    #case-list(
      numbering: "(a)",
      [$M$ is projective],
      [$M$ is injective],
      [$M^*$ is projective],
      [$M^*$ is injective.],
    )
] <prop:frobenius-self-injective>

#proof[
  + We define a linear map
    $phi.alt : lmodule(Lambda, Lambda) -> (Lambda_Lambda)^*$ via
    $phi.alt(x) : y -> lambda(y x)$. Then if $gamma in Lambda$,
    $
      (gamma(phi.alt(x)))y = (phi.alt(x))(y gamma) = lambda(y gamma x)
      = (phi.alt(gamma x))y,
    $
    #source(24)so $phi.alt$ is a homomorphism. By the defining property of
    $lambda$, $phi.alt$ is injective, and hence surjective by comparing
    dimensions.
  + It follows from self injectivity that $M$ is projective if and only if $M^*$
    is projective, so that (a) and (c) are equivalent. We have already remarked
    that (a) $<=>$ (d) and (b) $<=>$ (c) hold for all finite dimensional
    algebras.
]

It follows from the above proposition that if $P$ is a projective indecomposable
module for a Frobenius algebra then not only $P slash Rad(P)$ but also $Soc(P)$
are simple. In general they are not isomorphic, but in the special case of a
symmetric algebra we have the following:

#theorem[
  Suppose that $P$ is a projective indecomposable module for a symmetric algebra
  $Lambda$. Then $Soc(P) tilde.equiv P slash Rad(P)$.
] <th:symmetric-socle>

#proof[
  Let $e$ be a primitive idempotent in $Lambda$ with $P tilde.equiv Lambda e$.
  Let $lambda : Lambda -> k$ be a linear map as in
  Definition~@def:frobenius-symmetric. Then $Soc(P) = Soc(P) . e$ is a left
  ideal of $Lambda$ and so there is an element $x in Soc(P)$ with
  $lambda(x . e) != 0$. By the symmetry, $lambda(e . x) != 0$ and so
  $e . Soc(P) != 0$. But $e . Soc(P) tilde.equiv Hom_Lambda (P, Soc(P))$ by
  Lemma~@lem:idempotent-hom[(i)], and so there is a non-zero homomorphism from
  $P$ to $Soc(P)$, which therefore induces an isomorphism from $P slash Rad(P)$
  to $Soc(P)$.
]

#remark[
  We shall see in Section~@sec:operations that the group algebra of a finite
  group over a field of any characteristic is an example of a symmetric algebra.
]

#exercises[
  + Show that for a module $M$ over a self injective algebra we have
    $
      M tilde.equiv Omega Omega^(-1)(M) plus.o ("projective")
      tilde.equiv Omega^(-1) Omega(M) plus.o ("projective").
    $
    In particular, as long as $M$ has no projective summands, $M$ is
    indecomposable if and only if $Omega(M)$ is indecomposable.
  + Show that a finite dimensional algebra $Lambda$ is self injective if and
    only if for each simple $Lambda$-module $S$ with projective cover $P_S$,
    $Soc(P_S)$ is simple, and whenever $S tilde.equiv.not S'$,
    $Soc(P_S) tilde.equiv.not Soc(P_(S'))$.
  + Show that a finite dimensional self injective algebra $Lambda$ is Frobenius
    if and only if for each projective indecomposable $Lambda$-module $P$,
    $dim_k Soc(P) = dim_k P slash Rad(P)$.
  + Show that if $Lambda$ is a finite dimensional symmetric algebra then so is
    $Mat_n (Lambda)$.
]
