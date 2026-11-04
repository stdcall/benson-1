#import "main-defs.typ": *
#import "statements.typ": *

== Tensor induction <sec:tensor-induction>

We saw in Section~@sec:induction-restriction that if $Gamma$ is a subring of a
ring $Lambda$ then we may induce modules from $Gamma$ to $Lambda$. The
particular case of induction and restriction for group algebras was briefly
discussed in Section~@sec:induction-restriction-groups. The corresponding notion
of tensor induction for modules for group algebras, however, does not easily
generalise.

As in Section~@sec:induction-restriction-groups, if $H lt.eq G$ and $M$ is an
$R H$-module we can write
$
  M up^G = R G times.o_(R H) M = plus.o.big_(g in G slash H) g times.o M.
$

One way of checking that this gives a well defined $R G$-module which is
independent of the choice of coset representatives of $H$ in $G$ is to introduce
the following construction. Let $n = |G : H|$. Recall that the wreath product
$Sigma_n wreath H$ consists of elements $(pi; h_1, dots, h_n)$ with
$pi in Sigma_n$ and $h_1, dots, h_n in H$, and with multiplication given by
$
  (pi'; h'_1, dots, h'_n)(pi; h_1, dots, h_n)
  = (pi' pi; h'_(pi(1)) h_1, dots, h'_(pi(n)) h_n).
$
Given a choice of coset representatives $g_1, dots, g_n$ of $H$ in $G$, we
obtain an injective group homomorphism $i : G -> Sigma_n wreath H$ as follows.
For a given $g in G$, we can write $g . g_j = g_(pi(j)) h_j$ for uniquely
defined elements $pi in Sigma_n$ and $h_1, dots, h_n in H$ depending on $g$. We
then set $i(g) = (pi; h_1, dots, h_n)$. A different choice of coset
representatives gives rise to a conjugate embedding of $G$ in
$Sigma_n wreath H$.

Now given an $R H$-module $M$, we can make a direct sum $M^n$ of $n$ copies of
$M$ into a module for $Sigma_n wreath H$ via
$
  (pi; h_1, dots, h_n)(m_1, dots, m_n)
  = (h_(pi^(-1)(1)) m_(pi^(-1)(1)), dots, h_(pi^(-1)(n)) m_(pi^(-1)(n))).
$
The induced module is then
$ M up^G = i^* (M^n) = (M^n) down_G . $
In a similar way, since tensor product is commutative, we can make the tensor
product $M^(times.o n)$ of $n$ copies of $M$ into a module for
$Sigma_n wreath H$ via
$
  (pi; h_1, dots, h_n)(m_1 times.o dots.c times.o m_n)
  = h_(pi^(-1)(1)) m_(pi^(-1)(1)) times.o dots.c times.o
  h_(pi^(-1)(n)) m_(pi^(-1)(n)).
$

#definition[
  The *tensor induced*#idx("tensor", "induction")#idx("induction", "tensor")
  module $M tensorup^G$#idx("$tensorup$") is defined to be
  $ M tensorup^G = i^* (M^(times.o n)) = (M^(times.o n)) down_G . $
] <def:tensor-induction>

The basic properties of tensor induction are given in the following proposition.

#proposition[
  #source(109)Suppose $H < G$ and $M_1$, $M_2$ and $M_3$ are $R H$-modules.
  + $(M_1 times.o_R M_2) tensorup^G tilde.equiv
    M_1 tensorup^G times.o_R M_2 tensorup^G$.
  + If $H' lt.eq H lt.eq G$ and $M$ is an $R H'$-module then
    $M tensorup^H tensorup^G tilde.equiv M tensorup^G$.
  + $(M_1 plus.o M_2) tensorup^G tilde.equiv
    M_1 tensorup^G plus.o M_2 tensorup^G plus.o M'$, where $M'$ is a direct sum
    of modules induced from proper subgroups $K$ containing the intersection of
    the conjugates of $H$.
  + If $H' lt.eq H$ and $M$ is an $R H'$-module then $M up^H tensorup^G$ is a
    direct sum of modules induced from subgroups $K$ containing the intersection
    of the conjugates of $H'$, and with $K inter H lt.eq H'$.
  + (Mackey formula) If $K, H lt.eq G$ and $M$ is an $R K$-module then
    $
      M tensorup^G down_H tilde.equiv
      times.o.big_(H backslash G slash K) lconj(g, M) down_(H inter lconj(g, K))
      tensorup^H .
    $
  + (Dress [@bib:Dress1975a]) Suppose $X$ is a permutation representation of $G$
    and $0 -> M_1 -> M_2 -> M_3 -> 0$ is an $X$-split short exact sequence of
    $R H$-modules (see Definition~@def:permutation-split). Then
    $
      R X times.o_R (M_2 tensorup^G)
      tilde.equiv R X times.o_R ((M_1 plus.o M_3) tensorup^G).
    $
] <prop:tensor-induction>

