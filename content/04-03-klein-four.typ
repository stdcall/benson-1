#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-03-klein-four.typ": klein-four-ext-quiver, kronecker-quiver

== Representations of the Klein four group <sec:klein-four>

In this section we work through an example in detail to illustrate the concepts
introduced in the last two sections.

Denote by $V_4$#idx("$V_4$") the Klein four group#idx("Klein four group")#idx(
  "four",
  "group, Klein",
)#idx("group", "Klein four") (Kleinsche Vierergruppe), namely a direct product
of two cyclic groups of order two
$ V_4 = chevron.l x, y | x^2 = y^2 = [x, y] = 1 chevron.r. $
Let $k$ be a field of characteristic two. We shall investigate the
representations of $k V_4$. According to Section~@sec:p-groups, there is only
one simple $k V_4$-module, namely the trivial one dimensional module $k$, and we
have
$ dim_k Ext^1_(k V_4)(k, k) = 2. $
Thus the Ext-quiver for $k V_4$ is the following graph:
$ #klein-four-ext-quiver $
The arrows $a$, $b$ correspond to elements $x - 1$ and $y - 1$ of $J(k V_4)$
complementing $J^2(k V_4)$. The relations are $a^2 = 0$, $b^2 = 0$ and
$a b = b a$.

Unfortunately the kernel of the natural map from the path algebra of this graph
to $k V_4$ is rather large, and so we try to be a bit cleverer. Now according to
Section~@sec:p-groups, if we want to understand indecomposable $k V_4$-modules,
it suffices to understand $Lambda$-modules, where
$Lambda = k V_4 slash Soc(k V_4)$ is the three dimensional ring with basis
elements $1$, $x - 1$ and $y - 1$, and
$ (x - 1)^2 = (y - 1)^2 = (x - 1)(y - 1) = 0. $

#definition[
  The *Kronecker quiver*#idx("Kronecker quiver")#idx("quiver", "Kronecker") is
  the following graph:
  $ Q = #kronecker-quiver $
] <def:kronecker-quiver>

The path algebra of this quiver has two simple modules, $S_1$ and $S_2$,
corresponding to $x_1$ and $x_2$. We have
$
  dim_k Ext^1_(k Q)(S_i, S_j) = cases(
    2 & quad "if" i = 1\, j = 2,
    0 & quad "otherwise."
  )
$

If $M$ is a $k Lambda$-module, we obtain a representation of the quiver $Q$ by
letting the vector spaces $V_1$ and $V_2$ corresponding to the vertices $x_1$
and $x_2$ be $M slash (Im(x - 1) + Im(y - 1))$ and $Im(x - 1) + Im(y - 1)$. The
relations above for #source(120)$(x - 1)$ and $(y - 1)$ imply that they both act
trivially on $Im(x - 1) + Im(y - 1)$, so that they induce maps $a$ and $b$ from
$V_1$ to $V_2$.

Conversely if $a, b : V_1 -> V_2$ is a representation of $Q$, we obtain a
$k Lambda$-module whose underlying vector space is $V_1 plus.o V_2$, and where
$x$ acts as $1 + a$, and $y$ acts as $1 + b$.

These recipes are not quite inverse, but they do set up a one–one correspondence
between $Lambda$-modules and representations of $Q$ for which
$V_2 = Im(a) + Im(b)$, and preserving direct sums. There is only one
indecomposable representation of $Q$ for which $V_2 != Im(a) + Im(b)$, namely
the simple module $S_2$, and so the above is a one–one correspondence between
indecomposable $Lambda$-modules and indecomposable $k Q$-modules other than
$S_2$.

Beware that the isomorphism between a $Lambda$-module $M$ and its image under
the composite of these functors depends on a choice of complement for
$Im(x - 1) + Im(y - 1)$ in $M$, and so it is not a natural isomorphism of
functors. In particular, endomorphism rings are not preserved by the above
correspondences.

