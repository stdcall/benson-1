#import "main-defs.typ": *
#import "statements.typ": *

== Bilinear forms on representation rings <sec:bilinear-forms>

The material in this and the next section comes from [@bib:Benson1984d]. We
define two different bilinear forms#idx("bilinear form") $( med , med )$ and
$chevron.l med , med chevron.r$ on $a(k G)$ and $A(k G)$ as follows. If $M$ and
$N$ are finitely generated $k G$-modules, we let
$
  ([M], [N]) = dim_k Hom_(k G) (M, N) = dim_k (M^* times.o N)^G.
$
We extend $( med , med )$ bilinearly to give a bilinear form on $a(G)$ and
$A(G)$.

Now the bilinear form $( med , med )$ is usually not symmetric, but it is very
closely related to the symmetric bilinear form $chevron.l med , med chevron.r$
defined by bilinearly extending
$ chevron.l [M], [N] chevron.r = dim_k (M, N)_1^G, $
the dimension of the space of homomorphisms from $M$ to $N$ which factor through
some projective module (see Definition~@def:transfer).

#definition[
  We define elements $u$#idx("$u$") and $v$#idx("$v$") of $a(G)$ via
  $
    u = u_(k G) = [P_k] - [Omega^(-1)(k)], quad
    v = v_(k G) = [P_k] - [Omega(k)]
  $
  where $P_k$ is the projective cover ($=$ injective hull) of the trivial
  $k G$-module $k$, $Omega(k)$ is the kernel of $P_k arrow.twohead k$ and
  $Omega^(-1)(k)$ is the cokernel of $k arrow.hook P_k$. Note that
  $P_k tilde.equiv P_k^*$ and $Omega^(-1)(k) tilde.equiv Omega(k)^*$, so that
  $v$ is the 'dual' of $u$.
] <def:u-v>

#lemma[
  #source(209)The following expressions are equal:
  + $chevron.l [M], [N] chevron.r$,
  + The multiplicity of $P_k$ as a summand of $Hom_k (M, N) = M^* times.o N$,
  + $(u, [Hom_k (M, N)]) = (u.[M], [N])$,
  + The rank of the element $sum_(g in G) g$ of the group algebra $k G$ in its
    matrix representation on $Hom_k (M, N)$.

  In particular, since $P_k$ is self-dual, #statement-comment[(ii)] shows that
  $chevron.l med , med chevron.r$ is symmetric.
] <lem:symmetric-form>

#proof[
  Since each of these expressions is unaffected if we replace $M$ by the trivial
  module $k$ and $N$ by $Hom_k (M, N)$, we may assume that $M = k$. Also, since
  each expression is additive in $N$, we may suppose that $N$ is indecomposable.
  We shall show that each of these expressions is equal to 1 when
  $N tilde.equiv P_k$ and 0 otherwise.

  + If $chevron.l [k], [N] chevron.r != 0$ then there is a non-zero map $k -> N$
    which is a transfer from the trivial subgroup. The image of 1 under such a
    map is of the form $sum_(g in G) g(x)$ for some $x in N$. Let
    $lambda : P arrow.twohead N$ be the projective cover of $N$, and choose
    $y in P$ with $lambda(y) = x$. Then $sum_(g in G) g(y)$ is a non-zero
    $G$-invariant element of $P$ which is sent to the non-zero element
    $sum_(g in G) g(x)$ by $lambda$. Since projective $k G$-modules are
    injective (Proposition~@prop:group-algebra-symmetric) and
    $Soc(P_k) tilde.equiv k$ (Theorem~@th:symmetric-socle), the injective map
    $k -> P$ taking 1 to $sum_(g in G) g(y)$ extends to an inclusion of $P_k$ as
    a direct summand of $P$. The map $lambda$ does not kill the socle of this
    copy of $P_k$, so since $P_k$ is injective, it is a summand of $N$. Since
    $N$ is indecomposable this forces $N tilde.equiv P_k$. Clearly
    $chevron.l [k], [P_k] chevron.r = 1$.
  + The multiplicity of $P_k$ as a summand of an indecomposable module $N$ is
    clearly equal to 1 when $N tilde.equiv P_k$ and zero otherwise.
  + A homomorphism from $P_k$ to $N$ factors through
    $Omega^(-1)(k) = P_k slash k$ unless $N tilde.equiv P_k$, since $P_k$ is
    injective. Thus if $N tilde.equiv.not P_k$ we have $(u, [N]) = 0$. On the
    other hand, if $N tilde.equiv P_k$, then any homomorphism $P_k -> N$ is a
    multiple of this isomorphism plus a homomorphism factoring through
    $Omega^(-1)(k)$, and so $(u, [P_k]) = 1$.
  + This is clearly equal to (i).
]

