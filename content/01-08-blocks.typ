#import "main-defs.typ": *
#import "statements.typ": *

== Blocks and central idempotents <sec:blocks>

#definition[
  A *central idempotent*#idx("central", "idempotent")#idx(
    "idempotent",
    "central",
  ) in $Lambda$ is an idempotent in the centre of $Lambda$. A *primitive central
  idempotent*#idx("idempotent", "primitive central")#idx(
    "primitive",
    "central idempotent",
  ) is a central idempotent not expressible as the sum of two orthogonal central
  idempotents. There is a one–one correspondence between expressions
  $1 = e_1 + dots.c + e_s$ with $e_i$ orthogonal central idempotents and direct
  sum decompositions $Lambda = B_1 plus.o dots.c plus.o B_s$ of $Lambda$ as
  two-sided ideals, given by $B_i = e_i Lambda$.
] <def:central-idempotent>

Now suppose that $Lambda$ is Artinian. Then we can write
$Lambda = B_1 plus.o dots.c plus.o B_s$ with the $B_i$ indecomposable two-sided
ideals.

#lemma[
  This decomposition is unique; i.e., if
  $Lambda = B_1 plus.o dots.c plus.o B_s = B'_1 plus.o dots.c plus.o B'_t$ then
  $s = t$ and after renumbering if necessary, $B_i = B'_i$.
] <lem:block-decomposition-unique>

#proof[
  #source(28)Write $1 = e_1 + dots.c + e_s = e'_1 + dots.c + e'_t$. Then
  $e_i e'_j$ is either a central idempotent or zero for each pair $i$, $j$. Thus
  $e_i = e_i e'_1 + dots.c + e_i e'_t$, so that for a unique $j$,
  $e_i = e_i e'_j = e'_j$.
]

#definition[
  The indecomposable two-sided ideals in this decomposition are called the
  *blocks*#idx("block") of $Lambda$.
] <def:block>

Now suppose that $M$ is an indecomposable $Lambda$-module. Then
$M = e_1 M plus.o dots.c plus.o e_s M$ shows that for some $i$, $e_i M = M$, and
$e_j M = 0$ for $j != i$. We then say that $M$ *belongs to* the block $B_i$.
Thus the simple modules and projective indecomposables are classified into
blocks. Clearly if an indecomposable module is in a certain block, then so are
all its composition factors.

The following proposition states that the block decomposition is determined by
what happens modulo the square of the radical. It first appears in this form in
the literature in Külshammer [@bib:Kulshammer1987], although equivalent
statements have been well known for a long time.

#proposition[
  Suppose that $Lambda$ is Artinian and $I$ is a two sided ideal contained in
  $J^2(Lambda)$. Then the natural map $Lambda -> Lambda slash I$ induces a
  bijection between the set of idempotents in the centre $Z(Lambda)$ and the set
  of idempotents in $Z(Lambda slash I)$.
] <prop:central-idempotents-lift>

#proof[
  If $f$ is an idempotent in $Z(Lambda)$ then clearly $macron(f)$ is an
  idempotent in $Z(Lambda slash I)$. If $macron(f) = macron(f)'$ then $f - f f'$
  is nilpotent and idempotent, hence zero, so $f = f f' = f'$.

  Conversely if $e$ is an idempotent in $Z(Lambda slash I)$ then by
  Theorem~@th:idempotent-refinement there is an idempotent $f$ in $Lambda$ with
  $macron(f) = e$. So we must show that $f in Z(Lambda)$. Since
  $macron(f) in Z(Lambda slash I)$, we have
  $macron(f)(Lambda slash I)(1 - macron(f)) = 0$ and so
  $f Lambda(1 - f) subset.eq I subset.eq J^2$. Since $f$ and $1 - f$ are
  idempotent it follows that $f Lambda(1 - f) = f J^2(1 - f)$. We show by
  induction on $n$ that $f Lambda(1 - f) = f J^n (1 - f)$. Namely
  $
    f Lambda(1 - f) & = f J^(n-1) J(1 - f) subset.eq f J^(n-1) f J(1 - f)
                      + f J^(n-1)(1 - f) J(1 - f) \
                    & subset.eq f J^(n-1) f J^2(1 - f) + f J^n (1 - f) J(1 - f)
                      subset.eq f J^(n+1)(1 - f).
  $
  Since $J$ is nilpotent we thus have $f Lambda(1 - f) = 0$, and so for
  $a in Lambda$ we have $f a = f a f + f a(1 - f) = f a f$. Similarly
  $a f = f a f$ and so $f a = a f$, so that $f in Z(Lambda)$.
]

The following should be compared with the Wedderburn–Artin
theorem~@th:wedderburn-artin.

#proposition[
  Suppose that $M$ is a simple $Lambda$-module which is both projective and
  injective. Then $M$ is the unique simple module in a block $B$ of $Lambda$
  with $B tilde.equiv Mat_n (Delta)$. Here, $Delta$ is the division ring
  $End_Lambda (M)^op$ and $n = dim_(Delta^op)(M)$.
] <prop:simple-projective-injective>

#proof[
  Since $M$ is both projective and injective, we can write
  $lmodule(Lambda, Lambda) = n . M plus.o P$, where $P$ is a projective module
  which does not involve $M$. Hence by Lemma~@lem:idempotent-hom
  $Lambda = End_Lambda (lmodule(Lambda, Lambda))^op tilde.equiv
  Mat_n (End_Lambda (M))^op plus.o End_Lambda (P)^op$.
]

#exercise[
  #source(29)Show that every commutative Artinian ring is a direct sum of local
  rings.
]
