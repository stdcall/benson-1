#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-01-categories-functors.typ": naturality-square

== Categories and functors <sec:categories-functors>

We shall assume that the reader is familiar with the elementary notions of
*category*#idx("category") and *functor*#idx("functor") (covariant#idx(
  "covariant functor",
)#idx("functor", "covariant") and contravariant#idx(
  "contravariant functor",
)#idx("functor", "contravariant")) as explained in Mac~Lane [@bib:MacLane1974,
Sections 1.7 and 1.8].

#definition[
  If $F, F': cal(C) -> cal(D)$ are covariant functors, a *natural
  transformation*#idx("natural", "transformation")#idx(
    "transformation",
    "natural",
  ) $phi.alt: F arrow.r.squiggly F'$#idx("$arrow.r.squiggly$") assigns to each
  object $X in cal(C)$ a map $phi.alt_X: F(X) -> F'(X)$ in such a way that the
  square
  $
    #naturality-square
  $
  commutes for each morphism $alpha: X -> Y$ in $cal(C)$. Similarly if $F$ and
  $F'$ are contravariant, we make the same definition, but with the vertical
  arrows in the above diagram reversed. We write $Nat(F, F')$ for the set of
  natural transformations from $F$ to $F'$. A natural transformation
  $phi.alt: F arrow.r.squiggly F'$ is a *natural isomorphism*#idx(
    "natural",
    "isomorphism",
  )#idx("isomorphism", "natural") if $phi.alt_X$ is an isomorphism for each
  $X in cal(C)$.

  An *equivalence of categories*#idx("equivalence", "of categories") is a pair
  of functors $F: cal(C) -> cal(D)$ and $F': cal(D) -> cal(C)$ such that
  $F compose F'$ and $F' compose F$ are naturally isomorphic to the appropriate
  identity functors.
] <def:natural-transformation>

The following are examples of categories we shall be interested in during the
course of this book:
+ The category $bold("Grp")$#idx("$bold(\"Grp\")$") of groups and homomorphisms.
+ The categories $lmodule(Lambda, bold("Mod"))$ of left $Lambda$-modules and
  $lmodule(Lambda, bold("mod"))$#idx(
    "$lmodule(Lambda, bold(\"Mod\"))$, $lmodule(Lambda, bold(\"mod\"))$",
  ) of finitely generated left $Lambda$-modules, for a ring $Lambda$.
+ The categories $bold("Set")$#idx("$bold(\"Set\")$") of sets, $bold("Ab")$#idx(
    "$bold(\"Ab\")$",
  ) of abelian groups and $lmodule(k, bold("Vec"))$#idx(
    "$lmodule(k, bold(\"Vec\"))$",
  ) of $k$-vector spaces.
+ The category of functors from $lmodule(Lambda, bold("mod"))$ to $bold("Ab")$,
  or from $lmodule(Lambda, bold("mod"))$ to $lmodule(k, bold("Vec"))$ if
  $Lambda$ is a $k$-algebra. In this category the morphisms are the natural
  transformations.
+ The category of topological spaces and (continuous) maps.
+ The category of CW-complexes#idx("CW-complex") and homotopy classes of maps.
+ The category of chain complexes and chain maps.

#source(34)The correct setting for doing homological algebra is an *abelian
category*. A typical example of an abelian category is a category of modules for
a ring.

#definition[
  An *abelian category*#idx("abelian", "category")#idx("category", "abelian") is
  a category with the following extra structure.
  + For each pair of objects $A$ and $B$ the set of maps $Hom(A, B)$ is given
    the structure of an abelian group.
  + There is a *zero object*#idx("zero object")#idx("object, zero") $0$ with the
    property that $Hom(A, 0)$ and $Hom(0, A)$ are the trivial group for all
    objects $A$.
  + Composition of maps is a bilinear map
    $ Hom(B, C) times Hom(A, B) -> Hom(A, C). $
  + Finite direct sums exist (with the usual universal definition).
  + Every morphism $phi.alt: A -> B$ has a *kernel*#idx("kernel"), namely a map
    $sigma: K -> A$ such that $phi.alt compose sigma = 0$, and such that
    whenever $sigma': K' -> A$ with $phi.alt compose sigma' = 0$ there is a
    unique map $lambda: K' -> K$ with $sigma' = sigma compose lambda$.
  + Every morphism has a *cokernel*#idx("cokernel") (definition dual to that of
    kernel).
  + Every *monomorphism*#idx("monomorphism") (map with zero kernel) is the
    kernel of its cokernel.
  + Every *epimorphism*#idx("epimorphism") (map with zero cokernel) is the
    cokernel of its kernel.
  + Every morphism is the composite of a monomorphism and an epimorphism.

  An *additive functor*#idx("additive", "functor")#idx("functor", "additive")
  $F$ from one abelian category to another is one which induces a homomorphism
  of abelian groups
  $ Hom(A, B) -> Hom(F(A), F(B)) $
  for each pair $A$ and $B$.
] <def:abelian-category>

