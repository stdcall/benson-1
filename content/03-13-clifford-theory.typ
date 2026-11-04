#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-13-clifford-theory.typ": (
  central-pullback, determinant-kernel, units-extension,
)

== Clifford theory <sec:clifford-theory>
#idx("Clifford theory", target: [@sec:clifford-theory])#idx(
  "theory, Clifford",
  target: [@sec:clifford-theory],
)

Clifford theory is concerned with the relationship between modules and normal
subgroups. In this section we present a primitive version of the Clifford theory
developed by Clifford, Cline, Conlon, Dade, Green, Knörr, Puig, Ward, Willems
and others. Throughout this section, $R$ is a ring of coefficients with the
property that finitely generated $R G$-modules satisfy the Krull–Schmidt theorem
for all finite groups $G$.

Suppose $N$ is a normal subgroup of a finite group $G$, and $M_0$ is an
indecomposable $R G$-module which is projective relative to $N$. Then there is
an $R N$-module $M$ such that $M_0$ is a summand of $M up^G$. Now by the Mackey
decomposition theorem
$ M up^G down_N tilde.equiv plus.o.big_(g in G slash N) lconj(g, M) $
is a sum of conjugates of $M$. So by the Krull–Schmidt theorem, $M_0 down_N$ is
a direct sum of conjugates of $M$.

#definition[
  If $M$ is an indecomposable $R N$-module with $N lt.closed.eq G$, we define
  the *inertia group*#idx("group", "inertia")#idx("inertia group") $T = T(M)$ to
  be the set of all $g in G$ such that $M tilde.equiv lconj(g, M)$.
] <def:inertia-group>

#source(100)Thus in particular $N . C_G (N) lt.eq T$, and
$lconj(g, M) tilde.equiv lconj(g', M)$ if and only if $g$ and $g'$ are in the
same left coset of $T$ in $G$. If $T = G$, we say $M$ is *inertial*.

#proposition[
  Suppose $M$ is an indecomposable $R N$-module with $N lt.closed.eq G$, and
  with inertia group $T$. Let
  $ M up^T = M_1 plus.o dots.c plus.o M_r $
  with each $M_i$ indecomposable. Then each $M_i up^G$ is indecomposable, and
  $M_i up^G tilde.equiv M_j up^G$ if and only if $M_i tilde.equiv M_j$.
] <prop:inertia-induction>

#proof[
  Since $T$ is the inertia group, $M_i down_N$ is a sum of copies of $M$, say
  $M_i down_N tilde.equiv n_i . M$. Then
  $
    M_i up^G down_N tilde.equiv plus.o.big_(g in G slash T)
    (g times.o M_i) down_N tilde.equiv plus.o.big_(g in G slash T)
    n_i . lconj(g, M).
  $

  Now $M_i$ is a summand of $M_i up^G down_T$, and so if $M_i up^G$ is
  decomposable one of the summands, $X$ say, has the property that $M_i$ is a
  summand of $X down_T$, and so $n_i . M$ is a summand of $X down_N$. But then
  since $G$ acts on $X$, $n_i . lconj(g, M)$ is also a summand of $X down_N$.
  Since $lconj(g, M) tilde.equiv.not lconj(g', M)$ if $g$ and $g'$ are in
  different left cosets of $T$ in $G$, this implies that all summands of
  $M_i up^G down_N$ appear in $X down_N$, so that counting summands we must have
  $X = M_i up^G$.

  If $M_i up^G tilde.equiv M_j up^G$ but $M_i tilde.equiv.not M_j$, then by the
  Krull–Schmidt theorem $M_i$ is a summand of $Y$, where
  $M_j up^G down_T = M_j plus.o Y$. Then $Y down_N$ is a sum of copies of
  $lconj(g, M)$ for $g in.not T$, while $M_i down_N$ is a sum of copies of $M$.
  Since $lconj(g, M) tilde.equiv.not M$ for $g in.not T$, this is impossible.
]

The effect of this proposition is that from now on we may assume that $M$ is
inertial, so that $M_0$ is a summand of $M up^G$, and $M up^G down_N$ is a sum
of copies of $M$. We shall also assume that $R = k$ is an algebraically closed
field, and under these hypotheses we examine idempotents in
$E = End_(k G) (M up^G)$. By Frobenius reciprocity we have
$
  E tilde.equiv Hom_(k N) (M, M up^G down_N)
  = plus.o.big_(g in G slash N) Hom_(k N) (M, lconj(g, M)).
