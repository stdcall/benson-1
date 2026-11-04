#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-01-quivers.typ": four-subspace-quiver

== Representations of quivers <sec:quivers>

It follows from Morita theory (Section~@sec:morita) that to study the
representations of a finite dimensional algebra over an algebraically closed
field, it suffices to consider the case where every irreducible module is one
dimensional. We shall see that such an algebra is expressible as a quotient of
the path algebra of a quiver (directed graph) by an ideal contained in the ideal
of paths of length at least two. More generally, a finite dimensional basic
algebra over any field can be expressed essentially uniquely as a quotient of a
"modulated quiver" by such an ideal, provided certain sequences of bimodules
over division rings split (this condition is always satisfied over a perfect
field). This makes the representations of quivers important to the study of
representations of finite dimensional algebras.

#definition[
  A *quiver*#idx("quiver") is a directed graph, possibly with multiple arrows
  and loops.
] <def:quiver>

If $Q$ is a quiver and $k$ is a field, we define the *path algebra*#idx(
  "path algebra",
)#idx("algebra", "path") $k Q$ as follows. It is an algebra over $k$, which as a
vector space has a basis consisting of the *paths*
$bullet -> bullet -> dots.c -> bullet$ in $Q$. Multiplication is given on basis
elements by composition of paths _in reverse order_ (because we are dealing with
left rather than right modules) if the paths are composable in this way, and
zero otherwise. Thus for example corresponding to each vertex $x$ there is a
path of length zero giving rise to an idempotent basis element denoted $e_x$. A
free algebra is an example of a path algebra, for a graph with only one vertex.
Clearly $k Q$ is finitely generated if and only if $Q$ has only finitely many
vertices and arrows, and finite dimensional if and only if in addition it has no
oriented cycles.

A *representation*#idx("representation", "of a quiver")#idx(
  "quiver",
  "representation of",
) of a quiver $Q$ associates to each vertex $x$ of $Q$ a vector space $V_x$, and
to each arrow $x -> y$ a linear transformation $V_x -> V_y$ between the
corresponding vector spaces.

There is a natural one–one correspondence between representations of $Q$ and
$k Q$-modules given as follows. Given a representation of $Q$, we form a
$k Q$-module whose underlying vector space is $plus.o.big_x V_x$, and where the
action of a basis element $x_1 -> dots.c -> x_2$ is as the composite of the
corresponding maps:
$
  plus.o.big_x V_x ->> V_(x_1) -> dots.c -> V_(x_2) arrow.r.hook
  plus.o.big_x V_x.
$
#source(112)So for example the action of the idempotent $e_x$ is to project onto
$V_x$.

Conversely, given a $k Q$-module $V$, we form a representation of $Q$ by setting
$V_x = e_x V$. If $u$ is the basis element of $k Q$ corresponding to an arrow
$x -> y$, then $e_y u = u = u e_x$, and so $u$ maps $V_x$ to $V_y$. These are
the maps we use to define the representation of $Q$. It is clear that the above
procedures are mutually inverse.

There is a simple $k Q$-module $S_x$ of dimension one corresponding to each
vertex $x$ of $Q$. It consists of a one dimensional vector space at the vertex
$x$, and a zero dimensional vector space at each other vertex. In case $k Q$ is
finite dimensional, these are the only simple $k Q$-modules, but otherwise there
are others. For example, for a free algebra with at least two generators, there
are simple modules of every dimension.

#example[
  Let $Q$ be the following quiver.
  $ #four-subspace-quiver $
  If any of the maps corresponding to the four arrows is not injective, then the
  kernel splits off as a direct summand. Thus apart from four simple modules,
  the indecomposable $k Q$-modules are in one–one correspondence with
  indecomposable *four subspace systems*;#idx(
    "indecomposable",
    "four subspace system",
  ) namely a vector space $V$ together with four given subspaces $V_1$, $V_2$,
  $V_3$, $V_4$. There is an obvious notion of direct sum for such systems,
  namely $V plus.o W$; $V_1 plus.o W_1, dots, V_4 plus.o W_4$. The *four
  subspace problem*#idx("four", "subspace problem") is the problem of
  classifying the _indecomposable_ four subspace systems. This problem was
  solved in 1970 by Gel'fand and Ponomarev [@bib:Gelfand1972]. It turns out that
  for at most three subspaces, there are only finitely many isomorphism types of
  indecomposable system. For four subspaces, there are infinitely many, but they
  are classifiable (this situation is called *tame*#idx(
    "representation",
    "type",
    "tame",
  )#idx("tame", "representation type")), while for at least five they are in
  some sense unclassifiable (*wild*#idx("representation", "type", "wild")#idx(
    "wild representation type",
  )). We shall discuss all this in more detail later.
]

