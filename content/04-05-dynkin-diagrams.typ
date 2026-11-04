#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-05-dynkin-diagrams.typ": (
  bond, diagram-table, double-edge-chain, dynkin, euclidean, folding-scheme,
  infinite-dynkin, valued-bond,
)

== Dynkin and Euclidean Diagrams <sec:dynkin-diagrams>

In our discussion of representation type, and also in our discussion of tree
classes of Auslander–Reiten quivers later in this chapter, we shall have need to
refer to the list of diagrams given in the following definition. The infinite
diagrams are only needed in the latter topic. For the moment you should ignore
the numbers attached to the vertices of the Euclidean and infinite Dynkin
diagrams; these will appear in the proofs of Lemma~@lem:euclidean-additive and
Proposition~@prop:infinite-dynkin-additive.

#definition[
  + The following labelled graphs are called the (finite) *Dynkin diagrams*#idx(
      "Dynkin diagram",
    )#idx("finite", "Dynkin diagram").

    #diagram-table(
      (
        [$A_n$#idx("$A_n$")],
        dynkin.A,
        [$E_6$#idx("$E_6$, $E_7$, $E_8$")],
        dynkin.E6,
      ),
      ([$B_n$#idx("$B_n$")], dynkin.B, [$E_7$], dynkin.E7),
      ([$C_n$#idx("$C_n$")], dynkin.C, [$E_8$], dynkin.E8),
      ([$D_n$#idx("$D_n$")], dynkin.D, [$F_4$#idx("$F_4$")], dynkin.F4),
      ([], [($n$ nodes)], [$G_2$#idx("$G_2$")], dynkin.G2),
    )
    In these pictures, we have used #bond(2, 1) and #bond(3, 1) to denote the
    labelled edges #valued-bond(2, 1) and #valued-bond(3, 1) respectively.
  + The following are the *infinite Dynkin diagrams*#idx(
      "infinite",
      "Dynkin diagram",
    ).

    #diagram-table(
      (
        [$A_infinity$#idx("$A_infinity$, $A_infinity^infinity$")],
        infinite-dynkin.A,
        [$D_infinity$#idx("$D_infinity$")],
        infinite-dynkin.D,
      ),
      (
        [$B_infinity$#idx("$B_infinity$")],
        infinite-dynkin.B,
        [$A_infinity^infinity$],
        infinite-dynkin.A2,
      ),
      ([$C_infinity$#idx("$C_infinity$")], infinite-dynkin.C, [], []),
    )
  + The following are the *Euclidean diagrams*#idx("Euclidean diagram").

    #diagram-table(
      (
        [$tilde(A)_n$#idx("$tilde(A)_n$, $tilde(A)_11$, $tilde(A)_12$")],
        euclidean.A,
        [$tilde(A)_11$],
        euclidean.A11,
      ),
      (
        [$tilde(B)_n$#idx("$tilde(B)_n$, $tilde(B C)_n$, $tilde(B D)_n$")],
        euclidean.B,
        [$tilde(A)_12$],
        euclidean.A12,
      ),
      (
        [#source(129)$tilde(C)_n$#idx("$tilde(C)_n$, $tilde(C D)_n$")],
        euclidean.C,
        [$tilde(E)_6$#idx("$tilde(E)_6$, $tilde(E)_7$, $tilde(E)_8$")],
        euclidean.E6,
      ),
      (
        [$tilde(D)_n$#idx("$tilde(D)_n$")],
        euclidean.D,
        [$tilde(E)_7$],
        euclidean.E7,
      ),
      ([$tilde(B C)_n$], euclidean.BC, [$tilde(E)_8$], euclidean.E8),
      (
        [$tilde(B D)_n$],
        euclidean.BD,
        [$tilde(F)_41$#idx("$tilde(F)_41$, $tilde(F)_42$")],
        euclidean.F41,
      ),
      ([$tilde(C D)_n$], euclidean.CD, [$tilde(F)_42$], euclidean.F42),
      (
        [],
        [($n + 1$ nodes)],
        [$tilde(G)_21$#idx("$tilde(G)_21$, $tilde(G)_22$")],
        euclidean.G21,
      ),
      ([], [], [$tilde(G)_22$], euclidean.G22),
    )
] <def:dynkin-euclidean>

Note that $tilde(A)_0$ consists of a single vertex with a loop, and $tilde(A)_1$
consists of two vertices with two distinct edges going between them. Also note
that $B_2 = C_2$ and $A_3 = D_3$, but that there are no further duplications in
the above list.

Given two labelled graphs $T_1$ and $T_2$, we say that $T_1$ is *smaller*#idx(
  "smaller (labelled graph)",
)#idx("labelled graph", "smaller") than $T_2$ if there is an injective morphism
of graphs $rho : T_1 -> T_2$ such that for each edge
$x limits(class("relation", dash.em))^gamma y$ in $T_1$,
$attach(d, bl: x, tr: gamma, br: y)
lt.eq attach(d, bl: rho(x), tr: gamma, br: rho(y))$, and *strictly smaller*#idx(
  "labelled graph",
  "strictly smaller",
) if $rho$ can be chosen not to be an isomorphism. Note that an infinite
labelled graph may be strictly smaller than itself. $A_infinity$ is an example
of this.

#lemma[
  Given any connected labelled graph $T$, either $T$ is a (finite or infinite)
  Dynkin diagram or there is a Euclidean diagram which is smaller than $T$. Both
  possibilities may not occur simultaneously.
] <lem:dynkin-or-euclidean>

#proof[
  Suppose there is no Euclidean diagram which is smaller than $T$. Looking at
  $tilde(A)_n$, we see that $T$ has no cycles, and is hence a labelled tree.
  Looking at $tilde(A)_11$ and $tilde(A)_12$, all edges are of the form
  $(1, 1)$, $(2, 1)$ or $(3, 1)$. Looking at $tilde(G)_21$ and $tilde(G)_22$, if
  an edge of type $(3, 1)$ occurs then $T tilde.equiv G_2$. Looking at
  $tilde(B)_n$, $tilde(C)_n$ and $tilde(B C)_n$, there is at most one edge of
  type $(2, 1)$. Looking at $tilde(B D)_n$ #source(130)and $tilde(C D)_n$, if
  there is an edge of the form $(2, 1)$ then
  $ T = #double-edge-chain $
  and looking at $tilde(F)_41$ and $tilde(F)_42$ this forces
  $T tilde.equiv F_4$, $B_n$, $C_n$, $B_infinity$ or $C_infinity$. Otherwise $T$
  is a tree with all edges of type $(1, 1)$. Then looking at $tilde(D)_n$, it
  has at most one branch point. Finally, looking at $tilde(E)_6$, $tilde(E)_7$
  and $tilde(E)_8$ completes the proof.
]

#definition[
  The *Cartan matrix*#idx("Cartan", "matrix")#idx("matrix, Cartan") of a
  labelled graph $T$ (not to be confused with the Cartan matrix of an algebra)
  is the matrix whose rows and columns are indexed by the vertices of the graph,
  and with entries
  $c_(x y) = 2 delta_(x y) - sum_gamma attach(d, bl: x, tr: gamma, br: y)$,
  where the sum runs over edges $x limits(class("relation", dash.em))^gamma y$
  in $T$.

  The *symmetrised Cartan matrix*#idx("symmetrised Cartan matrix")#idx(
    "Cartan",
    "matrix",
    "symmetrised",
  ) of a valued graph has entries $tilde(c)_(x y) = c_(x y) f_y$, where $f_y$ is
  as given in the definition of a valued graph. Note that this matrix is
  symmetric.
] <def:cartan-matrix-graph>

Thus for example the Cartan matrix of $F_4$ is the matrix
$
  mat(
    align: #right,
    2, -1, 0, 0;
    -1, 2, -2, 0;
    0, -1, 2, -1;
    0, 0, -1, 2
  ).
$

#definition[
  A *subadditive function*#idx("subadditive function")#idx(
    "function, (sub)additive",
  ) on a labelled graph $T$ is a function $x |-> n_x$ from the vertices of $T$
  to the positive rationals satisfying $sum_x n_x c_(x y) gt.eq 0$ for all $y$.
  A subadditive function is called *additive*#idx("additive", "function") if
  $sum_x n_x c_(x y) = 0$ for all $y$.

  If $T$ is a labelled graph, the *opposite*#idx("opposite graph")#idx(
    "graph",
    "opposite",
  ) labelled graph $T^op$ has the same vertices and edges, but with the label
  $attach(d, bl: x, tr: gamma, br: y)$ replaced by
  $attach(d, bl: y, tr: gamma, br: x)$. If $T$ is a valued graph, then so is
  $T^op$, by replacing the $f_x$ by $n slash f_x$ for some positive integer $n$.
] <def:subadditive>

#remark[
  This broadens the usual definition, where the $n_x$ are taken to be positive
  integers. We shall make use of this broader definition in our analysis of
  periodic modules.
]

#lemma[
  + Each Euclidean diagram admits an additive function.
  + If $T^op$ admits an additive function then every subadditive function on $T$
    is additive.
  + Every subadditive function on a Euclidean diagram is additive.
] <lem:euclidean-additive>

#proof[
  + The numbers attached to the vertices of the Euclidean diagrams in the
    illustration form an additive function in each case.
  + Suppose $x |-> n_x$ is a subadditive function on $T$. By hypothesis there is
    a function $x |-> n'_x$ such that $sum_y c_(x y) n'_y = 0$ for all $x$. Thus
    $sum_(x, y) n_x c_(x y) n'_y = 0$, while $sum_x n_x c_(x y) gt.eq 0$ and
    $n'_y > 0$ for each $y$. Hence we have equality and $x |-> n_x$ is additive.
  + follows from (i) and (ii), since the opposite of any Euclidean diagram is
    Euclidean.
]

#lemma[
  #source(131)Suppose $T$ and $T'$ are connected labelled graphs and $T$ is
  strictly smaller than $T'$. Suppose also that $x |-> n_x$ is a subadditive
  function on $T'$. Then identifying $T$ with a subgraph of $T'$, the
  restriction of $x |-> n_x$ to $T$ is a subadditive function on $T$ which is
  not additive.
] <lem:strictly-smaller>

#proof[
  For $y$ a vertex of $T$, we have
  $
    2 n_y gt.eq sum_(x, gamma in T') n_x attach(d, bl: x, tr: gamma, br: y)
    gt.eq sum_(x, gamma in T) n_x attach(d, bl: x, tr: gamma, br: y),
  $
  where the sums are over edges $x limits(class("relation", dash.em))^gamma y$,
  and the $attach(d, bl: x, tr: gamma, br: y)$ are the values in $T'$ in the
  first sum and in $T$ in the second. Since $T$ is strictly smaller than $T'$,
  for some $y in T$ the second inequality is strict, and so the restriction of
  $x |-> n_x$ is not additive.
]

#proposition[
  Each of the infinite Dynkin diagrams admits an additive function.
  + For $A_infinity$ there are also subadditive functions which are not
    additive.
  + For the other infinite Dynkin diagrams every subadditive function is a
    multiple of a given bounded additive function.
] <prop:infinite-dynkin-additive>

#proof[
  The numbers attached to the vertices in the illustration form an additive
  function in each case.
  + $A_infinity$ is strictly smaller than itself, and so by
    Lemma~@lem:strictly-smaller there is a subadditive function which is not
    additive.
  + First we show that every subadditive function on $A_infinity^infinity$ is
    constant and additive. We label the vertices of $A_infinity^infinity$ with
    the integers. Suppose $j |-> n_j$ is a subadditive function on
    $A_infinity^infinity$, and suppose $n_(j-1) < n_j$ for some $j$. The
    inequality $2 n_(j-1) gt.eq n_j + n_(j-2)$ may be written in the form
    $n_(j-1) - n_(j-2) gt.eq n_j - n_(j-1)$, so that by induction on $r$ we have
    $n_(j-r) lt.eq n_j - r(n_j - n_(j-1))$ for all $r gt.eq 0$. Choosing $r$
    large enough so that $r(n_j - n_(j-1)) > n_j$ we see that $n_(j-r) < 0$,
    contradicting the definition of subadditive function. Similarly if
    $n_(j-1) > n_j$ we find that some $n_(j+r) < 0$.

    For $B_infinity$, $C_infinity$ and $D_infinity$, given a subadditive
    function we form a subadditive function on $A_infinity^infinity$ according
    to the following scheme.
    #folding-scheme
    The result follows immediately for $B_infinity$ and $C_infinity$. For
    $D_infinity$ we obtain $n_0 + n'_0 = n_1$. Subadditivity forces
    $2 n_0 gt.eq n_1$ and $2 n'_0 gt.eq n_1$ whence $n_0 = n'_0$, and the result
    follows.
]

#source(132)The following is a generalisation by Happel, Preiser and Ringel
[@bib:Happel1980] of the characterisation by Vinberg [@bib:Vinberg1971] and by
Berman, Moody and Wonenburger [@bib:Berman1972] of the finite Dynkin diagrams.

#theorem[
  Let $T$ be a connected labelled graph, and $x |-> n_x$ a subadditive function
  on $T$. Then the following hold:
  + $T$ is either a Dynkin diagram (finite or infinite) or a Euclidean diagram.
  + If $x |-> n_x$ is not additive then $T$ is a finite Dynkin diagram or
    $A_infinity$.
  + If $x |-> n_x$ is additive then $T$ is an infinite Dynkin diagram or a
    Euclidean diagram.
  + If $x |-> n_x$ is unbounded then $T tilde.equiv A_infinity$.
] <th:subadditive-classification>

#proof[
  + Suppose this is false. Then by Lemma~@lem:dynkin-or-euclidean there is a
    Euclidean diagram which is strictly smaller than $T$. Thus by
    Lemma~@lem:strictly-smaller there is a subadditive function on this
    Euclidean diagram which is not additive. This contradicts
    Lemma~@lem:euclidean-additive[(iii)].
  + This follows from Lemma~@lem:euclidean-additive[(iii)] and
    Proposition~@prop:infinite-dynkin-additive[(ii)].
  + Suppose this is false. Then $T$ is a finite Dynkin diagram by (i), and hence
    so is $T^op$. Thus $T^op$ is strictly smaller than some Euclidean diagram,
    and so by Lemma~@lem:strictly-smaller and
    Lemma~@lem:euclidean-additive[(i)], $T^op$ admits a subadditive function
    which is not additive, contradicting Lemma~@lem:euclidean-additive[(ii)].
  + If $x |-> n_x$ is unbounded then $T$ is infinite, and so by (i) it is an
    infinite Dynkin diagram. Hence by
    Proposition~@prop:infinite-dynkin-additive[(ii)],
    $T tilde.equiv A_infinity$.
]
