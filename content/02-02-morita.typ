#import "main-defs.typ": *
#import "statements.typ": *

== Morita theory <sec:morita>
#idx("Morita theory", target: [@sec:morita])

#source(37)When are two module categories $lmodule(Lambda, bold("Mod"))$ and
$lmodule(Gamma, bold("Mod"))$ equivalent as abelian categories? Let
$F: lmodule(Lambda, bold("Mod")) -> lmodule(Gamma, bold("Mod"))$,
$F': lmodule(Gamma, bold("Mod")) -> lmodule(Lambda, bold("Mod"))$ be an
equivalence. Since the definition of a projective module is purely categorical,
$F$ and $F'$ induce an equivalence between the full subcategories
$lmodule(Lambda, bold("Proj"))$ and $lmodule(Gamma, bold("Proj"))$ of projective
modules. Among all projective modules, one can recognise the finitely generated
ones as the projective modules $P$ for which $Hom_Lambda (P, -)$ distributes
over direct sums. So $F$ and $F'$ induce an equivalence between the full
subcategories $lmodule(Lambda, bold("proj"))$ and $lmodule(Gamma, bold("proj"))$
of finitely generated projective modules.

The image of the regular representation
$P = F'(lmodule(Gamma, Gamma)) in lmodule(Lambda, bold("Mod"))$ has the
following properties:
+ $P$ is a finitely generated projective module.
+ Every $Lambda$-module is a homomorphic image of a direct sum of copies of $P$.
+ $Gamma tilde.equiv End_Lambda (P)^op$.
Conversely, we shall see that if $P$ is a $Lambda$-module satisfying (i) and
(ii) then letting $Gamma = End_Lambda (P)^op$, $lmodule(Lambda, bold("Mod"))$ is
equivalent to $lmodule(Gamma, bold("Mod"))$. The proof goes via an intermediate
characterisation of equivalent module categories, using bimodules.

#definition[
  A $Lambda$-module $P$ satisfying conditions (i) and (ii) above is called a
  *progenerator*#idx("progenerator") for $lmodule(Lambda, bold("Mod"))$.
] <def:progenerator>

If $Lambda$ is an Artinian ring with
$Lambda slash J(Lambda) tilde.equiv plus.o.big Mat_(n_i) (Delta_i)$ and
corresponding projective indecomposables $P_i$, so that
$lmodule(Lambda, Lambda) = plus.o.big n_i P_i$, then a finitely generated
projective module $P = plus.o.big m_i P_i$ is a progenerator if and only if each
$m_i > 0$. If $Gamma = End_Lambda (P)^op$ then
$Gamma slash J(Gamma) tilde.equiv plus.o.big Mat_(m_i) (Delta_i)$. Thus the
simple modules have changed dimension from $n_i$ to $m_i$, without changing any
other aspect of the representation theory. The smallest possibility for $Gamma$
is to take each $m_i = 1$. In this case, we say that $Gamma$ is the *basic
algebra*#idx("basic algebra")#idx("algebra", "basic") of $Lambda$. Basic
algebras are characterised by the property that every simple module is one
dimensional over the corresponding division ring.

#definition[
  Two rings $Lambda$ and $Gamma$ are said to be *Morita equivalent*#idx(
    "equivalence",
    "Morita",
  ) if there are bimodules $lmodule(Lambda, P_Gamma)$ and
  $lmodule(Gamma, Q_Lambda)$ and surjective maps
  $phi.alt: P times.o_Gamma Q -> Lambda$ of $Lambda$-$Lambda$-bimodules and
  $psi: Q times.o_Lambda P -> Gamma$ of $Gamma$-$Gamma$-bimodules satisfying the
  identities $x psi(y times.o z) = phi.alt(x times.o y) z$ and
  $y phi.alt(z times.o w) = psi(y times.o z) w$ for $x$ and $z$ in $P$ and $y$
  and $w$ in $Q$.
] <def:morita-equivalent>

#lemma[
  If $P$ is a progenerator for $lmodule(Lambda, bold("Mod"))$, and
  $Gamma = End_Lambda (P)^op$ then $Lambda$ and $Gamma$ are Morita equivalent.
] <lem:progenerator-morita>

#proof[
  The ring $Gamma$ acts on $P$ on the right, making $P$ into a
  $Lambda$-$Gamma$-bimodule. Let $Q = Hom_Lambda (P, Lambda)$, as a
  $Gamma$-$Lambda$-bimodule. The map
  $phi.alt: P times.o_Gamma Hom_Lambda (P, Lambda) -> Lambda$ given by
  evaluation is surjective, since $Lambda$ is a homomorphic image of a sum of
  copies of $P$, while the map
  $psi: Hom_Lambda (P, Lambda) times.o_Lambda P -> #source(38)End_Lambda (P)^op$
  given by $psi(f times.o x)^op (y) = f(y).x$ is surjective since $P$ is a
  summand of a finite sum of copies of $lmodule(Lambda, Lambda)$, so that every
  endomorphism is a sum of endomorphisms factoring through
  $lmodule(Lambda, Lambda)$. The identities are easy to check.
]

#lemma[
  If $lmodule(Lambda, P_Gamma)$ and $lmodule(Gamma, Q_Lambda)$ are bimodules as
  in the definition of Morita equivalence, then the maps
  $phi.alt: P times.o_Gamma Q -> Lambda$ and $psi: Q times.o_Lambda P -> Gamma$
  are isomorphisms.
] <lem:morita-isomorphisms>

