#import "main-defs.typ": *
#import "statements.typ": *

== Idempotents and the Cartan matrix <sec:idempotents-cartan>
#idx("Cartan", "matrix", target: [@sec:idempotents-cartan])#idx(
  "matrix, Cartan",
  target: [@sec:idempotents-cartan],
)

Recall that an *idempotent*#idx("idempotent") in a ring $Lambda$ is a non-zero
element $e$ with $e^2 = e$. If $e != 1$ is an idempotent then so is $1 - e$.

#definition[
  Two idempotents $e_1$ and $e_2$ are said to be *orthogonal*#idx(
    "idempotent",
    "orthogonal",
  )#idx("orthogonal idempotents") if $e_1 e_2 = e_2 e_1 = 0$. An idempotent $e$
  is said to be *primitive*#idx("idempotent", "primitive")#idx(
    "primitive",
    "idempotent",
  ) if we cannot write $e = e_1 + e_2$ with $e_1$ and $e_2$ orthogonal
  idempotents.
] <def:orthogonal-primitive>

#source(25)There is a one–one correspondence between expressions
$1 = e_1 + dots.c + e_n$ with the $e_i$ orthogonal idempotents, and direct sum
decompositions
$lmodule(Lambda, Lambda) = Lambda_1 plus.o dots.c plus.o Lambda_n$ of the
regular representation, given by $Lambda_i = Lambda e_i$. Under this
correspondence, $e_i$ is primitive if and only if $Lambda_i$ is indecomposable.

#proposition[
  Two idempotents $e$ and $e'$ are conjugate#idx("conjugate idempotents")#idx(
    "idempotent",
    "conjugate",
  ) in $Lambda$ if and only if $Lambda e tilde.equiv Lambda e'$ and
  $Lambda(1 - e) tilde.equiv Lambda(1 - e')$.
] <prop:conjugate-idempotents>

#proof[
  If $e$ and $e'$ are conjugate, say $e mu = mu e'$ with $mu$ invertible, then
  $(1 - e) mu = mu(1 - e')$ and so $mu$ induces an isomorphism from $Lambda e$
  to $Lambda e'$ and from $Lambda(1 - e)$ to $Lambda(1 - e')$. Conversely if
  $Lambda e tilde.equiv Lambda e'$ and
  $Lambda(1 - e) tilde.equiv Lambda(1 - e')$, then by Lemma~@lem:idempotent-hom
  there are elements $mu_1 in e Lambda e'$, $mu_2 in e' Lambda e$,
  $mu_3 in (1 - e) Lambda(1 - e')$ and $mu_4 in (1 - e') Lambda(1 - e)$ such
  that
  $
    mu_1 mu_2 & = e     & quad mu_2 mu_1 & = e' \
    mu_3 mu_4 & = 1 - e & quad mu_4 mu_3 & = 1 - e'.
  $
  Letting $mu = mu_1 + mu_3$ and $mu' = mu_2 + mu_4$, we have
  $mu mu' = mu' mu = 1$ and $e mu = mu_1 = mu e'$.
]

Under the circumstances of the above proposition, we say $e$ and $e'$ are
*equivalent*#idx("equivalent idempotents")#idx("idempotent", "equivalent"). Note
that if the Krull–Schmidt theorem holds for finitely generated $Lambda$-modules,
then $Lambda e tilde.equiv Lambda e'$ implies
$Lambda(1 - e) tilde.equiv Lambda(1 - e')$ since
$lmodule(Lambda, Lambda) tilde.equiv Lambda e plus.o Lambda(1 - e)$.

#theorem(title: [Idempotent Refinement])[
  Let $N$ be a nilpotent ideal#idx("ideal", "nilpotent")#idx(
    "nilpotent",
    "ideal",
  ) in $Lambda$, and let $e$ be an idempotent in $Lambda slash N$. Then there is
  an idempotent $f$ in $Lambda$ with $e = macron(f)$.

  If $e_1$ is equivalent to $e_2$ in $Lambda slash N$, $macron(f)_1 = e_1$ and
  $macron(f)_2 = e_2$, then $f_1$ is equivalent to $f_2$ in $Lambda$.
] <th:idempotent-refinement>
#idx(
  "idempotent",
  "refinement theorem",
  target: [@th:idempotent-refinement],
)#idx(
  "refinement, idempotent",
  target: [@th:idempotent-refinement],
)#idx("theorem", "idempotent refinement", target: [@th:idempotent-refinement])

