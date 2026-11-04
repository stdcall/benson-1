#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-05-long-exact-sequences.typ": (
  first-extension, hom-resolution, horseshoe, tensored-resolution,
)

== Long exact sequences <sec:long-exact-sequences>

#lemma(title: [Horseshoe lemma])[
  #source(47)If $0 -> M' -> M -> M'' -> 0$ is a short exact sequence of left
  $Lambda$-modules, then given projective resolutions
  $ dots.c -> P'_2 -> P'_1 -> P'_0, quad dots.c -> P''_2 -> P''_1 -> P''_0 $
  of $M'$ and $M''$, we may complete to a short exact sequence of chain
  complexes
  $ #horseshoe $
] <lem:horseshoe>
#idx("horseshoe lemma", target: [@lem:horseshoe])#idx(
  "lemma",
  "horseshoe",
  target: [@lem:horseshoe],
)

#proof[
  It is easy to construct the required maps by induction, using the definition
  of a projective module.
]

#proposition[
  Suppose that
  $ 0 -> M' -> M -> M'' -> 0 $
  is a short exact sequence of left $Lambda$-modules.
  + If $M_0$ is a right $Lambda$-module, there is a long exact sequence#idx(
      "long exact sequence",
    )#idx("exact sequence, long")#idx(
      "sequence",
      "long exact",
    )
    $
      dots.c -> Tor^Lambda_n (M_0, M') -> Tor^Lambda_n (M_0, M)
      -> Tor^Lambda_n (M_0, M'') \
      -> Tor^Lambda_(n-1) (M_0, M') -> dots.c \
      dots.c -> Tor^Lambda_1 (M_0, M'') -> M_0 times.o_Lambda M'
      -> M_0 times.o_Lambda M -> M_0 times.o_Lambda M'' -> 0.
    $
  + If $M_0$ is a left $Lambda$-module there is a long exact sequence
    $
      0 -> Hom_Lambda (M'', M_0) -> Hom_Lambda (M, M_0)
      -> Hom_Lambda (M', M_0) \
      -> Ext^1_Lambda (M'', M_0) -> dots.c \
      dots.c -> Ext^n_Lambda (M'', M_0) -> Ext^n_Lambda (M, M_0)
      -> Ext^n_Lambda (M', M_0) \
      -> Ext^(n+1)_Lambda (M'', M_0) -> dots.c
    $
] <prop:long-exact-sequences>

#proof[
  + Tensor $M_0$ with the diagram given in the lemma and use
    Proposition~@prop:long-exact-homology.
  + Take homs from the diagram given in the lemma to $M_0$ and use
    Proposition~@prop:long-exact-cohomology.
]

Exactly the same proof shows in general that if $F : cal(A) -> cal(B)$ is a
right exact covariant additive functor then there is a long exact sequence
$
  dots.c -> L_n F(M') -> L_n F(M) -> L_n F(M'') -> L_(n-1) F(M') -> dots.c \
  -> L_1 F(M'') -> F(M') -> F(M) -> F(M'') -> 0,
$
#source(48)while if $F$ is a left exact contravariant additive functor then
there is a long exact sequence
$
  0 -> F(M'') -> F(M) -> F(M') -> R^1 F(M'') -> dots.c \
  -> R^n F(M'') -> R^n F(M) -> R^n F(M') -> R^(n+1) F(M'') -> dots.c
$
Of course, similar statements are true of the right derived functors of a left
exact covariant functor and left derived functors of right exact contravariant
functors. We leave the interested reader to formulate these cases.

We also obtain exact sequences in the other variable as follows.

#proposition[
  + Suppose that
    $ 0 -> M_0 -> M_1 -> M_2 -> 0 $
    is a short exact sequence of right $Lambda$-modules, and $M'$ is a left
    $Lambda$-module. Then there is a long exact sequence
    $
      dots.c -> Tor^Lambda_n (M_0, M') -> Tor^Lambda_n (M_1, M')
      -> Tor^Lambda_n (M_2, M') \
      -> Tor^Lambda_(n-1) (M_0, M') -> dots.c \
      dots.c -> Tor^Lambda_1 (M_2, M') -> M_0 times.o_Lambda M'
      -> M_1 times.o_Lambda M' -> M_2 times.o_Lambda M' -> 0.
    $
  + Suppose that $0 -> M_0 -> M_1 -> M_2 -> 0$ is a short exact sequence of left
    $Lambda$-modules and $M'$ is a left $Lambda$-module. Then there is a long
    exact sequence
    $
      0 -> Hom_Lambda (M', M_0) -> Hom_Lambda (M', M_1)
      -> Hom_Lambda (M', M_2) \
      -> Ext^1_Lambda (M', M_0) -> dots.c \
      dots.c -> Ext^n_Lambda (M', M_0) -> Ext^n_Lambda (M', M_1)
      -> Ext^n_Lambda (M', M_2) \
      -> Ext^(n+1)_Lambda (M', M_0) -> dots.c
    $
] <prop:long-exact-other-variable>

#proof[
  + Tensoring the short exact sequence with a resolution
    $ dots.c -> P'_2 -> P'_1 -> P'_0 $
    of $M'$ as a left $Lambda$-module gives a short exact sequence of chain
    complexes
    $ #tensored-resolution $
    Applying Proposition~@prop:long-exact-homology yields the required long
    exact sequence.
  + If
    $ dots.c -> P'_2 -> P'_1 -> P'_0 $
    #source(49)is a projective resolution of $M'$ as a left $Lambda$-module,
    then applying Proposition~@prop:long-exact-cohomology to the short exact
    sequence of cochain complexes
    $ #hom-resolution $
    yields the required long exact sequence.
]

#corollary[
  If $M$ is a module for an Artinian ring $Lambda$ and $S$ is a simple
  $Lambda$-module then
  + $Ext^n_Lambda (M, S) tilde.equiv Hom_Lambda (Omega^n M, S)$
  + $Ext^n_Lambda (S, M) tilde.equiv Hom_Lambda (S, Omega^(-n) M)$.
] <cor:ext-simple>

#proof[
  + Let
    $ dots.c -> P_2 -> P_1 -> P_0 $
    be a minimal resolution of $M$. Then the complex
    $
      Hom_Lambda (P_0, S) -> Hom_Lambda (P_1, S) -> Hom_Lambda (P_2, S)
      -> dots.c
    $
    has zero differential, since if the composite $P_(n+1) -> P_n -> S$ is
    non-zero then $P_n$ has a summand isomorphic to the projective cover of $S$
    and which is in the image of $P_(n+1) -> P_n$ and hence in the kernel of
    $P_n -> P_(n-1)$, contradicting the minimality of $P_n$. Hence
    $
      Ext^n_Lambda (M, S) & = Hom_Lambda (P_n, S)
                            = Hom_Lambda (P_n slash Im(P_(n+1) -> P_n), S) \
                          & = Hom_Lambda (Omega^n M, S).
    $
  + is proved similarly, using part~(ii) of the following proposition.
]

