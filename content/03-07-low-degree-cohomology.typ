#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-07-low-degree-cohomology.typ": (
  green-lifting, maranda-lifting,
)

== Low degree cohomology <sec:low-degree-cohomology>
#idx("low degree cohomology", target: [@sec:low-degree-cohomology])#idx(
  "cohomology",
  "low degree",
  target: [@sec:low-degree-cohomology],
)

We first give a group theoretic interpretation of
$ H^n (G, M) tilde.equiv Ext_(R G)^n (R, M) tilde.equiv Ext_(ZZ G)^n (ZZ, M) $
for an $R G$-module $M$, for $n = 1$ and 2. Such group theoretic interpretations
have been given for all $n$, but soon become contrived. The real home for
cohomology of groups is in module theory.

#definition[
  An *extension*#idx("extension", "of groups")#idx("group", "extension of") of a
  group $G$ by an $R G$-module $M$ is a short exact sequence of groups
  $ 1 -> M -> hat(G) -> G -> 1 $
  where $M$ is regarded as an abelian group (now written multiplicatively) and
  the action of $G$ on $M$ by conjugation is the same as the module action. A
  *central extension*#idx("central", "extension")#idx("extension", "central") of
  $G$ is as above but with trivial $G$-action on $M$. The extension
  *splits*#idx("split extension")#idx("extension", "split") if there is a copy
  of $G$ complementary to $M$ in $hat(G)$. In this case the group $hat(G)$ may
  be written as matrices of the form $mat(1, 0; m, g)$.

  An *isomorphism of extensions*#idx("isomorphism", "of extensions")#idx(
    "extension",
    "isomorphism of",
  ) must be the identity on both $M$ and $G$.
] <def:group-extension>

#proposition[
  The cohomology group $H^1 (G, M)$#idx("cohomology", "degree one") parametrises
  the set of conjugacy classes of complements#idx(
    "complements, conjugacy classes of",
  )#idx("conjugacy classes", "of complements") to the subgroup $M$ in the split
  extension $hat(G)$.
] <prop:complements-first-cohomology>

#proof[
  We write elements of $hat(G)$ as matrices as above. Then a complementary copy
  of $G$ in $hat(G)$ is given by matrices $mat(1, 0; beta[g], g)$. Since
  $
    mat(1, 0; beta[g_1], g_1) mat(1, 0; beta[g_2], g_2)
    = mat(1, 0; beta[g_1 g_2], g_1 g_2)
  $
  we have $beta[g_1] + g_1 beta[g_2] = beta[g_1 g_2]$ and so $beta : G -> M$ is
  a 1-cocycle for the bar resolution. Conjugating by $mat(1, 0; m, g')$ replaces
  $beta$ by $beta'$ where
  $ beta'[g] - beta[g] = (1 - g)(m - beta[g']) $
  which is the coboundary of the 0-cochain $[space] |-> m - beta[g']$.
]

In terms of extensions, there is an obvious action of $hat(G)$ on
$hat(M) = R plus.o M$ given by
$ mat(1, 0; m_1, g) mat(n; m_2) = mat(n; n m_1 + g(m_2)). $
The above calculation shows that two complementary copies of $G$ in $hat(G)$ are
conjugate if and only if the restrictions of the short exact sequence
$0 -> M -> hat(M) -> R -> 0$ correspond to the same element of
$Ext_(R G)^1 (R, M)$.

#subhead[Degree two cohomology]#idx("cohomology", "degree two")

#proposition[
  #source(88)The cohomology group $H^2 (G, M)$ parametrises the set of
  isomorphism classes of extensions of $G$ by the $R G$-module $M$.
] <prop:extensions-second-cohomology>

