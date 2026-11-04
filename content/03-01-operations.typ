#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-01-operations.typ": (
  coassociativity, cocommutativity, counit-triangles, summand-maps,
)

== Operations on $R G$-modules <sec:operations>
#idx("operations", "on $R G$-modules", target: [@sec:operations])

#definition[
  If $G$ is a finite group and $R$ is a commutative ring, we may form the *group
  ring*#idx("group", "ring")#idx("ring", "group") $R G$ whose elements are the
  formal linear combinations $sum_i r_i g_i$ with $r_i in R$ and $g_i in G$.
  Addition and multiplication are given by
  $
    sum_i r_i g_i + sum_j r'_j g_j = sum_i (r_i + r'_i) g_i, quad
    sum_i r_i g_i . sum_j r'_j g_j = sum_(i,j) r_i r'_j (g_i g_j).
  $
  Thus $R G$ is an $R$-algebra, which as an $R$-module is free of rank $|G|$.

  Of course, this definition also makes sense for infinite groups, provided we
  restrict our attention to finite sums.
] <def:group-ring>

The group ring $R G$ is an *augmented algebra*#idx("augmented algebra")#idx(
  "algebra",
  "augmented",
) with augmentation $epsilon : R G -> R$ given by
$ epsilon(sum_i r_i g_i) = sum_i r_i $
(cf. Section~@sec:ext-tor). Thus it makes sense to talk of the *trivial*#idx(
  "module",
  "trivial",
)#idx("trivial", "module") $R G$-module $R$. We write $H_n (G, M)$ and
$H^n (G, M)$#idx("$H_n (G, M)$, $H^n (G, M)$") for the homology and cohomology
groups with coefficients in $M$, namely the groups $H_n (R G, M)$ and
$H^n (R G, M)$ defined in Section~@sec:ext-tor. Note that in the former case we
should regard the left $R G$-module $M$ as a right module via $m g = g^(-1) m$.
This is a standard device which we shall make explicit in this section.
Similarly we write $H_n (G, bold(C))$ and $H^n (G, bold(C))$ for the
hyperhomology and hypercohomology groups discussed in
Section~@sec:chain-complex-operations.

We shall see in Section~@sec:standard-resolutions that a particular resolution
called the *standard resolution* or *bar resolution* may be used to write down
explicit #source(62)cocycles and coboundaries. This approach is only really
useful for low degree cohomology, and in Section~@sec:low-degree-cohomology we
provide group theoretical interpretations of degree one and degree two
cohomology.

In case $R = k$ is a field, the group ring $k G$ is a *symmetric algebra*#idx(
  "symmetric",
  "algebra",
)#idx("algebra", "symmetric") by the following proposition:

#proposition[
  The linear map $lambda : k G -> k$ sending a linear combination of group
  elements to the coefficient of the identity element satisfies the conditions
  of Definition~@def:frobenius-symmetric. In particular, every projective
  $k G$-module is injective, and if $P$ is a projective indecomposable
  $k G$-module then $Soc(P) tilde.equiv P slash Rad(P)$.
] <prop:group-algebra-symmetric>

#proof[
  Suppose $I$ is a non-zero left ideal of $k G$. If $sum_i r_i g_i$ is in $I$
  with $r_j != 0$, then $g_j^(-1) (sum_i r_i g_i)$ is also an element of $I$ and
  is not contained in $Ker(lambda)$. The same applies to right ideals and so
  condition (i) is satisfied. Condition (ii) is clearly satisfied. The remaining
  statements now follow by applying Proposition~@prop:frobenius-self-injective
  and Theorem~@th:symmetric-socle.
]

