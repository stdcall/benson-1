#import "main-defs.typ": *
#import "statements.typ": *

== The trivial source ring <sec:trivial-source-ring>

At the end of the last section, we made use of the natural map
$phi.alt : b(G) -> a(R G)$, which takes a permutation representation to the
matrix representation with the permuted points as basis. In other words, if $X$
is a permutation representation, then the free $R$-module $R X$ is an
$R G$-module with the obvious action. The map $phi.alt$ is usually not
injective, but we wish to study its image. For many purposes, it is better to
work with subrings of $a(R G)$ which are closed under taking direct summands, so
we make the following definition.

#definition[
  We write $a(G, Triv)$#idx("$a(G, \"Triv\")$") or $a(R G, Triv)$ for the
  subring of $a(R G)$ consisting of linear combinations of trivial source
  modules#idx("module", "trivial", "source")#idx(
    "trivial",
    "source module",
  ) (i.e., direct summands of permutation modules). As usual, we write
  $A(G, Triv)$ for $CC times.o_ZZ a(G, Triv)$, and so on.
] <def:trivial-source-ring>

Let $(K, cal(O), k)$ be a splitting $p$-modular system for $G$ and all its
subgroups. We investigated trivial source modules in
Section~@sec:trivial-source, and found that a trivial source $k G$-module has a
unique lift to a trivial source $cal(O) G$-module. Thus we have the following.

#lemma(closed: true)[
  The natural map
  $ a(cal(O) G, Triv) -> a(k G, Triv), $
  given by reducing trivial source $cal(O) G$-modules modulo $frak(p)$, is an
  isomorphism of rings.
] <lem:trivial-source-reduction>

We now investigate the ring homomorphisms
$ a(k G, Triv) tilde.equiv a(cal(O) G, Triv) -> CC. $

#source(196)

#definition[
  A group $H$ is said to be *p-hypo-elementary*#idx(
    "hypo-elementary group",
  )#idx("group", "hypo-elementary") if the quotient $H slash O_p (H)$ is
  cyclic;#idx("cyclic", "quotient")#idx("quotient", "cyclic") in other words, if
  $H$ has a normal $p$-subgroup for which the quotient is a cyclic $p'$-group.
] <def:hypo-elementary>

If $H$ is a $p$-hypo-elementary subgroup of $G$, and $g in H slash O_p (H)$, we
define a ring homomorphism
$ s_(H, g) : a(k G, Triv) -> CC $
as follows. If $M$ is a trivial source $k G$-module, let
$M down_H = M_1 plus.o M_2$, where $M_1$ is a direct sum of indecomposable
modules with vertex $O_p (H)$, and $M_2$ is a direct sum of indecomposable
modules with vertex properly contained in $O_p (H)$. Since $M$ is a trivial
source module, $O_p (H)$ acts trivially on $M_1$, and so $M_1$ is a module for
$H slash O_p (H)$. We define
$ s_(H, g) (M) = t_g (M_1). $
Since the tensor product of any module with a module whose vertex is properly
contained in $O_p (H)$ is a direct sum of such modules
(Corollary~@cor:tensor-relatively-projective), it is clear that $s_(H, g)$ is a
ring homomorphism.

#proposition(title: [Conlon])[
  Suppose $M_1$ and $M_2$ are trivial source $k G$-modules and
  $s_(H, g) (M_1) = s_(H, g) (M_2)$ for all pairs $(H, g)$. Then
  $M_1 tilde.equiv M_2$.
] <prop:conlon-trivial-source>

#proof[
  By stripping off common direct summands, we may suppose that no direct summand
  of $M_1$ is isomorphic to a direct summand of $M_2$. Let $D$ be a maximal
  element of the set of vertices of summands of $M_1$ and $M_2$. Suppose
  $M_1 down_(N_G (D)) = M'_1 plus.o M''_1$ and
  $M_2 down_(N_G (D)) = M'_2 plus.o M''_2$, where $M'_1$ and $M'_2$ are sums of
  modules with vertex $D$, and $M''_1$, $M''_2$ are sums of modules whose vertex
  does not contain $D$. Thus $M'_1$ and $M'_2$ are projective
  $N_G (D) slash D$-modules. Since $t_g (M'_1) = t_g (M'_2)$ for all
  $p'$-elements $g in N_G (D) slash D$, by Corollary~@cor:cartan-homomorphism we
  have $M'_1 tilde.equiv M'_2$ as modules for $N_G (D) slash D$. By
  Theorem~@th:green-correspondence, the Green correspondents of summands of
  $M'_1$ and $M'_2$ are summands of $M_1$ and $M_2$, contradicting the fact that
  $M_1$ and $M_2$ have no isomorphic summands.
]

#corollary[
  Every ring homomorphism $a(G, Triv) -> CC$ is of the form $s_(H, g)$ for some
  pair $(H, g)$ with $H$ $p$-hypo-elementary and $g$ a generator of
  $H slash O_p (H)$. The sum of these maps is an isomorphism after tensoring
  with $CC$:
  $
    sum s_(H, g) : A(G, Triv)
    -> plus.o.big_("ccl's of" \ "pairs" (H, g)) CC.
  $
] <cor:trivial-source-ring-homomorphisms>

#proof[
  By the proposition, the map $sum s_(H, g)$ is injective. To show that the
  $s_(H, g)$ are distinct, we evaluate them on Green correspondents of
  projective $N_G (D) slash D$-modules (viewed as $N_G (D)$-modules) as in the
  proof of the proposition. By Lemma~@lem:independence-homomorphisms it follows
  that $sum s_(H, g)$ is an isomorphism, and that there are no more ring
  homomorphisms from $a(G, Triv)$ to $CC$.
]
