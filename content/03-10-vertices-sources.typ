#import "main-defs.typ": *
#import "statements.typ": *

== Vertices and sources <sec:vertices-sources>

In this section, $R$ is a ring of coefficients such that the Krull–Schmidt
theorem holds for finitely generated $R G$-modules (e.g. $R$ a field or a
complete local domain).

#definition[
  Let $M$ be an indecomposable $R G$-module. Then $D$ is a *vertex*#idx(
    "vertex",
  ) of $M$ if $M$ is projective relative to $D$ but not relative to $D'$ for any
  proper subgroup $D'$ of $D$. A *source*#idx("source") of $M$ is an
  indecomposable $R D$-module $M_0$, where $D$ is a vertex of $M$, such that $M$
  is a direct summand of $M_0 up^G$ (cf. Proposition~@prop:higman).
] <def:vertex-source>

#proposition(title: [Green])[
  Let $M$ be an indecomposable $R G$-module.
  + The vertices of $M$ are conjugate in $G$.
  + Let $M_0$ and $M_1$ be two $R D$-modules which are both sources of $M$. Then
    there is an element $g in N_G (D)$ such that
    $M_0 tilde.equiv lconj(g, M_1)$.
  + If the $p'$ part of $|G|$ is invertible in $R$, then the vertices of $M$ are
    $p$-subgroups.
] <prop:vertices-conjugate>

#proof[
  + If $M$ is a summand of $M down_H up^G$ and also of $M down_K up^G$ then it
    is a summand of
    $
      M down_H up^G down_K up^G tilde.equiv plus.o.big_(H g K)
      M down_(H inter lconj(g, K)) up^G
    $
    by the Mackey decomposition theorem, so that if $H$ and $K$ are both
    vertices of $M$ then $H = lconj(g, K)$ for some $g in G$.
  + By Proposition~@prop:higman, some summand $M_2$ of $M down_D$ is a source of
    $M$. Thus $M_2$ is also a summand of
    $
      M_0 up^G down_D tilde.equiv plus.o.big_(D g D)
      lconj(g, M_0) down_(D inter lconj(g, D)) up^D .
    $
    Thus for some $g in N_G (D)$, $M_2 tilde.equiv lconj(g, M_0)$.
  + This follows from Corollary~@cor:index-invertible.
]

#exercise[
  #source(96)Use Rosenberg's lemma, Higman's criterion and
  Lemma~@lem:transfer-properties[(v)] to give an alternative proof of part (i)
  of the above proposition, under the assumption that the endomorphism ring
  $End_(R G) (M)$ is a local ring.
]