#theorem(title: [Kronecker])[
  Suppose $a, b : V_1 -> V_2$ is a pair of linear maps constituting a finite
  dimensional indecomposable representation of the Kronecker quiver over a field
  $k$. Then one of the following holds:
  + The vector spaces $V_1$ and $V_2$ have the same dimension, and the
    determinant of $a + lambda b$ is a non-zero element of $k[lambda]$.

    In this case, if $det(a) != 0$ then the representations can be written in
    the form
    $ a |-> I, quad b |-> J $
    where $I$ is an identity matrix and $J$ is an indecomposable rational
    canonical form#idx("rational canonical form")#idx(
      "canonical form, rational",
    ). A rational canonical form is indecomposable if and only if it has only
    one block, and is associated to a polynomial which is a power of an
    irreducible polynomial over $k$.

    If $det(a) = 0$ then the representation can be written in the form
    $ a |-> J_0, quad b |-> I $
    where $J_0$ is a rational canonical form associated with a polynomial of the
    form $lambda^n$. In some sense this corresponds to the "rational canonical
    form at infinity."
  + The dimension of $V_2$ is one larger than the dimension of $V_1$, and bases
    may be chosen so that $a$ and $b$ are represented by the matrices
    $
      a = mat(1, , 0, 0; , dots.down, , dots.v; 0, , 1, 0), quad
      b = mat(0, 1, , 0; dots.v, , dots.down, ; 0, 0, , 1).
    $
  + The dimension of $V_1$ is one larger than the dimension of $V_2$, and bases
    may be chosen so that $a$ and $b$ are represented by the transposes of the
    above matrices.
] <th:kronecker>

#source(121)

