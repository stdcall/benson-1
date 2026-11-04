#import "main-defs.typ": *
#import "statements.typ": *

== Ordinary character theory <sec:ordinary-characters>

#source(186)The easiest case in which to understand $a(G)$ is the case $R = CC$.
In a sense, this is the model for all further developments. In this case, we
have ring homomorphisms
$
  t_g : a(G) & -> CC \
           M & |-> tr(g, M),
$
one for each conjugacy class#idx("conjugacy classes")#idx("classes, conjugacy")
of elements $g in G$. Using modules induced from cyclic subgroups#idx(
  "cyclic",
  "subgroups",
)#idx("subgroups", "cyclic"), it is easy to see that these homomorphisms are
distinct (the argument is spelled out in detail in
Lemma~@lem:separating-element).

#lemma[
  The $ZZ$-rank of $a(CC G)$ (i.e., the number of isomorphism types of
  ordinary#idx("character", "ordinary")#idx(
    "ordinary",
    "character",
  ) irreducible representations of $G$) is equal to the number of conjugacy
  classes of elements of $G$.
] <lem:ordinary-irreducible-count>

#proof[
  By Maschke's theorem, $a(CC G) = cal(R) (CC G)$ has a $ZZ$-basis consisting of
  the irreducible $CC G$-modules. Using the Wedderburn structure theorem
  (Section~@sec:wedderburn-structure), $CC G$ is a sum of matrix algebras over
  $CC$. Each matrix component corresponds to an isomorphism class of simple
  module, and has a one dimensional centre given by scalar matrices. Thus the
  $ZZ$-rank of $a(CC G)$ is equal to the dimension of $Z(CC G)$. The lemma now
  follows from the fact that the conjugacy class sums form a basis for
  $Z(CC G)$.
]

#lemma[
  Suppose $R_1$ is a commutative ring, and $R_2$ is an integral domain. Then any
  set of distinct ring homomorphisms $lambda_i : R_1 -> R_2$ is linearly
  independent over $R_2$. In particular, if $A$ is a commutative $CC$-algebra
  and $lambda_1, dots, lambda_n : A -> CC$ are distinct algebra homomorphisms
  then $sum lambda_i : A -> CC^n$ is surjective.
] <lem:independence-homomorphisms>

#proof[
  Suppose $sum_(i=1)^n alpha_i lambda_i = 0$ is a linear relation between such
  ring homomorphisms, with $alpha_i in R_2$ and $n$ minimal. There is no linear
  relation with $n = 1$. Choose $y in R_1$ such that
  $lambda_1 (y) != lambda_2 (y)$. Then for all $x in R_1$ we have
  $
    sum_(i=1)^n alpha_i lambda_i (x) lambda_i (y)
    = sum_(i=1)^n alpha_i lambda_i (x y) = 0
  $
  and so
  $ sum_(i=2)^n alpha_i (lambda_i (y) - lambda_1 (y)) lambda_i (x) = 0. $
  Since $R_2$ is an integral domain, the coefficient of $lambda_2$ is non-zero,
  and so this is a shorter linear relation among the $lambda_i$, contradicting
  the minimality of $n$.
]

#proposition[
  Every ring homomorphism $cal(R) (CC G) = a(CC G) -> CC$ is of the form $t_g$
  for some $g in G$. The sum of these maps is an isomorphism after tensoring
  with $CC$:
  $
    sum t_g : CC times.o_ZZ cal(R) (G) = A(G)
    limits(arrow.r.long)^tilde.equiv plus.o.big_("ccl's" \ "of" g in G) CC.
  $
] <prop:ordinary-character-homomorphisms>

#source(187)

#proof[
  Using the above two lemmas, with $R_1 = a(CC G)$ and $R_2 = CC$, we see that
  there can be at most as many ring homomorphisms $a(CC G) -> CC$ as there are
  conjugacy classes of elements in $G$. Since the $t_g$ are such ring
  homomorphisms, we have equality.
]

The *character*#idx("character") of a $CC G$-module is its image under the above
map $sum t_g$.
