#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-06-extensions.typ": (
  equivalent-extensions, extension-map, kernel-extension, pushout-sum,
  resolution-to-extension, snake-diagram, yoneda-splice,
)

== Extensions <sec:extensions>

#definition[
  If $M$ and $M'$ are left $Lambda$-modules, an *$n$-fold extension* of $M$ by
  $M'$ is an exact sequence
  $ 0 -> M' -> M_(n-1) -> M_(n-2) -> dots.c -> M_0 -> M -> 0 $
  beginning with $M'$ and ending with $M$, and with $n$ intermediate terms.

  #source(51)Two $n$-fold extensions are *equivalent* if there is a *map of
  $n$-fold extensions*
  $ #extension-map $
  We complete this to an equivalence relation by symmetry and transitivity in
  the usual way.

  For $n = 1$, we simply call an $n$-fold extension an *extension*#idx(
    "extension",
    "of modules",
  ). Note that an equivalence of extensions is an isomorphism of short exact
  sequences.
] <def:n-fold-extension>

#lemma[
  Suppose that $Lambda$ is an algebra over a field $k$, and
  $ 0 -> M_1 -> M_2 -> M_3 -> 0 $
  is a short exact sequence of $Lambda$-modules of finite $k$-dimension. If
  $M_2 tilde.equiv M_1 plus.o M_3$ then the sequence splits; i.e., it represents
  the zero element of $Ext^1_Lambda (M_3, M_1)$.
] <lem:isomorphic-middle-splits>

#proof[
  By dimension counting, the last map in the exact sequence
  $
    0 -> Hom_Lambda (M_3, M_1) -> Hom_Lambda (M_3, M_2)
    -> Hom_Lambda (M_3, M_3) \
    -> Ext^1_Lambda (M_3, M_1)
  $
  is zero, so the previous map is surjective. A pre-image under this map of the
  identity homomorphism of $M_3$ is a splitting for the sequence.
]