#proof[
  We first deal with case (i). If $V_1$ and $V_2$ have the same dimension and
  $det(a) != 0$, then we can choose bases so that $a$ is represented by the
  identity matrix. Then $b$ is determined up to conjugation, and the result
  follows from the theory of rational canonical forms.

  In case $det(a + lambda b) != 0$ in $k[lambda]$ but $det(a) = 0$ we argue as
  follows. We homogenise by introducing a new variable $mu$, so that
  $det(mu a + lambda b)$ is a non-zero homogeneous polynomial in
  $k[lambda, mu]$. Suppose first that $k$ is infinite. Then there is some point
  $(lambda_1 : mu_1)$ in the projective line $PP^1(k)$ over $k$ so that
  $det(mu_1 a + lambda_1 b) != 0$. We set $a' = mu_1 a + lambda_1 b$ and
  $b' = a$ and argue as before. Since a rational canonical form can have at most
  one eigenvalue in $k$, we deduce that $det(b) != 0$ and the result follows by
  reversing the rôles of $a$ and $b$.

  In case $k$ is finite we use Galois descent#idx("Galois descent")#idx(
    "descent, Galois",
  ) as follows. For some finite extension $macron(k)$ of $k$ we can find a point
  $mu_1 a + lambda_1 b$ with $(lambda_1 : mu_1) in PP^1(macron(k))$ as above.
  Now the representation does not have to stay indecomposable over $macron(k)$,
  but it will be a sum of Galois conjugates of the same indecomposable, and the
  restriction back to $k$ will just be a direct sum of $[macron(k) : k]$ copies
  of the original representation. Thus we again deduce that $det(b) != 0$ and
  proceed as before.

  If case (i) does not occur then either $V_1$ and $V_2$ have different
  dimensions or $a + lambda b$ is singular as a matrix over $k[lambda]$. In
  either case, after dualising (and switching the rôles of $V_1$ and $V_2$) if
  necessary, we have a vector $v(lambda) = sum_(i=0)^n (-1)^i v_i lambda^i$
  satisfying $(a + lambda b) v(lambda) = 0$, i.e., $a v_0 = 0$,
  $a v_i = b v_(i-1)$ and $b v_n = 0$. Suppose such a $v(lambda)$ has been
  chosen with $n$ minimal. Our goal is to show that $dim V_1 = n + 1$,
  $dim V_2 = n$, and for a suitable choice of bases
  $
    a + lambda b = mat(
      lambda, 1, , 0;
      , dots.down, dots.down, ;
      0, , lambda, 1;
    ).
  $
  Let us write $E_lambda (n)$ for this matrix.

  First we claim that the vectors $a v_1, dots, a v_n$ are linearly independent.
  For otherwise if $sum_(i=1)^n alpha_i a v_i = 0$, we set $alpha_0 = 0$ and
  $v'_j = sum_(i=0)^n alpha_i v_(i-n+j)$ (with the convention that $v_i = 0$ if
  $i < 0$), and notice that
  $
    #aligned-rows(
      (
        $(a + lambda b) sum_(j=0)^(n-1) (-1)^j v'_j lambda^j$,
        $= sum_(j=0)^n (-1)^j (a v'_j - b v'_(j-1)) lambda^j$,
      ),
      (
        $$,
        $= sum_(i,j=0)^n (-1)^j alpha_i (a v_(i-n+j) - b v_(i-n+j-1))
        lambda^j = 0,$,
      ),
    )
  $
  contradicting the minimality of $n$. In particular it follows that
  $v_0, dots, v_n$ are linearly independent.

  Now if we choose our basis of $V_1$ to begin with $v_0, dots, v_n$ and of
  $V_2$ to begin with $a v_1, dots, a v_n$, then $a + lambda b$ is represented
  by a matrix of the form
  $ mat(E_lambda (n), C + lambda D; 0, A' + lambda B'). $

  #source(122)Thus the theorem will follow as soon as we show that we can find
  matrices $X$ and $Y$ with
  $
    mat(I, X; 0, I) mat(E_lambda (n), C + lambda D; 0, A' + lambda B')
    mat(I, Y; 0, I) = mat(E_lambda (n), 0; 0, A' + lambda B')
  $
  since one of the hypotheses was indecomposability. This equation is the same
  as
  $ X(A' + lambda B') + (C + lambda D) + E_lambda (n) Y = 0. $

  Separating out the constant term and the coefficient of $lambda$, we obtain
  $
     X A' + C + overline(Y) & = 0 \
    X B' + D + underline(Y) & = 0
  $
  where $overline(Y)$ and $underline(Y)$ denote the matrices obtained by
  removing the first, resp. the last row of $Y$. Eliminating the terms in $Y$,
  we end up with an equation of the form
  $
    (x_11, dots, x_(1 m), x_21, dots, x_(n m)) scaled(
      (underbrace(
          mat(
            delim: #none,
            A', , , 0;
            -B', A', , ;
            , -B', dots.down, ;
            , , dots.down, A';
            0, , , -B';
          ),
          n - 1,
        ))
    ) \
    = (d_21 - c_11, dots, d_(2, m-1) - c_(1, m-1), d_31 - c_21, dots,
      d_(n, m-1) - c_(n-1, m-1))
  $
  and so it remains to show that this $n m times (n - 1)(m - 1)$ matrix has full
  column rank. But a column vector
  $ (u_11, dots, u_(1, m-1), u_21, dots, u_(n-1, m-1)) $
  annihilated by this matrix gives rise to a vector
  $
    u(lambda) = ( & u_11 - u_21 lambda + dots.c plus.minus u_(n-1, 1)
                    lambda^(n-2), dots, \
                  & u_(1, m-1) - u_(2, m-1) lambda + dots.c
                    plus.minus u_(n-1, m-1) lambda^(n-2))
  $
  of degree at most $n - 2$ in $lambda$ satisfying
  $(A' + lambda B') u(lambda) = 0$. A non-zero vector annihilated by
  $E_lambda (n)$ has degree at least $n$, so $E_lambda (n)$ maps the vectors of
  degree at most $n - 1$, a space of dimension $n(n + 1)$, bijectively onto
  those of degree at most $n$; hence there is $w(lambda)$ of degree at most
  $n - 1$ with $E_lambda (n) w(lambda) = -(C + lambda D) u(lambda)$. Thus
  $
    mat(E_lambda (n), C + lambda D; 0, A' + lambda B') vec(w(lambda), u(lambda))
    = 0
  $
  and so there is also a column vector of degree at most $n - 1$ in $lambda$
  annihilated by $a + lambda b$, contradicting the minimality of
  $n$.#ed-note[The book argued with a row vector annihilated by this matrix; but
    such a row vector always exists, since the matrix has more rows than
    columns, and it gives no column vector annihilated by $a + lambda b$. For
    Kronecker's classification over an algebraically closed field see Simson and
    Skowroński [@bib:Simson2007], Theorem XI.4.6.]
]

