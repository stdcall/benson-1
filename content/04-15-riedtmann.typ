#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-15-riedtmann.typ": (
  a-infinity-quiver, covering-lift, example-copies, example-tree, other-tree,
  tree-graph, tree-quiver, zb-quiver,
)

== The Riedtmann structure theorem <sec:riedtmann>

We now describe the Riedtmann structure theorem#idx(
  "Riedtmann structure theorem",
  target: [@sec:riedtmann],
)#idx("theorem", "Riedtmann structure", target: [@sec:riedtmann]), which
describes the structure of an abstract *stable representation quiver*, of which
the stable quivers described in the last section are examples. The necessary
terminology is given in the following definitions. The proof of the structure
theorem involves a variant of the classical universal cover construction.

#definition[
  A *morphism of quivers*#idx("morphism of quivers")#idx(
    "quiver",
    "morphism of",
  ) $phi.alt : Q -> Q'$ assigns to each vertex $x$ of $Q$ a vertex $phi.alt(x)$
  of $Q'$ and to each arrow $x limits(arrow.r)^gamma y$ in $Q$ an arrow
  $phi.alt(x) limits(arrow.r.long)^(phi.alt(gamma)) phi.alt(y)$ in $Q'$.

  If $x$ is a vertex in a quiver $Q$ we write $x^-$ for the set of vertices $y$
  in $Q$ such that there is an arrow $y -> x$ in $Q$, and we write $x^+$ for the
  set of vertices $y$ in $Q$ such that there is an arrow $x -> y$ in $Q$.

  #source(167)A quiver is *locally finite*#idx("locally finite quiver")#idx(
    "quiver",
    "locally finite",
  ) if the sets $x^+$ and $x^-$ are finite sets for each $x$ in $Q$. A
  *loop*#idx("loop") in $Q$ is an arrow from a vertex to itself. A *multiple
  arrow*#idx("multiple arrow") in $Q$ is a set of at least two arrows from a
  given vertex to another given vertex. To a quiver $Q$ without loops or
  multiple arrows, we associate an undirected graph $macron(Q)$ whose vertices
  are the same as the vertices of $Q$, and where two vertices $x$ and $y$ are
  joined by an edge in $macron(Q)$ if there is an arrow $x -> y$ or $y -> x$ in
  $Q$.

  A *stable representation quiver*#idx(
    "stable",
    "representation quiver",
  )#idx("representation", "quiver, stable") or *translation quiver*#idx(
    "quiver",
    "translation",
  )#idx("translation", "quiver") is a quiver $Q$ together with an automorphism
  $tau$ called the *translation*#idx("translation") such that the following
  conditions are satisfied.
  + $Q$ contains no loops or multiple arrows.
  + For all vertices $x$ in $Q$, $x^- = tau(x)^+$.

  A morphism of stable representation quivers is a morphism of quivers commuting
  with the translation.

  A stable representation quiver is *connected*#idx(
    "connected",
    "stable representation quiver",
  )#idx("stable", "representation quiver", "connected") if it is non-empty and
  cannot be written as a disjoint union of two subquivers each stable under the
  translation. Note that this does not imply that the underlying quiver is
  connected.

  The *reduced graph*#idx("reduced graph")#idx("graph", "reduced") or *orbit
  graph*#idx("graph", "orbit")#idx("orbit", "graph") of a stable representation
  quiver $Q$ is the graph obtained from $Q$ by identifying each vertex $x$ with
  $tau(x)$ and then replacing each pair of arrows $x -> y$ and $y -> x$ by an
  undirected edge $x$---$y$.
] <def:quiver-morphism>

Thus for example the stable quiver of finitely generated $Lambda$-modules is a
stable representation quiver with translation $D T r$.

To a directed tree#idx("directed tree")#idx("tree", "directed") $B$ we associate
a stable representation quiver $ZZ B$#idx("$ZZ B$") as follows. The vertices of
$ZZ B$ are the pairs $(n, x)$ with $n in ZZ$ and $x$ a vertex of $B$. For each
arrow $x -> y$ in $B$ and each $n in ZZ$ we have two arrows $(n, x) -> (n, y)$
and $(n, y) -> (n - 1, x)$. The translation is defined via
$tau(n, x) = (n + 1, x)$. We regard $B$ as embedded in $ZZ B$ as the vertices
$(0, x)$ and the arrows connecting them.

