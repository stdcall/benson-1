#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/06-02-brauer-map.typ": brauer-transfer-square

== The Brauer map <sec:brauer-map>

From now on, we restrict our attention to the (diagonal) action of $G$ on $G$ by
conjugation, and drop the symbol $Delta$ used in the last section. The following
lemma is our starting point for the discussion of the Brauer map and Brauer's
three main theorems. The first of these gives a one–one correspondence between
blocks of $R G$ with defect group $D$ and blocks of $R N_G (D)$ with defect
group $D$. First note that we are assuming that $R$ is either $cal(O)$ or $k$,
so that by Corollary~@cor:defect-groups-lift it suffices to consider the case
$R = k$.

#lemma[
  Suppose $D$ is a $p$-subgroup of $G$. With the notation of
  Definition~@def:transfer, we have
  + $(k G)^D = k C_G (D) plus.o sum_(D' < D) (k G)_(D')^D$
  + $(k G)^(N_G (D)) = (k C_G (D))^(N_G (D)) plus.o
    sum_(D lt.eq.not Q <= N_G (D)) (k G)_Q^(N_G (D))$
  in each case as a direct sum of a subring and a two-sided ideal. Each summand
  in #statement-comment[(ii)] is contained in the corresponding summand in
  #statement-comment[(i)].
] <lem:brauer-decomposition>

#proof[
  The space $(k G)^D$ has as a basis the orbit sums of $D$ on elements of $G$.
  The orbits of length one span $k C_G (D)$, and the sums of orbits of length
  greater than one are transfers from proper subgroups of $D$. The intersection
  of $k C_G (D)$ and $sum_(D' < D) (k G)_(D')^D$ is zero since $k$ has
  characteristic $p$.

  Similarly, for the second statement we split up the orbits of $N_G (D)$ into
  those on which $D$ acts trivially and those on which $D$ has no fixed points.

  In each case, the right-hand summand is a two-sided ideal by
  Lemma~@lem:transfer-properties[(i)] and (ii).
]

#remark[
  The above lemma does not hold with $k$ replaced by $cal(O)$ since the two
  pieces on the right hand sides do not intersect in zero. However, it follows
  from the discussion in the last section that there is a one-one correspondence
  between blocks of $k G$ and blocks of $cal(O) G$ preserving defect groups, so
  that if we wish to count blocks then it suffices to work over $k$.
]

#proposition[
  Suppose $D$ is a normal $p$-subgroup of $G$. Then every idempotent in $Z(k G)$
  lies in $k C_G (D)$. In particular, if $C_G (D) <= D$ then $k G$ has only one
  block.
] <prop:normal-p-subgroup-idempotents>

#proof[
  Since $D$ is a $p$-subgroup, it acts trivially on every simple $k G$-module
  (its fixed points form a non-zero invariant submodule, by
  Lemma~@lem:p-group-simple), and hence on $k G slash J(k G)$. Since transfer
  from a proper subgroup #source(217)$D' < D$ to $D$ is zero on a module on
  which $D$ acts trivially, we have
  $sum_(D' < D) (k G)_(D')^D subset.eq J(k G)$. It now follows from
  Lemma~@lem:brauer-decomposition[(ii)] that every idempotent in $Z(k G)$ lies
  in $k C_G (D)$. If $C_G (D) <= D$ then $C_G (D)$ is a $p$-group, and so
  $k C_G (D)$ has only the identity as an idempotent, and hence $k G$ has only
  one block.
]

#definition[
  We define the *Brauer map*#idx("Brauer", "map")#idx("map", "Brauer")
  $ Br_D : (k G)^D -> k C_G (D) $
  to be the projection onto the first factor in the decomposition given in
  Lemma~@lem:brauer-decomposition[(i)]. Since the second factor in this
  decomposition is a two-sided ideal, this map is a ring homomorphism. Note also
  that by Lemma~@lem:brauer-decomposition[(ii)], the kernel of $Br_D$#idx(
    "$\"Br\"_D$",
  ) on $(k G)^(N_G (D))$ is equal to
  $sum_(D lt.eq.not Q <= N_G (D)) (k G)_Q^(N_G (D))$.
] <def:brauer-map>

