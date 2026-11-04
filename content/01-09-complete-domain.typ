#import "main-defs.typ": *
#import "statements.typ": *

== Algebras over a complete domain <sec:complete-domain>

In order to compare representations in characteristic zero with representations
in characteristic $p$, we use representations over the $p$-adic integers as an
intermediary. This is easier than using the ordinary integers because, as we
shall see, we have a Krull–Schmidt theorem. It is better than using the
$p$-local integers (i.e., the integers with numbers coprime to $p$ inverted)
because of the idempotent refinement theorem, which enables us to lift
projective indecomposables from characteristic $p$.

Since it is often convenient to deal with fields larger than the rationals, we
also look at rings of $frak(p)$-adic integers for $frak(p)$ a prime ideal in a
ring of algebraic integers. The most general set up of this sort is a complete
rank one discrete valuation ring, but we shall be content with rings of
$frak(p)$-adic integers. If $cal(O)$ is the ring of integers in an algebraic
extension $K$ of $QQ$ and $frak(p)$ is a prime ideal in $cal(O)$ lying above a
rational prime $p$, we form the completion
$
  cal(O)_frak(p) = invlim_n cal(O) slash frak(p)^n.
$
The natural map $cal(O) -> cal(O)_frak(p)$ is injective, and so $K$ is a
subfield of the field of fractions $K_frak(p)$ of $cal(O)_frak(p)$. The ring
$cal(O)_frak(p)$ has a unique maximal ideal $frak(p)_frak(p)$, which is
principal, $frak(p)_frak(p) = (pi)$. In particular $cal(O)_frak(p)$ is a
principal ideal domain, so that finitely generated torsion-free modules are
free. The quotient field
$ k = cal(O)_frak(p) slash frak(p)_frak(p) tilde.equiv cal(O) slash frak(p) $
is a field of characteristic $p$. We say that $(K_frak(p), cal(O)_frak(p), k)$
is a *p-modular system*. More generally, if $cal(O)$#idx("$cal(O)$") is a
complete rank one discrete valuation ring#idx(
  "complete discrete valuation ring",
)#idx("discrete valuation ring, complete") with field of fractions $K$ of
characteristic zero, maximal ideal $frak(p) = (pi)$#idx("$frak(p)$"), and
quotient field $k = cal(O) slash frak(p)$ of characteristic $p$, we shall say
that $(K, cal(O), k)$ is a $p$-modular system#idx("$p$-modular system")#idx(
  "system",
  "$p$-modular",
). For the remainder of this section, $K$, $cal(O)$ and $k$ will be of this
form.

Let $Lambda$ be an algebra over $cal(O)$ which as an $cal(O)$-module is free of
finite rank. Let $hat(Lambda) = K times.o_cal(O) Lambda$ and
$macron(Lambda) = k times.o_cal(O) Lambda = Lambda slash pi Lambda$. By a
$Lambda$-*lattice*#idx("lattice") we mean a finitely generated $cal(O)$-free
$Lambda$-module. If $M$ is a $Lambda$-lattice then we set
$hat(M) = K times.o_cal(O) M$ as a $hat(Lambda)$-module, and
$macron(M) = k times.o_cal(O) M = M slash pi M$ as a $macron(Lambda)$-module. If
$K$ is a splitting field for $hat(Lambda)$ and $k$ is a splitting field for
$macron(Lambda)$, we say that $(K, cal(O), k)$ is a *splitting p-modular
system*#idx("splitting", "$p$-modular system") for $Lambda$.

We call $hat(Lambda)$-modules *ordinary representations*#idx(
  "ordinary",
  "representation",
)#idx("representation", "ordinary"), $Lambda$-lattices *integral
representations*#idx("integral representation")#idx(
  "representation",
  "integral",
) and $macron(Lambda)$-modules *modular representations*#idx(
  "modular",
  "representation",
)#idx("representation", "modular").

#lemma[
  If $V$ is a $hat(Lambda)$-module then there is a $Lambda$-lattice $M$ with
  $hat(M) tilde.equiv V$.
] <lem:lattice-form>

