#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-03-chain-complexes.typ": (
  chain-homotopy, chain-map-squares, short-exact-complexes, snake,
)

== Chain complexes and homology <sec:chain-complexes>

Homological and cohomological concepts can be associated to groups, to modules,
to topological spaces, to posets, and so on. These concepts form a major part of
the subject matter of this book. They are defined in terms of *chain complexes*
and *cochain complexes*.

#definition[
  Let $cal(A)$ be an abelian category. A *chain complex*#idx(
    "chain",
    "complex",
  )#idx("complex, (co)chain") of objects in $cal(A)$ (for example, a chain
  complex of abelian groups, or of vector spaces, or of modules) consists of a
  collection $bold(C) = {C_n | n in ZZ}$ of objects $C_n in cal(A)$ indexed by
  the integers, together with maps $partial_n: C_n -> C_(n-1)$ (called the
  *differentials*#idx("differential")) satisfying
  $partial_n compose partial_(n+1) = 0$.

  A *cochain complex*#idx("cochain", "complex") of objects in $cal(A)$ consists
  of a collection $bold(C) = {C^n | n in ZZ}$ of objects $C^n in cal(A)$ indexed
  by the integers, together with maps $delta^n: C^n -> C^(n+1)$ satisfying
  $delta^n compose delta^(n-1) = 0$.

  If $x in C_n$ or $C^n$, we write $deg(x) = n$ and say $x$ has *degree*#idx(
    "degree",
  ) $n$.
] <def:chain-complex>

#remark[
  If ${C_n, partial_n}$ is a chain complex then letting $C^n = C_(-n)$,
  $delta^n = partial_(-n)$, we obtain a cochain complex ${C^n, delta^n}$, and
  vice-versa. Thus in some sense chain complexes and cochain complexes are the
  same thing. In the end, whether we regard something as a chain complex or a
  cochain complex usually depends on where it came from. It often happens, for
  example, that #source(40)$C_n = 0$ (resp. $C^n = 0$) for $n < 0$ or for
  $n < -1$. We say that a (co)chain complex $bold(C)$ is *bounded below*#idx(
    "bounded, below/above",
  ) if $C_n = 0$ (resp. $C^n = 0$) for all $n$ sufficiently large negative, and
  *bounded above* if this holds for all $n$ sufficiently large positive.
  $bold(C)$ is *bounded* if it is bounded both below and above.
]

#definition[
  The *homology*#idx("homology")#idx("$H_n$, $H^n$") of a chain complex
  $bold(C)$ is given by
  $
    H_n (bold(C)) = H_n (bold(C), partial_*)
    = frac(Ker (partial_n: C_n -> C_(n-1)), Im (partial_(n+1): C_(n+1) -> C_n))
    = frac(Z_n (bold(C)), B_n (bold(C))).
  $
  The *cohomology*#idx("cohomology") of a cochain complex $bold(C)$ is given by
  $
    H^n (bold(C)) = H^n (bold(C), delta^*)
    = frac(Ker (delta^n: C^n -> C^(n+1)), Im (delta^(n-1): C^(n-1) -> C^n))
    = frac(Z^n (bold(C)), B^n (bold(C))).
  $

  If $x in C_n$ with $partial_n (x) = 0$ (resp. $x in C^n$ with
  $delta^n (x) = 0$) then $x in Z_n (bold(C))$ is called a *cycle*#idx("cycle")
  (resp. $x in Z^n (bold(C))$ is a *cocycle*#idx("cocycle")), and we write $[x]$
  for the image of $x$ in $H_n (bold(C))$ (resp. $H^n (bold(C))$). If
  $x = partial_(n+1) (y)$ with $y in C_(n+1)$ (resp. $x = delta^(n-1) (y)$ with
  $y in C^(n-1)$) then $x in B_n (bold(C))$ is called a *boundary*#idx(
    "boundary",
  ) (resp. $x in B^n (bold(C))$ is a *coboundary*#idx("coboundary")). Thus
  $H_n (bold(C))$ (resp. $H^n (bold(C))$) consists of cycles modulo boundaries
  (resp. cocycles modulo coboundaries).
] <def:homology>