#definition[
  A *representation*#idx("representation") of $G$ over $R$ is a homomorphism
  $G -> GL_n (R)$, the group of non-singular $n times n$ matrices over $R$, for
  some $n$. Two representations are equivalent if one may be transformed into
  the other by a change of basis in $R^n$. A representation is called an
  *ordinary representation*#idx("ordinary", "representation")#idx(
    "representation",
    "ordinary",
  ) if $R$ is a field of characteristic zero (or more generally of
  characteristic not dividing $|G|$), a *modular representation*#idx(
    "modular",
    "representation",
  )#idx("representation", "modular") if $R$ is a field of characteristic $p$
  dividing $|G|$, and an *integral representation*#idx(
    "integral representation",
  )#idx("representation", "integral") if $R$ is a ring of algebraic integers or
  one of its localisations or completions at a prime ideal.
] <def:representation>

Note that a representation $phi.alt : G -> GL_n (R)$ makes $R^n$ into an
$R G$-module via
$ (sum_i r_i g_i) x = sum_i r_i phi.alt(g_i)(x). $
This gives a one–one correspondence between equivalence classes of
representations and isomorphism classes of finitely generated $R$-free
$R G$-modules.

One is often interested in a slightly wider class of modules. An
*RG-lattice*#idx("lattice") is a finitely generated $R$-projective $R G$-module.
We demand that a map of $R G$-lattices, when restricted to $R$, is a composite
of a split epi and a split mono.

#subhead[Tensors and Homs] If $M$ and $N$ are $R G$-modules, then we make
$M times.o_R N$#idx(
  "tensor",
  "product",
) and $Hom_R (M, N)$ into $R G$-modules via
$
  (sum_i r_i g_i)(m times.o n) & = sum_i r_i (g_i (m) times.o g_i (n)), \
   (sum_i r_i g_i)(phi.alt)(m) & = sum_i r_i g_i (phi.alt(g_i^(-1) m)).
$
#source(63)Note that only the group elements, and not general elements of the
group algebra, act "diagonally" in this definition. Thus we need to know where
the group is, inside the group algebra. This notion is captured in the following
definition:

#definition[
  A *bialgebra*#idx("bialgebra") consists of an algebra $Lambda$ over a
  commutative ring $R$ together with maps of algebras
  $ Delta : Lambda -> Lambda times.o_R Lambda $
  called the *comultiplication*#idx("comultiplication") and
  $ epsilon : Lambda -> R $
  called the *co-unit*#idx("co-unit"), such that the following diagrams commute:
  $ #coassociativity $
  (co-associativity#idx("co-associativity")) and
  $ #counit-triangles $
  (co-unitary property)

  Let $tau : Lambda times.o_R Lambda -> Lambda times.o_R Lambda$ be the twist
  map $tau(mu times.o nu) = nu times.o mu$. We say that $Lambda$ is
  *cocommutative*#idx("cocommutative") if the following diagram commutes:
  $ #cocommutativity $

  A *Hopf algebra*#idx("Hopf algebra")#idx("algebra", "Hopf") is a bialgebra
  $Lambda$ together with an $R$-linear map
  $ eta : Lambda -> Lambda $
  called the *antipode*#idx("antipode") such that if
  $Delta(lambda) = sum_i mu_i times.o nu_i$ then
  $
    sum_i mu_i eta(nu_i) = sum_i eta(mu_i) nu_i = epsilon(lambda) . 1 in Lambda.
  $
] <def:bialgebra>

We are mostly interested in the case where $Lambda$ is either commutative or
cocommutative. In this case, the antipode is unique, it is an anti-automorphism
of $Lambda$ (i.e., $eta(lambda mu) = eta(mu) eta(lambda)$), and its square is
the identity map. See for example Sweedler [@bib:Sweedler1969, Chapter~4] for
more details.

#source(64)If $Lambda$ is a bialgebra over $R$ and $M$, $N$ are (left)
$Lambda$-modules, we make $M times.o_R N$ into a $Lambda$-module as follows. If
$ Delta(lambda) = sum_i mu_i times.o nu_i in Lambda times.o_R Lambda $
then
$ lambda(m times.o n) = sum_i mu_i (m) times.o nu_i (n). $
We also make $R$ into a $Lambda$-module via $lambda(r) = epsilon(lambda) r$.
This module is called the *trivial module*#idx("module", "trivial")#idx(
  "trivial",
  "module",
).