#proof[
  Choose a basis $v_1, dots, v_n$ for $V$ as a vector space over $K$ and let
  $M = Lambda v_1 + dots.c + Lambda v_n subset.eq V$. As an $cal(O)$-module, $M$
  is finitely generated and torsion free, and hence free. Choose a free basis
  $x_1, dots, x_m$. Then the $x_i$ span $V$ and are $K$-independent, and hence
  $m = n$, and $V = K times.o_cal(O) M$.
]

#source(30)Such a $Lambda$-lattice $M$ is called an $cal(O)$-*form*#idx("form")
of $V$. In general a $hat(Lambda)$-module has many non-isomorphic
$cal(O)$-forms.

#lemma(title: [Fitting's lemma, $frak(p)$-adic version])[
  Let $M$ be a $Lambda$-lattice and suppose that $f in End_Lambda (M)$. Write
  $Im(f^infinity) = inter.big_(n=1)^infinity Im(f^n)$ and
  $Ker(f^infinity) = {x in M | forall n gt.eq 0 med exists m gt.eq 0 "s.t."
    f^m (x) in J(Lambda)^n M}$. Then
  $ M = Im(f^infinity) plus.o Ker(f^infinity). $
] <lem:fitting-p-adic>
#idx("Fitting's lemma", target: [@lem:fitting-p-adic])#idx(
  "lemma",
  "Fitting's",
  target: [@lem:fitting-p-adic],
)

#proof[
  This follows from the usual version of Fitting's lemma.
]

#theorem(title: [Krull–Schmidt theorem, $frak(p)$-adic version])[
  + If $M$ is an indecomposable $Lambda$-lattice then $End_Lambda (M)$ is a
    local ring.
  + The unique decomposition property holds for $Lambda$-lattices.
] <th:krull-schmidt-p-adic>
#idx("Krull–Schmidt theorem", target: [@th:krull-schmidt-p-adic])#idx(
  "theorem",
  "Krull–Schmidt",
  target: [@th:krull-schmidt-p-adic],
)

#proof[
  The proof of (i) is the same as the proof of @lem:indecomposable-local, and
  (ii) follows by Theorem~@th:local-endomorphisms-unique-decomposition.
]

#theorem(title: [Idempotent refinement])[
  + Let $e$ be an idempotent in $macron(Lambda)$. Then there is an idempotent
    $f$ in $Lambda$ with $e = macron(f)$. If $e_1$ is conjugate to $e_2$ in
    $macron(Lambda)$, $macron(f)_1 = e_1$ and $macron(f)_2 = e_2$ then $f_1$ is
    conjugate to $f_2$ in $Lambda$.
  + Let $1 = e_1 + dots.c + e_n$ with the $e_i$ primitive orthogonal idempotents
    in $macron(Lambda)$. Then we can write $1 = f_1 + dots.c + f_n$ with the
    $f_i$ primitive orthogonal idempotents in $Lambda$ and $macron(f)_i = e_i$.
    If $e_i$ is conjugate to $e_j$ then $f_i$ is conjugate to $f_j$.
  + Let $1 = e_1 + dots.c + e_n$ with the $e_i$ primitive central idempotents in
    $macron(Lambda)$. Then we can write $1 = f_1 + dots.c + f_n$ with the $f_i$
    primitive central idempotents in $Lambda$ and $macron(f)_i = e_i$.
] <th:idempotent-refinement-p-adic>
#idx(
  "idempotent",
  "refinement theorem",
  target: [@th:idempotent-refinement-p-adic],
)#idx(
  "theorem",
  "idempotent refinement",
  target: [@th:idempotent-refinement-p-adic],
)