#proposition[
  + Suppose that $M'$ is a right $Lambda$-module and
    $ dots.c -> P'_2 -->^(partial'_2) P'_1 -->^(partial'_1) P'_0 -> M' -> 0 $
    is a resolution of $M'$ by projective right $Lambda$-modules. Then
    $
      Tor^Lambda_n (M', M)
      tilde.equiv H_n (bold(P)' times.o M, partial'_* times.o 1).
    $
    In particular if $M'$ is projective then $Tor^Lambda_n (M', M) = 0$ for
    $n > 0$.
  + Suppose that $M'$ is a left $Lambda$-module and
    $ 0 -> M' -> I'_0 -->^(delta^0) I'_1 -->^(delta^1) I'_2 -> dots.c $
    is an injective resolution of $M'$. Then
    $
      Ext^n_Lambda (M, M') tilde.equiv H^n (Hom_Lambda (M, bold(I)'), delta^*).
    $
    #source(50)In particular if $M'$ is injective then
    $Ext^n_Lambda (M, M') = 0$ for $n > 0$.
] <prop:balance>

#proof[
  We shall prove (ii), since the proof of (i) is the dual of the same argument.
  The proof is an example of the inductive technique of *dimension
  shifting*#idx("dimension", "shifting"). We denote by
  $cal(E X T)^n_Lambda (M, M')$ the groups
  $H^n (Hom_Lambda (M, bold(I)'), delta^*)$, and we wish to show that
  $Ext^n_Lambda (M, M') tilde.equiv cal(E X T)^n_Lambda (M, M')$.

  Choose a short exact sequence
  $ 0 -> M_1 -> P -> M -> 0 $
  with $P$ projective. Then the long exact sequence
  $
    dots.c -> Ext^(n-1)_Lambda (P, M') -> Ext^(n-1)_Lambda (M_1, M') -> \
    Ext^n_Lambda (M, M') -> Ext^n_Lambda (P, M') -> dots.c
  $
  shows that $Ext^n_Lambda (M, M') tilde.equiv Ext^(n-1)_Lambda (M_1, M')$.

  The functor $cal(E X T)$ also clearly has long exact sequences in each
  variable by the same arguments as above, and so we obtain
  $cal(E X T)^n_Lambda (M, M') tilde.equiv cal(E X T)^(n-1)_Lambda (M_1, M')$.

  We are now finished by induction, since the case $n = 1$ follows from the
  diagram
  $ #first-extension $
]

#corollary(closed: true)[
  If either $M$ or $M'$ is flat then $Tor^Lambda_n (M', M) = 0$ for all $n > 0$.
] <cor:flat-tor-vanishing>

The proof of the following may now be safely left to the reader.

#proposition(closed: true)[
  #part-lines[
    + $Ext^n_Lambda (M, M') tilde.equiv Ext^(n-1)_Lambda (tilde(Omega)(M), M')
      tilde.equiv Ext^(n-1)_Lambda (M, tilde(Omega)^(-1)(M'))$ for $n > 1$.
    + $Tor^Lambda_n (M, M') tilde.equiv Tor^Lambda_(n-1) (tilde(Omega)(M), M')
      tilde.equiv Tor^Lambda_(n-1) (M, tilde(Omega)(M'))$ for $n > 1$.
  ]
] <prop:dimension-shifting>

#exercise[
  Formulate and prove a version of Proposition~@prop:balance for derived
  functors of functors of two variables with appropriate exactness properties.
]
