"""Exact checks of Chapter 6, Block theory (Sage, with GAP via libgap).

Benson, *Representations and Cohomology I*, second edition (1998),
Chapter 6 "Block theory", the introduction and Sections 6.1-6.6, printed
pp. 201-224.  Our files: content/06-00-block-theory.typ ...
content/06-06-klein-four-defect.typ.

The chapter is general theory.  Everything below is an exact computation
for small groups over finite splitting fields GF(q) (q - 1 divisible by
the p'-part of the exponent), over Z_(p) and in Q[l, r, m]: group algebras
as multiplication tables, the centre Z(kG) on the class sums, block
idempotents (ordinary characters grouped into p-blocks by GAP's
PrimeBlocks, reduced modulo a prime above p by a fixed map
Z[zeta_n] -> GF(q)), transfers computed on orbit sums, the Brauer map on
orbit sums, modules by matrices and the GAP MeatAxe (decompositions,
isomorphisms, radical series, Higman's criterion as "the identity lies in
the image of the transfer"), and decomposition matrices of the GAP
character table library.  Expected values are the book's statements,
read off the printed pages (the page and our label are named in each
message); the chapter files are not parsed.  Where the printed text was
corrected, the printed reading is kept as a refuted check next to the
corrected one.

Groups: S3, A4, S4, D8, Q8, SL(2,3), GL(2,3), A5, S5, SL(2,5),
GL(3,2) = PSL(2,7), PSL(2,11) and S3 x S3 for all their primes (centre
level), smaller lists for module computations, and for Sections 6.5-6.6
also PSL(2,8), PSL(2,13), D18, C7:C3, C5:C4, C3:C8, C2 x S3, V4 x C3,
V4 x S3, A4 x C3, A4 x S3, C3 x A4, C3 x A5, D8 x S3, SL(2,7) and the
library tables of A5, L3(2), L2(q), A6, A7, M11, M12, J1, U3(3), S5.

Checked here (by section):

6.1 (pp. 201-204)
  * p. 201: the block idempotents are orthogonal idempotents with sum 1,
    each primitive in Z(kG) (Z(kG)e = ke + a nilpotent ideal, the
    complement being the kernel of the central character omega_B, which is
    an algebra map and the same for all characters of the block): 13
    groups, all primes dividing their orders (30 pairs (G, p)).
  * Proposition 6.1.2 (prop:defect-group-transfer): e lies in (kG)^G_H iff
    H contains a conjugate of D, for every subgroup class H; D is a
    p-group of order p^(defect) (defect computed from the characters).
    Proposition 6.1.1 (prop:defect-group-sylow-intersection): D = S cap gS.
    Example p. 203: the principal block has Sylow defect groups.
  * Corollary 6.1.3 (cor:defect-groups-lift) over O = Z_(p) for the blocks
    with rational idempotent: e^ in OG reduces to e, lies in (OG)^G_D and
    not in (OG)^G_D' for D' < D of index p.  The transfer formula used
    (coefficient |G:H||x^H|/|x^G|) is checked against the definition.
6.2 (pp. 204-207)
  * Lemma 6.2.1 (lem:brauer-decomposition) (i), (ii), the ideal property,
    the inclusion (ii) in (i); Definition 6.2.3: Br_D is multiplicative on
    (kG)^D; for all p-subgroups of S4 (p = 2, 3), A5, GL(3,2), S5 (p = 2),
    SL(2,3), S3 x S3.
  * Proposition 6.2.2 (prop:normal-p-subgroup-idempotents) for every normal
    p-subgroup of 9 pairs (G, p); the corrected step of the proof (Lemma
    6.2.1 (ii): Z(kG) = (kC_G(D))^G + a nilpotent ideal, e = a^(p^n)); the
    printed step "every idempotent in (kG)^D lies in kC_G(D)" is refuted:
    S3 x S3, p = 3, D = C3 x 1, f = (1 + x)(1 + s)/2 (1 - x) with x the
    D-orbit sum of a non-central element.
  * Lemma 6.2.4 (lem:defect-group-brauer-map) for all blocks and all
    p-subgroups; the author's correction (kernel sum_(D'<D) (kG)^G_D'),
    the printed (kG)^G_D refuted.  Lemma 6.2.5 (lem:brauer-transfer): the
    square commutes on all D-orbit sums, the bottom map is onto, the
    Mackey formula with the conjugate gxg^-1 (author's correction), the
    printed product g.x refuted.  Theorem 6.2.6 (th:brauer-first-main) for
    all p-subgroups D of the 30 pairs; the Brauer correspondent b^G is
    well defined for D C_G(D) <= H <= N_G(D).  Lemma 6.2.7
    (lem:alperin-brauer-correspondence) by MeatAxe on k(H x H)-modules
    (S4 for p = 2, 3; A5 for p = 2, 5).
6.3 (pp. 207-208)
  * Theorem 6.3.1 (th:nagao): for M = e.k[G/H] (blocks e, several H),
    every p-subgroup D != 1 and K = C_G(D), N_G(D): Br_D(e) acts as an
    idempotent commuting with N_G(D), and every indecomposable summand of
    M' = (1 - Br_D(e)).M down_K is projective relative to some Q with
    D not <= Q <= K (Higman); the display of the proof, read for the
    N_G(D)-module (1 - Br_D(e)).M down_N_G(D) whose restriction to K is
    M', and the inclusion obtained on restricting to K = C_G(D); a control
    shows that summands of Br_D(e).M do fail the test (S4, A5, S5,
    GL(3,2)).  Corollaries 6.3.2, 6.3.3 (summands of e.k[G/D] with vertex
    D and their Green correspondents), 6.3.4 (defect zero, with all simple
    modules from the MeatAxe), 6.3.5 (a non-cyclic p-group has a quotient
    Z/p x Z/p, all groups of orders 2^n <= 64, 3^n <= 81, 5^n <= 125;
    k(N_G(D)/D) meets every block of k N_G(D)).
6.4 (pp. 208-212)
  * Theorem 6.4.1 (th:clifford-blocks) (i)-(v) for all normal subgroups of
    S4, S5, GL(2,3), S3 x S3, C3 x S3 and all p; (iii) as dim f.kG =
    n^2 dim e.kT and as the matrix units g1 x g2^-1 with x in e.kT (the
    printed "x in b^T" corrected: e.kT can be a sum of two blocks, C3 x S3,
    N = C3 x 1, p = 2).  The final statement holds for B the only block
    covering b (corrected statement) and for the blocks of largest defect
    covering b (Curtis-Reiner, Methods II, (61.5)); the printed statement
    for every covering block is refuted (N = 1: S3 and A5 at p = 2; also
    GL(2,3), S3 x S3).
  * Lemma 6.4.2 (lem:central-p-subgroup-blocks) for D8, Q8, SL(2,3),
    SL(2,5), SL(2,7) (p = 2, Q = Z(G)_2), C3 x A4 (p = 3) and D8 x S3
    (Q = D8): the bijection of blocks and of defect groups D <-> D/Q, the
    corrected proof (p-regular class sums map onto p-regular class sums;
    the block idempotents of kG/Q are supported on p-regular classes
    (Osima); Br_(D/Q)(pi(e)) = pi(Br_D(e)) != 0); the printed claims that
    pi maps Z(kC_G(Q)) onto Z(kC_G(Q)/Z(Q)) and (kG)^G_D onto
    (kG/Q)^(G/Q)_(D/Q) are refuted (dimensions 1 < 4 for D8 and Q8, ...);
    the second holds for D = Q.
  * Theorem 6.4.3 (th:brauer-first-main-extended): the four sets have equal
    sizes and b -> b^G is injective with values of defect D, all
    p-subgroups D of the groups of order <= 200 above.  Proposition 6.4.4
    (prop:normal-defect-matrix-ring): SL(2,5) (p = 2), C3 x A5 (p = 3),
    D8 x S3 (p = 2): one simple module, dim B = n^2 |D|, P_S down_D free of
    rank n, dim End(P_S) = |D|.  Theorem 6.4.5 (th:brauer-third-main) for
    all D, H, b as in the statement.
6.5 (pp. 212-218)
  * p. 212: e | |N_G(Q) : C_G(Q)| | p - 1, the blocks b1 of C_G(Q) form one
    N_G(Q)-class; Theorem 6.5.5 (th:cyclic-defect-quiver): l(B) = e (the
    rank of the characters of B on p-regular classes) and k(B) = e +
    (|D| - 1)/e, for 35 blocks of cyclic defect in 16 groups.  For 47
    blocks of the character table library: decomposition matrix of a
    Brauer tree with e edges and exceptional multiplicity (p^n - 1)/e,
    e | p - 1, Cartan matrix of the tree, determinant p^n.
  * Propositions 6.5.3, 6.5.4 (prop:cyclic-inertial-index-one,
    prop:cyclic-defect-normal) and Lemma 6.5.2 (lem:uniserial-
    indecomposables) by the MeatAxe for 11 pairs (A4, SL(2,3), C9, S3,
    D18, C7:C3, C5:C4, C3:C8, S4, A5 at 3 and 5): e simple modules, P_j
    uniserial of length p^n with layers S_(i+j), the e.p^n quotients
    P_j/Rad^i(P_j) distinct indecomposables; the layers (g - 1)^j kG /
    (g - 1)^(j+1) kG = k[G/Q] of the proof of 6.5.3; biserial projectives
    for cyclic blocks with Q not normal (A5, S4, GL(3,2)).
  * Proof of Theorem 6.5.5: det(I + mJ) and the star with an exceptional
    leaf (e, m <= 10); all trees with e <= 7 edges (47 trees), every
    exceptional vertex, m <= 6: det C = em + 1, the block form with one
    overlap entry and the expansion det C = det X det Y0 + det X0 det Y -
    z det X0 det Y0 at every edge with no end of valency one; with the
    exceptional vertex in L0 (corrected labelling) z = m + 1 if it is the
    left-hand vertex of E and z = 2 otherwise, and the four determinants
    used; the printed order "2 or m + 1" and the labelling "lies in L"
    (exceptional vertex the right-hand end of E) are refuted; the displays
    as identities in Q[l, r, m]: the z = 2 display and the corrected
    (l - 1) display, the printed (l + 1) refuted (difference
    -2m(m + 1)r); det(I + ((p^n - 1)/e)J) = p^n.
6.6 (pp. 218-224)
  * |Aut(V4)| = 6, e in {1, 3}.  Theorem 6.6.1 (th:klein-four-inertial-
    index-one) for V4 x C3, V4 x S3, C2 x S3 (D not normal), S3 x S3: one
    simple module, Rad(P_S)/Soc(P_S) = S + S, End(P_S) = kV4, dim B =
    4n^2.  Theorem 6.6.2 (th:klein-four-normal-inertial-index-three) for
    A4, A4 x C3, A4 x S3: three simples of one dimension n, dim B = 12n^2,
    Rad(P_j)/Soc(P_j) = S_(j-1) + S_(j+1); among the hearts invariant under
    S_j -> S_(j+1) only this one gives a symmetric Cartan matrix of 2-power
    determinant in one block (the printed "the determinant ... is a power
    of two ... leaves only one possibility" is refuted: 4I and 2I + 2P
    also have 2-power determinant); the quiver of p. 220 with the printed
    relations gives a 12-dimensional associative algebra, symmetric iff
    mu1 mu2 mu3 = 1 (27 triples over GF(4)), isomorphic to kA4 by an
    explicit map.  Theorem 6.6.3 (th:klein-four-inertial-index-three) (ii)
    for B_0(kA5): dimensions, the three hearts as printed, Cartan matrix
    and determinant 4, Ext-quiver, the 2-dimensional simple module
    restricted to V4 indecomposable with Omega(M) = M, and V4 a vertex of
    every simple module (Knoerr, Remark p. 223); the principal 2-blocks of
    PSL(2, q), q = 5, 11, 13, 19, 27, 29 have the Cartan matrix of kA4 or
    of B_0(kA5), and both occur.

Not established: none of the general theorems is proved here.  Every check
concerns the listed groups, primes, fields, modules, trees and parameter
ranges only.  The stable Auslander-Reiten quivers of 6.5-6.6, the
statements about infinitely many indecomposables (Corollary 6.3.5,
Proposition 6.5.3) and the Morita equivalences beyond the dimension,
Loewy and endomorphism-ring data stated above are not computed.  Block
idempotents and ordinary characters come from GAP (PrimeBlocks,
character tables); the decomposition matrices of 6.5-6.6 come from the
GAP character table library.  Nothing here compares our Typst text with
the printed book.

Run with:  sage -python checks/sage/chapter-6.py
"""


import itertools
import random

from sage.all import GF, QQ, ZZ, Integer, PolynomialRing, libgap

# Character tables and Brauer tables need GAP's table library; the
# SageMath container does not load it by default.
assert libgap.LoadPackage('ctbllib')

SCOPE = 'chapter-6'
COUNT = [0]
random.seed(20261104)


def check(cond, what):
    """One check of a statement of the book; fails loudly."""
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    """The printed reading, kept beside the corrected one: it must fail."""
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(s):
    return libgap.eval(s)


# ===========================================================================
# Linear algebra over a finite field (row reduction in Python; no BLAS)
# ===========================================================================


class Span:
    """Row space of vectors (lists) over a field, kept in echelon form."""

    def __init__(self, F, n, vecs=()):
        self.F, self.n = F, n
        self.rows = {}           # pivot -> row (pivot entry 1)
        for v in vecs:
            self.add(v)

    def reduce(self, v):
        v = [self.F(x) for x in v]
        for piv, row in self.rows.items():
            c = v[piv]
            if c:
                for j in range(self.n):
                    if row[j]:
                        v[j] -= c * row[j]
        return v

    def add(self, v):
        v = self.reduce(v)
        for piv in range(self.n):
            if v[piv]:
                c = ~v[piv]
                v = [c * x for x in v]
                for p2, row in list(self.rows.items()):
                    d = row[piv]
                    if d:
                        self.rows[p2] = [a - d * b for a, b in zip(row, v)]
                self.rows[piv] = v
                return True
        return False

    def __contains__(self, v):
        return not any(self.reduce(v))

    def dim(self):
        return len(self.rows)


def kernel(F, cols, n):
    """Kernel of the linear map with the given column images (vectors of
    length n), as a list of coefficient vectors."""
    m = len(cols)
    # augmented rows [image | identity]
    rows = [list(cols[i]) + [F(int(i == j)) for j in range(m)]
            for i in range(m)]
    piv_rows = []
    for c in range(n):
        r = next((i for i, row in enumerate(rows)
                  if i not in piv_rows and row[c]), None)
        if r is None:
            continue
        piv_rows.append(r)
        inv = ~rows[r][c]
        rows[r] = [inv * x for x in rows[r]]
        for i in range(m):
            if i != r and rows[i][c]:
                d = rows[i][c]
                rows[i] = [a - d * b for a, b in zip(rows[i], rows[r])]
    return [row[n:] for i, row in enumerate(rows) if i not in piv_rows]


# ===========================================================================
# Finite groups as multiplication tables (from GAP permutation groups)
# ===========================================================================


class Grp:
    """A finite group with elements numbered 0..n-1 (0 = identity); the
    product is that of GAP (apply the left factor first)."""

    def __init__(self, G, name, deg=None):
        if not G.IsPermGroup():
            G = libgap.eval(
                'G -> Image(SmallerDegreePermutationRepresentation('
                'Image(IsomorphismPermGroup(G))))')(G)
        self.G, self.name = G, name
        self.deg = deg or max(int(G.LargestMovedPoint()), 1)
        L = gap('function(g, d) return List(AsList(g), x -> ListPerm(x, d)); '
                'end')(G, self.deg)
        els = [tuple(int(i) - 1 for i in x) for x in L]
        ident = tuple(range(self.deg))
        els.remove(ident)
        els = [ident] + els
        self.els = els
        self.idx = {t: i for i, t in enumerate(els)}
        self.n = n = len(els)
        self.mul = [[self.idx[tuple([b[i] for i in a])] for b in els]
                    for a in els]
        self.inv = [row.index(0) for row in self.mul]
        self.all = tuple(range(n))
        # conjugacy classes (orbits of x -> g x g^-1)
        self.cls_of = [None] * n
        self.classes = []
        for x in range(n):
            if self.cls_of[x] is None:
                orb = sorted({self.conj(g, x) for g in range(n)})
                for y in orb:
                    self.cls_of[y] = len(self.classes)
                self.classes.append(orb)
        self.r = len(self.classes)
        self.order = [self.order_of(g) for g in range(n)]
        self.exponent = int(G.Exponent())

    # -- elements
    def conj(self, g, x):
        """g x g^-1."""
        return self.mul[self.mul[g][x]][self.inv[g]]

    def order_of(self, g):
        k, x = 1, g
        while x:
            x = self.mul[x][g]
            k += 1
        return k

    def key(self, gapel):
        return self.idx[tuple(int(i) - 1 for i in
                              libgap.ListPerm(gapel, self.deg))]

    def gap_el(self, i):
        return libgap.PermList([j + 1 for j in self.els[i]])

    # -- subgroups as sorted tuples of indices
    def closure(self, gens):
        S, frontier = {0}, [0]
        while frontier:
            new = []
            for a in frontier:
                for s in gens:
                    b = self.mul[a][s]
                    if b not in S:
                        S.add(b)
                        new.append(b)
            frontier = new
        return tuple(sorted(S))

    def from_gap(self, H):
        return tuple(sorted(self.key(h) for h in H.AsList()))

    def to_gap(self, H):
        return libgap.Group([self.gap_el(h) for h in H] or
                            [self.gap_el(0)])

    def conj_sub(self, g, H):
        return tuple(sorted(self.conj(g, h) for h in H))

    def centralizer(self, H):
        return tuple(x for x in self.all
                     if all(self.mul[x][h] == self.mul[h][x] for h in H))

    def normalizer(self, H):
        S = set(H)
        return tuple(x for x in self.all
                     if all(self.conj(x, h) in S for h in H))

    def is_conj_sub(self, A, B):
        """Some G-conjugate of A lies in B."""
        SB = set(B)
        return any(all(self.conj(g, a) in SB for a in A) for g in self.all)

    def are_conj(self, A, B):
        return len(A) == len(B) and self.is_conj_sub(A, B)

    def subgroup_classes(self):
        """Representatives of the conjugacy classes of subgroups (GAP)."""
        if not hasattr(self, '_subs'):
            cc = self.G.ConjugacyClassesSubgroups()
            self._subs = [self.from_gap(c.Representative()) for c in cc]
        return self._subs

    def p_subgroup_classes(self, p):
        return [H for H in self.subgroup_classes()
                if Integer(len(H)).is_power_of(p) or len(H) == 1]

    def sylow(self, p):
        return self.from_gap(self.G.SylowSubgroup(p))

    def is_normal(self, H):
        return len(self.normalizer(H)) == self.n

    def orbits(self, H, X=None):
        """Orbits of H on X (default G) under conjugation."""
        X = self.all if X is None else X
        seen, orbs = set(), []
        for x in X:
            if x in seen:
                continue
            o = sorted({self.conj(h, x) for h in H})
            seen.update(o)
            orbs.append(o)
        return orbs


def is_p_group(H, p):
    return len(H) == 1 or Integer(len(H)).is_power_of(p)


def p_part(n, p):
    return p ** Integer(n).valuation(p)


# ===========================================================================
# Reduction modulo a prime above p, and block idempotents
# ===========================================================================