#proof[
  + We may apply the idempotent refinement theorem~@th:idempotent-refinement for
    nilpotent ideals to obtain idempotents $f_i in Lambda slash pi^i Lambda$
    whose image in $Lambda slash pi^(i-1) Lambda$ is $f_(i-1)$. These define an
    element of
    $Lambda = invlim_n Lambda slash pi^n Lambda$
    which is easily seen to be idempotent.

    The conjugacy statement is proved exactly as in @th:idempotent-refinement.
  + Apply the same argument to Corollary~@cor:idempotent-refinement.
  + Lift each $e_i$ to an idempotent $f_i$ in $Lambda$. Then
    $f_i Lambda(1 - f_i)$ is contained in $J(cal(O)) f_i Lambda(1 - f_i)$. Thus
    Nakayama's Lemma implies that $f_i Lambda(1 - f_i) = 0$. By symmetry, we
    also have $(1 - f_i) Lambda f_i = 0$. This implies that $f_i$ is central in
    $Lambda$.
]

It follows from the above theorem that the decomposition of the regular
representation $lmodule(macron(Lambda), macron(Lambda))$ into projective
indecomposable modules lifts to a decomposition of $lmodule(Lambda, Lambda)$. So
given a simple $macron(Lambda)$-module $S_j$, it has a projective cover
$P_j = macron(Q)_j$ for some projective indecomposable $Lambda$-module $Q_j$
unique up to isomorphism.

#definition[
  Suppose that $V_1, dots, V_t$ are representatives for the isomorphism classes
  of irreducible $hat(Lambda)$-modules, and $M_1, dots, M_t$ are $cal(O)$-forms
  of them (see the above lemma). Then we define the *decomposition number*#idx(
    "decomposition",
    "number",
  ) $d_(i j)$#idx("$d_(i j)$") to be the multiplicity of $S_j$ as a composition
  factor of $macron(M)_i$.
] <def:decomposition-number>

#source(31)The following proposition shows that the decomposition numbers are
independent of the choices of $cal(O)$-forms.

#proposition[
  Suppose that $(K, cal(O), k)$ is a splitting system for $Lambda$, and that
  $hat(Lambda)$ is semisimple. Then $d_(i j)$ is the multiplicity of $V_i$ as a
  composition factor of $hat(Q)_j$. In particular
  $ c_(i j) = sum_k d_(k i) d_(k j). $#idx("$c_(i j)$")
] <prop:decomposition-numbers>

#proof[
  We have
  $
    d_(i j) & = dim_k Hom_(macron(Lambda)) (P_j, macron(M)_i) quad
              "by" #[@lem:multiplicity-projective] \
            & = rank_cal(O) Hom_Lambda (Q_j, M_i) quad "since" Q_j
              "is projective" \
            & = dim_K Hom_(hat(Lambda)) (hat(Q)_j, V_i)
  $
  which is equal to the multiplicity of $V_i$ as a composition factor of
  $hat(Q)_j$ since $hat(Lambda)$ is semisimple.
]

#remark(kind: "Remarks")[
  + Note carefully what this proposition is saying. It is saying that the
    decomposition matrix can be read in two different ways. The rows give the
    modular composition factors of modular reductions of the ordinary
    irreducibles, while the columns give the ordinary composition factors of
    lifts of the modular projective indecomposables. It is thus clear that the
    decomposition matrix times its transpose gives the modular irreducible
    composition factors of the modular projective indecomposables, namely the
    Cartan matrix.
  + If $Lambda$ is a group ring, we shall see in Chapter~@ch:group-algebras that
    $hat(Lambda)$ is semisimple, so that this proposition applies in this case.
  + This proposition makes it clear that the decomposition numbers $d_(i j)$ are
    independent of the choice of $cal(O)$-form $M_i$ chosen for the $V_i$.
  + It also follows from this proposition that the Cartan matrix $(c_(i j))$ is
    symmetric in this case. This is not true for more general algebras, even
    over splitting systems.
  + In case $(K, cal(O), k)$ is not a splitting system, a modification of the
    above proposition is true. Namely the multiplicity of $V_i$ as a composition
    factor of $hat(Q)_j$ is
    $
      d_(i j) . dim_k End_(macron(Lambda)) (S_j) slash
      dim_K End_(hat(Lambda)) (V_i)
    $
    and so
    $
      c_(i j) = sum_k d_(k i) d_(k j) . dim_k End_(macron(Lambda)) (S_j) slash
      dim_K End_(hat(Lambda)) (V_k).
    $
    The proof is the same.
]
