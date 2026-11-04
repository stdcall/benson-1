#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-08-induction-restriction.typ": (
  induced-pushout, restricted-pullback, restriction-triangles,
)

== Induction and restriction <sec:induction-restriction>

#definition[
  If $Gamma$ is a subring of a ring $Lambda$ and $M$ is a $Lambda$-module then
  we may restrict the action to give the *restricted*#idx("restriction")
  $Gamma$-module which we write as $M down_Gamma$#idx(
    "$arrow.b$, $arrow.t$, $arrow.t.double$",
  ). If $N$ is a $Gamma$-module we define the *induced*#idx("induction")
  $Lambda$-module $N up^Lambda = Lambda times.o_Gamma N$, where $Lambda$ is
  regarded as a $Lambda$-$Gamma$-bimodule by left and right multiplication. We
  define the *co-induced*#idx("co-induction") $Lambda$-module
  $N Up^Lambda = Hom_Gamma (Lambda, N)$, where $Lambda$ is regarded as a
  $Gamma$-$Lambda$-bimodule by left and right multiplication.
] <def:induction-restriction>

#lemma[
  If $Gamma$ and $Lambda$ are rings, and we have a left $Lambda$-module $M$, a
  $Lambda$-$Gamma$-bimodule $A$ and a left $Gamma$-module $N$, then there is a
  natural isomorphism
  $
    Hom_Gamma (N, Hom_Lambda (A, M)) tilde.equiv
    Hom_Lambda (A times.o_Gamma N, M).
  $
  In other words, $A times.o_Gamma -$ is left adjoint to $Hom_Lambda (A, -)$.
] <lem:tensor-hom-adjunction>

#proof[
  We have maps
  $
    phi.alt : Hom_Gamma (N, Hom_Lambda (A, M))
    -> Hom_Lambda (A times.o_Gamma N, M)
  $
  given by $phi.alt(alpha)(a times.o n) = alpha(n)(a)$ and
  $
    psi : Hom_Lambda (A times.o_Gamma N, M) -> Hom_Gamma (N, Hom_Lambda (A, M))
  $
  given by $psi(beta)(n)(a) = beta(a times.o n)$. It is easy to check that these
  are inverse isomorphisms.
]

#proposition(title: [Nakayama relations])[
  If $Gamma$ is a subring of $Lambda$, $M$ is a $Lambda$-module and $N$ is a
  $Gamma$-module then there are natural isomorphisms
  + $Hom_Gamma (N, M down_Gamma) tilde.equiv
    Hom_Lambda (N up^Lambda, M)$,
  + $Hom_Gamma (M down_Gamma, N) tilde.equiv
    Hom_Lambda (M, N Up^Lambda)$.
  In other words, $down_Gamma$ has a left adjoint $up^Lambda$ and a right
  adjoint $Up^Lambda$.
] <prop:nakayama-relations>
#idx("Nakayama", "relations", target: [@prop:nakayama-relations])#idx(
  "relations",
  "Nakayama",
  target: [@prop:nakayama-relations],
)

#proof[
  + Put $A$ equal to $Lambda$ as a $Lambda$-$Gamma$-bimodule in the lemma, and
    notice that $Hom_Lambda (Lambda, M)$ is equal to $M down_Gamma$ as a
    $Gamma$-module.
  + Put $A$ equal to $Lambda$ as a $Gamma$-$Lambda$-bimodule and swap the rôles
    of $Lambda$ and $Gamma$, and of $M$ and $N$ in the lemma. Notice that
    $Lambda times.o_Lambda M$ is equal to $M down_Gamma$ as a $Gamma$-module.
]

It is worth pointing out that the natural maps
$eta : M -> M down_Gamma Up^Lambda$ and $eta' : M down_Gamma up^Lambda -> M$
corresponding to the identity map on $M down_Gamma$ under the Nakayama
isomorphisms have an obvious interpretation. Namely
$eta(m) in Hom_Gamma (Lambda, M)$ is given by $eta(m)(lambda) = lambda m$; and
if $lambda times.o m in Lambda times.o_Gamma M$ then
$eta'(lambda times.o m) = lambda m$.

#corollary(title: [Eckmann–Shapiro Lemma], head-break: true)[
  #source(59)\(sometimes this is known as Shapiro's lemma#idx(
    "Shapiro's lemma",
  )#idx("lemma", "Shapiro's"), but see [@bib:Eckmann1946]) Suppose that $Gamma$
  is a subring of $Lambda$, and that $Lambda$ is projective as a $Gamma$-module.
  If $M$ is a $Lambda$-module and $N$ is a $Gamma$-module, then
  + $Ext^n_Gamma (N, M down_Gamma) tilde.equiv
    Ext^n_Lambda (N up^Lambda, M)$.
  + $Ext^n_Gamma (M down_Gamma, N) tilde.equiv
    Ext^n_Lambda (M, N Up^Lambda)$.
] <cor:eckmann-shapiro>
#idx("Eckmann–Shapiro lemma", target: [@cor:eckmann-shapiro])#idx(
  "lemma",
  "Eckmann–Shapiro",
  target: [@cor:eckmann-shapiro],
)

