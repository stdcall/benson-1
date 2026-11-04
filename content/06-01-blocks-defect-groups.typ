#import "main-defs.typ": *
#import "statements.typ": *

== Blocks and defect groups <sec:blocks-defect-groups>

Recall from Section~@sec:blocks that a block#idx("block") of $k G$ is an
indecomposable two-sided ideal direct summand. A decomposition of $k G$ into
blocks
$ k G = B_1 plus.o dots.c plus.o B_s $
corresponds to a decomposition of the identity element
$ 1 = e_1 + dots.c + e_s $
as a sum of orthogonal primitive central idempotents#idx(
  "central",
  "idempotent",
)#idx("idempotent", "central")#idx("idempotent", "primitive central")#idx(
  "primitive",
  "central idempotent",
). The correspondence is given by $B_i = e_i.k G$.

Since both $Z(cal(O) G)$ and $Z(k G)$#idx("$Z(k G)$, $Z(cal(O) G)$") have a
basis consisting of the conjugacy class sums in $G$, it follows that reduction
modulo $frak(p)$ is a surjective map $Z(cal(O) G) -> Z(k G)$, and so by
Theorem~@th:idempotent-refinement-p-adic[(iii)], the idempotents $e_i in k G$
may be lifted to orthogonal primitive central idempotents $f_i in cal(O) G$. We
thus have
$ cal(O) G = hat(B)_1 plus.o dots.c plus.o hat(B)_s $
with $hat(B)_i = f_i.cal(O) G$ and $B_i = k times.o_cal(O) hat(B)_i$.

#source(214)Now if $M$ is an indecomposable $k G$-module, the equation
$ M = e_1 M plus.o dots.c plus.o e_s M $
shows that $M = e_i M$ for a unique $i$, and $e_j M = 0$ for $j != i$. Similarly
if $M$ is an indecomposable $cal(O) G$-lattice, then $f_i M = M$ and $f_j M = 0$
for $j != i$. Finally, if $M$ is an irreducible $K G$-module (recall that all
indecomposable $K G$-modules are irreducible by Maschke's theorem) then
$f_i M = M$ for a unique $i$, and $f_j M = 0$ for $j != i$.

We thus think of a block as a sort of receptacle, into which are thrown
indecomposable summands of the algebras $k G$ and $cal(O) G$, primitive
idempotents in $Z(k G)$ and $Z(cal(O) G)$, indecomposable modules for $k G$,
$cal(O) G$ and $K G$, and so on.

Now the two sided ideal direct summands of $R G$ (recall $R in {cal(O), k}$) are
the same as the direct summands of $R G$ as an $R(G times G)$-module, where the
action of $R(G times G)$ on $R G$ is via left and right multiplication
$ (g_1, g_2) : g -> g_1 g g_2^(-1). $
With this action, $R G$ is equal to the permutation module of $R(G times G)$ on
the cosets of the diagonal
$ Delta(G) = {(g, g), g in G} subset.eq G times G. $
In other words, $R G tilde.equiv R_(Delta(G)) up^(G times G)$. It follows that
the $R(G times G)$-module $R G$ is projective relative to $Delta(G)$, and so the
vertices of any indecomposable summand $B = e.R G$ are conjugate to some
subgroup of the form $Delta(D) subset.eq Delta(G)$, where $D$ is a $p$-subgroup
of $G$ determined up to conjugacy by the block $B$. The group $D = D(B)$ is
called the *defect group*#idx("defect", "group")#idx("group", "defect") of the
block $B$. If $|D| = p^a$, we say that $B$ is a block of *defect*#idx("defect")
$a$.

#proposition(title: [J.~A. Green])[
  The defect group $D$ of any block $B$ of $R G$ is expressible as an
  intersection $S inter lconj(g, S)$ of two Sylow $p$-subgroups of $G$.
] <prop:defect-group-sylow-intersection>
#idx(
  "intersection of Sylow subgroups",
  target: [@prop:defect-group-sylow-intersection],
)#idx(
  "Sylow subgroups",
  "intersection of",
  target: [@prop:defect-group-sylow-intersection],
)

#proof[
  By the Mackey decomposition theorem, the restriction of $R G$ to an
  $R(S times S)$-module is
  $
    R_(Delta(G)) up^(G times G) down_(S times S) =
    plus.o.big_((1, g) in S times S backslash G times G slash Delta(G))
    R_((S times S) inter lconj((1, g), Delta(G))) up^(S times S).
  $
  The double coset representatives may be chosen to be of the form $(1, g)$ by
  adjusting by elements of $Delta(G)$. But
  $
    (S times S) inter lconj((1, g), Delta(G)) =
    lconj((1, g), Delta(S inter lconj(g^(-1), S)))
  $
  and so the restriction of $R G$ to $R(S times S)$ is a direct sum of
  permutation modules on cosets of subgroups of the form
  $lconj((1, g), Delta(S inter lconj(g^(-1), S)))$. Each transitive permutation
  module for $S times S$ is indecomposable, since for $R = k$ it has a one
  dimensional socle (see Section~@sec:p-groups). So the vertex of
  $R_(lconj((1, g), Delta(S inter lconj(g^(-1), S)))) up^(S times S)$
  #source(215)is exactly $lconj((1, g), Delta(S inter lconj(g^(-1), S)))$. Since
  $R G$ is projective relative to $S times S$ (Corollary~@cor:index-invertible)
  it follows that each indecomposable summand of $R G$ as an
  $R(G times G)$-module has a subgroup of the form $Delta(S inter lconj(g, S))$
  as a vertex.
]

