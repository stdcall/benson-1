#import "main-defs.typ": *
#import "statements.typ": *

#source(97)
== Green correspondence <sec:green-correspondence>
#idx("correspondence", "Green", target: [@sec:green-correspondence])#idx(
  "Green",
  "correspondence",
  target: [@sec:green-correspondence],
)

For the purpose of this section, $R$ is a commutative ring of coefficients such
that the Krull–Schmidt theorem holds for finitely generated $R G$-modules, and
such that the $p'$-part of $|G|$ is invertible in $R$.

Let $D$ be a fixed $p$-subgroup of $G$ and let $H$ be a subgroup of $G$
containing $N_G (D)$. In this situation, Green correspondence is a tool for
reducing questions about representations of $G$ to questions about
representations of $H$, modulo stuff "coming from below". Naïvely, this means
induced from proper subgroups of $D$, but we can refine the statement to see
exactly what subgroups are involved. Of course, the main tool here is Mackey
decomposition.

Let
$
  cal(X) & = {X lt.eq G | X lt.eq lconj(g, D) inter D "for some"
             g in G without H} \
  cal(Y) & = {Y lt.eq G | Y lt.eq lconj(g, D) inter H "for some"
             g in G without H}.
$
Note that $cal(X) subset.eq cal(Y)$ and $D in.not cal(Y)$.

#lemma[
  Let $M$ be an indecomposable $R H$-module which is projective relative to $D$.
  + Let $M up^G down_H tilde.equiv M plus.o M'$. Then $M'$ is a sum of modules
    projective relative to subgroups $Y in cal(Y)$.
  + Let $M up^G tilde.equiv V plus.o V'$ with $V$ indecomposable and $M$ a
    summand of $V down_H$. Then $V'$ is a sum of modules projective relative to
    subgroups $X in cal(X)$.
] <lem:green-correspondence>

#proof[
  + Let $U$ be an indecomposable $R D$-module with
    $U up^H tilde.equiv M plus.o M_0$ for some $M_0$. Then
    $ U up^G down_H tilde.equiv M up^G down_H plus.o M_0 up^G down_H . $
    But by the Mackey decomposition theorem,
    $ U up^G down_H tilde.equiv U up^H plus.o U' $
    with $U'$ a sum of modules projective relative to subgroups $Y in cal(Y)$.
    Thus
    $
      M up^G down_H plus.o M_0 up^G down_H tilde.equiv
      M plus.o M_0 plus.o U'
    $
    and so by the Krull–Schmidt theorem, $M up^G down_H tilde.equiv M plus.o M'$
    with $M'$ a sum of modules projective relative to subgroups $Y in cal(Y)$.
  + It is clear that $V'$ is projective relative to $D$. Suppose it has an
    indecomposable summand $V_1$ which is not projective relative to a subgroup
    in $cal(X)$, and suppose $D_1 lt.eq D$ is a vertex of $V_1$. Let $U_1$ be a
    source of $V_1$. Then $U_1$ is a summand of $V_1 down_(D_1)$, and so for
    some indecomposable summand $M_1$ of $V_1 down_H$, $U_1$ is a summand of
    $M_1 down_(D_1)$. Thus $M_1$ is not projective relative to a subgroup in
    $cal(Y)$, and hence neither is $V' down_H$, contradicting (i).
]

#theorem(title: [Green Correspondence])[
  Suppose as above that $H$ is a subgroup of $G$ containing $N_G (D)$. Then
  there is a one–one correspondence between indecomposable $R G$-modules with
  vertex $D$ and indecomposable $R H$-modules with vertex $D$ given as follows.
  + #source(98)If $V$ is an indecomposable $R G$-module with vertex $D$, then
    $V down_H$ has a unique indecomposable summand $f(V)$ with vertex $D$, and
    the remaining summands have vertices in $cal(Y)$.
  + If $M$ is an indecomposable $R H$-module with vertex $D$, then $M up^G$ has
    a unique indecomposable summand $g(M)$ with vertex $D$, and the remaining
    summands have vertices in $cal(X)$.
  + We have $f(g(M)) tilde.equiv M$ and $g(f(V)) tilde.equiv V$.
  + The correspondences $f$ and $g$ take trivial source modules to trivial
    source modules.
  + If $V_1$ and $V_2$ are $R G$-modules with vertex $D$, then the trace map
    $Tr_(H, G)$ induces an isomorphism
    $
      (f(V_1), f(V_2))^(H, cal(X)) limits(arrow.r.long)^(Tr_(H, G))
      (V_1, V_2)^(G, cal(X))
    $
    (see Definition~@def:transfer for the notation).
] <th:green-correspondence>