An $n$-fold extension of $M$ by $M'$ determines an element of
$Ext^n_Lambda (M, M')$ by completing the diagram
$ #resolution-to-extension $
using the remark after Theorem~@th:comparison. By enlarging the projective
resolution of $M$ if necessary, we may assume that $phi.alt$ is surjective.

It is easy to see that equivalent $n$-fold extensions define the same element of
$Ext^n_Lambda (M, M')$. Conversely, if two $n$-fold extensions define the same
element of $Ext^n_Lambda (M, M')$ then we have a commutative diagram
$ #equivalent-extensions $
and so they are equivalent. Thus we have interpreted $Ext^n_Lambda (M, M')$ as
the set of equivalence classes of $n$-fold extensions of $M$ by $M'$. In
particular, $Ext^1_Lambda (M, M')$ is the set of equivalence classes of
extensions $0 -> M' -> M_0 -> #source(52) M -> 0$, and in this case the
equivalence relation reduces to isomorphism of short exact sequences.

If $zeta in Ext^n_Lambda (M, M')$, we write $hat(zeta)$ for the corresponding
map $tilde(Omega)^n (M) -> M'$. By rechoosing the projective resolution of $M$
if necessary, we may always assume that $hat(zeta)$ is an epimorphism, and we
define $L_zeta$ to be its kernel. Thus we have a commutative diagram
$ #kernel-extension $
where the bottom row is an $n$-fold extension representing $zeta$.

Note that $L_zeta$ is only determined up to addition of projective modules, in
the sense that if $L'_zeta$ is defined using another projective resolution of
$M$ then there are projective modules $P$ and $P'$ with
$L_zeta plus.o P tilde.equiv L'_zeta plus.o P'$.

#subhead[Yoneda composition] If
$
  & 0 -> M' -> M_(n-1) -> dots.c -> M_0 -> M -> 0, \
  & 0 -> M'' -> M'_(m-1) -> dots.c -> M'_0 -> M' -> 0
$
represent elements $zeta in Ext^n_Lambda (M, M')$ and
$eta in Ext^m_Lambda (M', M'')$, then we can form their *Yoneda splice*#idx(
  "Yoneda",
  "splice",
)#idx("splice, Yoneda") as follows.
$ #yoneda-splice $
to obtain an element $eta compose zeta$ of $Ext^(n+m)_Lambda (M, M'')$. This way
we obtain a bilinear map
$
  Ext^m_Lambda (M', M'') times Ext^n_Lambda (M, M')
  -> Ext^(n+m)_Lambda (M, M'')
$
called *Yoneda composition*#idx("Yoneda", "composition")#idx(
  "composition",
  "Yoneda",
). If $m$ or $n$ is equal to zero (recall $Ext^0 = Hom$) this map is defined by
pushing out or pulling back in the obvious way. This composition is clearly
associative, and so it defines a ring structure on $Ext^*_Lambda (M, M)$, and
$Ext^*_Lambda (M, M')$ is an
$Ext^*_Lambda (M', M')$-$Ext^*_Lambda (M, M)$-bimodule. The reader should be
warned that the ring $Ext^*_Lambda (M, M)$ is often far from #source(53)being
commutative, even when $Lambda$ is a group ring $R G$, although it does turn out
that $H^* (R G, R) = Ext^*_(R G) (R, R)$ is _graded commutative_#idx(
  "graded",
  "commutative",
)#idx(
  "commutative graded",
). For further details see Section~@sec:cup-products.

If $zeta in Ext^n_Lambda (M, M')$ is represented by a map
$hat(zeta) : tilde(Omega)^n (M) -> M'$ and $eta in Ext^m_Lambda (M', M'')$ is
represented by $hat(eta) : tilde(Omega)^m (M') -> M''$, we obtain a
representative $hat(eta compose zeta)$ of the Yoneda splice as follows. As in
Section~@sec:projective-injective, we may form
$tilde(Omega)^m (hat(zeta)) : tilde(Omega)^(n+m)(M) -> tilde(Omega)^m (M')$
and then set
$
  hat(eta compose zeta) = hat(eta) compose tilde(Omega)^m (hat(zeta))
  : tilde(Omega)^(n+m)(M) -> M''.
$

#exercises[
  + Show that a chain complex is chain contractible if and only if it is a
    Yoneda splice of split short exact sequences.
  + Show that the natural isomorphism
    $
      Ext^n_Lambda (M plus.o M', M'') tilde.equiv Ext^n_Lambda (M, M'')
      plus.o Ext^n_Lambda (M', M'')
    $
    corresponds to a pushout diagram
    $ #pushout-sum $
    Similarly, write down a pullback diagram for the natural isomorphism
    $
      Ext^n_Lambda (M, M' plus.o M'') tilde.equiv Ext^n_Lambda (M, M')
      plus.o Ext^n_Lambda (M, M'').
    $

    Deduce that Yoneda composition is compatible with direct sum decomposition,
    so that elements of
    $
      Ext^n_Lambda (M_1 plus.o dots.c plus.o M_m, N_1 plus.o dots.c plus.o N_n)
    $
    may be written as matrices $(zeta_(i j))$ with
    $zeta_(i j) in Ext^n_Lambda (M_i, N_j)$, and Yoneda composition corresponds
    to matrix multiplication.
  + (Feit) If $Lambda$ is self injective, show that for $n > 0$ there is a
    natural isomorphism
    $ Ext^n_Lambda (M, M') tilde.equiv Ext^n_Lambda (Omega M, Omega M') $
    compatible with Yoneda composition, so that in particular
    $ Ext^*_Lambda (M, M) tilde.equiv Ext^*_Lambda (Omega M, Omega M) $
    as graded rings (after quotienting out the elements of
    $Ext^0_Lambda (M, M) = Hom_Lambda (M, M)$ which factor through a projective
    module).
  + Suppose that $Lambda$ is a ring and
    $ 0 -> M_1 -> M_2 -> M_3 -> 0 $
    is a short exact sequence of $Lambda$-modules representing an element
    $ rho in Ext^1_Lambda (M_3, M_1). $
    Show that for any $Lambda$-module $N$, the connecting homomorphisms
    $
      Ext^(n-1)_Lambda (N, M_3) -> Ext^n_Lambda (N, M_1), quad
      Ext^(n-1)_Lambda (M_1, N) -> Ext^n_Lambda (M_3, N)
    $
    #source(54)are equal to Yoneda composition with $rho$.
  + Suppose that $Lambda$ is an Artinian ring, and that $P_M$ is the projective
    cover of a $Lambda$-module $M$ with kernel $Omega(M)$. Show that the
    isomorphism between $Hom_Lambda (Omega M, S)$ and $Ext^1_Lambda (M, S)$
    given in Corollary~@cor:ext-simple can be described as follows. If
    $0 != phi.alt in Hom_Lambda (Omega M, S)$ then applying the snake lemma to
    the diagram
    $ #snake-diagram $
    we obtain a non-split extension of $M$ by $S$.
]
