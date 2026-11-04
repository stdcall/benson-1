#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-13-irreducible-maps.typ": irreducible-factorisation

== Irreducible maps and the Auslander–Reiten quiver <sec:irreducible-maps>

In this section, we describe a certain modulated quiver called the
Auslander–Reiten quiver, associated with almost split sequences, and describe
its elementary properties.

#definition[
  Suppose $M$ and $N$ are finitely generated indecomposable $Lambda$-modules. A
  map $lambda : M -> N$ is said to be *irreducible*#idx("irreducible map") if
  $lambda$ has no left or right inverse, and whenever $lambda = nu compose mu$
  is a factorisation of $lambda$, either $mu$ has a left inverse or $nu$ has a
  right inverse.
] <def:irreducible-map>

If $M = plus.o.big M_i$ and $N = plus.o.big N_j$ with the $M_i$ and $N_j$
indecomposable, we denote by $Rad(M, N)$ the space of maps $M -> N$ with the
property that no component $M_i -> N_j$ is an isomorphism. We denote by
$Rad^2 (M, N)$ the space #source(162)spanned by the homomorphisms of the form
$nu compose mu$ with $mu in Rad(M, M')$ and $nu in Rad(M', N)$ for some $M'$.
Then the set of irreducible maps is precisely $Rad(M, N) without Rad^2 (M, N)$.
The space $Irr(M, N) = Rad(M, N) slash Rad^2 (M, N)$ is an
$(End_Lambda (N) slash J End_Lambda (N))$–$(End_Lambda (M) slash
  J End_Lambda (M))$-bimodule.

The *Auslander–Reiten quiver*#idx("Auslander", "–Reiten", "quiver")#idx(
  "quiver",
  "Auslander–Reiten",
) of $Lambda$ is the modulated quiver given as follows. The vertices $x_alpha$
are indexed by the finitely generated indecomposable $Lambda$-modules $M_alpha$,
with associated division ring
$ Delta_alpha = (End_Lambda (M_alpha) slash J End_Lambda (M_alpha))^op. $
There is an arrow $x_alpha limits(->)^gamma x_beta$ if and only if
$Irr(M_alpha, M_beta) != 0$, and
$
  #aligned-rows(
    ($lmodule(beta, M)^gamma_alpha = M_(alpha beta)$, $= Irr(M_alpha, M_beta)$),
    (
      $lmodule(alpha, M)^gamma_beta = M'_(alpha beta)$,
      $= Hom_k (lmodule(beta, M)^gamma_alpha, k)
      tilde.equiv Hom_(Delta_alpha) (lmodule(beta, M)^gamma_alpha, Delta_alpha)
      tilde.equiv Hom_(Delta_beta) (lmodule(beta, M)^gamma_alpha, Delta_beta)$,
    ),
    (
      $lmodule(beta, d)^gamma_alpha = d_(alpha beta)$,
      $= dim_(Delta_alpha) (lmodule(beta, M)^gamma_alpha)$,
    ),
    (
      $lmodule(alpha, d)^gamma_beta = d'_(alpha beta)$,
      $= dim_(Delta_beta) (lmodule(alpha, M)^gamma_beta) quad "and"$,
    ),
    ($f_alpha$, $= dim_k (Delta_alpha).$),
  )
$

#lemma[
  If $lambda : M -> N$ is irreducible, then $lambda$ is either an epimorphism
  whose kernel is indecomposable, or a monomorphism whose cokernel is
  indecomposable.
] <lem:irreducible-epi-mono>

#proof[
  The factorisation $M limits(->)^mu M slash Ker(lambda) limits(->)^nu N$ shows
  that $lambda$ is either an epimorphism or a monomorphism.

  Suppose $lambda$ is an epimorphism with kernel $A plus.o B$. Then there is a
  factorisation
  $
    M limits(->)^mu M slash A limits(->)^nu M slash (A plus.o B) tilde.equiv N.
  $
  Since $mu$ is an epimorphism it does not have a left inverse, and so $nu$ has
  a right inverse $rho : N -> M slash A$. Similarly we obtain a right inverse
  $rho' : N -> M slash B$ for the map $nu' : M slash B -> N$. Since $M$ is the
  pullback of $nu$ and $nu'$, $rho$ and $rho'$ determine a map $N -> M$ right
  inverse to $lambda$, and so $lambda$ is not irreducible. The dual argument
  works for $lambda$ a monomorphism.
]

