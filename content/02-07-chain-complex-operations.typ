#import "main-defs.typ": *
#import "statements.typ": *

== Operations on chain complexes <sec:chain-complex-operations>

In this section, we discuss tensors and homs, duality, Ext and Tor for chain
complexes. The theory is parallel to the theory for modules, but the signs need
some attention. We leave the reader to formulate the corresponding notions for
cochain complexes.

We begin by discussing tensor products#idx("tensor", "product", "of complexes").
If $bold(C)$ and $bold(D)$ are chain complexes of right, resp. left
$Lambda$-modules, we define
$
  (bold(C) times.o_Lambda bold(D))_n
  = plus.o.big_(i+j=n) C_i times.o_Lambda D_j.
$
The differential
$
  partial_n : (bold(C) times.o_Lambda bold(D))_n
  -> (bold(C) times.o_Lambda bold(D))_(n-1)
$
is given by
$
  partial_n (x times.o y)
  = partial_i (x) times.o y + (-1)^i x times.o partial_j (y)
$
for $x in C_i$, $y in D_j$. The introduction of the signs $(-1)^i$ ensures that
$partial_n compose partial_(n+1) = 0$, as is easily checked.

The general convention about signs#idx("sign convention") is that if we pass
something of degree $i$ through something of degree $j$, we should multiply by
the sign $(-1)^(i j)$. We regard $partial$ as being of degree $-1$, so that the
above sign of $(-1)^i$ comes from passing the $partial$ through the $x$. As long
as one follows this convention carefully, the signs should take care of
themselves.

This boundary formula shows that if $x$ and $y$ are cycles then so is
$x times.o y$, and if one is a cycle and the other is a boundary then
$x times.o y$ is a boundary. Thus we have a well defined product map
$
  H_i (bold(C)) times.o_Lambda H_j (bold(D))
  -> H_(i+j)(bold(C) times.o_Lambda bold(D)).
$

#theorem(title: [Künneth theorem])[
  #source(55)If the cycles $Z_n (bold(C))$ and the boundaries $B_n (bold(C))$
  are flat $Lambda$-modules for all $n$, then there is a short exact sequence
  $
    0 -> plus.o.big_(i+j=n) H_i (bold(C)) times.o_Lambda H_j (bold(D))
    -> H_n (bold(C) times.o_Lambda bold(D)) -> \
    plus.o.big_(i+j=n-1) Tor^Lambda_1 (H_i (bold(C)), H_j (bold(D))) -> 0.
  $
] <th:kunneth>
#idx("Künneth", "theorem", target: [@th:kunneth])#idx(
  "theorem",
  "Künneth",
  target: [@th:kunneth],
)

#proof[
  Since $Z(bold(C))$ is flat, we have
  $
    (Z(bold(C)) times.o_Lambda Z(bold(D)))_n
    & = Ker (1 times.o partial : (Z(bold(C)) times.o_Lambda bold(D))_n
      -> (Z(bold(C)) times.o_Lambda bold(D))_(n-1)) \
    (Z(bold(C)) times.o_Lambda B(bold(D)))_n
    & = Im (1 times.o partial : (Z(bold(C)) times.o_Lambda bold(D))_(n+1)
      -> (Z(bold(C)) times.o_Lambda bold(D))_n)
  $
  and so
  $
    H(Z(bold(C)) times.o_Lambda bold(D)) = Z(bold(C)) times.o_Lambda H(bold(D)).
  $
  Similarly
  $
    H(B(bold(C)) times.o_Lambda bold(D)) = B(bold(C)) times.o_Lambda H(bold(D)).
  $

  We now tensor the short exact sequence of complexes
  $ 0 -> B(bold(C)) ->^i Z(bold(C)) -> H(bold(C)) -> 0 $
  with $H(bold(D))$. By Corollary~@cor:flat-tor-vanishing,
  $Tor^Lambda_1 (Z(bold(C)), H(bold(D))) = 0$ and so the long exact sequence of
  Section~@sec:long-exact-sequences becomes #symbol-display(
    "†",
    $
      0 -> Tor^Lambda_1 (H(bold(C)), H(bold(D)))
      -> H(B(bold(C)) times.o_Lambda bold(D))
      -->^(i_*) H(Z(bold(C)) times.o_Lambda bold(D)) \
      -> H(bold(C)) times.o_Lambda H(bold(D)) -> 0.
    $,
  ) <eq:kunneth-sequence>

  We next tensor the short exact sequence of complexes
  $ 0 -> Z(bold(C)) -> bold(C) -> B(bold(C))[-1] -> 0 $
  (where $[-1]$ denotes a shift of degree $-1$, so that
  $(B(bold(C))[-1])_n = B_(n-1)(bold(C))$) with $bold(D)$. Since
  $Tor^Lambda_1 (B(bold(C)), bold(D)) = 0$ we obtain a short exact sequence
  $
    0 -> Z(bold(C)) times.o_Lambda bold(D) -> bold(C) times.o_Lambda bold(D)
    -> (B(bold(C)) times.o_Lambda bold(D))[-1] -> 0.
  $
  Taking homology we obtain
  $
    dots.c -> H(B(bold(C)) times.o_Lambda bold(D))
    -> H(Z(bold(C)) times.o_Lambda bold(D))
    -> H(bold(C) times.o_Lambda bold(D)) \
    -> H(B(bold(C)) times.o_Lambda bold(D))[-1]
    -> H(Z(bold(C)) times.o_Lambda bold(D))[-1] -> dots.c
  $
  It is not hard to show that the boundary map of this sequence is the map
  $i_*$, and so we have
  $ 0 -> Coker(i_*) -> H(bold(C) times.o_Lambda bold(D)) -> Ker(i_*)[-1] -> 0 $
  which, using the exact sequence @eq:kunneth-sequence above, becomes
  $
    0 -> H(bold(C)) times.o_Lambda H(bold(D))
    -> H(bold(C) times.o_Lambda bold(D))
    -> Tor^Lambda_1 (H(bold(C)), H(bold(D)))[-1] -> 0.
  $
]

