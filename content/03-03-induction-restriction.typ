#import "main-defs.typ": *
#import "statements.typ": *

== Induction and restriction <sec:induction-restriction-groups>

Let $G$ be a finite group. If $H <= G$, then $R H$ is a subring of $R G$, and so
by Section~@sec:induction-restriction if $M$ is an $R G$-module we can restrict
it to an $R H$-module which we write as $M down_H$. If $N$ is an $R H$-module we
have the induced $R G$-module $N up^G = R G times.o_(R H) N$. Since $R G$ is
free as a right $R H$-module, of rank $|G : H|$, we can write
$N up^G = plus.o.big_(g_i in G slash H) g_i times.o N$ as a sum of $R$-modules,
where the sum runs over a set of coset representatives of $H$ in $G$. The action
of $G$ is given by $g(g_i times.o n) = g_j times.o h n$, where $g_j$ is the
coset representative with $g g_i = g_j h$ and $h in H$.

Since $R G tilde.equiv (R G)^* = Hom_R (R G, R)$ as $R G$-$R G$-bimodules,
induction and restriction behave well under duality in the sense that we have
$(M^*) down_H tilde.equiv (M down_H)^*$ and $(N^*) up^G tilde.equiv (N up^G)^*$.
It also follows that induction and co-induction coincide since
$
  N up^G = R G times.o_(R H) N tilde.equiv (R G)^* times.o_(R H) N
  tilde.equiv Hom_(R H) (R G, N) = N Up^G.
$

#proposition(title: [Nakayama relations])[
  #part-lines[
    + $Hom_(R H) (N, M down_H) tilde.equiv Hom_(R G) (N up^G, M)$
    + $Hom_(R H) (M down_H, N) tilde.equiv Hom_(R G) (M, N up^G)$.
  ]
] <prop:nakayama-relations-groups>
#idx("Nakayama", "relations", target: [@prop:nakayama-relations-groups])#idx(
  "relations",
  "Nakayama",
  target: [@prop:nakayama-relations-groups],
)

#proof[
  This was proved in Section~@sec:induction-restriction. This version for groups
  is also called *Frobenius reciprocity*#idx(
    "Frobenius",
    "reciprocity",
  )#idx("reciprocity, Frobenius").
]

#exercise[
  Show that the Nakayama isomorphism
  $ Hom_(R H) (M down_H, N) tilde.equiv Hom_(R G) (M, N up^G) $
  is given by the *exterior trace map*#idx("exterior trace map")#idx(
    "trace",
    "map",
    "exterior",
  ) $hat(Tr)_(H,G)$#idx("$hat(\"Tr\")$") defined by
  $
    hat(Tr)_(H,G) (phi.alt)(m)
    = sum_(g in G slash H) g times.o phi.alt(g^(-1) m).
  $
  Note that the expression $g times.o phi.alt(g^(-1) m)$ only depends on the
  left coset $g H$ of $H$ in $G$.
]

#corollary(title: [Eckmann–Shapiro Lemma])[
  $ Ext^n_(R H) (N, M down_H) tilde.equiv Ext^n_(R G) (N up^G, M) $
] <cor:eckmann-shapiro-groups>
#idx("Eckmann–Shapiro lemma", target: [@cor:eckmann-shapiro-groups])#idx(
  "lemma",
  "Eckmann–Shapiro",
  target: [@cor:eckmann-shapiro-groups],
)

#proof[
  This was proved in Section~@sec:induction-restriction, since $R G$ is
  projective (even free) as an $R H$-module.
]

#proposition[
  + $(N times.o_R M down_H) up^G tilde.equiv N up^G times.o_R M$
  + $Hom_R (N, M down_H) up^G tilde.equiv Hom_R (N up^G, M)$.
] <prop:induced-tensor-hom>

#proof[
  + By the associativity of tensor product we have
    $
      (N times.o_R M down_H) up^G
      & = R G times.o_(R H) (N times.o_R M down_H) \
      & tilde.equiv (R G times.o_(R H) N) times.o_R M = N up^G times.o_R M.
    $
    #source(73)
  + By Lemma~@lem:tensor-hom-adjunction we have
    $
      Hom_R (N, M down_H) up^G
      & tilde.equiv Hom_R (N, M down_H) Up^G \
      & = Hom_(R H) (R G, Hom_R (N, M down_H)) \
      & tilde.equiv Hom_R (R G times.o_(R H) N, M) = Hom_R (N up^G, M).
    $
]

Now if $H$ and $K$ are subgroups of $G$, we wish to describe what happens if we
induce a module from $K$ to $G$ and then restrict to $H$. Thus we need to
examine $R G$ as an $R H$-$R K$-bimodule, with left and right action by
multiplication. We have
$ lmodule(R H, R G)_(R K) tilde.equiv plus.o.big_(H g K) R(H g K) $
where $R(H g K)$ denotes a free $R$-module on the elements of the double coset
$H g K$, with left $R H$-action and right $R K$-action given by multiplication
as before.

If $M$ is a module for $K$, we write $g times.o M$ or $lconj(g, M)$ for the
$lconj(g, K)$-module with
$ (g k g^(-1))(g times.o m) = g times.o k m. $
With this notation we have
$
  R(H g K) & tilde.equiv R H times.o_(R(H inter lconj(g, K))) (g times.o R K) \
     h g k & <--> h times.o g times.o k.
$

#theorem(title: [Mackey Decomposition Theorem], head-break: true)[
  If $M$ is an $R K$-module then
  $
    M up^G down_H tilde.equiv
    plus.o.big_(H g K) (lconj(g, M)) down_(H inter lconj(g, K)) up^H.
  $
] <th:mackey>
#idx("Mackey", "decomposition theorem", target: [@th:mackey])#idx(
  "decomposition",
  "theorem, Mackey",
  target: [@th:mackey],
)#idx("theorem", "Mackey decomposition", target: [@th:mackey])