class Modular:
    """The p-modular reduction Z[zeta_n]_(p) -> GF(q) sending zeta_n to a
    primitive n'-th root of unity w (n' the p'-part of n); GF(q) contains
    the n'-th roots of unity, so it is a splitting field (Brauer)."""

    def __init__(self, n, p):
        self.n, self.p = n, p
        npr = n // p_part(n, p)
        f = 1
        while (p ** f - 1) % npr:
            f += 1
        self.q = p ** f
        self.F = GF(self.q, 'a') if f > 1 else GF(p)
        z = self.F.multiplicative_generator()
        self.w = z ** ((self.q - 1) // npr)
        self.wpow = [self.w ** j for j in range(n)]

    def red(self, x):
        cs = libgap.CoeffsCyc(x, self.n)
        s = self.F(0)
        for j, c in enumerate(cs):
            c = QQ(c.sage())
            if c:
                assert c.denominator() % self.p, 'not p-integral'
                s += self.F(c) * self.wpow[j]
        return s


class Blocks:
    """Centre Z(F G) on the class sums, the p-blocks (ordinary characters
    distributed by GAP's PrimeBlocks) and their idempotents over F."""

    def __init__(self, Gr, p, mod=None):
        self.Gr, self.p = Gr, p
        self.mod = mod or Modular(Gr.exponent, p)
        self.F = F = self.mod.F
        r = Gr.r
        # structure constants a[i][j][k] = coefficient of K_k in K_i K_j
        cnt = [[[0] * r for _ in range(r)] for _ in range(r)]
        cls = Gr.cls_of
        for i, Ki in enumerate(Gr.classes):
            for j, Kj in enumerate(Gr.classes):
                row = cnt[i][j]
                for x in Ki:
                    mx = Gr.mul[x]
                    for y in Kj:
                        row[cls[mx[y]]] += 1
        self.sc = [[[F(cnt[i][j][k] // len(Gr.classes[k]))
                     for k in range(r)] for j in range(r)] for i in range(r)]
        self.sc_int = [[[cnt[i][j][k] // len(Gr.classes[k])
                         for k in range(r)] for j in range(r)]
                       for i in range(r)]
        # ordinary characters on our classes
        tbl = Gr.G.CharacterTable()
        reps = [Gr.key(c.Representative())
                for c in tbl.ConjugacyClasses()]
        gcls = [cls[x] for x in reps]
        perm = [gcls.index(k) for k in range(r)]   # our class -> GAP's
        self.irr = [[chi[perm[k]] for k in range(r)] for chi in tbl.Irr()]
        pb = libgap.PrimeBlocks(tbl, p)
        blk = [int(b) - 1 for b in pb['block']]
        self.nblocks = max(blk) + 1
        self.block_chars = [[i for i, b in enumerate(blk) if b == B]
                            for B in range(self.nblocks)]
        self.defect = [int(d) for d in pb['defect']]
        inv_cls = [cls[Gr.inv[K[0]]] for K in Gr.classes]
        n = Gr.n
        self.idem_cyc = []
        self.idems = []
        for chars in self.block_chars:
            c = [sum((self.irr[i][0] * self.irr[i][inv_cls[k]]
                      for i in chars), libgap(0)) / n for k in range(r)]
            self.idem_cyc.append(c)
            self.idems.append([self.mod.red(x) for x in c])
        triv = next(i for i, chi in enumerate(self.irr)
                    if all(x == 1 for x in chi))
        self.principal = blk[triv]

    # -- the commutative algebra Z(FG) in class-sum coordinates
    def zmul(self, u, v):
        F, r, sc = self.F, self.Gr.r, self.sc
        w = [F(0)] * r
        for i in range(r):
            if not u[i]:
                continue
            for j in range(r):
                if not v[j]:
                    continue
                c = u[i] * v[j]
                row = sc[i][j]
                for k in range(r):
                    if row[k]:
                        w[k] += c * row[k]
        return w

    def one(self):
        return [self.F(int(k == self.Gr.cls_of[0])) for k in range(self.Gr.r)]

    def omega(self, chi):
        """Central character of chi reduced mod p (on class sums)."""
        Gr = self.Gr
        return [self.mod.red(len(Gr.classes[k]) * self.irr[chi][k] /
                             self.irr[chi][0]) for k in range(Gr.r)]

    def to_group_algebra(self, z):
        """Class-sum coordinates -> dict on elements of G."""
        d = {}
        for k, K in enumerate(self.Gr.classes):
            if z[k]:
                for x in K:
                    d[x] = z[k]
        return d


# ===========================================================================
# Transfer images in Z(kG), defect groups (Proposition 6.1.2)
# ===========================================================================


def transfer_classes(Gr, H, p, orbs=None):
    """For each class K of G the least p-adic valuation over x in K of the
    coefficient |G:H| |x^H| / |K| of K in Tr_H^G (H-orbit sum of x); the
    image (kG)^G_H is spanned by the K with valuation 0 (Definition 3.6.2,
    the transfer being computed on the basis of H-orbit sums)."""
    orbs = Gr.orbits(H) if orbs is None else orbs
    val = [None] * Gr.r
    idx = Gr.n // len(H)
    for o in orbs:
        k = Gr.cls_of[o[0]]
        v = Integer(idx * len(o) // len(Gr.classes[k])).valuation(p)
        assert (idx * len(o)) % len(Gr.classes[k]) == 0
        if val[k] is None or v < val[k]:
            val[k] = v
    return val


def transfer_direct(Gr, H, x):
    """Tr_H^G of the H-orbit sum of x, summed over coset representatives
    of G/H (integer coefficients)."""
    reps, seen = [], set()
    for g in Gr.all:
        if g in seen:
            continue
        reps.append(g)
        seen.update(Gr.mul[g][h] for h in H)
    orb = {Gr.conj(h, x) for h in H}
    d = {}
    for g in reps:
        for y in orb:
            z = Gr.conj(g, y)
            d[z] = d.get(z, 0) + 1
    return d


def in_transfer(e, val):
    """e (class coordinates over k) lies in (kG)^G_H."""
    return all(not c or val[k] == 0 for k, c in enumerate(e))


def br_support(Gr, e, C):
    """Br_P(e) for e in Z(kG) (class coordinates) as a dict on C = C_G(P)."""
    return {x: e[Gr.cls_of[x]] for x in C if e[Gr.cls_of[x]]}


GAP_CODE = r"""
B6Gens := function(K)
  if IsTrivial(K) then return [One(K)]; fi;
  return GeneratorsOfGroup(K);
end;

B6Hom := function(G, gens, mats)
  return GroupHomomorphismByImagesNC(G, Group(mats), gens, mats);
end;

# the module of K on the row space spanned by basis (rows), as generator
# matrices for B6Gens(K)
B6Sub := function(hom, K, basis)
  return List(B6Gens(K),
              k -> List(basis, v -> SolutionMat(basis, v * Image(hom, k))));
end;

B6Module := function(K, mats, F)
  if Length(mats) = 0 then return fail; fi;
  return GModuleByMats(mats, F);
end;

# is the identity of the K-module (gens -> mats) in Tr_Q^K(End_kQ(X))?
B6IdInTransfer := function(K, mats, Q, F)
  local gens, hom, n, mq, E, imgs, trans, Mt, phi, s, t;
  gens := B6Gens(K);
  hom := B6Hom(K, gens, mats);
  n := Length(mats[1]);
  mq := GModuleByMats(List(B6Gens(Q), q -> Image(hom, q)), n, F);
  E := MTX.BasisModuleEndomorphisms(mq);
  trans := RightTransversal(K, Q);
  Mt := List(trans, t -> Image(hom, t));
  imgs := [];
  for phi in E do
    s := Sum(Mt, t -> t^-1 * phi * t);
    Add(imgs, Concatenation(s));
  od;
  if imgs = [] then return false; fi;
  return SolutionMat(imgs, Concatenation(IdentityMat(n, F))) <> fail;
end;

# span (flattened) of sum_Q Tr_Q^K(End_kQ(X)) for a list of subgroups Q
B6TransferSpan := function(K, mats, Qs, F)
  local gens, hom, n, mq, E, imgs, trans, Mt, phi, Q;
  gens := B6Gens(K);
  hom := B6Hom(K, gens, mats);
  n := Length(mats[1]);
  imgs := [];
  for Q in Qs do
    mq := GModuleByMats(List(B6Gens(Q), q -> Image(hom, q)), n, F);
    E := MTX.BasisModuleEndomorphisms(mq);
    trans := RightTransversal(K, Q);
    Mt := List(trans, t -> Image(hom, t));
    for phi in E do
      Add(imgs, Concatenation(Sum(Mt, t -> t^-1 * phi * t)));
    od;
  od;
  return imgs;
end;

B6InSpan := function(imgs, v)
  if imgs = [] then return IsZero(v); fi;
  return SolutionMat(imgs, v) <> fail;
end;

# matrix of the group algebra element sum c_x x (list of [x, c])
B6AlgElt := function(hom, elt, n, F)
  local m, pr;
  m := NullMat(n, n, F);
  for pr in elt do
    m := m + pr[2] * Image(hom, pr[1]);
  od;
  return m;
end;

# radical layers of a module: list of semisimple modules
B6RadicalLayers := function(M)
  local layers, cur, rad, q;
  layers := [];
  cur := M;
  while MTX.Dimension(cur) > 0 do
    rad := MTX.BasisRadical(cur);
    q := MTX.InducedActionFactorModule(cur, rad);
    Add(layers, q);
    if Length(rad) = 0 then break; fi;
    cur := MTX.InducedActionSubmodule(cur, rad);
  od;
  return layers;
end;

# composition factors of a module as positions in a list of simples
B6FactorPositions := function(M, simples)
  local cf;
  cf := MTX.CompositionFactors(M);
  return SortedList(List(cf, c -> PositionProperty(simples,
                                    s -> MTX.IsEquivalent(s, c))));
end;

B6IsSummandIso := function(M, X)
  local d;
  d := MTX.Indecomposition(M);
  return ForAny(d, s -> MTX.Dimension(s[2]) = MTX.Dimension(X)
                        and MTX.IsomorphismModules(s[2], X) <> fail);
end;

B6BimoduleOfBlock := function(X, H, elist, F)
  local els, n, gH, mats, E, W, pr, perm;
  els := AsSSortedList(X);
  n := Length(els);
  perm := f -> PermutationMat(PermList(List(els,
                 x -> PositionSorted(els, f(x)))), n, F);
  gH := B6Gens(H);
  mats := Concatenation(List(gH, h -> perm(x -> h^-1 * x)),
                        List(gH, h -> perm(x -> x * h)));
  E := NullMat(n, n, F);
  for pr in elist do
    E := E + pr[2] * perm(x -> x * pr[1]);
  od;
  W := BaseMat(E);
  return GModuleByMats(List(mats, m -> List(W, w -> SolutionMat(W, w * m))),
                       F);
end;

B6RegularMats := function(G, gens, F)
  local els, n;
  els := AsSSortedList(G);
  n := Length(els);
  return List(gens, g -> PermutationMat(PermList(List(els,
                 x -> PositionSorted(els, x * g))), n, F));
end;
"""

_DONE = [False]


def init_gap():
    if not _DONE[0]:
        for chunk in GAP_CODE.split('\nend;\n'):
            if chunk.strip():
                libgap.eval(chunk + '\nend;')
        _DONE[0] = True


GROUPS_61 = [
    ('SymmetricGroup(3)', 'S3', [2, 3]),
    ('AlternatingGroup(4)', 'A4', [2, 3]),
    ('SymmetricGroup(4)', 'S4', [2, 3]),
    ('DihedralGroup(IsPermGroup, 8)', 'D8', [2]),
    ('QuaternionGroup(IsPermGroup, 8)', 'Q8', [2]),
    ('SL(2, 3)', 'SL(2,3)', [2, 3]),
    ('GL(2, 3)', 'GL(2,3)', [2, 3]),
    ('AlternatingGroup(5)', 'A5', [2, 3, 5]),
    ('SymmetricGroup(5)', 'S5', [2, 3, 5]),
    ('SL(2, 5)', 'SL(2,5)', [2, 3, 5]),
    ('PSL(3, 2)', 'GL(3,2)', [2, 3, 7]),
    ('PSL(2, 11)', 'PSL(2,11)', [2, 3, 5, 11]),
    ('DirectProduct(SymmetricGroup(3), SymmetricGroup(3))', 'S3xS3', [2, 3]),
]

_GROUP_CACHE = {}
_BLOCK_CACHE = {}


def group(gapname, name):
    if gapname not in _GROUP_CACHE:
        _GROUP_CACHE[gapname] = Grp(gap(gapname), name)
    return _GROUP_CACHE[gapname]


def blocks(Gr, p):
    key = (Gr.name, p)
    if key not in _BLOCK_CACHE:
        _BLOCK_CACHE[key] = Blocks(Gr, p)
    return _BLOCK_CACHE[key]


def is_nilpotent(B, z):
    r = B.Gr.r
    t = 1
    while t < r + 1:
        z = B.zmul(z, z)
        t *= 2
    return not any(z)


def defect_groups(Gr, B, subs=None):
    """For each block: the subgroup classes H with e in (kG)^G_H and a
    minimal one D (Proposition 6.1.2)."""
    subs = Gr.subgroup_classes() if subs is None else subs
    vals = {H: transfer_classes(Gr, H, B.p) for H in subs}
    res = []
    for e in B.idems:
        S = [H for H in subs if in_transfer(e, vals[H])]
        D = min(S, key=len)
        res.append((D, S))
    return res, vals


def section_6_1():
    # The transfer formula used below, against the definition (sum over
    # coset representatives), for all subgroups of S4 and A5.
    for gname, name in [('SymmetricGroup(4)', 'S4'),
                        ('AlternatingGroup(5)', 'A5')]:
        Gr = group(gname, name)
        ok = True
        for H in Gr.subgroup_classes():
            for o in Gr.orbits(H):
                d = transfer_direct(Gr, H, o[0])
                K = Gr.classes[Gr.cls_of[o[0]]]
                c = (Gr.n // len(H)) * len(o) // len(K)
                ok = ok and set(d) == set(K) and all(v == c
                                                     for v in d.values())
        check(ok, 'Def. 3.6.2: Tr_H^G of an H-orbit sum of x is '
              '|G:H| |x^H| / |x^G| times the class sum (all subgroups of '
              '%s)' % name)

    for gname, name, primes in GROUPS_61:
        Gr = group(gname, name)
        S_all = Gr.subgroup_classes()
        for p in primes:
            B = blocks(Gr, p)
            one = B.one()
            F = B.F
            tot = [F(0)] * Gr.r
            for i, e in enumerate(B.idems):
                check(B.zmul(e, e) == e,
                      'p. 201: block idempotent e is idempotent (%s, p=%d)'
                      % (name, p))
                for j, f in enumerate(B.idems):
                    if j != i:
                        check(not any(B.zmul(e, f)),
                              'p. 201: block idempotents orthogonal (%s, '
                              'p=%d)' % (name, p))
                tot = [a + b for a, b in zip(tot, e)]
            check(tot == one, 'p. 201: 1 = e_1 + ... + e_s (%s, p=%d)'
                  % (name, p))
            # primitivity: Z(kG) e = k e + N with N a nilpotent ideal
            for i, (e, chars) in enumerate(zip(B.idems, B.block_chars)):
                om = B.omega(chars[0])
                for chi in chars[1:]:
                    check(B.omega(chi) == om,
                          'p. 201: one central character mod p per block '
                          '(%s, p=%d)' % (name, p))
                ok = all(om[a] * om[b] == sum(B.sc[a][b][c] * om[c]
                                              for c in range(Gr.r))
                         for a in range(Gr.r) for b in range(Gr.r))
                check(ok, 'omega_B is an algebra map Z(kG) -> k (%s, p=%d)'
                      % (name, p))
                ev = lambda z: sum(a * b for a, b in zip(om, z))
                check(ev(e) == 1, 'omega_B(e_B) = 1 (%s)' % name)
                nil = True
                for k in range(Gr.r):
                    K = [F(int(j == k)) for j in range(Gr.r)]
                    z = B.zmul(K, e)
                    z = [a - ev(K) * b for a, b in zip(z, e)]
                    nil = nil and is_nilpotent(B, z)
                check(nil, 'p. 201: e_B primitive in Z(kG): Z(kG)e_B = '
                      'k e_B + (nilpotent ideal) (%s, p=%d, block %d)'
                      % (name, p, i))
            # defect groups by Proposition 6.1.2
            dg, vals = defect_groups(Gr, B)
            Syl = Gr.sylow(p)
            for i, (D, S) in enumerate(dg):
                check(is_p_group(D, p),
                      'Prop. 6.1.2: the minimal H with e in (kG)^G_H is a '
                      'p-group (%s, p=%d)' % (name, p))
                check(all((H in S) == Gr.is_conj_sub(D, H) for H in S_all),
                      'Prop. 6.1.2: e in (kG)^G_H iff H contains a '
                      'conjugate of D (%s, p=%d, all %d subgroup classes)'
                      % (name, p, len(S_all)))
                check(len(D) == p ** B.defect[i],
                      'Defect of the block = log_p |D| agrees with the '
                      'character-theoretic defect (GAP PrimeBlocks) '
                      '(%s, p=%d)' % (name, p))
                check(any(Gr.are_conj(D, tuple(sorted(
                    set(Syl) & set(Gr.conj_sub(g, Syl))))) for g in Gr.all),
                    'Prop. 6.1.1 (Green): D = S cap gS for a Sylow S '
                    '(%s, p=%d)' % (name, p))
            D0 = dg[B.principal][0]
            check(len(D0) == len(Syl),
                  'Example p. 203: the principal block has the Sylow '
                  'p-subgroups as defect groups (%s, p=%d)' % (name, p))
            check(len(dg) == B.nblocks, 'block count')
            corollary_6_1_3(Gr, B, dg)


def corollary_6_1_3(Gr, B, dg):
    """Over O = Z_(p) (blocks with rational idempotent only): e^ lies in
    (OG)^G_D and not in (OG)^G_D' for D' < D of index p."""
    p = B.p
    for i, (D, S) in enumerate(dg):
        cyc = B.idem_cyc[i]
        if not all(libgap.IsRat(c) for c in cyc):
            continue
        coef = [QQ(c.sage()) for c in cyc]
        check(all(c.denominator() % p for c in coef),
              'Cor. 6.1.3: the block idempotent e^ lies in OG (%s, p=%d)'
              % (Gr.name, p))
        check([B.F(c) for c in coef] == B.idems[i],
              'Cor. 6.1.3: e^ reduces to e (%s, p=%d)' % (Gr.name, p))
        val = transfer_classes(Gr, D, p)
        check(all(c == 0 or c.valuation(p) >= val[k]
                  for k, c in enumerate(coef)),
              'Cor. 6.1.3: e^ in (OG)^G_D (%s, p=%d, |D|=%d)'
              % (Gr.name, p, len(D)))
        if len(D) > 1:
            Dg = Gr.to_gap(D)
            for M in Dg.MaximalSubgroups():
                Dp = Gr.from_gap(M)
                v2 = transfer_classes(Gr, Dp, p)
                check(any(c != 0 and c.valuation(p) < v2[k]
                          for k, c in enumerate(coef)),
                      'Cor. 6.1.3: e^ not in (OG)^G_D\' for D\' < D '
                      '(%s, p=%d)' % (Gr.name, p))


def ga_mul(Gr, a, b):
    d = {}
    for x, c in a.items():
        mx = Gr.mul[x]
        for y, e in b.items():
            z = mx[y]
            d[z] = d.get(z, 0) + c * e
    return {z: c for z, c in d.items() if c}


def coset_reps(Gr, H, ambient=None):
    reps, seen = [], set()
    for g in (Gr.all if ambient is None else ambient):
        if g in seen:
            continue
        reps.append(g)
        seen.update(Gr.mul[g][h] for h in H)
    return reps


def tr(Gr, H, K, a):
    """Tr_{H,K}(a) = sum over g in K/H of g a g^-1 (a a dict)."""
    d = {}
    for g in coset_reps(Gr, H, K):
        for x, c in a.items():
            z = Gr.conj(g, x)
            d[z] = d.get(z, 0) + c
    return {z: c for z, c in d.items() if c}


def orbit_vec(orbs, a, F):
    """Coordinates of an H-invariant element a on the orbit sums."""
    v = []
    for o in orbs:
        cs = {F(a.get(x, 0)) for x in o}
        assert len(cs) == 1, 'not invariant'
        v.append(cs.pop())
    return v


def subgroup(Gr, gapH, name):
    """A subgroup of Gr as its own Grp (same points) with the map to Gr."""
    Hr = Grp(gapH, name, deg=Gr.deg)
    Hr.to_G = [Gr.idx[t] for t in Hr.els]
    Hr.from_G = {g: i for i, g in enumerate(Hr.to_G)}
    return Hr


SUB_CACHE = {}


def sub_of(Gr, H, name):
    key = (Gr.name, H)
    if key not in SUB_CACHE:
        SUB_CACHE[key] = subgroup(Gr, Gr.to_gap(H), name)
    return SUB_CACHE[key]


def brauer_vec(Gr, e, C, Nr):
    """Br_D(e) (e in Z(kG), class coordinates) in the class coordinates of
    N = Nr (C = C_G(D) inside N); checks N-invariance."""
    d = br_support(Gr, e, C)
    F = e[0].parent()
    v = []
    for K in Nr.classes:
        cs = {d.get(Nr.to_G[x], F(0)) for x in K}
        assert len(cs) == 1
        v.append(cs.pop())
    return v


def lemma_6_2_1(Gr, p, D):
    F = GF(p)
    C = set(Gr.centralizer(D))
    orbs = Gr.orbits(D)
    pos = {x: i for i, o in enumerate(orbs) for x in o}
    proper = [Gr.from_gap(H) for H in Gr.to_gap(D).AllSubgroups()
              if int(H.Size()) < len(D)]
    span = Span(F, len(orbs))
    hit = [False] * len(orbs)
    for Dp in proper:
        for o in Gr.orbits(Dp):
            t = tr(Gr, Dp, D, {x: 1 for x in o})
            v = orbit_vec(orbs, t, F)
            for i, c in enumerate(v):
                if c:
                    hit[i] = True
            span.add(v)
    triv = [len(o) == 1 for o in orbs]
    check(all(len(o) == 1 for o in orbs if o[0] in C) and
          all(o[0] in C for o in orbs if len(o) == 1),
          'Lemma 6.2.1: the orbits of length one span kC_G(D)')
    check(all(h == (not t) for h, t in zip(hit, triv)) and
          span.dim() == triv.count(False),
          'Lemma 6.2.1 (i): sum_(D\' < D) (kG)^D_D\' is spanned by the '
          'orbit sums of length > 1 and meets kC_G(D) in zero (%s, p=%d, '
          '|D|=%d)' % (Gr.name, p, len(D)))
    # two-sided ideal of (kG)^D: products with random invariant elements
    ok = True
    for _ in range(3 if not all(triv) else 0):
        a = {}
        for o in orbs:
            c = F.random_element()
            for x in o:
                a[x] = c
        o = random.choice([o for o in orbs if len(o) > 1])
        t = {x: F(1) for x in o}
        for prod in (ga_mul(Gr, a, t), ga_mul(Gr, t, a)):
            v = orbit_vec(orbs, prod, F)
            ok = ok and all(not c for c, tt in zip(v, triv) if tt)
    check(ok, 'Lemma 6.2.1 (i): the right-hand summand is a two-sided '
          'ideal (random elements, %s, p=%d)' % (Gr.name, p))
    # (ii) over N_G(D)
    N = Gr.normalizer(D)
    Nr = sub_of(Gr, N, 'N')
    norbs = Gr.orbits(N)
    span2 = Span(F, len(norbs))
    hit2 = [False] * len(norbs)
    for Qn in Nr.subgroup_classes():
        Q = tuple(sorted(Nr.to_G[x] for x in Qn))
        if set(D) <= set(Q):
            continue
        for o in Gr.orbits(Q):
            t = tr(Gr, Q, N, {x: 1 for x in o})
            v = orbit_vec(norbs, t, F)
            for i, c in enumerate(v):
                if c:
                    hit2[i] = True
            span2.add(v)
    inC = [o[0] in C for o in norbs]
    check(all(all(x in C for x in o) == ic for o, ic in zip(norbs, inC)),
          'Lemma 6.2.1 (ii): N_G(D)-orbits lie inside or outside C_G(D)')
    check(all(h == (not ic) for h, ic in zip(hit2, inC)) and
          span2.dim() == inC.count(False),
          'Lemma 6.2.1 (ii): sum_(D not<= Q <= N_G(D)) (kG)^N_Q is spanned '
          'by the N-orbit sums outside C_G(D) (those on which D has no '
          'fixed points) and meets (kC_G(D))^N in zero (%s, p=%d, |D|=%d)'
          % (Gr.name, p, len(D)))
    check(all(all(len(orbs[pos[x]]) > 1 for x in o)
              for o, ic in zip(norbs, inC) if not ic),
          'Lemma 6.2.1: each summand in (ii) lies in the corresponding '
          'summand in (i)')
    # Definition 6.2.3: Br_D is a ring homomorphism on (kG)^D
    ok = True
    for _ in range(3):
        a, b = {}, {}
        for o in orbs:
            c1, c2 = F.random_element(), F.random_element()
            for x in o:
                a[x], b[x] = c1, c2
        br = lambda z: {x: c for x, c in z.items() if x in C and c}
        ok = ok and br(ga_mul(Gr, a, b)) == ga_mul(Gr, br(a), br(b))
    check(ok, 'Def. 6.2.3: Br_D(ab) = Br_D(a) Br_D(b) on (kG)^D (random '
          'elements, %s, p=%d, |D|=%d)' % (Gr.name, p, len(D)))


def prop_6_2_2():
    cases = [('SymmetricGroup(3)', 'S3', 3), ('AlternatingGroup(4)', 'A4', 2),
             ('SymmetricGroup(4)', 'S4', 2), ('SL(2, 3)', 'SL(2,3)', 2),
             ('GL(2, 3)', 'GL(2,3)', 2), ('SL(2, 5)', 'SL(2,5)', 2),
             ('DihedralGroup(IsPermGroup, 8)', 'D8', 2),
             ('DirectProduct(SymmetricGroup(3), SymmetricGroup(3))', 'S3xS3',
              3),
             ('DirectProduct(SymmetricGroup(3), SymmetricGroup(3))', 'S3xS3',
              2)]
    for gname, name, p in cases:
        Gr = group(gname, name)
        B = blocks(Gr, p)
        Ns = [Gr.from_gap(H) for H in Gr.G.NormalSubgroups()]
        for D in Ns:
            if len(D) == 1 or not is_p_group(D, p):
                continue
            C = set(Gr.centralizer(D))
            check(all(all(not c or Gr.classes[k][0] in C
                          for k, c in enumerate(e)) for e in B.idems),
                  'Prop. 6.2.2: every block idempotent lies in kC_G(D) '
                  '(%s, p=%d, D normal of order %d)' % (name, p, len(D)))
            if C <= set(D):
                check(B.nblocks == 1, 'Prop. 6.2.2: C_G(D) <= D gives one '
                      'block (%s, p=%d)' % (name, p))
            # corrected step: Z(kG) = (kC_G(D))^G + I, I nilpotent ideal
            out = [k for k in range(Gr.r) if Gr.classes[k][0] not in C]
            F = B.F
            unit = lambda k: [F(int(j == k)) for j in range(Gr.r)]
            ok = all(all(not B.zmul(unit(k), unit(j))[m]
                         for m in range(Gr.r) if m not in out)
                     for k in out for j in range(Gr.r))
            ok = ok and all(is_nilpotent(B, unit(k)) for k in out)
            check(ok, 'Prop. 6.2.2 (corrected proof): the class sums '
                  'outside C_G(D) span a nilpotent ideal of Z(kG) (%s, '
                  'p=%d)' % (name, p))
            for e in B.idems:
                a = [c if k not in out else F(0) for k, c in enumerate(e)]
                z = a
                for _ in range(8):
                    z = B.zmul(z, z) if p == 2 else _pow(B, z, p)
                check(z == e, 'Prop. 6.2.2 (corrected proof): e = a + i '
                      'with a in (kC_G(D))^G, i nilpotent, and e = '
                      'a^(p^n) (%s, p=%d)' % (name, p))
    # The printed intermediate claim "every idempotent in (kG)^D lies in
    # kC_G(D)" fails: S3 x S3, p = 3, D = C3 x 1.
    Gr = group('DirectProduct(SymmetricGroup(3), SymmetricGroup(3))',
               'S3xS3')
    F = GF(3)
    D = next(Gr.from_gap(H) for H in Gr.G.NormalSubgroups()
             if int(H.Size()) == 3 and
             len(Gr.centralizer(Gr.from_gap(H))) == 18)
    C = Gr.centralizer(D)
    s = next(x for x in C if Gr.order[x] == 2)
    a = {0: F(2), s: F(2)}                       # (1 + s)/2
    t = next(x for x in Gr.all if x not in set(C)
             and any(Gr.mul[x][s] != Gr.mul[s][x] for _ in [0]))
    xo = {y: F(1) for y in {Gr.conj(d, t) for d in D}}   # D-orbit sum
    u = {0: F(1)}
    for y, c in xo.items():
        u[y] = u.get(y, 0) + c
    uinv = {0: F(1)}
    for y, c in xo.items():
        uinv[y] = uinv.get(y, 0) - c
    check(ga_mul(Gr, xo, xo) == {}, 'S3 x S3: the D-orbit sum x has '
          'x^2 = 0, so u = 1 + x has inverse 1 - x')
    check(ga_mul(Gr, u, uinv) == {0: F(1)}, 'u (1 - x) = 1')
    f = ga_mul(Gr, ga_mul(Gr, u, a), uinv)
    check(ga_mul(Gr, f, f) == f, 'f = u a u^-1 is an idempotent')
    check(all(f.get(Gr.conj(d, y), 0) == c for d in D for y, c in f.items())
          and all(f.get(y, 0) == f.get(Gr.conj(d, y), 0) for d in D
                  for y in Gr.all),
          'f lies in (kG)^D')
    refuted(all(y in set(C) for y in f),
            'proof of Prop. 6.2.2, p. 205: "every idempotent in (kG)^D lies '
            'in kC_G(D)" (S3 x S3, p = 3, D = C3 x 1)')


def _pow(B, z, n):
    r = B.one()
    for _ in range(n):
        r = B.zmul(r, z)
    return r


def lemmas_6_2_4_to_6_2_6(Gr, p):
    B = blocks(Gr, p)
    F = B.F
    dg, vals = defect_groups(Gr, B)
    Ps = Gr.p_subgroup_classes(p)
    for P in Ps:
        C = Gr.centralizer(P)
        vP = transfer_classes(Gr, P, p)
        for i, e in enumerate(B.idems):
            D = dg[i][0]
            cond = in_transfer(e, vP) and bool(br_support(Gr, e, C))
            check(cond == Gr.are_conj(P, D),
                  'Lemma 6.2.4: e in (kG)^G_P and Br_P(e) != 0 iff P is a '
                  'defect group (%s, p=%d, |P|=%d)' % (Gr.name, p, len(P)))
        # kernel of Br_P on (kG)^G_P (author's correction, p. 205)
        trK = [k for k in range(Gr.r) if vP[k] == 0]
        Cs = set(C)
        ker = {k for k in trK if not (set(Gr.classes[k]) & Cs)}
        lower = set()
        for Pp in [Gr.from_gap(H) for H in Gr.to_gap(P).AllSubgroups()
                   if int(H.Size()) < len(P)]:
            v = transfer_classes(Gr, Pp, p)
            lower |= {k for k in range(Gr.r) if v[k] == 0}
        check(ker == lower,
              'Lemma 6.2.4 (author\'s correction): the kernel of Br_P on '
              '(kG)^G_P is sum_(P\' < P) (kG)^G_P\' (%s, p=%d, |P|=%d)'
              % (Gr.name, p, len(P)))
        if ker != set(trK):
            refuted(ker == set(trK),
                    'printed p. 205: the kernel is sum_(P\' < P) (kG)^G_P '
                    '= (kG)^G_P (%s, p=%d, |P|=%d)' % (Gr.name, p, len(P)))
    # Lemma 6.2.5 and Theorem 6.2.6 for every p-subgroup D
    for D in Ps:
        N = Gr.normalizer(D)
        C = Gr.centralizer(D)
        Cs = set(C)
        Nr = sub_of(Gr, N, 'N_G(D)')
        orbs = Gr.orbits(D)
        ok_diag, ok_mack, ref_mack = True, True, True
        dcs = []                         # N \ G / D double cosets
        seen = set()
        for g in Gr.all:
            if g in seen:
                continue
            dcs.append(g)
            seen.update(Gr.mul[Gr.mul[n][g]][d] for n in N for d in D)
        for o in orbs:
            x = {y: F(1) for y in o}
            t = tr(Gr, D, Gr.all, x)
            brt = {y: c for y, c in t.items() if y in Cs}
            brx = {y: c for y, c in x.items() if y in Cs}
            ok_diag = ok_diag and brt == tr(Gr, D, N, brx)
            m = {}
            m2 = {}
            for g in dcs:
                gD = Gr.conj_sub(g, D)
                NgD = tuple(sorted(set(N) & set(gD)))
                gx = {Gr.conj(g, y): c for y, c in x.items()}
                for y, c in tr(Gr, NgD, N, gx).items():
                    m[y] = m.get(y, 0) + c
                lx = {Gr.mul[g][y]: c for y, c in x.items()}
                for y, c in tr(Gr, NgD, N, lx).items():
                    m2[y] = m2.get(y, 0) + c
            m = {y: c for y, c in m.items() if c}
            m2 = {y: c for y, c in m2.items() if c}
            ok_mack = ok_mack and m == t
            ref_mack = ref_mack and m2 == t
        check(ok_diag, 'Lemma 6.2.5: Br_D o Tr_(D,G) = Tr_(D,N_G(D)) o Br_D '
              'on all D-orbit sums (%s, p=%d, |D|=%d)'
              % (Gr.name, p, len(D)))
        check(ok_mack, 'Lemma 6.2.5 (author\'s correction): Tr_(D,G)(x) = '
              'sum_(N g D) Tr_(N cap gD, N)(gx) with the conjugate gxg^-1 '
              '(%s, p=%d, |D|=%d)' % (Gr.name, p, len(D)))
        MACKEY_PRINTED.append(ref_mack)
        # bottom map onto kC_G(D)^N_D
        cn = [o for o in Gr.orbits(N, C)]
        S1 = Span(F, len(cn))
        S2 = Span(F, len(cn))
        posn = {y: i for i, o in enumerate(cn) for y in o}
        for o in orbs:
            t = tr(Gr, D, Gr.all, {y: F(1) for y in o})
            v = [F(0)] * len(cn)
            for y, c in t.items():
                if y in Cs:
                    v[posn[y]] = c
            S1.add(v)
        for o in Gr.orbits(D, C):
            t = tr(Gr, D, N, {y: F(1) for y in o})
            v = [F(0)] * len(cn)
            for y, c in t.items():
                v[posn[y]] = c
            S2.add(v)
        check(S1.dim() == S2.dim() and all(r in S2 for r in S1.rows.values()),
              'Lemma 6.2.5: Br_D maps (kG)^G_D onto kC_G(D)^(N_G(D))_D '
              '(%s, p=%d, |D|=%d)' % (Gr.name, p, len(D)))
        # Theorem 6.2.6
        BN = Blocks(Nr, p, mod=B.mod)
        dgN, _ = defect_groups(Nr, BN)
        DN = tuple(sorted(Nr.from_G[x] for x in D))
        withD = [i for i in range(B.nblocks) if Gr.are_conj(dg[i][0], D)]
        withDN = [j for j in range(BN.nblocks)
                  if Nr.are_conj(dgN[j][0], DN)]
        imgs = [brauer_vec(Gr, B.idems[i], C, Nr) for i in withD]
        check(sorted(map(tuple, imgs)) ==
              sorted(tuple(BN.idems[j]) for j in withDN),
              'Thm 6.2.6 (Brauer\'s first main theorem): Br_D is a '
              'bijection from the blocks of G with defect group D to those '
              'of N_G(D) with defect group D (%s, p=%d, |D|=%d: %d blocks)'
              % (Gr.name, p, len(D), len(withD)))
        # Brauer correspondence for D C_G(D) <= H <= N_G(D)
        DC = set(Gr.closure(list(D) + list(C)))
        for Hn in Nr.subgroup_classes():
            H = tuple(sorted(Nr.to_G[x] for x in Hn))
            if not DC <= set(H) or len(Hn) == 1 and len(N) > 1:
                continue
            Hr = sub_of(Gr, H, 'H')
            BH = Blocks(Hr, p, mod=B.mod)
            brs = [brauer_vec(Gr, e, C, Hr) for e in B.idems]
            for j, eb in enumerate(BH.idems):
                prods = [BH.zmul(eb, b) for b in brs]
                nz = [i for i, z in enumerate(prods) if any(z)]
                check(len(nz) == 1 and prods[nz[0]] == eb,
                      'p. 205: e.Br_D(e_i) = e for exactly one i (the '
                      'Brauer correspondent b^G), D C_G(D) <= H <= N_G(D) '
                      '(%s, p=%d, |D|=%d, |H|=%d)'
                      % (Gr.name, p, len(D), len(H)))
                if len(H) == len(N):
                    if Nr.are_conj(dgN[j][0], DN):
                        i = nz[0]
                        check(Gr.are_conj(dg[i][0], D) and
                              brauer_vec(Gr, B.idems[i], C, Nr) == eb,
                              'Thm 6.2.6: b^G is the block with defect '
                              'group D corresponding to b (%s, p=%d)'
                              % (Gr.name, p))


MACKEY_PRINTED = []


def section_6_2():
    for gname, name, p in [('SymmetricGroup(4)', 'S4', 2),
                           ('SymmetricGroup(4)', 'S4', 3),
                           ('AlternatingGroup(5)', 'A5', 2),
                           ('PSL(3, 2)', 'GL(3,2)', 2),
                           ('SymmetricGroup(5)', 'S5', 2),
                           ('SL(2, 3)', 'SL(2,3)', 2),
                           ('DirectProduct(SymmetricGroup(3), '
                            'SymmetricGroup(3))', 'S3xS3', 3)]:
        Gr = group(gname, name)
        for D in Gr.p_subgroup_classes(p):
            lemma_6_2_1(Gr, p, D)
    prop_6_2_2()
    for gname, name, primes in GROUPS_61:
        Gr = group(gname, name)
        for p in primes:
            lemmas_6_2_4_to_6_2_6(Gr, p)
    refuted(all(MACKEY_PRINTED),
            'printed p. 206: the Mackey sum with the product g.x in place '
            'of the conjugate gxg^-1 (fails in %d of %d cases (G, p, D))'
            % (MACKEY_PRINTED.count(False), len(MACKEY_PRINTED)))


def MTX(name):
    return libgap.eval('MTX.' + name)


def gap_field(F):
    return libgap.eval('GF(%d)' % F.cardinality())


def gap_elt(Gr, d):
    """A dict on group elements -> GAP list of [element, coefficient]."""
    return [[Gr.gap_el(x), libgap(c)] for x, c in d.items() if c]


class GModule:
    """A kG-module given by matrices for the GAP generators of G (right
    action on row vectors, as in GAP), with its representation."""

    def __init__(self, Gr, mats, F):
        self.Gr, self.F = Gr, F
        self.gens = libgap.B6Gens(Gr.G)
        self.mats = mats
        self.n = int(libgap.Length(mats[0])) if len(mats) else 0
        self.hom = libgap.B6Hom(Gr.G, self.gens, mats)

    @classmethod
    def permutation(cls, Gr, H, F):
        gF = gap_field(F)
        n = Gr.n // len(H)
        gens = libgap.B6Gens(Gr.G)
        if n == 1:
            return cls(Gr, libgap([libgap.IdentityMat(1, gF) for g in gens]),
                       F)
        hom = libgap.FactorCosetAction(Gr.G, Gr.to_gap(H))
        mats = [libgap.PermutationMat(hom.Image(g), n, gF) for g in gens]
        return cls(Gr, libgap(mats), F)

    def alg(self, d):
        return libgap.B6AlgElt(self.hom, gap_elt(self.Gr, d), self.n,
                               gap_field(self.F))

    def sub(self, basis, K):
        """Matrices of B6Gens(K) on the row space of basis."""
        return libgap.B6Sub(self.hom, K, basis)


def block_modules(Gr, B, H):
    """e k[G/H] for the blocks e (as row spaces of the permutation module)."""
    F = B.F
    P = GModule.permutation(Gr, H, F)
    out = []
    for i, e in enumerate(B.idems):
        E = P.alg(B.to_group_algebra(e))
        bas = libgap.BaseMat(E)
        out.append((i, P, bas))
    return out


CONTROL = []


def nagao_checks(Gr, p, subs_for_modules, max_dim=24):
    init_gap()
    B = blocks(Gr, p)
    F = B.F
    gF = gap_field(F)
    nsum = 0
    for H in subs_for_modules:
        for i, P, bas in block_modules(Gr, B, H):
            if int(libgap.Length(bas)) == 0:
                continue
            for D in Gr.p_subgroup_classes(p):
                if len(D) == 1:
                    continue
                C = Gr.centralizer(D)
                N = Gr.normalizer(D)
                br = br_support(Gr, B.idems[i], C)
                Ebr = P.alg(br)
                # restricted to M = e k[G/H] (rows bas)
                Mg = Gr.to_gap(N)
                MN = P.sub(bas, Mg)
                n = int(libgap.Length(bas))
                Em = libgap.eval('function(bas, E) return List(bas, '
                                 'v -> SolutionMat(bas, v * E)); end')(bas,
                                                                       Ebr)
                check(Em * Em == Em and all(Em * m == m * Em for m in MN),
                      'Thm 6.3.1: Br_D(e) acts on M as an idempotent '
                      'commuting with N_G(D) (%s, p=%d)' % (Gr.name, p))
                one = libgap.IdentityMat(n, gF)
                Mp = libgap.BaseMat(one - Em)
                if int(libgap.Length(Mp)) == 0:
                    continue
                for K, Kname in ((C, 'C_G(D)'), (N, 'N_G(D)')):
                    Kg = Gr.to_gap(K)
                    Kr = sub_of(Gr, K, Kname)
                    Qs = [Kg.Subgroup([Gr.gap_el(Kr.to_G[x])
                                       for x in Q]) for Q in
                          (q for q in Kr.p_subgroup_classes(p))
                          if not set(D) <= {Kr.to_G[x] for x in Q}]
                    mats = libgap.eval('function(bas, Mp, ms) return List(ms,'
                                       ' m -> List(Mp, v -> SolutionMat(Mp, '
                                       'v * m))); end')(
                        bas, Mp, P.sub(bas, Kg))
                    mod = libgap.GModuleByMats(mats, gF)
                    summands = MTX('Indecomposition')(mod)
                    for s in summands:
                        X = s[1]
                        Xm = MTX('Generators')(X)
                        ok = any(bool(libgap.B6IdInTransfer(Kg, Xm, Q, gF))
                                 for Q in Qs)
                        nsum += 1
                        check(ok, 'Thm 6.3.1 (Nagao): each indecomposable '
                              'summand of M\' = (1 - Br_D(e)).M down_K is '
                              'projective relative to some Q with D not <= '
                              'Q <= K (%s, p=%d, |D|=%d, K=%s)'
                              % (Gr.name, p, len(D), Kname))
                    Mb = libgap.BaseMat(Em)
                    if int(libgap.Length(Mb)) and K is C:
                        matsb = libgap.eval(
                            'function(bas, Mp, ms) return List(ms, m -> '
                            'List(Mp, v -> SolutionMat(Mp, v * m))); end')(
                            bas, Mb, P.sub(bas, Kg))
                        for s in MTX('Indecomposition')(
                                libgap.GModuleByMats(matsb, gF)):
                            Xm = MTX('Generators')(s[1])
                            CONTROL.append(any(bool(libgap.B6IdInTransfer(
                                Kg, Xm, Q, gF)) for Q in Qs))
                    if K is N and int(libgap.Length(Mp)) <= max_dim:
                        # the display of the proof, read for the
                        # N_G(D)-module (1 - Br_D(e)).M down_N_G(D)
                        span_N = libgap.B6TransferSpan(Kg, mats, Qs, gF)
                        idv = libgap.Concatenation(libgap.IdentityMat(
                            int(libgap.Length(Mp)), gF))
                        check(libgap.B6InSpan(span_N, idv),
                              'proof of Thm 6.3.1: 1_M\' in sum_(D not<= Q '
                              '<= N_G(D)) (M\', M\')^(N_G(D))_Q for M\' = '
                              '(1 - Br_D(e)).M down_N_G(D) (%s, p=%d, '
                              '|D|=%d)' % (Gr.name, p, len(D)))
                        Kc = Gr.to_gap(C)
                        Krc = sub_of(Gr, C, 'C_G(D)')
                        Qc = [Kc.Subgroup([Gr.gap_el(Krc.to_G[x])
                                           for x in Q])
                              for Q in Krc.p_subgroup_classes(p)
                              if not set(D) <= {Krc.to_G[x] for x in Q}]
                        matsC = libgap.eval(
                            'function(bas, Mp, ms) return List(ms, m -> '
                            'List(Mp, v -> SolutionMat(Mp, v * m))); end')(
                            bas, Mp, P.sub(bas, Kc))
                        span_C = libgap.B6TransferSpan(Kc, matsC, Qc, gF)
                        check(all(libgap.B6InSpan(span_C, v)
                                  for v in span_N),
                              'proof of Thm 6.3.1: restriction to K = '
                              'C_G(D) maps sum_Q (M\', M\')^(N_G(D))_Q into '
                              'sum_Q (M\', M\')^K_Q (%s, p=%d, |D|=%d)'
                              % (Gr.name, p, len(D)))
    return nsum


def lemma_6_2_7(Gr, p):
    """Alperin's description of b^G: the blocks B of G whose restriction
    to H x H has b as a summand (MeatAxe)."""
    init_gap()
    B = blocks(Gr, p)
    F = B.F
    gF = gap_field(F)
    for D in Gr.p_subgroup_classes(p):
        C = Gr.centralizer(D)
        DC = set(Gr.closure(list(D) + list(C)))
        for H in Gr.subgroup_classes():
            if not DC <= set(H) or len(H) == Gr.n:
                continue
            Hr = sub_of(Gr, H, 'H')
            BH = Blocks(Hr, p, mod=B.mod)
            dgH, _ = defect_groups(Hr, BH)
            DH = tuple(sorted(Hr.from_G[x] for x in D))
            for j, eb in enumerate(BH.idems):
                if not Hr.are_conj(dgH[j][0], DH):
                    continue
                bG = brauer_corr(Gr, B, Hr, BH, j, D)
                bmod = libgap.B6BimoduleOfBlock(
                    Gr.to_gap(H), Gr.to_gap(H),
                    gap_elt(Gr, {Hr.to_G[x]: c for x, c in
                                 BH.to_group_algebra(eb).items()}), gF)
                for i, e in enumerate(B.idems):
                    Bmod = libgap.B6BimoduleOfBlock(
                        Gr.G, Gr.to_gap(H),
                        gap_elt(Gr, B.to_group_algebra(e)), gF)
                    summand = bool(libgap.B6IsSummandIso(Bmod, bmod))
                    check(summand == (i == bG),
                          'Lemma 6.2.7 (Alperin): b is a summand of '
                          'B down_(H x H) iff B = b^G (%s, p=%d, |D|=%d, '
                          '|H|=%d)' % (Gr.name, p, len(D), len(H)))


def brauer_corr(Gr, B, Hr, BH, j, D):
    """b^G for the block j of H (D C_G(D) <= H, D = a defect group of b, as
    indices of G): through the block b' of N_H(D) with (b')^H = b (p. 206);
    checks that b' and b^G are unique."""
    DH = tuple(sorted(Hr.from_G[x] for x in D))
    NH = tuple(sorted(Hr.to_G[x] for x in Hr.normalizer(DH)))
    NHr = sub_of(Gr, NH, 'N_H(D)')
    BNH = Blocks(NHr, B.p, mod=B.mod)
    eb = BH.idems[j]
    bb = [m for m, f in enumerate(BNH.idems)
          if BNH.zmul(f, brauer_vec(Hr, eb, Hr.centralizer(DH),
                                    rel_view(NHr, Hr))) == f]
    C = Gr.centralizer(D)
    bG = [i for i, e in enumerate(B.idems)
          if bb and BNH.zmul(BNH.idems[bb[0]], brauer_vec(Gr, e, C, NHr))
          == BNH.idems[bb[0]]]
    check(len(bb) == 1 and len(bG) == 1,
          'p. 206: b^G well defined for D C_G(D) <= H through N_H(D) '
          '(%s, p=%d, |D|=%d, |H|=%d)' % (Gr.name, B.p, len(D), len(Hr.all)))
    return bG[0]


def rel_view(Sub, Ambient):
    """View Sub (a subgroup of Gr) through the indices of Ambient (another
    subgroup of Gr containing it)."""
    class V:
        pass
    v = V()
    v.classes = Sub.classes
    v.to_G = [Ambient.from_G[x] for x in Sub.to_G]
    return v


def cor_6_3_2_to_6_3_4(Gr, p):
    init_gap()
    B = blocks(Gr, p)
    F = B.F
    gF = gap_field(F)
    dg, _ = defect_groups(Gr, B)
    G = Gr.G
    # Corollary 6.3.4 (blocks of defect zero)
    simples = libgap.IrreducibleModules(G, gF, 0)[1]
    blk_of = []
    for S in simples:
        mats = MTX('Generators')(S)
        Mo = GModule(Gr, mats, F)
        n = Mo.n
        acts = [Mo.alg(B.to_group_algebra(e)) for e in B.idems]
        ids = [i for i, a in enumerate(acts)
               if a == libgap.IdentityMat(n, gF)]
        zeros = [i for i, a in enumerate(acts) if a.IsZero()]
        check(len(ids) == 1 and len(zeros) == B.nblocks - 1,
              'p. 202: a simple module lies in exactly one block (%s, p=%d)'
              % (Gr.name, p))
        proj = bool(libgap.B6IdInTransfer(G, mats, G.TrivialSubgroup(), gF))
        blk_of.append((ids[0], n, proj))
    for i in range(B.nblocks):
        dimB = sum(int(B.irr[c][0]) ** 2 for c in B.block_chars[i])
        ss = [(n, pr) for b, n, pr in blk_of if b == i]
        semisimple = dimB == sum(n * n for n, pr in ss)
        trivialD = len(dg[i][0]) == 1
        projsimple = any(pr for n, pr in ss)
        check(semisimple == trivialD == projsimple,
              'Cor. 6.3.4: J(B) = 0 iff D = 1 iff B contains a projective '
              'simple module (%s, p=%d, block %d: dim %d, simples %s)'
              % (Gr.name, p, i, dimB, [n for n, pr in ss]))
    # Corollaries 6.3.3 and 6.3.2 via the summands of e.k[G/D]
    for i, e in enumerate(B.idems):
        D = dg[i][0]
        if len(D) == 1 or Gr.n // len(D) > 40:
            continue
        Dg = Gr.to_gap(D)
        maxD = list(Dg.MaximalSubgroups())
        N = Gr.normalizer(D)
        Ng = Gr.to_gap(N)
        Nr = sub_of(Gr, N, 'N_G(D)')
        QsN = [Ng.Subgroup([Gr.gap_el(Nr.to_G[x]) for x in Q])
               for Q in Nr.p_subgroup_classes(p)
               if not set(D) <= {Nr.to_G[x] for x in Q}]
        P = GModule.permutation(Gr, D, F)
        E = P.alg(B.to_group_algebra(e))
        W = libgap.BaseMat(E)
        mats = libgap.eval('function(W, ms) return List(ms, m -> List(W, '
                           'w -> SolutionMat(W, w * m))); end')(W, P.mats)
        found = 0
        for s in MTX('Indecomposition')(libgap.GModuleByMats(mats, gF)):
            Xm = MTX('Generators')(s[1])
            vertexD = not any(bool(libgap.B6IdInTransfer(G, Xm, Dp, gF))
                              for Dp in maxD)
            if not vertexD:
                continue
            found += 1
            # Green correspondent: the summand of X down_N with vertex D
            Xmod = GModule(Gr, Xm, F)
            idm = libgap.IdentityMat(Xmod.n, gF)
            resN = libgap.GModuleByMats(Xmod.sub(idm, Ng), gF)
            fX = []
            for t in MTX('Indecomposition')(resN):
                Ym = MTX('Generators')(t[1])
                if not any(bool(libgap.B6IdInTransfer(Ng, Ym, Q, gF))
                           for Q in QsN):
                    fX.append(t)
            check(len(fX) == 1, 'Green correspondence: X down_N_G(D) has '
                  'exactly one summand with vertex D (%s, p=%d)'
                  % (Gr.name, p))
            Ybas = fX[0][0]
            for j, ej in enumerate(B.idems):
                br = Xmod.alg(br_support(Gr, ej, Gr.centralizer(D)))
                img = int(libgap.RankMat(Ybas * br))
                full = int(libgap.Length(Ybas))
                check((img == full) == (i == j) and (img == 0) == (i != j),
                      "Cor. 6.3.2: e.M = M iff Br_D(e).M' = M' for the "
                      "Green correspondent M' (%s, p=%d, |D|=%d)"
                      % (Gr.name, p, len(D)))
        check(found >= 1, 'Cor. 6.3.3: the block has an indecomposable '
              'trivial source module with vertex exactly D (a summand of '
              'e.k[G/D]) (%s, p=%d, |D|=%d)' % (Gr.name, p, len(D)))


def section_6_3():
    init_gap()
    total = 0
    for gname, name, p in [('SymmetricGroup(4)', 'S4', 2),
                           ('SymmetricGroup(4)', 'S4', 3),
                           ('AlternatingGroup(5)', 'A5', 2),
                           ('AlternatingGroup(5)', 'A5', 3),
                           ('AlternatingGroup(5)', 'A5', 5),
                           ('SymmetricGroup(5)', 'S5', 2),
                           ('PSL(3, 2)', 'GL(3,2)', 2),
                           ('PSL(3, 2)', 'GL(3,2)', 3),
                           ('PSL(3, 2)', 'GL(3,2)', 7)]:
        Gr = group(gname, name)
        top = 24 if Gr.n <= 60 else (8 if p == 2 else 14)
        subs = [H for H in Gr.subgroup_classes()
                if 4 <= Gr.n // len(H) <= top]
        total += nagao_checks(Gr, p, subs)
    check(not all(CONTROL),
          'Thm 6.3.1, control: some indecomposable summand of '
          'Br_D(e).M down_C_G(D) is not projective relative to any Q with '
          'D not <= Q (%d of %d summands), so the test above discriminates'
          % (CONTROL.count(False), len(CONTROL)))
    for gname, name, p in [('SymmetricGroup(4)', 'S4', 3),
                           ('AlternatingGroup(5)', 'A5', 2),
                           ('AlternatingGroup(5)', 'A5', 5),
                           ('SymmetricGroup(4)', 'S4', 2)]:
        lemma_6_2_7(group(gname, name), p)
    for gname, name, primes in GROUPS_61:
        Gr = group(gname, name)
        if Gr.n > 200:
            continue
        for p in primes:
            if blocks(Gr, p).mod.q < 2 ** 16:
                cor_6_3_2_to_6_3_4(Gr, p)


def quotient(Gr, Q, name):
    """G/Q as a permutation group (Grp) and the projection as a list."""
    hom = libgap.eval('function(G, Q) local h, i; '
                      'h := NaturalHomomorphismByNormalSubgroup(G, Q); '
                      'i := IsomorphismPermGroup(Image(h)); '
                      'h := h * i; '
                      'i := SmallerDegreePermutationRepresentation(Image(h)); '
                      'return h * i; end')(Gr.G, Gr.to_gap(Q))
    Qb = Grp(hom.Image(), name)
    pi = [Qb.key(hom.Image(Gr.gap_el(x))) for x in Gr.all]
    return Qb, pi


def conj_class_perm(Gr, Nr, g):
    """The permutation of the N-classes induced by conjugation by g in G."""
    out = []
    for K in Nr.classes:
        y = Gr.conj(g, Nr.to_G[K[0]])
        out.append(Nr.cls_of[Nr.from_G[y]])
    return out


def conj_central(Gr, Nr, g, z):
    perm = conj_class_perm(Gr, Nr, g)
    w = [z[0].parent()(0)] * Nr.r
    for k, c in enumerate(z):
        w[perm[k]] = c
    return w


def stabiliser(Gr, Nr, e):
    return tuple(g for g in Gr.all if conj_central(Gr, Nr, g, e) == e)


def n_to_g_central(Gr, Nr, z, B):
    """A G-invariant element of Z(kN), in the class coordinates of G."""
    d = {}
    for k, K in enumerate(Nr.classes):
        for x in K:
            d[Nr.to_G[x]] = z[k]
    v = []
    for K in Gr.classes:
        cs = {d.get(x, B.F(0)) for x in K}
        assert len(cs) == 1
        v.append(cs.pop())
    return v


def theorem_6_4_1(Gr, p, Ngap_list):
    B = blocks(Gr, p)
    F = B.F
    dg, _ = defect_groups(Gr, B)
    for N in Ngap_list:
        Nr = sub_of(Gr, N, 'N')
        BN = Blocks(Nr, p, mod=B.mod)
        dgN, _ = defect_groups(Nr, BN)
        covered = {i: set() for i in range(B.nblocks)}
        final_ok = {}
        orbit_of = {}
        for j, e in enumerate(BN.idems):
            T = stabiliser(Gr, Nr, e)
            n = Gr.n // len(T)
            reps = coset_reps(Gr, T)
            conjs = [conj_central(Gr, Nr, g, e) for g in reps]
            f = [sum(c, F(0)) for c in zip(*conjs)]
            orbit_of[j] = frozenset(BN.idems.index(c) for c in conjs)
            fG = n_to_g_central(Gr, Nr, f, B)
            check(B.zmul(fG, fG) == fG, 'p. 209: f = sum_(G/T) geg^-1 is a '
                  'central idempotent of kG (%s, |N|=%d)' % (Gr.name, len(N)))
            for i, eB in enumerate(B.idems):
                pr = B.zmul(eB, fG)
                check(not any(pr) or pr == eB, 'p. 209: e\'f = e\' or 0')
                if any(pr):
                    covered[i].add(j)
                    # (ii) a defect group of B inside T
                    D = dg[i][0]
                    check(any(set(Gr.conj_sub(g, D)) <= set(T)
                              for g in Gr.all),
                          'Thm 6.4.1 (ii): some defect group of B lies in '
                          'T(b) (%s, p=%d, |N|=%d)' % (Gr.name, p, len(N)))
                    # (iv)
                    Db = tuple(sorted(Nr.to_G[x] for x in dgN[j][0]))
                    check(any(Gr.are_conj(tuple(sorted(
                        set(Gr.conj_sub(g, D)) & set(N))), Db)
                        and Nr.are_conj(tuple(sorted(
                            Nr.from_G[x] for x in set(Gr.conj_sub(g, D))
                            & set(N))), dgN[j][0])
                        for g in Gr.all),
                        'Thm 6.4.1 (iv): D(B) cap N is a defect group of b '
                        'for some choice of D(B) (%s, p=%d, |N|=%d)'
                        % (Gr.name, p, len(N)))
                    # final statement: p does not divide |T : D(B) N|
                    ok = False
                    for g in Gr.all:
                        Dg = Gr.conj_sub(g, D)
                        if set(Dg) <= set(T):
                            DN = Gr.closure(list(Dg) + list(N))
                            ok = ok or (len(T) // len(DN)) % p != 0
                    final_ok[(i, j)] = ok
            # (iii) dimensions: dim f.kG = n^2 dim e.kT
            Tr_ = sub_of(Gr, T, 'T')
            BT = Blocks(Tr_, p, mod=B.mod)
            eT = n_to_g_central(Tr_, rel_view(Nr, Tr_), e, BT)
            dim_eT = sum(sum(int(BT.irr[c][0]) ** 2
                             for c in BT.block_chars[m])
                         for m in range(BT.nblocks)
                         if any(BT.zmul(eT, BT.idems[m])))
            dim_f = sum(sum(int(B.irr[c][0]) ** 2 for c in B.block_chars[i])
                        for i in range(B.nblocks)
                        if any(B.zmul(fG, B.idems[i])))
            check(dim_f == n * n * dim_eT,
                  'Thm 6.4.1 (iii): dim f.kG = n^2 dim e.kT, n = |G:T| '
                  '(%s, p=%d, |N|=%d, n=%d)' % (Gr.name, p, len(N), n))
            # (iii) the matrix units g1 x g2^-1, x in e.kT
            ed = {Nr.to_G[x]: c for x, c in BN.to_group_algebra(e).items()}
            ok = True
            for _ in range(2):
                t = random.choice(T)
                x = ga_mul(Gr, ed, {t: F(1)})
                g1, g2 = random.choice(reps), random.choice(reps)
                u = ga_mul(Gr, ga_mul(Gr, {g1: F(1)}, x),
                           {Gr.inv[g2]: F(1)})
                for g in reps:
                    s = random.choice(T)
                    y = ga_mul(Gr, ed, {Gr.mul[s][Gr.inv[g]]: F(1)})
                    img = ga_mul(Gr, y, u)
                    if g == g1:
                        want = ga_mul(Gr, ga_mul(Gr, ed, {s: F(1)}),
                                      ga_mul(Gr, x, {Gr.inv[g2]: F(1)}))
                    else:
                        want = {}
                    ok = ok and img == want
            check(ok, 'Thm 6.4.1 (iii): right multiplication by g1 x g2^-1 '
                  '(x in e.kT) is the matrix unit sending (e.kT)g1^-1 to '
                  '(e.kT)g2^-1 (%s, p=%d, |N|=%d)' % (Gr.name, p, len(N)))
        # (i): blocks covered by B form one G-orbit; every b is covered
        for i in range(B.nblocks):
            orbs = {orbit_of[j] for j in covered[i]}
            check(len(orbs) == 1 and set().union(*orbs) == covered[i],
                  'Thm 6.4.1 (i): the blocks of N covered by B form a single '
                  'G-conjugacy class (%s, p=%d, |N|=%d)'
                  % (Gr.name, p, len(N)))
        check(set().union(*covered.values()) == set(range(BN.nblocks)),
              'p. 209: every block of kN is covered by some block of kG')
        # final statement (corrected): |T : D(B)N| prime to p when B is the
        # only block covering b; also for a block of largest defect group
        # covering b (Curtis-Reiner, Methods II, (61.5)); the printed
        # statement for every covering block fails
        for j in range(BN.nblocks):
            cov = [i for i in range(B.nblocks) if j in covered[i]]
            if len(cov) == 1:
                check(final_ok[(cov[0], j)], 'Thm 6.4.1, final statement '
                      '(corrected): B the only block covering b gives '
                      '|T : D(B) N| prime to p (%s, p=%d, |N|=%d)'
                      % (Gr.name, p, len(N)))
            big = max(len(dg[i][0]) for i in cov)
            check(all(final_ok[(i, j)] for i in cov
                      if len(dg[i][0]) == big),
                  'Thm 6.4.1: |T : D(B) N| prime to p for the blocks of '
                  'largest defect covering b (%s, p=%d, |N|=%d)'
                  % (Gr.name, p, len(N)))
            for i in cov:
                if not final_ok[(i, j)]:
                    FINAL_PRINTED.append('%s, p=%d, |N|=%d, |D(B)|=%d'
                                         % (Gr.name, p, len(N),
                                            len(dg[i][0])))
        # (v)
        for j, e in enumerate(BN.idems):
            Db = dgN[j][0]
            DbG = tuple(sorted(Nr.to_G[x] for x in Db))
            if not set(Gr.centralizer(DbG)) <= set(N):
                continue
            cov = [i for i in range(B.nblocks) if j in covered[i]]
            bG = brauer_corr(Gr, B, Nr, BN, j, DbG)
            check(cov == [bG], 'Thm 6.4.1 (v): C_G(D(b)) <= N gives b^G = B, '
                  'the unique block covering b (%s, p=%d, |N|=%d)'
                  % (Gr.name, p, len(N)))


FINAL_PRINTED = []


def theorem_6_4_1_cases():
    cases = [('SymmetricGroup(4)', 'S4', [2, 3], ['V4', 'A4']),
             ('SymmetricGroup(5)', 'S5', [2, 3, 5], ['A5']),
             ('GL(2, 3)', 'GL(2,3)', [2, 3], ['SL', 'Q8']),
             ('DirectProduct(SymmetricGroup(3), SymmetricGroup(3))', 'S3xS3',
              [2, 3], ['all']),
             ('DirectProduct(CyclicGroup(IsPermGroup, 3), SymmetricGroup(3))',
              'C3xS3', [2, 3], ['all'])]
    for gname, name, primes, which in cases:
        Gr = group(gname, name)
        Ns = [Gr.from_gap(H) for H in Gr.G.NormalSubgroups()
              if 1 < int(H.Size()) < Gr.n]
        for p in primes:
            theorem_6_4_1(Gr, p, Ns)
    # N = 1 (b = k, T = G): the printed final statement would make every
    # block of G have Sylow defect groups
    for gname, name, p in [('SymmetricGroup(3)', 'S3', 2),
                           ('AlternatingGroup(5)', 'A5', 2)]:
        Gr = group(gname, name)
        theorem_6_4_1(Gr, p, [(0,)])
    refuted(not FINAL_PRINTED, 'Thm 6.4.1, printed final statement: '
            '|T : D(B) N| is not divisible by p for every block B covering b '
            '(fails for %d pairs (B, b), e.g. %s)'
            % (len(FINAL_PRINTED), '; '.join(FINAL_PRINTED[:3])))
    # e.kT can be a sum of several blocks of kT (so "x in b^T" of the
    # printed proof cannot mean a single block): C3 x S3, N = C3 x 1, p = 2
    Gr = group('DirectProduct(CyclicGroup(IsPermGroup, 3), '
               'SymmetricGroup(3))', 'C3xS3')
    B = blocks(Gr, 2)
    N = next(Gr.from_gap(H) for H in Gr.G.NormalSubgroups()
             if int(H.Size()) == 3 and Gr.is_normal(Gr.from_gap(H))
             and len(Gr.centralizer(Gr.from_gap(H))) == 18)
    Nr = sub_of(Gr, N, 'N')
    BN = Blocks(Nr, 2, mod=B.mod)
    e = BN.idems[0]
    T = stabiliser(Gr, Nr, e)
    eG = n_to_g_central(Gr, Nr, e, B)
    nb = sum(1 for f in B.idems if any(B.zmul(eG, f)))
    check(len(T) == Gr.n and nb == 2,
          'Thm 6.4.1 (iii): for G = C3 x S3, N = C3 x 1, p = 2, T = G and '
          'e.kT is the sum of two blocks of kT; the matrix units need all '
          'x in e.kT')


def lemma_6_4_2():
    cases = [('DihedralGroup(IsPermGroup, 8)', 'D8', 2, 'centre'),
             ('QuaternionGroup(IsPermGroup, 8)', 'Q8', 2, 'centre'),
             ('SL(2, 3)', 'SL(2,3)', 2, 'centre'),
             ('SL(2, 5)', 'SL(2,5)', 2, 'centre'),
             ('SL(2, 7)', 'SL(2,7)', 2, 'centre'),
             ('DirectProduct(CyclicGroup(IsPermGroup, 3), '
              'AlternatingGroup(4))', 'C3xA4', 3, 'centre'),
             ('DirectProduct(DihedralGroup(IsPermGroup, 8), '
              'SymmetricGroup(3))', 'D8xS3', 2, 'D8')]
    fails_surj, fails_tr, holds_trQ = [], [], []
    for gname, name, p, which in cases:
        Gr = group(gname, name)
        if which == 'centre':
            Q = Gr.from_gap(Gr.G.Centre().SylowSubgroup(p))
        else:
            Q = next(Gr.from_gap(H) for H in Gr.G.NormalSubgroups()
                     if int(H.Size()) == 8 and not H.IsAbelian())
        CQ = Gr.centralizer(Q)
        check(len(Gr.closure(list(Q) + list(CQ))) == Gr.n and Gr.is_normal(Q),
              'Lemma 6.4.2: hypothesis G = Q C_G(Q) (%s)' % name)
        B = blocks(Gr, p)
        F = B.F
        Qb, pi = quotient(Gr, Q, name + '/Q')
        BQ = Blocks(Qb, p, mod=B.mod)

        def piz(z):
            d = {}
            for k, K in enumerate(Gr.classes):
                for x in K:
                    d[pi[x]] = d.get(pi[x], F(0)) + z[k]
            v = []
            for K in Qb.classes:
                cs = {d.get(x, F(0)) for x in K}
                assert len(cs) == 1
                v.append(cs.pop())
            return v
        unit = lambda k, r: [F(int(j == k)) for j in range(r)]
        img = Span(F, Qb.r)
        for k, K in enumerate(Gr.classes):
            if set(K) <= set(CQ):
                img.add(piz(unit(k, Gr.r)))
        if img.dim() < Qb.r:
            fails_surj.append('%s: %d < %d' % (name, img.dim(), Qb.r))
        # p-regular class sums of C_G(Q) map onto those of C_G(Q)/Z(Q)
        preg = [k for k in range(Qb.r)
                if Qb.order[Qb.classes[k][0]] % p]
        ok = all(any(piz(unit(k, Gr.r)) == unit(m, Qb.r)
                     for k, K in enumerate(Gr.classes)
                     if set(K) <= set(CQ) and Gr.order[K[0]] % p)
                 for m in preg)
        check(ok, 'Lemma 6.4.2 (corrected proof): every p-regular class sum '
              'of C_G(Q)/Z(Q) is the image of a p-regular class sum of '
              'C_G(Q) (%s)' % name)
        check(all(all(not c or k in preg for k, c in enumerate(f))
                  for f in BQ.idems),
              'Osima: the block idempotents of k[G/Q] are combinations of '
              'p-regular class sums (%s)' % name)
        check(all(f in img for f in BQ.idems),
              'Lemma 6.4.2: the block idempotents of k[G/Q] lie in '
              'pi(Z(kC_G(Q))) (%s)' % name)
        # the bijection of blocks
        imgs = [piz(e) for e in B.idems]
        check(sorted(map(tuple, imgs)) == sorted(map(tuple, BQ.idems)),
              'Lemma 6.4.2: pi is a bijection from the block idempotents of '
              'kG to those of k[G/Q] (%s, p=%d: %d blocks)'
              % (name, p, B.nblocks))
        dg, _ = defect_groups(Gr, B, Gr.p_subgroup_classes(p))
        dgQ, _ = defect_groups(Qb, BQ, Qb.p_subgroup_classes(p))
        for i, e in enumerate(B.idems):
            D = dg[i][0]
            j = BQ.idems.index(imgs[i])
            Dbar = tuple(sorted({pi[x] for x in D}))
            check(set(Q) <= set(D) and Qb.are_conj(Dbar, dgQ[j][0]),
                  'Lemma 6.4.2: D(B) contains Q and D(pi(B)) = D(B)/Q (%s, '
                  '|D|=%d)' % (name, len(D)))
            # Br_(D/Q)(pi(e)) = pi(Br_D(e)) != 0
            CD = Gr.centralizer(D)
            br = br_support(Gr, e, CD)
            pbr = {}
            for x, c in br.items():
                pbr[pi[x]] = pbr.get(pi[x], F(0)) + c
            pbr = {x: c for x, c in pbr.items() if c}
            ed = {}
            for k, K in enumerate(Qb.classes):
                for x in K:
                    if imgs[i][k]:
                        ed[x] = imgs[i][k]
            CDb = set(Qb.centralizer(Dbar))
            brQ = {x: c for x, c in ed.items() if x in CDb}
            check(pbr == brQ and brQ,
                  'Lemma 6.4.2 (corrected proof): Br_(D/Q)(pi(e)) = '
                  'pi(Br_D(e)) != 0 (%s, |D|=%d)' % (name, len(D)))
            # the printed claim pi((kG)^G_D) = (k[G/Q])^(G/Q)_(D/Q)
            v1 = transfer_classes(Gr, D, p)
            v2 = transfer_classes(Qb, Dbar, p)
            S1 = Span(F, Qb.r, [piz(unit(k, Gr.r)) for k in range(Gr.r)
                                if v1[k] == 0])
            S2 = Span(F, Qb.r, [unit(k, Qb.r) for k in range(Qb.r)
                                if v2[k] == 0])
            check(all(r in S2 for r in S1.rows.values()),
                  'Lemma 6.4.2: pi((kG)^G_D) lies in (k[G/Q])^(G/Q)_(D/Q) '
                  '(%s, |D|=%d)' % (name, len(D)))
            same = S1.dim() == S2.dim()
            if len(D) == len(Q):
                check(same, 'Lemma 6.4.2 with D = Q: pi((kG)^G_Q) = '
                      '(k[G/Q])^(G/Q)_1 (%s)' % name)
                holds_trQ.append(name)
            elif not same:
                fails_tr.append('%s, |D|=%d: %d < %d'
                                % (name, len(D), S1.dim(), S2.dim()))
    refuted(not fails_surj, 'proof of Lemma 6.4.2, p. 210: pi maps '
            'Z(kC_G(Q)) onto Z(kC_G(Q)/Z(Q)) [dimensions of image and '
            'target: %s]' % '; '.join(fails_surj))
    refuted(not fails_tr, 'proof of Lemma 6.4.2, p. 210: the image under '
            'pi of (kG)^G_D is (kG/Q)^(G/Q)_(D/Q) [%s]' % '; '.join(fails_tr))


def theorem_6_4_3(Gr, p):
    B = blocks(Gr, p)
    dg, _ = defect_groups(Gr, B)
    for D in Gr.p_subgroup_classes(p):
        C = Gr.centralizer(D)
        N = Gr.normalizer(D)
        DC = Gr.closure(list(D) + list(C))
        n1 = [i for i in range(B.nblocks) if Gr.are_conj(dg[i][0], D)]
        Nr = sub_of(Gr, N, 'N')
        BN = Blocks(Nr, p, mod=B.mod)
        dgN, _ = defect_groups(Nr, BN, Nr.p_subgroup_classes(p))
        DN = tuple(sorted(Nr.from_G[x] for x in D))
        n2 = [j for j in range(BN.nblocks) if Nr.are_conj(dgN[j][0], DN)]
        Hr = sub_of(Gr, DC, 'DC_G(D)')
        BH = Blocks(Hr, p, mod=B.mod)
        dgH, _ = defect_groups(Hr, BH, Hr.p_subgroup_classes(p))
        DH = tuple(sorted(Hr.from_G[x] for x in D))
        cls3, seen = [], set()
        for j, e in enumerate(BH.idems):
            if j in seen or not Hr.are_conj(dgH[j][0], DH):
                continue
            T = tuple(g for g in N if conj_central(Gr, Hr, g, e) == e)
            orbit = {BH.idems.index(conj_central(Gr, Hr, g, e)) for g in N}
            seen |= orbit
            if (len(T) // len(DC)) % p:
                cls3.append(j)
        # (iv): blocks of defect zero of DC/D with p' inertial index
        Qb, pi = quotient(Hr, DH, 'DC/D')
        BQ = Blocks(Qb, p, mod=B.mod)
        defect0 = [m for m in range(BQ.nblocks) if BQ.defect[m] == 0]
        # N acts on DC/D by conjugation (via lifts)
        cls4, seen4 = [], set()
        for m in defect0:
            if m in seen4:
                continue
            f = BQ.idems[m]
            Tm, orb = [], set()
            for g in N:
                perm = []
                for K in Qb.classes:
                    x = next(y for y in Hr.all if pi[y] == K[0])
                    z = Hr.from_G[Gr.conj(g, Hr.to_G[x])]
                    perm.append(Qb.cls_of[pi[z]])
                w = [BQ.F(0)] * Qb.r
                for k, c in enumerate(f):
                    w[perm[k]] = c
                orb.add(BQ.idems.index(w))
                if w == f:
                    Tm.append(g)
            seen4 |= orb
            if (len(Tm) // len(DC)) % p:
                cls4.append(m)
        check(len(n1) == len(n2) == len(cls3) == len(cls4),
              'Thm 6.4.3: equal numbers of (i) blocks of G with defect '
              'group D, (ii) blocks of N_G(D) with defect group D, (iii) '
              'N_G(D)-classes of blocks of D C_G(D) with defect group D and '
              'p-prime inertial index, (iv) classes of blocks of defect zero '
              'of D C_G(D)/D with p-prime inertial index (%s, p=%d, |D|=%d: '
              '%d)' % (Gr.name, p, len(D), len(n1)))
        # (iii) -> (i): b -> b^G has defect group D, injective on classes
        imgs = []
        for j in cls3:
            i = brauer_corr(Gr, B, Hr, BH, j, D)
            imgs.append(i)
            check(i in n1, 'Thm 6.4.3: b^G has defect group D (%s, p=%d)'
                  % (Gr.name, p))
        check(len(set(imgs)) == len(imgs),
              'Thm 6.4.3: b -> b^G is injective on N_G(D)-classes')


def theorem_6_4_5(Gr, p):
    B = blocks(Gr, p)
    for D in Gr.p_subgroup_classes(p):
        C = Gr.centralizer(D)
        DC = set(Gr.closure(list(D) + list(C)))
        for H in Gr.subgroup_classes():
            if not DC <= set(H):
                continue
            Hr = sub_of(Gr, H, 'H')
            BH = Blocks(Hr, p, mod=B.mod)
            dgH, _ = defect_groups(Hr, BH, Hr.p_subgroup_classes(p))
            DH = tuple(sorted(Hr.from_G[x] for x in D))
            for j in range(BH.nblocks):
                if not Hr.are_conj(dgH[j][0], DH):
                    continue
                i = brauer_corr(Gr, B, Hr, BH, j, D)
                check((i == B.principal) == (j == BH.principal),
                      'Thm 6.4.5 (Brauer\'s third main theorem): b^G = '
                      'B_0(kG) iff b = B_0(kH) (%s, p=%d, |D|=%d, |H|=%d)'
                      % (Gr.name, p, len(D), len(H)))


def section_6_4():
    theorem_6_4_1_cases()
    lemma_6_4_2()
    for gname, name, primes in GROUPS_61:
        Gr = group(gname, name)
        if Gr.n > 200:
            continue
        for p in primes:
            theorem_6_4_3(Gr, p)
            theorem_6_4_5(Gr, p)


# ===========================================================================
# Exact integer determinants (fraction-free elimination, no BLAS)
# ===========================================================================


def det_int(M):
    n = len(M)
    if n == 0:
        return 1
    A = [[QQ(x) for x in row] for row in M]
    d = QQ(1)
    for c in range(n):
        r = next((i for i in range(c, n) if A[i][c]), None)
        if r is None:
            return 0
        if r != c:
            A[c], A[r] = A[r], A[c]
            d = -d
        d *= A[c][c]
        for i in range(c + 1, n):
            if A[i][c]:
                f = A[i][c] / A[c][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
    return ZZ(d)


def brauer_tree_cartan(edges, mult):
    """Cartan matrix of a Brauer tree algebra: rows and columns indexed by
    the edges; c_EE = m(u) + m(v), c_EF = m(w) if E, F meet in w."""
    n = len(edges)
    C = [[0] * n for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        C[i][i] = mult[u] + mult[v]
        for j, (a, b) in enumerate(edges):
            if j != i:
                common = {u, v} & {a, b}
                C[i][j] = sum(mult[w] for w in common)
    return C


def cartan_determinant_checks():
    from sage.all import graphs
    # stars (p. 217)
    for e in range(1, 11):
        for m in range(1, 11):
            I_mJ = [[m + int(i == j) for j in range(e)] for i in range(e)]
            check(det_int(I_mJ) == e * m + 1,
                  'p. 217: det(I + mJ) = em + 1 (e=%d, m=%d)' % (e, m))
            S = [[(m + 1 if i == 0 else 2) if i == j else 1
                  for j in range(e)] for i in range(e)]
            check(det_int(S) == e * m + 1,
                  'p. 217: det of the star with exceptional leaf = em + 1 '
                  '(e=%d, m=%d)' % (e, m))
    # all trees with e <= 7 edges, every exceptional vertex, m <= 6
    ntrees = 0
    zchecks = [0, 0]
    printed_z_fails = 0
    printed_L_fails = 0
    for e in range(1, 8):
        flags = {'det': True, 'form': True, 'laplace': True, 'z': True,
                 'dets': True}
        nconf = [0, 0]
        for T in graphs.trees(e + 1):
            ntrees += 1
            V = T.vertices(sort=True)
            edges = [tuple(sorted(x[:2])) for x in T.edges(sort=True)]
            for exc in [None] + V:
                for m in range(1, 7):
                    if exc is None and m > 1:
                        continue
                    mult = {v: (m if v == exc else 1) for v in V}
                    C = brauer_tree_cartan(edges, mult)
                    nconf[0] += 1
                    flags['det'] &= det_int(C) == e * m + 1
                    # the induction step at every internal edge E
                    for E in edges:
                        u, v = E
                        if T.degree(u) == 1 or T.degree(v) == 1:
                            continue
                        Tm = T.copy()
                        Tm.delete_edge(u, v)
                        cu = set(Tm.connected_component_containing_vertex(u))
                        cv = set(Tm.connected_component_containing_vertex(v))
                        for left, right, lend, rend in ((cu, cv, u, v),
                                                        (cv, cu, v, u)):
                            L = [x for x in edges if set(x) <= left] + [E]
                            R = [E] + [x for x in edges if set(x) <= right]
                            l, r = len(L), len(R)
                            order = L[:-1] + [E] + R[1:]
                            Cm = brauer_tree_cartan(order, mult)
                            X = [row[:l] for row in Cm[:l]]
                            Y = [row[l - 1:] for row in Cm[l - 1:]]
                            X0 = [row[:l - 1] for row in Cm[:l - 1]]
                            Y0 = [row[l:] for row in Cm[l:]]
                            z = Cm[l - 1][l - 1]
                            nconf[1] += 1
                            flags['form'] &= all(
                                Cm[i][j] == 0 for i in range(l - 1)
                                for j in range(l, e))
                            dX, dY, dX0, dY0 = map(det_int, (X, Y, X0, Y0))
                            flags['laplace'] &= (det_int(Cm) == dX * dY0 +
                                                 dX0 * dY - z * dX0 * dY0)
                            if exc is None or m == 1:
                                continue
                            if exc in left:
                                # corrected labelling and values of z
                                zchecks[0] += 1
                                flags['z'] &= z == (m + 1 if exc == lend
                                                    else 2)
                                if z != (2 if exc == lend else m + 1):
                                    printed_z_fails += 1
                                want = r * m + 1 if exc == lend else r + 1
                                flags['dets'] &= ((dX, dX0, dY, dY0) ==
                                                  (l * m + 1, (l - 1) * m + 1,
                                                   want, r))
                            elif exc == rend:
                                zchecks[1] += 1
                                if dX0 != (l - 1) * m + 1:
                                    printed_L_fails += 1
        check(flags['det'], 'Thm 6.5.5 (proof): the Cartan matrix of every '
              'Brauer tree with e = %d edges, any exceptional vertex, m <= 6, '
              'has determinant em + 1 (%d configurations)' % (e, nconf[0]))
        if nconf[1]:
            check(flags['form'] and flags['laplace'],
                  'p. 218: at every edge E with no end of valency one, C is '
                  'block-diagonal with one overlap entry z and det C = det X '
                  'det Y0 + det X0 det Y - z det X0 det Y0 (e = %d, %d cases)'
                  % (e, nconf[1]))
            check(flags['z'] and flags['dets'],
                  'p. 218 (corrected): with the exceptional vertex in L0, '
                  'z = m + 1 if it is the left-hand vertex of E and z = 2 '
                  'otherwise; det X = lm + 1, det X0 = (l - 1)m + 1, det Y0 = '
                  'r, det Y = rm + 1 or r + 1 accordingly (e = %d)' % e)
    refuted(printed_z_fails == 0,
            'printed p. 218: "z equal to either 2 or m + 1, depending on '
            'whether the exceptional vertex is the left-hand vertex of E or '
            'not" (wrong in %d of %d configurations)'
            % (printed_z_fails, zchecks[0]))
    refuted(printed_L_fails == 0,
            'printed p. 218: labelling "the exceptional vertex lies in L": '
            'with the exceptional vertex the right-hand end of E, det X0 != '
            '(l - 1)m + 1 (%d of %d configurations)'
            % (printed_L_fails, zchecks[1]))
    # the two displays as polynomial identities
    R = PolynomialRing(QQ, 'l,r,m')
    l, r, m = R.gens()
    e = l + r - 1
    check((l * m + 1) * r + ((l - 1) * m + 1) * (r + 1)
          - 2 * ((l - 1) * m + 1) * r == e * m + 1,
          'p. 218: the display for z = 2 (identity in Q[l, r, m])')
    check((l * m + 1) * r + ((l - 1) * m + 1) * (r * m + 1)
          - (m + 1) * ((l - 1) * m + 1) * r == e * m + 1,
          'p. 218: the corrected display for z = m + 1 (identity in '
          'Q[l, r, m])')
    printed = ((l * m + 1) * r + ((l - 1) * m + 1) * (r * m + 1)
               - (m + 1) * ((l + 1) * m + 1) * r)
    refuted(printed == e * m + 1,
            'printed p. 218: (m + 1)((l + 1)m + 1)r in the display for '
            'z = m + 1')
    check(printed - (e * m + 1) == -2 * m * (m + 1) * r,
          'p. 218: the printed display differs by -2m(m + 1)r')
    # det(I + ((p^n - 1)/e) J) = p^n
    for q in [3, 5, 7, 9, 11, 13, 25, 27, 49, 125]:
        p = ZZ(q).prime_factors()[0]
        for e in ZZ(p - 1).divisors():
            k = (q - 1) // e
            M = [[k + int(i == j) for j in range(e)] for i in range(e)]
            check((q - 1) % e == 0 and det_int(M) == q,
                  'p. 217: det(I + ((p^n - 1)/e) J) = p^n (p^n=%d, e=%d)'
                  % (q, e))


# ===========================================================================
# Blocks of cyclic defect in groups (centre level and decomposition matrices)
# ===========================================================================


def is_cyclic_group(Gr, D):
    return any(Gr.order[x] == len(D) for x in D)


def cyclic_blocks(Gr, p):
    B = blocks(Gr, p)
    dg, _ = defect_groups(Gr, B, Gr.p_subgroup_classes(p))
    preg = [k for k in range(Gr.r) if Gr.order[Gr.classes[k][0]] % p]
    for i in range(B.nblocks):
        D = dg[i][0]
        if len(D) == 1 or not is_cyclic_group(Gr, D):
            continue
        # l(B) = rank of the ordinary characters of B on p-regular classes
        rows = [[B.irr[c][k] for k in preg] for c in B.block_chars[i]]
        lB = int(libgap.RankMat(rows))
        Q = tuple(sorted({x for x in D if Gr.order[x] in (1, p)}))
        N, C = Gr.normalizer(Q), Gr.centralizer(Q)
        check(set(Gr.normalizer(D)) <= set(N),
              'p. 212: N_G(Q) >= N_G(D) (%s, p=%d)' % (Gr.name, p))
        Cr = sub_of(Gr, C, 'C_G(Q)')
        BC = Blocks(Cr, p, mod=B.mod)
        brC = brauer_vec(Gr, B.idems[i], C, Cr)
        b1s = [j for j, f in enumerate(BC.idems) if BC.zmul(f, brC) == f]
        e1 = BC.idems[b1s[0]]
        orbit = {BC.idems.index(conj_central(Gr, Cr, g, e1)) for g in N}
        check(orbit == set(b1s), 'p. 212: the blocks b1 of C_G(Q) with '
              'b1^G = B form one N_G(Q)-conjugacy class (%s, p=%d)'
              % (Gr.name, p))
        T = [g for g in N if conj_central(Gr, Cr, g, e1) == e1]
        e = len(T) // len(C)
        nc = len(N) // len(C)
        check(nc % e == 0 and (p - 1) % nc == 0,
              'p. 212: e | |N_G(Q) : C_G(Q)| | p - 1 (%s, p=%d, e=%d)'
              % (Gr.name, p, e))
        check(lB == e, 'Thm 6.5.5: B has e simple modules (%s, p=%d, '
              '|D|=%d, e=%d)' % (Gr.name, p, len(D), e))
        nchar = len(B.block_chars[i])
        check(nchar == e + (len(D) - 1) // e,
              'Brauer tree: the number of ordinary characters of B is the '
              'number e + 1 of vertices plus (|D| - 1)/e - 1 exceptional '
              'ones (%s, p=%d)' % (Gr.name, p))
        CYCLIC_SEEN.append((Gr.name, p, len(D), e))


CYCLIC_SEEN = []


LIBRARY_CYCLIC = [('A5', [3, 5]), ('L3(2)', [3, 7]), ('L2(8)', [3, 7]),
                  ('L2(11)', [3, 5, 11]), ('L2(13)', [3, 7, 13]),
                  ('A6', [5]), ('A7', [5, 7]), ('M11', [5, 11]),
                  ('L2(16)', [3, 5, 17]), ('L2(17)', [3, 17]),
                  ('L2(19)', [3, 5, 19]), ('J1', [3, 5, 7, 11, 19]),
                  ('L2(25)', [13]), ('U3(3)', [7]), ('S5', [3, 5]),
                  ('M12', [11])]


def library_brauer_trees():
    """Decomposition matrices of the cyclic blocks (GAP character table
    library): Brauer tree property, e = l(B) | p - 1, multiplicity
    (|D| - 1)/e, Cartan matrix = that of the tree, determinant |D|."""
    assert libgap.LoadPackage('ctbllib')
    nblk = 0
    for name, primes in LIBRARY_CYCLIC:
        t = libgap.CharacterTable(name)
        for p in primes:
            m = libgap.eval('function(t, p) return t mod p; end')(t, p)
            sylow = p ** ZZ(int(t.Size())).valuation(p)
            check(sylow in [int(x) for x in t.OrdersClassRepresentatives()],
                  'cyclic Sylow %d-subgroups (%s)' % (p, name))
            info = libgap.BlocksInfo(m)
            for bnr, b in enumerate(info):
                d = int(b['defect'])
                if d == 0:
                    continue
                # cyclic Sylow p-subgroups: the defect group is cyclic
                Pn = p ** d
                dec = [[int(x) for x in row]
                       for row in libgap.DecompositionMatrix(m, bnr + 1)]
                l = len(dec[0])
                k = len(dec)
                mexc = (Pn - 1) // l
                check((p - 1) % l == 0 and (Pn - 1) % l == 0,
                      'Thm 6.5.5: e = l(B) divides p - 1 (%s mod %d)'
                      % (name, p))
                check(k == l + mexc,
                      'Brauer tree: k(B) = e + (p^n - 1)/e (%s mod %d)'
                      % (name, p))
                if l == 1:
                    check(all(row == [1] for row in dec),
                          'Thm 6.5.5: e = 1, the tree is one edge with an '
                          'exceptional end of multiplicity p^n - 1 (%s mod '
                          '%d)' % (name, p))
                    check(det_int([[Pn]]) == Pn and sum(dec[i][0] ** 2
                                                       for i in range(k))
                          == Pn, 'Thm 6.5.5: Cartan matrix (p^n) (%s mod %d)'
                          % (name, p))
                    nblk += 1
                    continue
                # vertices: rows, the exceptional ones (equal rows) merged
                rows = {}
                for i, row in enumerate(dec):
                    rows.setdefault(tuple(row), []).append(i)
                verts = list(rows)
                mult = {v: len(rows[v]) for v in verts}
                exc = [v for v in verts if mult[v] > 1]
                check(len(exc) <= 1 and (not exc or mult[exc[0]] == mexc)
                      and len(verts) == l + 1,
                      'Thm 6.5.5: e + 1 vertices, one exceptional of '
                      'multiplicity (p^n - 1)/e (%s mod %d)' % (name, p))
                ok = all(set(row) <= {0, 1} for row in verts)
                edges = []
                for c in range(l):
                    ends = [v for v in verts if v[c]]
                    ok = ok and len(ends) == 2
                    edges.append(tuple(ends))
                from sage.all import Graph
                Gt = Graph([verts, edges], format='vertices_and_edges',
                           multiedges=True)
                check(ok and Gt.is_tree(),
                      'Thm 6.5.5: the decomposition matrix is that of a '
                      'Brauer tree with e edges (%s mod %d, e=%d)'
                      % (name, p, l))
                if mexc == 1:
                    mm = {v: 1 for v in verts}
                else:
                    mm = {v: (mexc if v in exc else 1) for v in verts}
                Ct = brauer_tree_cartan(edges, mm)
                Cd = [[sum(dec[i][a] * dec[i][c] for i in range(k))
                       for c in range(l)] for a in range(l)]
                check(Cd == Ct, 'Brauer tree algebra: Cartan matrix D^T D '
                      'equals that of the tree (%s mod %d)' % (name, p))
                check(det_int(Cd) == Pn,
                      'Thm 6.5.5: det of the Cartan matrix = p^n (%s mod %d)'
                      % (name, p))
                nblk += 1


# ===========================================================================
# Modules: Propositions 6.5.3, 6.5.4, Lemma 6.5.2 (MeatAxe)
# ===========================================================================


def pims(Gr, F, idem=None):
    """Projective indecomposable modules (one per isomorphism type) of the
    block with idempotent idem (dict), via the regular module."""
    gF = gap_field(F)
    gens = libgap.B6Gens(Gr.G)
    R = libgap.B6RegularMats(Gr.G, gens, gF)
    if idem is not None:
        reg = GModule(Gr, R, F)
        E = reg.alg(idem)
        W = libgap.BaseMat(E)
        R = libgap.eval('function(W, ms) return List(ms, m -> List(W, '
                        'w -> SolutionMat(W, w * m))); end')(W, R)
    mod = libgap.GModuleByMats(R, gF)
    out = []
    for s in MTX('Indecomposition')(mod):
        P = s[1]
        if not any(int(MTX('Dimension')(P)) == int(MTX('Dimension')(Q))
                   and MTX('IsomorphismModules')(P, Q) != libgap.eval('fail')
                   for Q in out):
            out.append(P)
    return out


def layers(P):
    return list(libgap.B6RadicalLayers(P))


def simple_index(S, simples):
    assert MTX('IsIrreducible')(S)
    for i, T in enumerate(simples):
        MTX('IsIrreducible')(T)
        if MTX('IsEquivalent')(S, T):
            return i
    raise ValueError


def uniserial_series(P, simples):
    """The radical layers of P as indices of simples, or None if some layer
    is not simple."""
    out = []
    for L in layers(P):
        if not MTX('IsIrreducible')(L):
            return None
        out.append(simple_index(L, simples))
    return out


def props_6_5_3_and_6_5_4():
    init_gap()
    cases = [  # (group, name, p, |D|, e)
        ('AlternatingGroup(4)', 'A4', 3, 3, 1),
        ('SL(2, 3)', 'SL(2,3)', 3, 3, 1),
        ('CyclicGroup(IsPermGroup, 9)', 'C9', 3, 9, 1),
        ('SymmetricGroup(3)', 'S3', 3, 3, 2),
        ('DihedralGroup(IsPermGroup, 18)', 'D18', 3, 9, 2),
        ('SmallGroup(21, 1)', 'C7:C3', 7, 7, 3),
        ('SmallGroup(20, 3)', 'C5:C4', 5, 5, 4),
        ('SmallGroup(24, 1)', 'C3:C8', 3, 3, 2),
        ('SymmetricGroup(4)', 'S4', 3, 3, 2),
        ('AlternatingGroup(5)', 'A5', 5, 5, 2),
        ('AlternatingGroup(5)', 'A5', 3, 3, 2),
    ]
    for gname, name, p, nD, e in cases:
        Gr = group(gname, name)
        B = blocks(Gr, p)
        dg, _ = defect_groups(Gr, B, Gr.p_subgroup_classes(p))
        F = B.F
        gF = gap_field(F)
        simples = list(libgap.IrreducibleModules(Gr.G, gF, 0)[1])
        for i, eB in enumerate(B.idems):
            D = dg[i][0]
            if len(D) != nD:
                continue
            Q = tuple(sorted({x for x in D if Gr.order[x] in (1, p)}))
            Ps = pims(Gr, F, B.to_group_algebra(eB))
            # heads of the projectives
            heads = [simple_index(layers(P)[0], simples) for P in Ps]
            check(len(Ps) == e, 'Thm 6.5.5 / Props 6.5.3-6.5.4: e = %d '
                  'simple modules in B (%s, p=%d)' % (e, name, p))
            dims = {int(MTX('Dimension')(simples[h])) for h in heads}
            ser = [uniserial_series(P, simples) for P in Ps]
            if Gr.is_normal(Q) or e == 1:
                check(all(s is not None and len(s) == nD for s in ser),
                      'Props 6.5.3/6.5.4: each P_S is uniserial of length '
                      'p^n = %d (%s, p=%d)' % (nD, name, p))
            if e == 1:
                check(all(len(set(s)) == 1 for s in ser),
                      'Prop. 6.5.3: one simple module S, all composition '
                      'factors of P_S isomorphic to S (%s, p=%d)'
                      % (name, p))
            if Gr.is_normal(Q):
                check(len(dims) == 1, 'Prop. 6.5.4: the e simple modules '
                      'have the same dimension (%s, p=%d)' % (name, p))
                # cyclic labelling: Rad^i P_j / Rad^(i+1) P_j = S_(i+j)
                nxt = {s[0]: s[1] for s in ser}
                cyc = [heads[0]]
                while len(cyc) < e:
                    cyc.append(nxt[cyc[-1]])
                pos = {h: t for t, h in enumerate(cyc)}
                check(sorted(cyc) == sorted(heads) and
                      all(pos[s[i]] == (pos[s[0]] + i) % e
                          for s in ser for i in range(len(s))),
                      'Prop. 6.5.4: Rad^i(P_j)/Rad^(i+1)(P_j) = S_(i+j), '
                      'indices mod e (%s, p=%d, e=%d)' % (name, p, e))
                # Lemma 6.5.2 / Thm 6.5.5: the e.p^n quotients P/Rad^i P
                quots = [(P, i2) for P in Ps for i2 in range(1, nD + 1)]
                ok, mods = True, []
                for P, i2 in quots:
                    rad = libgap.eval(
                        'function(P, i) local b, M, j, S; M := P; '
                        'b := IdentityMat(MTX.Dimension(P), MTX.Field(P)); '
                        'for j in [1..i] do '
                        'S := MTX.BasisRadical(M); '
                        'if Length(S) = 0 then b := []; break; fi; '
                        'b := S * b; '
                        'M := MTX.InducedActionSubmodule(M, S); od; '
                        'return b; end')(P, i2)
                    if int(libgap.Length(rad)) == 0:
                        Mq = P
                    else:
                        Mq = MTX('InducedActionFactorModule')(
                            P, libgap.BaseMat(rad))
                    ok = ok and bool(MTX('IsIndecomposable')(Mq))
                    for M2 in mods:
                        if MTX('Dimension')(M2) == MTX('Dimension')(Mq) and \
                                MTX('IsomorphismModules')(M2, Mq) != \
                                libgap.eval('fail'):
                            ok = False
                    mods.append(Mq)
                check(ok and len(mods) == e * nD,
                      'Lemma 6.5.2 / Thm 6.5.5: the quotients P_j / '
                      'Rad^i(P_j) are e.p^n = %d pairwise non-isomorphic '
                      'indecomposable (uniserial) modules (%s, p=%d)'
                      % (e * nD, name, p))


def heart(P):
    rad = MTX('BasisRadical')(P)
    R = MTX('InducedActionSubmodule')(P, rad)
    soc = MTX('BasisSocle')(R)
    if int(libgap.Length(soc)) == int(MTX('Dimension')(R)):
        return None if int(libgap.Length(soc)) == 0 else R
    return MTX('InducedActionFactorModule')(R, soc)


def brauer_tree_modules():
    """PIMs of cyclic blocks with Q not normal: P/Rad P = Soc P, and the
    heart Rad(P)/Soc(P) is a sum of at most two uniserial modules (the
    shape of Brauer tree algebras, Section 4.18)."""
    init_gap()
    for gname, name, p in [('AlternatingGroup(5)', 'A5', 5),
                           ('AlternatingGroup(5)', 'A5', 3),
                           ('SymmetricGroup(4)', 'S4', 3),
                           ('PSL(3, 2)', 'GL(3,2)', 7)]:
        Gr = group(gname, name)
        B = blocks(Gr, p)
        dg, _ = defect_groups(Gr, B, Gr.p_subgroup_classes(p))
        gF = gap_field(B.F)
        simples = list(libgap.IrreducibleModules(Gr.G, gF, 0)[1])
        for i, eB in enumerate(B.idems):
            if len(dg[i][0]) == 1:
                continue
            Ps = pims(Gr, B.F, B.to_group_algebra(eB))
            ok = True
            for P in Ps:
                L = layers(P)
                top = simple_index(L[0], simples)
                socm = MTX('InducedActionSubmodule')(P, MTX('BasisSocle')(P))
                ok = ok and bool(MTX('IsIrreducible')(socm))
                ok = ok and simple_index(socm, simples) == top
                Hm = heart(P)
                if Hm is None:
                    continue
                summ = MTX('Indecomposition')(Hm)
                ok = ok and len(summ) <= 2 and all(
                    uniserial_series(s[1], simples) is not None
                    for s in summ)
            check(ok, 'Thm 6.5.5: the projectives of the cyclic block are '
                  'biserial: P/Rad(P) = Soc(P) and Rad(P)/Soc(P) is a sum of '
                  'at most two uniserial modules (%s, p=%d, %d PIMs)'
                  % (name, p, len(Ps)))


def section_6_5():
    cartan_determinant_checks()
    for gname, name, primes in [
            ('AlternatingGroup(4)', 'A4', [3]),
            ('SymmetricGroup(4)', 'S4', [3]),
            ('AlternatingGroup(5)', 'A5', [3, 5]),
            ('SymmetricGroup(5)', 'S5', [3, 5]),
            ('SL(2, 3)', 'SL(2,3)', [3]),
            ('GL(2, 3)', 'GL(2,3)', [3]),
            ('SL(2, 5)', 'SL(2,5)', [3, 5]),
            ('PSL(3, 2)', 'GL(3,2)', [3, 7]),
            ('PSL(2, 8)', 'PSL(2,8)', [3, 7]),
            ('PSL(2, 11)', 'PSL(2,11)', [3, 5, 11]),
            ('PSL(2, 13)', 'PSL(2,13)', [3, 7, 13]),
            ('SymmetricGroup(3)', 'S3', [3]),
            ('DihedralGroup(IsPermGroup, 18)', 'D18', [3]),
            ('SmallGroup(21, 1)', 'C7:C3', [7]),
            ('SmallGroup(20, 3)', 'C5:C4', [5]),
            ('SmallGroup(24, 1)', 'C3:C8', [3])]:
        Gr = group(gname, name)
        for p in primes:
            cyclic_blocks(Gr, p)
    library_brauer_trees()
    props_6_5_3_and_6_5_4()
    brauer_tree_modules()


def endo_algebra_is_kV4(P, F):
    """End(P) (MeatAxe basis) is a local commutative algebra of dimension 4
    with J^2 one-dimensional and x^2 = 0 for x in J, i.e. isomorphic to
    k<x, y>/(x^2, y^2, xy - yx) = k(Z/2 x Z/2) in characteristic 2."""
    E = list(MTX('BasisModuleEndomorphisms')(P))
    if len(E) != 4:
        return False
    comm = all(a * b == b * a for a in E for b in E)
    n = int(MTX('Dimension')(P))
    gF = gap_field(F)
    rad = MTX('BasisRadical')(P)
    one = libgap.IdentityMat(n, gF)
    Jb = []
    for f in E:
        # scalar by which f acts on the top: pick a vector outside Rad
        w = libgap.eval('function(P, rad, f) local s, q, x; '
                        's := SemiEchelonMat(rad); '
                        'q := First([1..MTX.Dimension(P)], '
                        'j -> s.heads[j] = 0); '
                        'x := List([1..MTX.Dimension(P)], i -> '
                        'Zero(MTX.Field(P))); x[q] := One(MTX.Field(P)); '
                        'return SolutionMat(Concatenation(rad, [x]), x * f)'
                        '[Length(rad) + 1]; end')(P, rad, f)
        Jb.append(f - w * one)
    Jspan = libgap.BaseMat([libgap.Concatenation(f) for f in Jb])
    ok = int(libgap.Length(Jspan)) == 3
    ok = ok and all((f * f).IsZero() for f in Jb)
    J2 = libgap.BaseMat([libgap.Concatenation(a * b) for a in Jb
                         for b in Jb])
    ok = ok and int(libgap.Length(J2)) == 1
    return comm and ok


def is_semisimple(M):
    return int(libgap.Length(MTX('BasisRadical')(M))) == 0


def klein_blocks(Gr, p=2):
    """Blocks with Klein four defect group, with the inertial index e."""
    B = blocks(Gr, p)
    dg, _ = defect_groups(Gr, B, Gr.p_subgroup_classes(p))
    out = []
    for i in range(B.nblocks):
        D = dg[i][0]
        if len(D) != 4 or is_cyclic_group(Gr, D):
            continue
        C, N = Gr.centralizer(D), Gr.normalizer(D)
        Cr = sub_of(Gr, C, 'C_G(D)')
        BC = Blocks(Cr, p, mod=B.mod)
        brC = brauer_vec(Gr, B.idems[i], C, Cr)
        b1 = next(j for j, f in enumerate(BC.idems)
                  if BC.zmul(f, brC) == f)
        e1 = BC.idems[b1]
        T = [g for g in N if conj_central(Gr, Cr, g, e1) == e1]
        e = len(T) // len(C)
        out.append((i, D, e))
    return B, out


def section_6_6():
    init_gap()
    # Aut(Z/2 x Z/2) has order six, so e in {1, 3}
    A = libgap.AutomorphismGroup(libgap.SmallGroup(4, 2))
    check(int(A.Size()) == 6 and [d for d in ZZ(6).divisors() if d % 2]
          == [1, 3], 'p. 218: |Aut(D)| = 6 and e is 1 or 3')
    seen = []
    # Theorem 6.6.1 (e = 1), Theorem 6.6.2 (D normal, e = 3)
    cases = [('DirectProduct(SmallGroup(4, 2), CyclicGroup(3))',
              'V4xC3', 1),
             ('DirectProduct(SmallGroup(4, 2), SymmetricGroup(3))',
              'V4xS3', 1),
             ('DirectProduct(CyclicGroup(IsPermGroup, 2), '
              'SymmetricGroup(3))', 'C2xS3', 1),
             ('DirectProduct(SymmetricGroup(3), SymmetricGroup(3))',
              'S3xS3', 1),
             ('AlternatingGroup(4)', 'A4', 3),
             ('DirectProduct(AlternatingGroup(4), SymmetricGroup(3))',
              'A4xS3', 3),
             ('DirectProduct(AlternatingGroup(4), CyclicGroup(3))',
              'A4xC3', 3)]
    for gname, name, ewant in cases:
        Gr = group(gname, name)
        B, kb = klein_blocks(Gr)
        F = B.F
        gF = gap_field(F)
        simples = list(libgap.IrreducibleModules(Gr.G, gF, 0)[1])
        for i, D, e in kb:
            seen.append((name, e))
            check(e in (1, 3), 'p. 218: e = 1 or 3 (%s)' % name)
            Ps = pims(Gr, F, B.to_group_algebra(B.idems[i]))
            dimB = sum(int(B.irr[c][0]) ** 2 for c in B.block_chars[i])
            heads = [simple_index(layers(P)[0], simples) for P in Ps]
            dims = [int(MTX('Dimension')(simples[h])) for h in heads]
            check(len(Ps) == e, 'Thms 6.6.1-6.6.3: B has %d simple module(s) '
                  '(%s)' % (e, name))
            n = dims[0]
            if e == 1:
                P = Ps[0]
                Hm = heart(P)
                fac = [simple_index(c, simples)
                       for c in MTX('CompositionFactors')(Hm)]
                check(is_semisimple(Hm) and fac == [heads[0]] * 2,
                      'Thm 6.6.1: Rad(P_S)/Soc(P_S) = S + S (%s)' % name)
                check(endo_algebra_is_kV4(P, F),
                      'Thm 6.6.1: End_B(P_S) is isomorphic to kD (%s)' % name)
                check(dimB == 4 * n * n,
                      'Thm 6.6.1: B = Mat_n(kD), dim B = 4 n^2 (%s, n=%d)'
                      % (name, n))
                if not Gr.is_normal(D):
                    seen.append((name, 'D not normal'))
            else:
                check(len(set(dims)) == 1 and dimB == 12 * n * n,
                      'Thm 6.6.2: three simple modules of the same dimension '
                      'n and B = Mat_n(kA4), dim B = 12 n^2 (%s, n=%d)'
                      % (name, n))
                pos = {h: t for t, h in enumerate(heads)}
                ok = True
                for t, P in enumerate(Ps):
                    Hm = heart(P)
                    fac = sorted(pos[simple_index(c, simples)]
                                 for c in MTX('CompositionFactors')(Hm))
                    ok = ok and is_semisimple(Hm) and \
                        fac == sorted([(t - 1) % 3, (t + 1) % 3])
                check(ok, 'Thm 6.6.2: Rad(P_j)/Soc(P_j) = S_(j-1) + S_(j+1) '
                      '(%s)' % name)
    # control: the test above rejects k(Z/4) (End of the regular module)
    Gc = group('CyclicGroup(IsPermGroup, 4)', 'C4')
    gF4 = libgap.eval('GF(4)')
    regc = libgap.GModuleByMats(libgap.B6RegularMats(
        Gc.G, libgap.B6Gens(Gc.G), gF4), gF4)
    check(not endo_algebra_is_kV4(regc, GF(4, 'a')),
          'control: End(k(Z/4)) = k(Z/4) is not recognised as kV4')
    check(('C2xS3', 'D not normal') in seen,
          'Thm 6.6.1 checked also for D not normal (C2 x S3)')
    rotation_invariant_hearts()
    kA4_quiver_and_relations()
    principal_block_A5()
    psl2_principal_blocks()


def rotation_invariant_hearts():
    """Proof of Thm 6.6.2: the hearts Rad(P_j)/Soc(P_j) = S_(j+a) + S_(j+b)
    invariant under S_j -> S_(j+1): the Cartan matrix 2I + P^a + P^b."""
    good, pow2 = [], []
    for a, b in itertools.combinations_with_replacement(range(3), 2):
        C = [[2 * int(i == j) + int((j - i) % 3 == a) + int((j - i) % 3 == b)
              for j in range(3)] for i in range(3)]
        d = det_int(C)
        sym = all(C[i][j] == C[j][i] for i in range(3) for j in range(3))
        conn = (a, b) != (0, 0)
        if d > 0 and ZZ(d).is_power_of(2):
            pow2.append((a, b, d))
            if sym and conn:
                good.append((a, b))
    check(good == [(1, 2)],
          'Thm 6.6.2 (proof): among the rotation-invariant hearts only '
          'S_(j-1) + S_(j+1) gives a symmetric Cartan matrix of 2-power '
          'determinant with S_1, S_2, S_3 in one block')
    refuted(len(pow2) == 1,
            'printed p. 220: "the determinant of the Cartan matrix is a '
            'power of two ... leaves only one possibility" (2-power '
            'determinants: %s)' % pow2)


def kA4_quiver_and_relations():
    """Theorem 6.6.2: the quiver of p. 220 with the printed relations
    presents kA4; the scalar mu_3 is forced to 1 by symmetry."""
    F = GF(4, 'a')
    w = F.gen()
    # the algebra Lambda_mu: basis e_L, e_T, e_R, the six arrows, and the
    # loops s_L = beta alpha, s_R = epsilon zeta, s_T = gamma delta
    arrows = {'alpha': ('L', 'T'), 'beta': ('T', 'L'), 'gamma': ('R', 'T'),
              'delta': ('T', 'R'), 'epsilon': ('L', 'R'), 'zeta': ('R', 'L')}
    V = ['L', 'T', 'R']

    def algebra(mu1, mu2, mu3):
        basis = ['e' + v for v in V] + list(arrows) + ['s' + v for v in V]
        idx = {b: i for i, b in enumerate(basis)}
        # products xy = "first y then x" (paths compose right to left)
        two = {}   # (x, y) -> (coefficient, basis element)
        # loops: beta alpha = mu1 zeta epsilon = s_L; epsilon zeta =
        # mu2 delta gamma = s_R; gamma delta = mu3 alpha beta = s_T
        two[('beta', 'alpha')] = (F(1), 'sL')
        two[('zeta', 'epsilon')] = (~F(mu1), 'sL')
        two[('epsilon', 'zeta')] = (F(1), 'sR')
        two[('delta', 'gamma')] = (~F(mu2), 'sR')
        two[('gamma', 'delta')] = (F(1), 'sT')
        two[('alpha', 'beta')] = (~F(mu3), 'sT')
        n = len(basis)

        def src_tgt(b):
            if b[0] == 'e' and len(b) == 2:
                return (b[1], b[1])
            if b[0] == 's' and len(b) == 2:
                return (b[1], b[1])
            return arrows[b]

        def deg(b):
            return 0 if b[0] == 'e' and len(b) == 2 else (
                2 if b[0] == 's' and len(b) == 2 else 1)

        def mul(x, y):
            v = [F(0)] * n
            sx, tx = src_tgt(x)
            sy, ty = src_tgt(y)
            if sx != ty:
                return v
            if deg(x) == 0:
                v[idx[y]] = F(1)
            elif deg(y) == 0:
                v[idx[x]] = F(1)
            elif deg(x) == 1 and deg(y) == 1 and (x, y) in two:
                c, b = two[(x, y)]
                v[idx[b]] = c
            return v
        table = [[mul(x, y) for y in basis] for x in basis]
        return basis, table

    def prod(table, u, v):
        n = len(u)
        out = [F(0)] * n
        for i in range(n):
            if u[i]:
                for j in range(n):
                    if v[j]:
                        c = u[i] * v[j]
                        for k, t in enumerate(table[i][j]):
                            if t:
                                out[k] += c * t
        return out

    basis, table = algebra(1, 1, 1)
    n = len(basis)
    units = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    ok = all(prod(table, prod(table, units[a], units[b]), units[c]) ==
             prod(table, units[a], prod(table, units[b], units[c]))
             for a in range(n) for b in range(n) for c in range(n))
    check(ok and n == 12, 'Thm 6.6.2: the quiver with the printed relations '
          'gives an associative algebra of dimension 12 = dim kA4')
    zero = ['delta alpha', 'beta gamma', 'alpha zeta', 'epsilon beta',
            'zeta delta', 'gamma epsilon']
    check(all(not any(table[basis.index(z.split()[0])]
                      [basis.index(z.split()[1])]) for z in zero),
          'Thm 6.6.2: the six printed zero relations hold (each a path of '
          'length two between distinct vertices)')
    # symmetric iff mu1 mu2 mu3 = 1 (all 27 choices over GF(4))
    units4 = [x for x in F if x]
    res = []
    for mus in itertools.product(units4, repeat=3):
        _, tab = algebra(*mus)
        res.append((mus[0] * mus[1] * mus[2] == 1) == is_symmetric(F, tab))
    check(all(res), 'Thm 6.6.2: Lambda_mu is a symmetric algebra iff '
          'mu1 mu2 mu3 = 1 (all 27 triples over GF(4)); so mu1 = mu2 = 1 '
          'forces mu3 = 1')
    # an explicit isomorphism with kA4 over GF(4)
    Gr = group('AlternatingGroup(4)', 'A4')
    V4 = [x for x in Gr.all if Gr.order[x] <= 2]
    c = next(x for x in Gr.all if Gr.order[x] == 3)
    c2 = Gr.mul[c][c]
    idem = []
    for j in range(3):
        idem.append({0: F(1), c: w ** (-j), c2: w ** (-2 * j)})
    ga = lambda a, b: ga_mul(Gr, a, b)
    one = {0: F(1)}
    tot = {}
    for d in idem:
        for x, cc in d.items():
            tot[x] = tot.get(x, F(0)) + cc
    tot = {x: cc for x, cc in tot.items() if cc}
    check(tot == one and all(ga(idem[i], idem[j]) == (idem[i] if i == j
                                                      else {})
                             for i in range(3) for j in range(3)),
          'kA4: e_j = sum_t omega^(-jt) c^t are orthogonal idempotents with '
          'sum 1')
    J0 = [{0: F(1), v: F(1)} for v in V4 if v]         # 1 + v, v in V4
    J = [ga(a, {g: F(1)}) for a in J0 for g in Gr.all]
    # choose for each arrow s -> t an element of e_t J e_s not in J^2
    vert = {'L': 0, 'T': 1, 'R': 2}
    J2 = [ga(a, b) for a in J0 for b in J0]

    def in_span(vecs, d):
        S = Span(F, Gr.n, [[v.get(x, F(0)) for x in Gr.all] for v in vecs])
        return [d.get(x, F(0)) for x in Gr.all] in S
    J2all = [ga(a, {g: F(1)}) for a in J2 for g in Gr.all]
    phi = {}
    for name_, (s, t) in arrows.items():
        cand = None
        for a in J:
            x = ga(ga(idem[vert[t]], a), idem[vert[s]])
            if x and not in_span(J2all, x):
                cand = x
                break
        phi[name_] = cand
    check(all(v is not None for v in phi.values()),
          'kA4: each arrow is realised by an element of e_t J e_s not in J^2')
    # scalars mu: beta alpha = mu1 zeta epsilon etc.
    def ratio(x, y):
        k = next(z for z in x)
        r = x[k] / y[k]
        assert {z: r * cc for z, cc in y.items()} == x
        return r
    mu1 = ratio(ga(phi['beta'], phi['alpha']), ga(phi['zeta'], phi['epsilon']))
    mu2 = ratio(ga(phi['epsilon'], phi['zeta']),
                ga(phi['delta'], phi['gamma']))
    mu3 = ratio(ga(phi['gamma'], phi['delta']), ga(phi['alpha'], phi['beta']))
    check(mu1 and mu2 and mu3 and mu1 * mu2 * mu3 == 1,
          'kA4: the relations hold with non-zero mu_i, mu1 mu2 mu3 = 1')
    # rescale zeta, delta (as on p. 220) and map the basis
    phi['zeta'] = {x: mu1 * cc for x, cc in phi['zeta'].items()}
    phi['delta'] = {x: mu1 * mu2 * cc for x, cc in phi['delta'].items()}
    img = {'eL': idem[0], 'eT': idem[1], 'eR': idem[2]}
    img.update(phi)
    img['sL'] = ga(phi['beta'], phi['alpha'])
    img['sR'] = ga(phi['epsilon'], phi['zeta'])
    img['sT'] = ga(phi['gamma'], phi['delta'])
    vecs = [[img[b].get(x, F(0)) for x in Gr.all] for b in basis]
    S = Span(F, Gr.n, vecs)
    hom = all(ga(img[basis[a]], img[basis[b]]) ==
              {x: cc for x, cc in
               ((x, sum((table[a][b][k] * img[basis[k]].get(x, F(0))
                         for k in range(n)), F(0))) for x in Gr.all) if cc}
              for a in range(n) for b in range(n))
    check(S.dim() == 12 and hom, 'Thm 6.6.2: an explicit isomorphism from '
          'the algebra of the quiver with relations (mu = 1) onto kA4')


def is_symmetric(F, tab):
    """Is there a linear form lambda with lambda(xy) = lambda(yx) whose
    bilinear form lambda(xy) is non-degenerate?  (Enumerates the forms
    vanishing on commutators.)"""
    n = len(tab)
    comms = [[a - b for a, b in zip(tab[i][j], tab[j][i])]
             for i in range(n) for j in range(n)]
    # lambda in the annihilator of the commutators: kernel of the map
    # lambda -> (lambda(c))_c, computed as the kernel of the transpose
    cols = [[c[k] for c in comms] for k in range(n)]
    ker = kernel(F, cols, len(comms))
    for coeffs in itertools.product(list(F), repeat=len(ker)):
        lam = [sum((cf * v[k] for cf, v in zip(coeffs, ker)), F(0))
               for k in range(n)]
        if not any(lam):
            continue
        G = [[sum((lam[k] * tab[i][j][k] for k in range(n)), F(0))
              for j in range(n)] for i in range(n)]
        if Span(F, n, G).dim() == n:
            return True
    return False


def principal_block_A5():
    Gr = group('AlternatingGroup(5)', 'A5')
    B = blocks(Gr, 2)
    F = GF(4, 'a')
    gF = libgap.eval('GF(4)')
    # over GF(4) (a splitting field for A5): idempotent of B_0 is rational
    e0 = B.idem_cyc[B.principal]
    d = {}
    for k, K in enumerate(Gr.classes):
        c = QQ(e0[k].sage())
        if c:
            for x in K:
                d[x] = F(c)
    simples = list(libgap.IrreducibleModules(Gr.G, gF, 0)[1])
    Ps = pims(Gr, F, d)
    heads = [simple_index(layers(P)[0], simples) for P in Ps]
    dims = [int(MTX('Dimension')(simples[h])) for h in heads]
    check(sorted(dims) == [1, 2, 2] and
          sorted(int(MTX('Dimension')(P)) for P in Ps) == [8, 8, 12],
          'Thm 6.6.3 (ii): B_0(kA5) has simple modules of dimensions 1, 2, 2 '
          'and projective covers of dimensions 12, 8, 8')
    i1 = dims.index(1)
    S1 = heads[i1]
    others = [h for h in heads if h != S1]
    # label S_2, S_3 so that the heart of P_2 is Uni(S_1, S_3, S_1)
    hearts = {}
    for P, h in zip(Ps, heads):
        Hm = heart(P)
        hearts[h] = [uniserial_series(s[1], simples)
                     for s in MTX('Indecomposition')(Hm)]
    S2 = others[0]
    S3 = others[1]
    check(hearts[S2] == [[S1, S3, S1]] and hearts[S3] == [[S1, S2, S1]],
          'Thm 6.6.3 (ii): Rad(P_2)/Soc(P_2) = Uni(S_1, S_3, S_1) and '
          'Rad(P_3)/Soc(P_3) = Uni(S_1, S_2, S_1)')
    check(sorted(map(tuple, hearts[S1])) ==
          sorted([(S2, S1, S3), (S3, S1, S2)]),
          'Thm 6.6.3 (ii): Rad(P_1)/Soc(P_1) = Uni(S_2, S_1, S_3) + '
          'Uni(S_3, S_1, S_2)')
    # Cartan matrix and determinant
    order = [S1, S2, S3]
    Cm = []
    for P, h in sorted(zip(Ps, heads), key=lambda t: order.index(t[1])):
        fac = [simple_index(c, simples)
               for c in MTX('CompositionFactors')(P)]
        Cm.append([fac.count(s) for s in order])
    check(Cm == [[4, 2, 2], [2, 2, 1], [2, 1, 2]] and det_int(Cm) == 4,
          'B_0(kA5): Cartan matrix [[4,2,2],[2,2,1],[2,1,2]], determinant 4')
    # Ext-quiver: Rad(P)/Rad^2(P)
    ok = True
    for P, h in zip(Ps, heads):
        L = layers(P)
        fac = sorted(simple_index(c, simples)
                     for c in MTX('CompositionFactors')(L[1]))
        want = sorted([S2, S3]) if h == S1 else [S1]
        ok = ok and fac == want
    check(ok, 'B_0(kA5): Ext^1(S_1, S_2) = Ext^1(S_1, S_3) = k, no other '
          'extensions between the simples')
    # the two-dimensional simple module restricted to a Sylow 2-subgroup
    V4 = Gr.sylow(2)
    Vg = Gr.to_gap(V4)
    for h in (S2, S3):
        S = simples[h]
        Mo = GModule(Gr, MTX('Generators')(S), F)
        idm = libgap.IdentityMat(2, gF)
        res = libgap.GModuleByMats(Mo.sub(idm, Vg), gF)
        check(MTX('IsIndecomposable')(res),
              'p. 223: the 2-dimensional simple kA5-module restricted to a '
              'Sylow 2-subgroup is indecomposable')
        # Omega(M) = M for this restriction (periodic, period one)
        reg = libgap.GModuleByMats(libgap.B6RegularMats(
            Vg, libgap.B6Gens(Vg), gF), gF)
        homs = MTX('BasisModuleHomomorphisms')(reg, res)
        surj = next(f for f in homs if int(libgap.RankMat(f)) == 2)
        ker = libgap.NullspaceMat(surj)
        om = MTX('InducedActionSubmodule')(reg, ker)
        check(MTX('IsomorphismModules')(om, res) != libgap.eval('fail'),
              'p. 223: that restriction M satisfies Omega(M) = M (periodic)')
    # Knoerr (Remark p. 223): D is a vertex of every simple module in B_0
    for h in heads:
        mats = MTX('Generators')(simples[h])
        Mo = GModule(Gr, mats, F)
        proper = [Gr.to_gap(Gr.from_gap(H)) for H in Vg.MaximalSubgroups()]
        check(not any(bool(libgap.B6IdInTransfer(Gr.G, mats, Q, gF))
                      for Q in proper),
              'Remark p. 223 (Knoerr): the defect group V4 is a vertex of '
              'each simple module of B_0(kA5)')


def psl2_principal_blocks():
    """Theorem 6.6.3: the principal 2-block of PSL(2, q), q = +-3 mod 8,
    has the Cartan matrix of kA4 or of B_0(kA5) (Cartan matrices are
    Morita invariants); GAP character table library."""
    CA5 = [[4, 2, 2], [2, 2, 1], [2, 1, 2]]
    assert libgap.LoadPackage('ctbllib')
    found = {}
    for q in [5, 11, 13, 19, 27, 29, 37, 43, 53, 59, 61]:
        t = libgap.CharacterTable('L2(%d)' % q)
        if t == libgap.eval('fail'):
            continue
        m = libgap.eval('function(t) return t mod 2; end')(t)
        if m == libgap.eval('fail'):
            continue
        info = libgap.BlocksInfo(m)
        b0 = next(i for i, b in enumerate(info)
                  if 1 in [int(x) for x in b['ordchars']])
        dec = [[int(x) for x in row]
               for row in libgap.DecompositionMatrix(m, b0 + 1)]
        l = len(dec[0])
        Cm = [[sum(r[a] * r[c] for r in dec) for c in range(l)]
              for a in range(l)]
        typ = None
        for perm in itertools.permutations(range(3)):
            P = [[Cm[perm[a]][perm[c]] for c in range(3)] for a in range(3)]
            if P == CA5:
                typ = 'A5'
            if P == [[2, 1, 1], [1, 2, 1], [1, 1, 2]]:
                typ = 'A4'
        check(l == 3 and typ is not None and int(info[b0]['defect']) == 2,
              'Thm 6.6.3: the principal 2-block of PSL(2, %d) (defect group '
              'Klein four) has three simple modules and the Cartan matrix of '
              'kA4 or of B_0(kA5)' % q)
        found[q] = typ
    check(set(found.values()) == {'A4', 'A5'},
          'Thm 6.6.3: both Morita types occur among the PSL(2, q)')


def cor_6_3_5_support():
    """Proof of Cor. 6.3.5: a non-cyclic p-group has a quotient
    Z/p x Z/p (all groups of order p^n, n <= 6 for p = 2, n <= 4 for p = 3,
    5); and k(N_G(D)/D) has a summand in every block of k N_G(D)."""
    for p, top in [(2, 6), (3, 4), (5, 3)]:
        bad = 0
        tot = 0
        for n in range(1, top + 1):
            for i in range(1, int(libgap.NumberSmallGroups(p ** n)) + 1):
                P = libgap.SmallGroup(p ** n, i)
                tot += 1
                cyc = bool(P.IsCyclic())
                rank = len(libgap.AbelianInvariants(
                    P.FactorGroup(P.FrattiniSubgroup())))
                if cyc == (rank >= 2):
                    bad += 1
        check(bad == 0, 'Cor. 6.3.5 (proof): a p-group is non-cyclic iff it '
              'has a quotient Z/p x Z/p (all %d groups of order p^n <= %d, '
              'p=%d)' % (tot, p ** top, p))
    init_gap()
    for gname, name, p in [('AlternatingGroup(5)', 'A5', 2),
                           ('SymmetricGroup(4)', 'S4', 2),
                           ('PSL(3, 2)', 'GL(3,2)', 2),
                           ('SymmetricGroup(5)', 'S5', 3)]:
        Gr = group(gname, name)
        for D in Gr.p_subgroup_classes(p):
            if len(D) == 1:
                continue
            N = Gr.normalizer(D)
            Nr = sub_of(Gr, N, 'N_G(D)')
            BN = Blocks(Nr, p, mod=blocks(Gr, p).mod)
            DN = tuple(sorted(Nr.from_G[x] for x in D))
            P = GModule.permutation(Nr, DN, BN.F)
            ok = all(not P.alg(BN.to_group_algebra(e)).IsZero()
                     for e in BN.idems)
            check(ok, 'Cor. 6.3.5 (proof): k(N_G(D)/D) has summands in every '
                  'block of k N_G(D) (%s, p=%d, |D|=%d)'
                  % (name, p, len(D)))


def prop_6_4_4():
    init_gap()
    cases = [('SL(2, 5)', 'SL(2,5)', 2, 'centre'),
             ('DirectProduct(CyclicGroup(IsPermGroup, 3), '
              'AlternatingGroup(5))', 'C3xA5', 3, 'centre'),
             ('DirectProduct(DihedralGroup(IsPermGroup, 8), '
              'SymmetricGroup(3))', 'D8xS3', 2, 'D8')]
    for gname, name, p, which in cases:
        Gr = group(gname, name)
        if which == 'centre':
            D = Gr.from_gap(Gr.G.Centre().SylowSubgroup(p))
        else:
            D = next(Gr.from_gap(H) for H in Gr.G.NormalSubgroups()
                     if int(H.Size()) == 8 and not H.IsAbelian())
        check(Gr.is_normal(D) and len(Gr.closure(list(D) + list(
            Gr.centralizer(D)))) == Gr.n,
              'Prop. 6.4.4: D normal and G = D C_G(D) (%s)' % name)
        B = blocks(Gr, p)
        dg, _ = defect_groups(Gr, B, Gr.p_subgroup_classes(p))
        F = B.F
        gF = gap_field(F)
        nb = 0
        for i, e in enumerate(B.idems):
            if not Gr.are_conj(dg[i][0], D):
                continue
            nb += 1
            Ps = pims(Gr, F, B.to_group_algebra(e))
            dimB = sum(int(B.irr[c][0]) ** 2 for c in B.block_chars[i])
            S = layers(Ps[0])[0]
            n = int(MTX('Dimension')(S))
            check(len(Ps) == 1 and dimB == n * n * len(D),
                  'Prop. 6.4.4: B has one simple module S and dim B = '
                  'n^2 |D| (n = dim S) (%s, p=%d, n=%d)' % (name, p, n))
            # P_S restricted to D is free of rank n (as for Mat_n(kD))
            P = Ps[0]
            Mo = GModule(Gr, MTX('Generators')(P), F)
            Dg = Gr.to_gap(D)
            res = libgap.GModuleByMats(Mo.sub(libgap.IdentityMat(
                Mo.n, gF), Dg), gF)
            reg = libgap.GModuleByMats(libgap.B6RegularMats(
                Dg, libgap.B6Gens(Dg), gF), gF)
            summ = MTX('Indecomposition')(res)
            check(len(summ) == n and all(
                MTX('IsomorphismModules')(s[1], reg) != libgap.eval('fail')
                for s in summ),
                'Prop. 6.4.4: P_S restricted to D is free of rank n, and '
                'End_B(P_S) has dimension |D| (%s)' % name)
            check(len(list(MTX('BasisModuleEndomorphisms')(P))) == len(D),
                  'Prop. 6.4.4: dim End_B(P_S) = |D| (%s)' % name)
        check(nb >= 1, 'Prop. 6.4.4: a block with defect group D exists '
              '(%s)' % name)


def prop_6_5_3_layers():
    """Proof of Prop. 6.5.3: for Q = <g> central of order p,
    (g - 1)^j kG / (g - 1)^(j+1) kG = k[G/Q] for j < p, (g - 1)^p = 0."""
    init_gap()
    for gname, name, p in [('SL(2, 3)', 'SL(2,3)', 2),
                           ('DirectProduct(CyclicGroup(IsPermGroup, 3), '
                            'SymmetricGroup(3))', 'C3xS3', 3),
                           ('DirectProduct(CyclicGroup(IsPermGroup, 5), '
                            'CyclicGroup(IsPermGroup, 4))', 'C5xC4', 5)]:
        Gr = group(gname, name)
        Z = Gr.from_gap(Gr.G.Centre().SylowSubgroup(p))
        Q = Gr.closure([next(x for x in Z if Gr.order[x] == p)])
        g = next(x for x in Q if x)
        F = GF(p)
        gF = gap_field(F)
        R = GModule(Gr, libgap.B6RegularMats(Gr.G, libgap.B6Gens(Gr.G), gF),
                    F)
        # left multiplication by g - 1 commutes with the right regular
        # action; its matrix on row vectors
        els = list(Gr.G.AsSSortedList())
        gg = Gr.gap_el(g)
        Lg = libgap.PermutationMat(libgap.PermList(
            [els.index(gg * x) + 1 for x in els]), Gr.n, gF)
        X = Lg - libgap.IdentityMat(Gr.n, gF)
        check((X ** p).IsZero(), '(g - 1)^p = 0 (%s)' % name)
        quot = GModule.permutation(Gr, Q, F)
        qmod = libgap.GModuleByMats(quot.mats, gF)
        ok = True
        for j in range(p):
            A = libgap.BaseMat(X ** j)
            Bb = libgap.BaseMat(X ** (j + 1))
            Mj = libgap.GModuleByMats(R.sub(A, Gr.G), gF)
            sub = libgap.eval('function(A, B) return List(B, b -> '
                              'SolutionMat(A, b)); end')(A, Bb) \
                if int(libgap.Length(Bb)) else libgap([])
            if int(libgap.Length(Bb)):
                fac = MTX('InducedActionFactorModule')(Mj, libgap.BaseMat(sub))
            else:
                fac = Mj
            ok = ok and MTX('IsomorphismModules')(fac, qmod) != \
                libgap.eval('fail')
        check(ok, 'Prop. 6.5.3 (proof): (g - 1)^j kG / (g - 1)^(j+1) kG = '
              'k[G/Q], j = 0..p-1 (%s, p=%d)' % (name, p))


def main():
    section_6_1()
    section_6_2()
    section_6_3()
    cor_6_3_5_support()
    section_6_4()
    prop_6_4_4()
    section_6_5()
    prop_6_5_3_layers()
    section_6_6()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