If $Lambda$ is a Hopf algebra over $R$ and $M$ and $N$ are (left)
$Lambda$-modules, then we make $Hom_R (M, N)$ into a $Lambda$-module as follows.
If $Delta(lambda) = sum_i mu_i times.o nu_i in Lambda times.o_R Lambda$ and
$phi.alt in Hom_R (M, N)$ then
$ lambda(phi.alt)(m) = sum_i mu_i (phi.alt(eta(nu_i)(m))). $

We shall write $M^*$ for the *dual module*#idx("dual", "module") to $M$, namely
the module $Hom_R (M, R)$. Note that we are viewing the dual of a _left_
$Lambda$-module as a _left_ $Lambda$-module. What is happening here is that
because of the antipode, we can regard right $Lambda$-modules as left
$Lambda$-modules via $lambda m = m eta(lambda)$ and vice-versa.

Suppose that $R = k$ is a field and $Lambda$ is cocommutative. If $M$ and $N$
are finite dimensional as $k$-vector spaces, then the natural vector space
isomorphisms
$ Hom_k (M, N) tilde.equiv M^* times.o_k N, quad M^(**) tilde.equiv M $
etc. are $Lambda$-module isomorphisms.

For example, a group algebra $R G$ is a cocommutative Hopf algebra, with
$
  Delta scaled((sum_i r_i g_i)) = sum_i r_i g_i times.o g_i, quad
  epsilon scaled((sum_i r_i g_i)) = sum_i r_i, \
  eta scaled((sum_i r_i g_i)) = sum_i r_i g_i^(-1).
$
With these definitions, the action of $R G$ on a tensor product $M times.o_R N$
is given by
$ g(m times.o n) = g m times.o g n. $
The action on $Hom_R (M, N)$ is given by
$ (g phi.alt)(m) = g(phi.alt(g^(-1) m)). $

If $R$ is an integral domain, we can recover the group $G$ from the Hopf algebra
$R G$ as the set of *grouplike elements*#idx("element", "grouplike")#idx(
  "group",
  "-like elements",
), i.e., the set of non-zero elements $lambda in R G$ satisfying
$Delta(lambda) = lambda times.o lambda$. Thus while many groups may have the
same group algebra as an algebra, the same is not true as a Hopf algebra.

#source(65)

#proposition[
  Suppose $P$ is a projective module and $M$ is an $R$-free module for a Hopf
  algebra $Lambda$ over $R$. Then $P times.o_R M$ is projective.
] <prop:projective-tensor>

#proof[
  Since projective modules are the same as direct summands of free modules, it
  suffices to prove that $Lambda times.o_R M$ is free. Notice that the action of
  $Lambda$ on $Lambda times.o_R M$ is the diagonal one defined through the map
  $Delta$, rather than the action given in the definition
  (@def:induction-restriction) of an induced module. For the induced module
  definition it is clear that $Lambda times.o_R M$ is free, because if
  ${m_alpha}$ is a free $R$-basis of $M$ then ${1 times.o m_alpha}$ is a free
  $Lambda$-basis of $Lambda times.o_R M$. So we define an $R$-linear map
  $ Lambda times.o_R M -> Lambda times.o_R M $
  as follows. If $Delta(lambda) = sum_i mu_i times.o nu_i$ then
  $lambda times.o m |-> sum_i mu_i times.o nu_i m$. This is an isomorphism of
  $R$-modules with inverse given by
  $lambda times.o m |-> sum_i mu_i times.o eta(nu_i) m$. Furthermore, it defines
  a $Lambda$-module isomorphism from $Lambda times.o_R M$ with the structure of
  induced module to $Lambda times.o_R M$ with the required diagonal action.
]

#corollary[
  Suppose $M$ and $N$ are modules for a Hopf algebra $Lambda$, and $N$ is
  $R$-free. Then
  $
    tilde(Omega)(M) times.o_R N plus.o ("projective")
    tilde.equiv tilde(Omega)(M times.o_R N) plus.o ("projective").
  $
  If $Lambda$ is finite dimensional over a field $k$, then
  $
    Omega(M) times.o_k N tilde.equiv Omega(M times.o_k N) plus.o ("projective").
  $
] <cor:omega-tensor>

