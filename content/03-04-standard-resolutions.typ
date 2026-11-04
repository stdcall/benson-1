#import "main-defs.typ": *
#import "statements.typ": *

== Standard resolutions <sec:standard-resolutions>

#source(75)Suppose $G$ is a group and $R$ is a commutative ring of coefficients.
The *standard resolution*#idx("standard resolution")#idx(
  "resolution",
  "standard",
) of $R$ as an $R G$-module is the resolution
$
  dots.c -> F_2 stretch(-->)^(partial_2) F_1 stretch(-->)^(partial_1) F_0
$
where $F_n$ is the free $R$-module on $(n + 1)$-tuples $(g_0, dots, g_n)$ of
elements of $G$, with $G$-action given by
$ g(g_0, dots, g_n) = (g g_0, dots, g g_n). $
The boundary map $partial_n$ is given by
$
  partial_n (g_0, dots, g_n)
  = sum_(i=0)^n (-1)^i (g_0, dots limits(arrow.t)^i dots, g_n)
$
where the vertical arrow denotes that $g_i$ is missing from the list. This
definition should be compared with the usual boundary map in simplicial
homology. See for example Spanier [@bib:Spanier1966, Chapter 4]. It is easy to
check that $partial_n compose partial_(n+1) = 0$.

The map $h_n : F_n -> F_(n+1)$ given by
$ h_n (g_0, dots, g_n) = (1, g_0, dots, g_n) $
satisfies
$ id_(F_n) = partial_(n+1) compose h_n + h_(n-1) compose partial_n $
and is hence a chain contraction (as a complex of $R$-modules, not of
$R G$-modules) of the augmented complex
$
  dots.c -> F_2 stretch(-->)^(partial_2) F_1 stretch(-->)^(partial_1) F_0
  limits(->)^epsilon R -> 0
$
where $epsilon(g) = 1$ for all $g in G$. Thus the complex is acyclic, i.e.,
$Im(partial_(n+1)) = Ker(partial_n)$, see Section~@sec:chain-complexes.

To see that $F_n$ is a free $R G$-module, we rewrite it in the *bar notation*
$
  (g_0, dots, g_n) & = g_0
  [g_0^(-1) g_1|g_1^(-1) g_2|dots.c|g_(n-1)^(-1) g_n] \
  [g_1|dots.c|g_n] & = (1, g_1, g_1 g_2, dots, g_1 dots.c g_n) \
  partial_n [g_1|dots.c|g_n] & = g_1 [g_2|dots.c|g_n]
  + sum_(i=1)^(n-1) (-1)^i
  [g_1|dots.c|g_i g_(i+1)|dots.c|g_n] \
  & quad + (-1)^n [g_1|dots.c|g_(n-1)].
$
It is easy to see that $F_n$ is the free $R G$-module on basis elements given by
the symbols $[g_1|dots.c|g_n]$#idx("$[g_1|dots.c|g_n]$"). Thus for example $F_0$
is the free module on the single symbol $[space]$. Because of this notation, the
standard resolution is also known as the *bar resolution*#idx(
  "bar resolution",
).

So we see that the ${F_n, partial_n}$ form a *free resolution*#idx(
  "free",
  "resolution",
)#idx("resolution", "free") of $Coker(partial_1) = R$ by $R G$-modules.

Now if $M$ is an $R G$-module we may form complexes
$
  dots.c -> M times.o_(R G) F_2 stretch(-->)^(1 times.o partial_2)
  M times.o_(R G) F_1 stretch(-->)^(1 times.o partial_1) M times.o_(R G) F_0
$
#source(76)and
$
  Hom_(R G) (F_0, M) stretch(-->)^(delta^0) Hom_(R G) (F_1, M)
  stretch(-->)^(delta^1) Hom_(R G) (F_2, M) -> dots.c
