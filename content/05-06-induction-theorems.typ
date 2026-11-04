#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/05-06-induction-theorems.typ": (
  artin-square, brauer-square, conlon-square, dress-square,
)

#source(197)
== Induction theorems <sec:induction-theorems>
#idx("induction", "theorem", target: [@sec:induction-theorems])#idx(
  "theorem",
  "induction",
  target: [@sec:induction-theorems],
)

As an application of the theory of Burnside rings and trivial source rings, we
shall prove some induction theorems in representation theory. Each of these
theorems says that a representation ring can be written as a sum of the images
of induction from a certain class of subgroups. Which class of subgroups is
involved depends on whether we look at the full representation ring or just the
Grothendieck ring, and what coefficients we allow in the representation ring.
The four induction theorems we have in mind are:
#enum(
  numbering: "A)",
  [Artin's induction theorem,],
  [Brauer's induction theorem,],
  [Conlon's induction theorem,],
  [Dress' induction theorem.],
)
The first two of these are theorems about Grothendieck rings, while the last two
are about representation rings.

The approach we shall be taking was communicated to me by Ken Brown, to whom I
am very grateful for permission to use this material here. It is a distillation
of ideas of many people, and I am sure they'll not feel too hurt if they are not
mentioned here.

#theorem(title: [Artin's induction theorem])[
  Suppose $k$ is a field. Then
  $
    CC times.o_ZZ cal(R)(k G) = sum_((g) lt.eq G)
    Im(ind_((g), G)).
  $
  Here, $chevron.l g chevron.r$ runs over the cyclic subgroups#idx(
    "cyclic",
    "subgroups",
  )#idx("subgroups", "cyclic") of $G$ if $k$ has characteristic zero, and the
  cyclic subgroups of order prime to the characteristic otherwise.
] <th:artin-induction>
#idx("Artin's induction theorem", target: [@th:artin-induction])#idx(
  "induction",
  "theorem",
  "Artin's",
  target: [@th:artin-induction],
)#idx("theorem", "Artin's induction", target: [@th:artin-induction])#idx(
  "theorem",
  "induction",
  "Artin's",
  target: [@th:artin-induction],
)

#proof[
  The proof of this theorem is easy, and will be our model for proving the other
  induction theorems. We start off by writing down a commutative diagram:
  $ #artin-square $

  In this diagram, $phi.alt$ is the map which takes a permutation representation
  to the matrix representation with the permuted points as basis. The elements
  $g$ run through a set of representatives of the conjugacy classes of elements
  of $G$ if $k$ has characteristic zero, and the conjugacy classes of elements
  of order prime to the characteristic otherwise. The horizontal maps are the
  ones given in Proposition~@prop:ordinary-character-homomorphisms,
  Theorem~@th:brauer-character-homomorphisms and
  Theorem~@th:burnside-ring-homomorphisms. Write $epsilon_H$ for the primitive
  idempotents in the top right hand corner of this diagram, and $epsilon_g$ for
  the primitive idempotents in the bottom right. Recall that $e_H$ is the
  preimage in $B(G)$ of $epsilon_H$. The map $lambda$ takes a primitive
  idempotent $epsilon_H$ to $sum_((g) = H) epsilon_g$ if $H$ is cyclic, and 0
  otherwise. It is an easy exercise to check that #source(
    198,
  )this diagram commutes. One proceeds coordinate at a time, and one uses the
  fact that the trace of a group element on a permutation representation is
  equal to the number of fixed points.

  It follows that $phi.alt(e_H) = 0$ unless $H$ is cyclic. But in
  Section~@sec:burnside-ring we showed that $e_H in Im(ind_(H, G))$. So applying
  $phi.alt$ to the equation
  $ 1 = sum_(H lt.eq_G G) e_H $
  in $B(G)$, we obtain the equation
  $ 1 = sum_(H lt.eq_G G \ "cyclic") phi.alt(e_H) $
  in $CC times.o_ZZ cal(R)(G)$. In particular, we have
  $
    1 in sum_((g) lt.eq G)
    Im(ind_((g), G)).
  $
  However, by the identity
  $ ind_(H, G) (a.res_(G, H) (b)) = ind_(H, G) (a).b $
  this sum of images of induction maps is an ideal in $CC times.o_ZZ cal(R)(G)$.
  Artin's induction theorem now follows from the fact that an ideal containing
  the identity element must be the whole ring.
]

We now turn our attention to Brauer's induction theorem. This time, we work with
integer, rather than complex coefficients in our representation rings. However,
since $b(G)$ does not have many idempotents (see Section~@sec:burnside-ring), we
must work with $q$-local coefficients as an intermediate step, where $q$ is a
prime which may or may not equal the characteristic of $k$.
$ #brauer-square $