The projective module $P_x = k Q . e_x$ corresponding to an idempotent $e_x$ may
be described as follows. The basis elements correspond to the paths in $Q$ which
begin with the vertex $x$, and the action of $k Q$ is given by (reverse)
composition of paths as before. We now show that these are essentially the only
projective modules, and that every submodule of a projective module is
projective.

#definition[
  A ring $Lambda$ is (left) *hereditary*#idx("hereditary ring")#idx(
    "ring",
    "hereditary",
  ) if every submodule of a projective (left) $Lambda$-module is projective.
] <def:hereditary>

Thus for example the ring of integers in an algebraic number field is
hereditary, and the next theorem shows that the path algebra of a quiver with
finitely many vertices is hereditary.

#source(113)

#definition[
  We write $k Q_((n))$ for the linear span in $k Q$ of the paths of length at
  least $n$. It is a two sided ideal in $k Q$.
] <def:path-length-ideal>

As a (left) $k Q$-module, $k Q_((n)) slash k Q_((n+1))$ is semisimple#idx(
  "semisimple",
  "module",
). It is a direct sum of simple modules of the form $S_x$, and the copies of a
particular $S_x$ correspond to the paths of length $n$ ending at $x$. That is,
$e_x . k Q_((n)) slash k Q_((n+1))$ has a basis consisting of the paths of
length $n$ ending at $x$. For example, if $k Q$ is finite dimensional then
$k Q_((n)) = J^n (k Q)$.

Now a path of length $m$, $x -> dots.c -> y$, induces an injective map
$ e_x . k Q_((n)) slash k Q_((n+1)) -> e_y . k Q_((n+m)) slash k Q_((n+m+1)) $
and the images of these maps for distinct paths are linearly independent.

If $F$ is any free $k Q$-module (not necessarily finitely generated) with a
chosen basis, then it inherits a filtration $F_((n))$ from the above filtration
on $k Q$. Again if $x -> dots.c -> y$ is a path of length $m$ then the induced
map
$ e_x . F_((n)) slash F_((n+1)) -> e_y . F_((n+m)) slash F_((n+m+1)) $
is injective, and the images of these maps for distinct paths are linearly
independent.

#theorem[
  Suppose $Q$ has only finitely many vertices. Then every submodule of a free
  $k Q$-module is isomorphic to a direct sum of modules of the form $k Q . e_x$,
  so that $k Q$ is a hereditary algebra. The Krull–Schmidt theorem holds for
  finitely generated projective $k Q$-modules.
] <th:path-algebra-hereditary>

