#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-08-functor-categories.typ": (
  kernel-ladder, representable-lift,
)

== Functor categories <sec:functor-categories>

In the last section, we classified the indecomposable representations of the
Dynkin diagrams by using the geometry of root systems. In the next few sections,
we present another method of classification, first formulated explicitly by
Gabriel. This is the method of functorial filtrations, and is based on
Auslander's work on the structure of functor categories. The idea is as follows.
We consider functors from the module category in question to vector spaces.
There are obvious notions of subfunctor and quotient functor, and it turns out
that the simple functors are in one–one correspondence with the indecomposable
modules. It is this observation of Auslander that initiated this circle of
ideas. It follows that to find all the indecomposable modules, it suffices to
find all the simple functors. We look at any functor which reflects isomorphisms
(see Definition~@def:reflect-isomorphisms), for example the underlying vector
space functor, and find its simple composition factors. Of course, in practice
this is easier said than done, but we shall give some examples where this method
has proved effective. We shall study in detail the case of the group algebras of
the dihedral groups (Ringel [@bib:Ringel1975b]), and mention without proof the
corresponding answer for the semidihedral groups (Crawley-Boevey
[@bib:CrawleyBoevey1989b]). Our exposition is broadly based on Gabriel
[@bib:Gabriel1975] and Ringel [@bib:Ringel1975b].

#definition[
  If $Lambda$ is a finite dimensional algebra over a field $k$, we denote by
  $bold("Fun")(Lambda)$ (resp. $bold("Fun")^compose (Lambda)$)#idx(
    "$bold(\"Fun\")(Lambda)$, $bold(\"Fun\")^compose (Lambda)$",
  ) the category whose objects are the covariant#idx("covariant functor")#idx(
    "functor",
    "covariant",
  ) (resp. contravariant#idx("contravariant functor")#idx(
    "functor",
    "contravariant",
  )) additive functors $lmodule(Lambda, bold("mod")) -> lmodule(k, bold("Vec"))$
  from finitely generated $Lambda$-modules to $k$-vector spaces, and whose
  morphisms are the natural transformations of functors.
] <def:functor-category>

#example(kind: "Examples")[
  + There is the forgetful functor $rho in bold("Fun")(Lambda)$ which assigns to
    each $Lambda$-module its underlying vector space.
  + Duality is a contravariant functor
    $D : lmodule(k, bold("Vec")) -> lmodule(k, bold("Vec"))$. Composing with
    this duality functor gives contravariant functors also denoted
    $D : bold("Fun")(Lambda) -> bold("Fun")^compose (Lambda)$ and
    $D : bold("Fun")^compose (Lambda) -> bold("Fun")(Lambda)$.
  + For any $Lambda$-module $M$ there is a covariant representable functor
    $ (M, -) = Hom_Lambda (M, -) in bold("Fun")(Lambda) $
    and a contravariant representable functor
    $ (-, M) = Hom_Lambda (-, M) in bold("Fun")^compose (Lambda). $
    #source(141)There are also the dual functors
    $
      D(M, -) in bold("Fun")^compose (Lambda) quad "and" quad
      D(-, M) in bold("Fun")(Lambda).
    $
]

It is easy to check directly that $bold("Fun")(Lambda)$ satisfies the axioms for
an abelian category, and we shall see later that it has a natural interpretation
as a module category for the *Auslander algebra*.

The kernel of a natural transformation $F_1 arrow.r.squiggly F_2$ of functors is
the functor assigning to each module $M$ the vector space kernel of
$F_1 (M) -> F_2 (M)$ and to each homomorphism $M -> M'$ the map of kernels
making the following diagram commute.
$ #kernel-ladder $
Cokernels are constructed dually. A natural transformation
$F_1 arrow.r.squiggly F_2$ is a monomorphism if and only if $F_1 (M) -> F_2 (M)$
is injective for each $M$. In this case we may identify $F_1$ as a
*subfunctor*#idx("subfunctor") of $F_2$. The *quotient functor*#idx(
  "quotient",
  "functor",
)#idx("functor", "quotient") $F_2 slash F_1$ is defined by
$(F_2 slash F_1)(M) = F_2 (M) slash F_1 (M)$. A *simple functor*#idx(
  "simple functor",
)#idx("functor", "simple") is defined to be a non-zero functor with no proper
subfunctors. A *finitely generated*#idx("finitely generated", "functor")#idx(
  "functor",
  "finitely generated",
) functor is one which is isomorphic to a quotient of $(M, -)$ for some $M$.