Recall from Section~@sec:burnside-ring that the primitive idempotents in
$b(G)_((q))$ are of the form
$ sum_(O^q (H) = H_0) e_H $
where $H$ runs through representatives of conjugacy classes of subgroups of $G$
for which $O^q (H)$ is a given $q$-perfect subgroup $H_0$ of $G$. Now $phi.alt$
kills such an idempotent if $H_0$ is non-cyclic. So in $cal(R)(G)_((q))$ we have
$
  1 = sum_(H_0 "cyclic") scaled((sum_(O^q (H) = H_0) phi.alt(e_H))).
$

#definition[
  #source(199)A group $H$ is $q$*-hyperelementary*#idx(
    "hyperelementary group",
  )#idx("group", "hyperelementary") if $O^q (H)$ is cyclic. In other words, $H$
  has a normal cyclic $q'$-subgroup for which the quotient is a $q$-group.
] <def:hyperelementary>

#proposition[
  $
    cal(R)(k G)_((q)) = sum_(H space q"-hyper-" \ "elementary")
    Im(ind_(H, G))
  $
] <prop:local-brauer-induction>

Similarly, if $S$ is the set of all primes not dividing $|G|$ then
$
  cal(R)(G)_((S)) = cal(R)(G)[ |G|^(-1)] = sum_(H "cyclic") Im(ind_(H, G)).
$

Combining these statements using the Chinese remainder theorem, we obtain the
first form of the Brauer induction theorem.

#theorem(title: [Brauer's induction theorem], closed: true)[
  $
    cal(R)(k G) = sum_(H space q"-hyper-" \ "elementary" \ "for some" q)
    Im(ind_(H, G)).
  $
] <th:brauer-induction>
#idx("Brauer's", "induction theorem", target: [@th:brauer-induction])#idx(
  "induction",
  "theorem",
  "Brauer's",
  target: [@th:brauer-induction],
)#idx("theorem", "Brauer's", "induction", target: [@th:brauer-induction])#idx(
  "theorem",
  "induction",
  "Brauer's",
  target: [@th:brauer-induction],
)

#corollary[
  Suppose $(K, cal(O), k)$ is a $p$-modular system. Then the decomposition map
  $ d : cal(R)(K G) -> cal(R)(k G) $
  (see Section~@sec:complete-domain) is surjective.
] <cor:decomposition-surjective>

#proof[
  Since $ind_(H, G)$ commutes with $d$, it follows from Brauer's induction
  theorem that it suffices to prove that $d$ is surjective in case $G$ is
  $q$-hyperelementary for some prime $q$. Since
  $cal(R)(k G) = cal(R)(k G slash O_p (G))$, we may also assume that
  $O_p (G) = 1$. If $q != p$ it follows that $G$ has order prime to $p$ so that
  $d$ is an isomorphism. If $q = p$ then $G$ is a split extension of a cyclic
  $p'$-group by a $p$-group acting faithfully, and one can check using Clifford
  theory that in this case the simple $k G$-modules lift to $cal(O) G$-lattices
  so that $d$ is onto in this case.
]

Examination of the representations of a $q$-hyperelementary group shows the
following, which we shall not prove.

#definition[
  If $H$ is a $q$-hyperelementary group, let $epsilon$ be a primitive
  $|O^q (H)|$th root of unity, and let $O^q (H) = chevron.l a chevron.r$. Then
  $H$ is $k$*-elementary*#idx("elementary group")#idx("group", "elementary") if,
  whenever $b in H$ and $b a b^(-1) = a^t$ with $t in ZZ$,
  $epsilon |-> epsilon^t$ is a Galois automorphism of $k(epsilon)$ over $k$.
] <def:k-elementary>

#theorem(title: [Witt–Berman])[
  We have
  $
    cal(R)(k G) = sum_(H lt.eq G \ k"-elementary") Im(ind_(H, G)).
  $
] <th:witt-berman>
#idx("Witt–Berman theorem", target: [@th:witt-berman])#idx(
  "theorem",
  "Witt–Berman",
  target: [@th:witt-berman],
)

#source(200)In particular, if $k = CC$, the *elementary* subgroups are the
subgroups which are a direct product of a $q$-group and a cyclic $q'$-group. The
full form of Brauer's induction theorem is the statement that $cal(R)(CC G)$ is
the sum of the images of induction from the elementary subgroups.

Next, we turn our attention to Conlon's induction theorem. This time, we are
working with the full ring of all representations in characteristic $p$, and
there are usually more of those than we can reasonably handle. The usual way to
get around this is to choose particular kinds of modules which are suited to the
problem in hand. In our case, we are trying to prove induction theorems, which
means that we are trying to prove that the identity element of the
representation ring is in a certain sum of ideals. This means that we need to
look at a suitable subring of the representation ring containing at least the
image of the natural map from the Burnside ring. It turns out that the trivial
source subring is the right one to look at.

