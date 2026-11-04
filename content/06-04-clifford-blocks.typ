#import "main-defs.typ": *
#import "statements.typ": *

== Clifford theory of blocks <sec:clifford-blocks>
#idx("block", "Clifford theory of", target: [@sec:clifford-blocks])#idx(
  "Clifford theory",
  "of blocks",
  target: [@sec:clifford-blocks],
)

In this section we examine the relationship between blocks and normal subgroups.
We use this to establish the extended version of Brauer's first main theorem,
and Brauer's third main theorem.

Let $N$ be a normal subgroup of $G$, $e$ a primitive central idempotent in
$k N$, and $b = e.k N$ the corresponding block of $k N$. For any $g in G$,
$g e g^(-1)$ is again a primitive central idempotent in $k N$, and is hence
either equal to or #source(221)orthogonal to $e$. We define the *inertia
group*#idx("inertia group") $T(b)$#idx("$T(b)$") to be the subgroup of $G$
consisting of those elements $g$ with $g e g^(-1) = e$. Thus
$ f = sum_(g in G slash T(b)) g e g^(-1) $
is a central idempotent in $k G$.

The identity element of $k G$ can be written as the sum of such elements $f$,
one for each conjugacy class in $k G$ of blocks of $k N$. Thus given any
primitive central idempotent $e'$ in $k G$ corresponding to a block
$B = e'.k G$, there exists a block $b$ of $k N$ as above, unique up to
conjugacy, such that $B$ is a summand of $f.k G$. This is equivalent to the
condition that $e' f = e'$, which in turn happens if and only if $e' f != 0$
since $e'$ is primitive. In the above situation, we say that the block $B$
*covers*#idx("block", "covering")#idx("covering", "block") the block $b$.
Clearly every block of $k N$ is covered by some block of $k G$.

#theorem[
  Suppose $B$ is a block of $k G$, and $N$ is a normal subgroup of $G$.
  + The blocks of $k N$ covered by $B$ form a single $G$-conjugacy class of
    blocks of $k N$.
  + Suppose $b = e.k N$ is a block of $k N$ covered by $B$. Then some defect
    group $D(B)$ is contained in the inertia group $T = T(b)$.
  + Let $f = sum_(g in G slash T) g e g^(-1)$ as above. Then we have
    $f.k G tilde.equiv Mat_n (e.k T)$ where $n = |G : T|$.
  + For some choice of $D(B)$ (but not necessarily for all choices of $D(B)$)
    the group $D(B) inter N$ is a defect group of $b$.
  + If $C_G (D(b)) <= N$ then $b^G = B$ and $B$ is the unique block covering
    $b$.
  Finally, if $k$ is algebraically closed and $B$ is the only block covering $b$
  then $|T : D(B) N|$ is not divisible by $p$.
] <th:clifford-blocks>