#proof[
  If $1 -> M -> hat(G) -> G -> 1$ is an extension, choose a set of coset
  representatives of $M$ in $hat(G)$, and write $hat(g)$ for the representative
  corresponding to an element $g in G$. Define a function
  $alpha : G times G -> M$ by
  $ hat(g)_1 hat(g)_2 = alpha[g_1|g_2] hat(g_1 g_2). $
  Because of the associative law in $hat(G)$, we have
  $
    alpha[g_1|g_2] + alpha[g_1 g_2|g_3] = g_1 alpha[g_2|g_3]
    + alpha[g_1|g_2 g_3]
  $
  (recall that addition in $M$ is really multiplication in $hat(G)$, and the
  action of $G$ on $M$ corresponds to conjugation in $hat(G)$) so that
  $delta alpha[g_1|g_2|g_3] = 0$, and $alpha$ is a 2-cocycle for the bar
  resolution. Choosing new coset representatives $tilde(g) = beta[g] hat(g)$
  replaces $alpha[g_1|g_2]$ by
  $ alpha[g_1|g_2] + beta[g_1] + g_1 beta[g_2] - beta[g_1 g_2]. $
  In other words it changes $alpha$ by the coboundary of the 1-cochain $beta$.

  Conversely given a 2-cocycle $alpha$, we can define an extension $hat(G)$ by
  putting a multiplication on the set of pairs $m in M$, $g in G$ as follows:
  $
    (m_1, g_1)(m_2, g_2) = (m_1 + g_1 (m_2) + alpha[g_1|g_2], g_1 g_2).
  $
  As above, the associative law corresponds to the equation $delta alpha = 0$.
]

If you like thinking in terms of matrices, suppose
$ 0 -> M -> A -> B -> R -> 0 $
represents an element of $H^2 (G, M) tilde.equiv Ext_(R G)^2 (R, M)$. Letting
$ M' = Coker(M -> A) tilde.equiv Ker(B -> R) $
we can think of $A$ and $B$ as matrices of the form
$
  A : mat(phi.alt_(M') (g), 0; a(g), phi.alt_M (g)) quad
  B : mat(1, 0; b(g), phi.alt_(M') (g)).
$
The group $hat(G)$ then consists of all matrices of the form
$
  mat(
    1, 0, 0;
    b(g), phi.alt_(M') (g), 0;
    *, a(g), phi.alt_M (g)
  )
$
where $*$ takes all possible values in $M = Hom_R (R, M)$. The matrices
$
  mat(
    1, 0, 0;
    0, 1, 0;
    *, 0, 1
  )
$
form a normal subgroup isomorphic to $M$, and the quotient is isomorphic to $G$.

The splitting of the extension corresponds to being able to choose consistent
values $c(g)$ for the entry $*$, preserved by multiplication. This is the
#source(89)same as the Yoneda product of $0 -> M -> A -> M' -> 0$ and
$0 -> M' -> B -> R -> 0$ being the zero element of $Ext_(R G)^2 (R, M)$. The
choice $c(g) + c'(g)$ also works if and only if
$ mat(1, 0; c'(g), phi.alt_M (g)) $
is an extension in $Ext_(R G)^1 (R, M) = H^1 (G, M)$.

#corollary[
  If $|G|$ is invertible in $R$ and $M$ is an $R G$-module then every extension
  of $G$ by $M$ splits.
] <cor:extensions-split>

#proof[
  This follows from Proposition~@prop:extensions-second-cohomology,
  Corollary~@cor:restriction-injective and the fact that
  $ H^2 (G, M) = Ext_(R G)^2 (R, M). $
]

#proposition[
  Let $tilde(G)$ be a central extension of a finite group $G$ by the
  multiplicative group $k^times$ of a field $k$ in which every element has a
  $|G|$th root. Then there is a finite subgroup $hat(G)$ of $tilde(G)$ with
  $tilde(G) = hat(G) . k^times$, and $hat(G) inter k^times$ a cyclic group of
  order prime to $p = char k$. In particular, if $G$ is a $p$-group and $k$ is a
  perfect field, then the extension splits and $tilde(G) = G times k^times$.
] <prop:central-extension-finite>

#proof[
  Since every element of $k$ has a $|G|$th root, the map $k^times -> k^times$
  given by raising to the $|G|$th power is onto, with kernel of order $m$
  dividing $|G|_(p')$. The short exact sequence
  $ 0 -> ZZ slash m -> k^times -> k^times -> 1 $
  (where 1 is the zero group written multiplicatively and $ZZ slash m$ is the
  $|G|$th roots of unity written additively) gives rise to an exact sequence
  $
    dots.c -> H^2 (G, ZZ slash m) -> H^2 (G, k^times) limits(->)^0
    H^2 (G, k^times) -> dots.c
  $
  where the second map is multiplication by $|G|$, and is hence zero by
  Proposition~@prop:transfer-restriction-index. Thus we may choose
  representatives $tilde(g)_i$ in $tilde(G)$ of the elements $g_i$ of $G$ so
  that letting $tilde(g)_i tilde(g)_j = alpha[g_i|g_j] tilde(g_i g_j)$, the
  2-cocycle $alpha$ takes values in the $|G|$th roots of unity. We take $hat(G)$
  to be the group generated by these $tilde(g)_i$, so that
  $hat(G) inter k^times$ is contained in the finite cyclic group of $|G|$th
  roots of unity.
]

#remark(kind: "Remarks")[
  + The example $k = QQ$, $G = ZZ slash 2$,
    $tilde(G) = chevron.l QQ^times, sqrt(2) chevron.r$ shows that the hypothesis
    that every element has a $|G|$th root is necessary.
  + If $alpha : G times G -> k^times$ is a 2-cocycle on $G$, then the *twisted
    group ring*#idx("twisted group ring")#idx("ring", "twisted group")#idx(
      "group",
      "ring",
      "twisted",
    ) $[k G]_alpha$ has basis elements $tilde(g)_i$ for $g_i in G$ and
    multiplication $tilde(g)_i tilde(g)_j = alpha[g_i|g_j] tilde(g_i g_j)$.
    According to the above proposition, if $k$ is algebraically closed there is
    a finite cyclic $p'$-central extension
    $ 1 -> Z -> hat(G) -> G -> 1 $
    and an injective map $Z arrow.hook k^times$ such that $[k G]_alpha$ is the
    summand of $k hat(G)$ on which $Z$ acts as scalars via this map, so that as
    a $k hat(G)$-module we have $[k G]_alpha tilde.equiv epsilon_Z up^(hat(G))$.
]

#corollary[
  #source(90)Suppose that a finite group $G$ acts as algebra automorphisms on
  $End_k (V)$, where $V$ is a finite dimensional vector space over an
  algebraically closed field $k$ of characteristic $p$. Then a finite cyclic
  $p'$-central extension $hat(G)$ of $G$ acts on $V$ in such a way that the
  induced action on $V times.o_k V^* = End_k (V)$ is the given one.
] <cor:projective-action-lift>

