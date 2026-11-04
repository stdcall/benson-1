#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/06-05-cyclic-defect.typ": cartan-overlap

== Blocks of cyclic defect <sec:cyclic-defect>

The situation of a block whose defect groups are cyclic#idx(
  "block",
  "of cyclic defect",
)#idx("cyclic", "defect")#idx("defect", "cyclic") is one which is very well
understood. The case of a cyclic defect group of order $p$ was originally
described by Brauer. Using ideas of Green and Thompson, the general case was
analysed by Dade. We shall only describe that part of the theory which has to do
with the modular representations. We shall not describe the ordinary characters
or decomposition numbers.

Suppose $B$ is a block of $k G$ whose defect group $D$ is cyclic of order $p^n$.
By Proposition~@prop:defect-group-transfer every indecomposable module in $B$
has vertex contained in $D$. Since a cyclic group has only finitely many
indecomposable modules, there are only finitely many sources and hence only
finitely many indecomposables in $B$. Thus $B$ has finite representation type.

Let $Q$ be the unique subgroup of $D$ of order $p$, so that
$N_G (Q) >= N_G (D)$. By Brauer's first main theorem, there is a unique block
$b$ of $N_G (Q)$ with $b^G = B$. By Theorem~@th:clifford-blocks, there is a
unique $N_G (Q)$-conjugacy class of blocks $b_1$ of $C_G (Q)$ (note that
$Q <= C_G (Q)$) with $b_1^(N_G (Q)) = b$ (so that $b_1^G = B$). Let
$T = T(b_1) <= N_G (Q)$ be the inertia group of $b_1$, and set
$e = |T : C_G (Q)|$, the *inertial index*#idx("inertial index")#idx(
  "index, inertial",
) of $B$ (this is not the usual definition, but it is equivalent and more
suitable for our purposes). We shall not use the letter $e$ to stand for an
idempotent during this section, so there should be no notational confusion. Note
that $e$ divides $|N_G (Q) : C_G (Q)|$, which in turn divides $p - 1$ since
$N_G (Q) slash C_G (Q)$ is isomorphic to a group of automorphisms of $Q$.

We next analyse the Green correspondence#idx("correspondence", "Green")#idx(
  "Green",
  "correspondence",
) between modules for $G$ and $N_G (Q)$.

#source(225)

#lemma[
  Green correspondence between $G$ and $N_G (Q)$ sets up a one–one
  correspondence between non-projective modules in $B$ and non-projective
  modules in $b$, in such a way that
  $
    #aligned-rows(
      (
        $M down_(N_G (Q))$,
        $= f(M) plus.o ("projective") plus.o ("modules not in" b)$,
      ),
      ($M' up^G$, $= g(M') plus.o ("projective").$),
    )
  $
  If $M_1$ and $M_2$ are modules in $B$ then
  $ (M_1, M_2)^(G, 1) tilde.equiv (f(M_1), f(M_2))^(N_G (Q), 1). $
  (see Definition~@def:transfer for the notation).
] <lem:cyclic-green-correspondence>

#proof[
  By Proposition~@prop:defect-group-transfer every non-projective module in $B$
  has vertex $D'$ with $1 < D' <= D$. Since $Q$ is a characteristic subgroup of
  $D'$ this means that $N_G (D') <= N_G (Q)$ and so we may apply Green
  correspondence. By Nagao's theorem a module with vertex $D'$ lies in $B$ if
  and only if its Green correspondent lies in $b$.

  The lemma now follows from Theorem~@th:green-correspondence once we have
  evaluated the sets of subgroups $cal(X)$ and $cal(Y)$. Since $Q$ is the unique
  minimal subgroup of $D$, if $x in.not N_G (Q)$ then we have
  $lconj(x, D) inter D = 1$, and so $cal(X) = {1}$. Similarly $cal(Y)$ consists
  of subgroups of $N_G (Q)$ not containing $Q$, so that any non-projective
  indecomposable $k N_G (Q)$-module with vertex in $cal(Y)$ does not lie in $b$
  by Proposition~@prop:defect-group-transfer.
]