We may now read off the classification of indecomposable modules for $k V_4$.

#theorem(
  title: [Bašev [@bib:Basev1961], Heller and Reiner [@bib:Heller1961]],
  head-break: true,
)[
  A complete set of representatives of isomorphism classes of indecomposable
  $k V_4$-modules is given as follows.
  + The projective indecomposable module of dimension $4$.
  + #source(123)For each even dimension $2 n$ and each indecomposable rational
    canonical form $J$ of dimension $n$ there is an indecomposable
    representation
    $ x |-> mat(I, I; 0, I) quad y |-> mat(I, J; 0, I). $
  + For each even dimension $2 n$ there is an indecomposable representation of
    the form
    $ x |-> mat(I, J_0; 0, I) quad y |-> mat(I, I; 0, I). $
    where $J_0$ denotes the rational canonical form associated to the polynomial
    $lambda^n$.
  + For each odd dimension $2 n + 1$ there are two indecomposable
    representations
    $
      x |-> mat(
        augment: #(hline: 3, vline: 1),
        , 1, , 0, 0;
        I, , dots.down, , dots.v;
        , 0, , 1, 0;
        0, , I, , ;
      )
      quad
      y |-> mat(
        augment: #(hline: 3, vline: 1),
        , 0, 1, , 0;
        I, dots.v, , dots.down, ;
        , 0, 0, , 1;
        0, , I, , ;
      )
    $
    and #statement-comment[(v)]
    $
      x |-> mat(
        augment: #(hline: 4, vline: 1),
        , 1, , 0;
        I, , dots.down, ;
        , 0, , 1;
        , 0, dots.c, 0;
        0, , I, ;
      )
      quad
      y |-> mat(
        augment: #(hline: 4, vline: 1),
        , 0, dots.c, 0;
        , 1, , 0;
        I, , dots.down, ;
        , 0, , 1;
        0, , I, ;
      )
    $
    which are isomorphic if and only if $n = 0$.
] <th:klein-four-modules>

#proof[
  Apart from the projective indecomposable module, the indecomposable
  $k V_4$-modules are in one–one correspondence with those for $Lambda$. Apart
  from the one dimensional simple module $S_2$, these are in one–one
  correspondence with those for $k Q$. The modules appearing in (ii) and (iii)
  correspond to case (i) of the previous theorem, while cases (iv) and (v)
  correspond to cases (ii) and (iii). The disappearance of the module $S_2$
  corresponds to the isomorphism between (iv) and (v) in the case $n = 0$.
]

#remark[
  If $k$ is algebraically closed, the indecomposable rational canonical forms
  are powers of a linear factor $(lambda - alpha)^n$. We write
  $V_(n, alpha)$#idx("$V_(n, alpha)$") for the corresponding indecomposable
  representation of type (ii) in this case. The representations of type (iii)
  are written $V_(n, infinity)$. Thus for each $n >= 1$ there is a family of
  modules parametrised by $PP^1(k)$. The modules of type (iv) are the modules
  $Omega^(-n)(k)$, and those of type (v) are the modules $Omega^n (k)$.
]