#proof[
  + and (ii) are clear from the definitions.
  #enum.item(3)[As modules for $Sigma_n wreath H$ we have
    $
      (M_1 plus.o M_2)^(times.o n) tilde.equiv M_1^(times.o n) plus.o
      M_2^(times.o n) plus.o M'
    $
    where
    $
      M' = plus.o.big_(1 lt.eq r lt.eq n-1)
      (M_1^(times.o r) times.o_R M_2^(times.o (n-r)))_((Sigma_r times
        Sigma_(n-r)) wreath H) up^(Sigma_n wreath H),
    $
    and the result follows by restricting to $G$.
  ]
  + The module
    $
      (M up^H)^(times.o n)
      = scaled((plus.o.big_(g in H slash H') g times.o M))^(times.o n)
    $
    is a direct sum of submodules corresponding to the $Sigma_n wreath H$-orbits
    of ways of choosing an $n$-tuple of coset representatives of $H'$ in $H$.
    The stabiliser in $H$ of such an $n$-tuple is the intersection of the
    corresponding conjugates of $H'$, and is therefore contained in some
    conjugate of $H'$. The result follows by restricting to $G$.
  + This follows by partitioning the set of left coset representatives of $K$ in
    $G$ as a disjoint union of orbits of $H$ corresponding to the double cosets.
  + Regard $M_1$ as a submodule of $M_2$ by abuse of notation. As an
    $R G$-module, $M_2 tensorup^G$ has a natural filtration
    $ M_1 tensorup^G = U_0 lt.eq U_1 lt.eq dots.c lt.eq U_n = M_2 tensorup^G $
    #source(110)\($n = |G : H|$), where $U_j$ is the linear span of the tensors
    $m_1 times.o dots.c times.o m_n$ for which at most $j$ of the $m_i$ do not
    lie in $M_1$. It is easy to see that
    $
      (M_1 plus.o M_3) tensorup^G tilde.equiv
      U_0 plus.o U_1 slash U_0 plus.o dots.c plus.o U_n slash U_(n-1).
    $
    Thus we must show that tensoring with $R X$ splits the above filtration of
    $M_2 tensorup^G$.

    Suppose $f : R X times.o_R M_3 -> R X times.o_R M_2$ is an $X$-splitting of
    the sequence $0 -> M_1 -> M_2 -> M_3 -> 0$ of the form
    $
      f(sum_(x in X) x times.o m_x) = sum_(x in X) x times.o f_x lr((m_x))
    $
    with $f_x$ linear maps from $M_3$ to $M_2$ (if there is any splitting of the
    form $f(sum_(x in X) x times.o m_x)
    = sum_(x, y in X) x times.o f_(x y) lr((m_y))$, then by dropping the terms
    with $x != y$, we obtain a splitting of the desired form). Since $f$ is an
    $R H$-module homomorphism, we have $h f_x lr((m_x)) = f_(h x) lr((h m_x))$
    for $h in H$. Now a splitting $phi.alt$ for the map
    $
      R X times.o_R U_j ->> (R X times.o_R U_j) slash (R X times.o_R U_(j-1))
      tilde.equiv R X times.o_R (U_j slash U_(j-1))
    $
    is given as follows. The typical generator for the right hand side is given
    as $x times.o (m_1 times.o dots.c times.o m_n)$, where $j$ of the $m_i$ are
    in $M_3$ and $n - j$ are in $M_1$. To apply $phi.alt$, we leave the $x$ and
    those $m_i$ which are in $M_1$ alone, and we replace those $m_i$ which are
    in $M_3$ by $f_(g_i^(-1) x) lr((m_i))$, where $g_i$ is the coset
    representative of $H$ in $G$ labelling the $i$th copy of $M_2$ in
    $M_2 tensorup^G = M_2^(times.o n)$. It is easily checked that $phi.alt$ is
    an $R G$-module homomorphism which splits the above surjection.
]

The reader is referred to Chapter 4 of Volume II for an extensive discussion of
the tensor induction construction at the level of chain complexes. In particular
this gives rise to the Evens norm map and Steenrod operations in cohomology. The
algebraic proof by Evens that the cohomology ring of a finite group is finitely
generated depends heavily on this construction.