We shall also need the following lemma.

#lemma[
  Suppose $Lambda$ is a finite dimensional algebra with the property that every
  projective indecomposable $Lambda$-module and every injective indecomposable
  $Lambda$-module is uniserial. Then every indecomposable $Lambda$-module is
  uniserial, and in particular is a quotient of a projective indecomposable.
] <lem:uniserial-indecomposables>

#proof[
  Suppose $M$ is indecomposable and $S$ is a simple submodule of $M$. Let $M'$
  be a submodule of $M$ which is maximal subject to the condition
  $S inter M' = 0$. Then $M slash M'$ has $S$ as its socle since otherwise we
  could enlarge $M'$. So the injective hull of $M slash M'$ is the injective
  hull of $S$ and hence uniserial, and so $M slash M'$ is uniserial. So the
  projective cover $P$ of $M slash M'$ is also uniserial. The map
  $P -> M slash M'$ lifts to a map $P -> M$ whose image $M''$ is a uniserial
  submodule of $M$ containing $S$ and hence intersects $M'$ trivially. Thus
  $M = M' plus.o M''$, and since $M'' != 0$ we have $M' = 0$.
]

We now analyse blocks of cyclic defect with inertial index one. This is an easy
case to understand, and acts as a model for the arguments in the general case.

#proposition[
  Suppose $B$ is a block of $k G$ with cyclic defect group $D$ of order $p^n$
  and with inertial index one. Then there is only one simple module $S$ in $B$,
  and the projective cover of $S$ is uniserial of length $p^n$.
] <prop:cyclic-inertial-index-one>

#source(226)