#proof[
  Tensor the short exact sequence
  $ 0 -> tilde(Omega)(M) -> P -> M -> 0 $
  with $N$ and use the proposition.
]

For group algebras we have another identity which is not obvious in the more
general case of a Hopf algebra.

#proposition[
  If $M$ and $N$ are $R G$-modules then
  $ Hom_(R G) (R, Hom_R (M, N)) tilde.equiv Hom_(R G) (M, N). $
] <prop:fixed-points-hom>

#proof[
  We can regard the left hand side of this as an $R$-submodule of $Hom_R (M, N)$
  by evaluating at the identity. Then it consists of the elements $phi.alt$ of
  $Hom_R (M, N)$ such that for all $g in G$, $g phi.alt(g^(-1) m) = phi.alt(m)$.
  This is equivalent to the statement that $phi.alt$ is an $R G$-module
  homomorphism.
]

#proposition[
  Suppose $M_1$, $M_2$ and $M_3$ are modules for a group algebra $R G$. Then
  there are natural isomorphisms
  + $Hom_(R G) (M_1 times.o_R M_2, M_3) tilde.equiv
    Hom_(R G) (M_2, Hom_R (M_1, M_3))$
  + If $M_1$ is $R$-projective, then
    $
      Ext^n_(R G) (M_1 times.o_R M_2, M_3) tilde.equiv
      Ext^n_(R G) (M_2, Hom_R (M_1, M_3))
    $
  + If $M_1$ is $R$-projective, then
    $ Ext^n_(R G) (M_1, M_3) tilde.equiv H^n (G, Hom_R (M_1, M_3)). $
] <prop:tensor-hom-ext>

#source(66)

#proof[
  + It is easy to check that the isomorphism
    $
      Hom_R (M_1 times.o_R M_2, M_3) tilde.equiv
      Hom_R (M_2, Hom_R (M_1, M_3))
    $
    of Lemma~@lem:tensor-hom-adjunction is an isomorphism of $R G$-modules. Now
    apply $Hom_(R G) (R, -)$ to both sides.
  + This follows from (i) by the usual dimension-shifting argument.
  + This is the special case of (ii) in which $M_2 = R$.
]

In general, tensor products of modules are hard to decompose. However, under
suitable conditions we can always tell when the trivial module is a direct
summand of a tensor product. The following theorem is proved in
[@bib:Benson1986c]:

#theorem[
  Suppose $R = k$ is an algebraically closed field of characteristic $p$
  (possibly $p = 0$), and $G$ is a group. If $M$ and $N$ are finite dimensional
  indecomposable $k G$-modules, then $M times.o_k N$ has the trivial module $k$
  as a direct summand if and only if the following two conditions are satisfied.
  + $M tilde.equiv N^*$
  + $p divides.not dim(N)$.
  (Note that if $p = 0$ then #statement-comment[(ii)] is automatically
  satisfied.)

  Moreover if $k$ is a direct summand of $N^* times.o_k N$ then it has
  multiplicity one (i.e., $k plus.o k$ is not a summand).
] <th:trivial-summand>

