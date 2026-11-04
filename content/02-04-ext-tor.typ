#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-04-ext-tor.typ": comparison, lifting

== Ext and Tor <sec:ext-tor>

Our first application of the theory of chain complexes and homology is to define
functors Ext#idx("Ext") and Tor#idx("Tor") for modules over a ring. We shall
interpret Ext in terms of extensions of modules.

#source(43)

#definition[
  A *projective resolution*#idx("projective", "resolution")#idx(
    "resolution",
    "projective",
  ) of a $Lambda$-module $M$ is a long exact sequence
  $
    dots.c -> P_2 stretch(-->)^(partial_2) P_1
    stretch(-->)^(partial_1) P_0
  $
  of modules with the $P_n$ projective and with
  $P_0 slash Im(partial_1) tilde.equiv M$. In other words, the sequence
  $ dots.c -> P_2 -> P_1 -> P_0 -> M -> 0 $
  is exact. Since every module is a homomorphic image of a free module,
  projective resolutions always exist.
] <def:projective-resolution>

We shall regard the sequences in the above definition as chain complexes. The
module $M$ appears in degree $-1$ in the second sequence.

#theorem(title: [Comparison theorem])[
  Any map of modules $M -> M'$ can be extended to a map of projective
  resolutions
  $
    #comparison
  $

  Given any two such maps ${f_n}$ and ${f'_n}$, there is a chain homotopy
  $h_n: P_n -> Q_(n+1)$, so that
  $f_n - f'_n = partial'_(n+1) compose h_n + h_(n-1) compose partial_n$.
] <th:comparison>
#idx("comparison theorem", target: [@th:comparison])#idx(
  "theorem",
  "comparison",
  target: [@th:comparison],
)

#proof[
  We construct the $f_n: P_n -> Q_n$ inductively as follows. Since
  $
    partial'_(n-1) compose f_(n-1) compose partial_n
    = f_(n-2) compose partial_(n-1) compose partial_n = 0,
  $
  we have
  $
    #lifting
  $
  and so we can find a map $f_n: P_n -> Q_n$ with
  $partial'_n compose f_n = f_(n-1) compose partial_n$.

  We also construct the $h_n$ inductively. We have
  $
    partial'_n compose (f_n - f'_n - h_(n-1) compose partial_n)
    & = (f_(n-1) - f'_(n-1) - partial'_n compose h_(n-1)) compose partial_n \
    & = h_(n-2) compose partial_(n-1) compose partial_n = 0
  $
  and so we may find a map $h_n: P_n -> Q_(n+1)$ with
  $f_n - f'_n - h_(n-1) compose partial_n = partial'_(n+1) compose h_n$.
]

#remark[
  The proof of the above theorem did not use all the hypotheses. It suffices for
  the upper complex to consist of projective modules but it need not be exact,
  and for the lower complex to be exact but not necessarily to consist of
  projective modules. We shall sometimes use this stronger form of the theorem.
]

#source(44)If $M'$ is a right $Lambda$-module and
$
  dots.c -> P_2 stretch(-->)^(partial_2) P_1
  stretch(-->)^(partial_1) P_0
$
is a projective resolution of a left $Lambda$-module $M$, we have a chain
complex
$
  dots.c M' times.o_Lambda P_2 stretch(-->)^(1 times.o partial_2)
  M' times.o_Lambda P_1 stretch(-->)^(1 times.o partial_1)
  M' times.o_Lambda P_0.
$
This complex is no longer necessarily exact, although it is clear that
$(1 times.o partial_(n-1)) compose (1 times.o partial_n) = 0$.

It follows from the above theorem that this complex is independent of choice of
projective resolution, up to chain homotopy equivalence. Thus the homology
groups are independent of this choice, and we define
$ Tor_n^Lambda (M', M) = H_n (M' times.o bold(P), 1 times.o partial_*). $

Similarly if $M'$ is a left $Lambda$-module and
$
  dots.c -> P_2 stretch(-->)^(partial_2) P_1
  stretch(-->)^(partial_1) P_0
