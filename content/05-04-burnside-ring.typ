#import "main-defs.typ": *
#import "statements.typ": *

== $G$-sets and the Burnside ring <sec:burnside-ring>

We now go through the same process with permutation representations as we went
through in the last two sections with linear representations. The result is
called the Burnside ring. There is a natural homomorphism from the Burnside ring
to the representation ring of $R G$ for any coefficient ring $R$, and we shall
use this fact to obtain information about representation rings (namely various
"induction theorems") in Section~@sec:induction-theorems.

We define the *Burnside ring*#idx("Burnside ring")#idx("ring", "Burnside")
$b(G)$#idx("$b(G)$") to be the ring with generators the isomorphism classes
$[X]$ of permutation representations of $G$ on finite sets, and relations
$ [X] + [Y] = [X dot(union) Y], quad [X].[Y] = [X times Y] $
giving the addition and multiplication in terms of disjoint union and Cartesian
product. The identity element of this ring corresponds to the one point set with
trivial action, and the zero element corresponds to the empty set.

#source(190)Now any permutation representation $X$ of $G$ may be expressed
uniquely as a disjoint union of orbits#idx("orbit"). The isomorphism classes of
transitive permutation representations are in one-one correspondence with the
conjugacy classes of subgroups in such a way that the permutation representation
$G slash H$ corresponds to the conjugacy class of $H$, which is characterised as
the stabiliser of a point. So the additive structure of $b(G)$ is easy to
describe. It is the free abelian group, with basis corresponding to the
transitive permutation representations $[G slash H]$#idx("$[G slash H]$"), one
for each conjugacy class of subgroups $H lt.eq G$.

#example[
  Suppose $G$ is the symmetric group $cal(S)_3$#idx(
    "group",
    "symmetric",
    "$cal(S)_3$",
  )#idx("symmetric", "group $cal(S)_3$"). Then we shall denote the transitive
  permutation representations of $G$ by 1, $a$, $b$ and $c$, on 1, 2, 3 and 6
  objects respectively. The multiplication table of $b(G)$ is as follows:

  #table(
    columns: 5,
    align: center,
    stroke: (x, y) => (
      left: if x <= 1 { 0.4pt },
      right: if x == 4 { 0.4pt },
      top: if y <= 1 { 0.4pt },
      bottom: if y == 4 { 0.4pt },
    ),
    [$times$], [1], [$a$], [$b$], [$c$],
    [1], [1], [$a$], [$b$], [$c$],
    [$a$], [$a$], [$2 a$], [$c$], [$2 c$],
    [$b$], [$b$], [$c$], [$b + c$], [$3 c$],
    [$c$], [$c$], [$2 c$], [$3 c$], [$6 c$],
  )

  What are the ring homomorphisms $f : b(G) -> CC$? Clearly for any such ring
  homomorphism we have $f(1) = 1$. Since $f(c)^2 = 6 f(c)$, either $f(c) = 0$ or
  $f(c) = 6$.

  Case (i): $f(c) = 6$. In this case $f(a) f(c) = 2 f(c)$ implies that
  $f(a) = 2$, while $f(b) f(c) = 3 f(c)$ implies that $f(b) = 3$.

  Case (ii): $f(c) = 0$ implies that $f(a) f(b) = 0$. In this case we have
  $f(a)^2 = 2 f(a)$ and $f(b)^2 = f(b)$, and so we have either $f(a) = 0$,
  $f(b) = 1$, or $f(a) = 2$, $f(b) = 0$, or $f(a) = 0$, $f(b) = 0$.

  We may summarise this information in the following table:

  #table(
    columns: 5,
    align: center,
    stroke: (x, y) => (
      left: if x == 1 { 0.4pt },
      right: if x == 4 { 0.4pt },
      top: if y == 0 and x >= 1 { 0.4pt },
      bottom: if y == 3 and x >= 1 { 0.4pt },
    ),
    [$c$], [6], [0], [0], [0],
    [$b$], [3], [1], [0], [0],
    [$a$], [2], [0], [2], [0],
    [1], [1], [1], [1], [1],
  )
]
We can interpret this table in terms of the numbers of fixed points on subgroups
as follows. If $H lt.eq G$, the map
$ f_H : b(G) -> ZZ subset.eq CC $
#idx("$f_H$")sending a permutation representation $X$ to $|X^H|$ is a ring
homomorphism, since
$
  |(X dot(union) Y)^H| = |X^H| + |Y^H|, quad
  |(X times Y)^H| = abs(X^H) abs(Y^H).
$
Clearly if $H$ is not conjugate to $K$ then $f_H != f_K$ (evaluate on
$G slash H$ and $G slash K$).

