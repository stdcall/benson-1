#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-17-webb.typ": (
  klein-four-component, projective-string-component, simples-component-a5,
  simples-component-b3, string-component, three-tube,
)

== Webb's Theorem <sec:webb>

Webb#idx("Webb's theorem", target: [@sec:webb])#idx(
  "theorem",
  "Webb's",
  target: [@sec:webb],
) [@bib:Webb1982] constructed a subadditive function on the labelled tree
associated by the Riedtmann structure theorem to a connected component of the
stable quiver of $k G$-modules. It then follows from
Theorem~@th:subadditive-classification that this labelled tree is either a
Dynkin diagram (finite or infinite) or a Euclidean diagram. He then went on to
examine each possibility in detail. His construction used the finite generation
of group cohomology. We shall present Okuyama's approach [@bib:Okuyama1987a] to
this theorem, in which it is only necessary to understand the cohomology of
cyclic groups of prime order.

#lemma[
  Let $M_1$ and $M_2$ be indecomposable $k G$-modules in the same connected
  component of the stable quiver, and let $N$ be a $k G$-module. Then
  $M_1 times.o N$ is projective if and only if $M_2 times.o N$ is projective.
] <lem:tensor-projective-component>

#proof[
  It suffices to prove this in case there is an irreducible map $M_1 -> M_2$. If
  $M_2 times.o N$ is projective, then so is $Omega^2 (M_2) times.o N$ by
  Corollary~@cor:omega-tensor. Thus if we tensor the almost split sequence
  terminating in $M_2$ with $N$ we obtain a sequence with both ends projective,
  and hence the middle is projective. But $M_1 times.o N$ is a summand of this
  middle term by Proposition~@prop:irreducible-maps, and is hence projective.
  The dual argument shows that if $M_1 times.o N$ is projective then so is
  $M_2 times.o N$.
]

Now given a connected component $Q$ of the stable quiver of $k G$-modules, we
construct a subadditive function as follows. Choose a fixed indecomposable
$k G$-module $M_0$ in $Q$. Let $P$ be a minimal $p$-subgroup of $G$ such that
the restriction $M_0 down_P$ is not projective. If $P'$ is a maximal subgroup of
$P$, #source(172)then $M_0 down_(P')$ is projective, $P'$ is normal in $P$ and
$P slash P'$ is a cyclic group of order $p$. Thus by
Corollary~@cor:cyclic-quotient-periodicity, if $X$ is an indecomposable summand
of $M_0 down_P$ then $X tilde.equiv Omega^2 (X)$. By
Proposition~@prop:summand-tensor-dual, $X^* times.o X$ is not projective, and
hence neither are $X^* times.o M_0 down_P$ nor
$(X^* times.o M_0 down_P) up^G tilde.equiv X^* up^G times.o M_0$. Thus by the
lemma, for any indecomposable $k G$-module $M$ in $Q$, $X^* up^G times.o M$ is
not projective.

We now define a function $f$ from the vertices of $Q$ to the natural numbers via
$ f(M) = dim_k Ext^1_(k G) (X up^G, M), $
which is equal to $dim_k Ext^1_(k P) (X, M down_P)$ by the Eckmann–Shapiro
lemma.

#lemma[
  The above constructed function $f$ from the vertices of $Q$ to the natural
  numbers has the following properties:
  + $f(M) > 0$ for every $M$ in $Q$
  + $f(Omega^2 (M)) = f(M)$
  + If $0 -> Omega^2 (M) -> E -> M -> 0$ is the almost split sequence
    terminating in $M$ then
    $ f(E) <= f(M) + f(Omega^2 (M)) = 2 f(M). $
    If $f(E) < 2 f(M)$ then $M$ is periodic (i.e., $Omega^n M tilde.equiv M$ for
    some $n >= 1$).
] <lem:okuyama-function>