#proposition[
  + If $N$ is a non-projective indecomposable $Lambda$-module, let the almost
    split sequence terminating in $N$ be
    $0 -> D T r thin N -> E limits(->)^sigma N -> 0$. Then $lambda : N' -> N$ is
    irreducible if and only if $N'$ is a summand of $E$ and
    $lambda = sigma compose i$ with $i$ an inclusion of $N'$ as a summand of
    $E$.

    If $N$ is projective indecomposable, $lambda : N' -> N$ is irreducible if
    and only if $lambda$ is an inclusion of $N'$ as a summand of $Rad(N)$.
  + If $M$ is a non-injective indecomposable $Lambda$-module, let the almost
    split sequence beginning with $M$ be
    $0 -> M limits(->)^(sigma') E -> T r D thin M -> 0$. Then $lambda : M -> M'$
    is irreducible if and only if $M'$ is a summand of $E$ and
    $lambda = pi compose sigma'$ with $pi$ a projection of $E$ onto $M'$ as a
    summand.

    If $M$ is injective indecomposable, $lambda : M -> M'$ is irreducible if and
    only if $lambda$ is a projection of $M slash Soc(M)$ onto $M'$ as a summand.
] <prop:irreducible-maps>

#source(163)

#proof[
  + Suppose first that $N$ is non-projective.
    $ #irreducible-factorisation $
    Since $lambda$ is not an isomorphism, $lambda$ factors as
    $sigma compose mu$. Since $sigma$ does not have a right inverse, $mu$ has a
    left inverse. Thus we may take $i = mu$.

    Conversely if $N'$ is a direct summand of $E$ with inclusion $i$, we must
    show that $sigma compose i$ is irreducible. Suppose it can be expressed as a
    composite $N' limits(->)^mu N'' limits(->)^nu N$. If $nu$ does not have a
    right inverse, then $nu$ factors through $sigma$, and so $mu$ has a left
    inverse.

    If $N$ is projective then every map to $N$ either has a right inverse or
    lands inside $Rad(N)$. Thus an irreducible map to $N$ must be an injection,
    and the inclusion into $Rad(N)$ has a left inverse.
  + This is proved dually.
]

#remark(kind: "Remarks")[
  + This proposition implies that for $M_alpha$ non-injective, $d'_(alpha beta)$
    is equal to the multiplicity of $M_beta$ as a direct summand of the middle
    term of the almost split sequence beginning with $M_alpha$, while for
    $M_alpha$ injective $d'_(alpha beta)$ is equal to the multiplicity of
    $M_beta$ as a direct summand of $M_alpha slash Soc(M_alpha)$. Similarly for
    $M_beta$ non-projective $d_(alpha beta)$ is the multiplicity of $M_alpha$ as
    a direct summand of the middle term of the almost split sequence terminating
    in $M_beta$, while for $M_beta$ projective $d_(alpha beta)$ is the
    multiplicity of $M_alpha$ as a direct summand of $Rad(M_beta)$. It follows
    that the Auslander–Reiten quiver is a locally finite graph; that is, each
    vertex is incident with only finitely many edges.

    It is conjectured that the Auslander–Reiten quiver of a finite dimensional
    algebra of infinite representation type always has infinitely many connected
    components. This has been proved by Crawley-Boevey [@bib:CrawleyBoevey1988b]
    in the case of tame representation type over an algebraically closed field,
    but otherwise this conjecture is still open.
  + Comparing this proposition with the minimal resolutions for the simple
    functors found in the last section, it is not hard to see that the
    Auslander–Reiten quiver of $Lambda$ is the Ext-quiver of the Auslander
    algebra $Aus(Lambda)$.
]

#lemma[
  Suppose $M$ and $N$ are indecomposable $Lambda$-modules and $f : M -> N$ is
  non-zero and is not an isomorphism.
  + There is an irreducible map $lambda : M -> M'$ and a map $mu : M' -> N$ with
    $mu compose lambda != 0$.
  + There is a map $nu : M -> N'$ and an irreducible map $lambda : N' -> N$ with
    $lambda compose nu != 0$.
] <lem:irreducible-factor>

#proof[
  We shall prove (ii); (i) is proved dually using
  Proposition~@prop:almost-split-left. Suppose $N$ is not projective. Let
  $0 -> D T r thin N -> E limits(->)^sigma N -> 0$ be the almost split sequence
  terminating in $N$. Since $f$ is not an isomorphism it factors through
  $sigma$. Write $E = plus.o.big_i E_i$ and
  $f = sigma compose rho = sum_i sigma_i compose rho_i$ with
  $sigma_i : E_i -> N$ #source(164)and $rho_i : M -> E_i$. Since $f != 0$, some
  $sigma_i compose rho_i != 0$, and $sigma_i$ is an irreducible map. On the
  other hand if $N$ is projective then $f$ factors through the injection
  $Rad(N) -> N$ and we apply the same argument.
]