$
Since $M tilde.equiv lconj(g, M)$ for all $g in G slash N$, we may decompose $E$
into a sum of pieces of the same dimension
$
  E = plus.o.big_(g in G slash N) E_g, quad
  E_g = Hom_(k N) (M, lconj(g, M)).
$
We have $E_g E_(g') = E_(g' g)$, $E_1 = End_(k N) (M)$ is a local ring, and
$J(E_1) E_g = E_g J(E_1)$ is of codimension one in $E_g$, consisting of the
non-isomorphisms. This is an example of what Dade calls a *strongly
$G slash N$-graded algebra*#idx("algebra", "strongly group-graded")#idx(
  "graded",
  "algebra",
  "strongly group-",
)#idx("strongly group-graded algebra"). In particular we have
$J(E_1) E subset.eq J(E)$, and each $E_g slash J(E_1) E_g$ is one dimensional,
so that $E slash J(E_1) E$ is a twisted group algebra for $G slash N$. Thus by
Proposition~@prop:central-extension-finite and the remarks following it, there
is a $p'$-cyclic central extension $1 -> Z -> hat(G slash N) -> G slash N -> 1$
and an injective map $Z arrow.hook k^times$ such that $E slash J(E_1) E$ is
isomorphic to the summand of $k hat(G slash N)$ on which $Z$ acts #source(101)as
scalars via this map. Thus by the Idempotent Refinement
Theorem~@th:idempotent-refinement the summands of $M up^G$ are in one–one
correspondence with the projective indecomposable $k hat(G slash N)$-modules
lying in this summand.

As an application of this set-up, we prove the following theorem.

#theorem(title: [Green's indecomposability theorem])[
  Suppose that $N$ is a normal subgroup of $G$ such that $G slash N$ is a
  $p$-group, and $M$ is an *absolutely indecomposable*#idx(
    "absolutely indecomposable",
  )#idx("indecomposable", "absolutely") $k N$-module (i.e., $k' times.o_k M$ is
  indecomposable for all extension fields $k'$ of $k$). Then $M up^G$ is
  absolutely indecomposable.
] <th:green-indecomposability>
#idx(
  "Green",
  "'s indecomposability theorem",
  target: [@th:green-indecomposability],
)#idx(
  "indecomposability theorem, Green's",
  target: [@th:green-indecomposability],
)#idx(
  "theorem",
  "Green's",
  "indecomposability",
  target: [@th:green-indecomposability],
)

#proof[
  Without loss of generality $k$ is algebraically closed. By applying induction
  on $|G : N|$, we may suppose $|G : N| = p$. If $M$ is not inertial, then by
  Proposition~@prop:inertia-induction $M up^G$ is indecomposable, and so we may
  suppose $M$ is inertial. Letting
  $ E = End_(k G) (M up^G) = plus.o.big_(g in G slash N) E_g $
  as above, $E slash J(E_1) E$ is a twisted group algebra for $G slash N$. But
  every $p'$-cyclic central extension of a cyclic group of order $p$ splits, and
  so $E slash J(E_1) E$ is isomorphic to the group algebra of $G slash N$. Since
  $J(E_1) E subset.eq J(E)$, this implies that $E slash J(E) tilde.equiv k$ and
  so $M up^G$ is indecomposable.
]

Returning to the set-up discussed before the theorem, the projective
indecomposable $k hat(G slash N)$-module corresponding to a summand $M_0$ of
$M up^G$ is called the *multiplicity module*#idx("module", "multiplicity")#idx(
  "multiplicity",
  "module",
), and another equivalent description of it is as follows. If we let
$M_0 down_N = M times.o_k V$ for some $k$-vector space $V$, then
$
  End_(k N) (M_0 down_N) slash J End_(k N) (M_0 down_N) tilde.equiv End_k (V)
$
admits an action of $G slash N$ as algebra automorphisms, so that by
Corollary~@cor:projective-action-lift, there is a finite $p'$-central extension
$hat(G slash N)$ of $G slash N$ and an action of $hat(G slash N)$ on $V$
compatible with this. This $k hat(G slash N)$-module is the multiplicity module.
Its dimension gives the multiplicity of $M$ as a summand of $M_0 down_N$.