#lemma(closed: true)[
  We have $f_H (G slash K) != 0$ if and only if $H$ is conjugate to a subgroup
  of $K$.
] <lem:marks-nonzero>

#source(191)Let $B(G) = CC times.o_ZZ b(G)$#idx("$B(G)$"). Then $f_H$ extends in
an obvious way to a $CC$-linear ring homomorphism
$ f_H : B(G) -> CC $

#theorem[
  Every ring homomorphism $b(G) -> CC$ is of the form $f_H$ for some
  $H lt.eq G$. The sum of these maps is an isomorphism after tensoring with
  $CC$:
  $ sum f_H : B(G) -> plus.o.big_(H lt.eq_G G) CC. $
] <th:burnside-ring-homomorphisms>

#proof[
  By Lemma~@lem:independence-homomorphisms, the $f_H$ are linearly independent,
  and so the above map $sum f_H$ is surjective. Since $dim_CC B(G)$ is equal to
  the number of conjugacy classes of subgroups, it follows that it is an
  isomorphism.
]

We write $epsilon_H$#idx("$epsilon_H$") for the primitive idempotent
corresponding to $H$ in the right hand side of the above isomorphism, and
$e_H$#idx("$e_H$") for the corresponding element of $B(G)$.

It follows from the above theorem that
$ sum f_H : b(G) -> plus.o.big_(H lt.eq_G G) ZZ $
is injective with finite cokernel. How big is this cokernel? Choosing bases by
listing subgroups in non-decreasing order of size, the matrix of $sum f_H$ is
$ mat(*, , circle.big; , dots.down, ; *, , *). $
The diagonal entries are $f_H (G slash H) = |N_G (H) : H|$, and so the size of
the cokernel, which is the determinant of this matrix, is equal to
$ product_(H lt.eq_G G) |N_G (H) : H|. $

#remark[
  Burnside calls the above matrix the *table of marks*#idx("table of marks"). In
  section 185 of his book [@bib:Burnside1911], you will find the following table
  of marks for the alternating group $A_4$#idx(
    "alternating group",
    "$A_4$",
  )#idx("group", "alternating", "$A_4$").

  #table(
    columns: 6,
    align: center,
    stroke: (x, y) => (
      left: if x == 1 { 0.4pt },
      right: if x == 5 { 0.4pt },
      bottom: if y == 0 or y == 5 { 0.4pt },
    ),
    [], [1], [$C_2$], [$C_3$], [$V_4$], [$A_4$],
    [1], [12], [0], [0], [0], [0],
    [$C_2$], [6], [2], [0], [0], [0],
    [$C_3$], [4], [0], [1], [0], [0],
    [$V_4$], [3], [3], [0], [3], [0],
    [$A_4$], [1], [1], [1], [1], [1],
  )
]

#subhead[Congruences#idx("Burnside ring", "congruence in")#idx(
    "congruence in $b(G)$",
  ) and Idempotents#idx("Burnside ring", "idempotent in")#idx(
    "idempotent",
    "in $b(G)$",
  ) in $b(G)$] The idempotents in $B(G)$ are the elements
$ sum_(H in cal(H)) e_H $
#source(192)where $cal(H)$ is a collection of representatives of distinct
conjugacy classes of subgroups.

#question[
  When is $sum_(H in cal(H)) e_H$ in $b(G)$?
] <qu:burnside-idempotents>

More generally, if $S$ is a set of primes, we can look at the localised Burnside
ring $b(G)_((S))$, obtained by allowing denominators coprime to $S$. Thus for
example if $S = {p}$, we write $b(G)_((p))$#idx("$b(G)_((p))$") for the
$p$-local Burnside ring#idx("Burnside ring", "$p$-local")#idx(
  "$p$-local Burnside ring",
), and if $S$ is the set of all primes other than $p$, we write $b(G)_p$ for
$ZZ[1 slash p] times.o_ZZ b(G)$. All these rings may be thought of as subrings
of $B(G)$.

#question[
  When is $sum_(H in cal(H)) e_H$ in $b(G)_((S))$?
] <qu:local-burnside-idempotents>

#lemma(title: [Burnside])[
  The number of orbits of $G$ on $X$ is equal to
  $ 1 / (|G|) sum_(g in G) |X^((g))| $
  and in particular
  $ sum_(g in G) |X^((g))| equiv 0 quad (mod |G|). $
] <lem:burnside-orbits>
#idx("Burnside's lemma", target: [@lem:burnside-orbits])#idx(
  "lemma",
  "Burnside's",
  target: [@lem:burnside-orbits],
)

#proof[
  Count ${(x, g) | x g = x}$ in two ways.
]