#proof[
  + This is clear from the definitions.
  + As a $k(N times N)$-module we have
    $k G = plus.o.big_(g in G slash N) g.k N$, and so letting $f$ be the
    idempotent $sum_(g in G slash T) g e g^(-1)$ as above, we have
    $
      #aligned-rows(
        (
          $f.k G$,
          $= plus.o.big_(g in G slash N) g(f.k N)
          = plus.o.big_(g in G slash N) plus.o.big_(h in G slash T)
          g(h e.k N.h^(-1))$,
        ),
        (
          $$,
          $= plus.o.big_((g_1, g_2) in \
          (G times G) slash (Delta(T).N times N))
          g_1 b g_2^(-1).$,
        ),
      )
    $
    The latter is just $b$ regarded as a $k(Delta(T).N times N)$-module induced
    up to $G times G$. It follows that as a $k(G times G)$-module, every block
    $B$ covering $b$ is projective relative to $Delta(T).N times N$. Thus for
    some defect group $D(B)$ we have $Delta(D(B)) <= Delta(T).N times N$. Since
    $N <= T$, it follows that $D(B) <= T$.
  + We have
    $
      f.k G = plus.o.big_((g_1, g_2) in (G times G) slash (T times T))
      g_1 (e.k T) g_2^(-1).
    $
    Similarly, $e.k G$ can be written as an $e.k T$-module in the form
    $ e.k G = plus.o.big_(g in G slash T) (e.k T) g^(-1) $
    #source(222)so that it is free of rank $n = |G : T|$ over $e.k T$. Thus we
    have
    $ End_(e.k T) (e.k G)^op tilde.equiv Mat_n (e.k T). $
    We have an algebra homomorphism $f.k G -> End_(e.k T) (e.k G)^op$ given by
    right multiplication. This is injective since if $(e y)(f x) = 0$ for all
    $y in k G$ then $f x = f.f x = sum_(g in G slash T) g e g^(-1).f x = 0$. It
    is surjective since the matrix entry corresponding to sending
    $(e.k T) g_1^(-1)$ to $(e.k T) g_2^(-1)$ with right multiplication by
    $x in e.k T$ is achieved by the element $g_1 x g_2^(-1) in f.k G$.
  + Since $B$ is a trivial source module with vertex $Delta(D(B))$, the
    restriction to $Delta(D(B))$ has the trivial module as a summand. Hence the
    restriction to $Delta(D(B)) inter (N times N)$ also has the trivial module
    as a summand, and so some summand of $B down_(N times N)$ has vertex
    containing $Delta(D(B)) inter (N times N)$. But the restriction of $B$ to
    $N times N$ is a sum of modules of the form $g_1 b g_2^(-1)$. The vertices
    of these modules are all $G times G$-conjugate to $Delta(D(b))$, and so some
    $G$-conjugate of $D(B) inter N$ is contained in $D(b)$. Since $b$ is a
    summand of $B down_(N times N)$, it is projective relative to some
    $G$-conjugate of $Delta(D(B) inter N)$, and so we have equality.
  + If $C_G (D(b)) <= N$, then by Lemma~@lem:alperin-brauer-correspondence $b^G$
    is the only block $B$ of $k G$ such that $b$ is a summand of
    $B down_(N times N)$, and is hence the only block covering $b$.

  Finally, suppose $k$ is algebraically closed and $B$ is the only block
  covering $b$, and let $S$ be a Sylow $p$-subgroup of $T$ containing $D(B)$. As
  in the proof of (ii), we regard $b$ as a module for $Delta(T)(N times N)$
  whose restriction to $N times N$ is indecomposable, and which induces up to
  $f.k G = B$. Hence $b down_(Delta(S)(N times N))$ is indecomposable and
  projective relative to $Delta(D(B))(N times N)$, so that by Green's
  Indecomposability Theorem~@th:green-indecomposability it is induced from a
  module for $Delta(D(B))(N times N)$. Since $b down_(Delta(D(B))(N times N))$
  is indecomposable the Mackey decomposition theorem implies that
  $Delta(D(B))(N times N) = Delta(S)(N times N)$, so that $D(B) N = S N$. This
  implies that $|T : D(B) N|$ is not divisible by $p$.
]

#lemma[
  Suppose $Q$ is a $p$-subgroup of $G$ and $G = Q C_G (Q)$. Then the natural map
  $pi : k G -> k G slash Q$ induces a one–one correspondence between blocks of
  $k G$ with defect group $D$ (which of course contain $Q$, for example by
  Proposition~@prop:defect-group-sylow-intersection) and blocks of $k G slash Q$
  with defect group $D slash Q$.
] <lem:central-p-subgroup-blocks>