If $End_k (M) = M times.o_k M^*$ extends to a $k G$-module, then by
Corollary~@cor:projective-action-lift, there is a finite $p'$-central extension
$hat(G)$ of $G$ and a $k hat(G)$-module $hat(M)$ such that
$End_k (hat(M)) tilde.equiv End_k (M)$ as algebras with $G$-action. This central
extension splits on $N$, so that $hat(G)$ is a pullback
$ #central-pullback $
and $hat(M) down_(N times Z) tilde.equiv M times.o_k epsilon^(-1)$ for an
appropriate one dimensional representation $epsilon$ of $Z$. Thus if we regard
$M up^G$ as a representation of $hat(G)$ with $Z$ in its kernel #source(102)then
$
  M up^G & tilde.equiv (M times.o_k epsilon^(-1) times.o_k epsilon)_(N times Z)
           up^(hat(G)) tilde.equiv
           (hat(M) down_(N times Z) times.o_k epsilon) up^(hat(G)) \
         & tilde.equiv hat(M) times.o_k epsilon_(N times Z) up^(hat(G))
           tilde.equiv hat(M) times.o_k [k G slash N]_alpha
$
where $[k G slash N]_alpha$ is the twisted group algebra for the 2-cocycle
$alpha$ corresponding to the one dimensional representation $epsilon$ of $Z$
(see the remarks after Proposition~@prop:central-extension-finite). Thus as a
module for $hat(G)$, the original module $M_0$ breaks up as a tensor product
$M_0 tilde.equiv hat(M) times.o_k V$ where $V$ is the multiplicity module as
before.

The extension $hat(M)$ does not always exist, as is easily seen by looking at
the example where $G = ZZ slash p^n$, $N = ZZ slash p$, and $M$ is any
$k N$-module with non-trivial action.

In general, the problem of whether $M$ can be extended to a module $hat(M)$ for
a suitable $hat(G)$ can be rephrased as follows. Consider for each $g in G$ the
set of all possible linear maps $phi.alt_g : M -> M$ such that
$g times.o phi.alt_g : lconj(g, M) = g times.o M -> M$ is an isomorphism of
$k N$-modules. Then for $g = 1$ this gives the multiplicative group
$(End_(k N) (M)^op)^times$. If we endow the set of all such pairs
$(g, phi.alt_g)$ with the composition
$(g, phi.alt_g) . (g', psi_(g')) = (g g', phi.alt_g compose psi_(g'))$, then we
obtain a (usually infinite) group $tilde(G)$, which fits into the following
diagram:
$ #units-extension $
and the $k N$-module $M$ extends in an obvious way to a $k tilde(G)$-module
$tilde(M)$. The question is, can this be reduced to a central extension? In
other words, if we let $K$ be the kernel of the map
$(End_(k N) (M)^op)^times -> k^times$ given by reduction modulo
$J End_(k N) (M)$ and set
$hat(G) slash N = (tilde(G) slash N) slash K = tilde(G) slash (N times K)$, then
we have a diagram of the form
$ #determinant-kernel $
#source(103)and the question is, does the exact sequence
$1 -> K -> tilde(G) slash N -> hat(G) slash N -> 1$ split? If it does, then the
$k tilde(G)$-module $tilde(M)$ restricts to give a $k hat(G)$-module $hat(M)$ as
required.

There are two cases of interest where the answer is yes. The first is the case
$K = 1$, in other words where $End_(k N) (M) tilde.equiv k$. In this case we
have $hat(G) = tilde(G)$ and so we can take $hat(M) = tilde(M)$. The second case
is the case where $G slash N$ is a $p'$-group. In this case, $K$ is a (usually
infinite non-abelian) nilpotent group#idx("group", "nilpotent")#idx(
  "nilpotent",
  "group",
) in which every element has order a power of $p$, and so the splitting follows
by repeated application of Corollary~@cor:extensions-split.

We summarise what we have proved in the following theorem:

#theorem(closed: true)[
  Let $N$ be a normal subgroup of a finite group $G$ and $k$ an algebraically
  closed field. Suppose $M$ is an inertial $k N$-module, and either
  + $End_(k N) (M) tilde.equiv k$, or
  + $char k = 0$ or $char k$ does not divide $|G slash N|$.
  Then there is a $p'$-cyclic central extension
  $ #central-pullback $
  such that $M$ extends to a module $hat(M)$ for $hat(G)$.

  If $M_0$ is a direct summand of $M up^G$, then regarding $M_0$ as a module for
  $hat(G)$ with $Z$ in the kernel, we have
  $ M_0 tilde.equiv hat(M) times.o_k V. $
  Here, $V$ is the multiplicity module for $M_0$, regarded as a module for
  $hat(G)$ with $N$ in the kernel.
] <th:clifford-extension>