Hence, if $H lt.closed.eq K lt.eq G$, then the quotient group $K slash H$ acts
on $X^H$, and we have
$ sum_(macron(k) in K slash H) |X^((H, k))| equiv 0 quad (mod |K slash H|). $
Here, $k$ denotes any pre-image of $macron(k)$ in $K$, and the group
$chevron.l H, k chevron.r$ is clearly independent of this choice.

We can obtain a complete set of congruences (i.e., characterising the image of
$b(G)$ under the map $sum f_H$) by taking $K = N_G (H)$ for each conjugacy class
of subgroups $H$ of $G$.

These congruences are independent since they form a lower triangular matrix of
congruences with ones on the diagonal. For example, in the case of the example
above from Burnside's book, the congruences say that
$
  mat(
    12, 0, 0, 0, 0; 6, 2, 0, 0, 0; 4, 0, 1, 0, 0; 3, 3, 0, 3, 0; 1, 1, 1, 1, 1
  )
  mat(1, 0, 0, 0, 0; 3, 1, 0, 0, 0; 8, 0, 1, 0, 0; 0, 1, 0, 1, 0; 0, 0, 0, 2, 1)
  equiv 0 quad (mod mat(12, 2, 1, 3, 1)).
$
The second matrix in the above equation has its rows and columns labelled by the
conjugacy classes of subgroups of $G$, and has a non-zero entry if and only if
the subgroup $H$ corresponding to the column is contained normally in a
conjugate of the subgroup $K$ corresponding to the row, with cyclic
quotient#idx("cyclic", "quotient")#idx("quotient", "cyclic"). The entry is the
number of times conjugates of $K$ appear in the above congruence for
$N_G (H) slash H$; namely the sum, over the subgroups $K$ in #source(193)the
given $G$-conjugacy class that contain $H$ normally with cyclic quotient, of the
number of generators of the cyclic group $K slash H$.

These congruences therefore define an additive subgroup of
$sum_(H lt.eq_G G) ZZ$ of the same index as $b(G)$, which therefore _is_ $b(G)$.
We have therefore proved the following theorem of Dress [@bib:Dress1971a] (our
presentation follows tom~Dieck [@bib:TomDieck1979]).

#theorem(closed: true)[
  The image of the map
  $ sum f_H : b(G) -> plus.o.big_(H lt.eq_G G) ZZ $
  is given by the congruences
  $
    sum_K |{"generators of" K slash H}|.f_K (x) equiv 0 quad (mod |N_G (H) : H|)
  $
  where the sum runs over the subgroups $K lt.eq G$ with $H lt.closed.eq K$ and
  $K slash H$ cyclic.
] <th:dress-congruences>

Note that we can separate these congruences into $p$-primary components by using
the pairs of groups $H lt.closed.eq N lt.eq G$ with
$N slash H in Syl_p (N_G (H) slash H)$.

#theorem(title: [Dress])[
  + An idempotent $sum_(H in cal(H)) e_H in B(G)$ lies in $b(G)$ if and only if,
    whenever $H lt.closed.eq H'$ with cyclic quotient,
    $H in cal(H) arrow.l.r.double H' in cal(H)$.
  + An idempotent $sum_(H in cal(H)) e_H in B(G)$ lies in $b(G)_((S))$ if and
    only if, whenever $H lt.closed.eq H'$ of index $p in S$, $H$ is conjugate to
    a subgroup in $cal(H)$ if and only if $H'$ is.
] <th:dress-idempotents>

#proof[
  Suppose $sum_(H in cal(H)) e_H in b(G)_((S))$ and $H lt.closed.eq H'$ with
  cyclic quotient of order $p in S$. Then the congruence
  $|X^H| equiv |X^(H')| mod |H' : H|$ implies that for all $x in b(G)_((S))$,
  $f_H (x) equiv f_(H') (x)$. Since $0 equiv.not 1 mod p$,
  $H in cal(H) arrow.l.r.double H' in cal(H)$. Conversely, by the above theorem,
  if these congruences are satisfied then $sum_(H in cal(H)) e_H in b(G)_((S))$.
]

#corollary(title: [Dress], closed: true)[
  + The primitive idempotents in $b(G)$ are of the form
    $ sum_(H^((infinity)) = H_0) e_H $
    where $H$ runs through representatives of conjugacy classes of subgroups of
    $G$ for which $H^((infinity))$ is a given perfect subgroup $H_0$ of $G$.

    In particular, $G$ is soluble#idx("soluble group")#idx("group", "soluble")
    if and only if the only idempotents in $b(G)$ are 0 and 1.
  + The primitive idempotents in $b(G)_((p))$ are of the form
    $ sum_(O^p (H) = H_0) e_H $
    where $H$ runs through representatives of conjugacy classes of subgroups of
    $G$ for which $O^p (H)$ is a given $p$-perfect subgroup $H_0$ of $G$ (i.e.,
    subgroup with no normal subgroup of index $p$).
] <cor:dress-primitive-idempotents>