#source(124)We can also read off the classification of indecomposable modules
for the alternating group $A_4$#idx("alternating group", "$A_4$")#idx(
  "group",
  "alternating",
  "$A_4$",
) in characteristic two using Clifford theory. Namely, every such module is a
summand of a module induced from $V_4$. Let us suppose for convenience that $k$
is algebraically closed, and let ${1, omega, macron(omega)}$ be the cube roots
of unity in $k$. The action of an element $t$ of order three on the
indecomposable $k V_4$-modules is easy to see. Namely, it fixes the modules
$Omega^(plus.minus n)(k)$, so that these extend in three ways to form the
modules $Omega^(plus.minus n)$ of the three one dimensional simples $k$,
$omega$, $macron(omega)$. The action on $PP^1(k)$ is via
$alpha |-> 1 slash (1 - alpha)$. Thus the fixed points correspond to the cube
roots of unity $omega$ and $macron(omega)$. For a non-fixed $alpha$,
$W_(n, alpha) = V_(n, alpha) up^(A_4)$#idx("$W_(n, alpha)$") is indecomposable.
For $alpha in {omega, macron(omega)}$ $V_(n, alpha) up^(A_4)$ has three
summands, $W_(n, alpha)(1)$,
$W_(n, alpha)(omega) = W_(n, alpha)(1) times.o omega$ and
$W_(n, alpha)(macron(omega)) = W_(n, alpha)(1) times.o macron(omega)$. For
example, $W_(n, macron(omega))(1)$ is given in terms of matrices as follows.
$
  x |-> mat(I, X; 0, I) quad y |-> mat(I, Y; 0, I) \
  t |-> diag(
    omega^(n-2), omega^(n-4), dots, omega^(-n), omega^n,
    omega^(n-2), dots, omega^(-n+2)
  )
$
where $X$ (resp. $Y$) is an $n times n$ matrix with $macron(omega)$ (resp.
$omega$) on every diagonal entry, $omega$ (resp. $macron(omega)$) on every entry
just below the diagonal, and zeros elsewhere.

#subhead[Linear relations] Following Ringel [@bib:Ringel1975b], we use
Kronecker's classification to classify the linear relations on a vector space.
We shall use this later in the classification of representations of dihedral
groups.

#definition[
  A *linear relation*#idx("linear relation")#idx("relations", "linear") on a
  vector space $V$ is a subspace of $V times V$. For example, if
  $lambda : V -> V$ is an endomorphism then we also write $lambda$ for the
  *graph*#idx("graph") of $lambda$, namely the relation
  ${(v, lambda(v))} <= V times V$. If $C$ is a linear relation and $U$ is a
  subspace of $V$, we write $C U$ for
  ${v in V | "for some" u in U, (u, v) in C}$. We write $C^(-1)$ for the linear
  relation ${(v, w) in V times V | (w, v) in C}$. If $C$ and $D$ are relations,
  we write $C D$ for the linear relation
  ${(v, w) in V times V | "for some" x in V, (v, x) in C "and" (x, w) in D}$.
] <def:linear-relation>

If $a, b : W -> V$ is a representation of the Kronecker quiver, then we obtain a
linear relation ${(a(v), b(v)), v in W} <= V times V$. Conversely, if
$C <= V times V$ is a linear relation then the projections $pi_1, pi_2 : C -> V$
give us a representation of the Kronecker quiver. These recipes set up a one–one
correspondence between the representations of the Kronecker quiver for which
$Ker(a) inter Ker(b) = 0$, and linear relations. The only indecomposable
representation of the Kronecker quiver for which $Ker(a) inter Ker(b) != 0$ is
the simple module $S_1$. Thus we may read off the list of indecomposable linear
relations from Theorem~@th:kronecker.

One particular consequence of this classification which we shall need later is
the following. If $C$ is a linear relation on $V$, let
$C' = union.big_n C^n 0_V$, and $C'' = inter.big_n C^n V$. Then $C' <= C''$, and
$C'' slash C'$ is called the *regular part*#idx(
  "regular",
  "part of relation",
)#idx("relations", "regular part") of the relation. The following proposition
asserts that the regular part of a relation splits off:

#source(125)