#proof[
  We define idempotents $e_i in Lambda slash N^i$ inductively as follows. Let
  $e_1 = e$. For $i > 1$, let $a$ be any element of $Lambda slash N^i$ with
  image $e_(i-1)$ in $Lambda slash N^(i-1)$. Then
  $a^2 - a in N^(i-1) slash N^i$, and so $(a^2 - a)^2 = 0$. Let
  $e_i = 3a^2 - 2a^3$. Then $e_i$ has image $e_(i-1)$ in $Lambda slash N^(i-1)$,
  and
  $
    e_i^2 - e_i = (3a^2 - 2a^3)(3a^2 - 2a^3 - 1)
    = -(3 - 2a)(1 + 2a)(a^2 - a)^2 = 0.
  $
  If $N^r = 0$, we take $f = e_r$.

  Note that in this proof, if $Lambda$ happens to be an algebra over a field $k$
  of characteristic $p$, we can instead take $e_i = a^p$ if we wish.

  Now suppose that $e_1$ is conjugate to $e_2$, say
  $macron(mu) e_1 = e_2 macron(mu)$ for some $mu in Lambda$. Let
  $nu = f_2 mu f_1 + (1 - f_2) mu(1 - f_1)$. Then $nu f_1 = f_2 nu$, and
  $1 - mu^(-1) nu = mu^(-1)(f_2 mu + mu f_1 - 2 f_2 mu f_1)
  = mu^(-1)(f_2 mu - mu f_1)(1 - 2 f_1) in N$ so that
  $ (1 + (1 - mu^(-1) nu) + (1 - mu^(-1) nu)^2 + dots.c) mu^(-1) $
  is an inverse for $nu$.
]

#corollary[
  Let $N$ be a nilpotent ideal in $Lambda$. Let $1 = e_1 + dots.c + e_n$ with
  the $e_i$ primitive orthogonal idempotents in $Lambda slash N$. Then we can
  write $1 = f_1 + dots.c + f_n$ with the $f_i$ primitive orthogonal idempotents
  in $Lambda$ and $macron(f)_i = e_i$. If $e_i$ is conjugate to $e_j$ then $f_i$
  is conjugate to $f_j$.
] <cor:idempotent-refinement>

#proof[
  #source(26)Define idempotents $f'_i$ inductively as follows. $f'_1 = 1$, and
  for $i > 1$, $f'_i$ is any lift of $e_i + e_(i+1) + dots.c + e_n$ to an
  idempotent in the ring $f'_(i-1) Lambda f'_(i-1)$. Then
  $f'_i f'_(i+1) = f'_(i+1) = f'_(i+1) f'_i$. Let $f_i = f'_i - f'_(i+1)$.
  Clearly $macron(f)_i = e_i$. If $j > i$, $f_j = f'_(i+1) f_j f'_(i+1)$, and so
  $f_i f_j = (f'_i - f'_(i+1)) f'_(i+1) f_j f'_(i+1) = 0$. Similarly
  $f_j f_i = 0$.
]

Now for the rest of this section, suppose that $Lambda$ satisfies D.C.C. on left
ideals. Then by the Wedderburn Structure Theorem~@th:wedderburn-artin, we may
write $Lambda slash J(Lambda) = plus.o.big_(i=1)^r Mat_(n_i) (Delta_i)$. Write
$S_i$ for the simple $Lambda$-module corresponding to the $i^(t h)$ matrix
factor. Then the regular representation of $Lambda slash J(Lambda)$ is
isomorphic to $plus.o.big_(i=1)^r n_i S_i$. This decomposition corresponds to an
expression $1 = e_1 + e_2 + dots.c$ in $Lambda slash J(Lambda)$ with the $e_i$
orthogonal idempotents. Lifting to an expression $1 = f_1 + f_2 + dots.c$ in
$Lambda$ as in the above corollary, we have a direct sum decomposition
$ lmodule(Lambda, Lambda) = plus.o.big_(i=1)^r n_i P_i $
with $P_i slash J(Lambda) P_i tilde.equiv S_i$. By the Krull–Schmidt theorem,
every projective indecomposable module is isomorphic to one of the $P_i$.

#lemma[
  $Hom_Lambda (P_i, S_j) tilde.equiv
  cases(Delta_i & quad "if" i = j, 0 & quad "otherwise.")$
] <lem:hom-projective-simple>

#proof[
  $P_i$ has a unique top composition factor, and this is isomorphic to $S_i$.
]

#lemma[
  $dim_(Delta_i) Hom_Lambda (P_i, M)$ is the multiplicity of $S_i$ as a
  composition factor of $M$.
] <lem:multiplicity-projective>