#source(194)#subhead[Induction and Restriction] If $H lt.eq G$,
*restriction*#idx("restriction")#idx("$\"res\"_(G, H)$") is a ring homomorphism
$ res_(G, H) : b(G) -> b(H). $

Induction#idx("induction")#idx("$\"ind\"_(H, G)$") is defined on permutation
representations as follows. If $X$ is an $H$-set, define
$ G times_H X = (G times X) slash tilde.op $
where the equivalence relation $tilde.op$ is given by
$(g h, x) tilde.op (g, h x)$ for all $h in H$. The map
$
  ind_(H, G) : b(H) & -> b(G) \
                  X & |-> G times_H X
$
is a homomorphism of additive groups, but not of rings. The following lemma
summarises some properties of induction and restriction.

#lemma[
  + $(G times_H X)^G = emptyset$ if $H < G$.
  + $ind_(H, G) (a.res_(G, H) (b)) = ind_(H, G) (a).b$.
  + (Mackey formula#idx(
      "Mackey",
      "formula",
      "for permutation representations",
    )):
    $
      res_(G, H) ind_(K, G) (a) = sum_(H g K)
      ind_(H inter lconj(g, K), H)
      res_(lconj(g, K), H inter lconj(g, K)) (lconj(g, a)).
    $
] <lem:burnside-induction-restriction>

#proof[
  This is left as an easy exercise.
]

#theorem[
  Suppose $H$ is a subgroup of $G$. Then
  + $ind_(H, G) (e_H) = abs(N_G (H) : H) e_H$, where the first $e_H$ is in
    $B(H)$ and the second is in $B(G)$. In particular, as an element of $B(G)$,
    we have
    $ e_H in Im(ind_(H, G)). $
  + $B(G) = Im(ind_(H, G)) plus.o Ker(res_(G, H))$ as a direct sum of ideals.
] <th:burnside-induced-idempotent>

#proof[
  The restriction of $e_H$ to any proper subgroup of $H$ is zero, since all
  $f_K$ vanish on it. So by the Mackey formula, for $K lt.eq G$ we have
  $
    #aligned-rows(
      (
        $res_(G, K) ind_(H, G) (e_H)$,
        $= sum_(K g H) ind_(K inter lconj(g, H), K)
        res_(lconj(g, H), K inter lconj(g, H)) (lconj(g, e_H))$,
      ),
      (
        $$,
        $= sum_(K g H \ K gt.eq lconj(g, H)) ind_(lconj(g, H), K)
        (lconj(g, e_H)).$,
      ),
    )
  $
  The value of $f_K$ on an element induced from a proper subgroup of $K$ is
  zero, and so we have
  $
    f_K (ind_(H, G) (e_H)) = f_K (res_(G, K) ind_(H, G) (e_H))
    = cases(|N_G (H) : H| & quad H tilde.op K, 0 & quad H tilde.not K.)
  $
  It follows that $f_K (ind_(H, G) (e_H)) = f_K (abs(N_G (H) : H) e_H)$ for all
  $K lt.eq G$, and so by Theorem~@th:burnside-ring-homomorphisms we have
  $ind_(H, G) (e_H) = abs(N_G (H) : H) e_H$.

  It now follows that the $e_(H')$ with $H' lt.eq H$ lie in $Im(ind_(H, G))$
  while the $e_(H')$ with $H'$ not conjugate to a subgroup of $H$ lie in
  $Ker(res_(G, H))$, which proves the given direct sum decomposition.
]

#source(195)The second part of the above theorem has the following implication
for representation rings [@bib:Benson1984d].

#corollary[
  For any coefficient ring $R$ we have
  $ A(R G) = Im(ind_(H, G)) plus.o Ker(res_(G, H)) $
  as a direct sum of ideals.
] <cor:representation-ring-decomposition>

#proof[
  There is a natural map $phi.alt : b(G) -> a(R G)$, which takes a permutation
  representation to the matrix representation with the permuted points as basis.
  We also write $phi.alt$ for the corresponding map $B(G) -> A(R G)$. Writing
  $1 = e + e'$ with $e in Im(ind_(H, G))$ and $e' in Ker(res_(G, H))$ as in the
  theorem, we see that $1 = phi.alt(e) + phi.alt(e')$ in $A(R G)$ so that
  $ A(R G) = Im(ind_(H, G)) + Ker(res_(G, H)). $
  If $x in Im(ind_(H, G)) inter Ker(res_(G, H))$ then
  $x = x.1 = x.phi.alt(e) + x.phi.alt(e') = 0$ since the product of elements of
  $Im(ind_(H, G))$ and $Ker(res_(G, H))$ is zero.
]