#proof[
  By Proposition~@prop:normal-p-subgroup-idempotents, every idempotent in
  $Z(k G)$ lies in $k C_G (Q)$. Conversely $Z(k C_G (Q)) <= Z(k G)$ since
  $G = Q C_G (Q)$, and so the primitive idempotents in $Z(k G)$ are the same as
  the primitive idempotents in $Z(k C_G (Q))$.

  Now the map
  $ pi : k G -> k G slash Q tilde.equiv k C_G (Q) slash Z(Q) $
  maps $Z(k C_G (Q))$ onto a subalgebra of $Z(k C_G (Q) slash Z(Q))$ containing
  all its idempotents, and has as its kernel $J(k Q).C_G (Q)$, which is
  nilpotent. So by the idempotent refinement theorem it induces a one–one
  correspondence between idempotents in $Z(k C_G (Q))$ and in $Z(k G slash Q)$.
  Since $pi$ maps $(k G)_D^G$ into $(k G slash Q)_(D slash Q)^(G slash Q)$, and
  $Br_(D slash Q) (pi(e)) = pi(Br_D (e)) != 0$ for a block idempotent $e$ with
  defect group $D$, the statement about defect groups follows from
  Lemma~@lem:defect-group-brauer-map.#ed-note[The book claimed that $pi$ maps
    $Z(k C_G (Q))$ onto $Z(k C_G (Q) slash Z(Q))$ and $(k G)_D^G$ onto
    $(k G slash Q)_(D slash Q)^(G slash Q)$. Both fail for $p = 2$, $G = D_8$ or
    $Q_8$ and $Q = Z(G)$: the image of $Z(k G)$ is $k . 1$, while $k G slash Q$
    is commutative of dimension 4. The image contains all idempotents, since
    block idempotents are combinations of $p$-regular class sums; see Curtis and
    Reiner [@bib:Curtis1987], (56.37), and Thévenaz [@bib:Thevenaz1995],
    Proposition 39.2 and Corollary 39.3.]
]

#theorem(
  title: [Brauer's first main theorem, extended version],
  head-break: true,
)[
  #source(223)Suppose that $k$ is algebraically closed. Then there is a one–one
  correspondence between the following:
  + Blocks of $k G$ with defect group $D$.
  + Blocks of $k N_G (D)$ with defect group $D$.
  + $N_G (D)$-conjugacy classes of blocks $b$ of $k D C_G (D)$ with defect group
    $D$, such that $|T(b) : D C_G (D)|$ is not divisible by $p$.
  + $N_G (D)$-conjugacy classes of blocks $b$ of $k D C_G (D) slash D$ of defect
    zero, such that $|T(b) : D C_G (D)|$ is not divisible by $p$.

  The correspondence between #statement-comment[(i)], #statement-comment[(ii)]
  and #statement-comment[(iii)] is given by the Brauer map $b |-> b^G$, while
  the correspondence between #statement-comment[(iii)] and
  #statement-comment[(iv)] is given by the natural map
  $pi : k D C_G (D) -> k D C_G (D) slash D$.
] <th:brauer-first-main-extended>
#idx(
  "Brauer's",
  "first main theorem",
  "extended",
  target: [@th:brauer-first-main-extended],
)#idx(
  "extended first main theorem",
  target: [@th:brauer-first-main-extended],
)#idx(
  "theorem",
  "extended first main",
  target: [@th:brauer-first-main-extended],
)

#proof[
  The correspondence between (i) and (ii) was shown in
  Theorem~@th:brauer-first-main. The correspondence between (iii) and (iv) was
  shown in the above lemma (with $Q = D$). So it remains to discuss the
  correspondence between (ii) and (iii). We may thus assume that $D$ is normal
  in $G$. We apply Theorem~@th:clifford-blocks with $N = D C_G (D)$. This says
  that if $B$ is a block of $k G$ with defect group $D$ then the blocks of $k N$
  covered by $B$ also have $D$ as defect group and $p$ does not divide
  $|T(b) : D C_G (D)|$. Conversely if $b$ is a block of $D C_G (D)$ with defect
  group $D$ and $p$ does not divide $|T(b) : D C_G (D)|$ then $B = b^G$ is the
  unique block of $k G$ which covers $b$. Moreover the defect group $D(b^G)$ is
  a $p$-subgroup of $T(b)$ which intersects $D C_G (D)$ in exactly $D$, so that
  since $p$ does not divide $|T(b) : D C_G (D)|$, $D$ is a defect group of
  $b^G$.
]

It is worth making more explicit the structure of the blocks given in part (iii)
of the above theorem.

