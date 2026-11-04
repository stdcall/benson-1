#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-06-relative-projectivity.typ": (
  relative-injective-extension, relative-projective-lifting,
)

== Relative projectivity and transfer <sec:relative-projectivity>

#definition[
  Suppose $H$ is a subgroup of $G$. An $R G$-module $M$ is said to be
  *projective relative to $H$*#idx("projective", "relatively")#idx(
    "relative",
    "projectivity",
  ) or *relatively $H$-projective* if whenever we are given modules $M_1$ and
  $M_2$, a map $lambda : M -> M_1$ and an epimorphism $mu : M_2 -> M_1$ such
  that there exists a map of $R H$-modules $nu : M down_H -> M_2 down_H$ with
  $lambda = mu compose nu$, then there exists a map of $R G$-modules
  $nu' : M -> M_2$ with $lambda = mu compose nu'$.
  $
    #relative-projective-lifting
  $
  If $H = 1$ and $R$ is a field, this agrees with the definition of projective
  $R G$-module given in Section~@sec:projective-injective.

  An $R G$-module $M$ is said to be *injective relative to $H$*#idx(
    "injective",
    "relatively",
  )#idx("relative", "injectivity") or *relatively $H$-injective* if whenever we
  are given modules $M_1$ and $M_2$, a map $lambda : M_1 -> M$ and a
  monomorphism $mu : M_1 -> M_2$ such that there exists a map of $R H$-modules
  $nu : M_2 down_H -> M down_H$ with $lambda = nu compose mu$, then there exists
  a map of $R G$-modules $nu' : M_2 -> M$ with $lambda = nu' compose mu$.
  $
    #relative-injective-extension
  $

  A short exact sequence of $R G$-modules is *$H$-split*#idx("$H$-split") if it
  splits on restriction to $H$.
] <def:relative-projectivity>

The concept of relative projectivity was studied by D.~G. Higman, who related it
to the transfer map as follows:

#definition[
  If $H$ is a subgroup of $G$, and $M$ and $M'$ are $R G$-modules, we define the
  *transfer*#idx("transfer") or *trace map*#idx("trace", "map")#idx("Tr")
  $ Tr_(H, G) : Hom_(R H) (M' down_H, M down_H) -> Hom_(R G) (M', M) $
  as follows. Choose a set ${g_i, i in I}$ of left coset representatives of $H$
  in $G$ and set
  $ Tr_(H, G) (phi.alt)(m) = sum_(i in I) g_i phi.alt(g_i^(-1) m). $
  Since $phi.alt$ is an $R H$-module homomorphism, $g_i phi.alt(g_i^(-1) m)$
  only depends on the left coset $g_i H$ and so this map is independent of
  choice of coset representatives of $H$ in $G$.

  #source(81)In other words, $Tr_(H, G)$ is the composite of the exterior trace
  map
  $
    hat(Tr)_(H, G) : Hom_(R H) (M' down_H, M down_H) stretch(-->)^tilde.equiv
    Hom_(R G) (M', M down_H up^G)
  $
  defined in Section~@sec:induction-restriction-groups and the map induced by
  the natural surjection $M down_H up^G -> M$.

  We write $(M', M)^G$ for $Hom_(R G) (M', M)$, we write $(M', M)_H^G$ for the
  image of $Tr_(H, G)$, and we set
  $ (M', M)^(G, H) = (M', M)^G slash (M', M)_H^G $
  as an $R$-module. Similarly if $cal(X)$ is a collection of subgroups of $G$ we
  write $(M', M)_cal(X)^G$ for the linear span of the $(M', M)_H^G$,
  $H in cal(X)$, and $(M', M)^(G, cal(X))$ for
  $(M', M)^G slash (M', M)_cal(X)^G$.

  In case $M' = R$, $(R, M)^G$ is just the space of fixed points $M^G$. In this
  case we write $M_H^G$ and $M^(G, H)$ for the image and cokernel of
  $Tr_(H, G) : M^H -> M^G$.
] <def:transfer>

#lemma[
  + If $alpha in Hom_(R H) (M_1, M_2)$ and $beta in Hom_(R G) (M_2, M_3)$ then
    $ beta compose Tr_(H, G) (alpha) = Tr_(H, G) (beta compose alpha). $
  + If $alpha in Hom_(R G) (M_1, M_2)$ and $beta in Hom_(R H) (M_2, M_3)$ then
    $ Tr_(H, G) (beta) compose alpha = Tr_(H, G) (beta compose alpha). $
  + If $H <= K <= G$ then $Tr_(K, G) Tr_(H, K) (alpha) = Tr_(H, G) (alpha)$.
  + If $H$ and $K$ are two subgroups of $G$, then for
    $alpha in Hom_(R K) (M_1, M_2)$,
    $Tr_(K, G) (alpha) = sum_(H g K) Tr_(H inter lconj(g, K), H) (g alpha)$.
    Recall that $(g alpha)(m) = g(alpha(g^(-1) m))$.
  + If $alpha in End_(R H) (M)$ and $beta in End_(R K) (M)$, then
    $
      Tr_(H, G) (alpha) Tr_(K, G) (beta)
      = sum_(H g K) Tr_(H inter lconj(g, K), G) (alpha g beta).
    $
  + Suppose $K <= H <= G$, $M_1$ is an $R G$-module, $M_2$ is an $R H$-module
    and $i : M_2 -> M_2 up^G down_H$ is the natural map taking $m$ to
    $1 times.o m$. Then
    $ hat(Tr)_(H, G) Tr_(K, H) (alpha)(m) = Tr_(K, G) (i compose alpha)(m). $
] <lem:transfer-properties>

#proof[
  (i), (ii) and (iii) are clear from the definition.
  #enum.item(4)[For each double coset $H g K$, let $lambda(g)$ be a set of left
    coset representatives of $H inter lconj(g, K)$ in $H$. Then
    $union.big_(H g K) {h g | h in lambda(g)}$ is a set of left coset
    representatives of $K$ in $G$.]
  + We have
    $
      #aligned-rows(
        (
          $Tr_(H, G) (alpha) Tr_(K, G) (beta)$,
          $= Tr_(H, G) (alpha Tr_(K, G) (beta))
          = Tr_(H, G) (sum_(H g K) alpha Tr_(H inter lconj(g, K), H) (g beta))$,
        ),
        (
          $$,
          $= Tr_(H, G) (sum_(H g K) Tr_(H inter lconj(g, K), H) (alpha g beta))
          = sum_(H g K) Tr_(H inter lconj(g, K), G) (alpha g beta).$,
        ),
      )
    $
  + #source(82)We have
    $
      #aligned-rows(
        (
          $hat(Tr)_(H, G) Tr_(K, H) (alpha)(m)$,
          $= sum_(g in G slash H) sum_(h in H slash K)
          g times.o h alpha h^(-1) g^(-1) (m)$,
        ),
        (
          $$,
          $= sum_(g in G slash K) g times.o alpha g^(-1) (m)
          = Tr_(K, G) (i compose alpha)(m).$,
        ),
      )
    $
]

Setting $M = M_1 = M_2 = M_3$ in parts (i) and (ii) of the above lemma, it
follows that $(M, M)_H^G$ is a two-sided ideal in $End_(R G) (M)$, and so the
quotient $(M, M)^(G, H)$ inherits a ring structure. Similarly, $(M, M)_cal(X)^G$
is a two-sided ideal and $(M, M)^(G, cal(X))$ is a ring.

The following two propositions explain the relationship between relative
projectivity and transfer:

#proposition(title: [D.~G. Higman])[
  Let $M$ be an $R G$-module and $H$ a subgroup of $G$. Then the following are
  equivalent:
  + $M$ is projective relative to $H$.
  + Every $H$-split epimorphism of $R G$-modules $lambda : M' -> M$ (i.e., one
    which splits as a map of $R H$-modules) splits.
  + $M$ is injective relative to $H$.
  + Every $H$-split monomorphism of $R G$-modules splits.
  + $M$ is a direct summand of $M down_H up^G$.
  + $M$ is a direct summand of some module induced from $H$.
  + (Higman's criterion#idx("Higman's criterion")#idx(
      "criterion, Higman's",
    )) The identity map on $M$ is in the image of $Tr_(H, G)$.
] <prop:higman>