#corollary[
  #source(56)If $Z_n (bold(C))$ and $H_n (bold(C))$ are projective
  $Lambda$-modules for all $n$ then
  $
    H_n (bold(C) times.o_Lambda bold(D)) tilde.equiv
    plus.o.big_(i+j=n) H_i (bold(C)) times.o_Lambda H_j (bold(D)).
  $
] <cor:kunneth-projective>

#proof[
  The sequence
  $ 0 -> B_n (bold(C)) -> Z_n (bold(C)) -> H_n (bold(C)) -> 0 $
  splits since $H_n (bold(C))$ is projective, and so $B_n (bold(C))$ is also
  projective. Thus $Z_n (bold(C))$ and $B_n (bold(C))$ are flat, and also
  $Tor^Lambda_1 (H_i (bold(C)), H_j (bold(D))) = 0$, so the result follows from
  the Künneth theorem.
]

#corollary(closed: true)[
  If $Z_n (bold(C))$ and $H_n (bold(C))$ are projective $Lambda$-modules and
  either $bold(C)$ or $bold(D)$ is exact then so is
  $bold(C) times.o_Lambda bold(D)$.
] <cor:kunneth-exact>

#remark[
  The case $Lambda = R$ a commutative ring of coefficients is a useful special
  case of the above theorems. In particular, if $R$ is *hereditary*#idx(
    "hereditary ring",
  )#idx("ring", "hereditary"), namely if every submodule of a projective module
  is projective (for example this happens if $R$ is a Dedekind domain) then as
  long as the modules $C_n$ are projective over $R$ then the cycles
  $Z_n (bold(C))$ and boundaries $B_n (bold(C))$ are projective and hence flat,
  so that the hypothesis of Theorem~@th:kunneth is satisfied.

  We shall see in Section 3.6 of Volume II that the Künneth theorem is an
  especially simple case of the *Künneth spectral sequence*#idx(
    "Künneth",
    "spectral sequence",
  )#idx("spectral sequence", "Künneth") in which the hypotheses on
  $Z_n (bold(C))$ and $B_n (bold(C))$ are dropped. This special case is the one
  where the spectral sequence has only two non-vanishing columns, and no
  non-zero differentials.
]

Next we discuss homomorphisms. If $bold(C)$ and $bold(D)$ are chain complexes of
left $Lambda$-modules, we define a new chain complex#idx("$bold(\"Hom\")$")
$
  bold(Hom)_Lambda (bold(C), bold(D))_n = product_(i+n=j) Hom_Lambda (C_i, D_j)
$
with differential
$
  partial_n : bold(Hom)_Lambda (bold(C), bold(D))_n
  -> bold(Hom)_Lambda (bold(C), bold(D))_(n-1)
$
defined so that
$ partial_j (f_i (x)) = (partial_n f)_i (x) + (-1)^n f_(i-1)(partial_i (x)) $
for $f = (f_i)$ with $f_i in Hom_Lambda (C_i, D_j)$ and $x in C_i$. In other
words, $partial_n$ is defined by
$ (partial_n f)_i (x) = partial_j (f_i (x)) - (-1)^n f_(i-1)(partial_i (x)), $
i.e., $partial f = [partial, f]$, the graded commutator of $partial$ and $f$.

If $M$ is a left $Lambda$-module, we write $M[n]$ for the chain complex
consisting of $M$ in degree $-n$ and zero elsewhere. If $bold(C)$ is a chain
complex of left $Lambda$-modules, we write $bold(C)[n]$#idx("$bold(C)[n]$") for
$Lambda[n] times.o_Lambda bold(C)$. Namely we have
$(bold(C)[n])_i = (bold(C))_(i+n)$. Note that the differential in $bold(C)[n]$
is $(-1)^n$ times the differential in $bold(C)$.