#definition[
  If $bold(C)$ and $bold(D)$ are chain complexes (resp. cochain complexes), a
  *chain map*#idx("chain", "map")#idx("map", "(co)chain") (resp. *cochain
  map*#idx("cochain", "map")) $f: bold(C) -> bold(D)$ consists of maps
  $f_n: C_n -> D_n$ (resp. $f_n: C^n -> D^n$), $n in ZZ$, such that the
  following diagram commutes.
  $
    #chain-map-squares
  $

  Clearly a (co)chain map $f: bold(C) -> bold(D)$ induces a well defined map
  $f_*: H_n (bold(C)) -> H_n (bold(D))$ (resp.
  $f^*: H^n (bold(C)) -> H^n (bold(D))$) defined by $f_* [x] = [f(x)]$ (resp.
  $f^* [x] = [f(x)]$) for $x in Z_n$ (resp. $Z^n$).

  From now on, we shall formulate concepts and theorems for chain complexes, and
  leave the reader to formulate them for cochain complexes.
] <def:chain-map>

#definition[
  If $f, f': bold(C) -> bold(D)$ are chain maps, we say $f$ and $f'$ are *chain
  homotopic*#idx("chain", "homotopy")#idx("homotopy, chain") (written
  $f tilde.eq f'$) if there are maps $h_n: C_n -> D_(n+1)$, $n in ZZ$, such that
  $
    f_n - f'_n = partial_(n+1) compose h_n + h_(n-1) compose partial_n.
  $
  $
    #chain-homotopy
  $

  #source(41)We say $bold(C)$ and $bold(D)$ are *chain homotopy equivalent*#idx(
    "chain",
    "homotopy",
    "equivalence",
  )#idx("equivalence", "chain homotopy") (written $bold(C) tilde.eq bold(D)$) if
  there are chain maps $f: bold(C) -> bold(D)$ and $f': bold(D) -> bold(C)$ such
  that the composites are chain homotopic to the identity maps
  $f compose f' tilde.eq id_bold(D)$ and $f' compose f tilde.eq id_bold(C)$.

  We say $bold(C)$ is *chain contractible* if it is chain homotopy equivalent to
  the zero complex. This is equivalent to the condition that there is a *chain
  contraction*#idx("chain", "contraction")#idx("contraction, chain"), i.e., a
  collection of maps $s_n: C_n -> C_(n+1)$ with
  $id_(C_n) = partial_(n+1) compose s_n + s_(n-1) compose partial_n$.
] <def:chain-homotopy>

The reason for this definition is that homotopic maps between topological spaces
(see Chapter 1 of Volume II) give rise to chain homotopic maps between their
singular chain complexes. A contractible space will have a chain contractible
_reduced_ singular chain complex. See for example Spanier [@bib:Spanier1966,
Section 4.4]. Thus the following proposition is the algebraic counterpart of the
fact that the singular homology groups of a topological space are homotopy
invariants.

#proposition[
  If $f, f': bold(C) -> bold(D)$ are chain homotopic then
  $f_* = f'_*: H_n (bold(C)) -> H_n (bold(D))$. Thus a homotopy equivalence
  $bold(C) tilde.eq bold(D)$ induces isomorphisms
  $H_n (bold(C)) tilde.equiv H_n (bold(D))$ for all $n in ZZ$.
] <prop:homotopy-invariance>

#proof[
  If $x in C_n$ with $partial_n (x) = 0$ then
  $
    f_* [x] - f'_* [x] & = [f_n (x) - f'_n (x)]
                         = [partial_(n+1) (h_n (x)) + h_(n-1) (partial_n (x))] \
                       & = [partial_(n+1) (h_n (x))] = 0.
  $
]

