#import "main-defs.typ": *
#import "statements.typ": *

#source(118)
== Finite dimensional hereditary algebras <sec:hereditary-algebras>

In the last section, we saw that the path algebra of a quiver with finitely many
vertices is hereditary. Conversely, we shall see in this section that over an
algebraically closed field, every finite dimensional hereditary algebra is
Morita equivalent to the path algebra of a quiver with finitely many vertices
and no oriented cycles.

#lemma(title: [Eilenberg and Nakayama [@bib:Eilenberg1957]])[
  Let $Lambda$ be a ring and $I$ a two sided ideal contained in $J^2(Lambda)$
  which is finitely generated both as a left ideal and as a right ideal. If
  $Lambda slash I$ is hereditary then $I = 0$.
] <lem:eilenberg-nakayama>
#idx("Eilenberg–Nakayama lemma", target: [@lem:eilenberg-nakayama])#idx(
  "lemma",
  "Eilenberg–Nakayama",
  target: [@lem:eilenberg-nakayama],
)

#proof[
  Since $I$ is finitely generated as a right ideal, by Nakayama's lemma, if
  $I = I . J(Lambda)$ then $I = 0$. Thus it suffices to work modulo
  $I . J(Lambda)$, and so we assume $I . J(Lambda) = 0$. Let
  $Gamma = Lambda slash I$, so that $Gamma$ is hereditary. Since $I$ annihilates
  the $Lambda$-module $J(Lambda)$, we may regard $J(Lambda)$ as a
  $Gamma$-module. The map of $Gamma$-modules
  $J(Lambda) -> J(Lambda) slash I = J(Gamma)$ splits, as $J(Gamma)$ is a
  projective $Gamma$-module, so
  $J(Lambda) tilde.equiv J(Lambda) slash I plus.o I$. But
  $I subset.eq J^2(Lambda) = (J(Lambda) slash I) . J(Lambda) = Rad(J(Lambda))$
  as a $Gamma$-module, so by another application of Nakayama's lemma (this time
  on the left), $I = 0$.
]

#lemma[
  Suppose $Lambda$ is a finite dimensional hereditary algebra and $S_i$, $S_j$
  are simple modules with $Ext^1_Lambda (S_i, S_j) != 0$. Then the projective
  cover $P_i$ of $S_i$ contains a copy of the projective cover $P_j$ of $S_j$ as
  a proper submodule.
] <lem:hereditary-projective-cover>

#proof[
  Since $Ext^1_Lambda (S_i, S_j) != 0$, there is a non-zero homomorphism
  $P_j -> P_i$ whose image is in $J(P_i)$ but not in $J^2(P_i)$. The image of
  this map is a submodule of a projective module, and hence projective, and so
  the map splits. Since $P_j$ is indecomposable, this implies that this
  homomorphism is injective.
]

#lemma[
  If $Lambda$ is a finite dimensional hereditary algebra then the Ext-quiver of
  $Lambda$ contains no oriented cycles.
] <lem:hereditary-no-cycles>

#proof[
  Suppose $S_1 -> S_2 -> dots.c -> S_n -> S_1$ is an oriented cycle. Then by the
  previous lemma we have $P_1 supset P_2 supset dots.c supset P_n supset P_1$.
  These are strict inclusions of finite dimensional modules, and so this
  situation is impossible.
]

#proposition[
  Suppose $Lambda$ is a finite dimensional hereditary basic algebra over an
  algebraically closed field. Then $Lambda tilde.equiv k Q_Lambda$, the path
  algebra of its Ext-quiver.
] <prop:hereditary-path-algebra>

#proof[
  By Lemma~@lem:hereditary-no-cycles, $k Q_Lambda$ is finite dimensional, and so
  $J^n k Q_Lambda$ is the ideal of paths of length at least $n$. By
  Proposition~@prop:gabriel-quiver, there is a surjective map
  $phi.alt : k Q_Lambda -> Lambda$ whose kernel is contained in
  $J^2 k Q_Lambda$. Thus by Lemma~@lem:eilenberg-nakayama $phi.alt$ is an
  isomorphism.
]

The same arguments apply in the case of a modulated quiver, using
Corollary~@cor:perfect-field-quotient.

#source(119)

#proposition(closed: true)[
  Suppose $Lambda$ is a finite dimensional hereditary basic algebra over a
  perfect field. Then $Lambda tilde.equiv k Q_Lambda$, the path algebra of its
  Ext-quiver.
] <prop:hereditary-perfect-field>

#remark[
  The above proposition is no longer true over a field which is not perfect,
  since the splitting condition in Proposition~@prop:modulated-quotient may
  fail. An example of a finite dimensional hereditary algebra which is not
  isomorphic to the path algebra of its Ext-quiver may be found in Dlab and
  Ringel [@bib:Dlab1978].
]