Freyd [@bib:Freyd1964] has shown that given any _small_ abelian category
$cal(A)$ (i.e., one where the class of objects is small enough to be a set)
there is a _full exact_ embedding#idx("full exact embedding")#idx(
  "embedding",
  "full exact",
) $F: cal(A) -> lmodule(Lambda, bold("Mod"))$ for a suitable ring $Lambda$.
Here, _full_ means that for $X, Y in cal(A)$, every map in
$lmodule(Lambda, bold("Mod"))$ from $F(X)$ to $F(Y)$ is in the image of $F$.
_Exact_ means that $F$ takes exact sequences to exact sequences. This has the
effect that diagram chasing may be performed in an abelian category as though
the objects had elements. Since we shall only be working with categories where
this is obviously true, we shall write our proofs this way. It is a simple
matter and a worthless exercise to translate such a proof into a proof using
only the axioms.

Thus you should not memorise the definition of an abelian category, but rather
remember the Freyd category embedding theorem#idx(
  "Freyd category embedding theorem",
), and look up the definitions whenever you need them.

Often in representation theory, it is more convenient to work not in a module
category but in a *stable module category*#idx("stable", "module category")#idx(
  "category",
  "stable module",
). We write $lmodule(Lambda, underline(bold("mod")))$#idx(
  "$lmodule(Lambda, underline(bold(\"mod\")))$",
) for the category of finitely generated $Lambda$-modules modulo projectives.
Namely, the #source(35)objects of $lmodule(Lambda, underline(bold("mod")))$ are
the same as those of $lmodule(Lambda, bold("mod"))$, but two maps in
$lmodule(Lambda, bold("mod"))$ are regarded as the same in
$lmodule(Lambda, underline(bold("mod")))$ if their difference factors through a
projective module. Thus for example the projective modules are isomorphic to the
zero object in $lmodule(Lambda, underline(bold("mod")))$. We write
$underline(Hom)_Lambda (M, N)$ and $underline(End)_Lambda (M)$ for the hom sets
in $lmodule(Lambda, underline(bold("mod")))$, namely homomorphisms modulo those
factoring through a projective module.

If the Krull–Schmidt theorem holds in $lmodule(Lambda, bold("mod"))$ then the
indecomposable objects in $lmodule(Lambda, underline(bold("mod")))$ correspond
to the non-projective indecomposable objects in $lmodule(Lambda, bold("mod"))$.

Recall from Section~@sec:projective-injective that if $M$ is a $Lambda$-module
then $tilde(Omega)(M)$ is defined to be the kernel of some epimorphism $P -> M$
with $P$ projective. Schanuel's lemma can be interpreted as saying that while
$tilde(Omega)$ is not a functor on $lmodule(Lambda, bold("mod"))$, it passes
down to a well defined functor
$
  Omega: lmodule(Lambda, underline(bold("mod")))
  -> lmodule(Lambda, underline(bold("mod"))).
$

Similarly we write $lmodule(Lambda, overline(bold("mod")))$#idx(
  "$lmodule(Lambda, overline(bold(\"mod\")))$",
) for the category of finitely generated $Lambda$-modules modulo injectives, and
$overline(Hom)_Lambda (M, N)$ and $overline(End)_Lambda (M)$ for the hom sets in
$lmodule(Lambda, overline(bold("mod")))$. The functor $tilde(Omega)^(-1)$ passes
down to a well defined functor
$
  Omega^(-1): lmodule(Lambda, overline(bold("mod")))
  -> lmodule(Lambda, overline(bold("mod"))).
$

If $Lambda$ is self injective, so that finitely generated projective and
injective modules coincide, then $lmodule(Lambda, underline(bold("mod")))
= lmodule(Lambda, overline(bold("mod")))$ and the functors $Omega$ and
$Omega^(-1)$ are inverse to each other.

#subhead[Representable functors]

