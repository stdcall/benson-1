#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-12-almost-split.typ": (
  almost-split-comparison, almost-split-factorisation, almost-split-pushout,
  almost-split-pushout-back, induced-almost-split,
)

== Almost split sequences <sec:almost-split>

Almost split sequences were introduced by Auslander and Reiten
[@bib:Auslander1975]. They proved their existence for Artin algebras (a ring is
an *Artin algebra*#idx("Artin algebra")#idx("algebra", "Artin") if it is
finitely generated as a module over its centre, and its centre is an Artinian
ring). We shall content ourselves with the case of a finite dimensional algebra,
even though the proof for a general Artin algebra is not much harder. Finally we
shall show how almost split sequences are related to functor categories.

#definition[
  Let $Lambda$ be a ring. A short exact sequence of finitely generated
  $Lambda$-modules
  $ 0 -> M -> E limits(->)^sigma N -> 0 $
  is called an *almost split sequence*#idx("almost split sequence")#idx(
    "sequence",
    "almost split",
  ) or *Auslander–Reiten sequence*#idx("Auslander", "–Reiten", "sequence")#idx(
    "sequence",
    "Auslander–Reiten",
  ) if the following conditions are satisfied:
  + $M$ and $N$ are indecomposable.
  + The map $sigma$ does not split.
  + Given any $Lambda$-module $N'$ and map $rho : N' -> N$ which is not a split
    epimorphism then $rho$ factors through $sigma$ as in the following diagram:
    $ #almost-split-factorisation $
  Note that if $rho$ is a split epimorphism, that is, $N$ is a summand of $N'$
  and $rho$ is the projection, then by condition (ii) $rho$ cannot factor
  through $sigma$.
] <def:almost-split-sequence>

The extraordinary thing about this definition is that such sequences should
exist at all. Clearly if $N$ is projective, there can be no almost split
sequence terminating in $N$.

#theorem(title: [Auslander, Reiten [@bib:Auslander1975]])[
  Suppose $Lambda$ is an Artin algebra. Given any finitely generated
  indecomposable non-projective module $N$, there exists an almost split
  sequence terminating in $N$. This sequence is unique up to isomorphism of
  short exact sequences.
] <th:almost-split-existence>

We shall only prove this theorem for finite dimensional algebras. We first prove
uniqueness, since this is a general argument and is quite easy.

#lemma[
  Suppose
  $
    0 -> M -> E limits(->)^sigma N -> 0 \
    0 -> M' -> E' limits(->)^(sigma') N -> 0
  $
  are almost split sequences terminating in the same module $N$. Then they are
  isomorphic as short exact sequences.
] <lem:almost-split-unique>

#source(156)

#proof[
  The definition guarantees us a commutative diagram:
  $ #almost-split-comparison $
  The composite map $M -> M' -> M$ is not nilpotent since otherwise the map
  $sigma$ would split. Thus by Fitting's Lemma~@lem:fitting it is an
  isomorphism, and so by the five lemma the sequences are isomorphic.
]