#proof[
  We shall only prove the first statement in case $k Q$ is finite dimensional.
  The general case may be found in Bergman [@bib:Bergman1974, Cor. 2.6], and is
  quite hard.

  Suppose $P$ is a submodule of a free $k Q$-module $F$. Define $F_((n))$ as
  above, and $P_((n)) = P inter F_((n))$. Since $inter.big_n F_((n)) = {0}$ we
  have $inter.big_n P_((n)) = {0}$. As above, if $x -> dots.c -> y$ is a path of
  length $m$ then the induced map
  $e_x . P_((n)) slash P_((n+1)) -> e_y . P_((n+m)) slash P_((n+m+1))$ is
  injective.

  Since $k Q$ is finite dimensional, we have $k Q_((1)) = J(k Q)$. Now
  $P slash k Q_((1)) . P$ is a module for $k Q slash k Q_((1))$, which is a
  finite direct sum of copies of $k$. Thus we may write $P slash k Q_((1)) . P$
  as a direct sum of modules isomorphic to some $S_x$, say
  $ P slash k Q_((1)) . P = plus.o.big_(x, alpha) S_(x, alpha) $
  with $S_(x, alpha) tilde.equiv S_x$. Letting
  $P_(x, alpha) tilde.equiv k Q . e_x$ be the corresponding projective
  $k Q$-module, we have a surjective $k Q$-module homomorphism
  $ phi.alt : plus.o.big_(x, alpha) P_(x, alpha) -> P slash k Q_((1)) . P $
  which may be lifted to a $k Q$-module homomorphism
  $ psi : plus.o.big_(x, alpha) P_(x, alpha) -> P. $

  #source(114)We claim that $psi$ is an isomorphism. The injectivity of $psi$
  follows from the injectivity of
  $e_x . P_((n)) slash P_((n+1)) -> e_y . P_((n+m)) slash P_((n+m+1))$ above.
  Write $X$ for $Coker(psi)$. Tensoring the short exact sequence
  $ 0 -> plus.o.big_(x, alpha) P_(x, alpha) limits(->)^psi P -> X -> 0 $
  over $k Q$ with $k Q slash k Q_((1))$, we obtain
  $
    plus.o.big_(x, alpha) S_(x, alpha) -> P slash k Q_((1)) . P
    -> X slash k Q_((1)) . X -> 0
  $
  so that $X slash J(k Q) . X = X slash k Q_((1)) . X = 0$, and hence by
  Nakayama's lemma $X = 0$, so that $psi$ is an isomorphism.

  To prove the Krull–Schmidt theorem for finitely generated projective
  $k Q$-modules, we note that
  $
    k Q slash k Q_((1)) times.o_(k Q) plus.o.big_(x, alpha) P_(x, alpha)
    = plus.o.big_(x, alpha) S_(x, alpha)
  $
  with $S_(x, alpha) tilde.equiv S_x$. Thus if the module is finitely generated,
  the number of copies of each $P_(x, alpha)$ is finite, and hence well defined
  by applying the Krull–Schmidt theorem for finitely generated
  $k Q slash k Q_((1))$-modules.
]

#corollary(closed: true)[
  Every projective module over a free algebra (over a field) is free.
] <cor:free-algebra-projective>

#example[
  The following is an example where $Q$ has infinitely many vertices, so that
  $k Q$ is a ring without identity. Let $Q$ be the quiver
  $ dots.c -> bullet -> bullet -> bullet $
  Then a representation $V$ of $Q$ is the same thing as an inverse system of
  vector spaces $dots.c -> V_2 -> V_1 -> V_0$. A $k Q$-module is projective if
  and only if every map involved is injective, and the inverse limit is zero.
  Thus every submodule of a projective $k Q$-module is projective, and so $k Q$
  is hereditary.

  Let $bold(k)$ denote the representation $dots.c -> k -> k -> k$ of $Q$ in
  which each arrow is the identity map. Then giving a homomorphism
  $bold(k) -> V$ is the same thing as choosing an element $v_i$ in each $V_i$ in
  such a way that $v_i$ goes to $v_(i-1)$ in $V_(i-1)$. Thus
  $Hom_(k Q)(bold(k), V) = invlim V_i$. Since every submodule of a projective
  module is projective, every module has a projective resolution of length one,
  and so $Ext^n_(k Q)(bold(k), V) = 0$ for $n > 1$. The functor
  $Ext^1_(k Q)(bold(k), V)$ is usually written $attach(invlim, tr: 1) V_i$#idx(
    "$attach(limits(lim), b: arrow.l, tr: 1)$",
  ) or $R^1 invlim V_i$, since it is the first (and only) right derived
  functor#idx("derived functors")#idx("functor", "right derived")#idx(
    "right",
    "derived functors",
  ) of $invlim$. By Proposition~@prop:long-exact-sequences, given a short exact
  sequence $0 -> V' -> V -> V'' -> 0$ of $k Q$-modules, there is a six term
  exact sequence
  $
    0 -> invlim V'_i -> invlim V_i -> invlim V''_i
    -> attach(invlim, tr: 1) V'_i -> attach(invlim, tr: 1) V_i
    -> attach(invlim, tr: 1) V''_i -> 0.
  $
  Of course, the above discussion applies equally well when the field $k$ is
  replaced by $ZZ$, because a subgroup of a free abelian group is again free
  abelian. Thus we have a functor $attach(invlim, tr: 1)$ for inverse systems of
  abelian groups, and a six #source(115)term sequence as before. For further
  discussion of $attach(invlim, tr: 1)$, see Milnor [@bib:Milnor1962] and
  Bousfield–Kan [@bib:Bousfield1972], Sections IX.2 and XI.6.
]