#proof[
  The implications (i) $=>$ (ii) $=>$ (v) $=>$ (vi) and (iii) $=>$ (iv) $=>$ (v)
  are clear, using the natural $H$-split maps $M arrow.hook M down_H up^G$ and
  $M down_H up^G arrow.twohead M$.

  (vi) $=>$ (vii): If $M$ is a direct summand of $N up^G$ for an $R H$-module
  $N$ then we denote by $rho$ the $R H$-module endomorphism
  $N up^G down_H -> N up^G down_H$ given by
  $
    rho(g times.o n) = cases(
      g times.o n & quad "if" g in H,
      0 & quad "otherwise"
    )
  $
  i.e., the projection onto $N$ as a summand of $N up^G down_H$ (cf. the Mackey
  decomposition theorem). Then we have $Tr_(H, G) (rho) = 1$, the identity
  endomorphism of $N up^G$.

  Now we denote by $theta$ the $R H$-module endomorphism of $M$ given by the
  composite
  $
    theta : M down_H arrow.hook N up^G down_H limits(->)^rho N up^G down_H
    arrow.twohead M down_H.
  $
  By Lemma~@lem:transfer-properties[(i)] and (ii), we have
  $Tr_(H, G) (theta) = 1$.

  #source(83)\(vii) $=>$ (i): Let
  $
    #relative-projective-lifting
  $
  be as in the definition of relative projectivity. If $theta in End_(R H) (M)$
  with $Tr_(H, G) (theta) = 1$ then we let $nu' = Tr_(H, G) (nu compose theta)$.
  By Lemma~@lem:transfer-properties[(i)] and (ii) we have
  $
    mu compose nu' & = mu compose Tr_(H, G) (nu compose theta)
                     = Tr_(H, G) (mu compose nu compose theta) \
                   & = Tr_(H, G) (lambda compose theta)
                     = lambda compose Tr_(H, G) (theta) = lambda.
  $
  (vii) $=>$ (iii) is proved dually.
]

#corollary[
  Suppose an $R G$-module $M$ is projective as an $R$-module and has a finite
  projective resolution as an $R G$-module. Then $M$ is projective as an
  $R G$-module.
] <cor:finite-resolution-projective>

#proof[
  Let
  $ 0 -> P_n -> P_(n-1) -> dots.c -> P_0 -> M -> 0 $
  be a projective resolution of $M$ with $n$ minimal. Since $M$ is
  $R$-projective, this sequence is $R$-split. By Proposition~@prop:higman, $P_n$
  is injective relative to the trivial subgroup, and so the map $P_n -> P_(n-1)$
  splits, contradicting the minimality of $n$ unless $n = 0$.
]

#proposition[
  Suppose $M_1$ and $M_2$ are $R G$-modules, $H$ is a subgroup of $G$ and
  $alpha in Hom_(R G) (M_1, M_2)$. Then the following are equivalent.
  + $alpha in (M_1, M_2)_H^G$.
  + $alpha$ factors as $M_1 -> M_2 down_H up^G -> M_2$ where the latter map is
    the natural surjection $M_2 down_H up^G -> M_2$.
  + $alpha$ factors as
    $M_1 limits(arrow.r.long)^(alpha_1) M limits(arrow.r.long)^(alpha_2) M_2$
    for some $M$ projective relative to $H$.
] <prop:transfer-image-factors>

#proof[
  (i) $=>$ (ii): This follows from the fact that $Tr_(H, G)$ is the composite of
  $hat(Tr)_(H, G)$ and the map induced by $M_2 down_H up^G -> M_2$.

  (ii) $=>$ (iii) is clear.

  (iii) $=>$ (i): Write $id_M = Tr_(H, G) (theta)$ as in the previous
  proposition. If $alpha = alpha_2 compose alpha_1$ then
  $
    alpha = alpha_2 compose Tr_(H, G) (theta) compose alpha_1
    = Tr_(H, G) (alpha_2 compose theta compose alpha_1) in (M_1, M_2)_H^G
  $
  by Lemma~@lem:transfer-properties[(i)] and (ii).
]

#corollary[
  If $M$ and $N$ are $R G$-modules with $M$ relatively $H$-projective, then
  $M times.o_R N$ is also relatively $H$-projective.
] <cor:tensor-relatively-projective>