#proof[
  + This follows from Corollary~@cor:p-group-ext-vanishing.
  + By Proposition~@prop:dimension-shifting, we have
    $
      f(Omega^2 (M)) & = dim_k Ext^1_(k G) (X up^G, Omega^2 (M)) \
                     & = dim_k Ext^1_(k G) (Omega^2 (X up^G), Omega^2 (M)) \
                     & = dim_k Ext^1_(k G) (X up^G, M) = f(M).
    $
  + This inequality follows from the long exact Ext sequence
    $
      dots.c -> Ext^1_(k P) (X, Omega^2 M down_P) -> Ext^1_(k P) (X, E down_P)
      -> Ext^1_(k P) (X, M down_P) -> dots.c .
    $
    If $M$ is not periodic then the restriction of $M$ to a vertex is still not
    periodic, and so the subgroup $P$ used in the construction of $f$ is a
    proper subgroup of the vertex. But then by
    Proposition~@prop:almost-split-restriction the sequence
    $0 -> Omega^2 (M) -> E -> M -> 0$ splits on restriction to $P$ and so the
    long exact Ext sequence reduces to a short exact sequence and
    $f(E) = 2 f(M)$.
]

#theorem[
  + (Webb [@bib:Webb1982]) Let $T$ be the tree class of a connected component
    $Q$ of the stable quiver of $k G$-modules. Then $T$ is either a Dynkin
    diagram (finite or infinite) or a Euclidean diagram (apart from
    $tilde(A)_n$).
  + The reduced graph $macron(T)$ of $Q$ is also either a Dynkin diagram (finite
    or infinite) or a Euclidean diagram (this time $tilde(A)_n$ is allowed).
] <th:webb>

#proof[
  (Okuyama) By the lemma, the function $f$ commutes with the translation
  $Omega^2$ of $Q$, and satisfies $2 f(x) >= sum_(y in x^-) f(y)$. Thus $f$
  passes to a subadditive function on both $T$ and $macron(T)$. The result now
  follows from Theorem~@th:subadditive-classification.
]

#source(173)

#remark[
  Webb's original subadditive function was constructed as follows
  [@bib:Webb1982] (see also the treatment given in [@bib:Benson1984c]). Let
  $ eta_M (t) = sum_(n=0)^infinity t^n dim_k (P_n) $
  where
  $ dots.c -> P_2 -> P_1 -> P_0 $
  is a minimal resolution of $M$. Then it follows from the finite generation of
  cohomology that $eta_M (t)$ is a rational function of $t$ of the form
  $p(t) slash product_(i=1)^r (1 - t^(k_i))$. If the pole at $t = 1$ of
  $eta_M (t)$ has order $c$ (this is the same as the *complexity*#idx(
    "complexity",
  ) of $M$, see Chapter 5 of Volume II) then let $eta(M)$ be the value of the
  rational function $(product_(i=1)^r k_i) eta_M (t) (1 - t)^c$ at $t = 1$. Then
  $eta(Omega^2 (M)) = eta(M)$, and if $0 -> Omega^2 (M) -> E -> M -> 0$ is the
  almost split sequence terminating in $M$ then $eta(E) <= 2 eta(M)$. Thus $eta$
  passes to a subadditive function on $T$ and $macron(T)$ as above.
]

Following Webb, we now investigate the possibilities allowed by
Theorem~@th:webb.

#theorem[
  Let $Q$ be a connected component of the stable quiver of $k G$-modules. Then
  one of the following occurs.
  + $Q$ consists of all the non-projective modules in a block of $k G$ of finite
    representation type. (We investigate this situation in
    Corollary~@cor:block-finite-type and Theorem~@th:cyclic-defect-quiver, where
    we see that $Q$ is a finite tube $(ZZ slash e) A_(p^n - 1)$.)
  + $Q$ is isomorphic to $ZZ T$ for some infinite Dynkin diagram
    $T = A_infinity$, $B_infinity$, $C_infinity$, $D_infinity$ or
    $A_infinity^infinity$. (Components of type $ZZ A_infinity$ are in fact by
    far the most common. To the best of my knowledge nobody knows of an example
    where $ZZ B_infinity$ or $ZZ C_infinity$ occurs. $ZZ A_infinity^infinity$
    occurs for infinitely many components in the case of a block with dihedral
    defect group in characteristic two, and $ZZ D_infinity$ occurs for
    infinitely many components in the case of a block with semidihedral defect
    group in characteristic two.)
  + $Q$ contains a periodic module. In this case $Q$ is an infinite $n$-tube
    $(ZZ slash n) A_infinity$ for some $n >= 1$.
  + The reduced graph is a Euclidean diagram. (This possibility has been
    investigated by Okuyama [@bib:Okuyama1987a] and Bessenrodt
    [@bib:Bessenrodt1991a], who have shown that this only occurs in
    characteristic two for blocks whose defect group is a Klein four group. In
    this case the reduced graph is $tilde(A)_12$, $tilde(B)_3$ or $tilde(A)_5$.)
] <th:component-types>