#definition[
  Suppose $Lambda$ is a finite dimensional algebra over an algebraically closed
  field $k$. Let $S_1, dots, S_r$ be the isomorphism classes of simple
  $Lambda$-modules with projective covers $P_i = Lambda e_i$. The
  *Ext-quiver*#idx("Ext", "-quiver")#idx("quiver", "Ext-") $Q(Lambda)$ has
  vertices $x_1, dots, x_r$ corresponding to these simple modules, and the
  number of arrows from $x_i$ to $x_j$ is $dim_k Ext^1_Lambda (S_i, S_j)$. Note
  that according to the remarks in Section~@sec:ext-tor, this is the same as the
  dimension of
  $
    Hom_Lambda (P_j, Rad(P_i)) slash Hom_Lambda (P_j, Rad^2(P_i))
    = e_j J(Lambda) e_i slash e_j J^2(Lambda) e_i.
  $
] <def:ext-quiver>

#proposition(title: [Gabriel [@bib:Gabriel1980]])[
  Suppose $Lambda$ is a finite dimensional basic algebra over an algebraically
  closed field $k$, and let $Q = Q(Lambda)$ be its Ext-quiver. Then there is a
  surjective map of algebras $phi.alt : k Q ->> Lambda$ such that the kernel of
  $phi.alt$ is contained in the ideal of paths of length at least two. In
  particular, in case $k Q$ is finite dimensional, this latter ideal is equal to
  the square of the radical, and $phi.alt$ induces a bijection between the
  simple $Lambda$-modules and the simple $k Q$-modules, and between the blocks
  of $Lambda$ and the blocks of $k Q$.
] <prop:gabriel-quiver>
#idx("Gabriel's theorem", target: [@prop:gabriel-quiver])#idx(
  "theorem",
  "Gabriel's",
  target: [@prop:gabriel-quiver],
)

#proof[
  Since $Lambda$ is a basic algebra, we can choose the $e_i$ with
  $e_1 + dots.c + e_r = 1$ and $e_i e_j = e_j e_i = 0$, and send the idempotent
  corresponding to $x_i$ in $k Q$ to the idempotent $e_i$ in $Lambda$. Choose a
  complement to $e_j J^2(Lambda) e_i$ in $e_j J(Lambda) e_i$ as a vector space,
  and choose a basis for it. Send the basis elements of $k Q$ corresponding to
  the arrows from $x_i$ to $x_j$ to these basis elements. Every relation in
  $k Q$ says that products of non-composable paths are zero. These relations are
  satisfied by the corresponding products in $Lambda$ by the relations
  $e_i e_j = e_j e_i = 0$, and so this map extends to a well defined map
  $k Q -> Lambda$. It is surjective modulo $J^2(Lambda)$, and so by
  Proposition~@prop:surjective-mod-radical-square it is surjective. In case
  $k Q$ is finite dimensional, the bijection of blocks comes from
  Proposition~@prop:central-idempotents-lift.
]

#definition[
  A *system of linear relations*#idx("system", "of linear relations")#idx(
    "linear relation",
    "on a quiver",
  ) on a quiver $Q$ is a two sided ideal $I$ contained in the ideal of paths of
  length at least two. This is the same as assigning to each pair of vertices
  $x$ and $y$ in $Q$ a subspace of the space of paths of length at least two
  from $x$ to $y$, called the *relations*#idx("relations"), in such a way that
  composing a relation on either side with any path gives another relation.

  We call the pair $(Q, I)$ a *quiver with relations*#idx(
    "quiver",
    "with relations",
  )#idx("relations", "quiver with"). The *path algebra*#idx("path algebra") of a
  quiver with relations is the algebra $k Q slash I$.
] <def:linear-relations>

The importance of the above definition is that by the proposition, every basic
algebra over an algebraically closed field is isomorphic to the path algebra of
a quiver with relations.

