#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/05-09-psi-operations.typ": brauer-lift-square

== Psi operations <sec:psi-operations>

In this section we construct *psi operations*#idx("psi operations")#idx(
  "operations",
  "psi",
) $psi^n : a(k G) -> a(k G)$. These are the representation theoretic version of
raising group elements to the $n$th power, in the sense that the effect on
Brauer characters is given by $t_g (psi^n (x)) = t_(g^n) (x)$. They were first
introduced in characteristic zero by Frobenius, who used them to study the
number of solutions of $x^n = 1$ in a group. As an application of these
operations, we give Kervaire's proof [@bib:Kervaire1976] that the determinant of
the Cartan matrix is a power of $p$. In Chapter 2 of Volume II we shall study
the analogous operations in topological K-theory, and explain how these are
related to the cohomology of the finite general linear groups.

We first construct the operations $psi^n$ in the case where $n$ is coprime to
$p$. Let $k$ be a field of characteristic $p$ and let $k[epsilon]$ be the field
obtained from $k$ by adjoining a primitive $n$th root of unity $epsilon$ to $k$.
Let
$ T = chevron.l t | t^n = 1 chevron.r $
be a cyclic group#idx("cyclic", "group")#idx("group", "cyclic") of order $n$. If
$M$ is a $k G$-module then $M^(times.o n)$ is a $k(T times G)$-module with $T$
permuting the tensor multiplicands (this is just the tensor induced module#idx(
  "tensor",
  "induction",
) $M tensorup^(T times G)$). Since $n$ is coprime to $p$, after tensoring with
$k[epsilon]$, this breaks up as a direct sum of eigenspaces on which $t$ acts
with eigenvalues #source(206)$epsilon^j$. Each eigenspace is a
$k[epsilon]G$-module, and whenever
$chevron.l t^j chevron.r = chevron.l t^(j') chevron.r$ the $epsilon^j$
eigenspace is isomorphic to the $epsilon^(j')$ eigenspace. By considering the
action of the Galois group $Gal(k[epsilon] slash k)$, it follows that these
eigenspaces are defined over $k$. We write
$[M^(times.o n)]_(epsilon^j) = [M^(times.o n)]_d$ for the eigenspace
corresponding to a primitive $d$th root of unity $epsilon^j$ with $d divides n$,
considered as a $k G$-module. We define
$
  psi^n (M) = sum_(j=1)^n e^(2 pi i j slash n) [M^(times.o n)]_(epsilon^j)
  in A(G).
$
Now $sum_(1 lt.eq j lt.eq d \ (j, d) = 1) e^(2 pi i j slash d)$ is equal to the
Möbius function#idx("Möbius function") $mu(d)$#idx("$mu(d)$"), which takes
values 0 or $plus.minus 1$. It follows that
$ psi^n (M) = sum_(d divides n) mu(d) [M^(times.o n)]_d $
is an element of $a(G)$.

We define $psi^(p^a)$ to be the Frobenius map $F^a$ defined in
Proposition~@prop:frobenius-field-of-definition. Then for a general value of
$n = p^a.h$ with $p divides.not h$, we define $psi^n = psi^(p^a) compose psi^h$.

#proposition[
  If $M_1$ and $M_2$ are $k G$-modules then
  + $psi^n (M_1 plus.o M_2) = psi^n (M_1) + psi^n (M_2)$.
  + $psi^n (M_1 times.o M_2) = psi^n (M_1) psi^n (M_2)$.
  + $psi^m compose psi^n = psi^(m n)$.
] <prop:psi-ring-homomorphism>

#proof[
  + As $k G$-modules, we have
    $
      (M_1 plus.o M_2)^(times.o n) =
      plus.o.big_(j_1 = 1, 2, \ dots.c \ j_n = 1, 2)
      (M_(j_1) times.o dots.c times.o M_(j_n)).
    $
    Under the action of $T$, there are two fixed summands, namely
    $M_1^(times.o n)$ and $M_2^(times.o n)$. Apart from these, each orbit forms
    a $k(T times G)$-module induced from a proper subgroup of the form
    $T' times G$. It is easy to check that for such a module, the sum of
    $e^(2 pi i j slash n)$ times the $epsilon^j$ eigenspace is zero.
  + $(M_1 times.o M_2)^(times.o n) tilde.equiv M_1^(times.o n) times.o
    M_2^(times.o n)$, and so
    $
      [(M_1 times.o M_2)^(times.o n)]_(epsilon^j) tilde.equiv
      plus.o.big_(m=1)^n [M_1^(times.o n)]_(epsilon^m)
      [M_2^(times.o n)]_(epsilon^(j-m)).
    $
    Thus we have
    $
      psi^n (M_1 times.o M_2) & = sum_(j=1)^n e^(2 pi i j slash n)
                                [(M_1 times.o M_2)^(times.o n)]_(epsilon^j) \
                              & = sum_(j, m=1)^n e^(2 pi i m slash n)
                                [M_1^(times.o n)]_(epsilon^m)
                                e^(2 pi i (j - m) slash n)
                                [M_2^(times.o n)]_(epsilon^(j-m)) \
                              & = psi^n (M_1) psi^n (M_2).
    $
  + The proof can be found in [@bib:Benson1984a].
]