#proposition[
  If $C$ is a linear relation on $V$, then there are subspaces $U$ and $W$ of
  $V$ with $V = U plus.o W$, and
  $C = (C inter (U times U)) plus.o (C inter (W times W))$, with
  $C inter (U times U)$ the graph of an automorphism of $U$, and
  $C' plus.o U = C''$. The regular part of $C inter (W times W)$ is zero.
] <prop:regular-part-splits>

#proof[
  This follows from the classification.
]

Note in particular that $C$ induces an automorphism $phi.alt$ of $C'' slash C'$,
defined by
$ phi.alt(x + C') = (C x inter C'') + C'. $

#corollary(closed: true)[
  If $C$ is a linear relation on $V$, and $U$ is chosen as above, then
  $(C^(-1))' plus.o U = (C^(-1))''$.
] <cor:inverse-relation>

#subhead[Integral representations] The integral representations of the Klein
four group were first classified by L.~A. Nazarova [@bib:Nazarova1967]. We shall
follow the approach of M.~C.~R. Butler [@bib:Butler1974b]. In both these
approaches, the problem is reduced to the four subspace problem, which had
already been solved by Gel'fand and Ponomarev [@bib:Gelfand1972]. We shall give
an outline of this reduction here. For a list of the four subspace
configurations, see Brenner [@bib:Brenner1974].

Suppose $R$ is a principal ideal domain in which $2 != 0$ is prime (e.g.
$R = ZZ$), let $K$ be the field of fractions of $R$, a field of characteristic
zero, and $k = R slash (2)$, a field of characteristic two. Then we can make $R$
into an $R V_4$-module in four different ways, corresponding to the four
different choices of signs. We call these rank one modules $L_1$, $L_2$, $L_3$
and $L_4$, and we write $e_1, dots, e_4$ for the corresponding idempotents in
$K G$ (a typical one is $(1 + x - y - x y) slash 4$), so that
$e_i e_j = delta_(i j) e_j$ and $e_1 + dots.c + e_4 = 1$.

#definition[
  If $M$ is an $R$-torsion free $R G$-module, we say $M$ is *reduced* if it has
  no summands isomorphic to $L_1, dots, L_4$ or $R G$.
] <def:reduced-module>

If $M$ is a reduced $R G$-module, we define
$e_* M = e_1 M + dots.c + e_4 M subset.eq K M$. Since $e_1 + dots.c + e_4 = 1$,
we have $e_* M = M + e_i M + e_j M + e_k M$ for any
${i, j, k} subset.eq {1, 2, 3, 4}$. Thus letting
$ V = e_* M slash M, quad V_i = (e_i M + M) slash M subset.eq V $
we have a four subspace system $V$; $V_1, dots, V_4$ in which $V$ is the sum of
any three of the $V_i$.

#definition[
  A four subspace system $V$; $V_1, dots, V_4$ is *reduced* if $V$ is the sum of
  any three of the $V_i$.
] <def:reduced-four-subspace>

It turns out that all but five of the indecomposable four subspace systems are
reduced.

Conversely, given a reduced four subspace system $V$; $V_1, dots, V_4$, we form
a reduced $R V_4$-module as follows. Let $M_i$ be a direct sum of $dim(V_i)$
copies of $L_i$, so that $M_i slash 2 M_i tilde.equiv V_i$. Then we have a map
$M_1 plus.o dots.c plus.o M_4 -> V$ given by reduction modulo two followed by
inclusion, and we define $M$ to be the kernel of this map. It is easy to see
that this is a reduced $R V_4$-module.

#source(126)

#theorem[
  The above processes set up a one–one correspondence between the reduced
  $R$-torsion free $R V_4$-modules and the reduced four subspace systems. This
  correspondence preserves direct sums.
] <th:butler>

#proof[
  See Butler [@bib:Butler1974b].
]

#corollary(closed: true)[
  The Krull–Schmidt theorem holds for $R$-torsion free $R V_4$-lattices.
] <cor:krull-schmidt-klein-four>