#subhead[The long exact sequence in homology]#idx("long exact sequence")#idx(
  "exact sequence, long",
)#idx("sequence", "long exact")

#definition[
  A *short exact sequence* $0 -> bold(C)' -> bold(C) -> bold(C)'' -> 0$ of chain
  complexes consists of maps of chain complexes $bold(C)' -> bold(C)$ and
  $bold(C) -> bold(C)''$ such that for each $n$,
  $0 -> C'_n -> C_n -> C''_n -> 0$ is a short exact sequence.
] <def:short-exact-complexes>

$
  #short-exact-complexes
$

#source(42)

#proposition[
  A short exact sequence $0 -> bold(C)' -> bold(C) -> bold(C)'' -> 0$ of chain
  complexes gives rise to a long exact sequence
  $
    dots.c -> H_n (bold(C)') -> H_n (bold(C)) -> H_n (bold(C)'')
    -> H_(n-1) (bold(C)') -> H_(n-1) (bold(C)) -> dots.c
  $
] <prop:long-exact-homology>

#proof[
  We define the *switchback map*#idx("switchback map") or *connecting
  homomorphism*#idx("connecting homomorphism")#idx("homomorphism", "connecting")
  $ partial: H_n (bold(C)'') -> H_(n-1) (bold(C)') $
  as follows. If $x in bold(C)''_n$ with $partial''_n (x) = 0$, so that
  $[x] in H_n (bold(C)'')$, choose $y in C_n$ with $psi_n (y) = x$. Then
  $psi_(n-1) partial_n (y) = partial''_n psi_n (y) = 0$ and so
  $partial_n (y) = phi.alt_(n-1) (z)$ with $z in C'_(n-1)$. We have
  $phi.alt_(n-2) partial'_(n-1) (z) = partial_(n-1) phi.alt_(n-1) (z)
  = partial_(n-1) partial_n (y) = 0$ and so $partial'_(n-1) (z) = 0$. We define
  $partial [x] = [z] in H_(n-1) (bold(C)')$.

  If $y'$ is another element of $C_n$ with $psi_n (y') = x$ and $z' in C'_(n-1)$
  with $partial_n (y') = phi.alt_(n-1) (z')$, then $psi_n (y - y') = 0$, and so
  $y - y' = phi.alt_n (u)$ for some $u in C'_n$. We have
  $phi.alt_(n-1) partial'_n (u) = partial_n phi.alt_n (u)
  = partial_n (y) - partial_n (y') = phi.alt_(n-1) (z) - phi.alt_(n-1) (z')$ and
  so $partial'_n (u) = z - z'$. Thus $[z] = [z'] in H_(n-1) (bold(C)')$. This
  shows that $partial: H_n (bold(C)'') -> H_(n-1) (bold(C)')$ is well defined.
  Exactness of the sequence is not hard to check.
]

We find it worthwhile to record the cohomological version of the above
proposition.

#proposition(closed: true)[
  A short exact sequence of cochain complexes gives rise to a long exact
  sequence
  $
    dots.c -> H^n (bold(C)') -> H^n (bold(C)) -> H^n (bold(C)'')
    -> H^(n+1) (bold(C)') -> H^(n+1) (bold(C)) -> dots.c
  $
] <prop:long-exact-cohomology>

A particular case of the above exact sequences is the following:

#lemma(title: [Snake Lemma])[
  A commutative diagram of short exact sequences
  $
    #snake
  $
  gives rise to a six term exact sequence
  $
    0 -> Ker alpha -> Ker beta -> Ker gamma -> Coker alpha -> Coker beta
    -> Coker gamma -> 0.
  $
] <lem:snake>
#idx("lemma", "snake", target: [@lem:snake])#idx(
  "snake lemma",
  target: [@lem:snake],
)

#proof[
  We regard the diagram as a short exact sequence of chain complexes of length
  two, and apply Proposition~@prop:long-exact-homology.
]
