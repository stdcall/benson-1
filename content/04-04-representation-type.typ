#import "main-defs.typ": *
#import "statements.typ": *

== Representation type of algebras <sec:representation-type>

In this section, we describe without proof the trichotomy theorem for the
representation type#idx("representation", "type") of finite dimensional
algebras. We then investigate the representation type of finite dimensional
hereditary algebras. There are many variations of the following definitions in
the literature. The idea is always the same. An algebra is of finite
representation type if there are only finitely many indecomposables; otherwise
it is of infinite representation type#idx(
  "infinite",
  "representation type",
)#idx(
  "representation",
  "type",
  "infinite",
). It is of tame representation type if the indecomposables in each dimension
come in finitely many one parameter families with finitely many exceptions. In
some sense this is supposed to represent classifiability of the representations,
although in particular cases this can be a very hard problem. It is of wild
representation type if the representation theory "includes" that of a free
algebra in two variables. The latter in some sense includes the representation
theory of an arbitrary finite dimensional algebra, and the consensus feeling is
that the representations of a wild algebra are in some sense unclassifiable.
This is the same as the problem of finding a canonical form for pairs of not
necessarily commuting matrices. The definition of tame does not make sense over
a finite field, for obvious reasons.

#definition[
  Suppose $k$ is an infinite field.

  A finite dimensional algebra $Lambda$ is of *finite representation type*#idx(
    "finite",
    "representation type",
  )#idx(
    "representation",
    "type",
    "finite",
  ) if there are only finitely many isomorphism classes of indecomposable
  $Lambda$-modules.

  A finite dimensional algebra $Lambda$ is of *tame representation type*#idx(
    "tame",
    "representation type",
  )#idx(
    "representation",
    "type",
    "tame",
  ) if it is not of finite representation type, and for any dimension $n$, there
  is a finite set of $Lambda$–$k[T]$-bimodules $M_i$ which are free as right
  $k[T]$-modules, with the property that all but a finite number of
  indecomposable $Lambda$-modules of dimension $n$ are of the form
  $M_i times.o_(k[T]) M$ for some $i$, and for some indecomposable $k[T]$-module
  $M$. If the $M_i$ may be chosen independently of $n$, we say $Lambda$ has
  *domestic representation type*#idx(
    "domestic representation type",
  )#idx("representation", "type", "domestic"). Note that the indecomposable
  $k[T]$-modules are classified by their rational canonical forms#idx(
    "rational canonical form",
  )#idx("canonical form, rational"), which are the powers of irreducible
  polynomials over $k$.

  A finite dimensional algebra $Lambda$ has *wild representation type*#idx(
    "wild representation type",
  )#idx("representation", "type", "wild") if there is a finitely generated
  $Lambda$–$k chevron.l X, Y chevron.r$-bimodule $M$ which is free as a right
  $k chevron.l X, Y chevron.r$-module, such that the functor
  $M times.o_(k chevron.l X, Y chevron.r) -$ from finite dimensional
  $k chevron.l X, Y chevron.r$-modules to finite dimensional $Lambda$-modules
  preserves indecomposability and isomorphism class. Here,
  $k chevron.l X, Y chevron.r$ is the free algebra on two variables; namely the
  path algebra of the graph with one vertex and two arrows.
] <def:representation-type>

#source(127)We shall omit the proof of the following trichotomy theorem, which
is rather technical.

#theorem(
  title: [Drozd [@bib:Drozd1977, @bib:Drozd1979]; Crawley-Boevey
    [@bib:CrawleyBoevey1988b]],
  closed: true,
  head-break: true,
)[
  Over an algebraically closed field, every finite dimensional algebra is of
  finite, tame or wild representation type, and these types are mutually
  exclusive.
] <th:trichotomy>
#idx("trichotomy theorem", target: [@th:trichotomy])#idx(
  "theorem",
  "trichotomy",
  target: [@th:trichotomy],
)

A precise statement about the unclassifiability of finite dimensional modules
over a free algebra on two variables is the following. The theory of finite
dimensional $Lambda$-modules is said to be *decidable*#idx(
  "decidable module theory",
)#idx("module", "theory, decidable") if there is a Turing machine#idx(
  "Turing machine",
) algorithm which will decide the truth or falsehood of any sentence in the
language of finite dimensional $Lambda$-modules.

#theorem(
  title: [Baur [@bib:Baur1975]; Kokorin and Mart'yanov [@bib:Kokorin1973]],
  closed: true,
  head-break: true,
)[
  Let $k$ be any field. Then the theory of finite dimensional
  $k chevron.l X, Y chevron.r$-modules is undecidable#idx(
    "undecidable module theory",
  ).
] <th:undecidable>

The proof consists of encoding the word problem for finitely presented groups
into the module theory of $k chevron.l X, Y chevron.r$. It is conjectured that
for finite dimensional algebras $Lambda$, the theory of finite dimensional
$Lambda$-modules is undecidable if and only if $Lambda$ has wild representation
type. For an extensive discussion of this question, see Prest [@bib:Prest1988],
where a proof is also given for the above theorem. The conjecture has been
verified for path algebras of quivers (without relations).

For group algebras the trichotomy theorem is much easier to prove. The following
is a more precise statement:

#theorem(
  title: [Bondarenko and Drozd [@bib:Bondarenko1977]; see also Ringel
    [@bib:Ringel1975a]],
  closed: true,
  head-break: true,
)[
  Let $G$ be a finite group and $k$ an infinite field of characteristic $p$.
  + $k G$ has finite representation type if and only if $G$ has cyclic Sylow
    $p$-subgroups#idx("Sylow subgroups", "cyclic")#idx(
      "cyclic",
      "Sylow subgroups",
    ).
  + $k G$ has domestic representation type if and only if $p = 2$ and the Sylow
    $2$-subgroups of $G$ are isomorphic to the Klein four group#idx(
      "Klein four group",
    )#idx("group", "Klein four")#idx("four", "group, Klein")#idx(
      "Sylow subgroups",
      "Klein four",
    ).
  + $k G$ has tame representation type if and only if $p = 2$ and the Sylow
    $2$-subgroups are dihedral#idx("dihedral groups")#idx(
      "group",
      "dihedral",
    )#idx("Sylow subgroups", "dihedral"), semidihedral#idx(
      "semidihedral groups",
    )#idx("group", "semidihedral")#idx("Sylow subgroups", "semidihedral") or
    generalised quaternion#idx("generalised quaternion groups")#idx(
      "group",
      "generalised quaternion",
    )#idx("quaternion groups, generalised")#idx(
      "Sylow subgroups",
      "generalised quaternion",
    ).
  + In all other cases $k G$ has wild representation type.
] <th:group-algebra-representation-type>

We shall be investigating the indecomposable representations of some of the tame
group algebras#idx("tame", "group algebras") later in this chapter. We shall
also see that for path algebras, there is a connection between the
representation type and the positivity of a certain quadratic form defined in
terms of the quiver. In fact, the representation type is finite if and only if
the associated form is positive definite, and tame if and only if the associated
form is positive semidefinite (and not definite). We shall only prove some of
these results, and give references for the rest. The classification of quivers
according to the associated quadratic form is the subject of the next two
sections, and leads to the Dynkin and Euclidean diagrams.

#exercise[
  #source(128)Use the theory of vertices and sources to prove part (i) of the
  above theorem. For a proof of a stronger version of this, see
  Corollary~@cor:block-finite-type.
]
