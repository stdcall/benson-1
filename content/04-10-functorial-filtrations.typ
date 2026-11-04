#import "main-defs.typ": *
#import "statements.typ": *

== Functorial filtrations <sec:functorial-filtrations>

#definition[
  A functor $F in bold("Fun")(Lambda)$ is said to *reflect isomorphisms*#idx(
    "reflecting isomorphisms",
  )#idx("isomorphism", "reflecting") if a homomorphism $f : M -> M'$ in
  $lmodule(Lambda, bold("mod"))$ is an isomorphism if and only if
  $F(f) : F(M) -> F(M')$ is an isomorphism. For example, the underlying vector
  space functor reflects isomorphisms. Note in particular that if $F$ reflects
  isomorphisms and $M != 0$ then $F(M) != 0$.
] <def:reflect-isomorphisms>

#lemma[
  If $F$ is a functor which reflects isomorphisms then $F$ has every simple
  functor $S_M$ as a subquotient.
] <lem:simple-subquotients>

#proof[
  If $M$ is a finitely generated indecomposable module, then by Yoneda's lemma
  $ Nat((M, -), F) tilde.equiv F(M) != 0 $
  and so there is a non-zero natural transformation from $(M, -)$ to $F$. The
  image of this modulo the image of $Rad(M, -)$ is the desired subquotient.
]

#definition[
  A collection of subquotients, or *intervals*#idx("interval")
  $F'_alpha slash F''_alpha$ of a functor $F in bold("Fun")(Lambda)$ is said to
  *cover* $F$ if given any $M in lmodule(Lambda, bold("mod"))$ and $x in F(M)$
  there is an index $alpha$ with $x in F'_alpha (M)$ but
  $x in.not F''_alpha (M)$. Two intervals $F'_alpha slash F''_alpha$ and
  $F'_beta slash F''_beta$ are said to *avoid* each other if either
  $F'_beta <= F''_alpha$ or $F''_beta >= F'_alpha$. A *filtration*#idx(
    "filtration, functorial",
  )#idx("functorial filtration") of $F$ is a collection of intervals covering
  $F$ and avoiding each other.
] <def:filtration>

#lemma[
  #source(145)Suppose $F$ is a functor which reflects isomorphisms and
  $F'_alpha slash F''_alpha$ is a collection of intervals covering $F$. Then
  $f : M -> M'$ is an isomorphism if and only if $(F'_alpha slash F''_alpha)(f)$
  is an isomorphism for each index $alpha$.
] <lem:intervals-detect-isomorphisms>

#proof[
  Suppose $(F'_alpha slash F''_alpha)(f)$ is an isomorphism for each $alpha$.
  Since the $F'_alpha slash F''_alpha$ cover $F$, it follows that $F(f)$ is an
  isomorphism. Since $F$ reflects isomorphisms, $f$ is an isomorphism.
]

#lemma[
  Suppose ${M_alpha}$ is a complete set of representatives of the isomorphism
  classes of finitely generated indecomposable $Lambda$-modules, and ${S_alpha}$
  are the corresponding simple functors. Then we have the following:
  + $S_alpha (M_beta) tilde.equiv cases(
      End_Lambda (M_beta) slash J End_Lambda (M_beta) & quad "if" alpha = beta,
      0 & quad "otherwise."
    )$
  + A homomorphism $f : M -> M'$ in $lmodule(Lambda, bold("mod"))$ is an
    isomorphism if and only if $S_alpha (f)$ is an isomorphism for each $alpha$.
] <lem:simple-functors>

#proof[
  + This is clear from the discussion earlier in this section.
  + If $f : M -> M'$ is not an isomorphism then it is either not injective or
    not surjective. If it is not injective then some indecomposable summand
    $M_alpha$ of $M$ intersects the kernel non-trivially, and then $S_alpha (f)$
    is not an isomorphism. Similarly if $f$ is not surjective then some
    indecomposable summand $M_beta$ of $M'$ is not contained in the image, and
    then $S_beta (f)$ is not an isomorphism.
]

#remark[
  The number of times a simple functor $S_M$ occurs in a filtration of the
  underlying vector space functor is equal to the dimension of $M$ (over the
  division ring $End_Lambda (M) slash J End_Lambda (M)$) by part (i) of the
  above lemma. So when we filter the underlying vector space functor we should
  expect to have this many repetitions of the simple functors, and it is
  important to discard all except one copy at some stage so that the list of
  functors obtained can satisfy (i).
]