#proof[
  This follows from the Proposition~@prop:higman, using the identity
  $
    M down_H up^G times.o_R N tilde.equiv
    (M down_H times.o_R N down_H) up^G
  $
  (Proposition~@prop:induced-tensor-hom).
]

#corollary[
  #source(84)If $M$ and $N$ are $R G$-modules with $M$ relatively $H$-projective
  and $N$ relatively $K$-projective, then $M times.o_R N$ is a summand of a sum
  of modules which are projective relative to subgroups of the form
  $H inter lconj(g, K)$.
] <cor:tensor-relative-intersections>

#proof[
  This follows in the same way, using Corollary~@cor:mackey-products[(i)].
]

#corollary[
  Suppose $|G : H|$ is invertible in $R$. Then every $R G$-module $M$ is
  projective relative to $H$.
] <cor:index-invertible>

#proof[
  $Tr_(H, G) (id_M slash abs(G : H)) = id_M$.
]

#corollary(closed: true)[
  Suppose $R$ is a field of characteristic $p$ or a commutative local ring whose
  residue class field has characteristic $p$. Suppose $H$ contains a Sylow
  $p$-subgroup#idx("subgroups", "Sylow")#idx("Sylow subgroups") of $G$. Then
  every $R G$-module is projective relative to $H$.
] <cor:sylow-relatively-projective>

#corollary(closed: true)[
  Suppose $|G|$ is invertible in $R$. Then every $R G$-module which is
  projective as an $R$-module is projective as an $R G$-module. In particular
  every short exact sequence of such modules splits.
] <cor:order-invertible>

#corollary(title: [Maschke's theorem], closed: true)[
  Suppose $k$ is a field of characteristic coprime to $|G|$. Then every short
  exact sequence of $k G$-modules splits. In particular $k G$ is semisimple#idx(
    "ring",
    "semisimple",
  )#idx("semisimple", "ring").
] <cor:maschke>
#idx("Maschke's theorem", target: [@cor:maschke])#idx(
  "theorem",
  "Maschke's",
  target: [@cor:maschke],
)

#remark[
  The usual proof of Maschke's theorem is as follows. If $M_1$ is a submodule of
  a $k G$-module $M$ and if $rho$ is any linear projection of $M$ onto $M_1$
  then $rho' = (1 slash abs(G)) sum_(g in G) g rho g^(-1)$ is a $G$-invariant
  projection and so $M = M_1 plus.o Ker(rho')$. This is in a sense the prototype
  for the proof of Higman's criterion.
]

#definition[
  If $X$ is a permutation representation of $G$, we write $R X$ for the
  corresponding matrix representation whose basis elements are the elements of
  $X$, and we say a short exact sequence $0 -> M_1 -> M_2 -> M_3 -> 0$ is
  $X$-split if the sequence
  $ 0 -> R X times.o_R M_1 -> R X times.o_R M_2 -> R X times.o_R M_3 -> 0 $
  splits.

  We say that $M$ is projective relative to $X$, or relatively $X$-projective,
  if every $X$-split epimorphism $M' -> M -> 0$ splits.
] <def:permutation-split>

The following two lemmas show that these concepts are equivalent to those
introduced in Definition~@def:relative-projectivity, but better behaved on
restriction to subgroups.

#lemma(closed: true)[
  Suppose $X$ is a transitive permutation representation of $G$ with point
  stabiliser $H$. Then a short exact sequence of $R G$-modules is $X$-split if
  and only if it is $H$-split. An $R G$-module $M$ is relatively $X$-projective
  if and only if it is relatively $H$-projective.
] <lem:transitive-permutation-split>

#lemma(closed: true)[
  Suppose $X$ is a permutation representation of $G$ and $H$ is a subgroup of
  $G$.
  + #source(85)If a short exact sequence of $R G$-modules is $X$-split then its
    restriction to $H$ is also $X$-split.
  + If an $R G$-module $M$ is relatively $X$-projective then $M down_H$ is also
    relatively $X$-projective.
] <lem:permutation-split-restriction>