#proof[
  We first prove that if $B$ has only one simple module $S$ then the projective
  cover of $S$ is uniserial. For this purpose we use the fact that $B$ has
  finite representation type.

  Denote by $P_S$ the projective cover of $S$. We have
  $Rad(P_S) slash Rad^2(P_S) != 0$, since otherwise $S$ is projective so that by
  Corollary~@cor:defect-zero $S$ lies in a block of defect zero. If
  $Rad(P_S) slash Rad^2(P_S)$ is a sum of at least two copies of $S$ then $P_S$
  has a quotient $M$ with $Rad(M) tilde.equiv S plus.o S$ and
  $M slash Rad(M) tilde.equiv S$. Thus the basic algebra $End_(k G) (P_S)^op$ of
  $B$ has as a quotient the algebra $End(M)^op$. Setting
  $Delta = End_(k G) (S)^op$ we have
  $End_(k G) (M)^op tilde.equiv Delta[X, Y] slash (X^2, X Y, Y^2)$. This algebra
  has infinitely many non-isomorphic indecomposable modules. This may be seen as
  follows. The algebra $Delta[X, Y] slash (X^2, Y^2)$ is a self-injective
  algebra of dimension four over $Delta$, and the modules $Omega^n k$ are all
  non-isomorphic indecomposables on which $X Y$ acts as zero. Since $B$ has only
  finitely many indecomposables, we deduce that
  $Rad(P_S) slash Rad^2(P_S) tilde.equiv S$. It follows that $P_S$ is uniserial,
  since by induction on $i$, if $Rad^i (P_S) slash Rad^(i+1)(P_S) tilde.equiv S$
  then $Rad^i (P_S) slash Rad^(i+2)(P_S)$ is a quotient of
  $P_S slash Rad^2(P_S)$ and so we have either $Rad^(i+1)(P_S) = 0$ or
  $Rad^(i+1)(P_S) slash Rad^(i+2)(P_S) tilde.equiv S$.

  We now prove the proposition by induction on the order of $G$, and we begin
  with the case where the subgroup $Q$ of order $p$ in $D$ is central in $G$
  (note that the case $D = 1$ was dealt with in Corollary~@cor:defect-zero).
  Applying Lemma~@lem:central-p-subgroup-blocks, we see that the natural map
  $pi : k G -> k G slash Q$ induces a one–one correspondence between blocks of
  $k G$ with defect group $D$ and blocks of $k G slash Q$ with defect group
  $D slash Q$. If $macron(B)$ is the block of $k G slash Q$ corresponding to $B$
  then the inertial index of $macron(B)$ is again one, and since $G slash Q$ is
  smaller than $G$ the inductive hypothesis shows that $macron(B)$ has only one
  simple module $S$. Since $Q$ acts trivially on simple $B$-modules, $B$ also
  has only one simple module, namely $S$ again. Now if $g$ is a generator of $Q$
  then as a $k G$-module we have
  $ (g - 1)^j k G slash (g - 1)^(j+1) k G tilde.equiv k G slash Q $
  for $j = 0, 1, dots, p - 1$, and $(g - 1)^p = 0$. Thus
  $(g - 1)^j B slash (g - 1)^(j+1) B tilde.equiv macron(B)$ and so the length of
  the projective cover of $S$ as a $B$-module is $p$ times what it is as a
  $macron(B)$-module. This completes the proof in case $Q <= Z(G)$.

  Next, we treat the case where $Q$ is normal but not central. In this case we
  apply Theorem~@th:clifford-blocks to the normal subgroup $C_G (Q)$, which is
  equal to $T$ since $e = 1$. We see that if $b_1$ is a block of $k C_G (Q)$
  covered by $B$ then $B tilde.equiv Mat_m (b_1)$, where $m = |G : T|$. Thus $B$
  is Morita equivalent to $b_1$ and the result follows in this case.

  Finally, if $Q$ is not normal in $G$ then we apply Green correspondence
  between $G$ and $N_G (Q)$, as in the Lemma~@lem:cyclic-green-correspondence.
  If $B$ has more than one simple module, say $S$ and $S'$ are simple
  $B$-modules, then the Green correspondents $f(S)$ and $f(S')$ are uniserial
  modules for $N_G (Q)$, and so one is a quotient of the other, say $f(S')$ is a
  quotient of $f(S)$. Now it follows from
  Proposition~@prop:transfer-image-factors that a homomorphism from one module
  to another lies in the image of $Tr_(1, G)$ if and only if it factors through
  the projective cover of the second module. Since $f(S)$ is not projective, the
  surjection $f(S) -> f(S')$ does not #source(227)lie in
  $(f(S), f(S'))_1^(N_G (Q))$. Hence we have $(f(S), f(S'))^(N_G (Q), 1) != 0$
  so that by Lemma~@lem:cyclic-green-correspondence $(S, S')^(G, 1) != 0$. Since
  $S$ and $S'$ are distinct simple modules this is absurd, and so $B$ has only
  one simple module. Since the length of the projective cover of this simple
  module is one more than the number of non-projective indecomposables in $B$,
  it also follows from the Green correspondence that this is the same as the
  length for the corresponding block of $N_G (Q)$.
]

The next easiest case to consider is the one in which $Q$ is normal in $G$. To
avoid complications we assume that $k$ is algebraically closed.

#proposition[
  Suppose $k$ is algebraically closed, and $B$ is a block of $k G$ with cyclic
  defect group $D$ of order $p^n$ and inertial index $e$. Suppose further that
  the subgroup $Q$ of $D$ of order $p$ is normal in $G$. Then there are $e$
  simple modules in $B$, all of the same dimension over $k$. These simple
  modules may be labelled $S_1, dots, S_e$ in such a way that the projective
  cover $P_j$ of $S_j$ is uniserial of length $p^n$ with
  $Rad^i (P_j) slash Rad^(i+1)(P_j) tilde.equiv S_(i+j)$, with the subscripts
  being taken modulo $e$.

  $B$ is Morita equivalent to the group algebra of a split extension with normal
  subgroup $D$ and complement cyclic of order $e$ acting faithfully on $D$.
] <prop:cyclic-defect-normal>

#proof[
  Let $b_1$ be a block of $C_G (Q)$ covered by $B$, and let $T = T(b_1)$ be the
  inertia group. Then by Theorem~@th:clifford-blocks $B$ is isomorphic to a
  complete matrix algebra over $b_1^T$. It thus suffices to prove the
  proposition with $G = T$. We may apply the last proposition to $b_1$ to see
  that it has a unique simple module $S$, and its projective cover is uniserial
  of length $p^n$.

  We first claim that $S$ extends to a simple $k G$-module in exactly $e$ ways,
  and that these are all the simple modules in $B$ (note that this is not true
  unless $G = T$). Since $b_1$ is stable under conjugation by $G$, so is the
  simple module $S$. Thus if $g in G$ generates the cyclic group
  $G slash C_G (Q)$ we have $g times.o S tilde.equiv S$. Let $theta$ be an
  element of $End_k (S)$ such that $g times.o s |-> theta(s)$ is such a
  $k C_G (Q)$-module isomorphism. In other words,
  $theta(g^(-1) h g(s)) = h(theta(s))$ for $h in C_G (Q)$. Then
  $g^j times.o s |-> theta^j (s)$ gives an isomorphism
  $g^j times.o S tilde.equiv S$. Since $g^e in C_G (Q)$,
  $g^e (s) |-> theta^e (s)$ is a $k C_G (Q)$-module endomorphism of $S$. Since
  $k$ is algebraically closed, it follows that for some $mu in k$ we have
  $g^e (s) = mu theta^e (s)$. Since $e$ is coprime to $p$, there are exactly $e$
  distinct choices for an element $lambda in k$ with $lambda^e = mu$. For each
  such choice, we may extend $S$ to a simple $k G$-module by letting $g$ act as
  the endomorphism $lambda theta$. Distinct choices of $lambda$ give
  non-isomorphic extensions of $S$ to a $k G$-module, since an isomorphism
  between two such extensions restricts to give an isomorphism on $C_G (Q)$,
  which may therefore be taken to be the identity map.

  If we let $S_1, dots, S_e$ be the extensions of $S$ to $k G$-modules, then
  $ Hom_(k G) (S_j, S up^G) tilde.equiv Hom_(k C_G (Q)) (S, S) tilde.equiv k $
  #source(228)and so by counting dimensions we have
  $S up^G = S_1 plus.o dots.c plus.o S_e$. Now if $M$ is any simple $k G$-module
  then
  $
    Hom_(k G) (M, S up^G) tilde.equiv Hom_(k C_G (Q)) (M down_(C_G (Q)), S)
    != 0
  $
  and so $M$ must be one of the $S_j$.

  Now by the Eckmann–Shapiro lemma
  $
    Ext_(k G)^1 (S_j, S_1 plus.o dots.c plus.o S_e) tilde.equiv
    Ext_(k C_G (Q))^1 (S, S) tilde.equiv k
  $
  so that there is a unique value of $i$ for which
  $Ext_(k G)^1 (S_j, S_i) tilde.equiv k$, and for the remaining values of $i$ we
  have $Ext_(k G)^1 (S_j, S_i) = 0$. Since $B$ is a block, all simple modules
  are connected by some chain of extensions, and it follows that we may label
  the simple modules in such a way that
  $Ext_(k G)^1 (S_j, S_(j+1)) tilde.equiv k$, where $j$ is taken modulo $e$.
  Thus if we denote by $P_j$ the projective cover of $S_j$ we have
  $Rad(P_j) slash Rad^2(P_j) tilde.equiv S_(j+1)$. It follows that $P_j$ is
  uniserial with either $Rad^i (P_j) slash Rad^(i+1)(P_j) tilde.equiv S_(i+j)$
  or $Rad^i (P_j) = 0$, since by induction on $i$, if
  $Rad^i (P_j) slash Rad^(i+1)(P_j) tilde.equiv S_(i+j)$ then
  $Rad^i (P_j) slash Rad^(i+2)(P_j)$ is a quotient of
  $P_(i+j) slash Rad^2(P_(i+j))$ and so either $Rad^(i+1)(P_j) = 0$ or
  $Rad^(i+1)(P_j) slash Rad^(i+2)(P_j) tilde.equiv S_(i+j+1)$. The restriction
  of $P_j$ to $C_G (Q)$ is some multiple of $P_S$; this multiple has to be one
  since $P_S up^G$ is projective and hence equal to the sum of the $P_j$. Thus
  the length of $P_j$ is the same as the length of $P_S$, namely $p^n$.

  Finally, to see that $B$ is Morita equivalent to the group algebra of a split
  extension of $D$ by $ZZ slash e$, we notice that the Ext-quiver is an oriented
  cycle of length $e$ with relations saying that any composite of $p^n$
  successive arrows is zero, so this determines the basic algebra by the method
  of Section~@sec:quivers. Since the group algebra of the split extension is a
  block of the type being considered, it has the same Morita type.
]

#theorem[
  Suppose $k$ is algebraically closed, and $B$ is a block of $k G$ with cyclic
  defect group $D$ of order $p^n$ and inertial index $e$. Then there are $e$
  simple modules and $e . p^n$ indecomposable modules in $B$. The stable
  Auslander–Reiten quiver of $B$ is a finite tube $(ZZ slash e) A_(p^n - 1)$.
  The algebra $B$ is a Brauer tree algebra (see
  Section~@sec:brauer-graph-algebras) for a Brauer tree with $e$ edges and
  exceptional multiplicity $(p^n - 1) slash e$.
] <th:cyclic-defect-quiver>