#proposition(title: [J.~A. Green])[
  Suppose $B = e.R G$ is a block of $R G$ with defect group $D$. Then $e$ lies
  in $R G_(Delta(H))^(Delta(G)) subset.eq Z(R G)$ if and only if $H$ contains a
  conjugate of $D$ (see Definition~@def:transfer for the notation). Furthermore,
  every $R G$-module in the block $B$ is projective relative to $D$.
] <prop:defect-group-transfer>

#proof[
  We have seen that as an $R(G times G)$-module, $B$ is projective relative to
  $Delta(G)$. Thus by Higman's criterion (Proposition~@prop:higman), $H$
  contains a defect group of $B$ if and only if there is a map
  $alpha in End_(R Delta(H)) (R G)$ such that $Tr_(Delta(H), Delta(G)) (alpha)$
  is the identity map on $B = e.R G$. If $alpha$ is such a map then we have
  $
    #aligned-rows(
      (
        $e = (Tr_(Delta(H), Delta(G)) (alpha))(e)$,
        $= sum_((g, g) in Delta(G) slash Delta(H))
        (g, g) alpha((g^(-1), g^(-1))(e))$,
      ),
      (
        $$,
        $= sum_(g in G slash H) g alpha(e) g^(-1)
        = Tr_(Delta(H), Delta(G)) alpha(e)$,
      ),
    )
  $
  and so $e in R G_(Delta(H))^(Delta(G))$. Conversely if
  $e = Tr_(Delta(H), Delta(G)) (a) in R G_(Delta(H))^(Delta(G))$ then we define
  a map $alpha : R G -> R G$ by $alpha(x) = a.x$. Since $a in R G^(Delta(H))$ we
  have $alpha in End_(R Delta(H)) (R G)$, and for $x in e.R G$ we have
  $
    (Tr_(Delta(H), Delta(G)) (alpha))(x)
    & = sum_((g, g) in Delta(G) slash Delta(H))
    (g, g) alpha((g^(-1), g^(-1))(x)) \
    & = sum_(g in G slash H) g.a.g^(-1) x g.g^(-1)
    = (Tr_(Delta(H), Delta(G)) (a)).x = e x = x.
  $

  Finally, if $M$ is an $R G$-module in the block $B$, then $e$ acts as the
  identity on $M$, and so the above element $a = alpha(e)$ acts as an
  endomorphism of $M$ whose transfer is the identity. Again applying Higman's
  criterion, we see that $M$ is projective relative to $D$.
]

#remark[
  In fact there is always an indecomposable module in $B$ whose vertex is
  exactly $D$, as we shall see when we come to discuss Brauer's second main
  theorem in Section~@sec:second-main-theorem.
]

#example[
  The block of $R G$ containing the trivial $R G$-module $R$ is called the
  *principal block*#idx("principal block")#idx("block", "principal"). Since a
  Sylow $p$-subgroup#idx("Sylow subgroups")#idx("subgroups", "Sylow") of $G$ is
  a vertex of the trivial module, it is also a defect group of the principal
  block, by the above proposition. The principal block is usually denoted
  $B_0 = B_0 (G)$#idx("$B_0(G)$").
]

#corollary[
  If $B$ is a block of $k G$ and $hat(B)$ is the corresponding block of
  $cal(O) G$ then $B$ and $hat(B)$ have the same defect groups.
] <cor:defect-groups-lift>

#proof[
  #source(216)If $D$ is a defect group of $B$ then by the proposition the
  corresponding central idempotent $e$ lies in $(k G)_(Delta(D))^(Delta(G))$.
  Thus the central idempotent $hat(e)$ corresponding to $hat(B)$ lies in
  $(cal(O) G)_(Delta(D))^(Delta(G)) + frak(p) Z(cal(O) G)$. So by Rosenberg's
  Lemma~@lem:rosenberg#idx("Rosenberg's lemma")#idx("lemma", "Rosenberg's") we
  have either $hat(e) in (cal(O) G)_(Delta(D))^(Delta(G))$ or
  $hat(e) in frak(p) Z(cal(O) G)$. But
  $frak(p) Z(cal(O) G) subset.eq frak(p) G subset.eq J(cal(O) G)$ so the latter
  is impossible. Conversely if $hat(e) in (cal(O) G)_(Delta(D))^(Delta(G))$ then
  $e in (k G)_(Delta(D))^(Delta(G))$.
]