#example[
  Let $Q$ be the quiver
  $ dots.c -> bullet -> bullet -> bullet -> dots.c $
  #source(116)and let $I$ be the ideal generated by the paths of length at least
  two. Then a $k Q slash I$-module is the same thing as a chain complex of
  vector spaces. The projective $k Q slash I$-modules are the exact complexes.

  More generally, for any ring $Lambda$, one may form the path algebra
  $Lambda Q$ in the obvious way, and a $Lambda Q slash I$-module is the same as
  a chain complex of $Lambda$-modules. The projective $Lambda Q slash I$-modules
  are the split exact sequences of projective $Lambda$-modules.
]

We now indicate what modifications have to be made to the above discussion in
case $k$ is not algebraically closed. We confidently leave the details to the
reader.

#definition[
  A *labelled graph*#idx("labelled graph")#idx("graph", "labelled") is an
  undirected graph together with a pair of positive integers
  $(attach(d, bl: x, tr: gamma, br: y), attach(d, bl: y, tr: gamma, br: x))$
  for each edge $x limits(class("relation", dash.em))^gamma y$. We usually omit
  to write in the label in case
  $attach(d, bl: x, tr: gamma, br: y) = attach(d, bl: y, tr: gamma, br: x) = 1$.
  An *orientation*#idx("orientation") of a labelled graph assigns a direction
  $x -> y$ or $x <- y$ to each edge $x class("relation", dash.em) y$.

  A *valued graph*#idx("valued graph")#idx("graph", "valued") is a labelled
  graph with the property that there exist positive integers $f_x$, one for each
  vertex, with $attach(d, bl: x, tr: gamma, br: y) f_y
  = attach(d, bl: y, tr: gamma, br: x) f_x$ for each edge
  $x limits(class("relation", dash.em))^gamma y$. Thus for example a labelled
  graph with no cycles is always a valued graph.

  A *modulation*#idx("modulation") of a valued graph consists of an assignment
  of a division ring $Delta_x$ to each vertex $x$, and a
  $Delta_x$–$Delta_y$-bimodule $lmodule(x, M)_y^gamma$ to each edge
  $x limits(class("relation", dash.em))^gamma y$ satisfying
  + $lmodule(y, M)_x^gamma tilde.equiv
    Hom_(Delta_x)(lmodule(x, M)_y^gamma, Delta_x) tilde.equiv
    Hom_(Delta_y)(lmodule(x, M)_y^gamma, Delta_y)$
  + $dim_(Delta_y)(lmodule(x, M)_y^gamma) = attach(d, bl: x, tr: gamma, br: y)$.

  Finally, a *modulated quiver*#idx("modulated quiver")#idx(
    "quiver",
    "modulated",
  ) consists of a valued graph together with an orientation and a modulation.
] <def:labelled-graph>

If $Lambda$ is a finite dimensional algebra over a field $k$, which is not
necessarily algebraically closed, its Ext-quiver is defined as a modulated
quiver as follows. Again the vertices $x_i$ correspond to the isomorphism
classes of simple modules $S_i$, with $Delta_i = End_Lambda (S_i)^op$. There is
an arrow $x_i limits(->)^gamma x_j$ if and only if
$Ext^1_Lambda (S_i, S_j) != 0$, and
$
  #aligned-rows(
    (
      $lmodule(j, M)_i^gamma$,
      $= M_(i j) = Ext^1_Lambda (S_i, S_j) quad
      #[as a $Delta_j$-$Delta_i$-bimodule,]$,
    ),
    (
      $lmodule(i, M)_j^gamma$,
      $= M'_(i j) = Hom_k (lmodule(j, M)_i^gamma, k)
      tilde.equiv Hom_(Delta_i)(lmodule(j, M)_i^gamma, Delta_i)
      tilde.equiv Hom_(Delta_j)(lmodule(j, M)_i^gamma, Delta_j)$,
    ),
    (
      $attach(d, bl: j, tr: gamma, br: i)$,
      $= d_(i j) = dim_(Delta_i)(lmodule(j, M)_i^gamma)$,
    ),
    (
      $attach(d, bl: i, tr: gamma, br: j)$,
      $= d'_(i j) = dim_(Delta_j)(lmodule(i, M)_j^gamma) quad "and" quad
      f_i = dim_k (Delta_i).$,
    ),
  )