#proof[
  By Theorem~@th:webb, the reduced graph is either a Dynkin diagram (finite or
  infinite) or a Euclidean diagram. The latter is covered by case (iv), so we
  concentrate on the former.

  If the reduced graph is a finite Dynkin diagram then by
  Theorem~@th:subadditive-classification[(iii)] the subadditive function $f$
  used in the proof of Theorem~@th:webb is not additive. So by
  Lemma~@lem:okuyama-function[(iii)] there is a periodic module in $Q$. By
  Theorem~@th:happel-preiser-ringel every module in $Q$ is periodic, so $Q$ has
  only finitely many vertices. Now by #source(
    174,
  )Proposition~@prop:finite-component, $Q$ consists of all the modules in a
  block of $k G$ of finite representation type, and we are in case (i).

  If the reduced graph is an infinite Dynkin diagram, i.e., one of $A_infinity$,
  $B_infinity$, $C_infinity$, $D_infinity$, $A_infinity^infinity$, then the tree
  class $T$ is also an infinite Dynkin diagram by
  Lemma~@lem:tree-class-reduced-graph, and by the Riedtmann structure theorem
  $Q tilde.equiv ZZ T slash Pi$ for some admissible group of automorphisms $Pi$.
  If $Pi$ is trivial then $Q tilde.equiv ZZ T$ and we are in case (ii). If $T$
  is one of $A_infinity$, $B_infinity$, $C_infinity$ or $D_infinity$, then every
  non-trivial admissible group of automorphisms will identify two vertices in
  the same $D T r$-orbit. In this case $Q$ contains a periodic module and so by
  Theorem~@th:happel-preiser-ringel, $Q$ is an infinite tube, and we are in case
  (iii). If $T tilde.equiv A_infinity^infinity$ then every non-trivial
  admissible group of automorphisms will either identify two vertices in the
  same $D T r$-orbit so that again using Theorem~@th:happel-preiser-ringel we
  are in case (iii), or produce a quotient with only finitely many
  $D T r$-orbits so that the reduced graph is of type $tilde(A)_n$ and we are in
  case (iv).
]

