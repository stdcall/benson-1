#import "main-defs.typ": *
#import "statements.typ": *

= Block theory <ch:block-theory>

#source(213)There are now quite a few decent expositions of block theory#idx(
  "block",
  "theory",
) available. The reader is advised to consult Alperin [@bib:Alperin1986], Curtis
and Reiner [@bib:Curtis1987], Dornhoff [@bib:Dornhoff1972], Feit
[@bib:Feit1982], Landrock [@bib:Landrock1984], Nagao and Tsushima
[@bib:Nagao1988], and of course the collected works of Brauer [@bib:Brauer1980].
For this reason, we shall not attempt an encyclopædic treatment, but we shall
rather try to concentrate on aspects of the theory which are closely related to
other topics discussed in this book.

The approach we shall take is the module theoretic approach initiated by Green
[@bib:Green1968]. In this approach, the group algebra $k G$ is regarded as a
module for $k(G times G)$, and the indecomposable direct summands of this module
are the blocks. A vertex of a block as a $k(G times G)$-module is always
conjugate to a diagonally embedded subgroup $diag(D)$, $D <= G$, and $D$ is
called a defect group of the block. It turns out that the group $D$ in some
sense determines how complicated the block is.

Throughout this chapter, $(K, cal(O), k)$ will denote a $p$-modular system#idx(
  "$p$-modular system",
)#idx("system", "$p$-modular"). Thus $cal(O)$ is a complete rank one discrete
valuation ring with field of fractions $K$ of characteristic zero, maximal ideal
$frak(p)$, and quotient field $k$ of characteristic $p$. When we write $R$ for
the coefficient ring, we shall assume that $R in {cal(O), k}$.
