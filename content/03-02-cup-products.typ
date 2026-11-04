#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-02-cup-products.typ": cup-twist, cup-yoneda-map

== Cup products <sec:cup-products>

Suppose $Lambda$ is a Hopf algebra over $R$ which is projective as an
$R$-module. If $M$, $M'$, $N$ and $N'$ are $Lambda$-modules which are projective
as $R$-modules, then we define the *cup product*#idx(
  "cup product",
)#idx("product", "cup")
$
  union : Ext^m_Lambda (M, M') times Ext^n_Lambda (N, N')
  -> Ext^(m+n)_Lambda (M times.o_R N, M' times.o_R N')
$
as follows. Choose exact sequences
$
  0 -> M' -> M_(m-1) -> dots.c -> M_0 -> M -> 0 \
  0 -> N' -> N_(n-1) -> dots.c -> N_0 -> N -> 0
$
representing the given elements $zeta in Ext^m_Lambda (M, M')$ and
$eta in Ext^n_Lambda (N, N')$. We can make sure the $M_i$ and $N_j$ are
$R$-projective, for example by choosing the sequences
$
  0 -> M' -> P_(m-1) slash L_zeta -> dots.c -> P_0 -> M -> 0 \
  0 -> N' -> Q_(n-1) slash L_eta -> dots.c -> Q_0 -> N -> 0
$
of Section~@sec:extensions. By Corollary~@cor:kunneth-projective of the Künneth
theorem, the tensor product over $R$ of the complexes
$
  0 -> M' -> M_(m-1) -> dots.c -> M_0 \
  0 -> N' -> N_(n-1) -> dots.c -> N_0
$
is a sequence
$
  0 -> M' times.o_R N' -> (M_(m-1) times.o_R N') plus.o (M' times.o_R N_(n-1))
  -> dots.c -> M_0 times.o_R N_0
$
whose homology is $M times.o_R N$ in degree zero and is exact elsewhere. Thus we
may complete to an exact sequence
$
  0 -> M' times.o_R N' -> (M_(m-1) times.o_R N') plus.o (M' times.o_R N_(n-1))
  -> \
  dots.c -> M_0 times.o_R N_0 -> M times.o_R N -> 0
$
representing an element of $Ext^(m+n)_Lambda (M times.o_R N, M' times.o_R N')$.
Maps of $m$-fold and $n$-fold extensions, as in
Definition~@def:n-fold-extension, tensor together to give a map of
$(m + n)$-fold extensions, and so the resulting element $zeta union eta$ of
$Ext^(m+n)_Lambda (M times.o_R N, M' times.o_R N')$ depends only on $zeta$ and
$eta$.

Since tensor products of chain complexes are associative, cup product is also
associative.

If $Lambda$ is cocommutative, then tensor products of complexes are *graded
commutative*#idx("graded", "commutative")#idx("commutative graded") in the sense
that given complexes $bold(C)$ and $bold(D)$ of $Lambda$-modules, #source(
  69,
)there is an isomorphism of complexes
$
  bold(C) times.o_R bold(D) & -> bold(D) times.o_R bold(C) \
                x times.o y & |-> (-1)^(deg(x) deg(y)) y times.o x
$
It follows that the cup product is graded commutative in the same sense. In
particular the cup product makes $Ext^*_Lambda (R, R)$ a graded commutative ring
with unit.

In terms of projective resolutions, cup product can be viewed as follows. If
$
  bold(P) : & quad dots.c -> P_2 -> P_1 -> P_0 \
  bold(Q) : & quad dots.c -> Q_2 -> Q_1 -> Q_0
$
are resolutions of $M$ and $N$ respectively then again by the Künneth theorem
the tensor product over $R$ of these complexes is a projective resolution of
$M times.o_R N$. If $zeta in Ext^m_Lambda (M, M')$ and
$eta in Ext^n_Lambda (N, N')$ are represented by maps $hat(zeta) : P_m -> M'$
and $hat(eta) : Q_n -> N'$ then
$hat(zeta) times.o hat(eta) : P_m times.o_R Q_n -> M' times.o_R N'$ can be
extended by zero to give a map
$(bold(P) times.o_R bold(Q))_(m+n) -> M' times.o_R N'$. Since
$
  delta(hat(zeta) times.o hat(eta))
  = delta(hat(zeta)) times.o hat(eta)
  + (-1)^(deg(zeta)) hat(zeta) times.o delta(hat(eta))
$
the product of two cocycles is a cocycle, and the product of a cocycle with a
coboundary or a coboundary with a cocycle is a coboundary. This product
therefore passes down to a well defined product on cohomology which may easily
be checked to agree with the map defined above.

In particular, if $M = N = R$ then we may take $bold(P) = bold(Q)$. Thus the
extension of $hat(zeta) times.o hat(eta)$ to a cocycle
$bold(P) times.o_R bold(P) -> M' times.o_R N'$ may be composed with a chain map
$bold(P) -> bold(P) times.o_R bold(P)$ extending the obvious isomorphism
$R times.o_R R -> R$ to give a cocycle $bold(P) -> M' times.o_R N'$. Such a
chain map $Delta : bold(P) -> bold(P) times.o bold(P)$ exists and is unique up
to homotopy by the Comparison Theorem~@th:comparison. It also follows from the
comparison theorem that such a map is homotopy cocommutative and co-associative,
in the sense that the composite of $Delta$ with the map
$bold(P) times.o_R bold(P) -> bold(P) times.o_R bold(P)$ sending
$x times.o y |-> (-1)^(deg(x) deg(y)) y times.o x$ is homotopic to $Delta$, and
$(1 times.o Delta) compose Delta$ is homotopic to
$(Delta times.o 1) compose Delta$. Such a map $Delta$ is called a *diagonal
approximation*#idx("diagonal approximation")#idx(
  "approximation, diagonal",
). In fact we shall see that using the standard resolution, which we shall
investigate soon, the diagonal approximation may be chosen to be co-associative
(not just up to homotopy). The same is not true of cocommutativity, and this is
really the reason for the existence of Steenrod operations, which we shall
discuss in Chapter 4 of Volume II.

We now have two different definitions of products on $Ext^*_Lambda (R, R)$,
namely Yoneda composition (Section~@sec:extensions) and cup product. The
following proposition shows that these agree, and that more generally every cup
product may be viewed as a Yoneda composition. The converse is not true, because
for example Yoneda composition is in general not graded commutative on
$Ext^*_(k G) (M, M)$.

#source(70)

#proposition[
  If $M$, $M'$, $N$ and $N'$ are modules for a Hopf algebra $Lambda$, and
  $zeta in Ext^m_Lambda (M, M')$, $eta in Ext^n_Lambda (N, N')$, then the cup
  product
  $ zeta union eta in Ext^(m+n)_Lambda (M times.o_R N, M' times.o_R N') $
  is equal to the Yoneda composite of
  $ zeta times.o id_(N') in Ext^m_Lambda (M times.o_R N', M' times.o_R N') $
  and
  $ id_M times.o eta in Ext^n_Lambda (M times.o_R N, M times.o_R N'). $
] <prop:cup-yoneda>

#proof[
  Denote by $bold(M)$ and $bold(N)$ complexes
  $
    0 -> M' -> M_(m-1) -> dots.c -> M_0 \
    0 -> N' -> N_(n-1) -> dots.c -> N_0
  $
  which together with maps $epsilon : M_0 -> M$ and $epsilon' : N_0 -> N$
  correspond to elements $zeta in Ext^m_Lambda (M, M')$ and
  $eta in Ext^n_Lambda (N, N')$. Then we have a map of $(m + n)$-fold extensions
  $ #cup-yoneda-map $
  given by the composite maps
  $
    phi.alt_i : cases(
      (bold(M) times.o_R bold(N))_i -> M_0 times.o_R N_i
      limits(->)^epsilon M times.o_R N_i & quad 0 <= i <= n - 1,
      (bold(M) times.o_R bold(N))_i -> M_(i-n) times.o_R N'
      & quad n <= i <= m + n - 1.
    )
  $
  It is easy to check that this diagram commutes, which proves the proposition.
]

#corollary(closed: true)[
  Suppose $Lambda$ is a cocommutative Hopf algebra (for example a group
  algebra). If $zeta in H^* (Lambda, R) = Ext^*_Lambda (R, R)$, denote by
  $zeta_M$ the image of $zeta$ under the natural map
  $
    Ext^*_Lambda (R, R) limits(arrow.r.long)^(times.o_R M) Ext^*_Lambda (M, M)
  $
  given by tensoring exact sequences with $M$. Then for any
  $xi in Ext^*_Lambda (M, M)$ we have
  $ zeta_M compose xi = (-1)^(deg(zeta) deg(xi)) xi compose zeta_M. $
] <cor:cup-graded-central>

In fact, the above discussion becomes clearer at the level of hypercohomology
(see Section~@sec:chain-complex-operations). The tensor product map
$
  bold(Hom)_Lambda (bold(C), bold(D)) times.o_R
  bold(Hom)_Lambda (bold(C)', bold(D)')
  -> bold(Hom)_Lambda (bold(C) times.o_R bold(C)', bold(D) times.o_R bold(D)')
$
gives rise to a cup product map
$
  Ext^*_Lambda (bold(C), bold(D)) times.o_R Ext^*_Lambda (bold(C)', bold(D)')
  & -> Ext^*_Lambda (bold(C) times.o_R bold(C)', bold(D) times.o_R bold(D)') \
  zeta times.o eta & |-> zeta union eta.
$

#source(71)

#lemma[
  If $zeta in Ext^m_(R G) (bold(C), bold(D))$,
  $eta in Ext^n_(R G) (bold(C)', bold(D)')$ then the cup product
  $
    zeta union eta in
    Ext^(m+n)_(R G) (bold(C) times.o_R bold(C)', bold(D) times.o_R bold(D)')
  $
  is equal to the Yoneda composite of
  $
    zeta times.o id_(bold(D)') in
    Ext^m_(R G) (bold(C) times.o_R bold(D)', bold(D) times.o_R bold(D)')
  $
  and
  $
    id_bold(C) times.o eta in
    Ext^n_(R G) (bold(C) times.o_R bold(C)', bold(C) times.o_R bold(D)').
  $
] <lem:cup-yoneda-complexes>

#proof[
  This follows easily from the corresponding (obvious) statement at the level of
  $bold(Hom)$.
]

Since tensor products are graded commutative, so are cup products, in the sense
that the following diagram commutes:
$ #cup-twist $
But in general Yoneda products are not graded commutative. So
$Ext^*_Lambda (bold(C), bold(C))$ is in general a non-commutative graded ring
and a module over the graded commutative ring
$H^* (Lambda, R) = Ext^*_Lambda (R, R)$.

#exercises[
  + (Massey products) Suppose $bold(P)$ is a projective resolution of the
    trivial module $R$ over a Hopf algebra $Lambda$, and
    $Delta : bold(P) -> bold(P) times.o_R bold(P)$ is a diagonal approximation.
    Choose a chain homotopy
    $theta : bold(P) -> bold(P) times.o_R bold(P) times.o_R bold(P)$ from
    $(Delta times.o 1) compose Delta$ to $(1 times.o Delta) compose Delta$. If
    $alpha$, $beta$ and $gamma$ are cocycles $bold(P) -> R$ representing
    cohomology classes $a$, $b$ and $c$, and with cup products $a b = 0$ and
    $b c = 0$, choose cochains $u$ and $v$ with
    $(alpha times.o beta) compose Delta = delta u$ and
    $(beta times.o gamma) compose Delta = delta v$. Show that the cochain
    $
      (u times.o gamma) compose Delta
      - (-1)^(deg(alpha)) (alpha times.o v) compose Delta \
      - (-1)^(deg(alpha) + deg(beta) + deg(gamma))
      (alpha times.o beta times.o gamma) compose theta
    $
    is a cocycle, and its cohomology class is well defined modulo the ideal
    generated by $a$ and $c$, and independent of the choices of $bold(P)$,
    $Delta$, $theta$, $u$ and $v$. This cohomology class is called the Massey
    product#idx("Massey product")#idx("product", "Massey")
    $chevron.l a, b, c chevron.r$.

    Note that there are two extreme cases in the above set-up. In case $Delta$
    is strictly co-associative (for example for the bar resolution,
    Section~@sec:standard-resolutions), the formula simplifies since we may take
    $theta = 0$. In the other extreme, if we are in a situation where we may
    take for $bold(P)$ the minimal resolution (for example if $Lambda$ is finite
    dimensional over a field) then we have $u = v = 0$ and so the other two
    terms drop out. Thus non-trivial Massey products may be viewed as
    obstructions to finding a strictly co-associative comultiplication on the
    minimal resolution.
  + Give a definition of Massey product with respect to Yoneda composition. Show
    that in the circumstances where the Yoneda composition is #source(
      72,
    )expressible as a cup product as above, your definition agrees with the
    above definition.
]