#lemma[
  In $a(G)$ we have $u v = 1$.
] <lem:u-v-inverse>

#proof[
  Tensoring the short exact sequence $0 -> Omega(k) -> P_k -> k -> 0$ with
  $Omega^(-1)(k)$, we obtain a short exact sequence
  $
    0 -> Omega(k) times.o Omega^(-1)(k) -> P_k times.o Omega^(-1)(k)
    -> Omega^(-1)(k) -> 0.
  $
  We also have a short exact sequence $0 -> k -> P_k -> Omega^(-1)(k) -> 0$ so
  that by Schanuel's lemma we obtain
  $
    P_k plus.o Omega(k) times.o Omega^(-1)(k) tilde.equiv
    k plus.o P_k times.o Omega^(-1)(k).
  $
  Since tensoring with $P_k$ splits short exact sequences, we also have
  $ P_k times.o P_k tilde.equiv P_k times.o Omega(k) plus.o P_k $
  and so
  $
    P_k times.o P_k plus.o Omega(k) times.o Omega^(-1)(k) tilde.equiv
    k plus.o P_k times.o Omega^(-1)(k) plus.o P_k times.o Omega(k).
  $
  #source(210)It follows that
  $ ([P_k] - [Omega(k)])([P_k] - [Omega^(-1)(k)]) = [k] $
  in $a(G)$.
]

#proposition[
  If $x$ and $y$ are elements of $a(G)$ or $A(G)$, then
  + $(x, y) = chevron.l v x, y chevron.r = chevron.l x, u y chevron.r$
  + $chevron.l x, y chevron.r = (u x, y) = (x, v y)$
  + $(x, y) = (y, v^2 x) = (u^2 y, x)$.
] <prop:forms-u-v>

#proof[
  It follows from Lemma~@lem:symmetric-form that
  $chevron.l x, y chevron.r = (u x, y)$. The rest follows from the identity
  $u v = 1$ and the fact that $u$ is obtained from $v$ by dualising.
]

#lemma[
  If $H$ is a subgroup of $G$ then $res_(G, H) (u_(k G)) = u_(k H)$ and
  $res_(G, H) (v_(k G)) = v_(k H)$.
] <lem:u-v-restriction>

#proof[
  The second of these follows by applying Schanuel's lemma to the sequences
  $
    0 -> Omega(k)_(k G) down_H -> (P_k)_(k G) down_H -> k -> 0 \
    0 -> Omega(k)_(k H) -> (P_k)_(k H) -> k -> 0
  $
  and the first follows by duality.
]

#proposition[
  If $x in a(H)$ and $y in a(G)$ then
  + $(x, res_(G, H) (y)) = (ind_(H, G) (x), y)$ and
    $(res_(G, H) (y), x) = (y, ind_(H, G) (x))$.
  + $chevron.l x, res_(G, H) (y) chevron.r = chevron.l ind_(H, G) (x), y
    chevron.r$.
] <prop:forms-frobenius-reciprocity>

#proof[
  The first of these follows from the Nakayama relations, and the second follows
  since
  $
    chevron.l x, res_(G, H) (y) chevron.r
    & = (u_(k H) x, res_(G, H) (y)) = (ind_(H, G) (u_(k H) x), y) \
    & = (ind_(H, G) (res_(G, H) (u_(k G)) x), y)
    = (u_(k G) ind_(H, G) (x), y) \
    & = chevron.l ind_(H, G) (x), y chevron.r.
  $
]
