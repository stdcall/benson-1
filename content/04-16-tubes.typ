#import "main-defs.typ": *
#import "statements.typ": *

== Tubes <sec:tubes>

In this section we investigate a special type of stable quiver component called
tubes.

#definition[
  An infinite *n-tube*#idx("tube") is a stable representation quiver of the form
  $(ZZ slash n) A_infinity$. A finite $n$-tube of length $q$ is a stable
  representation quiver of the form $(ZZ slash n) A_q$.

  A module $M$ is said to be *DTr-periodic*#idx("module", "periodic")#idx(
    "periodic",
    "module",
  ) (or just periodic) if $(D T r)^n M tilde.equiv M$ for some $n >= 1$.
] <def:tube>

Note that in case $Lambda$ is symmetric we have $D T r = Omega^2$ by
Proposition~@prop:symmetric-dtr, so that a $D T r$-periodic module is the same
as an $Omega$-periodic module.

#theorem(title: [Happel, Preiser and Ringel [@bib:Happel1980]])[
  Suppose that $Q$ is a connected component of the stable quiver of finitely
  generated $Lambda$-modules which contains some periodic module. Then every
  module in $Q$ is periodic. If $Q$ is infinite then it is a tube. If $Q$ is
  finite then the tree class is a finite Dynkin diagram, and is equal to the
  reduced graph (but $Q$ need not be a tube).
] <th:happel-preiser-ringel>

#proof[
  Suppose $(D T r)^n M = M$, and let $x$ be the vertex of $Q$ corresponding to
  $M$. Then $(D T r)^n$ induces a permutation on $x^-$, which is a finite set by
  Proposition~@prop:irreducible-maps, and so some power of $(D T r)^n$
  stabilises $x^-$ pointwise. The same is true of $x^+$, so arguing by induction
  we see that every module in $Q$ is periodic.

  #source(171)Now the function on the reduced graph or tree class of $Q$ which
  assigns to each vertex the average number of composition factors in the
  (finite) $D T r$-orbit in $Q$ corresponding to the vertex is easily seen to be
  subadditive. So by Theorem~@th:subadditive-classification[(i)] this graph is
  either a Dynkin diagram or a Euclidean diagram. If $Q$ is infinite and this
  subadditive function is additive, then $Q$ is a component of the
  Auslander-Reiten quiver, and so by Theorem~@th:auslander-infinite-component
  this additive function is unbounded. By
  Theorem~@th:subadditive-classification[(iv)] the tree class is then
  $A_infinity$.#ed-note[The book says here that this case cannot happen, by
    Theorem~@th:subadditive-classification[(ii)] and (iv). It does happen: the
    1-tubes of the Klein four group in Examples~(i) after
    Theorem~@th:component-types are infinite components without projective
    modules, and the dimension $2 n$ of the $n$th module is an unbounded
    additive function on their tree class $A_infinity$.] If $Q$ is infinite and
  this subadditive function is not additive, then by
  Theorem~@th:subadditive-classification[(iv)] the tree class is $A_infinity$.
  Since the only automorphisms of $ZZ A_infinity$ are the translations, by
  Theorem~@th:riedtmann it follows from the fact that every module is periodic
  that for some $n >= 1$, $Q tilde.equiv (ZZ slash n) A_infinity$.

  If $Q$ is finite, then it is connected to at least one projective or injective
  module, since otherwise $Q$ is a component of the Auslander-Reiten quiver, and
  we deduce from Proposition~@prop:finite-component that $Q$ consists of all the
  indecomposable modules in a block of $Lambda$ of finite representation type.
  Thus the above subadditive function is not additive. So by
  Theorem~@th:subadditive-classification[(ii)] the tree class and reduced graph
  are both finite Dynkin diagrams. Finally by
  Lemma~@lem:tree-class-reduced-graph and the fact that finite Dynkin diagrams
  are trees, we see that the tree class and reduced graph are equal.
]
