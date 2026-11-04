#import "main-defs.typ": *
#import "statements.typ": *

== Stable elements <sec:stable-elements>

In Section~@sec:relative-projectivity (Corollary~@cor:restriction-injective), we
saw that if $|G : H|$ is invertible in $R$ then
$res_(G, H) : Ext^n_(R G) (M, M') -> Ext^n_(R H) (M, M')$ is injective. More
generally (cf. Corollary~@cor:index-invertible) we shall see in this section
that if $M$ or $M'$ is projective relative to $H$ then the above map
$res_(G, H)$ is injective, and we identify the image as the *stable
elements*#idx("stable", "elements") in $Ext^n_(R H) (M, M')$.

#definition[
  If $H$ is a subgroup of $G$ and $M$, $M'$ are $R G$-modules, an element
  $alpha$ of $Ext^n_(R H) (M, M')$ is said to be *stable*#idx(
    "element",
    "stable",
  ) with respect to $G$ if for all $g in G$
  $
    res_(H, H inter lconj(g, H)) (alpha)
    = res_(lconj(g, H), H inter lconj(g, H)) (g alpha).
  $
] <def:stable-element>

#proposition[
  Suppose $H$ is a subgroup of $G$, and $M$, $M'$ are $R G$-modules with either
  $M$ or $M'$ projective relative to $H$. Then the map
  $ res_(G, H) : Ext^n_(R G) (M, M') -> Ext^n_(R H) (M, M') $
  is injective, and its image is the set of stable elements with respect to $G$.
] <prop:stable-elements>

#proof[
  We shall deal with the case where $M'$ is projective relative to $H$; the case
  where $M$ is projective relative to $H$ is similar. Let
  $theta in #source(92)End_(R H) (M')$ with $Tr_(H, G) (theta) = 1$ as in
  Higman's criterion (Proposition~@prop:higman). By
  Lemma~@lem:cohomology-transfer-properties[(ii)], if
  $alpha in Ext^n_(R G) (M, M')$ then
  $ Tr_(H, G) (theta res_(G, H) (alpha)) = Tr_(H, G) (theta) alpha = alpha. $
  This proves that $res_(G, H)$ is injective, since $alpha$ may be recovered
  from $res_(G, H) (alpha)$.

  Conversely, suppose that $beta in Ext^n_(R H) (M, M')$ is stable with respect
  to $G$. Then by Lemma~@lem:cohomology-transfer-properties we have
  $
    res_(G, H) Tr_(H, G) (theta beta)
    & = sum_(H g H) Tr_(H inter lconj(g, H), H)
    res_(lconj(g, H), H inter lconj(g, H)) (g(theta beta)) \
    & = sum_(H g H) Tr_(H inter lconj(g, H), H)
    (res_(lconj(g, H), H inter lconj(g, H)) (g(theta))
      res_(lconj(g, H), H inter lconj(g, H)) (g(beta))) \
    & = sum_(H g H) Tr_(H inter lconj(g, H), H)
    (res_(lconj(g, H), H inter lconj(g, H)) (g(theta))
      res_(H, H inter lconj(g, H)) (beta)) \
    & = scaled(
      (sum_(H g H) Tr_(H inter lconj(g, H), H)
        res_(lconj(g, H), H inter lconj(g, H)) (g(theta)))
    ) beta
    = Tr_(H, G) (theta) . beta = beta
  $
  and so $beta$ is in the image of $res_(G, H)$.
]

Of course, the same description may be applied to $H^n (G, M)$ since this is
just $Ext^n_(R G) (R, M)$.

#definition[
  A subgroup $H$ of $G$ is said to *control $p$-fusion*#idx(
    "control of $p$-fusion",
  )#idx("fusion, control of")#idx("$p$-fusion, control of") in $G$ if it
  contains a Sylow#idx("subgroups", "Sylow")#idx("Sylow subgroups") $p$-subgroup
  of $G$, and whenever $K_1$ and $K_2$ are $p$-subgroups of $H$ and
  $lconj(g, K_1) = K_2$ for some $g in G$ then there is an $h in H$ with
  $g k_1 g^(-1) = h k_1 h^(-1)$ for all $k_1 in K_1$.
] <def:control-fusion>

#proposition[
  If $H$ controls $p$-fusion in $G$, and the $p'$ part of $|G|$ is invertible in
  $R$, then the restriction map
  $ res_(G, H) : H^n (G, R) -> H^n (H, R) $
  is an isomorphism.
] <prop:control-fusion-isomorphism>

#proof[
  Let $S$ be a Sylow $p$-subgroup of $G$. We must show that if we calculate
  $H^n (G, R)$ or $H^n (H, R)$ as stable elements in $H^n (S, R)$ we get the
  same result in both cases.

  If $g in G$, let $K_1 = lconj(g^(-1), S) inter S$ and
  $K_2 = S inter lconj(g, S)$. Then $lconj(g, K_1) = K_2$, so there is an
  element $h in H$ with $g k_1 g^(-1) = h k_1 h^(-1)$ for all $k_1 in K_1$. In
  particular $h^(-1) g$ centralises $K_1$, and so if $alpha in H^n (K_1, R)$
  then $g alpha = h alpha in H^n (K_2, R)$ so that the stable element
  calculations do give the same answer.
]

#remark[
  The above proof does not work for the restriction map from
  $Ext^n_(R G) (M_1, M_2)$ to $Ext^n_(R H) (M_1, M_2)$ if $M_1$ and $M_2$ are
  non-trivial. The problem is that $C_G (K_1)$ does not necessarily act
  trivially on $Ext^n_(R K_1) (M_1, M_2)$.
]