$
is a projective resolution of a left $Lambda$-module $M$, we have a cochain
complex
$
  Hom_Lambda (P_0, M') stretch(-->)^(delta^0) Hom_Lambda (P_1, M')
  stretch(-->)^(delta^1) Hom_Lambda (P_2, M') -> dots.c
$
where $delta^n$ is given by composition with $partial_(n+1)$. This complex is
independent of choice of projective resolution, up to chain homotopy
equivalence. Thus its cohomology groups are independent of this choice, and we
define
$ Ext_Lambda^n (M, M') = H^n (Hom_Lambda (bold(P), M'), delta^*). $
Note that $Tor_0^Lambda (M', M) = M' times.o_Lambda M$ and
$Ext_Lambda^0 (M, M') = Hom_Lambda (M, M')$.

#example[
  In case $Lambda = ZZ$, a $Lambda$-module is the same as an abelian group.
  Since every subgroup of a free abelian group is again a free abelian group, it
  follows that every module has a projective resolution of length one (i.e.,
  $P_n = 0$ for $n >= 2$), and so $Tor_n^ZZ$ and $Ext_ZZ^n$ are zero for
  $n >= 2$.

  It was conjectured by J.~H.~C. Whitehead#idx("Whitehead's conjecture")#idx(
    "conjecture",
    "Whitehead's",
  ) that if $Ext_ZZ^1 (A, ZZ) = 0$ then $A$ is free as an abelian group. It is
  now known, thanks to the extraordinary work of S. Shelah [@bib:Shelah1974]
  that the truth of this conjecture _depends on the set theory being used!_
]

#remark(kind: "Remarks")[
  + If $M$ is projective, then $bold(P)$ can be taken to be non-zero only in
    degree zero, and equal to $M$ there, so that in this case
    $Ext_Lambda^n (M, M')$ and $Tor_n^Lambda (M', M)$ are zero for $n > 0$.
  + We write $tilde(Omega)^n (M)$#idx(
      "$tilde(Omega)^n (M)$, $tilde(Omega)^(-n) (M)$",
    ) for $Ker(partial_(n-1))$ in a projective resolution of $M$. Note that by
    Schanuel's lemma if $tilde(Omega)^n (M)'$ is defined similarly using another
    projective resolution of $M$ then there are projective modules $P$ and $P'$
    with
    $tilde(Omega)^n (M) plus.o P' tilde.equiv tilde(Omega)^n (M)' plus.o P$. If
    $M$ is finitely generated and the Krull–Schmidt theorem holds for finitely
    generated $Lambda$-modules then there is a unique *minimal resolution*#idx(
      "minimal resolution",
    )#idx("resolution", "minimal") of $M$, and we write $Omega^n (M)$#idx(
      "$Omega^n (M)$, $Omega^(-n) (M)$",
    ) for $Ker(partial_(n-1))$ in this particular resolution.

    Dually we write $tilde(Omega)^(-n) (M)$ for the $n$th cokernel in an
    injective resolution, and $Omega^(-n) (M)$ if the resolution is minimal.
  + #source(45)The discussion above of Ext and Tor is a particular case of the
    concept of *derived functors*#idx("derived functors")#idx(
      "functor",
      "derived",
    ). Suppose that $cal(A)$ and $cal(B)$ are abelian categories and that every
    object in $cal(A)$ is a quotient of a projective object. If
    $F: cal(A) -> cal(B)$ is a covariant additive functor, and $M$ is an object
    in $cal(A)$, we form a projective resolution
    $
      dots.c -> P_2 stretch(-->)^(partial_2) P_1
      stretch(-->)^(partial_1) P_0
    $
    of $M$, apply $F$ to obtain a chain complex
    $
      dots.c -> F(P_2) stretch(-->)^(F(partial_2)) F(P_1)
      stretch(-->)^(F(partial_1)) F(P_0)
    $
    whose homology groups are the *left derived functors*#idx(
      "left",
      "derived functors",
    )#idx("functor", "left derived")
    $ L_n F(M) = H_n (F(bold(P)), F(partial_*)). $
    Using the comparison theorem in the same way as before, we see that these
    are independent of the choice of resolution. If $F$ is right exact then
    $L_0 F(M) = F(M)$. Thus for example the left derived functors of
    $M' times.o_Lambda -$ are
    $ L_n (M' times.o_Lambda -) = Tor_n^Lambda (M', -). $

    Similarly, the *right derived functors*#idx(
      "right",
      "derived functors",
    )#idx("functor", "right derived") of the covariant additive functor $F$ are
    defined by applying $F$ to an injective resolution
    $
      I_0 stretch(-->)^(delta^0) I_1
      stretch(-->)^(delta^1) I_2 -> dots.c
    $
    of $M$. The right derived functors are then the cohomology groups
    $ R^n F(M) = H^n (F(bold(I)), F(delta^*)). $
    If $F$ is left exact then $R^0 F(M) = F(M)$.

    For contravariant functors, the left derived functors are defined using an
    injective resolution and the right derived functors are defined using a
    projective resolution. Thus for example the right derived functors of
    $Hom_Lambda (-, M')$ are $R^n Hom_Lambda (-, M') = Ext_Lambda^n (-, M')$.

    The reader may wonder why we have not discussed $L_n (- times.o_Lambda M)$
    and $R^n Hom_Lambda (M, -)$. This is because it turns out that we get
    nothing but Tor and Ext again, as we shall see in Proposition~@prop:balance.
]