$
where $delta^n$ is given by composition with $partial_(n+1)$. Since the
${F_n, partial_n}$ form a free resolution of $R$ as an $R G$-module we have
$
  H_n (G, M) & = Tor_n^(R G) (M, R)
               = H_n (M times.o_(R G) bold(F), 1 times.o partial_*) \
  H^n (G, M) & = Ext_(R G)^n (R, M) = H^n (Hom_(R G) (bold(F), M), delta^*),
$
see Section~@sec:chain-complexes. Some people start with this definition in
terms of the standard resolution as their basic definition of group homology and
cohomology.

Notice how explicit the above description is. Since
$Hom_(R G) (F_n, M) tilde.equiv Hom_R (R G^n, M)$, an $n$-cocycle is a function
from $G^n$ to $M$, and the coboundary formula above is given by
$
  & delta^n alpha(g_1, dots, g_(n+1)) = g_1 alpha(g_2, dots, g_(n+1)) + \
  & sum_(i=1)^n (-1)^i alpha(g_1, dots, g_i g_(i+1), dots, g_(n+1))
    + (-1)^(n+1) alpha(g_1, dots, g_n).
$

For the standard resolution, there is a strictly co-associative diagonal
approximation#idx("diagonal approximation") called the *Alexander–Whitney
map*#idx("Alexander–Whitney map") given by
$
  Delta(g_0, dots, g_n) = sum_(j=0)^n (g_0, dots, g_j) times.o (g_j, dots, g_n)
$
or in bar notation,
$
  Delta[g_1|dots.c|g_n]
  = sum_(j=0)^n [g_1|dots.c|g_j] times.o g_1 dots g_j
  [g_(j+1)|dots.c|g_n].
$

#subhead[Inflation] If $N$ is a normal subgroup of $G$ and $M$ is an
$R(G slash N)$-module then we have an *inflation map*#idx("inflation")
$ inf_(G slash N, G) : H^n (G slash N, M) -> H^n (G, M) $
given as follows. If $bold(P)$ is a projective resolution of $R$ as an
$R(G slash N)$-module and $bold(Q)$ is a projective resolution of $R$ as an
$R G$-module, then by the Comparison Theorem~@th:comparison and the remark after
it, the identity map of $R$ lifts to a chain map $rho : bold(Q) -> bold(P)$
uniquely up to homotopy. Thus if $hat(zeta) : P_n -> M$ is a cocycle
representing $zeta in H^n (G slash N, M)$ then
$hat(zeta) compose rho : Q_n -> M$ is also a cocycle and represents
$inf_(G slash N, G) (zeta) in H^n (G, M)$. It is easy to check that any other
cocycle representing $zeta$ will give rise to the same element of $H^n (G, M)$.

If $N$ does not act trivially on $M$, then we still write $inf_(G slash N, G)$
for the composite of the inflation from $H^n (G slash N, M^N)$ to $H^n (G, M^N)$
with the map $H^n (G, M^N) -> H^n (G, M)$ induced by the inclusion.

In terms of the standard resolution, we may take $rho$ to be the obvious map
sending group elements to their coset representatives, so that
$hat(zeta) compose rho$ is constant on cosets.

#exercise[
  #source(77)Using the standard resolutions for $G$ and $G slash N$, show that
  if $M$ is an $R G$-module then there is a five-term exact sequence
  $
    0 -> H^1 (G slash N, M^N) stretch(-->)^"inf" H^1 (G, M)
    -> H^1 (N, M)^(G slash N) \
    -> H^2 (G slash N, M^N) stretch(-->)^"inf" H^2 (G, M).
  $
  This sequence does not continue. We shall derive this sequence in Chapter~3 of
  Volume II as a consequence of the spectral sequence of the group extension.
]

Note that by using the resolution for $G$ to calculate $H^* (N, M)$, it is clear
that $G slash N$ acts, and that the image of restriction
$H^* (G, M) -> H^* (N, M)$ lies in the fixed points of this action.