It follows from this proposition that we may extend $psi^n$ linearly to give a
ring homomorphism
$ psi^n : a(G) -> a(G). $
#source(207)Note that since $psi^n$ is given in terms of direct summands of
tensor powers, the image of $a(G, H)$ is contained in $a(G, H)$, and the image
of $a(G, Triv)$ is contained in $a(G, Triv)$.

#proposition[
  Let $t_g$ be the ring homomorphism $a(G) slash a_0 (G, 1) -> CC$ defined in
  Section~@sec:brauer-characters. Then
  $ t_g (psi^n (x)) = t_(g^n) (x). $
] <prop:psi-brauer-character>

#proof[
  Suppose $M$ is a $k G$-module, and suppose without loss of generality that $k$
  is algebraically closed. Then we may choose a basis $m_1, dots, m_r$ of $M$
  consisting of eigenvectors of $g$. Let $g m_j = lambda_j m_j$. Then
  $
    t_g (psi^n (M)) & = t_g (res_(G, chevron.l g chevron.r) psi^n (M))
                      = t_g (psi^n (M down_(chevron.l g chevron.r)))
                      = t_g (psi^n (plus.o.big_(j=1)^r
                          chevron.l m_j chevron.r)) \
                    & = sum_(j=1)^r t_g psi^n (chevron.l m_j chevron.r)
                      = sum_(j=1)^r lambda_j^n = t_(g^n) (M).
  $
]

#theorem(title: [Brauer])[
  Suppose $k$ is a field of characteristic $p$. Then the determinant of the
  Cartan matrix is a power of $p$.
] <th:cartan-determinant>

#proof[
  (Kervaire; for another proof see Corollary~@cor:cartan-determinant). This is
  the same as saying that the cokernel of the Cartan homomorphism
  $ c : a(G, 1) -> a(G) -> a(G) slash a_0 (G, 1) = cal(R)(G) $
  is a $p$-group.

  Let $m$ be the $p'$-part of the exponent of $G$. If $x in a(G, 1)$ then
  $psi^m (x)$ is again an element of $a(G, 1)$. By
  Proposition~@prop:psi-brauer-character, each $t_g$ has value
  $ t_g (psi^m (x)) = t_1 (x) $
  equal to the "dimension" of $x$. Thus by
  Proposition~@prop:brauer-composition-factors, if $P$ is a projective
  $k G$-module then $(dim_k P).1$ is in the image of $c$.

  For each prime $q != p$ dividing $|G|$, let $Q$ be a Sylow $q$-subgroup of
  $G$. Then $k_Q up^G$ is a projective $k G$-module since it is induced from a
  projective $k Q$-module. Thus by the above, $|G : Q|.1 in Im(c)$. It now
  follows from the Chinese remainder theorem that $|G|_p.1 in Im(c)$, where
  $|G|_p$ is the $p$-part of the order of $G$. Since $Im(c)$ is an ideal, it
  follows that $|G|_p$ annihilates the cokernel of $c$, and the theorem is
  proved.
]

Finally, we show how Corollary~@cor:decomposition-surjective leads to an
explicit description of $cal(R)(k G)$ in case $k$ is a field of $p^n$ elements,
in terms of the operation $psi^(p^n)$.

#proposition(title: [The Brauer Lift])[
  Let $(K, cal(O), k)$ be a $p$-modular system. Then for every $n$ the
  decomposition map
  $ d : cal(R)(K G) -> cal(R)(k G) $
  induces an isomorphism
  $
    cal(R)(K G)^(psi^(p^n)) tilde.equiv cal(R)(k G)^(psi^(p^n))
    = cal(R)(k_0 G)
  $
  #source(208)where $k_0 = {lambda in k | lambda^(p^n) = lambda}$.
] <prop:brauer-lift>
#idx("Brauer", "lift", target: [@prop:brauer-lift])#idx(
  "lift, Brauer",
  target: [@prop:brauer-lift],
)

#proof[
  By Theorem~@th:brauer-character-homomorphisms we have a diagram
  $ #brauer-lift-square $
  so that by Proposition~@prop:psi-brauer-character, $d$ commutes with the
  action of the $psi$ operations. It also follows from
  Proposition~@prop:psi-brauer-character that for $m$ large enough, $psi^(p^m)$
  kills the kernel of $d$. Suppose $x in cal(R)(k G)$ is fixed by $psi^(p^n)$.
  Choose $m$ as above to be a multiple of $n$. By
  Corollary~@cor:decomposition-surjective, $x$ has a pre-image $y$ in
  $cal(R)(K G)$. Since $psi^(p^n) (y) - y$ is killed by $d$, it is killed by
  $psi^(p^m)$, and so $psi^(p^(m+n)) (y) = psi^(p^m) (y)$ is a pre-image of $x$
  which is fixed by $psi^(p^n)$. Thus
  $d : cal(R)(K G)^(psi^(p^n)) -> cal(R)(k G)^(psi^(p^n))$ is an isomorphism.

  Finally, by Proposition~@prop:frobenius-field-of-definition we have
  $cal(R)(k G)^(psi^(p^n)) = cal(R)(k_0 G)$.
]

The way the above proposition is usually stated is that given a modular
representation $M$, the class function which assigns to each element $g in G$
the value of $t_(g') (M)$, where $g'$ is the $p'$-part of $g$, is a generalised
ordinary character (i.e., the character of a difference of two characteristic
zero representations).
