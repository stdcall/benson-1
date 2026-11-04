#import "main-defs.typ": *
#import "statements.typ": *

== A quotient without nilpotent elements <sec:quotient-without-nilpotents>

In this section, we prove that if $k$ is a field of characteristic $p$, then
$A(k G)$ has a fairly large quotient $A(G) slash A(G; p)$ with no non-zero
nilpotent elements. As an application of this, we show that if $G$ has cyclic
Sylow $p$-subgroups#idx("cyclic", "Sylow subgroups")#idx(
  "Sylow subgroups",
  "cyclic",
) then $A(G)$ has no non-zero nilpotent elements#idx(
  "nilpotent",
  "elements in $A(G)$",
). This was first proved by Green and O'Reilly [@bib:Green1964,
@bib:OReilly1965] using some heavy computations for metacyclic groups#idx(
  "metacyclic groups",
)#idx("group", "metacyclic"). The proof we present here is taken from
[@bib:Benson1986c].

#proposition[
  Let $k$ be an algebraically closed field of characteristic $p$. Suppose $M$ is
  a finitely generated indecomposable $k G$-module with $p divides dim_k M$.
  Then for any $k G$-module $N$ and any summand $U$ of $M times.o N$ we have
  $p divides dim_k U$.
] <prop:divisible-dimension-summands>

#proof[
  Suppose $dim_k U$ is not divisible by $p$. Then by
  Theorem~@th:trivial-summand, the trivial module $k$ is a summand of
  $U times.o U^*$ and hence of
  $(M times.o N) times.o U^* = M times.o (N times.o U^*)$. But again applying
  Theorem~@th:trivial-summand, we see that this implies that $dim_k M$ is not
  divisible by $p$, contradicting the hypothesis.
]

#definition[
  #source(204)Suppose $k$ is a field of characteristic $p$. We write $a(G; p)$
  for the additive span in $a(k G)$ of the elements $[M]$ with the property that
  for any extension field $hat(k) supset.eq k$, every summand of
  $hat(k) times.o_k M$ has dimension divisible by $p$. We write $A(G; p)$ for
  $CC times.o_ZZ a(G; p) subset.eq A(G)$.
] <def:divisible-span>

#lemma[
  + $a(G; p)$ is an ideal in $a(G)$.
  + $A(G; p)$ is an ideal in $A(G)$.
] <lem:divisible-span-ideal>

#proof[
  This follows immediately from Proposition~@prop:divisible-dimension-summands.
]

#lemma[
  If $x = sum a_i [M_i] in A(G)$, write $x^*$ for $sum macron(a)_i [M_i^*]$
  where $macron(a)_i$ is the complex conjugate of $a_i$. If $x x^* in A(G; p)$
  then $x in A(G; p)$.
] <lem:conjugate-product>

#proof[
  Without loss of generality, $k$ is algebraically closed. If the trivial module
  $[k]$ does not appear with positive multiplicity in
  $
    x x^* = sum_i |a_i|^2 [M_i times.o M_i^*]
    + sum_(i != j) a_i macron(a)_j [M_i times.o M_j^*]
  $
  then by Theorem~@th:trivial-summand, each $[M_i]$ lies in $A(G; p)$.
]

#theorem[
  The quotient ring $A(G) slash A(G; p)$ has no non-zero nilpotent elements.
] <th:quotient-no-nilpotents>

#proof[
  If $A(G) slash A(G; p)$ has a non-zero nilpotent element, then there is a
  non-zero element $x in A(G)$, not in $A(G; p)$, but with $x^2 in A(G; p)$. Let
  $y = x x^*$. Then $y y^* = (x x^*)^2 in A(G; p)$. Applying the lemma twice, we
  deduce first that $y in A(G; p)$, and then that $x in A(G; p)$.
]