$
Note that if $Ext^1_Lambda (S_i, S_j) != 0$ and $Ext^1_Lambda (S_j, S_i) != 0$
then there are two distinct arrows $x_i limits(->)^gamma x_j$ and
$x_j limits(->)^(gamma') x_i$ with separate bimodules.

A *representation* $V$ of a modulated quiver assigns to each vertex $x$ a
$Delta_x$-module $V_x$ and to each arrow $x limits(->)^gamma y$ a homomorphism
$ lmodule(y, M)_x^gamma times.o_(Delta_x) V_x -> V_y. $

#source(117)Just as before, representations of a modulated quiver $Q$ are in
natural one–one correspondence with modules for the *path algebra* $k Q$. We
give a more abstract definition of this path algebra than in the unmodulated
case, but it amounts to the same thing. Namely we set
$Delta = plus.o.big_x Delta_x$,
$M = plus.o.big_(x limits(->)^gamma y) lmodule(x, M)_y^gamma$ as a
$Delta$–$Delta$-bimodule, and then we define the space
$k Q_((n)) slash k Q_((n+1))$ of paths of length $n$ to be the $n$-fold tensor
product $M times.o_Delta M times.o_Delta dots.c times.o_Delta M$ (and
$k Q_((0)) slash k Q_((1)) = Delta$). Then the path algebra $k Q$ is the direct
sum of the $k Q_((n)) slash k Q_((n+1))$ as a tensor algebra.

Imitating the proof of Proposition~@prop:gabriel-quiver, we find that there are
two possible obstructions, both of which disappear over a perfect field.

#proposition(closed: true)[
  Suppose that $Lambda$ is a finite dimensional basic algebra over a field $k$.
  Suppose that
  + the map of algebras $Lambda -> Lambda slash J(Lambda)$ splits, so that we
    may choose a copy of $Delta_i$ in $End_Lambda (P_i)$ complementary to
    $J End_Lambda (P_i)$, and
  + the short exact sequence
    $
      0 -> e_i J^2(Lambda) e_j -> e_i J(Lambda) e_j
      -> e_i J(Lambda) slash J^2(Lambda) e_j -> 0
    $
    splits as a sequence of $Delta_j$–$Delta_i$-bimodules.

  Then $Lambda$ is a quotient of the path algebra of its Ext-quiver by an ideal
  contained in the ideal of paths of length at least two.
] <prop:modulated-quotient>

#corollary[
  Suppose that $Lambda$ is a finite dimensional basic algebra over a perfect
  field $k$. Then $Lambda$ is a quotient of the path algebra of its Ext-quiver
  by an ideal contained in the ideal of paths of length at least two.
] <cor:perfect-field-quotient>

#proof[
  Over a perfect field, there are no inseparable extensions, and so
  $Delta_i times.o Delta_j^op$ is semisimple. Thus every exact sequence of
  $Delta_i$–$Delta_j$-bimodules splits. In particular the sequence
  $
    0 -> J(Lambda) slash J^2(Lambda) -> Lambda slash J^2(Lambda)
    -> Lambda slash J(Lambda) -> 0
  $
  of $Lambda slash J(Lambda)$-$Lambda slash J(Lambda)$-bimodules splits and so
  the $Delta_i$'s lift to $Lambda slash J^2(Lambda)$. Continuing inductively,
  the map $Lambda -> Lambda slash J(Lambda)$ splits, and so we may apply the
  proposition.
]

#remark(kind: "Remarks")[
  + There should be a way of modifying the definition of the Ext-quiver of
    $Lambda$ to contain sufficient cocycle information so that a suitable "path
    algebra" will always map onto $Lambda$. To the best of my knowledge no-one
    has attempted to do this.
  + Let $k_0$ be a field of characteristic $p$. Over the field $k = k_0(x)$,
    which is not perfect, let $Lambda$ be the commutative algebra
    $k[y, epsilon] slash (epsilon^p, y^p - x - epsilon)$ of dimension $p^2$.
    Then $Lambda slash J(Lambda) = k_0(y)$ is an inseparable extension of $k$ of
    degree $p$, and the map $Lambda -> Lambda slash J(Lambda)$ does not split as
    a map of algebras over $k$. This example shows that the above corollary does
    not extend to non-perfect fields.
  + Since the group algebra of a finite group over the field of $p$ elements has
    a finite splitting field, the above corollary is true for a block of such a
    group algebra over any field.
]