The idea of the proof of existence of almost split sequences is as follows.
Given an indecomposable module $N$, let us suppose that we can find an
indecomposable module $M$ depending functorially on $N$, and such that there is
a natural duality between $Hom_Lambda (N, -)$ and $Ext^1_Lambda (-, M)$. Well,
we should modify this slightly since Ext does not see homomorphisms which factor
through a projective module. So we work in the stable module category
$lmodule(Lambda, underline(bold("mod")))$ (see
Section~@sec:categories-functors), and let us suppose that
$underline(Hom)_Lambda (N, -)$ and $Ext^1_Lambda (-, M)$ are dual. Since for $N$
non-projective $underline(End)_Lambda (N)$ is a local ring and
$Ext^1_Lambda (N, M)$ is its dual, the latter has a simple socle as an
$underline(End)_Lambda (N)$-module. We claim that any extension
$0 -> M -> E limits(->)^sigma N -> 0$ representing a non-zero element of this
socle is an almost split sequence. This is because
$
  & rho : N' -> N "is split epi" \
  & <=> rho_* : underline(Hom)_Lambda (N, N') -> underline(End)_Lambda (N)
    "has" id_N "in its image" \
  & <=> rho_* : underline(Hom)_Lambda (N, N') -> underline(End)_Lambda (N)
    "is surjective" \
  & <=> rho^* : Ext^1_Lambda (N, M) -> Ext^1_Lambda (N', M) "is injective" \
  & <=> rho^* "does not kill" Soc Ext^1_Lambda (N, M) \
  & <=> rho "does not factor through" sigma.
$

The required functor taking $N$ to $M$ is called the *Auslander–Reiten
translation*#idx("Auslander", "–Reiten", "translation")#idx(
  "translation",
  "Auslander–Reiten",
) $D T r$#idx("$D T r$"), and is the composite of two contravariant functors
$T r$ and $D$.

The first clue as to how to obtain the required functor is the identity
$
  Ext^1_Lambda (N, Hom_k (N', k)) tilde.equiv
  Hom_k (Tor^Lambda_1 (N', N), k)
$
from Proposition~@prop:dimension-shifted-adjunction. So the functor $D$ is
simply the duality functor. If $M$ is a finitely generated module then we set
$
  D(M) = M^* = Hom_k (M, k) tilde.equiv Hom_Lambda (M, Hom_k (Lambda, k))
  = Hom_Lambda (M, Lambda^*),
$
as a finitely generated $Lambda^op$-module. Here, $Lambda^*$ is a
$Lambda$-$Lambda$-bimodule in the obvious way. We also write $D$ for the
corresponding functor from finitely generated $Lambda^op$-modules to finitely
generated $Lambda$-modules, so that
$D^2 : lmodule(Lambda, bold("mod")) -> lmodule(Lambda, bold("mod"))$ is
isomorphic to the identity functor. $D$ passes down to these quotients to
#source(157)give dualities
$D : lmodule(Lambda, underline(bold("mod")))
-> lmodule(Lambda^op, overline(bold("mod")))$
and $D : lmodule(Lambda, overline(bold("mod")))
-> lmodule(Lambda^op, underline(bold("mod")))$. It should be pointed out that we
now have three different notations for vector space duality, namely $D(M)$,
$M^*$ and $Hom_k (M, k)$. We apologise for this burden on the reader, which has
arisen in an attempt not to break with traditional notations.

We are thus left with the problem of finding a contravariant functor
$T r : lmodule(Lambda, underline(bold("mod")))
-> lmodule(Lambda^op, underline(bold("mod")))$
with the property that
$ underline(Hom)_Lambda (N, -) tilde.equiv Tor^Lambda_1 (T r thin N, -). $
The way to construct this functor is as follows. Form the beginning of a
projective resolution
$ P_1 limits(->)^f P_0 -> N -> 0 $
and let $T r thin N$ be the cokernel of the $Lambda^op$-module homomorphism
$ f^* : Hom_Lambda (P_0, Lambda) -> Hom_Lambda (P_1, Lambda). $

Now $T r$ is a well defined contravariant functor from
$lmodule(Lambda, underline(bold("mod")))$ to
$lmodule(Lambda^op, underline(bold("mod")))$, and it is easy to see that
$T r^2 : lmodule(Lambda, underline(bold("mod")))
-> lmodule(Lambda, underline(bold("mod")))$
is isomorphic to the identity functor.

We have an exact sequence
$
  0 -> Hom_Lambda (N, Lambda) -> Hom_Lambda (P_0, Lambda)
  -> Hom_Lambda (P_1, Lambda) -> T r thin N -> 0
$
whose last three terms form the beginning of a projective resolution of
$T r thin N$ as a $Lambda^op$-module, and so we may use it to calculate Tor.
Namely,
$
  #aligned-rows(
    (
      $Tor^Lambda_1 (T r thin N, N')$,
      $= frac(
        Ker(
          Hom_Lambda (P_0, Lambda) times.o N'
          -> Hom_Lambda (P_1, Lambda) times.o N'
        ),
        Im(
          Hom_Lambda (N, Lambda) times.o N'
          -> Hom_Lambda (P_0, Lambda) times.o N'
        )
      )$,
    ),
    (
      $$,
      $= frac(
        Ker(Hom_Lambda (P_0, N') -> Hom_Lambda (P_1, N')),
        Im(Hom_Lambda (N, Lambda) times.o N' -> Hom_Lambda (P_0, N'))
      )$,
    ),
    (
      $$,
      $= frac(
        Hom_Lambda (N, N'),
        Im(Hom_Lambda (N, Lambda) times.o N' -> Hom_Lambda (N, N'))
      )$,
    ),
    ($$, $= underline(Hom)_Lambda (N, N').$),
  )
$

We have thus proved that
$ underline(Hom)_Lambda (N, N') tilde.equiv Tor^Lambda_1 (T r thin N, N') $
so that
$
  #aligned-rows(
    (
      $Ext^1_Lambda (N', D T r thin N)$,
      $= Ext^1_Lambda (N', Hom_k (T r thin N, k))$,
    ),
    ($$, $tilde.equiv Hom_k (Tor^Lambda_1 (T r thin N, N'), k)$),
    ($$, $tilde.equiv Hom_k (underline(Hom)_Lambda (N, N'), k)$),
  )
$
as required. To complete the proof of the existence of almost split sequences
for finite dimensional algebras, we only need show that $D T r$ takes
indecomposables to indecomposables. But both $D$ and $T r$ are self inverse, and
so they must take indecomposables to indecomposables.

#source(158)Note that $D T r$ gives a bijection between the non-projective
indecomposable $Lambda$-modules and the non-injective indecomposable
$Lambda$-modules. Thus given any non-injective indecomposable $Lambda$-module
$M$, there is a unique almost split sequence beginning with $M$, and it has the
form $0 -> M -> E -> T r D thin M -> 0$. This is related to the following dual
property of almost split sequences.

#proposition[
  If $0 -> M limits(->)^(sigma') E -> N -> 0$ is an almost split sequence and
  $rho : M -> M'$ is not a split monomorphism then $rho$ factors through
  $sigma'$.
] <prop:almost-split-left>

#proof[
  Suppose $rho$ does not factor through $sigma'$. Then in the pushout
  $ #almost-split-pushout $
  the second sequence does not split. Thus we may complete a diagram
  $ #almost-split-pushout-back $
  Since $rho' compose rho$ is not nilpotent it is an isomorphism by Fitting's
  Lemma~@lem:fitting, and so $rho$ is a split monomorphism.
]

#corollary(closed: true)[
  If $0 -> M -> E -> N -> 0$ is an almost split sequence then so is
  $0 -> N^* -> E^* -> M^* -> 0$.
] <cor:almost-split-dual>

We now give an interpretation of almost split sequences in terms of functor
categories. The following proposition is clear from the definition:

#proposition(closed: true)[
  An almost split sequence of $Lambda$-modules
  $ 0 -> M -> E -> N -> 0 $
  gives rise to exact sequences
  $ 0 -> Hom_Lambda (N', M) -> Hom_Lambda (N', E) -> Hom_Lambda (N', N) -> 0 $
  if $N'$ has no summand isomorphic to $N$, and
  $
    0 -> Hom_Lambda (N, M) -> Hom_Lambda (N, E) -> End_Lambda (N) \
    -> End_Lambda (N) slash J End_Lambda (N) -> 0.
  $
  Dually, we have exact sequences
  $ 0 -> Hom_Lambda (N, M') -> Hom_Lambda (E, M') -> Hom_Lambda (M, M') -> 0 $
  #source(159)if $M'$ has no summand isomorphic to $M$, and
  $
    0 -> Hom_Lambda (N, M) -> Hom_Lambda (E, M) -> End_Lambda (M) \
    -> End_Lambda (M) slash J End_Lambda (M) -> 0.
  $
] <prop:almost-split-functors>

We may express this in terms of functors as an exact sequence of contravariant
functors
$ 0 -> (-, M) -> (-, E) -> (-, N) -> S_N -> 0 $
where $S_N$ is the simple functor associated to $N$, as in
Theorem~@th:auslander-functors.

Similarly the dual property of almost split sequences shows that there is also
an exact sequence of covariant functors
$ 0 -> (N, -) -> (E, -) -> (M, -) -> S_M -> 0. $

Since $M$ and $N$ are indecomposable, $(M, -)$, $(N, -)$, $(-, M)$ and $(-, N)$
are projective indecomposable functors, and so the above sequences are *minimal
projective resolutions*#idx("minimal resolution")#idx("resolution", "minimal")
of the simple functors $S_N$ for $N$ non-projective indecomposable and $S_M$ for
$M$ non-injective indecomposable in $bold("Fun")^compose (Lambda)$ and
$bold("Fun")(Lambda)$ respectively.

Similarly if $N$ is projective indecomposable then there is a minimal projective
resolution of $S_N$ in $bold("Fun")^compose (Lambda)$ of the form
$ 0 -> (-, Rad(N)) -> (-, N) -> S_N -> 0 $
while if $M$ is injective indecomposable then there is a minimal resolution of
$S_M$ in $bold("Fun")(Lambda)$ of the form
$ 0 -> (M slash Soc(M), -) -> (M, -) -> S_M -> 0. $

Dually, we have injective resolutions
$ 0 -> S_M -> D(M, -) -> D(E, -) -> D(N, -) -> 0 $
and
$ 0 -> S_N -> D(-, N) -> D(-, E) -> D(-, M) -> 0 $
in $bold("Fun")^compose (Lambda)$ and $bold("Fun")(Lambda)$ respectively, and
similarly for the injective/projective modules.

#exercise[
  Show that if $0 -> M -> E -> N -> 0$ is a short exact sequence of finitely
  generated $Lambda$-modules with the property that
  $ 0 -> (-, M) -> (-, E) -> (-, N) -> S_(N_0) -> 0 $
  is exact, then the sequence is the sum of the almost split sequence
  terminating in $N_0$ and a split sequence. (Hint: write
  $N = n . N_0 plus.o N'$ and apply the sequence of functors to $N$)
]

There is one situation in which the almost split sequence is easy to write down.

#source(160)

#proposition[
  Suppose $P$ is a projective and injective indecomposable module. Then there is
  an almost split sequence
  $ 0 -> Rad(P) -> P plus.o Rad(P) slash Soc(P) -> P slash Soc(P) -> 0. $
  This is the only almost split sequence having $P$ as a summand of the middle
  term.
] <prop:almost-split-projective-injective>

#proof[
  It is easy to check directly from the definitions that this is an almost split
  sequence. Conversely, if $P$ is a summand of the middle term of an almost
  split sequence and the right-hand term is not $P slash Soc(P)$, then there is
  a map from $P slash Soc(P)$ to the right-hand term which is not a split
  epimorphism and does not lift, contradicting the definition of an almost split
  sequence.
]

We are particularly interested in almost split sequences for group algebras of
finite groups. The first observation holds for all symmetric algebras.

#proposition[
  Suppose $Lambda$ is a finite dimensional symmetric algebra. Then for any
  non-projective indecomposable module $M$ we have $D T r(M) = Omega^2 (M)$, the
  second kernel of a minimal resolution of $M$.
] <prop:symmetric-dtr>

#proof[
  Since $Lambda$ is symmetric, $Lambda tilde.equiv Lambda^*$ as
  $Lambda$–$Lambda$-bimodules. Hence the functors $Hom_Lambda (-, Lambda^*)$ and
  $Hom_Lambda (-, Lambda)$ coincide, and so the functor $T r$ applied to $M$
  yields the dual of $Omega^2 (M)$.
]

Note in particular that in this situation
$
  Ext^1_Lambda (N, D T r thin M) = Ext^1_Lambda (N, Omega^2 (M))
  tilde.equiv underline(Hom)_Lambda (N, Omega(M))
$
and so the duality between $underline(Hom)_Lambda (M, N)$ and
$Ext^1_Lambda (N, D T r thin M)$ becomes a duality between the spaces
$underline(Hom)_Lambda (M, N)$ and $underline(Hom)_Lambda (N, Omega(M))$.

#proposition(closed: true)[
  Suppose $Lambda$ is a finite dimensional symmetric algebra. Then there is a
  natural duality between the spaces $underline(Hom)_Lambda (M, N)$ and
  $underline(Hom)_Lambda (N, Omega(M))$.
] <prop:symmetric-duality>

#remark[
  In case $Lambda$ is self injective but not necessarily symmetric, we may
  modify the above propositions as follows. We define $nu$#idx("$nu$") to be the
  *Nakayama functor*#idx("Nakayama", "functor")#idx("functor", "Nakayama")
  $ nu = Lambda^* times.o_Lambda - = D Hom_Lambda (-, Lambda). $
  Then we have $D T r = nu Omega^2$, and there is a natural duality between the
  spaces $underline(Hom)_Lambda (M, N)$ and
  $underline(Hom)_Lambda (N, nu Omega(M))$.
]

We now specialise to group algebras.

#proposition[
  An almost split sequence $0 -> M -> E -> N -> 0$ of modules for a group
  algebra $k G$ splits on restriction to a subgroup $H$ if and only if $H$ does
  not contain a vertex of $N$ (or equivalently of $M$).
] <prop:almost-split-restriction>

#source(161)

#proof[
  The sequence splits on restriction to $H$ if and only if for all $k H$-modules
  $N'$ the sequence
  $
    0 -> Hom_(k H) (N', M down_H) -> Hom_(k H) (N', E down_H)
    -> Hom_(k H) (N', N down_H) -> 0
  $
  is exact. By the Nakayama relations~@prop:nakayama-relations-groups this
  happens if and only if the sequence
  $
    0 -> Hom_(k G) (N' up^G, M) -> Hom_(k G) (N' up^G, E)
    -> Hom_(k G) (N' up^G, N) -> 0
  $
  is exact. By the defining property of almost split sequences, this happens if
  and only if $N$ is not a direct summand of $N' up^G$ for any $k H$-module
  $N'$.
]

The following theorem was proved in [@bib:Benson1984d].

#theorem[
  Suppose $M$ is an indecomposable $k G$-module with vertex $D$, and suppose $H$
  is a subgroup of $G$ containing $N_G (D)$, so that the Green correspondent
  $f(M)$ is defined as a $k H$-module. If $0 -> Omega^2 f(M) -> E -> f(M) -> 0$
  is the almost split sequence terminating in $f(M)$, then the induced sequence
  $0 -> Omega^2 f(M) up^G -> E up^G -> f(M) up^G -> 0$ is isomorphic to the
  direct sum of the almost split sequence terminating in $M$ and a (possibly
  zero) split short exact sequence.
] <th:almost-split-green-correspondence>

#proof[
  By the Nakayama Relations~@prop:nakayama-relations-groups and
  Proposition~@prop:almost-split-functors, we have a diagram
  $ #induced-almost-split $
  By the Burry–Carlson–Puig Theorem~@th:burry-carlson-puig, we have
  $S_(f(M)) (N down_H) tilde.equiv S_M (N)$, and so we have an exact sequence
  $
    0 -> Hom_(k G) (N, Omega^2 f(M) up^G) -> Hom_(k G) (N, E up^G) \
    -> Hom_(k G) (N, f(M) up^G) -> S_M (N) -> 0.
  $
  The result now follows from the exercise before
  Proposition~@prop:almost-split-projective-injective.
]