#proof[
  Every automorphism of $End_k (V)$ is inner by
  Proposition~@prop:skolem-noether, and so we obtain a map
  $G -> PGL(V) = GL(V) slash k^times$. This gives rise to a central extension
  $tilde(G)$ of $G$ by $k^times$ and a map $tilde(G) -> GL(V)$. By the
  proposition, we may pass down to a finite extension $hat(G)$ of $G$ and a map
  $hat(G) -> GL(V)$, as required.
]

#exercise[
  Show that $Ext_(R G)^1 (R, R)$ is isomorphic to the set $Hom(G, R^+)$ of group
  homomorphisms from $G$ to the additive group of $R$. Note that every such
  homomorphism has the derived group of $G$ in its kernel, and that
  $Hom(G, R^+)$ is an abelian group in an obvious way.
]

#subhead[Lifting theorems] We now give an application of the above
interpretation of degree two cohomology to the problem of lifting
representations.

#theorem(title: [Green])[
  Suppose $(K, cal(O), k)$ is a $p$-modular system (see
  Section~@sec:complete-domain) with $k = cal(O) slash frak(p)$, and $M$ is a
  finitely generated $k G$-module such that $Ext_(k G)^2 (M, M) = 0$. Then there
  is an $cal(O) G$-lattice $hat(M)$ with $hat(M) slash frak(p) tilde.equiv M$.
] <th:green-lifting>
#idx("Green", "'s lifting theorem", target: [@th:green-lifting])#idx(
  "lifting theorem",
  "Green's",
  target: [@th:green-lifting],
)#idx("theorem", "Green's", "lifting", target: [@th:green-lifting])

