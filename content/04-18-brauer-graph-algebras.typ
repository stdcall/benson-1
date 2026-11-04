#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-18-brauer-graph-algebras.typ": (
  brauer-graph-picture, ext-quiver, projective-modules,
)

== Brauer graph algebras <sec:brauer-graph-algebras>

In this section we describe some finite dimensional algebras which arise in the
representation theory of finite groups, namely the class of Brauer graph
algebras#idx("algebra", "Brauer graph")#idx("Brauer", "graph", "algebra"). We
show that there is a simple condition given in terms of almost split sequences
which guarantees that a finite dimensional algebra is a Brauer graph algebra.
Among the Brauer graph algebras, we identify #source(178)the ones of finite
representation type as being the Brauer tree algebras. In
Section~@sec:cyclic-defect, we shall see that blocks of cyclic defect of a
finite group are Brauer tree algebras. The ideas involved in this section are an
adaptation of the ideas in Erdmann [@bib:Erdmann1987]. Throughout this section
we work over an algebraically closed field $k$ of coefficients.

#definition[
  A *Brauer graph*#idx("Brauer", "graph")#idx("graph", "Brauer") consists of a
  finite undirected connected graph (possibly with loops and multiple edges),
  together with the following data. To each vertex we assign a cyclic ordering
  of the edges incident to it, and an integer greater than or equal to one,
  called the *multiplicity*#idx("multiplicity", "in Brauer graph") of the
  vertex.

  A *Brauer tree*#idx("Brauer", "tree")#idx("tree", "Brauer") is a Brauer graph
  which is a tree, and having at most one vertex with multiplicity greater than
  one. If there is such a vertex, it is called the *exceptional vertex*#idx(
    "exceptional",
    "vertex",
  )#idx("vertex", "exceptional"), and its multiplicity is called the
  *exceptional multiplicity*;#idx(
    "exceptional",
    "multiplicity",
  )#idx("multiplicity", "exceptional") otherwise the exceptional multiplicity is
  defined to be one.
] <def:brauer-graph>

Note that at least in the case of a tree, the cyclic ordering on the edges
around a vertex is usually indicated by drawing the tree in such a way that the
ordering is anticlockwise around each vertex. Thus the cyclic orderings are
sometimes thought of as being given by a "planar embedding"#idx(
  "planar embedding",
)#idx("embedding", "planar").

We say a finite dimensional algebra $Lambda$ is a Brauer graph algebra for a
given Brauer graph, if there is a one-one correspondence between the edges $j$
of the graph and the simple $Lambda$-modules $S_j$ in such a way that the
projective cover $P_j$ of $S_j$ has the following description. We have
$P_j slash Rad(P_j) tilde.equiv Soc(P_j) tilde.equiv S_j$, and
$Rad(P_j) slash Soc(P_j)$ is a direct sum of two (possibly zero) uniserial
modules $U_j$ and $V_j$ corresponding to the two vertices $u$ and $v$ at the end
of the edge $j$. If the edges around $u$ are cyclically ordered
$j, j_1, j_2, dots, j_r, j$ and the multiplicity of the vertex $u$ is $e_u$,
then the corresponding uniserial module $U_j$ has composition factors (from the
top)
$
  S_(j_1), S_(j_2), dots, S_(j_r), S_j, S_(j_1), dots, S_(j_r), S_j, dots,
  dots, S_(j_r)
$
so that $S_(j_1), dots, S_(j_r)$ appear $e_u$ times and $S_j$ appears $e_u - 1$
times.

For example, a Brauer graph algebra for the Brauer graph
$ #brauer-graph-picture $
#source(179)\(unmarked vertices have multiplicity one, and the cyclic ordering
is anticlockwise around the vertices) has projective modules as follows:
$ #projective-modules $

Note that by the methods of Section~@sec:quivers, at least if there are no
loops, the basic algebra of a Brauer graph algebra over an algebraically closed
field is almost determined by the Brauer graph. Namely, the Ext-quiver#idx(
  "Ext",
  "-quiver",
) consists of one vertex for each edge of the Brauer graph, and directed edges
going in oriented cycles corresponding to the vertices of the Brauer graph (or
rather, those with either valency or multiplicity greater than one). For
example, the Ext-quiver in the above example is
$ #ext-quiver $
There is one relation corresponding to each edge, and it says that going round
the cycle corresponding to the vertex at one end, a number of times equal to the
multiplicity, is equal to some non-zero multiple of doing the same for the
vertex at the other end. In the above example the relations say that there are
constants $lambda_1$, $lambda_2$, $lambda_3$ with
$
  beta alpha beta alpha beta alpha = lambda_1 . gamma delta, quad
  alpha beta alpha beta alpha beta = lambda_2 . epsilon eta zeta, quad
  delta gamma = lambda_3 . eta zeta epsilon, quad
  eta zeta epsilon eta = 0.