Similarly $bold("Fun")^compose (Lambda)$ is an abelian category and the notions
of subfunctor, quotient functor, simple functor and finitely generated functor
are defined analogously.

#theorem(title: [Auslander])[
  The finitely generated projective objects#idx("projective", "functor")#idx(
    "functor",
    "projective",
  ) in the category $bold("Fun")(Lambda)$ (resp. $bold("Fun")^compose (Lambda)$)
  are the representable functors $(M, -)$ (resp. $(-, M)$).

  If $M$ is indecomposable then the functor $(M, -)$ (resp. $(-, M)$) has a
  unique maximal subfunctor, written $Rad(M, -)$ (resp. $Rad(-, M)$), consisting
  of those homomorphisms which are not split monomorphisms (resp. split
  epimorphisms). Every simple functor in $bold("Fun")(Lambda)$ (resp.
  $bold("Fun")^compose (Lambda)$) is of the form
  $S_M = (M, -) slash Rad(M, -)$#idx("$S_M$") (resp.
  $S_M = (-, M) slash Rad(-, M)$) for some indecomposable $Lambda$-module $M$.
] <th:auslander-functors>
#idx("Auslander", "'s theorem", target: [@th:auslander-functors])#idx(
  "theorem",
  "Auslander's",
  target: [@th:auslander-functors],
)

#proof[
  We shall prove these statements in $bold("Fun")(Lambda)$; the statements in
  $bold("Fun")^compose (Lambda)$ are proved dually.

  First we shall prove that representable functors are projective. To show that
  $(M, -)$ is projective, we must show that given natural transformations
  $lambda$ and $mu$ as in the following diagram
  $ #representable-lift $
  #source(142)we may find $nu$ such that $mu compose nu = lambda$. But by
  Yoneda's Lemma~@lem:yoneda#idx("lemma", "Yoneda's")#idx("Yoneda", "lemma"),
  $ Nat((M, -), F_i) tilde.equiv F_i (M) $
  so that the map
  $ Nat((M, -), F_1) limits(arrow.r.long)^(mu_*) Nat((M, -), F_2) $
  is epi and so we may find $nu$ such that $mu compose nu = mu_* (nu) = lambda$.

  Conversely, if $F$ is a finitely generated projective object in
  $bold("Fun")(Lambda)$ then $F$ is a quotient of $(M, -)$ for some $M$. Thus
  there is a short exact sequence of functors
  $ 0 -> F' -> (M, -) -> F -> 0. $
  Since $F$ is projective, this sequence splits and
  $(M, -) tilde.equiv F plus.o F'$. So there is an idempotent natural
  transformation from $(M, -)$ to itself whose image is $F$. But by Yoneda's
  Lemma, all natural transformations from $(M, -)$ to itself come from
  endomorphisms of $M$, and so $F tilde.equiv (M', -)$ for some direct summand
  $M'$ of $M$. This completes the determination of the finitely generated
  projectives in $bold("Fun")(Lambda)$.

  Now if $M$ is indecomposable, every proper subfunctor $F$ of $(M, -)$ is
  contained in $Rad(M, -)$, since if a split monomorphism $f : M -> M'$ with
  splitting $f' : M' -> M$ (so that $f' compose f = id_M$) is in $F(M')$, then
  given any map $f'' : M -> N$ we have
  $ f'' = f'' compose f' compose f = F(f'' compose f')(f) in F(N). $

  Now if $S$ is a simple functor, then choose an indecomposable module $M$ with
  $S(M) != 0$. By Yoneda's Lemma, there is a non-zero natural transformation
  from $(M, -)$ to $S$. Since $S$ is simple, this natural transformation is an
  epimorphism. The kernel is a proper subfunctor of $(M, -)$, and is hence
  contained in the radical. Since $S$ is simple, the kernel is equal to the
  radical.
]
