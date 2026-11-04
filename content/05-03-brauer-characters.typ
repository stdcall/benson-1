#import "main-defs.typ": *
#import "statements.typ": *

== Brauer character theory <sec:brauer-characters>

If $R = k$ is a field of characteristic $p$, we have to modify the procedure
given in the last section for obtaining ring homomorphisms $a(k G) -> CC$. Let
$hat(k)$ be an algebraic closure of $k$, and let $gamma$ be the $p'$-part of the
exponent of $G$. Then the $gamma$th roots of unity in $hat(k)$ and in $CC$ both
form a cyclic group#idx("cyclic", "group")#idx("group", "cyclic") of order
$gamma$. We choose once and for all an isomorphism between these cyclic groups.
Let $g$ be a $p'$-element of $G$. Given a $k G$-module $M$, we restrict it to
$chevron.l g chevron.r$ and extend the field to $hat(k)$. Then the
representation breaks up as a direct sum of eigenspaces of $g$, and each
eigenvalue of $g$ is a $gamma$th root of unity in $hat(k)$. We define $t_g (M)$
to be the sum of the corresponding roots of unity in $CC$. It is clear that
$t_g : a(G) -> CC$ is a ring homomorphism. We also write $t_g$ for the
corresponding algebra homomorphism $A(G) -> CC$.

#lemma[
  Suppose $k$ contains the primitive $gamma$th roots of unity, where $gamma$ is
  the $p'$-part of the exponent of $G$. Let $t_g$ be as above. Then there is an
  element $x in A(G, 1)$ with $t_g (x) != 0$ and $t_(g') (x) = 0$ for $g'$ a
  $p'$-element not conjugate to $g$ in $G$.
] <lem:separating-element>