#proof[
  Use the previous lemma and induction on the composition length of $M$. Since
  $P_i$ is projective, an exact sequence
  $ 0 -> M' -> M -> S_j -> 0 $
  induces a short exact sequence
  $
    0 -> Hom_Lambda (P_i, M') -> Hom_Lambda (P_i, M) -> Hom_Lambda (P_i, S_j)
    -> 0.
  $
]

Dually we have:

#lemma(closed: true)[
  Suppose that $I_S$ is the injective hull of a simple $Lambda$-module $S$, and
  $Delta = End_Lambda (S)$. Then $dim_Delta Hom_Lambda (M, I_S)$ is equal to the
  multiplicity of $S$ as a composition factor of $M$.
] <lem:multiplicity-injective>

Combining these lemmas, we have the following:

#theorem(title: [Landrock [@bib:Landrock1983]])[
  Suppose that $S$ and $T$ are simple modules for a finite dimensional algebra
  $Lambda$ over a splitting field $k$. Then the multiplicity of $T$ as a
  composition factor in the $n$th Loewy layer#idx("Loewy", "layer")#idx(
    "layer",
    "Loewy",
  ) of the projective cover $P_S$ is equal to the multiplicity of the dual $S^*$
  (which is a right $Lambda$-module) as a composition factor in the $n$th Loewy
  layer of the projective cover $P_(T^*)$.
] <th:landrock>
#idx("Landrock's theorem", target: [@th:landrock])#idx(
  "theorem",
  "Landrock's",
  target: [@th:landrock],
)

#proof[
  #source(27)Since $k$ is a splitting field, each $Delta_i$ is equal to $k$.
  Since
  $
    Rad^n Soc^n I_T = 0 quad "and" quad
    Soc^n (P_S slash Rad^n P_S) = P_S slash Rad^n P_S,
  $
  we have
  $
    Hom_Lambda (P_S slash Rad^n P_S, I_T)
    & = Hom_Lambda (P_S slash Rad^n P_S, Soc^n I_T) \
    & = Hom_Lambda (P_S, Soc^n I_T).
  $
  By Lemma~@lem:multiplicity-injective, the dimension of the left hand side is
  equal to the multiplicity of $T$ as a composition factor in the first $n$
  Loewy layers of $P_S$. By Lemma~@lem:multiplicity-projective, the dimension of
  the right hand side is equal to the multiplicity of $S$ in the first $n$ socle
  layers of $I_T$. The dual of $I_T$ is $P_(T^*)$, so this is equal to the
  multiplicity of $S^*$ in the first $n$ Loewy layers of $P_(T^*)$. The theorem
  follows by subtraction.
]

#definition[
  The *Cartan invariants*#idx("Cartan", "invariants")#idx(
    "invariants, Cartan",
  ) of $Lambda$ are defined as
  $ c_(i j) = dim_(Delta_i) Hom_Lambda (P_i, P_j), $
  namely the multiplicity of $S_i$ as a composition factor of $P_j$. The matrix
  $(c_(i j))$#idx("$c_(i j)$") is called the *Cartan matrix* of the ring
  $Lambda$.
] <def:cartan-matrix>

In general, the matrix $(c_(i j))$ may be singular, but we shall see in
Corollary~@cor:cartan-homomorphism that this never happens for a group algebra
of a finite group. In fact, we shall see in Corollary~@cor:cartan-determinant
and Theorem~@th:cartan-determinant that the determinant of the Cartan matrix of
a group algebra over a field of characteristic $p > 0$ is a power of $p$.

Finally, the following general fact about idempotents is often useful.

#lemma(title: [Rosenberg's lemma])[
  Suppose that $e$ is an idempotent in a ring $Lambda$, $e Lambda e$ is a local
  ring (cf. Lemmas~@lem:idempotent-hom, @lem:indecomposable-local and
  Theorem~@th:krull-schmidt-p-adic), and $e in sum_alpha I_alpha$, where
  $I_alpha$ is a family of two-sided ideals in $Lambda$. Then for some $alpha$
  we have $e in I_alpha$.
] <lem:rosenberg>
#idx("Rosenberg's lemma", target: [@lem:rosenberg])#idx(
  "lemma",
  "Rosenberg's",
  target: [@lem:rosenberg],
)

#proof[
  Each $e I_alpha e$ is an ideal in the local ring $e Lambda e$, and so for some
  value of $alpha$ we have $e I_alpha e = e Lambda e$.
]