#proposition[
  Suppose $k$ is an algebraically closed field, and suppose $B$ is a block of
  $k G$ with normal defect group $D$ and $G = D C_G (D)$. Then
  $B tilde.equiv Mat_n (k D)$.
] <prop:normal-defect-matrix-ring>

#proof[
  Since $D$ acts trivially on simple $k G$-modules, and the block of defect zero
  of $k G slash D$ corresponding to $B$ as in the last theorem has only one
  simple module by Corollary~@cor:defect-zero, it follows that $B$ has only one
  simple module $S$. So to prove that $B tilde.equiv Mat_n (k D)$ it suffices to
  show that $B$ is Morita equivalent to $k D$.

  If $M$ is a $k D$-module then $M up^G$ is a $k G$-$k C_G (D)$-bimodule, with
  right $C_G (D)$-action given by $(g times.o m) x = g x times.o m$. So we have
  a functor $lmodule(k D, bold("mod")) -> lmodule(B, bold("mod"))$ given by
  $M |-> M up^G times.o_(k C_G (D)) S$. Similarly, we regard the dual $S^*$ of
  $S$ as a $k D$-$k G$-bimodule with trivial left action and we have a functor
  $lmodule(B, bold("mod")) -> lmodule(k D, bold("mod"))$ given by
  $N |-> S^* times.o_(k G) N$. Using the identity
  $S^* times.o_(k C_G (D)) S tilde.equiv Hom_(k C_G (D)) (S, S) tilde.equiv k$
  it is easy to see that these functors give an equivalence of categories.
]

#theorem(title: [Brauer's third main theorem])[
  Suppose $H$ is a subgroup of $G$ with $D C_G (D) <= H$, and $b$ is a block of
  $k H$ with defect group $D$. Then $b^G$ is the principal block $B_0 (k G)$ if
  and only if $b$ is the principal block $B_0 (k H)$.
] <th:brauer-third-main>
#idx(
  "Brauer's",
  "third main theorem",
  target: [@th:brauer-third-main],
)#idx("theorem", "Brauer's", "third main", target: [@th:brauer-third-main])#idx(
  "third main theorem",
  target: [@th:brauer-third-main],
)

#proof[
  #source(224)If we apply Nagao's Theorem~@th:nagao to the trivial module, we
  find that if $b = B_0 (k H)$ then $b^G = B_0 (k G)$. Conversely, suppose
  $b^G = B_0 (k G)$. We may suppose $H <= N_G (D)$, since applying this case
  twice gives the general case. Let $D'$ be a defect group of $b^(N_G (D))$.
  Then $D <= D' <= N_G (D)$ so that $C_G (D') <= C_G (D) <= N_G (D)$ and hence
  $D' C_G (D') <= N_G (D)$. By the extended first main theorem there is a unique
  $N_G (D')$-conjugacy class of blocks $b'$ of $k D' C_G (D')$ with
  $(b')^G = B_0 (k G)$. Since $B_0 (k D' C_G (D'))$ is such a block and is
  stable under $N_G (D')$-conjugation, this is the unique such block. But there
  is also a block $b'$ of $k D' C_G (D')$ with $(b')^(N_G (D)) = b^(N_G (D))$.
  For such a block we also have $(b')^G = B_0 (k G)$ and hence
  $b' = B_0 (k D' C_G (D'))$. Now by the first part of the proof we have
  $b^(N_G (D)) = B_0 (k N_G (D))$. So we may assume that $D$ is normal in $G$.

  We now apply Theorem~@th:clifford-blocks with $N = D C_G (D)$. Let $b'$ be a
  block of $k N$ covered by $b$. By part (iv) of this theorem $D$ is a defect
  group of $b'$. Since $C_G (D) <= N$, by part (v) we have $(b')^H = b$ and so
  $(b')^G = B_0 (k G)$. But also $B_0 (k N)^G = B_0 (k G)$, so that since
  $B_0 (k N)$ is stable under $G$-conjugation we have $b' = B_0 (k N)$ and hence
  $b = (b')^H = B_0 (k H)$.
]