#lemma[
  Suppose $k$ is algebraically closed. Suppose $H$ is $p$-hypo-elementary with
  $1 != D = O_p (H)$ cyclic. Let $H_1$ be a subgroup of $H$ of index $p$ (it is
  easy to see that there is one, but it need not be normal). Then
  $ A(H; p) = Im(ind_(H_1, H)). $
] <lem:divisible-span-induced>

#proof[
  It follows from Jordan normal form that the indecomposable $k D$-modules are
  just the Jordan blocks of size at most $|D|$ with eigenvalue one, so that they
  are uniserial modules.

  Since $k H slash J(k H) = k(H slash D)$ is a direct sum of distinct one
  dimensional modules, the Idempotent Refinement
  Theorem~@th:idempotent-refinement shows that each projective indecomposable
  module for $k H$ restricts to the regular representation of $k D$, which is
  uniserial of length $|D|$. It follows that if $M$ is any indecomposable
  $k H$-module then $M$ is uniserial and $M down_D$ is indecomposable.

  Let $D_1$ be the subgroup of $D$ of index $p$. If $M_1$ is an indecomposable
  $k D_1$-module then $Hom_(k D) (k, M_1 up^D) tilde.equiv Hom_(k D_1) (k, M_1)$
  is one dimensional, and so $M_1 up^D$ is indecomposable. It follows that a
  $k D$-module has dimension divisible by $p$ if and only if it is induced from
  a $k D_1$-module. Thus an indecomposable $k H$-module $M$ has dimension
  divisible by $p$ if and only if it is projective relative to $H_1$.

  It only remains to show that if $N$ is an indecomposable $k H_1$-module then
  $N up^H$ is indecomposable. But this is clear since
  $N up^H down_D tilde.equiv N down_(D_1) up^D$ by the Mackey decomposition
  theorem.
]

#theorem(title: [Green, O'Reilly])[
  #source(205)Suppose that the group $G$ has cyclic Sylow $p$-subgroups, and $k$
  is a field of characteristic $p$. Then $A(k G)$ has no non-zero nilpotent
  elements.
] <th:green-oreilly>

#proof[
  Without loss of generality $k$ is algebraically closed. By
  Corollary~@cor:hypo-elementary-restriction, the sum of the restriction maps to
  $A(k H)$ with $H$ $p$-hypo-elementary is injective, so it suffices to prove
  the theorem in case $G = H$ is $p$-hypo-elementary with $D = O_p (H)$ cyclic.
  We prove the theorem by induction on $|D|$. If $|D| = 1$ then $H$ has order
  coprime to $p$, and the theorem follows from
  Proposition~@prop:ordinary-character-homomorphisms. If $|D| > 1$, let $H_1$ be
  a subgroup of $H$ of index $p$. Then by
  Corollary~@cor:representation-ring-decomposition and the lemma, we have
  $
    A(H) = Im(ind_(H_1, H)) plus.o Ker(res_(H, H_1))
    = A(H; p) plus.o Ker(res_(H, H_1))
  $
  as a direct sum of ideals. Thus $res_(H, H_1)$ maps $A(H; p)$ injectively into
  $A(H_1)$, and so $A(H; p)$ has no non-zero nilpotent elements by the inductive
  hypothesis. Since $A(H) slash A(H; p)$ has no non-zero nilpotent elements by
  Theorem~@th:quotient-no-nilpotents, this completes the proof of the theorem.
]

#remark[
  It turns out that if the Sylow $p$-subgroups of $G$ are not cyclic, or
  elementary abelian 2-groups (with $p = 2$), then there are non-zero nilpotent
  elements in $A(G)$ (Zemanek [@bib:Zemanek1971a, @bib:Zemanek1973]). In case
  $p = 2$ and the Sylow 2-subgroups of $G$ are elementary abelian of order four,
  Conlon [@bib:Conlon1966] has shown that there are no non-zero nilpotent
  elements in $A(G)$. For larger elementary abelian 2-groups, this question is
  still open. See also Section 5.9 of Volume II for a cohomological method for
  producing non-zero nilpotent elements in $A(G)$.
]
