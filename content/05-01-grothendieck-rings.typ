#import "main-defs.typ": *
#import "statements.typ": *

== Representation rings and Grothendieck rings <sec:grothendieck-rings>

#idx("Grothendieck ring")#idx("ring", "Grothendieck")Suppose $R$ is a
commutative ring of coefficients. We define the *representation ring*#idx(
  "representation",
  "ring",
)#idx("ring", "representation") $a(G) = a(R G)$#idx("$a(G)$") to be the ring
with generators the isomorphism classes $[M]$ of $R G$-lattices (finitely
generated $R$-projective $R G$-modules), and relations
$ [M] + [N] = [M plus.o N], quad [M].[N] = [M times.o N]. $

The identity and zero elements of this ring are given by
$ 1 = [R], wide 0 = [0] $
where $R$ is the trivial $R G$-lattice and 0 is the zero lattice.

The usual properties of direct sum and tensor product show that $a(G)$ is a
commutative associative ring with identity. In the presence of the Krull–Schmidt
theorem#idx("Krull–Schmidt theorem")#idx("theorem", "Krull–Schmidt"), the
additive structure of $a(G)$ is clear. Each element can be written uniquely as a
finite sum $sum_i n_i [M_i]$ with the $M_i$ indecomposable. Thus the additive
group of $a(G)$ is free abelian on generators $[M_alpha]$, one for each
isomorphism class of indecomposable lattice $M_alpha$. Note that there are
usually infinitely many of these, so that $a(G)$ is quite a large object. It is,
for example, usually not a Noetherian ring.

It is often convenient to introduce various rings of coefficients (not to be
confused with the ring $R$) into the representation ring. We set#idx(
  "$A(G)$, $a(G)_QQ$, $a(G)_p$, $a(G)_((S))$",
)
$
  A(G) = CC times.o_ZZ a(G), quad a(G)_QQ = QQ times.o_ZZ a(G), quad
  a(G)_p = ZZ[1 slash p] times.o_ZZ a(G).
$

More generally, if $S$ is a set of primes, we can look at the localised
representation ring $a(G)_((S))$, obtained by allowing denominators coprime to
$S$. Thus for example if $S = {p}$, we write $a(G)_((p))$ for the $p$-local
representation ring, and if $S$ is the set of all primes other than $p$, we
obtain $a(G)_p$ as above.

#source(185)We also introduce various ideals and subrings of $a(G)$ as follows.
If $H$ is a subgroup of $G$, we denote by $a(G, H)$#idx(
  "$a(G, H)$, $a(G, cal(X))$",
) the ideal (cf. Corollary~@cor:tensor-relatively-projective) in $a(G)$ spanned
by the relatively $H$-projective $R G$-lattices. If $X$ is a permutation
representation of $G$, we write $a(G, X)$ for the ideal spanned by the
relatively $X$-projective $R G$-lattices (see
Definition~@def:permutation-split). Similarly, if $cal(X)$ is a collection of
subgroups closed under conjugation and intersections, we denote by
$a(G, cal(X))$ the ideal (cf. Corollary~@cor:tensor-relative-intersections) in
$a(G)$ spanned by summands of sums of relatively $H$-projective $R G$-lattices
for $H in cal(X)$. We similarly write $A(G, H)$, $A(G, X)$, $A(G, cal(X))$,
$a(G, H)_QQ$, and so on, for the corresponding notions in $A(G)$, $a(G)_QQ$,
etc.

If $H$ is a subgroup of $G$, we denote by $a_0 (G, H)$#idx(
  "$a_0(G, H)$, $a_0(G, cal(X))$",
) the ideal spanned by the difference elements of the form $M_2 - M_1 - M_3$,
where $0 -> M_1 -> M_2 -> M_3 -> 0$ is a short exact sequence of $R G$-lattices
which splits on restriction to $H$. If $X$ is a permutation representation of
$G$, we write $a_0 (G, X)$ for the ideal spanned by the difference elements of
the above form for $X$-split sequences. If $cal(X)$ is a collection of subgroups
closed under conjugation and intersections, we write $a_0 (G, cal(X))$ for the
intersection of the $a_0 (G, H)$ for $H in cal(X)$. The *Grothendieck ring* of
$R G$-lattices is by definition the quotient
$cal(R) (G) = a(G) slash a_0 (G, 1)$#idx("$cal(R)(G)$"). Note that all short
exact sequences of $R G$-lattices split on restriction to the trivial subgroup,
since $R G$-lattices are by definition projective as $R$-modules.

We write $K_0 (R G)$#idx("$K_0(R G)$") for the ring with generators the
isomorphism classes $[P]$ of finitely generated projective $R G$-modules, with
the same relations
$ [P] + [Q] = [P plus.o Q], quad [P].[Q] = [P times.o Q] $
as before. This is called the Grothendieck ring of projective $R G$-modules. The
same definition may be made with $R G$ replaced by any ring $Lambda$. Note that
the "ring" $K_0 (R G)$ does not in general have an identity element.

Now in case $H = 1$, an $R G$-lattice which is relatively 1-projective is
projective. It follows that $a(R G, 1)$ is the image in $a(R G)$ of the natural
map $K_0 (R G) -> a(R G)$. If the Krull–Schmidt theorem holds for
$R G$-lattices, this map is injective and we have
$K_0 (R G) tilde.equiv a(R G, 1)$. It is unclear whether this is true in the
absence of the Krull–Schmidt theorem.

If $H$ is a subgroup of $G$, we have restriction and induction maps on
representation rings and Grothendieck rings given by restriction and induction
of $R G$-lattices and $R H$-lattices#idx("$\"res\"_(G, H)$")#idx(
  "$\"ind\"_(H, G)$",
)
$
  res_(G, H) & : a(R G) -> a(R H) & wide res_(G, H) & : K_0 (R G) -> K_0 (R H) \
  ind_(H, G) & : a(R H) -> a(R G) &      ind_(H, G) & : K_0 (R H) -> K_0 (R G).
$
Note that $res_(G, H)$ is a ring homomorphism, while $ind_(H, G)$ is just an
additive map, whose image is an ideal by
Proposition~@prop:induced-tensor-hom[(i)].

Tensor induction#idx("tensor", "induction")#idx("induction", "tensor") is not
additive. However, by Proposition~@prop:tensor-induction[(i)], (iii) and (iv),
it induces a well defined ring homomorphism#idx(
  "$\"ind\"_(H, G)^times.o$",
)
$
  ind_(H, G)^times.o : a(R H) slash sum_(K < H) Im(ind_(K, H))
  -> a(R G) slash sum_(K < G) Im(ind_(K, G)).
$