#proof[
  As $R H$-modules we have
  $
    #aligned-rows(
      (
        $M up^G down_H$,
        $tilde.equiv lmodule(R H, R G)_(R K) times.o_(R K) M
        tilde.equiv plus.o.big_(H g K) R(H g K) times.o_(R K) M$,
      ),
      (
        $$,
        $tilde.equiv plus.o.big_(H g K) R H times.o_(R(H inter lconj(g, K)))
        (g times.o R K) times.o_(R K) M$,
      ),
      (
        $$,
        $tilde.equiv plus.o.big_(H g K) R H times.o_(R(H inter lconj(g, K)))
        (g times.o M) down_(H inter lconj(g, K))
        tilde.equiv plus.o.big_(H g K)
        (lconj(g, M)) down_(H inter lconj(g, K)) up^H.$,
      ),
    )
  $
]

#remark[
  For a more traditional proof without this notational overload, see for example
  Curtis and Reiner [@bib:Curtis1962], §44.
]

#corollary[
  If $M$ is an $R K$-module and $N$ is an $R H$-module then we have
  + $M up^G times.o_R N up^G tilde.equiv
    limits(plus.o.big)_(H g K)
    (lconj(g, M) down_(H inter lconj(g, K))
      times.o_R N down_(H inter lconj(g, K))) up^G$
  + $Hom_R (M up^G, N up^G) tilde.equiv
    limits(plus.o.big)_(H g K)
    (Hom_R (lconj(g, M) down_(H inter lconj(g, K)),
        N down_(H inter lconj(g, K)))) up^G$
  + $M up^G times.o_(R G) N up^G tilde.equiv
    limits(plus.o.big)_(H g K)
    (lconj(g, M) down_(H inter lconj(g, K))
      times.o_(R(H inter lconj(g, K))) N down_(H inter lconj(g, K)))$
  + #source(74)$Hom_(R G) (M up^G, N up^G) tilde.equiv
    limits(plus.o.big)_(H g K)
    (Hom_(R(H inter lconj(g, K)))
      (lconj(g, M) down_(H inter lconj(g, K)), N down_(H inter lconj(g, K))))$
  + $Tor^(R G)_n (M up^G, N up^G) tilde.equiv
    limits(plus.o.big)_(H g K)
    (Tor_n^(R(H inter lconj(g, K)))
      (lconj(g, M) down_(H inter lconj(g, K)), N down_(H inter lconj(g, K))))$
  + $Ext^n_(R G) (M up^G, N up^G) tilde.equiv
    limits(plus.o.big)_(H g K)
    (Ext^n_(R(H inter lconj(g, K)))
      (lconj(g, M) down_(H inter lconj(g, K)),
        N down_(H inter lconj(g, K))))$.
] <cor:mackey-products>

#proof[
  + Using Proposition~@prop:induced-tensor-hom and the Mackey decomposition
    theorem we have
    $
      M up^G times.o_R N up^G
      & tilde.equiv (M up^G down_H times.o_R N) up^G
      tilde.equiv ((plus.o.big_(H g K)
          lconj(g, M) down_(H inter lconj(g, K)) up^H) times.o_R N) up^G \
      & tilde.equiv (((plus.o.big_(H g K)
            lconj(g, M) down_(H inter lconj(g, K)))
          times.o_R N down_(H inter lconj(g, K))) up^H) up^G \
      & tilde.equiv plus.o.big_(H g K)
      (lconj(g, M) down_(H inter lconj(g, K))
        times.o_R N down_(H inter lconj(g, K))) up^G.
    $
  The proofs of (ii), (iii) and (iv) are similar, and (v) and (vi) follow from
  (iii) and (iv) by dimension shifting.
]

In terms of the above descriptions, composition of maps is given as follows.
Suppose $M_1$, $M_2$ and $M_3$ are $R H$, $R K$ and $R L$-modules respectively,
where $H$, $K$ and $L$ are three subgroups of $G$. If double coset
multiplication is given by
$ (H g K)(K g' L) = sum_i n_i (H g k_i g' L) $
and
$
  alpha in Hom_(R G) (M_2 up^G, M_1 up^G), quad
  beta in Hom_(R G) (M_3 up^G, M_2 up^G)
$
are elements corresponding to
$
  macron(alpha) & in Hom_(R(H inter lconj(g, K)))
  (lconj(g, M_2) down_(H inter lconj(g, K)), M_1 down_(H inter lconj(g, K))),
  \
  macron(beta) & in Hom_(R(K inter lconj(g', L)))
  (lconj(g', M_3) down_(K inter lconj(g', L)), M_2 down_(K inter lconj(g', L)))
$
then $alpha compose beta$ is the sum of the elements corresponding to
$n_i macron(alpha) compose (lconj(g k_i, macron(beta)))$, where
$
  macron(alpha) compose (lconj(g k_i, macron(beta))) in
  Hom_(R(H inter lconj(g k_i g', L))) (lconj(g k_i g', M_3), M_1)
$
is the composite map
$
  lconj(g k_i g', M_3) limits(arrow.r.long)^(lconj(g k_i, macron(beta)))
  lconj(g k_i, M_2) = lconj(g, M_2) limits(->)^macron(alpha) M_1.
$

Applying dimension shifting as usual, we obtain a similar formula for Yoneda
composition of elements
$
  alpha in Ext^m_(R G) (M_2 up^G, M_1 up^G), quad
  beta in Ext^n_(R G) (M_3 up^G, M_2 up^G)
$
as the sum of the elements corresponding to the Yoneda composites
$n_i macron(alpha) compose (lconj(g k_i, macron(beta)))$.