#proof[
  We prove by induction that $M = M_1$ lifts to an
  $(cal(O) slash frak(p)^i) G$-lattice $M_i$ with
  $M_i slash frak(p)^(i-1) tilde.equiv M_(i-1)$. If such a lift $M_i$ has been
  found, then finding $M_(i+1)$ is the same as finding the diagonal map in the
  following diagram.
  $
    #green-lifting
  $
  The obstruction to finding such a lift lies in
  $ H^2 (G, End_k (M)) = Ext_(k G)^2 (M, M) = 0, $
  and so the diagonal map exists. Such a map gives a representation of $G$ as
  matrices over $cal(O) slash frak(p)^(i+1)$. By completeness of $cal(O)$, we
  now obtain an $cal(O) G$-lattice $hat(M)$ with the desired properties.
]

In general, a representation may lift to $cal(O) slash frak(p)^i$ for $i$
arbitrarily large, and then fail to lift further. For example, the trivial
representation of the cyclic group of order two over $FF_2$ lifts to the matrix
$(2^(i-1) + 1)$ as a representation over $ZZ slash 2^i$, which then fails to
lift to a representation over $ZZ slash 2^(i+1)$. But in a sense, this lift only
failed because we chose the wrong lift from $ZZ slash 2^(i-1)$ to
$ZZ slash 2^i$. The following theorem shows that if we can lift as far as
$ZZ slash p^(2r+1)$, where $p^r$ is the order of the Sylow subgroups#idx(
  "subgroups",
  "Sylow",
)#idx("Sylow subgroups"), then the reduction to $ZZ slash p^(r+1)$ lifts to the
$p$-adics.

The following theorem is essentially due to Maranda#idx(
  "Maranda's theorem",
)#idx("theorem", "Maranda's") [@bib:Maranda1953].

#theorem[
  #source(91)Suppose $G$ is a finite group of order $p^r q$ with $q$ coprime to
  $p$, and $(K, cal(O), k)$ is a $p$-modular system. If $M$ is a finitely
  generated $k G$-module which lifts to a finitely generated
  $cal(O) slash p^a$-free $(cal(O) slash p^a) G$-module $tilde(M)$ with
  $a >= 2r + 1$, then there is a finitely generated $cal(O)$-free
  $cal(O) G$-module $hat(M)$ with
  $hat(M) slash p^(a-r) hat(M) tilde.equiv tilde(M) slash p^(a-r) tilde(M)$.
] <th:maranda>

#proof[
  Suppose $M$ has dimension $n$ over $k$. Since $2(a - r) >= a + 1$, the kernel
  of the map
  $ GL_n (cal(O) slash p^(a+1)) -> GL_n (cal(O) slash p^(a-r)) $
  is an abelian group, isomorphic to
  $End_cal(O) (tilde(M) slash p^(r+1) tilde(M))$. Now consider the following
  diagram of groups and homomorphisms.
  $
    #maranda-lifting
  $
  The obstruction to lifting $G -> GL_n (cal(O) slash p^a)$ to a map
  $G -> GL_n (cal(O) slash p^(a+r+1))$ lies in
  $H^2 (G, End_cal(O) (tilde(M) slash p^(r+1) tilde(M)))$. Since $p^r$ is the
  $p$-part of $|G|$, by Proposition~@prop:transfer-restriction-index,
  multiplication by $p^r$ annihilates this cohomology group. Thus the composite
  $G -> GL_n (cal(O) slash p^a) -> GL_n (cal(O) slash p^(a-r))$ lifts to a map
  $G -> GL_n (cal(O) slash p^(a+1))$. Now proceed by induction and use
  completeness to obtain an appropriate map $G -> GL_n (cal(O))$ lifting the
  given map $G -> GL_n (cal(O) slash p^(a-r))$.
]