#definition[
  A covariant functor $F: cal(C) -> bold("Set")$ is said to be
  *representable*#idx("representable functor")#idx("functor", "representable")
  if it is naturally isomorphic to a functor of the form
  $ (X, -): Y -> Hom(X, Y). $
  A contravariant functor is representable if it is naturally isomorphic to a
  functor of the form
  $ (-, Y): X -> Hom(X, Y). $

  If Hom sets in $cal(C)$ have natural structures as abelian groups or vector
  spaces, then we have the same definition of representability of functors
  $F: cal(C) -> bold("Ab")$ or $F: cal(C) -> lmodule(k, bold("Vec"))$.
] <def:representable-functor>

One of the most useful elementary lemmas from category theory is Yoneda's lemma,
which says that natural transformations from representable functors are
representable.

#lemma(title: [Yoneda])[
  + If $F: cal(C) -> bold("Set")$ is a covariant functor and $(X, -)$ is a
    representable functor then the set of natural transformations from $(X, -)$
    to $F$ is in natural bijection with $F(X)$ via the map
    $
                            Nat((X, -), F) & stretch(-->)^tilde.equiv F(X) \
      (phi.alt: (X, -) arrow.r.squiggly F) & |-> phi.alt_X (id_X).
    $
  + #source(36)If $F: cal(C) -> bold("Set")$ is a contravariant functor and
    $(-, X)$ is a representable functor then the set of natural transformations
    from $(-, X)$ to $F$ is in natural bijection with $F(X)$ via the map
    $
                            Nat((-, X), F) & stretch(-->)^tilde.equiv F(X) \
      (phi.alt: (-, X) arrow.r.squiggly F) & |-> phi.alt_X (id_X).
    $
] <lem:yoneda>
#idx("lemma", "Yoneda's", target: [@lem:yoneda])#idx(
  "Yoneda",
  "lemma",
  target: [@lem:yoneda],
)

#proof[
  + It is easy to check that the map
    $
           F(X) & -> Nat((X, -), F) \
      x in F(X) & |-> \( phi.alt: (X, -) arrow.r.squiggly F \
                & quad quad phi.alt_Y (alpha: X -> Y) = F(alpha)(x) in F(Y) \)
    $
    is inverse to the given map. The proof of (ii) is similar.
]

#subhead[Adjoint functors]

#definition[
  An *adjunction*#idx("adjunction") between functors $F: cal(C) -> cal(D)$ and
  $G: cal(D) -> cal(C)$ consists of bijections
  $ Hom(F X, Y) -> Hom(X, G Y) $
  natural in each variable $X in cal(C)$ and $Y in cal(D)$. We say that $F$ is
  the *left adjoint*#idx("left", "adjoint")#idx("adjoint", "left")#idx(
    "adjoint",
    "functor",
  )#idx("functor", "adjoint") and $G$ is the *right adjoint*#idx(
    "right",
    "adjoint",
  )#idx("adjoint", "right").
] <def:adjunction>

It is not hard to see that if a functor has a right (or left) adjoint, then it
is unique up to natural isomorphism. Examples of adjunctions abound. The most
familiar example is probably the adjunction
$ Hom(X times Y, Z) tilde.equiv Hom(Y, Hom(X, Z)) $
between the functors $X times -$ and $Hom(X, -)$ on $bold("Set")$. Similarly in
$lmodule(k, bold("Vec"))$ we have
$ Hom(U times.o V, W) tilde.equiv Hom(V, Hom(U, W)). $
Another class of examples is given by free objects. For example if
$F: bold("Set") -> bold("Grp")$ takes a set to the free group with that set as
basis, then $F$ is left adjoint to the forgetful functor
$G: bold("Grp") -> bold("Set")$ which assigns to each group its underlying set
of elements.

#lemma[
  Suppose that $cal(C)$ and $cal(D)$ are abelian categories and
  $F: cal(C) -> cal(D)$ has a right adjoint $G: cal(D) -> cal(C)$. Then $F$
  takes epimorphisms to epimorphisms and $G$ takes monomorphisms to
  monomorphisms.
] <lem:adjoint-epi-mono>

#proof[
  A map $X -> X'$ is an epimorphism if and only if for every $Z in cal(C)$, the
  map $Hom(X', Z) -> Hom(X, Z)$ is injective. In particular
  $ Hom(X', G Y) -> Hom(X, G Y) $
  is injective so that
  $ Hom(F X', Y) -> Hom(F X, Y) $
  is injective for every $Y in cal(D)$. Thus $F X -> F X'$ is an epimorphism.
  The other statement is proved dually.
]