#proof[
  Choose a projective resolution
  $ bold(P) : quad dots.c -> P_2 -> P_1 -> P_0 $
  of $N$ as a $Gamma$-module. Since
  $(lmodule(Gamma, Gamma)) up^Lambda = lmodule(Lambda, Lambda)$
  and induction preserves direct sums, induction takes projective
  $Gamma$-modules to projective $Lambda$-modules. Since $Lambda$ is projective
  as a $Gamma$-module, induction takes exact sequences to exact sequences, and
  so
  $
    bold(P) up^Lambda : quad dots.c -> P_2 up^Lambda
    -> P_1 up^Lambda -> P_0 up^Lambda
  $
  is a projective resolution of $N up^Lambda$ as a $Lambda$-module. Hence
  $
    #aligned-rows(
      (
        $Ext^n_Gamma (N, M down_Gamma)$,
        $= H^n (Hom_Gamma (bold(P), M down_Gamma))$,
      ),
      (
        $$,
        $tilde.equiv H^n (Hom_Lambda (bold(P) up^Lambda, M))
        tilde.equiv Ext^n_Lambda (N up^Lambda, M).$,
      ),
    )
  $

  The argument for co-induction is similar.
]

Note that there is a natural surjective map from $M down_Gamma up^Lambda$ to $M$
given by $lambda times.o m |-> lambda m$, and injective map from $N$ to
$N up^Lambda down_Gamma$ given by $n |-> 1 times.o n$.

In terms of $n$-fold extensions, the correspondence given by the Eckmann–Shapiro
lemma is as follows. If
$ 0 -> M down_Gamma -> N_(n-1) -> dots.c -> N_0 -> N -> 0 $
represents an element of $Ext^n_Gamma (N, M down_Gamma)$ then we can form the
pushout
$ #induced-pushout $
to obtain an $n$-fold extension
$
  0 -> M -> X -> N_(n-2) up^Lambda -> dots.c
  -> N_0 up^Lambda -> N up^Lambda -> 0.
$
Conversely if
$ 0 -> M -> M_(n-1) -> dots.c -> M_0 -> N up^Lambda -> 0 $
represents an element of $Ext^n_Lambda (N up^Lambda, M)$ then we form the
pullback
$ #restricted-pullback $
#source(60)to obtain an $n$-fold extension
$
  0 -> M down_Gamma -> M_(n-1) down_Gamma -> dots.c
  -> M_1 down_Gamma -> Y -> N -> 0.
$

Finally, the following is a dimension-shifted version of
Lemma~@lem:tensor-hom-adjunction.

#proposition[
  If $Gamma$ and $Lambda$ are rings, and we have an injective left
  $Lambda$-module $I$, a $Lambda$-$Gamma$-bimodule $A$ and a left $Gamma$-module
  $N$, then
  $
    Ext^n_Gamma (N, Hom_Lambda (A, I)) tilde.equiv
    Hom_Lambda (Tor^Gamma_n (A, N), I).
  $
] <prop:dimension-shifted-adjunction>

#proof[
  Choose a projective resolution
  $ bold(P) : quad dots.c -> P_2 -> P_1 -> P_0 $
  of $N$ as a $Gamma$-module. Then
  $
    Ext^n_Gamma (N, Hom_Lambda (A, I))
    & = H^n (Hom_Gamma (bold(P), Hom_Lambda (A, I))) \
    & tilde.equiv H^n (Hom_Lambda (A times.o_Gamma bold(P), I))
  $
  Since $I$ is injective $Hom_Lambda (-, I)$ takes exact sequences to exact
  sequences and so this is equal to
  $
    Hom_Lambda (H_n (A times.o_Gamma bold(P)), I)
    = Hom_Lambda (Tor^Gamma_n (A, N), I).
  $
]

#exercise[
  Suppose that $Gamma$ is a subring of $Lambda$, and that $Lambda$ is projective
  as a $Gamma$-module. If $M$ and $N$ are $Lambda$-modules, denote by
  $eta : M -> M down_Gamma Up^Lambda$ and $eta' : M down_Gamma up^Lambda -> M$
  the natural maps discussed above. Show that the following diagrams commute.
  $ #restriction-triangles $
  Here, the vertical maps are the Eckmann–Shapiro isomorphisms.
]