Recall from Proposition~@prop:conlon-trivial-source and its corollary that every
ring homomorphism from $a(G, Triv)$ to $CC$ is of the form $s_(H, g)$ for some
pair $(H, g)$ with $H$ $p$-hypo-elementary and $g$ an element of
$H slash O_p (H)$, and that we have an isomorphism
$ A(G, Triv) tilde.equiv plus.o.big_("ccl’s of" \ "pairs" (H, g)) CC. $

Just as before we draw a commutative diagram:
$ #conlon-square $

Write $epsilon_H$ for the primitive idempotents in the top right hand corner of
this diagram, and $epsilon_(H, g)$ for the primitive idempotents in the bottom
right. The map $lambda$ sends $epsilon_H$ to $sum_g epsilon_((H, g))$ if $H$ is
$p$-hypo-elementary, and zero otherwise. We now deduce in the usual way that
$
  1_(A(G, Triv)) in sum_(H space p"-hypo-" \ "elementary") Im(ind_(H, G)).
$
We have thus proved the following theorem.

#theorem(
  title: [Conlon's induction theorem],
  closed: true,
  head-break: true,
)[
  Suppose $k$ is a field of characteristic $p$. Then
  $
    A(k G) = sum_(H space p"-hypo-" \ "elementary") Im(ind_(H, G)).
  $
] <th:conlon-induction>
#idx("Conlon's induction theorem", target: [@th:conlon-induction])#idx(
  "induction",
  "theorem",
  "Conlon's",
  target: [@th:conlon-induction],
)#idx("theorem", "Conlon's induction", target: [@th:conlon-induction])#idx(
  "theorem",
  "induction",
  "Conlon's",
  target: [@th:conlon-induction],
)

#source(201)In contrast to the situation for the Brauer induction theorem,
however, none of these subgroups goes away when the field becomes large. One can
show that all the conjugacy classes of maximal $p$-hypo-elementary subgroups are
really necessary in the above theorem.

#corollary[
  The sum of the restriction maps
  $
    sum res_(G, H) : A(k G) -> plus.o.big_("ccl’s of" H \ p"-hypo-elementary")
    A(k H)
  $
  is injective.
] <cor:hypo-elementary-restriction>

#proof[
  We express the identity element $1 in A(k G)$ as a sum of elements
  $ind_(H, G) (x_H)$ with $x_H in A(k H)$ and $H$ $p$-hypo-elementary. If
  $y in A(k G)$, then
  $
    y = y.1 = y. sum ind_(H, G) (x_H) = sum ind_(H, G) (res_(G, H) (y).x_H).
  $
  It follows that if $res_(G, H) (y)$ is zero for all $H$ $p$-hypo-elementary
  then $y = 0$.
]

Finally, Dress' induction theorem consists of doing all of the above at once.
Let $q$ be a prime, which may equal $p$ or not. Then we have as usual a
commutative diagram:
$ #dress-square $

The primitive idempotent
$ sum_(O^q (H) = H_0) e_H in b(G)_((q)) $
goes to zero in $a(G, Triv)_((q))$ unless $H_0$ is $p$-hypo-elementary, and so
$a(G)$ is the sum of the images of induction from the so-called "Dress
subgroups".

#definition[
  If $q$ is a prime (not necessarily different from $p$), a $(p, q)$*-Dress
  subgroup*#idx("Dress group")#idx("group", "Dress") is a subgroup $H$ such that
  $H slash O_p (H)$ is $q$-hyperelementary. A $k$*-Dress subgroup* is a subgroup
  $H$ such that $H slash O_p (H)$ is $k$-elementary for the field $k$ of
  characteristic $p$.
] <def:dress-subgroup>

#theorem(title: [Dress' induction theorem], closed: true)[
  Suppose that $k$ is a field of characteristic $p$ and $S$ is a set of primes.
  Then
  $
    a(k G)_((S)) = sum_(H space (p, q)"-Dress" \ "subgroup," q in S)
    Im(ind_(H, G)).
  $
  #source(202)In particular, taking for $S$ the set of all primes,
  $
    a(k G) = sum_(H space (p, q)"-Dress" \ "subgroup, any" q) Im(ind_(H, G)).
  $
] <th:dress-induction>
#idx("Dress' induction theorem", target: [@th:dress-induction])#idx(
  "induction",
  "theorem",
  "Dress'",
  target: [@th:dress-induction],
)#idx("theorem", "Dress' induction", target: [@th:dress-induction])#idx(
  "theorem",
  "induction",
  "Dress'",
  target: [@th:dress-induction],
)

As with the Witt–Berman theorem, one can show that over a given field $k$, the
necessary subgroups are the $k$-Dress subgroups. Thus for a large enough field
$k$, the subgroups needed are the subgroups $H$ for which $H slash O_p (H)$ is a
direct product of a $q$-group and a cyclic group of order coprime to $p$ and
$q$. This time, we may assume $p != q$, since otherwise the $O_p$ just grows.
