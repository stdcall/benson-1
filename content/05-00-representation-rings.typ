#import "main-defs.typ": *
#import "statements.typ": *

= Representation rings and Burnside rings <ch:representation-rings>

#source(183)Representation rings#idx("representation", "ring")#idx(
  "ring",
  "representation",
)#idx("Burnside ring")#idx("ring", "Burnside") are a convenient way of
organising information about direct sums and tensor products of modules. J.~A.
Green was the first person to make a systematic investigation of representation
rings in the 1960’s [@bib:Green1962]. For this reason representation rings are
also known as Green rings#idx("Green", "ring")#idx("ring", "Green"). In this
chapter we investigate representation theory from the point of view of the
structure of representation rings.

In the study of representation theory in characteristic zero, it is customary to
work in terms of the character table, namely the square table whose rows are
indexed by the ordinary irreducible representations, whose columns are indexed
by the conjugacy classes of group elements, and where a typical entry gives the
_trace_#idx("trace") of the group element on the representation. Why do we use
the trace function? This is because the maps $M |-> tr(g, M)$ are precisely the
ring homomorphisms from the representation ring to $CC$, and these homomorphisms
separate representations. In particular, in this case the representation ring is
semisimple#idx("ring", "semisimple")#idx("semisimple", "ring"). This has the
effect that we can compute with representations easily and effectively in terms
of their characters; representations are distinguished by their characters,
direct sum corresponds to addition and tensor product corresponds to
multiplication. The orthogonality relations state that we may determine the
dimension of the space of homomorphisms from one representation to another by
taking the inner product of their characters.

How much of this carries over to characteristic $p$, where $p divides |G|$? The
first problem is that Maschke's theorem no longer holds; a representation may be
indecomposable without being irreducible. Thus the concepts of representation
ring $a(G)$ and Grothendieck ring#idx("Grothendieck ring")#idx(
  "ring",
  "Grothendieck",
) do not coincide. The latter is a quotient of the former by the "ideal of short
exact sequences" $a_0 (G, 1)$. Brauer discovered the remarkable fact (he did not
state it in this language) that the Grothendieck ring
$cal(R) (G) = a(G) slash a_0 (G, 1)$ is _semisimple_, and found the set of
algebra homomorphisms from this to $CC$, in terms of lifting eigenvalues. Thus
he gets a square character table, giving information about composition factors
of modules, but saying nothing about how they are glued together. For some time,
it was conjectured that $a(G)$ has no nilpotent elements in general. However, it
is now known that $a(G)$ has no nilpotent elements whenever the Sylow
$p$-subgroups of $G$ are cyclic#idx("cyclic", "Sylow subgroups")#idx(
  "Sylow subgroups",
  "cyclic",
) ($p$ is the characteristic of $k$), as well as a few other cases in
characteristic two, whilst in general there are nilpotent elements (Green
[@bib:Green1962], O'Reilly [@bib:OReilly1964], Zemanek [@bib:Zemanek1971a,
@bib:Zemanek1973], Benson and #source(184)Carlson [@bib:Benson1986c]). It is
still not known whether there are nilpotent elements in the representation ring
of an elementary abelian 2-group of order at least eight.

The next feature of ordinary character theory which we may wish to mimic is the
bilinear form#idx("bilinear form")#idx("form", "bilinear") and orthogonality
relations#idx("orthogonality relations")#idx("relations", "orthogonality").
There are two sensible bilinear forms to use here, which both agree with the
usual inner product#idx("inner product")#idx("product", "inner") in the case of
characteristic zero. These are
$
  (M, N) = dim_k Hom_(k G) (M, N), quad
  chevron.l M, N chevron.r = rank "of" sum_(g in G) g "on" Hom_k (M, N).
$
There are elements $u$ and $v$ of $a(G)$ with $u v = 1$,
$(M, N) = chevron.l v.M, N chevron.r = chevron.l M, u.N chevron.r$ and
$chevron.l M, N chevron.r = (u.M, N) = (M, v.N)$. It is thus easy to pass back
and forth between these two bilinear forms, and the second has the advantage
that it is symmetric. The non-singularity of these bilinear forms follows from
the fact that the almost split sequences provide dual elements to the
indecomposable modules. These dual elements correspond to the simple modules and
the almost split sequences.