#proposition[
  Suppose $M$ and $N$ are indecomposable $Lambda$-modules, and $f : M -> N$ is
  non-zero and is not an isomorphism. Suppose there is no chain of irreducible
  maps from $M$ to $N$ of length less than $n$.
  + There exists a chain of irreducible maps
    $ M = M_0 -> M_1 -> dots.c -> M_(n-1) -> M_n $
    and a map $M_n -> N$ such that the composite map from $M$ to $N$ is
    non-zero.
  + There exists a chain of irreducible maps
    $ N_0 -> N_1 -> dots.c -> N_(n-1) -> N_n = N $
    and a map $M -> N_0$ such that the composite map from $M$ to $N$ is
    non-zero.
] <prop:irreducible-chains>

#proof[
  This follows from the lemma and induction on $n$.
]

Finite quiver components are especially easy to deal with. The idea of the proof
of the following proposition will reappear in the next chapter when we deal with
bilinear forms on representation rings.

#proposition[
  Suppose that a component $Q$ of the Auslander–Reiten quiver of $Lambda$ has
  only finitely many vertices. Then $Q$ consists of all the indecomposable
  modules in a block of $Lambda$ of finite representation type.
] <prop:finite-component>

#proof[
  Let $CC^Q$ be a complex vector space whose basis elements $e_x$ correspond to
  the vertices of $Q$. Letting $M_x$ denote the indecomposable $Lambda$-module
  corresponding to $x$, we impose a bilinear form on $CC^Q$ by setting
  $(e_x, e_y) = dim_k Hom_Lambda (M_x, M_y)$. For each non-projective $M_x$, we
  have an almost split sequence
  $ 0 -> M_(tau(x)) -> E_x = plus.o.big_(y in x^-) M_y -> M_x -> 0 $
  and we set
  $ f_x = e_x + e_(tau(x)) - sum_(y in x^-) e_y in CC^Q. $
  If $M_x$ is projective, then $Rad(M_x) = plus.o.big_(y in x^-) M_y$ and we set
  $ f_x = e_x - sum_(y in x^-) e_y in CC^Q. $
  It follows from Proposition~@prop:almost-split-functors for $M_x$
  non-projective, and is clear for $M_x$ projective, that $(e_x, f_y) = 0$
  unless $x = y$, and
  $ (e_x, f_x) = dim_k End_Lambda (M_x) slash J End_Lambda (M_x) != 0. $
  Thus the bilinear form $(med, med)$ is non-singular on $CC^Q$.

  Now if $Q$ does not consist of all the indecomposable modules in a block of
  $Lambda$, then there is an indecomposable module $M$ not in $Q$ and a non-zero
  #source(165)homomorphism from $M$ to some $M_x$. By the non-singularity of
  $(med, med)$, we can find a non-zero element $sum lambda_x e_x in CC^Q$ such
  that
  $ dim_k Hom_Lambda (M, M_y) = (sum lambda_x e_x, e_y) $
  for all $y in Q$. Choose $x$ with $lambda_x != 0$, so that
  $(sum lambda_x e_x, f_x) != 0$. If $M_x$ is not projective, then the sequence
  $
    0 -> Hom_Lambda (M, M_(tau(x))) -> Hom_Lambda (M, E_x)
    -> Hom_Lambda (M, M_x)
  $
  is not exact on the right. Hence using Proposition~@prop:almost-split-functors
  again, $M tilde.equiv M_x$, contradicting the fact that $M$ is not in $Q$. On
  the other hand, if $M_x$ is projective, then
  $ Hom_Lambda (M, Rad(M_x)) -> Hom_Lambda (M, M_x) $
  is not surjective, and so there is a surjective map $M -> M_x$. Since $M_x$ is
  projective, this forces $M tilde.equiv M_x$.
]

The projective and injective modules often get in the way when we are looking at
the Auslander–Reiten quiver. Indeed, if we remove all the modules of the form
$(D T r)^n (I)$ for $I$ injective and $(T r D)^n (P)$ for $P$ projective, we
obtain the largest subquiver of the Auslander–Reiten quiver for which $D T r$ is
an automorphism. This is called the *stable quiver*#idx(
  "stable",
  "quiver",
)#idx("quiver", "stable"). In Section~@sec:riedtmann we investigate the possible
structure of a connected component of the stable quiver.

#exercise[
  Show that any short exact sequence $0 -> M -> E -> N -> 0$ with
  $M tilde.equiv D T r(N)$ indecomposable and both maps irreducible is an almost
  split sequence.
]
