#import "main-defs.typ": *
#import "statements.typ": *

== Brauer's second main theorem <sec:second-main-theorem>
#idx(
  "Brauer's",
  "second main theorem",
  target: [@sec:second-main-theorem],
)#idx(
  "second main theorem, Brauer's",
  target: [@sec:second-main-theorem],
)#idx(
  "theorem",
  "Brauer's",
  "second main",
  target: [@sec:second-main-theorem],
)

The following is Nagao's module theoretic version of Brauer's second main
theorem.

#theorem(title: [Nagao])[
  Let $e in Z(k G)$ be a central idempotent, let $D$ be a $p$-subgroup of $G$,
  and let $K$ be a subgroup with $C_G (D) <= K <= N_G (D)$. If $M$ is a
  $k G$-module with $M = e.M$ then
  $ M down_K = Br_D (e).M down_K plus.o M' $
  where $M'$ is a direct sum of modules projective relative to $p$-subgroups $Q$
  with $D lt.eq.not Q <= K$.
] <th:nagao>
#idx("Nagao's theorem", target: [@th:nagao])#idx(
  "theorem",
  "Nagao's",
  target: [@th:nagao],
)

#proof[
  We have $M' = (1 - Br_D (e)).M down_K$. Since $e$ acts as the identity
  endomorphism of $M$, $e - Br_D (e)$ acts as the identity endomorphism on $M'$.
  So by Lemma~@lem:brauer-decomposition[(ii)] we have
  $
    1_(M') in sum_(D lt.eq.not Q <= N_G (D)) (M', M')_Q^(N_G (D)) subset.eq
    sum_(D lt.eq.not Q <= K) (M', M')_Q^K.
  $
  Thus by Rosenberg's Lemma~@lem:rosenberg and Higman's criterion~@prop:higman,
  each indecomposable summand of $M'$ is projective relative to some
  $p$-subgroup $Q$ with $D lt.eq.not Q <= K$.
]

#corollary(closed: true)[
  Suppose $D$ is a $p$-subgroup of $G$, $M$ is an indecomposable $k G$-module
  with vertex $D$, and $e$ is a primitive idempotent in $Z(k G)$. If we denote
  by $M'$ the $N_G (D)$ module corresponding to $M$ under the Green
  correspondence (see Theorem~@th:green-correspondence), then $e.M = M$ if and
  only if $Br_D (e).M' = M'$.
] <cor:nagao-green-correspondent>

#corollary[
  Suppose $B = e.k G$ is a block with defect group $D$. Then there is an
  indecomposable trivial source module $M = e.M$ in the block $B$, with vertex
  exactly $D$.
] <cor:trivial-source-defect-group>

#proof[
  #source(220)Let $M_0$ be a projective indecomposable
  $k(N_G (D) slash D)$-module regarded as an indecomposable $k N_G (D)$-module
  with vertex $D$, and chosen so that $Br_D (e).M_0 = M_0$. Then by the above
  corollary the Green correspondent $M$ of $M_0$ is a trivial source
  indecomposable $k G$-module with vertex $D$, and $e.M = M$.
]

#corollary(title: [Blocks of defect zero])[
  If $B = e.k G$ is a block with defect group $D$, then the following are
  equivalent:
  + $J(B) = 0$ (and hence $B$ is a complete matrix ring over a division ring).
  + $D$ is the trivial subgroup of $G$.
  + $B$ contains a projective simple module.
] <cor:defect-zero>
#idx("block", "of defect zero", target: [@cor:defect-zero])#idx(
  "defect",
  "zero",
  target: [@cor:defect-zero],
)

#proof[
  By the above corollary and Proposition~@prop:defect-group-transfer, $D$ is the
  trivial subgroup if and only if every module in $B$ has vertex the trivial
  subgroup, which is the same as being projective. By Lemma~@lem:semisimple-ring
  this is equivalent to the condition that $J(B) = 0$. Now by
  Proposition~@prop:group-algebra-symmetric projective modules for $k G$ are
  injective, and so by Proposition~@prop:simple-projective-injective this
  happens if and only if $B$ contains a projective simple module.
]

#corollary[
  If $B$ is a block of $k G$ with defect group $D$, then $B$ has finite
  representation type#idx("finite", "representation type")#idx(
    "representation",
    "type",
    "finite",
  ) if and only if $D$ is cyclic#idx("block", "of cyclic defect").
] <cor:block-finite-type>

#proof[
  If $D$ is cyclic, then every subgroup $D'$ of $D$ is cyclic and so $k D'$ has
  finite representation type. So by Proposition~@prop:defect-group-transfer
  there are only finitely many possible sources for modules in $B$, and
  therefore $B$ has finite representation type. Conversely, if $D$ is not cyclic
  then $D$ has a quotient $ZZ slash p times ZZ slash p$, so there are infinitely
  many indecomposable $k D$-modules with vertex exactly $D$. Let $b$ be the
  Brauer correspondent of $B$, as a block of $N_G (D)$. Now if we induce the
  trivial $k D$-module to $N_G (D)$ then the resulting module
  $k(N_G (D) slash D)$ has summands in every block of $k N_G (D)$ (since every
  simple $k N_G (D)$-module has $D$ acting trivially). So given any
  indecomposable $k D$-module $M$ with vertex $D$, $M up^(N_G (D))$ has some
  summand $M'$ in $b$. Since $M up^(N_G (D)) down_D$ is a sum of conjugates of
  $M$, the module $M$ is a source of $M'$. Since each conjugacy class in
  $N_G (D)$ of $k D$-modules has finite cardinality, we obtain infinitely many
  non-isomorphic indecomposable modules in $b$ with vertex $D$ this way. By
  Corollary~@cor:nagao-green-correspondent, the Green correspondents of these
  give infinitely many non-isomorphic indecomposable modules in $B$ with vertex
  $D$.
]
