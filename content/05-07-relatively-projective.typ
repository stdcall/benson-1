#import "main-defs.typ": *
#import "statements.typ": *

== Relatively projective and relatively split ideals <sec:relative-ideals>

Suppose $k$ is a field of characteristic $p$. The main theorem in this section
is a theorem of Dress [@bib:Dress1975a], which states that for any subgroup
$H lt.eq G$, the representation ring with $p$ inverted
$ a(G)_p = ZZ[1 slash p] times.o_ZZ a(G) $
decomposes as a direct sum of the ideal of relatively $H$-projective
modules#idx("ideal", "relatively", "projective")#idx(
  "relatively",
  "projective",
  "ideal",
) $a(G, H)_p$ and the ideal of $H$-split sequences#idx(
  "ideal",
  "relatively",
  "split",
)#idx("relatively", "split ideal") $a_0 (G, H)_p$. More generally, for any
permutation representation $X$ of $G$, $a(G)_p$ decomposes as a direct sum of
$a(G, X)_p$ and $a_0 (G, X)_p$. This latter statement is more amenable to proof
by induction. The case $H = 1$ (or equivalently $X$ is the trivial permutation
representation on one point) will tell us that the determinant of the Cartan
matrix is a power of $p$. We give another proof of this using psi operations in
Section~@sec:psi-operations. Brauer's original proof used his characterisation
of characters.

#theorem(title: [Dress])[
  Suppose $X$ is a permutation representation of $G$, and $k$ is a field of
  characteristic $p$. Then
  $ a(k G)_p = a(G, X)_p plus.o a_0 (G, X)_p. $
] <th:dress-relative-decomposition>

#proof[
  We first observe that it suffices to show that the identity element
  $1 in a(G)_p$ lies in $a(G, X)_p + a_0 (G, X)_p$. For since $a(G, X)_p$ and
  $a_0 (G, X)_p$ are ideals, we then have $a(G)_p = a(G, X)_p + a_0 (G, X)_p$.
  Elements of $a(G, X)_p$ and $a_0 (G, X)_p$ have zero product, so if
  $1 = alpha + beta$ with $alpha in a(G, X)_p$ and $beta in a_0 (G, X)_p$ then
  for any $x in a(G, X)_p inter a_0 (G, X)_p$ we have
  $ x = x.1 = x.alpha + x.beta = 0, $
  and so $a(G, X)_p inter a_0 (G, X)_p = 0$.

  We prove the theorem by induction on the order of $G$. For any subgroup $H$ of
  $G$ we have
  $
    ind_(H, G) (a(H, X)_p) subset.eq a(G, X)_p, quad
    ind_(H, G) (a_0 (H, X)_p) subset.eq a_0 (G, X)_p.
  $
  If $G$ is not a $(p, q)$-Dress subgroup for some $q != p$, then Dress'
  induction theorem~@th:dress-induction (with $S$ equal to the collection of all
  primes other than $p$) says that $a(G)_p$ is the sum of the images of
  induction from proper subgroups. We may thus suppose that $G$ is a
  $(p, q)$-Dress subgroup for some prime $q != p$. In particular, setting
  $P = O_p (G)$, we see that $G slash P$ is a $p'$-group. If $P$ stabilises
  #source(203)any point in $X$, then by Corollary~@cor:index-invertible,
  $a(G)_p = a(G, X)_p$, and we are done. So we may suppose $P$ does not
  stabilise any point in $X$.

  Recall that the tensor induction map
  $
    ind_(P, G)^times.o : a(P)_p slash sum_(K < P) Im(ind_(K, P))
    -> a(G)_p slash sum_(K < G) Im(ind_(K, G))
  $
  is a ring homomorphism. By Proposition~@prop:tensor-induction[(vi)], the image
  of $a_0 (P, X)_p$ under this map lies in $a_0 (G, X)_p$. It thus suffices to
  show that the identity element of $a(P)_p$ lies in
  $a_0 (P, X)_p + sum_(K < P) Im(ind_(K, P))$. Now if $X = X_1 dot(union) X_2$
  then $a_0 (P, X)_p = a_0 (P, X_1)_p inter a_0 (P, X_2)_p$, so since $P$ does
  not stabilise any point in $X$, we may suppose that $X$ is a non-trivial
  transitive permutation representation of $P$. Let $P'$ be a maximal subgroup
  of $P$ containing the stabiliser of a point in $X$, so that
  $a_0 (P, X)_p gt.eq a_0 (P, P')_p$. Since $P'$ is normal in $P$, and
  $P slash P'$ is a cyclic group of order $p$,
  $a(P slash P', 1) = Im(ind_(1, P slash P'))$ is spanned by the regular
  representation. The composition factors of this are exactly $p$ copies of the
  trivial module, and so we have
  $
    a(P slash P')_p = a(P slash P', 1)_p plus.o a_0 (P slash P', 1)_p
    = Im(ind_(1, P slash P')) plus.o a_0 (P slash P', 1)_p
  $
  (cf. Corollary~@cor:cartan-homomorphism). Inflating to $P$, we see that the
  identity element of $a(P)_p$ lies in $Im(ind_(P', P)) + a_0 (P, P')_p$ as
  required.
]

#remark[
  The statement of the theorem is equivalent to the statement that the quotient
  $a(G) slash (a(G, X) + a_0 (G, X))$ is entirely $p$-torsion.
]

#corollary(title: [Brauer])[
  Suppose that $k$ is a field of characteristic $p$. Then the determinant of the
  Cartan matrix of $k G$ is a power of $p$.
] <cor:cartan-determinant>

#proof[
  This is the case of the theorem in which $X$ is a single point (cf.
  Corollary~@cor:cartan-homomorphism). For another proof of this theorem using
  psi operations, see Theorem~@th:cartan-determinant.
]
