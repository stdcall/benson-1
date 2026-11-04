#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/common.typ": ladder
#import "diagrams/01-05-projective-injective.typ": (
  injective-extension, minimal-projectives, projective-lifting,
  schanuel-pullback,
)

== Projective and injective modules <sec:projective-injective>

#definition[
  A module $P$ is said to be *projective*#idx("projective", "module")#idx(
    "module",
    "projective",
  ) if given modules $M$ and $M'$, a map $lambda : P -> M$ and an epimorphism
  $mu : M' -> M$ there exists a map $nu : P -> M'$ such that the following
  diagram commutes.
  $
    #projective-lifting
  $

  #source(21)A module $I$ is said to be *injective*#idx(
    "injective",
    "module",
  )#idx("module", "injective") if given two modules $M$ and $M'$, a map
  $lambda : M -> I$ and a monomorphism $M -> M'$, there is a map $nu : M' -> I$
  such that the following diagram commutes.
  $
    #injective-extension
  $
] <def:projective-injective>

#lemma[
  The following are equivalent.
  + $P$ is projective.
  + Every epimorphism $lambda : M -> P$ splits.
  + $P$ is a direct summand of a free module#idx("free", "module")#idx(
      "module",
      "free",
    ).
] <lem:projective-equivalent>

#proof[
  The proof of this lemma is left as an easy exercise for the reader.
]

Note that if $P$ is a projective left $Lambda$-module and
$ dots.c -> M_n -> M_(n-1) -> M_(n-2) -> dots.c $
is a long exact sequence of right $Lambda$-modules then the sequence
$
  dots.c -> M_n times.o_Lambda P -> M_(n-1) times.o_Lambda P
  -> M_(n-2) times.o_Lambda P -> dots.c
$
is also exact. A left module with this property is called *flat*#idx(
  "flat module",
)#idx("module", "flat"). Similarly a right $Lambda$-module with the above
property with respect to long exact sequences of left $Lambda$-modules is called
flat.

Since every module $M$ is a quotient of a free module, it is certainly a
quotient of a projective module. If $Lambda$ is Artinian, and $P_1$ and $P_2$
are minimal projective modules (with respect to direct sum decomposition)
mapping onto a finitely generated module $M$, then we have a diagram
$
  #minimal-projectives
$
If the composite map $P_1 -> P_2 -> P_1$ is not an isomorphism then by Fitting's
lemma $P_1$ has a summand mapping to zero in $M$ and so $P_1$ is not minimal.
Applying this argument both ways round, we see that $P_1 tilde.equiv P_2$. This
module is called the *projective cover*#idx("projective", "cover")#idx(
  "cover",
  "projective",
) $P_M$#idx("$P_M$") of $M$. We write $Omega(M)$#idx("$Omega(M)$") for the
kernel, so that we have a short exact sequence
$ 0 -> Omega(M) -> P_M -> M -> 0. $
Even when $Lambda$ is not Artinian, we have the following.

#lemma(title: [Schanuel])[
  Suppose that $0 -> M_1 -> P_1 -> M -> 0$ and $0 -> M_2 -> P_2 -> M -> 0$ are
  short exact sequences of modules with $P_1$ and $P_2$ projective. Then
  $M_1 plus.o P_2 tilde.equiv P_1 plus.o M_2$.
] <lem:schanuel>
#idx("Schanuel's lemma", target: [@lem:schanuel])#idx(
  "lemma",
  "Schanuel's",
  target: [@lem:schanuel],
)

#proof[
  #source(22)Let $X$ be the submodule of $P_1 plus.o P_2$ consisting of those
  elements $(x, y)$ where $x$ and $y$ have the same image in $M$ (the
  *pullback*#idx("pullback") of $P_1 -> M$ and $P_2 -> M$). Then we have a
  commutative diagram with exact rows and columns
  $
    #schanuel-pullback
  $
  The two sequences with $X$ in the middle must split since they end with a
  projective module, and so we have
  $M_1 plus.o P_2 tilde.equiv X tilde.equiv M_2 plus.o P_1$.
]

Thus if we define $tilde(Omega)(M)$#idx("$tilde(Omega)(M)$") to be the kernel of
_some_ epimorphism $P -> M$ with $P$ projective, Schanuel's lemma shows that
$tilde(Omega)(M)$ is well defined up to adding and removing projective summands.

If $alpha : M_1 -> M_2$ is a module homomorphism then we may lift as in the
following diagram
$
  #ladder(
    ($0$, $tilde(Omega)(M_1)$, $P_1$, $M_1$, $0$),
    ($0$, $tilde(Omega)(M_2)$, $P_2$, $M_2$, $0$),
    (none, [], [], [], none),
  )
$
and obtain a map $tilde(Omega)(alpha) : tilde(Omega)(M_1) -> tilde(Omega)(M_2)$
which is unique up to the addition of maps factoring through a projective
module. For a discussion of the right functorial setting for $tilde(Omega)$, see
Section~@sec:categories-functors.

The discussion of injective modules is achieved by means of a dualising
operation as follows.

#lemma[
  Every $Lambda$-module may be embedded in an injective module.
] <lem:injective-embedding>

#proof[
  If $M$ is a left $Lambda$-module, the dual abelian group
  $ M^o = Hom_ZZ (M, QQ slash ZZ) $
  is a right $Lambda$-module in the obvious way, and vice-versa. There is also
  an obvious injective map $M arrow.hook M^(o o)$. If $P$ is projective, then
  the dual $P^o$ is injective, as is easy to see by applying duality to the
  definition. Thus if $P$ is #source(23)a projective right $Lambda$-module
  mapping onto $M^o$ then $M arrow.hook M^(o o) arrow.hook P^o$ is an embedding
  of $M$ into an injective left $Lambda$-module.
]

If $M -> I$ is an embedding of $M$ into an injective module $I$ then we write
$tilde(Omega)^(-1)(M)$ for the cokernel.

Injective modules are better behaved than projective modules in the sense that
for any ring $Lambda$ and any module $M$ there is a unique minimal injective
module $I$ (with the obvious universal property) into which $M$ embeds. This is
called the *injective hull*#idx("injective", "hull")#idx("hull, injective") of
$M$. A proof of this statement, which is the Eckmann–Schöpf theorem#idx(
  "Eckmann–Schöpf theorem",
)#idx("theorem", "Eckmann–Schöpf"), may be found in Curtis and Reiner
[@bib:Curtis1962], Theorem~57.13. If $M -> I$ is the injective hull of $M$, we
write $Omega^(-1)(M)$#idx("$Omega^(-1) (M)$") for the cokernel.

#exercise[
  (Broué) Suppose that $Lambda$ is a $k$-algebra. Write $Omega_Lambda$ for the
  kernel of the multiplication map $Lambda times.o_k Lambda -> Lambda$, so that
  $Omega_Lambda$ is a $Lambda$-$Lambda$-bimodule (usually called the degree one
  differentials). Show that if $M$ is a $Lambda$-module then
  $Omega_Lambda times.o_Lambda M$ is a $Lambda$-module of the form
  $tilde(Omega)(M)$.
]