In a sense, we are only really interested in the map
$ Br_D : Z(k G) -> Z(k C_G (D)) $
obtained by restricting the above map to $Z(k G) = (k G)^G subset.eq (k G)^D$,
and its effect on idempotents. The point of the extended definition will become
clearer in Lemma~@lem:brauer-transfer.

If $H$ is a subgroup of $G$ with $D C_G (D) <= H <= N_G (D)$ then by the above
proposition, every idempotent in $Z(k H)$ lies in $k C_G (D)$. Let $e in Z(k H)$
be a primitive idempotent corresponding to a block $b$ of $k H$, and
$1 = e_1 + dots.c + e_s$ be a decomposition of 1 as a sum of primitive
orthogonal idempotents in $Z(k G)$ corresponding to the block decomposition
$k G = B_1 + dots.c + B_s$. Then in $Z(k H)$ we have
$
  e = e.Br_D (1) = e.Br_D (e_1) + dots.c
  + e.Br_D (e_s).
$
Since $e$ is primitive, we have $e = e.Br_D (e_i)$ for some $i$, and
$e.Br_D (e_j) = 0$ for $j != i$. We define the Brauer correspondent $b^G$#idx(
  "$b^G$",
) of $b$ to be the block $B_i$ of $k G$. In general, the Brauer correspondence
is not a one–one correspondence, but in case $H = N_G (D)$, Brauer's first main
theorem, which we prove next, states that it is a one-one correspondence between
blocks with defect group $D$.

#lemma[
  A block idempotent $e in Z(k G)$ has defect group $D$ if and only if
  $e in (k G)_D^G$ and $Br_D (e) != 0$.
] <lem:defect-group-brauer-map>

#proof[
  By Proposition~@prop:defect-group-transfer, $e$ has defect group $D$ if and
  only if $e in (k G)_D^G$ and $e in.not (k G)_(D')^G$ for $D' < D$. By
  Rosenberg's Lemma~@lem:rosenberg, the latter condition is equivalent to
  $e in.not sum_(D' < D) (k G)_(D')^G$. The lemma now follows from the fact that
  the kernel of $Br_D$ on $(k G)_D^G$ is $sum_(D' < D) (k G)_(D')^G$.
]

#lemma[
  #source(218)We have a commutative diagram
  $ #brauer-transfer-square $
  in which the bottom map is surjective. Note that we have
  $(k G)_D^G subset.eq (k G)^G = Z(k G)$ and
  $k C_G (D)_D^(N_G (D)) subset.eq Z(k C_G (D))$.
] <lem:brauer-transfer>

#proof[
  By Lemma~@lem:transfer-properties[(iv)], for $x in (k G)^D$ we have
  $
    Br_D (Tr_(D, G) (x))
    = Br_D (sum_(N_G (D) g D)
      Tr_(N_G (D) inter lconj(g, D), N_G (D)) (lconj(g, x)))
    = Br_D (Tr_(D, N_G (D)) (x))
  $
  since the Brauer map is defined in such a way that it vanishes on the
  remaining terms. Comparing parts (i) and (ii) of
  Lemma~@lem:brauer-decomposition, we see that $Br_D$ commutes with
  $Tr_(D, N_G (D))$, and so the above diagram commutes. Since the top and right
  hand maps are surjective, it follows that the bottom map is also surjective.
]