#proof[
  + Let $S$ be a source of $V$ and let $S up^H tilde.equiv M plus.o M'$ with $M$
    an indecomposable module such that $V$ is a summand of $M up^G$. By part (i)
    of the above lemma, $M$ is the only summand of $M up^G down_H$ with $D$ as
    vertex, and the rest have vertices in $cal(Y)$. But some summand of
    $V down_H$ has vertex $D$, since $V$ is a summand of $V down_H up^G$, and so
    we take $f(V) = M$.
  + Choose an indecomposable summand $V$ of $M up^G$ such that $M$ is a summand
    of $V down_H$. Then by part (ii) of the above lemma,
    $M up^G tilde.equiv V plus.o V'$ with $V'$ a sum of modules with vertices in
    $cal(X)$. We take $g(M) = V$.
  + and (iv) are clear from (i) and (ii).
  #enum.item(5)[According to Proposition~@prop:nakayama-relations-groups and the
    exercise following it, the exterior trace map $hat(Tr)_(H, G)$ induces an
    isomorphism
    $
      (V_1 down_H, f(V_2))^H limits(arrow.r.long)^(hat(Tr)_(H, G))
      (V_1, f(V_2) up^G)^G.
    $
    By Lemma~@lem:transfer-properties[(vi)], this takes homomorphisms in
    $(V_1 down_H, f(V_2))^H_(cal(X))$ to homomorphisms in
    $(V_1, f(V_2) up^G)^G_(cal(X))$ and induces an isomorphism
    $
      (V_1 down_H, f(V_2))^(H, cal(X)) limits(arrow.r.long)^(hat(Tr)_(H, G))
      (V_1, f(V_2) up^G)^(G, cal(X)).
    $
    Since $f(V_2) up^G$ is a direct sum of $V_2$ and modules projective relative
    to subgroups in $cal(X)$ we have
    $ (V_1, f(V_2) up^G)^(G, cal(X)) tilde.equiv (V_1, V_2)^(G, cal(X)). $
    Since $Tr_(H, G)$ is the composite of $hat(Tr)_(H, G)$ and the map induced
    by the natural surjection $V_2 down_H up^G -> V_2$, it follows that if we
    regard $f(V_2)$ as a summand of $V_2 down_H$ then $Tr_(H, G)$ induces an
    isomorphism
    $
      (V_1 down_H, f(V_2))^(H, cal(X)) limits(arrow.r.long)^(Tr_(H, G))
      (V_1, V_2)^(G, cal(X)).
    $
    Finally, $V_1 down_H$ is a direct sum of $f(V_1)$ and modules projective
    relative to subgroups in $cal(Y)$. Since $f(V_2)$ is projective relative to
    $D$, applying Lemma~@lem:transfer-properties[(v)] #source(99)shows that any
    homomorphism from a module projective relative to a subgroup in $cal(Y)$ to
    $f(V_2)$ is a sum of transfers from subgroups in $cal(X)$. Thus
    $
      (V_1 down_H, f(V_2))^(H, cal(X)) tilde.equiv
      (f(V_1), f(V_2))^(H, cal(X)).
    $
  ]
]

The following theorem gives us more information in the situation where we have
Green correspondence.

#theorem(
  title: [D.~Burry and J.~F. Carlson [@bib:Burry1982b], L.~Puig
    [@bib:Puig1981]],
  head-break: true,
)[
  Suppose that $H$ is a subgroup of $G$ containing $N_G (D)$. Let $V$ be an
  indecomposable $R G$-module such that $V down_H$ has a direct summand $M$ with
  vertex $D$. Then $V$ has vertex $D$, and $V$ is the Green correspondent
  $g(M)$.
] <th:burry-carlson-puig>
#idx("Burry–Carlson–Puig theorem", target: [@th:burry-carlson-puig])#idx(
  "theorem",
  "Burry–Carlson–Puig",
  target: [@th:burry-carlson-puig],
)

#proof[
  Let $e = Tr_(D, H) (alpha) in (V, V)^H_D$ be the idempotent corresponding to
  the summand $M$ of $V down_H$. By Lemma~@lem:transfer-properties, we have
  $
    Tr_(D, G) (alpha) = sum_(H g D) Tr_(H inter lconj(g, D), H) (g alpha)
    = e + sum_(H g D \ g in.not H) Tr_(H inter lconj(g, D), H) (g alpha)
    equiv e mod (V, V)^H_(cal(Y)).
  $
  Since $M$ is not $cal(Y)$-projective, $e in.not (V, V)^H_(cal(Y))$, and so
  $Tr_(D, G) (alpha)$ is an idempotent in
  $(V, V)^G slash ((V, V)^G inter (V, V)^H_(cal(Y)))$. Since $(V, V)^G$ is a
  local ring, this means that
  $(V, V)^G = Tr_(D, G) (alpha) (V, V)^G subset.eq (V, V)^G_D$, and so $V$ is
  projective relative to $D$. Hence $V$ has vertex $D$ and $M$ is its Green
  correspondent.
]

Once Green correspondence has been applied, we are left with a module which is
projective relative to a normal $p$-subgroup. Analysis of such a situation is
the subject of the next section.
