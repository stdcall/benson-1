#import "main-defs.typ": *
#import "statements.typ": *

== Cyclic and abelian groups <sec:cyclic-abelian>
#idx("abelian", "group", target: [@sec:cyclic-abelian])

The standard resolution constructed above is of exponential growth, whereas we
shall see in Chapter~5 of Volume II that for finite groups there always exist
resolutions of polynomial growth. The problem is that resolutions of polynomial
growth are in general much harder to write down. One case where there is an
easily describable *periodic*#idx("periodic", "resolution")#idx(
  "resolution",
  "periodic",
) resolution is the case of a cyclic group#idx("cyclic", "group").

Let $ZZ slash n = chevron.l x | x^n = 1 chevron.r$ be a cyclic group of order
$n$. We have two maps
$
  N : R(ZZ slash n) & -> R(ZZ slash n) & quad quad T : R(ZZ slash n)
  & -> R(ZZ slash n) \
  x & |-> 1 + x + dots.c + x^(n-1) & x & |-> 1 - x.
$

#proposition[
  The sequence
  $
    dots.c stretch(-->)^N R(ZZ slash n) stretch(-->)^T R(ZZ slash n)
    stretch(-->)^N R(ZZ slash n) stretch(-->)^T R(ZZ slash n)
  $
  is a free resolution of $R$ as an $R(ZZ slash n)$-module.
] <prop:cyclic-resolution>

#proof[
  This is easy to check.
]

#corollary(closed: true)[
  If $M$ is an $R(ZZ slash n)$-module then
  $
    #aligned-rows(
      ($H^0 (ZZ slash n, M)$, $= M^(ZZ slash n) = {m in M | (1 - x) m = 0}$),
      (
        $H^(2r) (ZZ slash n, M)$,
        $= M^(ZZ slash n) slash (1 + x + dots.c + x^(n-1)) M quad (r > 0)$,
      ),
      (
        $H^(2r+1) (ZZ slash n, M)$,
        $= {m in M | (1 + x + dots.c + x^(n-1)) m = 0} slash (1 - x) M.$,
      ),
    )
  $
] <cor:cyclic-cohomology>

#corollary[
  Suppose $M$ is an $R G$-module, and $H$ is a normal subgroup of $G$ with
  $G slash H$ cyclic. If $M down_H$ is projective then
  $
    M plus.o ("projective") tilde.equiv tilde(Omega)^2 (M) plus.o
    ("projective").
  $
] <cor:cyclic-quotient-periodicity>

#proof[
  Since $M down_H$ is projective, so is
  $
    M down_H up^G tilde.equiv
    M times.o_R R down_H up^G
    = M times.o_R R(G slash H).
  $
  Thus tensoring $M$ with the sequence
  $ 0 -> R -> R(G slash H) limits(->)^T R(G slash H) -> R -> 0 $
  #source(78)we obtain a sequence of the form
  $ 0 -> M -> ("projective") -> ("projective") -> M -> 0. $
]

The proof of the above corollary also shows the following.

#corollary[
  Suppose $G = ZZ slash n$ is cyclic of order $n$. Then there is an element
  $sigma in H^2 (G, R)$ such that for all $R G$-modules $M$, cup product with
  $sigma$ induces an isomorphism
  $ H^r (G, M) stretch(-->)^tilde.equiv H^(r+2) (G, M) $
  for all $r > 0$. In particular, if $n$ is not invertible in $R$ then $sigma$
  is not nilpotent.
] <cor:cyclic-periodicity>

#proof[
  We take $sigma in Ext_(R G)^2 (R, R)$ to correspond to the 2-fold extension
  $ 0 -> R -> R G limits(->)^T R G -> R -> 0. $
]

We now calculate the ring structure of $H^* (ZZ slash n, k)$, where $k$ is a
field of characteristic $p$. The above calculation shows that
$H^r (ZZ slash n, k)$ is one dimensional over $k$ for each $r$. Choose a
non-zero element $x in H^1 (ZZ slash n, k)$. This is represented, as in
Section~@sec:extensions, by a map $hat(x) : Omega(k) -> k$. Now the projective
cover of $k$ is $k(ZZ slash p^s)$, where $p^s$ is the exact power of $p$
dividing $n$. In other words, the generator for the cyclic group is represented
by a Jordan block of size $p^s$ with eigenvalue 1. The remaining projective
modules are obtained by tensoring this one with the simple modules for
$k(ZZ slash n)$ (if $k$ is a splitting field, these are one dimensional and
there are $n slash p^s$ of them). Thus $Omega(k)$ is a uniserial module of
length $p^s - 1$ with all its composition factors trivial. The map $hat(x)$
takes the unique top composition factor of $Omega(k)$ onto the trivial module.

Now choose a non-zero element $y in H^2 (ZZ slash n, k)$. Since
$Omega^2 (k) tilde.equiv k$, $hat(y) : Omega^2 (k) -> k$ is an isomorphism. We
calculate products by the method at the end of Section~@sec:extensions. Namely,
$y^2$ is represented by the map
$ hat(y) compose Omega^2 (hat(y)) : Omega^4 (k) -> k $
which is again an isomorphism, so that $y^2$ is a non-zero element of
$H^4 (ZZ slash n, k)$. Continuing this way, the powers $y^r$ are non-zero
elements in $H^(2r) (ZZ slash n, k)$. Similarly $x y^r$ is represented by the
surjective map
$
  hat(x) compose Omega(hat(y)) compose Omega^3 (hat(y)) compose dots.c compose
  Omega^(2r-1) (hat(y)) : Omega^(2r+1) (k) tilde.equiv Omega(k) -> k