#proposition[
  Suppose that $Lambda$ is Artinian, and $P = Lambda e$ and $P' = Lambda e'$ are
  projective indecomposable $Lambda$-modules, so that $P slash Rad(P) = S$ and
  $P' slash Rad(P') = S'$ are simple (by the idempotent refinement theorem).
  Then
  $ Ext_Lambda^1 (S, S') tilde.equiv Hom_Lambda (Rad(P) slash Rad^2(P), S'). $

  As an $End_Lambda (S')$-$End_Lambda (S)$-bimodule this is dual to the
  $End_Lambda (S)$-$End_Lambda (S')$-bimodule
  $e' J(Lambda) e slash e' J^2(Lambda) e$. In particular, if $Lambda$ is a
  finite dimensional algebra over a field $k$, then
  $
    dim_k Ext_Lambda^1 (S, S') = dim_k (e' J(Lambda) e slash e' J^2(Lambda) e).
  $
] <prop:ext-one-simple>

#source(46)

#proof[
  If $Rad(P) slash Rad^2(P) = plus.o.big_i n_i S_i$ as a direct sum of simple
  modules, then letting $P_i slash Rad(P_i) = S_i$, the minimal projective
  resolution of $S$ has the form
  $ dots.c -> plus.o.big_i n_i P_i -> P $
  and so
  $
    Ext_Lambda^1 (S, S') tilde.equiv Hom_Lambda (plus.o.big_i n_i P_i, S')
    tilde.equiv Hom_Lambda (plus.o.big_i n_i S_i, S')
  $
  which we can rewrite as $Hom_Lambda (Rad(P) slash Rad^2(P), S')$. This is dual
  to
  $
    & Hom_Lambda (S', Rad(P) slash Rad^2(P))
      tilde.equiv Hom_Lambda (P', Rad(P) slash Rad^2(P)) \
    & quad quad tilde.equiv Hom_Lambda (P', Rad(P))
      slash Hom_Lambda (P', Rad^2(P))
      tilde.equiv e' J(Lambda) e slash e' J^2(Lambda) e
  $
  by Lemma~@lem:idempotent-hom.
]

#subhead[Augmented algebras]

#definition[
  An *augmented algebra*#idx("augmented algebra")#idx("algebra", "augmented")
  $Lambda$ over a commutative ring of coefficients $R$ is an algebra together
  with a surjective *augmentation map*#idx("augmentation map")
  $epsilon: Lambda -> R$ of $R$-algebras.
] <def:augmented-algebra>

If $Lambda$ is an augmented algebra, then $R$ may be given the structure of a
left $Lambda$-module via $lambda(x) = epsilon(lambda) x$, and of a right
$Lambda$-module via $(x) lambda = epsilon(lambda) x$.

We define the *homology groups*#idx("homology", "of an augmented algebra") of
$Lambda$ with coefficients in a right $Lambda$-module $M$ to be
$ H_n (Lambda, M) = Tor_n^Lambda (M, R) $
and the *cohomology groups*#idx("cohomology", "of an augmented algebra") of
$Lambda$ with coefficients in a left $Lambda$-module $M$ to be
$ H^n (Lambda, M) = Ext_Lambda^n (R, M). $
The special case $M = R$ is of particular importance, since as we shall see in
Section~@sec:extensions, there is a ring structure in this case.

#remark[
  Suppose that $R -> R'$ is a homomorphism of coefficient rings, and $Lambda$ is
  projective as an $R$-module. Then tensoring with $R'$ will take a projective
  resolution of $R$ as a $Lambda$-module to a projective resolution of $R'$ as
  an $R' times.o_R Lambda$-module. Thus we have
  $
    H_n (Lambda, R') tilde.equiv H_n (R' times.o_R Lambda, R'),
    quad H^n (Lambda, R') tilde.equiv H^n (R' times.o_R Lambda, R').
  $
]

#exercise[
  Show that Ext and Tor are bilinear in the sense that there are natural
  isomorphisms
  $
    Ext_Lambda^n (M plus.o M', M'')
    & tilde.equiv Ext_Lambda^n (M, M'') plus.o Ext_Lambda^n (M', M'') \
    Ext_Lambda^n (M, M' plus.o M'')
    & tilde.equiv Ext_Lambda^n (M, M') plus.o Ext_Lambda^n (M, M'')
  $
  and similarly for $Tor_n^Lambda$.
]