#proof[
  The trivial $k G$-module $k$ is a direct summand of $M times.o_k N$ if and
  only if we can find homomorphisms
  $ k -> M times.o_k N -> k $
  whose composite is non-zero.

  Using the isomorphism
  $ Hom_(k G) (k, M times.o_k N) tilde.equiv Hom_(k G) (N^*, M) $
  we see that the sum of the submodules of $M times.o_k N$ isomorphic to $k$ is
  $Hom_(k G) (N^*, M)$. Thus the trivial module is a summand if and only if the
  composite map
  $
    Hom_(k G) (N^*, M) limits(arrow.r.hook)^i M times.o_k N
    limits(arrow.r.twohead)^p (Hom_(k G) (M, N^*))^*
  $
  is non-zero.

  Associated to $p compose i$, there is a map
  $ eta : Hom_(k G) (N^*, M) times.o_k Hom_(k G) (M, N^*) -> k $
  with the property that $p compose i != 0$ if and only if $eta != 0$. This map
  is given as follows. Choose a basis $n_1, dots, n_r$ for $N$ and let
  $n'_1, dots, n'_r$ be the dual basis for $N^*$. Let
  $alpha in Hom_(k G) (N^*, M)$ and $beta in Hom_(k G) (M, N^*)$. Then
  $
    i(alpha) = sum_(j=1)^r alpha(n'_j) times.o n_j, quad
    p(m times.o n)(beta) = beta(m)(n),
  $
  #source(67)and so by definition
  $
    eta(alpha times.o beta) & = ((p compose i)(alpha))(beta)
    = p scaled((sum_(j=1)^r alpha(n'_j) times.o n_j))(beta) \
    & = sum_(j=1)^r p(alpha(n'_j) times.o n_j)(beta)
    = sum_(j=1)^r beta(alpha(n'_j))(n_j)
    = tr(beta compose alpha).
  $
  Hence we may factor $eta$ as composition followed by trace
  $
    Hom_(k G) (N^*, M) times.o_k Hom_(k G) (M, N^*) limits(->)^compose
    End_(k G) (N^*) limits(->)^tr k.
  $

  Since $N^*$ is indecomposable, $End_(k G) (N^*)$ is a local ring
  (Lemma~@lem:indecomposable-local), and so since $k$ is algebraically closed,
  every $k G$-module endomorphism of $N^*$ is of the form $lambda I + n$ with
  $lambda in k$ and $n$ nilpotent. Now we have $tr(n) = 0$, and
  $tr(I) = dim(N^*) = dim(N)$. Thus for $k$ to be a direct summand of
  $M times.o_k N$ (i.e., for $eta$ to be non-zero) $p$ cannot divide $dim(N)$.
  Moreover, we must have elements $alpha in Hom_(k G) (N^*, M)$ and
  $beta in Hom_(k G) (M, N^*)$ such that $tr(beta compose alpha) != 0$; namely,
  such that $beta compose alpha$ is an isomorphism. Since $M$ is indecomposable
  this means we must have $M tilde.equiv N^*$. Moreover, in the case where
  $p divides.not dim(N)$ and $M tilde.equiv N^*$, it is clear that
  $eta(beta compose alpha) != 0$ for any isomorphisms $alpha$ and $beta$.

  Finally, suppose $k$ is a direct summand of $N^* times.o_k N$ with
  multiplicity greater than one. Then the image of $p compose i$ has dimension
  greater than one. This means that there are subspaces of $Hom_(k G) (N^*, M)$
  and $Hom_(k G) (M, N^*)$ of dimension greater than one, on which $eta$ is a
  non-singular pairing. Thus there is a subspace of $Hom_(k G) (N^*, M)$ of
  dimension greater than one all of whose non-zero elements are isomorphisms,
  and this we know to be impossible.
]

See also Auslander and Carlson [@bib:Auslander1986] for a discussion of more
general coefficient rings $R$. The following is also useful:

#proposition[
  If $M$ is a finite dimensional module for a cocommutative Hopf algebra
  $Lambda$ over a field $k$, then $M$ is a summand of
  $M times.o_k M^* times.o_k M$. Thus the following are equivalent:
  + $M$ is projective
  + $M times.o_k M^*$ is projective
  + $M times.o_k M$ is projective
  + $M^*$ is projective
  + $M$ is injective.
] <prop:summand-tensor-dual>

#proof[
  Choose dual bases $m_1, dots, m_r$ of $M$ and $m'_1, dots, m'_r$ of $M^*$. We
  have maps
  $ #summand-maps $
  Thus $M$ is a summand of $M times.o_k M^* times.o_k M$.
]

#source(68)

#corollary(closed: true)[
  If $Lambda$ is a finite dimensional cocommutative Hopf algebra over a field
  $k$, then $Lambda$ is self injective.
] <cor:hopf-self-injective>

In fact, this corollary is still true without the assumption of cocommutativity,
but the argument is harder.