#subhead[Transfer in cohomology]#idx("cohomology", "transfer in")#idx(
  "transfer",
  "in cohomology",
) We can extend the notion of transfer from Hom to Ext as follows. First note
that projective $R G$-modules are still projective as $R H$-modules for
$H <= G$. So a projective resolution of $M$ as an $R G$-module gives us a
projective resolution of $M$ as an $R H$-module. Thus we obtain a restriction
map#idx("restriction", "in cohomology")
$ res_(G, H) : Ext_(R G)^n (M, M') -> Ext_(R H)^n (M, M'). $

If
$ dots.c -> P_2 stretch(-->)^(partial_2) P_1 stretch(-->)^(partial_1) P_0 $
is a projective resolution of an $R G$-module $M$, and $M'$ is another
$R G$-module then for any $alpha in Hom_(R H) (P_n, M')$ we have
$Tr_(H, G) (alpha) compose partial_(n+1)
= Tr_(H, G) (alpha compose partial_(n+1))$
by Lemma~@lem:transfer-properties. Thus $Tr_(H, G)$ induces a well defined map
$ Tr_(H, G) : Ext_(R H)^n (M, M') -> Ext_(R G)^n (M, M'). $
It is easy to check that this is independent of the choice of the resolution.

#lemma[
  + If $alpha in Ext_(R H)^m (M_1, M_2)$ and $beta in Ext_(R G)^n (M_2, M_3)$
    then
    $
      beta compose Tr_(H, G) (alpha)
      = Tr_(H, G) (res_(G, H) (beta) compose alpha)
      in Ext_(R G)^(m+n) (M_1, M_3).
    $
  + If $alpha in Ext_(R G)^m (M_1, M_2)$ and $beta in Ext_(R H)^n (M_2, M_3)$
    then
    $
      Tr_(H, G) (beta) compose alpha
      = Tr_(H, G) (beta compose res_(G, H) (alpha)).
    $
  + If $H <= K <= G$ then $Tr_(K, G) Tr_(H, K) (alpha) = Tr_(H, G) (alpha)$.
  + (Mackey formula#idx("Mackey", "formula")) If $H$, $K <= G$, then for
    $alpha in Ext_(R K)^n (M_1, M_2)$ we have
    $
      res_(G, H) Tr_(K, G) (alpha) = sum_(H g K) Tr_(H inter lconj(g, K), H)
      res_(lconj(g, K), H inter lconj(g, K)) (g alpha).
    $
  + If $alpha in Ext_(R H)^m (M, M)$ and $beta in Ext_(R K)^n (M, M)$, then
    $
      Tr_(H, G) (alpha) Tr_(K, G) (beta)
      = sum_(H g K) Tr_(H inter lconj(g, K), G) (alpha g beta).
    $
] <lem:cohomology-transfer-properties>

#proof[
  This is clear from Lemma~@lem:transfer-properties.
]

