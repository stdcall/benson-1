#import "main-defs.typ": *
#import "statements.typ": *

== The Auslander algebra <sec:auslander-algebra>

#definition[
  The *Auslander algebra*#idx("algebra", "Auslander")#idx(
    "Auslander",
    "algebra",
  ) of a finite dimensional algebra $Lambda$ is defined to be
  $ Aus(Lambda) = End_Lambda (Xi) $#idx("$\"Aus\"(Lambda)$")
  where $Xi = plus.o.big_alpha M_alpha$ is a direct sum of one $Lambda$-module
  from each isomorphism class of finitely generated indecomposable
  $Lambda$-modules.
] <def:auslander-algebra>

The following lemma is a direct consequence of the definitions.

#lemma(closed: true)[
  The following are equivalent:
  + $Lambda$ has finite representation type.
  + $Xi$ is a finitely generated $Lambda$-module.
  + $Aus(Lambda)$ is a finite dimensional algebra.
] <lem:auslander-finite-type>

#source(143)Now given a covariant additive functor
$F : lmodule(Lambda, bold("mod")) -> lmodule(k, bold("Vec"))$ we produce a
module for $Aus(Lambda)$ by taking the direct sum $plus.o.big_alpha F(M_alpha)$
as the underlying vector space, and letting $Aus(Lambda)$ act in the obvious
way. Namely, an endomorphism of $plus.o.big_alpha M_alpha$ is specified by
giving a homomorphism $M_alpha -> M_beta$ for each pair of indices $alpha$,
$beta$ in such a way that for each $alpha$ all but finitely many are zero. This
gives a homomorphism $F(M_alpha) -> F(M_beta)$ for each pair, with the same
restriction, and hence an endomorphism of $plus.o.big_alpha F(M_alpha)$. Of
course, if $Lambda$ has finite representation type then this module is just
$F(Xi)$. We shall write $F(Xi)$ for this $Aus(Lambda)$-module even when $Lambda$
does not have finite representation type, despite the fact that in this case
$Xi$ is not in $lmodule(Lambda, bold("mod"))$. All we are really doing is
extending $F$ in a natural way to the category of $Lambda$-modules which are
(possibly infinite) direct sums of finite dimensional ones.

Conversely, if $X$ is an $Aus(Lambda)$-module then we define a covariant
additive functor
$Phi_X : lmodule(Lambda, bold("mod")) -> lmodule(k, bold("Vec"))$ as follows. If
$M$ is a finitely generated $Lambda$-module, then $Hom_Lambda (M, Xi)$ is an
$Aus(Lambda)$-module and we set
$ Phi_X (M) = Hom_(Aus(Lambda)) (Hom_Lambda (M, Xi), X). $

#lemma[
  If $F : lmodule(Lambda, bold("mod")) -> lmodule(k, bold("Vec"))$ is a
  covariant additive functor then there is a natural isomorphism
  $ Hom_(Aus(Lambda)) (Hom_Lambda (M, Xi), F(Xi)) tilde.equiv F(M). $
] <lem:auslander-hom-functor>

#proof[
  Since both sides are additive in $M$, we may assume without loss of generality
  that $M$ is indecomposable. Choose a split surjection
  $pi : Xi arrow.r.twohead M$, with splitting $i : M arrow.r.hook Xi$, so that
  $pi compose i = id_M$. If $phi.alt$ is an element of the left hand side of the
  above equation, then $F(pi)(phi.alt(i)) in F(M)$. Conversely if $x in F(M)$
  then the map taking $rho : M -> Xi$ to $F(rho)(x) in F(Xi)$ is an
  $Aus(Lambda)$-module homomorphism. It is easy to check that these processes
  are mutually inverse. In particular, any other split surjection gives rise to
  a map with the same inverse, which is therefore the same map.
]

#proposition[
  There is an equivalence of categories between $bold("Fun")(Lambda)$ and the
  category of $Aus(Lambda)$-modules, given in one direction by $F |-> F(Xi)$ and
  in the other direction by $X |-> Phi_X$.

  The finitely generated functors correspond to $Aus(Lambda)$-modules which are
  quotients of $Hom_Lambda (M, Xi)$ for some finitely generated $Lambda$-module
  $M$. Note that this is not the same as the category of finitely generated
  $Aus(Lambda)$-modules unless $Lambda$ has finite representation type.
] <prop:functors-auslander-modules>

#proof[
  If $X$ is an $Aus(Lambda)$-module then
  $
    Phi_X (Xi) = Hom_(Aus(Lambda)) (Hom_Lambda (Xi, Xi), X)
    = Hom_(Aus(Lambda)) (Aus(Lambda), X) tilde.equiv X.
  $
  Conversely if $F in bold("Fun")(Lambda)$ then
  $
    Phi_(F(Xi)) (M) = Hom_(Aus(Lambda)) (Hom_Lambda (M, Xi), F(Xi))
    tilde.equiv F(M)
  $
  by the lemma.

  The statement about finitely generated functors follows immediately from the
  definitions.
]

#corollary[
  #source(144)There is a natural one–one correspondence between simple
  $Aus(Lambda)$-modules and finitely generated indecomposable $Lambda$-modules.
] <cor:simple-auslander-modules>

#proof[
  This follows from Theorem~@th:auslander-functors and
  Proposition~@prop:functors-auslander-modules.
]

#remark(kind: "Remarks")[
  + In the case of finite representation type, a similar equivalence exists
    between $bold("Fun")^compose (Lambda)$ and $Aus(Lambda)^op$-modules, but
    this breaks down for infinite representation type.
  + The simple $Aus(Lambda)$-module corresponding to an indecomposable
    $Lambda$-module $M$ is $Hom_Lambda (M, Xi)$ modulo those homomorphisms which
    are not split monomorphisms. We shall give this the same name $S_M$ as the
    corresponding functor. As a vector space, this is just
    $End_Lambda (M) slash J End_Lambda (M)$. Endomorphisms of $M$ give rise to
    endomorphisms of $S_M$, and so we have
    $
      End_(Aus(Lambda)) (S_M)
      tilde.equiv End_Lambda (M) slash J End_Lambda (M).
    $
  + We shall see later that in fact the algebra $Aus(Lambda)$ has global
    dimension two. In other words, every $Aus(Lambda)$-module has a projective
    resolution of the form
    $ 0 -> P_2 -> P_1 -> P_0 -> X -> 0. $
    This is related to the theory of almost split sequences. The Ext-quiver of
    $Aus(Lambda)$ is called the *Auslander–Reiten quiver*#idx(
      "Auslander",
      "–Reiten",
      "quiver",
    )#idx("quiver", "Auslander–Reiten") of $Lambda$, and this is also intimately
    connected with the theory of almost split sequences. But more of this later.
]