$
and is hence a non-zero element of $H^(2r+1) (ZZ slash n, k)$.

The only thing left to do now is to calculate $x^2$. This is represented by the
map
$ hat(x) compose Omega(hat(x)) : Omega^2 (k) tilde.equiv k -> Omega(k) -> k. $
If $p^s - 1 = 1$ this composite is a non-zero multiple of $y$. If $p^s - 1 > 1$
then the composite is zero and so $x^2 = 0$.

We summarise the results of this calculation in the following proposition.

#proposition(closed: true)[
  #source(79)Suppose $p^s$ is the $p$-part of $n$, and $k$ is a field of
  characteristic $p$. Then the cohomology ring $H^* (ZZ slash n, k)$ has the
  following structure.
  + If $p^s = 2$ then $H^* (ZZ slash n, k) tilde.equiv k[x]$ with $deg(x) = 1$.
  + If $p^s > 2$ then $H^* (ZZ slash n, k) tilde.equiv k[x, y] slash (x^2)$ with
    $deg(x) = 1$ and $deg(y) = 2$.
] <prop:cyclic-cohomology-ring>

An alternative proof is given in Cartan and Eilenberg [@bib:Cartan1956,
Chap.~XII §7], where more general coefficient rings are discussed. They use the
explicit diagonal approximation
$Delta_(r s) : R(ZZ slash n) -> R(ZZ slash n) times.o_R R(ZZ slash n)$ given by
$
  Delta_(r s)(1) = cases(
    1 times.o 1 & quad r "even",
    1 times.o x & quad r "odd," s "even",
    sum_(0 <= i < j <= n-1) x^i times.o x^j & quad r "odd," s "odd.",
  )
$

To calculate the cohomology of a general finite abelian group, we need a version
of the Künneth formula.

#theorem[
  Suppose $R$ is a hereditary ring of coefficients (see the remark at the end of
  Section~@sec:chain-complex-operations). If $G_1$ and $G_2$ are groups, $M_1$
  is an $R G_1$-module and $M_2$ is an $R G_2$-module, and $M_1$ or $M_2$ is
  projective as an $R$-module, then there is a short exact sequence
  $
    0 -> plus.o.big_(i+j=n) H^i (G_1, M_1) times.o_R H^j (G_2, M_2)
    -> H^n (G_1 times G_2, M_1 times.o_R M_2) \
    -> plus.o.big_(i+j=n+1) Tor_1^R (H^i (G_1, M_1), H^j (G_2, M_2)) -> 0.
  $
  Here, $M_1 times.o_R M_2$ is regarded as an $R(G_1 times G_2)$-module via
  $(g_1, g_2)(m_1 times.o m_2) = g_1 m_1 times.o g_2 m_2$.
] <th:kunneth-groups>
#idx("Künneth", "theorem", target: [@th:kunneth-groups])#idx(
  "theorem",
  "Künneth",
  target: [@th:kunneth-groups],
)

#proof[
  If $bold(P)$ and $bold(Q)$ are finitely generated projective resolutions of
  $R$ as $R G_1$ and $R G_2$-modules respectively, then
  $bold(P) times.o_R bold(Q)$ is a projective resolution of $R$ as an
  $R(G_1 times G_2)$-module (exactness follows from the Künneth
  theorem~@th:kunneth since $R$ is hereditary). The theorem now follows by
  applying Theorem~@th:kunneth to the complex
  $
    Hom_(R(G_1 times G_2)) (bold(P) times.o_R bold(Q), M_1 times.o_R M_2) \
    tilde.equiv Hom_(R G_1) (bold(P), M_1) times.o_R
    Hom_(R G_2) (bold(Q), M_2).
  $
]

#remark[
  If $R = k$ is a field then
  $H^* (G_1 times G_2, k) tilde.equiv H^* (G_1, k) times.o_k H^* (G_2, k)$ as
  graded rings; i.e.,
  $(x times.o y)(x' times.o y') = (-1)^(deg(y) deg(x')) x x' times.o y y'$. This
  follows from the cup product description of the ring structure and the
  corresponding commutativity formula for tensor products of chain complexes.
]

#corollary(closed: true)[
  If $G = (ZZ slash p)^s$ is an elementary abelian group of order $p^s$ and $k$
  is a field of characteristic $p$ then the cohomology ring $H^* (G, k)$ has the
  following structure.
  + If $p = 2$ then $H^* (G, k) tilde.equiv k[x_1, dots, x_s]$ is a polynomial
    algebra with $deg(x_i) = 1$.
  + #source(80)If $p > 2$ then
    $H^* (G, k) tilde.equiv Lambda(x_1, dots, x_s) times.o_k k[y_1, dots, y_s]$
    is a tensor product of an exterior algebra and a polynomial algebra with
    $deg(x_i) = 1$, $deg(y_i) = 2$.
] <cor:elementary-abelian-cohomology>
