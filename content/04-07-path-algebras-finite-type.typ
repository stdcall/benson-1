#import "main-defs.typ": *
#import "statements.typ": *

== Path algebras of finite type <sec:path-algebras-finite-type>

#source(136)The main theorem of this section is Gabriel's theorem, which says
that the path algebra of a (modulated) quiver $Q$ is of finite representation
type if and only if $Q$ is a Dynkin diagram (with some orientation). In this
case, the indecomposable $k Q$-modules are in one–one correspondence with the
positive roots in the associated root system. The proofs we shall give for these
statements are due to Tits and Bernstein–Gel'fand–Ponomarev.

#proposition[
  + If $Q$ is a modulated quiver of finite representation type then the
    underlying valued graph $T$ of $Q$ is a Dynkin diagram.
  + If $Q$ is of tame representation type then $T$ is either Dynkin or
    Euclidean. (In fact $T$ is Euclidean, but this requires the proof, given
    later in this section, that the Dynkin diagrams are indeed of finite
    representation type.)
] <prop:finite-type-dynkin>

#proof[
  + We shall first give the proof in the case of a quiver (i.e., the case where
    all the $attach(d, bl: x, tr: gamma, br: y)$ are equal to one) over an
    infinite field, and then indicate what alterations are needed for the
    general case.

    Suppose $T$ is not a Dynkin diagram. Then by
    Proposition~@prop:bilinear-form-definite, there is a vector
    $v = sum_x n_x v_x in RR^T$ with the $n_x$ non-negative integers, such that
    $(v, v) lt.eq 0$. In other words,
    $ 2 sum_x n_x^2 lt.eq sum_(x dash.em y) n_x n_y. $
    Each edge gets counted both ways round in this sum, so this can be written
    as
    $ sum_x n_x^2 lt.eq sum_(x -> y) n_x n_y. $

    Let $V_x$ be a vector space of dimension $n_x$. We shall show that there are
    infinitely many isomorphism classes of representations of $T$ using these
    particular $V_x$, and hence with dimension vector $(n_x)$. Such a
    representation is determined by assigning a linear map $V_x -> V_y$ to each
    arrow $x -> y$, and two such representations are isomorphic if and only if
    there are automorphisms in $product_x GL(V_x)$ taking one to the other. In
    other words we are interested in the orbits of $product_x GL(V_x)$ on
    $product_(x -> y) Hom(V_x, V_y)$. The former is an algebraic group of
    dimension $sum_x n_x^2$ while the latter is an algebraic variety of
    dimension $sum_(x -> y) n_x n_y$. Moreover, the diagonally embedded scalars
    act trivially, so that we are really looking at the action of
    $product_x GL(V_x)$/scalars, of dimension $(sum_x n_x^2) - 1$. According to
    the above inequality, this algebraic group has strictly smaller dimension
    than the variety, and so there must be infinitely many orbits and $T$ is not
    of finite representation type.

    If $k$ is not infinite, then we apply the above argument over the algebraic
    closure $macron(k)$ of $k$. Each representation over the algebraic closure
    is defined over some finite extension of $k$, and so gives rise to a
    representation of larger #source(137)dimension over $k$ by restriction of
    scalars. Only finitely many representations over $macron(k)$ give rise to
    each representation over $k$ this way, and so we have infinitely many
    representations over $k$.

    If $Q$ is a modulated quiver then we must replace $GL(V_x)$ by
    $GL_(Delta_x)(V_x)$ where $n_x = dim_(Delta_x)(V_x)$ so that this has
    dimension $n_x^2 f_x$. We replace the space $Hom(V_x, V_y)$ by
    $Hom_(Delta_y)(lmodule(y, M)_x^gamma times.o_(Delta_x) V_x, V_y)$ of
    $k$-dimension $n_x n_y attach(d, bl: y, tr: gamma, br: x) f_x$. The
    corresponding inequality is
    $
      sum_x n_x^2 f_x lt.eq sum_(x limits(->)^gamma y) n_x n_y
      attach(d, bl: y, tr: gamma, br: x) f_x
    $
    and so the proof proceeds as before.
  + If $T$ is neither Dynkin nor Euclidean, then there is a Euclidean diagram
    strictly smaller than $T$. Thus by Proposition~@prop:bilinear-form-definite,
    there is a non-zero vector $v$ with non-negative integral coördinates with
    respect to the $v_x$, and with $(v, v) < 0$. The same argument as in (i)
    then shows that the space of orbits with this particular dimension vector is
    at least two dimensional. This is not quite enough to complete the proof,
    because a direct sum of two one parameter families can be used to give a two
    parameter family. However, the point is that $(n v, n v) = n^2 (v, v)$ is
    strictly negative, and grows quadratically in size with $n$. It follows that
    the spaces of orbits with these dimension vectors are also growing
    quadratically in dimension with $n$, whereas finite sums of one parameter
    families can only account for a number of parameters which grows linearly
    with $n$.
]