$

By replacing the generators by multiples of the same generators, some of the
parameters can be set equal to one. If the graph is a tree, then all the
parameters can be set equal to one by this method, but in general the number of
remaining parameters will equal the number of edges minus the number of vertices
plus one (this is $H^1$ of the graph!). However, even these parameters are
forced to be equal to one if the algebra is assumed to be symmetric. Thus in the
above example $lambda_1$ and $lambda_2$ may be set equal to one by replacing
$gamma$ and $epsilon$ by suitable multiples, but then $lambda_3$ is fixed. But
if $lambda$ is a linear map on $Lambda$ as in the definition of a symmetric
algebra, then
$
  lambda(eta zeta epsilon) & = lambda(epsilon eta zeta)
                             = lambda(alpha beta alpha beta alpha beta)
                             = lambda(beta alpha beta alpha beta alpha) \
                           & = lambda(gamma delta) = lambda(delta gamma)
                             = lambda_3 . lambda(eta zeta epsilon)
$
#source(180)and so since $lambda$ may not vanish on the one dimensional ideal
defined by this element, we have $lambda_3 = 1$.

We now investigate some conditions which force a finite dimensional symmetric
algebra to be a Brauer graph algebra. Suppose $Lambda$ is a finite dimensional
symmetric algebra. If $S$ is a simple $Lambda$-module with projective cover
$P_S$, and $U$ is a summand of $Rad(P_S) slash Soc(P_S)$, then we write
$overline(U)$ for the extension of $S = P_S slash Rad(P_S)$ by $U$
$ 0 -> U -> overline(U) -> S -> 0 $
and $underline(U)$ for the extension of $U$ by $S = Soc(P_S)$
$ 0 -> S -> underline(U) -> U -> 0. $

#lemma(title: [Erdmann [@bib:Erdmann1987]])[
  Suppose $Lambda$, $S$, $P_S$, $U$ and $overline(U)$ are as above. If
  $0 != U != Rad(P_S) slash Soc(P_S)$ then in the almost split sequence ending
  in $overline(U)$, the middle term is indecomposable.
] <lem:erdmann-middle-term>

#proof[
  Suppose $Rad(P_S) slash Soc(P_S)$ decomposes as $U plus.o V$ with $U$ and $V$
  non-zero. Note that $underline(V) tilde.equiv Omega(overline(U))$. Let $m$ be
  the number of simple summands in $Soc(U) tilde.equiv Soc(overline(U))$ and $n$
  be the number of simple summands in
  $
    V slash Rad(V) tilde.equiv underline(V) slash Rad(underline(V))
    tilde.equiv Soc(Omega underline(V))
    tilde.equiv Soc(Omega^2 overline(U)).
  $
  If the almost split sequence ending in $overline(U)$ is
  $ 0 -> Omega^2 overline(U) -> M limits(arrow.r)^alpha overline(U) -> 0 $
  then since $overline(U) tilde.equiv.not P_S slash Soc(P_S)$, $M$ has no
  projective summands. The almost split sequence beginning with
  $underline(V) = Omega overline(U)$ is
  $ 0 -> underline(V) -> Omega^(-1) M -> Omega^(-2) underline(V) -> 0 $
  and so by dualising and reversing the rôles of $U$ and $V$ if necessary, we
  may assume that $n <= m$. Since $Soc(overline(U))$ is a proper submodule of
  $overline(U)$, the inclusion $Soc(overline(U)) arrow.r.hook overline(U)$
  factors through $alpha$ and so $Soc(M)$ has $m + n <= 2 m$ simple summands.

  If $M = plus.o.big_(i=1)^k M_i$ then the components
  $alpha_i : M_i -> overline(U)$ of $alpha$ are irreducible maps by
  Proposition~@prop:irreducible-maps. Since $overline(U)$ has a unique maximal
  submodule, if $alpha_i$ is injective, then $M_i$ is a submodule of $U$. But
  then $alpha_i$ has the non-trivial factorisation
  $M_i arrow.r.hook P_S slash Soc(P_S) ->> overline(U)$. So each $alpha_i$ is
  surjective, and the map $P_S ->> overline(U)$ lifts to $P_S -> M_i$. This lift
  has $Soc(P_S)$ in its kernel, and $P_S slash Soc(P_S) ->> overline(U)$ is
  surjective on socles, so $alpha_i (Soc(M_i)) = Soc(overline(U))$. If $alpha_i$
  is injective on socles then it is injective, contradicting the fact that it is
  an irreducible map. Thus $Soc(M_i)$ has strictly greater than $m$ summands.
  Since $Soc(M)$ has at most $2 m$ summands, this forces $M$ to be
  indecomposable.
]

