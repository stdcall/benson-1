#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-09-relative-cohomology.typ": (
  relative-comparison, relative-horseshoe,
)

#source(93)
== Relative cohomology <sec:relative-cohomology>
#idx("cohomology", "relative", target: [@sec:relative-cohomology])#idx(
  "relative",
  "cohomology",
  target: [@sec:relative-cohomology],
)

#lemma(title: [Relative Schanuel's lemma])[
  Suppose $0 -> M_1 -> X_1 -> M -> 0$ and $0 -> M_2 -> X_2 -> M -> 0$ are
  $H$-split short exact sequences of modules with $X_1$ and $X_2$ projective
  relative to $H$. Then $M_1 plus.o X_2 tilde.equiv M_2 plus.o X_1$.
] <lem:relative-schanuel>
#idx("lemma", "relative", "Schanuel's", target: [@lem:relative-schanuel])#idx(
  "relative",
  "Schanuel's lemma",
  target: [@lem:relative-schanuel],
)#idx("Schanuel's lemma", "relative", target: [@lem:relative-schanuel])

#proof[
  Form a pullback diagram just as in the proof of Schanuel's
  lemma~@lem:schanuel.
]

#definition[
  A *relatively $H$-projective resolution*#idx(
    "projective",
    "resolution",
    "relatively",
  )#idx("relatively", "projective", "resolution")#idx(
    "resolution",
    "relatively projective",
  ) of an $R G$-module $M$ is a long exact sequence
  $
    dots.c -> X_2 limits(arrow.r.long)^(partial_2) X_1
    limits(arrow.r.long)^(partial_1) X_0
  $
  of $R G$-modules with the following properties.
  + $X_0 slash Im(partial_1) tilde.equiv M$.
  + Each $X_i$ is projective relative to $H$.
  + Each sequence
    $ 0 -> X_(n+1) slash Ker(partial_(n+1)) -> X_n -> Im(partial_n) -> 0 $
    as well as
    $ 0 -> Im(partial_1) -> X_0 -> M -> 0 $
    splits on restriction to $H$.
] <def:relative-projective-resolution>

Since the surjection $M down_H up^G -> M$ always splits on restriction to $H$,
relatively $H$-projective resolutions always exist.

#theorem(title: [Comparison theorem], closed: true)[
  Given a map of modules $M -> M'$ and relatively $H$-projective resolutions of
  $M$ and $M'$, we can extend to a map of chain complexes
  $ #relative-comparison $

  Given any two such maps ${f_n}$ and ${f'_n}$, there is a chain homotopy
  $h_n : X_n -> Y_(n+1)$, so that
  $f_n - f'_n = partial'_(n+1) compose h_n + h_(n-1) compose partial_n$.
] <th:relative-comparison>
#idx("comparison theorem", target: [@th:relative-comparison])#idx(
  "theorem",
  "comparison",
  target: [@th:relative-comparison],
)

If $M'$ is an $R G$-module and
$
  dots.c -> X_2 limits(arrow.r.long)^(partial_2) X_1
  limits(arrow.r.long)^(partial_1) X_0
$
is a relatively $H$-projective resolution of an $R G$-module $M$, we have a
chain complex
$
  Hom_(R G) (X_0, M') limits(arrow.r.long)^(delta^0) Hom_(R G) (X_1, M')
  limits(arrow.r.long)^(delta^1) Hom_(R G) (X_2, M') -> dots.c
$
where $delta^n$ is given by composition with $partial_(n+1)$. By the comparison
theorem this complex is independent of choice of relatively $H$-projective
resolution, up to #source(94)chain homotopy equivalence. Thus its cohomology
groups are independent of this choice, and we define
$ Ext^n_(G, H) (M, M') = H^n (Hom_(R G) (bold(X), M'), delta^*). $
We can now define the *relative cohomology* of $G$ to be
$ H^n (G, H, M) = Ext^n_(G, H) (R, M). $

Just as in Section~@sec:extensions, we may view elements of
$Ext^n_(G, H) (M, M')$ as equivalence classes of $H$-split $n$-fold extensions
$ 0 -> M' -> M_(n-1) -> dots.c -> M_0 -> M -> 0. $
Two such are equivalent if there is a map of $H$-split $n$-fold extensions
taking one to the other. We complete this as usual to an equivalence relation.
Note that two $H$-split $n$-fold extensions can be equivalent as $n$-fold
extensions without being equivalent as $H$-split $n$-fold extensions, so that
the natural map
$ Ext^n_(G, H) (M, M') -> Ext^n_(R G) (M, M') $
is not necessarily injective.

Yoneda composition gives an associative bilinear product
$
  Ext^m_(G, H) (M', M'') times Ext^n_(G, H) (M, M')
  -> Ext^(m+n)_(G, H) (M, M'')
$
and hence a ring structure on $Ext^*_(G, H) (M, M)$. Note that in general the
ring $Ext^*_(G, H) (R, R)$ is not necessarily Noetherian, even when $R$ is a
field. This is in contrast to the case of $Ext^*_(R G) (R, R)$, which is known
to be Noetherian whenever $R$ is (see Chapter 4 of Volume II).

#subhead[Long exact sequences]
#idx("long exact sequence")#idx("exact sequence, long")#idx(
  "sequence",
  "long exact",
)

#lemma(title: [Relative horseshoe lemma], closed: true)[
  If $0 -> M' -> M -> M'' -> 0$ is an $H$-split short exact sequence of
  $R G$-modules, then given relatively $H$-projective resolutions
  $ dots.c -> X'_2 -> X'_1 -> X'_0, quad dots.c -> X''_2 -> X''_1 -> X''_0 $
  of $M'$ and $M''$, we may complete to a short exact sequence of chain
  complexes
  $ #relative-horseshoe $
] <lem:relative-horseshoe>
#idx("horseshoe lemma", "relative", target: [@lem:relative-horseshoe])#idx(
  "lemma",
  "relative",
  "horseshoe",
  target: [@lem:relative-horseshoe],
)#idx("relative", "horseshoe lemma", target: [@lem:relative-horseshoe])

#source(95)Thus as in Section~@sec:long-exact-sequences, if $M_0$ is another
$R G$-module we have long exact sequences
$
  0 -> Hom_(R G) (M'', M_0) -> Hom_(R G) (M, M_0) -> Hom_(R G) (M', M_0) -> \
  Ext^1_(G, H) (M'', M_0) -> dots.c -> Ext^n_(G, H) (M'', M_0) -> \
  Ext^n_(G, H) (M, M_0) -> Ext^n_(G, H) (M', M_0)
  -> Ext^(n+1)_(G, H) (M'', M_0) -> dots.c
$
and
$
  0 -> Hom_(R G) (M_0, M') -> Hom_(R G) (M_0, M) -> Hom_(R G) (M_0, M'') -> \
  Ext^1_(G, H) (M_0, M') -> dots.c -> Ext^n_(G, H) (M_0, M') -> \
  Ext^n_(G, H) (M_0, M) -> Ext^n_(G, H) (M_0, M'')
  -> Ext^(n+1)_(G, H) (M_0, M') -> dots.c
$