This means that we must now concentrate on the representations of Dynkin
diagrams. For this purpose, we introduce the concept of a reflection functor,
which is a means of reversing the orientations on some of the edges of a quiver,
while almost giving an equivalence of categories.

#definition[
  A vertex $x$ of a (modulated) quiver is a *sink*#idx("sink") (resp.
  *source*#idx("source")) if all the arrows between $x$ and another vertex point
  towards (resp. away from) $x$.

  If $x$ is any vertex of $Q$ we define a new (modulated) quiver $s_x Q$ with
  the same underlying (labelled) graph as $Q$ but with the orientations of the
  edges meeting $x$ reversed.

  An ordering $x_1, dots, x_n$ of the vertices of $Q$ is *admissible*#idx(
    "admissible",
    "ordering",
  )#idx("ordering, admissible") if for each $i$, $x_i$ is a sink for
  $s_(i+1) dots s_n Q$. There exists an admissible ordering for the vertices of
  $Q$ if and only if there are no oriented cycles in $Q$.
] <def:sink-source>

Now suppose $y$ is a sink in $Q$. We define functors
$
  S_y^+ : lmodule(k Q, bold("mod")) -> lmodule(k(s_y Q), bold("mod")),
  quad
  S_y^- : lmodule(k(s_y Q), bold("mod")) -> lmodule(k Q, bold("mod"))
$
as follows. Given a representation $V = {V_x}$ of $Q$, we define a
representation $S_y^+ (V) = W = {W_x}$ of $s_y Q$ by letting $W_x = V_x$ for
$x != y$, and letting $W_y$ #source(138)be the kernel of the sum of the maps
going towards $V_y$:
$
  0 -> W_y -> plus.o.big_(x limits(->)^gamma y "in" Q)
  lmodule(y, M)_x^gamma times.o_(Delta_x) V_x limits(->)^(phi.alt) V_y.
$
There are obvious maps
$ W_y -> lmodule(y, M)_x^gamma times.o_(Delta_x) V_x $
and hence
$ lmodule(x, M)_y^gamma times.o_(Delta_y) W_y -> W_x $
since $lmodule(x, M)_y^gamma tilde.equiv
Hom_(Delta_y)(lmodule(y, M)_x^gamma, Delta_y)$. Thus the $W_x$ form a
representation of $s_y Q$. A map of representations $V -> V'$ of $Q$ gives rise
in an obvious way to a map of representations $S_y^+ V -> S_y^+ V'$ of $s_y Q$.

The functor $S_y^-$ is constructed dually. Given a representation ${W_x}$ of
$s_y Q$, we let $V_x = W_x$ for $x != y$, and we let $V_y$ be the cokernel of
the sum of the maps going away from $W_y$. Namely, each map
$lmodule(x, M)_y^gamma times.o_(Delta_y) W_y -> W_x$ gives rise as above to a
map $W_y -> lmodule(y, M)_x^gamma times.o_(Delta_x) W_x$, and we have an exact
sequence
$
  W_y limits(->)^psi plus.o.big_(y limits(->)^gamma x "in" s_y Q)
  lmodule(y, M)_x^gamma times.o_(Delta_x) W_x -> V_y -> 0.
$

If we start off with a representation $V$ of $Q$ for which the map $phi.alt$
above is surjective, it is clear that $S_y^- S_y^+ (V) tilde.equiv V$. Thus
$S_y^-$ and $S_y^+$ give an equivalence between the subcategory of
$lmodule(k Q, bold("mod"))$ for which the map $phi.alt$ is surjective, and the
subcategory of $lmodule(k(s_y Q), bold("mod"))$ for which the map $psi$ is
injective.

Now every representation of $Q$ breaks up as a direct sum of the cokernel of
$phi.alt$ concentrated at $y$, and a representation for which $phi.alt$ is
surjective. Similarly, every representation of $s_y Q$ breaks up as a direct sum
of the kernel of $psi$ concentrated at $y$, and a representation for which $psi$
is injective. Thus we have established the following proposition.

#proposition(closed: true)[
  The functors $S_y^+$ and $S_y^-$ establish a bijection between the
  indecomposable representations of $Q$ and the indecomposable representations
  of $s_y Q$, with the exception of the simple module $S_y$ corresponding to $y$
  in each case, which is killed by these functors.
] <prop:reflection-functors>

Now let us examine the effect of these functors on dimension vectors. If $V$ is
a representation of $Q$ for which the map $phi.alt$ is surjective, then the
dimension over $Delta_y$ of $W_y$ is equal to
$
  dim_(Delta_y) W_y = sum_(x limits(->)^gamma y "in" Q)
  attach(d, bl: x, tr: gamma, br: y) dim_(Delta_x) V_x - dim_(Delta_y) V_y.
$
The dimension of the remaining $W_x$ is the same as the dimension of $V_x$.
Therefore the effect of $S_y^+$ on the dimension vector is the same as the
effect of applying the reflection $w_y$.