#proof[
  We shall show that $Ker(phi.alt) = 0$. Let
  $phi.alt(sum_i x_i times.o y_i) = 1 in Lambda$ and suppose that
  $phi.alt(sum_j z_j times.o w_j) = 0$. Then
  $
    sum_j z_j times.o w_j
    & = sum_(i,j) (z_j times.o w_j) phi.alt(x_i times.o y_i)
    = sum_(i,j) z_j times.o psi(w_j times.o x_i) y_i \
    & = sum_(i,j) z_j psi(w_j times.o x_i) times.o y_i
    = sum_(i,j) phi.alt(z_j times.o w_j)(x_i times.o y_i) = 0.
  $
]

#proposition[
  Suppose that $Lambda$ and $Gamma$ are Morita equivalent, with bimodules $P$
  and $Q$ and maps $phi.alt: P times.o_Gamma Q -> Lambda$ and
  $psi: Q times.o_Lambda P -> Gamma$ as in the above definition. Then the
  functors
  $
    Q times.o_Lambda - : lmodule(Lambda, bold("Mod"))
    -> lmodule(Gamma, bold("Mod")),
    quad P times.o_Gamma - : lmodule(Gamma, bold("Mod"))
    -> lmodule(Lambda, bold("Mod"))
  $
  provide an equivalence of abelian categories between
  $lmodule(Lambda, bold("Mod"))$ and $lmodule(Gamma, bold("Mod"))$. They also
  induce equivalences between $lmodule(Lambda, bold("mod"))$ and
  $lmodule(Gamma, bold("mod"))$.
] <prop:morita-functors>

#proof[
  This follows directly from the associativity of tensor product and the above
  lemma.
]

#theorem(title: [Morita])[
  Two module categories $lmodule(Lambda, bold("Mod"))$ and
  $lmodule(Gamma, bold("Mod"))$ are equivalent if and only if
  $lmodule(Lambda, bold("mod"))$ and $lmodule(Gamma, bold("mod"))$ are
  equivalent. This happens if and only if $Gamma tilde.equiv End_Lambda (P)^op$
  for some progenerator $P$ of $lmodule(Lambda, bold("Mod"))$.
] <th:morita>
#idx("theorem", "Morita", target: [@th:morita])

#proof[
  This follows from Lemma~@lem:progenerator-morita and
  Proposition~@prop:morita-functors.
]

#proposition[
  If $lmodule(Lambda, bold("Mod"))$ is equivalent to
  $lmodule(Gamma, bold("Mod"))$ then the centres $Z(Lambda)$ and $Z(Gamma)$ are
  isomorphic rings.
] <prop:morita-centres>

#proof[
  If $lambda in Z(Lambda)$, then multiplication by $lambda$ is a natural
  transformation from the identity functor on $lmodule(Lambda, bold("Mod"))$ to
  itself. Conversely, we claim that all such natural transformations are of this
  form. Given such a natural transformation $phi.alt$, let $lambda$ be the value
  on the identity element of the regular representation,
  $lambda = phi.alt_(lmodule(Lambda, Lambda)) (1) in Lambda$. Then for any
  $Lambda$-module $M$ and $m in M$, we define $f: lmodule(Lambda, Lambda) -> M$
  by $f(lambda) = lambda m$. By naturality we have
  $
    phi.alt_M (m) = phi.alt_M (f(1)) = f(phi.alt_(lmodule(Lambda, Lambda)) (1))
    = f(lambda) = lambda m.
  $
  Thus $phi.alt$ is equal to multiplication by $lambda$, which in particular
  implies that $lambda in Z(Lambda)$.

  It follows that the ring $Z(Lambda)$ may be recovered from
  $lmodule(Lambda, bold("Mod"))$, so that $Z(Lambda) tilde.equiv Z(Gamma)$.
]

#source(39)

#exercises[
  + If $Lambda$ and $Gamma$ are Morita equivalent, prove that $Lambda$ is
    semisimple Artinian if and only if $Gamma$ is.
  + If $Lambda$ and $Gamma$ are finite dimensional algebras over a field, prove
    that a Morita equivalence between $Lambda$ and $Gamma$ induces a bijection
    between the simple $Lambda$-modules and the simple $Gamma$-modules, and that
    corresponding projective modules have the same multiplicities of
    corresponding simple modules in each Loewy layer.
  + If $Lambda$ and $Gamma$ are Morita equivalent $cal(O)$-algebras of the form
    described in Section~@sec:complete-domain, prove that $Lambda$ and $Gamma$
    have the same decomposition matrices.
  + Show that if $Lambda$ and $Gamma$ are Morita equivalent finite dimensional
    algebras then $Lambda$ is self injective if and only if $Gamma$ is self
    injective, and that $Lambda$ is symmetric if and only if $Gamma$ is
    symmetric. Show that if $Lambda$ is Frobenius then $Gamma$ does not have to
    be Frobenius. Show that the basic algebra of a finite dimensional self
    injective algebra is always Frobenius.
  + Show that if $lmodule(Lambda, P_Gamma)$ and $lmodule(Gamma, Q_Lambda)$ are
    bimodules inducing a Morita equivalence between $Lambda$ and $Gamma$ then
    there are adjunctions
    $
      Hom_Lambda (P times.o_Gamma -, -)
      & tilde.equiv Hom_Gamma (-, Q times.o_Lambda -) \
      Hom_Lambda (-, P times.o_Gamma -)
      & tilde.equiv Hom_Gamma (Q times.o_Lambda -, -)
    $
    so that $P times.o_Gamma -$ is both left and right adjoint to
    $Q times.o_Lambda -$.

    Use these adjunctions and the fact that
    $ Z(Lambda) = Hom_(Lambda times.o Lambda^op) (P times.o_Gamma Q, Lambda) $
    to give an alternative proof that $Z(Lambda) = Z(Gamma)$.
]