#proof[
  Suppose $g$ has order $n$, and let $epsilon$ be the primitive $n$th root of
  unity in $k$ corresponding to $e^(2 pi i slash n) in CC$. Let $M_j$ be the one
  dimensional representation $g |-> (epsilon^j)$ of $chevron.l g chevron.r$ and
  take
  $ x = sum_(j=1)^n e^(-2 pi i j slash n) [M_j up^G] in A(G). $
  Since $chevron.l g chevron.r$ is a $p'$-group, the modules $M_j up^G$ are
  projective, and so $x in A(G, 1)$. Now let $g'$ be a $p'$-element of $G$. By
  the Mackey decomposition theorem, $M_j up^G down_((g'))$ is a direct sum of
  modules induced from the subgroups
  $chevron.l g' chevron.r inter lconj(z, chevron.l g chevron.r)$ of
  $chevron.l g' chevron.r$, one for each double coset
  $chevron.l g' chevron.r z chevron.l g chevron.r$. The eigenvalues of $g'$ on a
  module induced from a proper subgroup of $chevron.l g' chevron.r$ fall into
  cosets of a non-trivial group of roots of unity, so that $t_(g')$ vanishes on
  such a module. If $g' in lconj(z, chevron.l g chevron.r)$, the double coset is
  the coset $z chevron.l g chevron.r$, and the summand is $lconj(z, M_j)$, on
  which $g'$ acts as $z^(-1) g' z$ acts on $M_j$. Since
  $
    sum_(j=1)^n e^(-2 pi i j slash n) t_(g^m) (M_j)
    = cases(n & quad "if" g^m = g, 0 & quad "otherwise")
  $
  it follows that $t_(g') (x)$ is $n$ times the number of cosets
  $z chevron.l g chevron.r$ with $z^(-1) g' z = g$, that is,
  $|{z in G | z^(-1) g' z = g}|$, which is non-zero if and only if $g'$ is
  conjugate to $g$ in $G$.#ed-note[The book's proof claimed that
    $M_j up^G down_((g'))$ is free when $g'$ is not conjugate to an element of
    $chevron.l g chevron.r$, and that $M_j up^G down_((g))$ is the sum of the
    conjugates of $M_j$ and a free module; the author's list of corrections
    marks this proof as wrong. For $G$ cyclic of order 4 with generator $a$,
    $g = a^2$, $g' = a$ and $p = 3$, the module $M_j up^G$ has dimension 2, so
    it is not free over $chevron.l g' chevron.r = G$. For the Brauer character
    of an induced module see Curtis and Reiner [@bib:Curtis1981], Lemma
    (21.28).]
]

#proposition[
  Suppose $M$ and $M'$ are $k G$-modules. Then the following are equivalent:
  + $t_g (M) = t_g (M')$ for all $p'$-elements $g in G$.
  + $M$ and $M'$ have the same composition factors.
] <prop:brauer-composition-factors>

#source(188)

#proof[
  Since all short exact sequences split on restriction to
  $chevron.l g chevron.r$ for $g$ a $p'$-element, it is clear that (ii) implies
  (i). Conversely, suppose $t_g (M) = t_g (M')$ for all $p'$-elements $g in G$.
  We may replace $M$ and $M'$ with completely reducible modules with the same
  composition factors, without affecting the values of $t_g (M)$ and $t_g (M')$.
  Let the irreducible $k G$-modules be $M_1, dots, M_r$, and let the
  multiplicity of $M_i$ in $M$ be $a_i$ and in $M'$ be $b_i$.

  If $k'$ is a finite extension of $k$, then the map
  $cal(R) (k G) -> cal(R) (k' G)$ given by extension of scalars is injective,
  since composing with the map $cal(R) (k' G) -> cal(R) (k G)$ given by
  restriction of scalars gives multiplication by $|k' : k|$. We may thus assume
  that $k$ is a splitting field for $G$.

  By the Wedderburn structure theorem, we may choose elements $x_i in k G$ with
  trace 1 on $M_i$ and zero on the other $M_j$. Namely, regarding
  $k G slash J(k G)$ as a sum of matrix algebras over $k$, we choose a pre-image
  $x_i$ in $k G$ of the element consisting of a 1 in the top left entry of the
  $i$th matrix component and zeros everywhere else.

  Since the trace of an element of $G$ is equal to the trace of its $p'$-part,
  the hypothesis tells us that every element of $k G$ has the same trace on $M$
  as on $M'$. In particular, the elements $x_i$ do, and so
  $a_i equiv b_i mod p$. So stripping off some common direct summands, we may
  assume that $a_i equiv b_i equiv 0 mod p$. If we divide these multiplicities
  by $p$, the values of $t_g$ are also divided by $p$, and so we may continue by
  induction to show that the multiplicities are equal.
]

#theorem[
  Every ring homomorphism $cal(R) (G) = a(k G) slash a_0 (k G, 1) -> CC$ is of
  the form $t_g$ for some $p'$-element $g in G$. If $k$ contains the $gamma$th
  roots of unity, then the sum of these maps is an isomorphism after tensoring
  with $CC$:
  $
    sum t_g : CC times.o_ZZ cal(R) (G) = A(G) slash A_0 (G, 1)
    limits(arrow.r.long)^tilde.equiv
    plus.o.big_("ccl's of" \ p'"-elements" g in G) CC.
  $
] <th:brauer-character-homomorphisms>

#proof[
  By the proposition, the map $sum t_g$ is injective. By
  Lemmas~@lem:separating-element and~@lem:independence-homomorphisms, the $t_g$
  are linearly independent, and so $sum t_g$ is surjective, and there are no
  more ring homomorphisms $a(k G) slash a_0 (k G, 1) -> CC$.
]

The *Brauer character*#idx("Brauer", "character")#idx("character", "Brauer") of
a $k G$-module is its image under the above map $sum t_g$. In contrast to the
situation in characteristic zero, it turns out that in characteristic $p$ the
field of definition of a representation may be deduced from the character
values, in the following sense.

#proposition[
  Let $k$ be an algebraically closed field of characteristic $p$, and let
  $phi.alt : G -> GL_r (k)$ be a map affording a $k G$-module $M$. Denote by
  $F^n : GL_r (k) -> GL_r (k)$ the *Frobenius map*#idx("Frobenius", "map")#idx(
    "map",
    "Frobenius",
  ), which replaces matrix entries by their $p^n$th powers. If the
  representation $F^n (M)$ afforded by the map $F^n compose phi.alt$ is
  isomorphic to $M$, then there is an $FF_(p^n) G$-module $M_0$ with
  $ k times.o_(FF_(p^n)) M_0 tilde.equiv M. $
  Note that the character of $F^n (M)$ is given by
  $t_g (F^n (M)) = t_(g^(p^n)) (M)$.
] <prop:frobenius-field-of-definition>

#source(189)

#proof[
  Since $M tilde.equiv F^n (M)$, there is a matrix $X in GL_r (k)$ such that for
  all $g in G$, $X phi.alt(g) X^(-1) = F^n phi.alt(g)$. By a theorem of Lang
  (see for example Srinivasan [@bib:Srinivasan1979], p.~11), the map
  $Y |-> F^n (Y)^(-1) Y$ on $GL_r (k)$ is surjective, and so we may write
  $X = F^n (Y)^(-1) Y$ for some $Y in GL_r (k)$. Then for all $g in G$ we have
  $Y phi.alt(g) Y^(-1) = F^n (Y phi.alt(g) Y^(-1))$. Thus changing basis by
  means of $Y$, we see that the image of $G -> GL_r (k)$ lies in
  $GL_r (FF_(p^n))$ as required.
]

#corollary(closed: true)[
  Suppose $k$ contains the primitive $gamma$th roots of unity, where $gamma$ is
  the $p'$-part of the exponent of $G$. Then the $ZZ$-rank of $cal(R) (k G)$
  (i.e., the number of isomorphism types of $p$-modular irreducible
  representations of $G$) is equal to the number of conjugacy classes of
  $p'$-elements of $G$.
] <cor:p-regular-classes>

#exercise[
  Use the above arguments to count the number of isomorphism types of
  $p$-modular irreducible representations of $G$ in case $k$ does not contain
  the $gamma$th roots of unity.
]

#corollary[
  The representation ring $A(G)$ decomposes as a direct sum of ideals
  $ A(G) = A(G, 1) plus.o A_0 (G, 1). $
  The *Cartan homomorphism*#idx("Cartan", "homomorphism")#idx(
    "homomorphism",
    "Cartan",
  )
  $ c : A(G, 1) arrow.hook A(G) arrow.twohead A(G) slash A_0 (G, 1) $
  is an isomorphism. In particular, the Cartan matrix is non-singular. Thus
  projective $k G$-modules with the same Brauer character are isomorphic.
] <cor:cartan-homomorphism>

#proof[
  By Lemmas~@lem:separating-element and~@lem:independence-homomorphisms, the
  $t_g$ are linearly independent on $A(G, 1)$, and so $c$ is surjective. But the
  number of isomorphism types of projective indecomposables is equal to the
  number of isomorphism types of irreducibles, so the dimensions of $A(G, 1)$
  and $A(G) slash A_0 (G, 1)$ are equal, so $c$ is an isomorphism. Letting
  $e = c^(-1) (1)$, we see that $e$ is an idempotent, $A(G, 1) = e.A(G)$, and
  $A_0 (G, 1) = (1 - e).A(G)$.
]