#theorem[
  Suppose $Lambda$ is a finite dimensional symmetric algebra with $e$ simple
  modules, none of which is projective or periodic of period one. Then there are
  at least $2 e$ almost split sequences whose middle terms have only one
  non-projective summand. If there are exactly $2 e$ such almost split sequences
  then $Lambda$ is a Brauer graph algebra.
] <th:brauer-graph-algebra>

#source(181)

#proof[
  For each simple module $S$ we produce at least two almost split sequences
  satisfying the given condition. Let $P_S$ be the projective cover of $S$. Then
  $Soc(P_S) <= Rad(P_S)$ and $Rad(P_S) slash Soc(P_S)$ is non-zero, since $S$ is
  not projective or periodic of period one. If it is indecomposable then the
  almost split sequences terminating in $S$ and $P_S slash Soc(P_S)$ satisfy the
  given condition (see Proposition~@prop:almost-split-projective-injective). If
  $Rad(P_S) slash Soc(P_S) = U plus.o V$ with $U$ and $V$ non-zero then by the
  lemma the almost split sequences terminating in $overline(U)$ and
  $overline(V)$ satisfy the given condition. It is easy to see that the $2 e$
  almost split sequences produced in this way are distinct.

  Now suppose there are $e$ simple modules $S_1, dots, S_e$ and exactly $2 e$
  such almost split sequences. Let $P_i$ be the projective cover of $S_i$. Then
  the quotient $Rad(P_i) slash Soc(P_i)$ has at most two indecomposable
  summands, since otherwise we can produce more almost split sequences by the
  above process. If there are exactly two summands, we call them $U_i$ and
  $V_i$. If $Rad(P_i) slash Soc(P_i)$ is indecomposable we write $U_i$ for it,
  and set $V_i = 0$ and $overline(V)_i = underline(V)_i = S_i$. Now the $2 e$
  almost split sequences ending in the $overline(U)_i$ and $overline(V)_i$ have
  to equal, as a set, the $2 e$ almost split sequences ending in
  $underline(U)_i$ and $underline(V)_i$. Thus each $overline(U)_i$ and
  $overline(V)_i$ is one of the $underline(U)_j$ or $underline(V)_j$. In
  particular there is a permutation $rho$ of the set
  ${overline(U)_i, overline(V)_i, 1 <= i <= e}$ with
  $rho(overline(U)_i) = underline(U)_i$ and
  $rho(overline(V)_i) = underline(V)_i$. Thus $Soc(overline(U)_i)$ and
  $Soc(overline(V)_i)$ are simple. Arguing by induction using the maps
  $underline(U)_i -> overline(U)_i$ and $underline(V)_i -> overline(V)_i$ which
  have kernel and cokernel $S_i$, we see that each $overline(U)_i$ and
  $overline(V)_i$ is uniserial and of the same length as $rho(overline(U)_i)$,
  resp. $rho(overline(V)_i)$. The composition factors, from the top, of
  $overline(U)_i$ are given by repeated application of $rho$:
  $
    overline(U)_i slash Rad overline(U)_i,
    rho overline(U)_i slash Rad rho overline(U)_i,
    rho^2 overline(U)_i slash Rad rho^2 overline(U)_i, dots
  $

  We build the Brauer graph corresponding to $Lambda$ by taking an edge for each
  $S_i$. The two ends of this edge correspond to $overline(U)_i$ and
  $overline(V)_i$. The edges in cyclic order around the vertex at the end at
  $overline(U)_i$ correspond to the simple modules in the list above. The length
  of $overline(U)_i$ is a multiple of the number of distinct modules in this
  list, namely the number of images of $overline(U)_i$ under $rho$, and this
  multiple is used as the multiplicity at the vertex.
]

#proposition[
  If $Lambda$ is a Brauer graph algebra of finite representation type then the
  Brauer graph is a Brauer tree.
] <prop:brauer-tree-finite-type>