#theorem(title: [Brauer's first main theorem])[
  The map $Br_D$ establishes a one–one correspondence, called the *Brauer
  correspondence*#idx("Brauer", "correspondence")#idx(
    "correspondence",
    "Brauer",
  ), between block idempotents in $Z(k G)$ with defect group $D$ and block
  idempotents in $Z(k N_G (D))$ with defect group $D$. If $b$ is a block of
  $k N_G (D)$ with defect group $D$ then $b^G$ is the corresponding block of
  $k G$ with defect group $D$.
] <th:brauer-first-main>
#idx(
  "Brauer's",
  "first main theorem",
  target: [@th:brauer-first-main],
)#idx(
  "first main theorem, Brauer's",
  target: [@th:brauer-first-main],
)#idx("theorem", "Brauer's", "first main", target: [@th:brauer-first-main])

#proof[
  By Lemma~@lem:defect-group-brauer-map, a block idempotent $e in Z(k G)$ has
  defect group $D$ if and only if $e in (k G)_D^G$ and $Br_D (e) != 0$. By
  Lemma~@lem:brauer-transfer, the map
  $Br_D : (k G)_D^G -> k C_G (D)_D^(N_G (D))$ is onto, and by
  Proposition~@prop:normal-p-subgroup-idempotents, every block idempotent in
  $Z(k N_G (D))$ with defect group $D$ lies in $k C_G (D)_D^(N_G (D))$.
]

Brauer's first main theorem allows us to extend the above notation $b^G$ as
follows. If $D C_G (D) <= H <= G$ (but $H$ not necessarily contained in
$N_G (D)$) and $b$ is a block of $H$ with defect group $D$, then by the first
main theorem, there is a unique block $b'$ of $N_H (D)$ with $(b')^H = b$. We
then write $b^G$ for the block $(b')^G$. It is easy to see that if $H <= K <= G$
then $(b^K)^G = b^G$.

Another way to view the Brauer correspondence, due to Alperin, is as follows.

#lemma[
  Suppose $D C_G (D) <= H <= G$ and $b$ is a block of $k H$ with defect group
  $D$. Then $b^G$ is the unique block $B$ of $k G$ such that $b$ is a summand of
  the restriction $B down_(H times H)$ as a $k(H times H)$-module.
] <lem:alperin-brauer-correspondence>

#proof[
  We first show that $k G$ has a unique block $B$ with $b$ a summand of
  $B down_(H times H)$. As in Proposition~@prop:defect-group-sylow-intersection,
  we have
  $
    k G down_(H times H) = k_(Delta(G)) up^(G times G) down_(H times H) =
    plus.o.big_((1, g) in H times H backslash G times G slash Delta(G))
    k_((H times H) inter lconj((1, g), Delta(G))) up^(H times H)
  $
  #source(219)and
  $
    (H times H) inter lconj((1, g), Delta(G)) =
    lconj((1, g), Delta(H inter lconj(g^(-1), H))).
  $
  If $lconj((1, g), Delta(H inter lconj(g^(-1), H)))
  >= lconj((h_1, h_2), Delta(D))$ then for $x in D$ we have
  $h_1 x h_1^(-1) = g^(-1) h_2 x h_2^(-1) g$ and so
  $h_2^(-1) g h_1 in C_G (D) <= H$ and so $g in H$. It follows that for
  $g in.not H$, no summand
  $k_((H times H) inter lconj((1, g), Delta(G))) up^(H times H)$ has vertex
  containing $Delta(D)$. The identity double coset corresponds to the summand
  $k H$, and so $k G down_(H times H)$ has only one summand isomorphic to $b$.
  It follows that there is a unique block of $k G$ whose restriction to
  $H times H$ has a summand isomorphic to $b$.

  To prove that this summand is $b^G$, we argue as follows. It suffices to prove
  this in case $H <= N_G (D)$, since applying this case twice yields the general
  case. But in this case, if $B$ is a summand of $k G$ such that $b$ is not a
  summand of $B down_(H times H)$, and $e$ and $e'$ are the central idempotents
  in $k H$ and $k G$ corresponding to $b$ and $B$ respectively, then the
  projection of $e e'$ onto $k H$ as a summand of $k G$ is zero, so
  $e Br_D (e') = Br_D (e e') = 0$ and $B != b^G$.
]