#example(kind: "Examples")[
  If $B = #tree-quiver(example-tree)$ then
  $macron(B) = #tree-graph(example-tree)$ and
  $ ZZ B = dots.c #zb-quiver(example-tree, example-copies) dots.c $

  If $B = #tree-quiver(other-tree)$ then $macron(B)$ and $ZZ B$ are again as
  above. Keep this example in mind when reading the proof of the next
  proposition.
]

#source(168)

#lemma[
  Let $B$ be a directed tree and $Q$ a stable representation quiver. Given a
  quiver morphism $phi.alt : B -> Q$ and an integer $n$, there is a unique
  morphism of stable representation quivers $f : ZZ B -> Q$ such that
  $f(n, x) = phi.alt(x)$.
] <lem:zb-extension>

#proof[
  $f(m, x) = tau^(m-n) phi.alt(x)$ is clearly the unique such morphism.
]

#proposition[
  Let $B$ and $B'$ be directed trees. Then $ZZ B tilde.equiv ZZ B'$ as stable
  representation quivers if and only if $macron(B) tilde.equiv macron(B)'$.
] <prop:zb-isomorphism>

#proof[
  Since $macron(B)$ is the reduced graph of $ZZ B$, if $ZZ B tilde.equiv ZZ B'$
  then $macron(B) tilde.equiv macron(B)'$. Conversely, suppose
  $phi.alt : macron(B) tilde.equiv macron(B)'$. Choose a vertex $x$ of $B$, and
  send it to $(0, phi.alt(x))$ in $ZZ B'$. Since $B$ is connected we may extend
  this uniquely to a morphism of quivers $B -> ZZ B'$ in such a way that each
  $x$ in $B$ is sent to some $(a_x, phi.alt(x))$ in $ZZ B'$. Now by the lemma,
  we obtain a morphism of stable representation quivers $ZZ B -> ZZ B'$ sending
  $(n, x)$ to $(n + a_x, phi.alt(x))$. This is an isomorphism with inverse
  sending $(n, phi.alt(x))$ to $(n - a_x, x)$.
]

#definition[
  A group $Pi$ of automorphisms of a stable representation quiver $Q$ is said to
  be *admissible*#idx("admissible", "automorphisms")#idx(
    "automorphism, admissible",
  ) if no orbit of $Pi$ on the vertices of $Q$ intersects a set of the form
  ${x} union x^+$ or ${x} union x^-$ in more than one point. The quotient quiver
  $Q slash Pi$, defined in the obvious way, is then a stable representation
  quiver.

  A morphism of stable representation quivers $phi.alt : Q -> Q'$ is called a
  *covering*#idx("covering", "of quivers")#idx("quiver", "covering of") if it is
  surjective, and for each vertex $x$ of $Q$ the induced maps
  $x^- -> phi.alt(x)^-$ and $x^+ -> phi.alt(x)^+$ are bijective. It is clearly
  enough to check that $x^+ -> phi.alt(x)^+$ is bijective for each vertex $x$ of
  $Q$.

  Thus for example the canonical projection $Q -> Q slash Pi$, for $Pi$ an
  admissible group of automorphisms of $Q$, is a covering.
] <def:admissible-group>

#example[
  Taking $B = A_infinity$, we obtain a stable representation quiver
  $ ZZ B = #a-infinity-quiver $
  Let $Pi$ be the group of automorphisms generated by the $n$th power of the
  translation, $tau^n$. Then $Pi$ is admissible, and the resulting stable
  representation quiver $ZZ A_infinity slash (n)$ is called a *tube*;#idx(
    "tube",
  ) see Section~@sec:tubes.
]

#lemma[
  Let $B$ be a directed tree, $pi : ZZ B -> Q$ a morphism of stable
  representation quivers, $phi.alt : Q' -> Q$ a covering, and $(n, x)$ a vertex
  of #source(169)$ZZ B$. Then for each vertex $y$ of $Q'$ with
  $phi.alt(y) = pi(n, x)$, there is a unique morphism $psi : ZZ B -> Q'$ with
  $phi.alt compose psi = pi$ and $y = psi(n, x)$.
  $ #covering-lift $
] <lem:covering-lift>

#proof[
  The map $psi(n, x) = y$ clearly extends uniquely to a map from the copy of $B$
  consisting of the elements $(n, -)$ to $Q'$ whose composite with $phi.alt$ is
  $pi$. The lemma now follows from Lemma~@lem:zb-extension.
]