We now present a naïve form of the functorial filtration method, and then we
state the method in the generality we need. For convenience we state the
following proposition over an algebraically closed field.

#proposition[
  Let $Lambda$ be a finite dimensional algebra over an algebraically closed
  field $k$.

  Suppose ${M_alpha}$ is a collection of finitely generated $Lambda$-modules and
  ${S_alpha}$ is a collection of functors in $bold("Fun")(Lambda)$ such that
  + $S_alpha (M_beta) tilde.equiv cases(
      k & quad "if" alpha = beta,
      0 & quad "otherwise."
    )$
  + $S_alpha (M)$ is finite dimensional for all finitely generated
    $Lambda$-modules $M$, so that $S_alpha (M) times.o_k M_alpha$ makes sense as
    a finitely generated $Lambda$-module and has the property that
    $S_alpha (S_alpha (M) times.o M_alpha) tilde.equiv S_alpha (M)$. Moreover,
    for every finitely generated $Lambda$-module $M$ there is a map
    $gamma_(alpha, M) : S_alpha (M) times.o M_alpha -> M$ such that
    $S_alpha (gamma_(alpha, M))$ is an isomorphism.
  + #source(146)A map $f : M -> M'$ in $lmodule(Lambda, bold("mod"))$ is an
    isomorphism if and only if $S_alpha (f)$ is an isomorphism for all indices
    $alpha$.
  + For any finitely generated $Lambda$-module $M$, only finitely many of the
    $S_alpha (M)$ are non-zero.

  Then the $M_alpha$ are indecomposable and form a complete set of
  representatives of the isomorphism classes of finitely generated
  indecomposable $Lambda$-modules without repetitions.
] <prop:functorial-filtration>

#proof[
  Suppose $M$ is a finitely generated $Lambda$-module. By (iv), the sum
  $plus.o.big_alpha S_alpha (M) times.o M_alpha$ is a finitely generated
  $Lambda$-module. By (ii) there is a natural map
  $
    sum_alpha gamma_(alpha, M) :
    plus.o.big_alpha S_alpha (M) times.o M_alpha -> M
  $
  and by (i) $S_beta (sum_alpha gamma_(alpha, M))$ is an isomorphism for each
  $beta$. So by (iii) $sum_alpha gamma_(alpha, M)$ is an isomorphism. Thus every
  finitely generated $Lambda$-module is uniquely expressible as a direct sum of
  modules $M_alpha$ from the given list. In particular, these must be
  indecomposable and form a complete list of representatives of the isomorphism
  classes of indecomposable finitely generated $Lambda$-modules without
  repetition.
]

#remark(kind: "Remarks")[
  + One of the remarkable things about this proposition is that we do not have
    to demonstrate explicitly that the $M_alpha$ are indecomposable or
    non-isomorphic in order to satisfy the hypotheses of the proposition.
  + Condition (ii) of the proposition is implied by the existence of a
    surjective natural transformation $(M_alpha, -) arrow.r.squiggly S_alpha$
    for each $alpha$, but is sometimes easier to check. The reason for this
    implication is as follows. Let $x_alpha in S_alpha (M_alpha)$ correspond to
    the given natural transformation via Yoneda's lemma. Since the natural
    transformation is surjective, given a finitely generated $Lambda$-module $M$
    and a basis ${v_(alpha, j)}$ for $S_alpha (M)$ for each $alpha$, we can find
    homomorphisms $gamma_(alpha, j, M) : M_alpha -> M$ such that
    $S_alpha (gamma_(alpha, j, M))(x_alpha) = v_(alpha, j)$. Then we take
    $gamma_(alpha, M) = sum_j gamma_(alpha, j, M) :
    S_alpha (M) times.o M_alpha -> M$.
  + Condition (iii) is guaranteed if there is a functor $F$ which reflects
    isomorphisms and a set of intervals covering $F$ and each isomorphic to some
    $S_alpha$.
  + If we filter the underlying vector space functor then only finitely many of
    the intervals can be non-zero on a given finitely generated $Lambda$-module,
    since the underlying vector space is finite dimensional.
]