#proof[
  Let $Q$ be the subgroup of $D$ of order $p$, and let $b$ be the Brauer
  correspondent of $B$ in $N_G (Q)$. Then by the previous proposition there are
  $e$ simple modules in $b$, and their projective covers are uniserial of length
  $p^n$. Thus every indecomposable in $b$ is uniserial and a quotient of a
  projective indecomposable. Each projective indecomposable has $p^n - 1$
  non-projective quotients, and so $b$ has $e(p^n - 1)$ non-projective
  indecomposables. It now follows from the Green correspondence
  (Lemma~@lem:cyclic-green-correspondence) that $B$ also has $e(p^n - 1)$
  non-projective indecomposables. So we must show that $B$ has $e$ simple
  modules, and hence also $e$ projective indecomposables.

  We first claim that if $S$ and $S'$ are simple $B$-modules then the Green
  correspondents $f(S)$ and $f(S')$ have non-isomorphic heads. For otherwise,
  since they are uniserial modules, one is a quotient of the other, and just as
  #source(229)in the proof of Proposition~@prop:cyclic-inertial-index-one this
  implies that $0 != (f(S), f(S'))^(N_G (Q), 1) tilde.equiv (S, S')^(G, 1)$
  which is absurd. Thus there are at most $e$ simple modules in $B$.

  Conversely if $S_0$ and $S'_0$ are simple modules in $b$, we claim that the
  same simple $B$-module $S$ cannot appear in the top radical layer of the Green
  correspondents $g(S_0)$ and $g(S'_0)$. For if $S$ appears in
  $g(S_0) slash Rad g(S_0)$ then
  $0 != (g(S_0), S)^(G, 1) tilde.equiv (S_0, f(S))^(N_G (Q), 1)$ so that $S_0$
  is a submodule of $f(S)$, and similarly $S'_0$ is also a submodule of $f(S)$
  and so $S_0 tilde.equiv S'_0$. So there are at least $e$ simple modules in
  $B$.

  It follows from Lemma~@lem:cyclic-green-correspondence,
  Corollary~@cor:nagao-green-correspondent and
  Theorem~@th:almost-split-green-correspondence that the induction to $G$ of an
  almost split sequence of modules in $b$ is a sum of an almost split sequence
  of modules in $B$ and a split sequence of projective modules. Thus the stable
  Auslander–Reiten quiver of $B$ is isomorphic to that for $b$. It is easy to
  see from the structure of the projective modules in $b$ given in the previous
  proposition that the irreducible maps between modules in $b$ are the
  injections and surjections with simple kernels and cokernels, so that the
  stable Auslander–Reiten quiver of $b$, and hence also for $B$, is a tube of
  type $(ZZ slash e) A_(p^n - 1)$. In particular there are at most $2 e$ almost
  split sequences in $B$ with the property that the middle term has only one
  non-projective summand. Thus we may apply Theorem~@th:brauer-graph-algebra to
  deduce that $B$ is a Brauer graph algebra. Since $B$ has finite representation
  type, we may then apply Proposition~@prop:brauer-tree-finite-type to deduce
  that $B$ is a Brauer tree algebra. The number of edges in the tree is equal to
  the number of isomorphism classes of simple modules, namely $e$. Following
  Alperin [@bib:Alperin1986], the multiplicity of the exceptional vertex may be
  determined by looking at the determinant of the Cartan matrix as follows. It
  follows from Lemma~@lem:cyclic-green-correspondence that Green correspondence
  gives an isomorphism between the cokernels of the Cartan homomorphisms for $b$
  and for $B$ (cf. Corollary~@cor:cartan-homomorphism and
  Theorem~@th:cartan-determinant). So the determinant of the Cartan matrix of
  $B$ is equal to that of $b$, namely $det(I + ((p^n - 1) slash e) J) = p^n$,
  where $I$ is an $e times e$ identity matrix and $J$ is a matrix of the same
  size with all entries equal to one. We claim that for a Brauer tree with $e$
  edges and exceptional multiplicity $m$ the determinant of the Cartan matrix is
  $e m + 1$, which gives the value of $m$ as $(p^n - 1) slash e$ as required. We
  prove this by induction on $e$. We first treat the case in which the tree is a
  star; in other words there is at most one vertex of valency greater than one.
  If the exceptional vertex is the one with valency greater than one, then as
  above the determinant is $det(I + m J) = e m + 1$, while if the exceptional
  vertex has valency one then the determinant is
  $
    det mat(m + 1, 1, dots.c, 1; 1, 2, , 1; dots.v, , , dots.v; 1, 1, dots.c, 2)
    = e m + 1.
  $
  Finally, if the tree is not a star then there exists an edge $E$ such that
  neither of the vertices at its ends has valency one. Denote by $L$ and $R$ the
  trees to the left and right of $E$, intersecting in exactly $E$, and with
  union the whole #source(230)tree. Denote by $L_0$ and $R_0$ the trees obtained
  from $L$ and $R$ by removing the edge $E$. We choose the labelling so that the
  exceptional vertex, if there is one, lies in $L_0$. Denote by $l$ and $r$ the
  numbers of edges in $L$ and $R$, so that $l + r = e + 1$. The Cartan matrix
  has the form
  $ C = #cartan-overlap $
  with a single entry $z$ in the overlap, equal to either $m + 1$ or $2$,
  depending on whether the exceptional vertex is the left-hand vertex of $E$ or
  not. Denote by $X_0$ and $Y_0$ the submatrices of $X$ and $Y$ obtained by
  removing the row and column containing the overlap. Then $X$, $Y$, $X_0$ and
  $Y_0$ are the Cartan matrices of $L$, $R$, $L_0$ and $R_0$. By the inductive
  hypothesis we know the determinants of $X$, $Y$, $X_0$ and $Y_0$.

  Expanding $det(C)$ about the row containing the overlap, we see that
  $
    det(C) = det(X) det(Y_0) + det(X_0) det(Y) - z . det(X_0) det(Y_0).
  $
  If $z = 2$ this equals
  $
    (l m + 1) r + ((l - 1) m + 1)(r + 1) - 2((l - 1) m + 1) r = e m + 1,
  $
  while if $z = m + 1$ it equals
  $
    (l m + 1) r + ((l - 1) m + 1)(r m + 1) - (m + 1)((l - 1) m + 1) r
    = e m + 1.
  $
  This completes the calculation of the determinant of $C$.
]