#proposition(closed: true)[
  If $alpha in Ext_(R G)^n (M, M')$ then
  $Tr_(H, G) res_(G, H) (alpha) = abs(G : H) . alpha$. In particular if $M$ is
  $R$-projective then for any $alpha in Ext_(R G)^n (M, M')$ with $n > 0$, we
  have $abs(G) . alpha = 0$.
] <prop:transfer-restriction-index>

#corollary(closed: true)[
  If $|G : H|$ is invertible in $R$ then the restriction map
  $ res_(G, H) : Ext_(R G)^n (M, M') -> Ext_(R H)^n (M, M') $
  is injective. In particular, if $|G|$ is invertible in $R$ and $M$ is
  $R$-projective, then $Ext_(R G)^n (M, M') = 0$ for $n > 0$.
] <cor:restriction-injective>

#corollary[
  #source(86)Suppose a Sylow $p$-subgroup $P$ of $G$ is a T.I. set#idx(
    "Sylow subgroups",
    "T.I.",
  )#idx("T.I. set") (i.e., for all $g in G$ we have either $lconj(g, P) = P$ or
  $lconj(g, P) inter P = {1}$), and suppose $|G : P|$ is invertible in $R$ and
  $M$ is $R$-projective. Then the restriction map
  $ res_(G, N_G (P)) : Ext_(R G)^n (M, M') -> Ext_(R N_G (P))^n (M, M') $
  is an isomorphism, and multiplication by $|G : N_G (P)| - 1$ annihilates every
  element of $Ext_(R G)^n (M, M')$, for $n > 0$. Moreover,
  $Ext_(R N_G (P))^n (M, M')$ is equal to the invariants of $N_G (P) slash P$
  acting on $Ext_(R P)^n (M, M')$.
] <cor:ti-sylow>

#proof[
  As above, $Tr_(N_G (P), G) res_(G, N_G (P)) (alpha) = abs(G : N_G (P)) alpha$,
  so that $res_(G, N_G (P))$ is injective. But on the other hand, the Mackey
  formula~@lem:cohomology-transfer-properties[(iv)] shows that
  $ res_(G, N_G (P)) Tr_(N_G (P), G) (beta) = beta $
  since the intersection of any two distinct conjugates of $N_G (P)$ is a group
  of order dividing $|G : P|$. Hence $res_(G, N_G (P))$ and $Tr_(N_G (P), G)$
  are inverse isomorphisms, and $abs(G : N_G (P)) alpha = alpha$.

  Finally, the Mackey formula shows that if $alpha in Ext_(R P)^n (M, M')$ then
  $
    res_(N_G (P), P) Tr_(P, N_G (P)) (alpha) = sum_(g in N_G (P) slash P)
    g alpha.
  $
  Since $|N_G (P) slash P|$ is invertible in $R$, the image of
  $sum_(g in N_G (P) slash P) g$ is equal to the invariants.
]

#example[
  Suppose $G = cal(S)_p$, the symmetric group on $p$ letters#idx(
    "group",
    "symmetric",
    "$cal(S)_p$",
  )#idx("symmetric", "group $cal(S)_p$"), for $p$ odd, and $k$ is a field of
  characteristic $p$. A Sylow $p$-subgroup $P$ of $G$ is a cyclic group of order
  $p$, whose normaliser is a Frobenius group of order $p(p - 1)$#idx(
    "Frobenius",
    "group of order $p(p - 1)$",
  )#idx("group", "Frobenius, of order $p(p - 1)$")
  $
    N_G (P) = chevron.l g, h | g^p = 1, h^(p-1) = 1, h g h^(-1) = g^s
    chevron.r
  $
  where $s$ is a primitive root modulo $p$. Now by
  Proposition~@prop:cyclic-cohomology-ring, we have
  $ H^* (P, k) = k[x, y] slash (x^2) $
  with $deg(x) = 1$ and $deg(y) = 2$. It is easy to check that the action of
  $N_G (P)$ on $H^* (P, k)$ is given by $h : x |-> s x$, $h : y |-> s y$ (for
  example, use the explicit description of degree one and degree two cohomology
  given in Section~@sec:low-degree-cohomology).

  Now by Corollary~@cor:ti-sylow, it follows that
  $
    H^* (cal(S)_p, k) tilde.equiv H^* (N_G (P), k)
    tilde.equiv H^* (P, k)^(N_G (P) slash P).
  $
  Since $h : y^n |-> s^n y^n$ and $h : x y^(n-1) |-> s^n x y^(n-1)$, it follows
  that the invariants have a basis consisting of the elements of the form
  $y^(k(p-1))$ and $x y^(k(p-1)-1)$. These elements therefore form a basis for
  $H^* (cal(S)_p, k)$.

  Similarly, if $epsilon$ denotes the sign representation of $cal(S)_p$, then
  $epsilon down_P = k down_P$, so $H^* (P, epsilon)$ is as before. However, as
  modules for $N_G (P) slash P$ we have
  $H^* (P, epsilon) = H^* (P, k) times.o_k epsilon$. Since $h$ is an odd element
  of $cal(S)_p$, it acts as $-1 = s^((p-1) slash 2)$ on $epsilon$. Thus we have
  $h : y^n |-> s^((p-1) slash 2 + n) y^n$ and
  $h : x y^(n-1) |-> s^((p-1) slash 2 + n) x y^(n-1)$, and so
  $
    H^* (cal(S)_p, epsilon) tilde.equiv H^* (N_G (P), epsilon) tilde.equiv
    [H^* (P, k) times.o_k epsilon]^(N_G (P) slash P)
  $
  #source(87)has a basis consisting of the elements of the form
  $ y^((2k+1)(p-1) slash 2) quad "and" quad x y^((2k+1)(p-1) slash 2 - 1). $
]