#example(kind: "Examples")[
  + In Section~@sec:klein-four we described the classification of modules for
    the Klein four group#idx("Klein four group")#idx("four", "group, Klein"). It
    is not hard to see that for the indecomposable modules $M$ of even dimension
    we have $Omega(M) tilde.equiv M$, so that $M$ lies in a 1-tube. The
    indecomposable rational canonical forms corresponding to the modules going
    up this 1-tube correspond to the ascending powers of a given irreducible
    polynomial. For example, if $k$ is algebraically closed, the 1-tubes take
    the form
    $ V_(1, a) arrows.rl V_(2, a) arrows.rl V_(3, a) arrows.rl dots.c $
    and so the corresponding almost split sequences are
    $
      0 -> V_(n, a) -> V_(n-1, a) plus.o V_(n+1, a) -> V_(n, a) -> 0.
    $
    So these modules form a family of 1-tubes parametrised by $PP^1(k)$. The
    remaining modules are the projective indecomposable and the modules of the
    form $Omega^(plus.minus n) (k)$. These form a quiver component of type
    $ZZ tilde(A)_12$.
    $ #klein-four-component $

  + We also described in Section~@sec:klein-four the classification of modules
    for the alternating group $A_4$#idx("alternating group", "$A_4$")#idx(
      "group",
      "alternating",
      "$A_4$",
    ) in characteristic two. The modules $W_(n, alpha)$ for
    $alpha in.not {omega, macron(omega)}$ are periodic of period one and hence
    lie in 1-tubes. For $alpha in {omega, macron(omega)}$ the #source(
      175,
    )modules $W_(n, alpha)(1)$, $W_(n, alpha)(omega)$ and
    $W_(n, alpha)(macron(omega))$ form a 3-tube as follows:
    $ #three-tube $
    (identify left and right edges to make a 3-tube)

    The modules $Omega^(plus.minus n)$ of simples all lie in a single quiver
    component isomorphic to $ZZ tilde(A)_5$ as follows:
    $ #simples-component-a5 $
    (identify top and bottom edges to make a $ZZ tilde(A)_5$).

    The same story holds over any field containing three cube roots of unity. If
    $k$ does not have three cube roots of unity the simple modules are $k$ and a
    two dimensional module $S$ which when tensored with the field extension
    obtained by adjoining cube roots of unity gives
    $omega plus.o macron(omega)$. In this case the only difference is that the
    modules $Omega^(plus.minus n)$ of simples form a quiver component #source(
      176,
    )isomorphic to $ZZ tilde(B)_3$#idx("$ZZ tilde(B)_3$") as follows:
    $ #simples-component-b3 $
    (No identifications).

  + In Section~@sec:dihedral-groups we described the classification of modules
    for the dihedral group $D_(4q)$ in characteristic two, where $q$ is a power
    of two. The almost split sequences and Auslander–Reiten quiver are described
    as follows. We define two functions $L_q$ and $R_q$ from the set $cal(W)$ of
    words to itself as follows. Let $A = (a b)^(q-1) a$ and $B = (b a)^(q-1) b$.
    If a word $C$ starts with $A b^(-1)$ or $B a^(-1)$ then $L_q (C)$ is
    obtained by removing that part; otherwise $L_q (C) = A^(-1) b C$ or
    $B^(-1) a C$, whichever is a word. Similarly if $C$ ends in $a B^(-1)$ or
    $b A^(-1)$ then $R_q (C)$ is obtained by removing that part; otherwise
    $R_q (C) = C a^(-1) B$ or $C b^(-1) A$, whichever is a word. The maps $L_q$
    and $R_q$ restrict to bijections from the set of words of modules of the
    first kind for $D_(4q)$ with $A$, $B$ (resp. $A^(-1)$, $B^(-1)$) removed to
    the same set with $A^(-1)$, $B^(-1)$ (resp. $A$, $B$) removed, and on this
    set with $A^(plus.minus 1)$, $B^(plus.minus 1)$ removed we have
    $L_q compose R_q = R_q compose L_q$.

    The Auslander–Reiten translate on modules for $D_(4q)$ is given on modules
    of the first kind by $Omega^2 M(C) = M(L_q R_q C)$ ($C != A^(-1), B^(-1)$),
    and on modules of the second kind by
    $Omega^2 M(C, phi.alt) tilde.equiv M(C, phi.alt)$. The almost split sequence
    terminating in $M(C)$ is
    $ 0 -> M(L_q R_q C) -> M(L_q C) plus.o M(R_q C) -> M(C) -> 0 $
    unless $C$ or $C^(-1)$ is $A$, $B$ or $A B^(-1)$, in which case the almost
    split sequences are
    $
      0 -> M(A) -> M(A b^(-1) A) -> M(A) -> 0 \
      0 -> M(B) -> M(B a^(-1) B) -> M(B) -> 0 \
      0 -> M(A^(-1) B) -> M((a b)^(q-1)) plus.o M((b a)^(q-1)) plus.o P
      -> M(A B^(-1)) -> 0
    $
    where $P$ is the projective indecomposable of dimension $4 q$.

    If $p(x)$ is an irreducible polynomial in $k[x]$, let $phi.alt_(n, p)$
    denote an indecomposable automorphism of a finite dimensional vector space,
    with rational canonical form associated to the polynomial $p(x)^n$. Then the
    almost split sequence terminating in the module of the second kind
    $M(C, phi.alt_(n, p))$ is
    $
      0 -> M(C, phi.alt_(n, p)) -> M(C, phi.alt_(n+1, p)) plus.o
      M(C, phi.alt_(n-1, p)) -> M(C, phi.alt_(n, p)) -> 0
    $
    (where the term $M(C, phi.alt_(n-1, p))$ is absent if $n = 1$).

    #source(177)The modules of the first kind form an infinite set of quiver
    components of type $ZZ A_infinity^infinity$#idx("$ZZ A_infinity^infinity$")
    $ #string-component $
    One of these has $P$ attached to it:
    $ #projective-string-component $
    There are also two 1-tubes of modules of the first kind:
    $
      M(A) arrows.rl M(R_q A) arrows.rl M(R_q^2 A) arrows.rl dots.c \
      M(B) arrows.rl M(R_q B) arrows.rl M(R_q^2 B) arrows.rl dots.c
    $
    All the modules of the second kind lie in 1-tubes:
    $
      M(C, phi.alt_(1, p)) arrows.rl M(C, phi.alt_(2, p)) arrows.rl
      M(C, phi.alt_(3, p)) arrows.rl dots.c
    $
]