#source(57)The *dual*#idx("dual", "of chain complex")#idx(
  "chain",
  "complex",
  "dual of",
) of $bold(C)$ is the chain complex of right $Lambda$-modules
$bold(Hom)_Lambda (bold(C), Lambda[0])$. Note that the differential on the dual
is given by
$ (partial_n f)(x) = (-1)^(n-1) f(partial_(-n+1)(x)). $
Evaluation is a map of chain complexes
$ bold(Hom)_Lambda (bold(C), Lambda[0]) times.o_Lambda bold(C) -> Lambda[0] $
sending $f times.o x$ to $f(x)$.

We now discuss Ext and Tor for chain complexes. This is sometimes also called
*hypercohomology*#idx("hypercohomology").

#definition[
  Suppose that $bold(C)$ is a chain complex of left $Lambda$-modules, bounded
  below. Then a *projective resolution*#idx(
    "projective",
    "resolution",
    "of chain complex",
  )#idx("chain", "complex", "projective resolution of") of $bold(C)$ is a chain
  complex $bold(P)$ of projective left $Lambda$-modules, bounded below, together
  with a map of chain complexes $bold(P) -> bold(C)$ which is an isomorphism on
  homology.#ed-note[The list of corrections of the author states that this
    definition is not right and that the Cartan–Eilenberg resolutions cannot be
    avoided: maps of complexes lift to a resolution in the above sense only up
    to homotopy, and it is not a double complex, as the spectral sequences built
    from it in Volume II require; see Weibel [@bib:Weibel1994], Definition 5.7.1
    and Lemma 5.7.2.]
] <def:complex-resolution>

Note that in the case $bold(C) = M[0]$, this agrees with
Definition~@def:projective-resolution. Existence of projective resolutions is
easy to prove inductively using the definition of projective modules. The
Comparison Theorem~@th:comparison also holds for projective resolutions of chain
complexes, up to homotopy.

If $bold(D)$ is a chain complex of right $Lambda$-modules, we may thus define
$ Tor^Lambda_n (bold(D), bold(C)) = H_n (bold(D) times.o_Lambda bold(P)), $
and this will be independent of the choice of projective resolution $bold(P)$.
Note that if $bold(D)$ is also bounded below, and $bold(P)'$ is a projective
resolution of $bold(D)$, then
$bold(D) times.o_Lambda bold(P) <- bold(P)' times.o_Lambda bold(P)
-> bold(P)' times.o_Lambda bold(C)$ induce isomorphisms on homology, so that
$ Tor^Lambda_n (bold(D), bold(C)) = H_n (bold(P)' times.o_Lambda bold(C)). $
This gives an alternative proof of Proposition~@prop:balance.

Similarly if $bold(D)$ is a chain complex of left $Lambda$-modules, we may
define
$ Ext^n_Lambda (bold(C), bold(D)) = H^n (bold(Hom)_Lambda (bold(P), bold(D))). $
(Note that $H^n$ really means $H_(-n)$; we are regarding a chain complex as a
cochain complex by negating the degrees.) If $bold(D)$ is bounded above, and
$bold(I)$ is an injective resolution of $bold(D)$ (defined in the obvious way),
then
$
  bold(Hom)_Lambda (bold(P), bold(D)) -> bold(Hom)_Lambda (bold(P), bold(I))
  <- bold(Hom)_Lambda (bold(C), bold(I))
$
induce isomorphisms on homology, and so
$ Ext^n_Lambda (bold(C), bold(D)) = H^n (bold(Hom)_Lambda (bold(C), bold(I))). $
If $Lambda$ is an augmented algebra, we write $H_n (Lambda, bold(C))$ and
$H^n (Lambda, bold(C))$ for the abelian groups $Tor^Lambda_n (bold(C), R)$ and
$Ext^n_Lambda (R, bold(C))$.

Composition of maps in $bold(Hom)$ gives rise to Yoneda composition
$
  Ext^*_Lambda (bold(D), bold(E)) times.o Ext^*_Lambda (bold(C), bold(D))
  -> Ext^*_Lambda (bold(C), bold(E)),
$
which agrees with the usual Yoneda composition in case $bold(C)$, $bold(D)$ and
$bold(E)$ are modules concentrated in degree zero. Indeed, this was part of the
original #source(58)motivation for the definition of the derived category, which
is really what we are using in disguise (see [@bib:Deligne1977], Appendix~1).

#exercise[
  Show that an element $f in bold(Hom)_Lambda (bold(C), bold(D))_0$ is a map of
  chain complexes if and only if $f$ is a cycle ($partial_0 f = 0$), and that
  $f$ and $g$ are homotopic if and only if $f - g$ is a boundary.
]