#example[
  The group algebra of a cyclic $p$-group over an algebraically closed field of
  characteristic $p$ is of the form $Lambda = k[T] slash (T^n)$, where $n$ is
  the order of the group and $T$ is of the form $g - 1$ for a generator $g$. It
  is easy to classify the modules for this algebra using Jordan canonical forms,
  but we shall use it as an example to illustrate the functorial filtration
  method.

  As our modules we take $M_i = k[T] slash (T^i)$, a uniserial $Lambda$-module
  of dimension $i$ for $1 <= i <= n$. We have functors
  $ F_(i j) = Ker(T^i) inter (Im(T^j) + Ker(T^(i-1))) in bold("Fun")(Lambda). $
  #source(147)Since $Ker(T^i) supset.eq Im(T^j)$ if $i >= n - j$, we have
  $F_(i+1, n-i) (M) = Ker(T^i) = F_(i, 0) (M)$, and so we only consider the
  $F_(i j)$ with $i <= n - j$. If $M$ is a $Lambda$-module with underlying
  vector space $V$, we have the inclusions
  $
    #aligned-rows(
      ($$, $V = F_(n, 0) (M) supset.eq (F_(n, 1) (M) =) F_(n-1, 0) (M)
      supset.eq F_(n-1, 1) (M)$),
      ($$, $quad supset.eq (F_(n-1, 2) (M) =) F_(n-2, 0) (M) supset.eq dots.c
      supset.eq F_(1, n-1) (M) supset.eq F_(1, n) (M) = 0.$),
    )
  $
  Moreover, if $n - j >= i > 1$, the action of $T$ induces an isomorphism from
  $F_(i, j-1) slash F_(i, j)$ to $F_(i-1, j) slash F_(i-1, j+1)$. Thus if we
  take as our functors $S_i = F_(i, 0) slash F_(i, 1) tilde.equiv dots.c
  tilde.equiv F_(1, i-1) slash F_(1, i)$, then $S_i$ appears as an interval in
  our filtration exactly $i$ times. Since $(M_i, -) = Ker(T^i) = F_(i, 0)$, each
  $S_i$ is a quotient of $(M_i, -)$ and so condition (ii) is satisfied according
  to remark (ii). The other conditions are easily checked using the other
  remarks. So we may conclude that the $M_i$ form a complete list of
  representatives of the isomorphism classes of indecomposable $Lambda$-modules,
  without repetitions.
]

The following is the form of the functorial filtration theorem used by Ringel
[@bib:Ringel1975b] for his classification of the indecomposable modules for the
dihedral 2-groups. The point of this version is that it allows for the
classification of entire one parameter families of modules at a time. We shall
give an outline of Ringel's classification in the next section.

#theorem[
  Let $bold(M)$ and $bold(A)_alpha$ be abelian categories, and let
  $S_alpha : bold(M) -> bold(A)_alpha$ and $T_alpha : bold(A)_alpha -> bold(M)$
  be additive functors such that the following conditions are satisfied.
  + $S_alpha T_beta = cases(
      id_(bold(A)_alpha) & quad "if" alpha = beta,
      0 & quad "otherwise."
    )$
  + For every $M$ in $bold(M)$ there is a map
    $gamma_(alpha, M) : T_alpha S_alpha (M) -> M$ such that
    $S_alpha (gamma_(alpha, M))$ is an isomorphism.
  + A map $f : M -> M'$ in $bold(M)$ is an isomorphism if and only if
    $S_alpha (f)$ is an isomorphism for all indices $alpha$.
  + For any $M$ in $bold(M)$, only finitely many of the $S_alpha (M)$ are
    non-zero.

  Then the objects $T_alpha (A)$ with $A$ indecomposable in $bold(A)_alpha$, are
  indecomposable and form a complete set of representatives of the isomorphism
  classes of indecomposable objects in $bold(M)$ without repetitions.
] <th:functorial-filtration>

#proof[
  The proof is exactly the same as the proof of the above proposition.
]

Note that we are interested in the case where $bold(M)$ is the category of
finite dimensional $Lambda$-modules for some algebra $Lambda$. The
$bold(A)_alpha$ are things like the category of finite dimensional vector spaces
or the category of finite dimensional $k[T]$-modules. The latter will be used to
capture entire one parameter families of modules at once.