#proof[
  We first show that if the graph has a cycle then the algebra has infinite
  representation type. If $S_1, dots, S_r$ are simple modules which form a cycle
  in the graph of minimal length, then the projective cover $P_i$ of $S_i$ has a
  quotient $M_i$ with $M_i slash Rad(M_i) tilde.equiv S_i$ and
  $Soc(M_i) tilde.equiv S_(i-1) plus.o S_(i+1)$, where the subscripts are taken
  modulo $r$, and $Rad(M_i) slash Soc(M_i)$ does not involve any of
  $S_1, dots, S_r$ as subquotients. So $M_1 plus.o M_3$ has a diagonal copy of
  $S_2$ as a submodule, which we may quotient out. Similarly
  $M_1 plus.o M_3 plus.o M_5 plus.o dots.c plus.o M_(r-1)$ (going once round the
  cycle if $r$ is even and twice if $r$ is odd) has a diagonally embedded
  submodule $S_2 plus.o S_4 plus.o dots.c plus.o S_(r-2)$ which we quotient out
  to make a module $hat(M)$, which still has two copies of $S_r$ in its socle.
  Since $k$ is infinite, there are infinitely many isomorphisms $lambda$ from
  the copy of $S_r$ in #source(182)$Soc(M_1)$ and the copy in $Soc(M_(r-1))$.
  Each such isomorphism defines a diagonally embedded copy of $S_r$ in $hat(M)$,
  and we write $M(lambda)$ for the quotient. We claim that the $M(lambda)$ are
  non-isomorphic indecomposable $Lambda$-modules. First we show that $M(lambda)$
  is indecomposable. If $r = 1$ or $2$ then $M(lambda)$ has a unique minimal
  submodule and is hence indecomposable, so suppose $r > 2$. Note that
  $M(lambda) slash Rad(M(lambda))$ has no composition factors in common with
  $Rad(M(lambda)) slash Soc(M(lambda))$. Denote by $phi.alt_i (lambda)$ the map
  $M_i -> M(lambda)$ defined by the construction. Suppose
  $M(lambda) = M' plus.o M''$. Since $M(lambda) slash Rad(M(lambda))$ is
  multiplicity free, the image of $phi.alt_i (lambda)$ composed with projection
  onto one of the summands, say $M'$, has non-zero image in $M' slash Rad(M')$
  and the composite with the other projection has zero image in
  $M'' slash Rad(M'')$. Since $S_i$ does not appear as a composition factor of
  $Rad(M'') slash Soc(M'')$ this means that the image of
  $M_i limits(arrow.r.long)^(phi.alt_i (lambda)) M(lambda) -> M''$ lies in
  $Soc(M'')$ and so the image of $Soc(M_i)$ in $M''$ is zero. Thus both the
  simple summands of $Soc(M_i)$ lie in $M'$. One of these simple summands also
  lies in the image of $Soc(M_(i+2))$, and so arguing by induction we see that
  every simple module in the socle of $M$ lies in the socle of $M'$ and so
  $M'' = 0$.

  Next we show that if $M(lambda) tilde.equiv M(mu)$ then $lambda = mu$. Suppose
  that $psi : M(lambda) -> M(mu)$ is an isomorphism. Then
  $psi compose phi.alt_i (lambda)$ agrees on $Soc(M_i)$ with some non-zero
  multiple $alpha_i phi.alt_i (mu)$ of $phi.alt_i (mu)$. Comparing the socles of
  $M_i$ and $M_(i+1)$, we see that $alpha_i = alpha_(i+1)$, so that by induction
  $alpha_1 = alpha_r$. Then comparing the socles of $M_1$ and $M_r$ we see that
  $lambda = mu$. We have assumed that $r > 2$ in this argument, but a similar
  argument works for $r <= 2$.

  We have now shown that if $Lambda$ is of finite representation type then the
  graph has no cycles, so it remains to show that there is at most one vertex
  with multiplicity greater than one. If there is more than one, we may choose a
  path with no repetitions, where the two end vertices have multiplicity greater
  than one and none of the remaining vertices do. Let $S_1, dots, S_r$ be the
  simple modules corresponding to the edges along this path. As before, the
  projective cover $P_i$ of $S_i$ has a quotient $M_i$ with
  $M_i slash Rad(M_i) tilde.equiv S_i$, $Rad(M_i) slash Soc(M_i)$ does not
  involve any of $S_1, dots, S_r$, $Soc(M_i) tilde.equiv S_(i-1) plus.o S_(i+1)$
  for $2 <= i <= r - 1$, $Soc(M_1) tilde.equiv S_1 plus.o S_2$ and
  $Soc(M_r) tilde.equiv S_(r-1) plus.o S_r$. So we may apply exactly the same
  procedure as before to obtain quotients $M(lambda)$ of
  $M_1 plus.o M_3 plus.o dots.c plus.o M_(r-1) plus.o M_r plus.o M_(r-2)
  plus.o dots.c plus.o M_2$ if $r$ is even and
  $M_1 plus.o M_3 plus.o dots.c plus.o M_(r-2) plus.o M_r plus.o M_(r-1)
  plus.o M_(r-3) plus.o dots.c plus.o M_2$ if $r$ is odd. Exactly the same
  arguments show that the $M(lambda)$ are distinct and indecomposable.
]

#remark(kind: "Recent Progress", punct: ":")[
  Since the first edition of this book was published, Erdmann [@bib:Erdmann1995]
  has proved that for a block of a group algebra having wild representation
  type, all connected components of the stable quiver have type $A_infinity$.
]
