#import "main-defs.typ": *
#import "statements.typ": *

== Non-singularity <sec:non-singularity>

In this section we use the almost split sequences, discussed in
Chapter~@ch:representations-algebras, to prove that the bilinear forms
$( med , med )$ and $chevron.l med , med chevron.r$ on $a(G)$ introduced in the
last section are non-singular#idx("non-singularity", "representation rings").
The material in this section comes from [@bib:Benson1984d].

Recall from Theorem~@th:almost-split-existence that given any non-projective
module $N$, there is an almost split sequence terminating in $N$
$ 0 -> M -> E -> N -> 0 $
unique up to isomorphism of short exact sequences, and by
Proposition~@prop:symmetric-dtr we have $M tilde.equiv Omega^2 (N)$.

Recall also from Proposition~@prop:almost-split-functors that an almost split
sequence
$ 0 -> M -> E -> N -> 0 $
gives rise to an exact sequence
$ 0 -> Hom_Lambda (N', M) -> Hom_Lambda (N', E) -> Hom_Lambda (N', N) -> 0 $
#source(211)if $N'$ has no summand isomorphic to $N$, and
$
  #aligned-rows(
    ($0 -> Hom_Lambda (N, M) -> Hom_Lambda (N, E)$, $-> End_Lambda (N)$),
    ($$, $-> End_Lambda (N) slash J End_Lambda (N) -> 0.$),
  )
$
It follows that if we set $tau_0 [N] = [N] + [M] - [E]$#idx("$tau_0$, $tau_1$")
in $a(G)$ then we have
$
  ([N'], tau_0 [N]) = cases(
    d(N) & quad "if" N tilde.equiv N',
    0 & quad "otherwise",
  )
$
(where $d(N) = dim_k End_(k G) (N) slash J End_(k G) (N)$, which is always 1 if
$k$ is algebraically closed), so that the $tau_0 [N]$ form a sort of "dual
basis" to the basis of indecomposable modules $[N]$ for $a(G)$.

There are two problems with this statement. The first is that we have only
defined $tau_0 [N]$ for $N$ a non-projective indecomposable. However, it is easy
to see that the right definition for $N$ projective is
$tau_0 [N] = [N] - Rad(N)$. This is because any homomorphism to $N$ whose image
does not lie in $Rad(N)$ is surjective and hence splits.

Having now defined $tau_0$ on the basis elements $[N]$, we extend antilinearly
to define
$ tau_0 sum_i a_i [N_i] = sum_i macron(a)_i tau_0 [N_i] $
in $A(G)$, where $macron(a)_i$ denotes the complex conjugate of $a_i$.

The second problem is that for infinite dimensional vector spaces, duality does
not work very well, and it turns out that the $tau_0 [N]$ do not form a basis of
$A(G)$ unless $A(G)$ is finite dimensional (which happens if and only if the
Sylow $p$-subgroups of $G$ are cyclic; see
Theorem~@th:group-algebra-representation-type). But in any case, we have now
proved the following theorem, which may be thought of as a non-singularity
statement for the bilinear form $( med , med )$.

#theorem(closed: true)[
  Suppose $N$ and $N'$ are indecomposable $k G$-modules, and $tau_0$ is as
  defined above. Then
  $
    ([N'], tau_0 [N]) = cases(
      d(N) & quad "if" N tilde.equiv N',
      0 & quad "otherwise",
    )
  $
  where $d(N) = dim_k End_(k G) (N) slash J End_(k G) (N)$.

  Thus for any $x = sum_i a_i [M_i] in A(G)$ we have
  $(x, tau_0 (x)) = sum_i |a_i|^2 d(M_i) gt.eq 0$ with equality if and only if
  $x = 0$.
] <th:tau-zero-dual>

The following corollary may also be proved directly without using almost split
sequences.

#corollary(closed: true)[
  Suppose $N_1$ and $N_2$ are two $k G$-modules, such that for every
  $k G$-module $M$ we have
  $ dim_k Hom_(k G) (M, N_1) = dim_k Hom_(k G) (M, N_2). $
  Then $N_1 tilde.equiv N_2$.
] <cor:hom-dimensions-determine>

#source(212)So far, everything we have done works just as well for an arbitrary
finite dimensional algebra. However, we now wish to do the same for the inner
product $chevron.l med , med chevron.r$, and for this we need to use the
multiplication in $A(G)$, as well as the fact that $k G$ is a symmetric algebra.

In the last section, we saw that it is very easy to pass between the
$( med , med )$ and $chevron.l med , med chevron.r$ using the elements $u$ and
$v$. We take
$ tau_1 [N] = u.tau_0 [N], $
so that $chevron.l [N'], tau_1 [N] chevron.r = ([N'], tau_0 [N])$ is equal to
$d(N)$ if $N tilde.equiv N'$ and zero otherwise.

Now suppose $N$ is a non-projective indecomposable. By
Corollary~@cor:omega-tensor we have
$N times.o Omega(k) tilde.equiv Omega(N) plus.o ("projective")$, and so modulo
projectives we have
$
  u.tau_0 [N] = -Omega^(-1)(tau_0 [N])
  = -[Omega^(-1)(N)] - [Omega^(-1)(M)] + [Omega^(-1)(E)].
$
But recall from Corollary~@cor:cartan-homomorphism that
$A(G) = A(G, 1) plus.o A_0 (G, 1)$ as a direct sum of ideals. Since
$tau_0 [N] in A_0 (G, 1)$, this shows that
$u.tau_0 [N] = [X] - [Omega^(-1)(N)] - [Omega^(-1)(M)]$ without working modulo
projectives, where $0 -> Omega^(-1)(M) -> X -> Omega^(-1)(N) -> 0$ is obtained
by applying $Omega^(-1)$ to the almost split sequence, so that
$X tilde.equiv Omega^(-1)(E)$ modulo projectives.

On the other hand, if $N$ is projective indecomposable, then $N = P_S$ is the
projective cover of a simple module $S$. Schanuel's lemma shows that
$v.[S] = [P_S] - [Omega(S)] = tau_0 [N]$, and so $tau_1 [N] = u.v.[S] = [S]$.

We record what we have proved in the following theorem, which is a
non-singularity statement for $chevron.l med , med chevron.r$.

#theorem(closed: true)[
  Suppose $N$ and $N'$ are indecomposable $k G$-modules, and define $tau_1 [N]$
  to be $N slash Rad(N) tilde.equiv Soc(N)$ if $N$ is projective, and
  $ [X] - [Omega^(-1)(N)] - [Omega(N)] $
  if $N$ is not projective, where
  $ 0 -> Omega(N) -> X -> Omega^(-1)(N) -> 0 $
  is the almost split sequence terminating in $Omega^(-1)(N)$. Then
  $
    chevron.l [N'], tau_1 [N] chevron.r
    = cases(
      d(N) & quad "if" N tilde.equiv N',
      0 & quad "otherwise",
    )
  $
  where $d(N) = dim_k End_(k G) (N) slash J End_(k G) (N)$.
] <th:tau-one-dual>