#theorem(title: [Riedtmann structure theorem], head-break: true)[
  Given a connected stable representation quiver $Q$, there is a directed tree
  $B$ and an admissible group of automorphisms $Pi subset.eq Aut(ZZ B)$ such
  that $Q tilde.equiv ZZ B slash Pi$. The graph $macron(B)$ associated to $B$ is
  determined by $Q$ uniquely up to canonical isomorphism, and $Pi$ is uniquely
  defined up to conjugation in $Aut(ZZ B)$.
] <th:riedtmann>

#proof[
  Given $Q$, we construct $B$ as follows. Choose a vertex $x$ of $Q$, and let
  $B$ have as vertices the paths
  $ (x = y_0 -> y_1 -> dots.c -> y_n) quad quad (n >= 0) $
  for which no $y_i = tau(y_(i+2))$. The arrows of $B$ are
  $
    (x = y_0 -> dots.c -> y_(n-1)) arrow.r.long
    (x = y_0 -> dots.c -> y_(n-1) -> y_n).
  $
  Clearly $B$ is a directed tree.

  The quiver morphism $B -> Q$ given by
  $ (x = y_0 -> dots.c -> y_n) |-> y_n $
  extends uniquely, by Lemma~@lem:zb-extension, to a morphism
  $phi.alt : ZZ B -> Q$. We check that $phi.alt : ZZ B -> Q$ is a covering
  morphism. If
  $ u = (x = y_0 -> dots.c -> y_n) $
  is a vertex of $B$, then $u^+$ is the set of vertices of the form
  $ (x = y_0 -> dots.c -> y_n -> z) $
  for which $tau(z) != y_(n-1)$ if $n >= 1$, while $u^-$ consists of the single
  vertex $(x = y_0 -> dots.c -> y_(n-1))$. Thus
  $
    (m, u)^+ = {(m, v), v in u^+} union {(m - 1, v), v in u^-}
  $
  has image $tau^m ({z in y_n^+ | tau(z) != y_(n-1)} union {tau^(-1) (y_(n-1))})
  = tau^m (y_n)^+$ in $Q$. Thus $(m, u)^+$ is in bijection with $tau^m (y_n)^+$
  as desired.

  Now let $Pi$ be the *fundamental group*#idx("fundamental group")#idx(
    "group",
    "fundamental",
  ) of $Q$ at $x$, namely the group of morphisms of stable representation
  quivers $rho : ZZ B -> ZZ B$ with $phi.alt compose rho = phi.alt$. Since $Q$
  has no loops, $Pi$ is admissible. It follows from Lemma~@lem:covering-lift
  that $Pi$ is transitive on the vertices of $ZZ B$ whose image is a given
  vertex of $Q$, and so $Q tilde.equiv ZZ B slash Pi$.

  #source(170)Also by Lemma~@lem:covering-lift, we see that if $ZZ B -> Q$ and
  $ZZ B' -> Q$ are two such covers, then we obtain inverse isomorphisms
  $ZZ B limits(arrow.r)^g ZZ B'$ and $ZZ B' limits(arrow.r.long)^(g^(-1)) ZZ B$.
  Hence $Pi' = g Pi g^(-1)$, and so by Proposition~@prop:zb-isomorphism,
  $macron(B) tilde.equiv macron(B)'$.
]

The stable representation quiver $ZZ B$ is called the *universal cover*#idx(
  "cover",
  "universal",
)#idx("universal", "cover") of $Q$, and the isomorphism type of $macron(B)$ is
called the *tree class*#idx("tree", "class") of $Q$.

#lemma[
  There is a natural map $kappa$ from the tree $macron(B)$ associated to $Q$ to
  the reduced graph of $Q$, which is surjective and does not identify adjacent
  points in $macron(B)$.
] <lem:tree-class-reduced-graph>

#proof[
  The composite map from $ZZ B$ to $Q$ and then to the reduced graph of $Q$ is
  surjective, and has the property that $(n, x)$ and $(n + 1, x)$ have the same
  image. Thus we have a well defined surjective map from $macron(B)$ to the
  reduced graph of $Q$. Since $Q tilde.equiv ZZ B slash Pi$ with $Pi$ an
  admissible group of automorphisms, this map does not identify adjacent points.
]

Finally, we note that a connected component $Q$ of the stable quiver of
$Lambda$-modules comes with a modulation which is invariant under the
translation $D T r$. Thus the tree class and reduced graph of $Q$ are modulated
graphs, and in particular have labelled graphs associated to them.

We shall see that for group algebras the tree class and reduced graph are very
restricted in possible shape.