#source(139)Conversely if $W$ is a representation of $s_y Q$ for which the map
$psi$ is injective, then the effect of $S_y^-$ on the dimension vector of $W$ is
again the same as the effect of applying the reflection $w_y$.

#definition[
  Suppose $x_1, dots, x_n$ is an admissible ordering for the vertices of a
  (modulated) quiver $Q$. Then the *Coxeter functor*#idx(
    "Coxeter",
    "functor",
  )#idx("functor", "Coxeter") with respect to this ordering is the functor
  $
    C^+ = S_(x_1)^+ dots.c S_(x_n)^+ :
    lmodule(k Q, bold("mod")) -> lmodule(k Q, bold("mod")).
  $
  Note that since each arrow gets reversed twice, $s_1 dots s_n Q = Q$. We also
  set
  $
    C^- = S_(x_n)^- dots.c S_(x_1)^- :
    lmodule(k Q, bold("mod")) -> lmodule(k Q, bold("mod")).
  $
] <def:coxeter-functor>

#lemma[
  Given any indecomposable $k Q$-module $V$, either
  + $C^- C^+ (V) tilde.equiv V$, and the effect of $C^+$ on the dimension vector
    of $V$ is the same as the effect of the Coxeter transformation
    $c = w_1 dots w_n$, or
  + $C^+ (V) = 0$.
] <lem:coxeter-functor>

#proof[
  This is clear from the above discussion.
]

We are now ready to classify the indecomposable representations of a Dynkin
diagram.

#theorem(title: [Gabriel])[
  Suppose $Q$ is a modulated quiver whose underlying labelled graph $T$ is a
  Dynkin diagram. Then there is a natural one–one correspondence between the
  indecomposable representations of $Q$ and the positive roots in $RR^T$, in
  such a way that each indecomposable is associated to its dimension vector. In
  particular, $Q$ has finite representation type.
] <th:gabriel>
#idx("Gabriel's theorem", target: [@th:gabriel])#idx(
  "theorem",
  "Gabriel's",
  target: [@th:gabriel],
)

#proof[
  (Bernstein–Gel'fand–Ponomarev [@bib:Bernstein1973]) Choose an admissible
  ordering for the vertices of $Q$ (this may be done since every Dynkin diagram
  is a tree). Let $C^+$ be the corresponding Coxeter functor on
  $lmodule(k Q, bold("mod"))$ and $c$ the corresponding Coxeter transformation
  on $RR^T$. Suppose $V$ is an indecomposable representation of $Q$, with
  dimension vector $v in RR^T$. By Lemma~@lem:coxeter-no-fixed-points[(ii)], for
  some $m gt.eq 1$ the vector $c^m (v)$ is not positive. Thus by
  Lemma~@lem:coxeter-functor we have $(C^+)^m (V) = 0$. Choose $m$ as small as
  possible with $(C^+)^m (V) = 0$. Thus for some $i$,
  $S_(i+1)^+ dots.c S_n^+ (C^+)^(m-1) (V) != 0$ but
  $S_i^+ S_(i+1)^+ dots.c S_n^+ (C^+)^(m-1) (V) = 0$. So by
  Proposition~@prop:reflection-functors we have
  $S_(i+1)^+ dots.c S_n^+ (C^+)^(m-1) (V) tilde.equiv S_i$, and
  $ V tilde.equiv (C^-)^(m-1) S_n^- dots.c S_(i+1)^- (S_i). $
  Thus the dimension vector of $V$ is $c^(-m+1) w_n dots w_(i+1) (v_i)$, a
  positive root. This argument also shows that any indecomposable representation
  with the same dimension vector as $V$ is isomorphic to $V$.

  Conversely, if $v$ is a positive root then for some $m gt.eq 1$ the vector
  $c^m (v)$ is not positive. Choose the shortest expression of the form
  $ w_i dots w_n (w_1 dots w_n)^(m-1) (v) $
  which is not a positive root. Then by Lemma~@lem:roots[(iii)],
  $w_(i+1) dots w_n c^(m-1) (v) = v_i$ and so the representation
  $(C^-)^(m-1) S_n^- dots.c S_(i+1)^- S_i$ has dimension vector $v$.
]

#corollary[
  #source(140)If $Q$ is a modulated quiver of tame representation type then $T$
  is a Euclidean diagram.
] <cor:tame-euclidean>

#proof[
  This follows from Proposition~@prop:finite-type-dynkin and
  Theorem~@th:gabriel.
]

We shall not prove that if $T$ is a Euclidean diagram then $Q$ is in fact tame.
A proof of this can be found in Dlab and Ringel [@bib:Dlab1976]. A complete
classification of the indecomposables in the case of the Euclidean diagrams of
types $tilde(A)_n$, $tilde(D)_n$ and $tilde(E)_n$ may be found in Ringel
[@bib:Ringel1984].
