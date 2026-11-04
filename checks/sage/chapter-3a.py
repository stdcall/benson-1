"""Exact checks of Chapter 3, Sections 3.1-3.7 (Sage, with GAP via libgap).

Benson, *Representations and Cohomology I*, second edition (1998),
Chapter 3 "Modules for group algebras", the introduction and Sections
3.1-3.7, printed pp. 49-79.  Our files: content/03-00-group-algebras.typ
... content/03-07-low-degree-cohomology.typ.  (Sections 3.8-3.15 are
checked in another script.)

The chapter is mostly general theory.  Everything below is an exact
computation over finite fields, ZZ or QQ for small groups (cyclic groups,
C2 x C2, C2^3, C3 x C3, S3, D8, Q8, A4, S4, S5): explicit modules given by
matrices, linear algebra, Smith normal forms, and the GAP MeatAxe (through
libgap) for decompositions and isomorphism tests of modules.  Projective
resolutions are built by linear algebra (no GAP package is used).  Expected
values are the book's statements and formulas, read off the printed pages
(the page and our label are named in each message); the chapter files are
not parsed.  Where the printed text was corrected, the printed reading is
kept as a refuted check next to the corrected one.

Checked here (by section):

3.1 (pp. 49-56)
  * Proposition 3.1.2: lambda(ab) is a symmetric non-degenerate form on kG;
    Soc(P) ~ P/Rad(P) for every projective indecomposable (MeatAxe) for S3,
    A4, D8, Q8, C3 x C3 over GF(2), GF(3), GF(4).
  * Hopf algebra structure of RG (p. 52): Delta and eta are an algebra map
    and an anti-automorphism with eta^2 = 1, antipode identity, on random
    elements of GF(3)S3; grouplike elements of GF(5)C4 and GF(5)(C2 x C2)
    (exhaustive): exactly the group, although the two algebras are both
    GF(5)^4 (16 idempotents each, 4 algebra maps to GF(5)).
  * Hom_k(M, N) ~ M* (x) N and M** ~ M as modules (p. 52).
  * Proposition 3.1.5: the explicit isomorphism of the proof from the
    induced to the diagonal structure on Lambda (x) M.
  * Corollary 3.1.6, Theorem 3.1.9, Proposition 3.1.10 for all Jordan
    blocks of C_q, q in {2, 3, 4, 5, 8, 9}; Theorem 3.1.9 also for the six
    indecomposable GF(3)S3-modules and for k, Omega(k), Omega^-1(k) and
    permutation modules of D8 over GF(2) (absolutely indecomposable modules
    over a finite field; the theorem is stated for algebraically closed k).
  * Propositions 3.1.7, 3.1.8 (i)-(iii) (dimensions of Hom and Ext^1, Ext^2)
    for modules of S3, A4, D8.
  * Proposition 3.1.10: the maps M -> M (x) M* (x) M -> M of the proof.

3.2 (pp. 56-60)
  * Corollary 2.7.2 (not 2.7.3) gives the homology of the tensor product of
    the two truncated complexes (checked on an example over GF(3)C3).
  * The map of (m + n)-fold extensions in the proof of Proposition 3.2.1,
    with the maps phi_i of the text, for m = n = 1 over GF(3)C3.
  * Graded commutativity of the cup product (Alexander-Whitney cochains) in
    H*(C3 x C3, GF(3)), H*(C3, GF(3)), H*(C2 x C2, GF(2)).

3.3 (pp. 60-62)
  * Proposition 3.3.1 and the exterior trace map, Corollary 3.3.2 (Ext^1,
    Ext^2), Proposition 3.3.3, induction = co-induction; Mackey
    decomposition (Theorem 3.3.4) as module isomorphisms (MeatAxe) for 18
    triples (G, H, K, M) in S4, A4, Q8, D8 over GF(2), GF(3); Corollary
    3.3.5 (i), (ii) as isomorphisms (modules of dimension <= 48), (iii),
    (iv) as dimensions for all 18, (vi) for n <= 2 (the corrected (iii),
    with the restriction).

3.4 (pp. 63-65)
  * Standard resolution of S3 and C3: d d = 0, the contraction identity,
    bar notation and its boundary formula, the coboundary formula, the
    Alexander-Whitney map (chain map, co-associative, bar form).
  * Inflation (corrected: resolutions of R): the coset map is a chain map
    over the identity of R; the printed reading (resolutions of M) gives
    Ext(M, M), refuted for C2, R = ZZ, M = ZZ/2.  The five-term sequence of
    the exercise (exactness at H^1(G/N), H^1(G), and the dimension count at
    H^1(N)^{G/N}, H^2(G/N)) for 12 pairs (G, N) in D8, Q8, A4, S3, C9; the
    image of restriction lies in the G/N-fixed points.

3.5 (pp. 65-68)
  * Proposition 3.5.1 (exact over ZZ, n <= 8, degrees <= 6); Corollary 3.5.2
    against bar cochains (ZZ and finite fields, several modules);
    Corollary 3.5.3 (A4 over GF(3), H = C2 x C2); Corollary 3.5.4; the
    facts of the computation of H*(Z/n, k) (projective cover of k,
    Omega(k), Omega^2(k) ~ k); Proposition 3.5.5 by the Cartan-Eilenberg
    diagonal (n <= 12) and independently by Alexander-Whitney cochains
    (Z/n, n in {2, 3, 4, 5, 6, 8, 9}, degrees <= 4).
  * The diagonal approximation Delta_rs (p. 67): with 0 <= i < j <= n - 1
    and T = x - 1 (Cartan-Eilenberg) it is a chain map (n = 2..8, total
    degree <= 6), as in Brown, Cohomology of Groups, V.1, Exercise (p. 108);
    the printed i <= j is refuted; with T = 1 - x of Proposition 3.5.1 the
    odd-odd component changes sign.
  * Theorem 3.5.6 (Kuenneth): H^n(C_a x C_b, ZZ) for 6 pairs, n <= 6, from
    the tensor product of the periodic resolutions (whose exactness is
    checked); the corrected Tor term in degree n + 1 holds, the printed
    n - 1 is refuted; H^2 = G^ab and H^3 = M(G) (GAP) independently.  The
    added hypothesis (M_1 or M_2 projective over R): with M_1 = ZZ,
    M_2 = ZZ/p the sequence holds, with M_1 = M_2 = ZZ/p it fails.
  * Remark and Corollary 3.5.7: dim H^n((Z/p)^s, GF(p)) = binom(n+s-1, s-1)
    and the ring structure in degrees <= 3 for (Z/2)^2, (Z/2)^3, (Z/3)^2.

3.6 (pp. 68-75)
  * Lemma 3.6.3 (iii)-(vi) on random maps (S4); Higman's criterion
    (Proposition 3.6.4 (v) <=> (vii)) for 84 triples (G, H, M) (38 with M
    relatively H-projective, 46 without) in S3, A4, D8; Corollaries
    3.6.9-3.6.12 and the Remark (the author's correction 1/|G| is checked;
    the printed sum is refuted).
  * Transfer in cohomology (corrected paragraph): Tr(alpha) o d = Tr(alpha
    o d) on resolutions; the printed second identity has mismatched
    domains.  Lemma 3.6.16 (iv) (Mackey formula, corrected restriction from
    lconj(g, K)) on cochains; the printed res_(K, H cap gK) is undefined
    for some double cosets.
  * Proposition 3.6.17: Tr res = |G : H| on cochains; the corrected second
    sentence (M projective over R) on the integral computations of 3.5;
    the printed sentence refuted by Ext^1_(ZZ C2)(ZZ/3, ZZ) ~ ZZ/3.
  * Corollary 3.6.18; Corollary 3.6.19 for S3 (p = 2) and A4 (p = 3) with
    M = k; the corrected hypothesis (M projective over R): for R = ZZ_(2),
    G = S3, M = M' = V (2-dimensional, killed by 2) restriction to N_G(P)
    on Ext^1 is not surjective.  (Ext over ZZ_(2) G of these 2-torsion
    modules equals Ext over ZZ G tensored with ZZ_(2), i.e. Ext over ZZ G;
    it is computed over ZZ.)
  * The Example (p. 74-75): H^n(S_p, k), H^n(S_p, sign) for p = 3, 5,
    n <= 8.

3.7 (pp. 75-79)
  * Proposition 3.7.2: |H^1(G, M)| = number of conjugacy classes of
    complements (GAP) for 8 pairs, and the conjugation formula
    beta' - beta = (1 - g)(m - beta[g']) exhaustively.
  * Proposition 3.7.3: associativity <=> cocycle; the 8 classes of
    H^2(C2 x C2, GF(2)) give C2^3 (split), C4 x C2 (3), D8 (3), Q8 (1); 27
    classes for H^2(C3 x C3, GF(3)); cohomologous cocycles give isomorphic
    extensions.  (The split of the 8 classes by isomorphism type is the
    classical count, not stated in the book.)  Corollary 3.7.4.
  * Proposition 3.7.5 (corrected kernel ZZ/m, m | |G|_p'): finite fields
    and RR (algebraic reals); the printed ZZ/|G|_p' is refuted by GF(8),
    GF(2) and RR with |G| = 3.  The Pauli lift of C2 x C2 (order 8, centre
    of order 2).  Remark (i) with the corrected <QQ^x, sqrt 2>.
  * The exercise H^1(G, R) = Hom(G, R^+) for 6 groups and R = GF(2), GF(3),
    ZZ/4.
  * The example before Theorem 3.7.8 ((2^(i-1) + 1) over ZZ/2^i);
    Theorem 3.7.8: the kernels in the corrected diagram are
    End(M~ / p^(r+1) M~) and the vertical map is p^r (printed p^(r-1)
    refuted by orders); the conclusion exhaustively for C2 (n <= 2, a = 3)
    and C4 (n = 1, a = 5).

Not established: none of the general theorems is proved here.  Every
check concerns the listed groups, fields, modules and degrees only;
resolutions are truncated at the stated degree; MeatAxe isomorphism tests
are exact for the given modules.  Cohomology over fields is computed from
resolutions built here by linear algebra (cross-checked during writing
against GAP's HAP package, which is not used by this script).  Nothing here
compares our Typst text with the printed book.

Run with:  sage -python checks/sage/chapter-3a.py
"""
import itertools
import random

from sage.all import (
    AA, GF, QQ, ZZ, AlternatingGroup, CyclicPermutationGroup, DihedralGroup,
    PermutationGroup, PolynomialRing, QuaternionGroup, SymmetricGroup,
    binomial, block_matrix, factor, gcd, libgap, set_random_seed, vector,
)
from sage.all import identity_matrix as _identity_matrix
from sage.all import matrix as dmatrix
from sage.all import zero_matrix as _zero_matrix

SCOPE = 'chapter-3a'
COUNT = [0]
random.seed(20261104)
set_random_seed(20261104)


# Products of dense matrices over finite rings of odd characteristic go
# through the local OpenBLAS build, which stops with SIGILL on this machine;
# such matrices are created sparse (exact all the same).  Pure rank and
# kernel computations use dense copies ("dmatrix", no products).
def _sparse(R):
    try:
        return R.is_finite() and R.characteristic() != 2
    except (AttributeError, NotImplementedError):
        return False


def matrix(*args, **kw):
    if args and _sparse(args[0]):
        kw.setdefault('sparse', True)
    return dmatrix(*args, **kw)


def identity_matrix(R, n):
    return _identity_matrix(R, n, sparse=_sparse(R))


def zero_matrix(R, r, c=None):
    return _zero_matrix(R, r, r if c is None else c, sparse=_sparse(R))


def sp(A):
    return A.sparse_matrix() if _sparse(A.base_ring()) else A


def kernel_basis(A):
    return A.dense_matrix().right_kernel().basis()


def check(cond, what):
    """One check of a statement of the book; fails loudly."""
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    """The printed reading, kept beside the corrected one: it must fail."""
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


# ===========================================================================
# Finite groups as multiplication tables
# ===========================================================================


class FinGroup:
    """A finite group with elements numbered 0..n-1 (0 = identity)."""

    def __init__(self, mul, inv, gens, name, sage=None, els=None):
        self.mul, self.inv, self.gens, self.name = mul, inv, gens, name
        self.n = len(mul)
        self.all = tuple(range(self.n))
        self.sage, self.els = sage, els

    @classmethod
    def from_sage(cls, G, name):
        e = G.identity()
        els = [e] + [g for g in G if g != e]
        idx = {g: i for i, g in enumerate(els)}
        mul = [[idx[a * b] for b in els] for a in els]
        inv = [idx[a ** -1] for a in els]
        gens = [idx[g] for g in G.gens()]
        Gr = cls(mul, inv, gens, name, G, els)
        Gr.idx = idx
        return Gr

    def el(self, s):
        return self.idx[self.sage(s)]

    def m(self, *xs):
        r = 0
        for x in xs:
            r = self.mul[r][x]
        return r

    def power(self, g, k):
        r = 0
        for _ in range(k):
            r = self.mul[r][g]
        return r

    def order_of(self, g):
        k, r = 1, g
        while r != 0:
            r = self.mul[r][g]
            k += 1
        return k

    def conj(self, g, h):
        """g h g^-1."""
        return self.mul[self.mul[g][h]][self.inv[g]]

    def closure(self, gens):
        S = {0}
        frontier = [0]
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

    def gens_of(self, H):
        gens, cur = [], (0,)
        for h in H:
            if len(cur) == len(H):
                break
            if h not in cur:
                gens.append(h)
                cur = self.closure(gens)
        return gens

    def conj_subgroup(self, g, H):
        return tuple(sorted(self.conj(g, h) for h in H))

    def left_cosets(self, H, ambient=None):
        """Representatives t_i of the left cosets t H in ambient (default
        G) and the map x -> (i, h) with x = t_i h."""
        reps, where = [], {}
        for x in (self.all if ambient is None else ambient):
            if x in where:
                continue
            i = len(reps)
            reps.append(x)
            for h in H:
                where[self.mul[x][h]] = (i, h)
        return reps, where

    def double_cosets(self, H, K):
        reps, seen = [], set()
        for g in self.all:
            if g in seen:
                continue
            reps.append(g)
            for h in H:
                for k in K:
                    seen.add(self.m(h, g, k))
        return reps

    def intersect(self, H, K):
        return tuple(sorted(set(H) & set(K)))

    def is_normal(self, N):
        S = set(N)
        return all(self.conj(g, x) in S for g in self.all for x in N)

    def quotient(self, N):
        """G/N as a FinGroup and the projection (list)."""
        reps, where = self.left_cosets(N)
        pi = [where[x][0] for x in self.all]
        q = len(reps)
        mul = [[pi[self.mul[reps[a]][reps[b]]] for b in range(q)]
               for a in range(q)]
        inv = [pi[self.inv[reps[a]]] for a in range(q)]
        assert pi[0] == 0
        Q = FinGroup(mul, inv, sorted(set(pi[g] for g in self.gens) - {0}),
                     self.name + '/N')
        return Q, pi

    def to_gap(self):
        perms = [[self.mul[g][x] + 1 for x in self.all] for g in self.gens]
        dom = list(range(1, self.n + 1))
        return libgap(PermutationGroup(perms, domain=dom))


def group(name):
    if name == 'C2xC2':
        G = PermutationGroup(['(1,2)', '(3,4)'])
    elif name == 'C2^3':
        G = PermutationGroup(['(1,2)', '(3,4)', '(5,6)'])
    elif name == 'C3xC3':
        G = PermutationGroup(['(1,2,3)', '(4,5,6)'])
    elif name == 'S3':
        G = SymmetricGroup(3)
    elif name == 'S4':
        G = SymmetricGroup(4)
    elif name == 'S5':
        G = SymmetricGroup(5)
    elif name == 'A4':
        G = AlternatingGroup(4)
    elif name == 'D8':
        G = DihedralGroup(4)
    elif name == 'Q8':
        G = QuaternionGroup()
    elif name.startswith('C'):
        G = CyclicPermutationGroup(int(name[1:]))
    return FinGroup.from_sage(G, name)


def sylow(Gr, p):
    P = libgap(Gr.sage).SylowSubgroup(p)
    return tuple(sorted(Gr.idx[Gr.sage(x)] for x in P.AsList()))


def subgroups(Gr):
    """Representatives of the conjugacy classes of subgroups."""
    out = []
    for c in libgap(Gr.sage).ConjugacyClassesSubgroups():
        H = c.Representative()
        out.append(tuple(sorted(Gr.idx[Gr.sage(x)] for x in H.AsList())))
    return out


# ===========================================================================
# Modules: a subgroup H (tuple of indices) acting by matrices
# ===========================================================================


class Mod:
    def __init__(self, Gr, H, F, dim, mats):
        self.Gr, self.H, self.F, self.dim = Gr, tuple(H), F, dim
        self.mats = mats


def from_gens(Gr, F, dim, genmats, H=None):
    H = Gr.all if H is None else H
    mats = {0: identity_matrix(F, dim)}
    frontier = [0]
    while frontier:
        new = []
        for a in frontier:
            for s, A in genmats.items():
                b = Gr.mul[a][s]
                if b not in mats:
                    mats[b] = mats[a] * A
                    new.append(b)
        frontier = new
    assert set(mats) == set(H)
    for s, A in genmats.items():
        for a in H:
            assert mats[Gr.mul[a][s]] == mats[a] * A, 'not a representation'
    return Mod(Gr, H, F, dim, mats)


def trivial(Gr, F, H=None):
    H = Gr.all if H is None else H
    return Mod(Gr, H, F, 1, {h: identity_matrix(F, 1) for h in H})


def sign(Gr, F, H=None):
    H = Gr.all if H is None else H
    return Mod(Gr, H, F, 1,
               {h: matrix(F, [[Gr.els[h].sign()]]) for h in H})


def perm_module(Gr, F, K, H=None):
    """Permutation module of H on the left cosets x K (K <= H)."""
    H = Gr.all if H is None else H
    cos, where = [], {}
    for x in H:
        if x in where:
            continue
        i = len(cos)
        cos.append(x)
        for k in K:
            where[Gr.mul[x][k]] = i
    d = len(cos)
    mats = {}
    for g in H:
        A = zero_matrix(F, d)
        for i, x in enumerate(cos):
            A[where[Gr.mul[g][x]], i] = 1
        mats[g] = A
    return Mod(Gr, H, F, d, mats)


def regular(Gr, F, H=None):
    return perm_module(Gr, F, (0,), H)


def restrict(M, K):
    return Mod(M.Gr, K, M.F, M.dim, {k: M.mats[k] for k in K})


def conjugate(M, g):
    """lconj(g, M): a module of g K g^-1 on which g k g^-1 acts as k."""
    Gr = M.Gr
    return Mod(Gr, Gr.conj_subgroup(g, M.H), M.F, M.dim,
               {Gr.conj(g, k): M.mats[k] for k in M.H})


def tensor(*Ms):
    M = Ms[0]
    for N in Ms[1:]:
        assert M.H == N.H
        M = Mod(M.Gr, M.H, M.F, M.dim * N.dim,
                {h: M.mats[h].tensor_product(N.mats[h]) for h in M.H})
    return M


def dual(M):
    Gr = M.Gr
    return Mod(Gr, M.H, M.F, M.dim,
               {h: M.mats[Gr.inv[h]].transpose() for h in M.H})


def hom_module(M, N):
    """Hom_R(M, N), (g phi)(m) = g phi(g^-1 m); X stored column-major."""
    Gr = M.Gr
    return Mod(Gr, M.H, M.F, M.dim * N.dim,
               {h: M.mats[Gr.inv[h]].transpose().tensor_product(N.mats[h])
                for h in M.H})


def direct_sum(*Ms):
    M0 = Ms[0]
    F = M0.F
    mats = {}
    for h in M0.H:
        mats[h] = block_matrix(
            [[M.mats[h] if i == j else zero_matrix(F, M.dim, Mj.dim)
              for j, Mj in enumerate(Ms)] for i, M in enumerate(Ms)],
            subdivide=False)
    return Mod(M0.Gr, M0.H, F, sum(M.dim for M in Ms), mats)


def induce(N, ambient=None):
    """N up^ambient, basis t_i (x) n over left coset representatives."""
    Gr = N.Gr
    ambient = Gr.all if ambient is None else tuple(ambient)
    reps, where = Gr.left_cosets(N.H, ambient)
    d = N.dim
    mats = {}
    for g in ambient:
        A = zero_matrix(N.F, len(reps) * d)
        for i, t in enumerate(reps):
            j, h = where[Gr.mul[g][t]]
            A.set_block(j * d, i * d, N.mats[h])
        mats[g] = A
    return Mod(Gr, ambient, N.F, len(reps) * d, mats)


def coinduce(N, ambient=None):
    """Hom_(RH)(RG, N): functions f on G with f(h x) = h f(x); a basis is
    given by the values on right coset representatives; (g f)(x) = f(x g)."""
    Gr = N.Gr
    ambient = Gr.all if ambient is None else tuple(ambient)
    H = N.H
    rreps, rwhere = [], {}
    for x in ambient:
        if x in rwhere:
            continue
        i = len(rreps)
        rreps.append(x)
        for h in H:
            rwhere[Gr.mul[h][x]] = (i, h)
    d = N.dim
    mats = {}
    for g in ambient:
        A = zero_matrix(N.F, len(rreps) * d)
        for i, r in enumerate(rreps):
            # (g f)(r) = f(r g) = h f(r_j) where r g = h r_j
            j, h = rwhere[Gr.mul[r][g]]
            A.set_block(i * d, j * d, N.mats[h])
        mats[g] = A
    return Mod(Gr, ambient, N.F, len(rreps) * d, mats)


def hom_space(M, N):
    """Basis of Hom_H(M, N) (matrices dimN x dimM)."""
    assert M.H == N.H
    gens = M.Gr.gens_of(M.H)
    F, n, m = M.F, N.dim, M.dim
    if not gens:
        return [matrix(F, n, m, list(v)) for v in
                identity_matrix(F, n * m).rows()]
    rows = block_matrix(
        [[identity_matrix(F, m).tensor_product(N.mats[s])
          - M.mats[s].transpose().tensor_product(identity_matrix(F, n))]
         for s in gens], subdivide=False)
    return [matrix(F, m, n, list(v)).transpose()
            for v in kernel_basis(rows)]


def is_hom(M, N, X):
    return all(N.mats[h] * X == X * M.mats[h] for h in M.H)


def fixed_dim(M):
    gens = M.Gr.gens_of(M.H)
    if not gens:
        return M.dim
    A = block_matrix([[M.mats[s] - identity_matrix(M.F, M.dim)]
                      for s in gens], subdivide=False)
    return A.right_kernel().dimension()


def submodule(M, B):
    """The submodule spanned by the columns of B (assumed invariant)."""
    B = sp(B)
    return Mod(M.Gr, M.H, M.F, B.ncols(),
               {h: sp(B.solve_right(M.mats[h] * B)) for h in M.H})


def quotient_module(M, B):
    F = M.F
    k = B.ncols()
    full = B.augment(identity_matrix(F, M.dim))
    C = sp(full.matrix_from_columns(full.pivots()))
    Ci = sp(C.inverse())
    d = M.dim - k
    return Mod(M.Gr, M.H, F, d,
               {h: (Ci * M.mats[h] * C).submatrix(k, k, d, d) for h in M.H})


def random_hom(M, N):
    B = hom_space(M, N)
    F = M.F
    X = zero_matrix(F, N.dim, M.dim)
    for b in B:
        X += F.random_element() * b
    return X


def jordan_block_module(Gr, F, a):
    """C_q (generator Gr.gens[0]) acting by a unipotent Jordan block."""
    J = identity_matrix(F, a)
    for i in range(a - 1):
        J[i + 1, i] = 1
    return from_gens(Gr, F, a, {Gr.gens[0]: J})


def jordan_type(M):
    """Block sizes of the generator of a cyclic p-group module."""
    g = M.Gr.gens[0]
    X = M.mats[g] - identity_matrix(M.F, M.dim)
    ranks = [M.dim]
    P = identity_matrix(M.F, M.dim)
    while ranks[-1] > 0:
        P = P * X
        ranks.append(P.rank())
    # number of blocks of size >= k is ranks[k-1] - ranks[k]
    ge = [ranks[k - 1] - ranks[k] for k in range(1, len(ranks))]
    sizes = []
    for k in range(1, len(ge) + 1):
        exact = ge[k - 1] - (ge[k] if k < len(ge) else 0)
        sizes += [k] * exact
    return sorted(sizes, reverse=True)


def is_projective(M, p):
    """Over a field of characteristic p: M is projective iff free on a Sylow
    p-subgroup P, iff the norm of P acts with rank dim M / |P|."""
    P = sylow(M.Gr, p)
    if len(P) == 1:
        return True
    Nm = sum(M.mats[x] for x in P)
    return M.dim % len(P) == 0 and Nm.rank() == M.dim // len(P)


# ===========================================================================
# MeatAxe (GAP) bridge
# ===========================================================================

_GAPF = {}


def mtx(name):
    key = 'MTX.' + name
    if key not in _GAPF:
        _GAPF[key] = libgap.eval(key)
    return _GAPF[key]


FAIL = libgap.eval('fail')


def gap_module(M):
    gens = M.Gr.gens_of(M.H)
    gF = libgap.GF(M.F.order())
    if not gens:
        return libgap.GModuleByMats([libgap(identity_matrix(M.F, M.dim))],
                                    gF)
    return libgap.GModuleByMats([libgap(M.mats[s]) for s in gens], gF)


def isomorphic(M, N):
    if M.dim != N.dim:
        return False
    if M.dim == 0:
        return True
    return mtx('IsomorphismModules')(gap_module(M), gap_module(N)) != FAIL


def summand_classes(M):
    """Indecomposable summands grouped by isomorphism:
    list of [gap module, dimension, multiplicity]."""
    if M.dim == 0:
        return []
    iso = mtx('IsomorphismModules')
    classes = []
    for x in mtx('Indecomposition')(gap_module(M)):
        X, d = x[1], int(libgap.Length(x[0]))
        for c in classes:
            if c[1] == d and iso(c[0], X) != FAIL:
                c[2] += 1
                break
        else:
            classes.append([X, d, 1])
    return classes


def trivial_multiplicity(X):
    """Multiplicity of the trivial module k as a direct summand of X: the
    rank of the pairing Hom_G(X, k) x Hom_G(k, X) -> End(k) = k, phi, psi ->
    phi o psi (the map eta of the proof of Theorem 3.1.9 for N = k)."""
    F = X.F
    gens = X.Gr.gens_of(X.H)
    I = identity_matrix(F, X.dim)
    A = block_matrix([[X.mats[s] - I] for s in gens], subdivide=False)
    fix = kernel_basis(A)                         # Hom_G(k, X)
    Bt = block_matrix([[X.mats[s].transpose() - I] for s in gens],
                      subdivide=False)
    cofix = kernel_basis(Bt)                      # Hom_G(X, k)
    if not fix or not cofix:
        return 0
    # the pairing matrix (phi_i(psi_j)); written out entrywise, since dense
    # products in odd characteristic are avoided (see matrix above)
    return matrix(F, [[sum(u[i] * v[i] for i in range(X.dim)) for v in fix]
                      for u in cofix]).rank()


def is_summand(M, N):
    iso = mtx('IsomorphismModules')
    b = summand_classes(N)
    for X, d, k in summand_classes(M):
        if sum(l for Y, e, l in b if e == d and iso(X, Y) != FAIL) < k:
            return False
    return True


def gap_mats_to_mod(Gr, F, X, H=None):
    """A MeatAxe module X (generators = Gr.gens_of(H)) back to a Mod."""
    H = Gr.all if H is None else H
    gens = Gr.gens_of(H)
    mats = [matrix(F, [[F(c.sage()) for c in row] for row in A])
            for A in libgap.eval('x -> x.generators')(X)]
    return from_gens(Gr, F, mats[0].nrows(), dict(zip(gens, mats)), H)


# ===========================================================================
# Free resolutions over F G (F a finite field) by linear algebra
# ===========================================================================


def act_free(Gr, r, g, v):
    n = Gr.n
    w = [0] * (r * n)
    row = Gr.mul[g]
    for i in range(r):
        base = i * n
        for x in range(n):
            c = v[base + x]
            if c:
                w[base + row[x]] = c
    return vector(v.base_ring(), w)


def free_perm(Gr, F, r, g):
    n = Gr.n
    A = zero_matrix(F, r * n)
    row = Gr.mul[g]
    for i in range(r):
        for x in range(n):
            A[i * n + row[x], i * n + x] = 1
    return A


def free_module(Gr, F, r, H=None):
    H = Gr.all if H is None else H
    return Mod(Gr, H, F, r * Gr.n, {h: free_perm(Gr, F, r, h) for h in H})


def _generators(K_basis, act, F, dim):
    gens = []
    S = dmatrix(F, 0, dim)
    target = len(K_basis)
    for v in K_basis:
        if S.nrows() == target:
            break
        if S.nrows() and dmatrix(F, S.rows() + [v]).rank() == S.nrows():
            continue
        gens.append(v)
        S = dmatrix(F, S.rows() + act(v)).echelon_form()
        S = S.matrix_from_rows(range(S.rank()))
    assert S.nrows() == target
    return gens


class Resolution:
    """F_n -> ... -> F_0 -> M for a module M of the whole group G."""

    def __init__(self, M, nmax):
        Gr, F = M.Gr, M.F
        n = Gr.n
        self.M, self.Gr, self.F = M, Gr, F
        g0 = _generators(identity_matrix(F, M.dim).columns(),
                         lambda v: [M.mats[g] * v for g in Gr.all], F, M.dim)
        self.ranks = [len(g0)]
        self.imgs = [g0]
        D = matrix(F, [M.mats[x] * v for v in g0
                       for x in range(n)]).transpose()
        self.D = [D]                      # D[k] : F_k -> F_{k-1} (or M)
        for k in range(1, nmax + 1):
            r = self.ranks[-1]
            K = kernel_basis(D)
            gk = _generators(K, lambda v, r=r: [act_free(Gr, r, g, v)
                                                for g in Gr.all], F, r * n)
            self.ranks.append(len(gk))
            self.imgs.append(gk)
            D = matrix(F, [act_free(Gr, r, x, v) for v in gk
                           for x in range(n)]).transpose()
            self.D.append(D)

    def coboundary(self, k, N):
        """delta^k : Hom_G(F_k, N) = N^{r_k} -> N^{r_{k+1}}."""
        Gr, d = self.Gr, N.dim
        rk, rk1 = self.ranks[k], self.ranks[k + 1]
        D = zero_matrix(N.F, rk1 * d, rk * d)
        for j, v in enumerate(self.imgs[k + 1]):
            for i in range(rk):
                A = zero_matrix(N.F, d)
                for x in range(Gr.n):
                    c = v[i * Gr.n + x]
                    if c:
                        A += c * N.mats[x]
                D.set_block(j * d, i * d, A)
        return D

    def ext_dims(self, N, nmax):
        ds = [self.coboundary(k, N).dense_matrix() for k in range(nmax + 1)]
        out = []
        for k in range(nmax + 1):
            out.append(ds[k].ncols() - ds[k].rank()
                       - (ds[k - 1].rank() if k else 0))
        return out

    def omega(self, k):
        """Omega~^k(M) = image of F_k -> F_{k-1} (k >= 1) as a module."""
        Gr, F = self.Gr, self.F
        r = self.ranks[k - 1]
        B = self.D[k].dense_matrix().column_space().basis_matrix().transpose()
        return submodule(free_module(Gr, F, r), B)


def ext_dims(M, N, nmax):
    return Resolution(M, nmax + 1).ext_dims(N, nmax)


# ===========================================================================
# Bar (inhomogeneous) cochains C^n(G, M) = maps G^n -> M
# ===========================================================================


class Bar:
    def __init__(self, Gr, M):
        self.Gr, self.M, self.F, self.d = Gr, M, M.F, M.dim
        self._delta = {}

    def index(self, t):
        r = 0
        for x in t:
            r = r * self.Gr.n + x
        return r

    def delta(self, n):
        """The printed coboundary formula of p. 64."""
        if n in self._delta:
            return self._delta[n]
        Gr, d, F = self.Gr, self.d, self.F
        N = Gr.n
        ent = {}

        def add(r, c, A):
            for a in range(d):
                for b in range(d):
                    if A[a, b]:
                        key = (r * d + a, c * d + b)
                        ent[key] = ent.get(key, 0) + A[a, b]
        I = identity_matrix(F, d)
        for t in itertools.product(range(N), repeat=n + 1):
            r = self.index(t)
            add(r, self.index(t[1:]), self.M.mats[t[0]])
            for i in range(1, n + 1):
                s = t[:i - 1] + (Gr.mul[t[i - 1]][t[i]],) + t[i + 1:]
                add(r, self.index(s), (-1) ** i * I)
            add(r, self.index(t[:n]), (-1) ** (n + 1) * I)
        D = matrix(F, N ** (n + 1) * d, N ** n * d, ent, sparse=True)
        D = D.dense_matrix()
        self._delta[n] = D
        return D

    def h_dim(self, n):
        D = self.delta(n)
        return D.ncols() - D.rank() - (self.delta(n - 1).rank() if n else 0)

    def cocycles(self, n):
        return self.delta(n).right_kernel()

    def is_coboundary(self, c, n):
        if n == 0:
            return c.is_zero()
        B = self.delta(n - 1)
        return B.augment(dmatrix(self.F, c).transpose()).rank() == B.rank()

    def independent_mod_coboundaries(self, cs, n):
        B = self.delta(n - 1)
        rb = B.rank()
        A = B.augment(dmatrix(self.F, cs).transpose())
        return A.rank() == rb + len(cs)

    def cup(self, a, p, b, q):
        """Alexander-Whitney product of cochains, trivial coefficients."""
        N = self.Gr.n
        out = []
        for t in itertools.product(range(N), repeat=p + q):
            out.append(a[self.index(t[:p])] * b[self.index(t[p:])])
        return vector(self.F, out)

    def nonzero_class(self, n):
        Z = self.cocycles(n).basis()
        for z in Z:
            if not self.is_coboundary(z, n):
                return z
        return None


# ===========================================================================
# Abelian groups and integral cochain complexes
# ===========================================================================


def canon(free, torsion):
    pp = []
    for d in torsion:
        d = ZZ(d)
        if d == 0:
            free += 1
        elif d != 1:
            pp += [p ** e for p, e in factor(d)]
    return (free, tuple(sorted(pp)))


def ab_tensor(A, B):
    fa, ta = A
    fb, tb = B
    return canon(fa * fb, list(ta) * fb + list(tb) * fa
                 + [gcd(x, y) for x in ta for y in tb])


def ab_tor(A, B):
    return canon(0, [gcd(x, y) for x in A[1] for y in B[1]])


def ab_sum(*As):
    tors = []
    for a in As:
        tors += list(a[1])
    return canon(sum(a[0] for a in As), tors)


def ab_order(A):
    assert A[0] == 0
    o = 1
    for x in A[1]:
        o *= x
    return o


def exponent(A):
    assert A[0] == 0
    e = 1
    for x in A[1]:
        e = e * x // gcd(e, x)
    return e


def cohomology_Z(deltas, k):
    """H^k of a cochain complex of free ZZ-modules (integer matrices)."""
    Dk = deltas[k]
    rk = Dk.rank()
    if k > 0:
        Dp = deltas[k - 1]
        return canon(Dk.ncols() - rk - Dp.rank(),
                     [d for d in Dp.elementary_divisors() if d not in (0, 1)])
    return canon(Dk.ncols() - rk, [])


def exact_Z(ds, onto=True):
    """ds[i] : C_{i+1} -> C_i; exact at C_1 .. C_{len-1}, and (onto) ds[0]
    onto."""
    if onto and (any(d not in (0, 1) for d in ds[0].elementary_divisors())
                 or ds[0].rank() != ds[0].nrows()):
        return False
    for i in range(len(ds) - 1):
        a, b = ds[i], ds[i + 1]
        if not (a * b).is_zero() or a.rank() + b.rank() != a.ncols():
            return False
        if any(d not in (0, 1) for d in b.elementary_divisors()):
            return False
    return True


def cyc_D(m, n, T_sign=-1):
    """Coefficients (powers of x) in Z[C_n] of D_m: m odd: T (T_sign = -1:
    1 - x, Proposition 3.5.1; +1: x - 1), m even: N."""
    if m % 2 == 1:
        v = [0] * n
        v[0] += -T_sign
        v[1 % n] += T_sign
        return v
    return [1] * n


def regular_Z_matrix(coeffs, n):
    """Left multiplication by sum c_u x^u on Z[C_n] (basis x^0..x^(n-1))."""
    A = zero_matrix(ZZ, n)
    for u, c in enumerate(coeffs):
        for v in range(n):
            A[(u + v) % n, v] += c
    return A


def product_resolution(a, b, top):
    """P (x) Q for C_a x C_b (generators x, y), P, Q the resolutions of
    Proposition 3.5.1; degree k has generators (i, k - i).  Returns for
    k = 1..top the images d(e_i (x) f_j) as dicts
    ((i', j'), (u, v)) -> coefficient of x^u y^v (e_i' (x) f_j')."""
    out = {}
    for k in range(1, top + 1):
        imgs = {}
        for i in range(k + 1):
            j = k - i
            o = {}
            if i >= 1:
                for u, c in enumerate(cyc_D(i, a)):
                    if c:
                        key = ((i - 1, j), (u, 0))
                        o[key] = o.get(key, 0) + c
            if j >= 1:
                for v, c in enumerate(cyc_D(j, b)):
                    if c:
                        key = ((i, j - 1), (0, v))
                        o[key] = o.get(key, 0) + (-1) ** i * c
            imgs[(i, j)] = o
        out[k] = imgs
    return out


def product_resolution_Z_matrices(a, b, top):
    """The augmented complex P (x) Q as integer matrices over the ZZ-basis
    x^u y^v (generator) of each free module."""
    ab = a * b
    pr = product_resolution(a, b, top)

    def pos(gen_index, u, v):
        return gen_index * ab + u * b + v
    mats = [matrix(ZZ, [[1] * ab])]           # augmentation C_0 -> ZZ
    for k in range(1, top + 1):
        src = [(i, k - i) for i in range(k + 1)]
        tgt = [(i, k - 1 - i) for i in range(k)]
        A = zero_matrix(ZZ, len(tgt) * ab, len(src) * ab)
        for s, g in enumerate(src):
            for (gen, (u, v)), c in pr[k][g].items():
                t = tgt.index(gen)
                for u0 in range(a):
                    for v0 in range(b):
                        A[pos(t, (u + u0) % a, (v + v0) % b),
                          pos(s, u0, v0)] += c
        mats.append(A)
    return mats


def trivial_cochains(pr, top, R=ZZ):
    """Hom(P (x) Q, R) with trivial coefficients: delta^k matrices."""
    deltas = []
    for k in range(top):
        src = [(i, k - i) for i in range(k + 1)]
        tgt = [(i, k + 1 - i) for i in range(k + 2)]
        D = zero_matrix(R, len(tgt), len(src))
        for r, g in enumerate(tgt):
            for (gen, uv), c in pr[k + 1][g].items():
                D[r, src.index(gen)] += c
        deltas.append(D)
    return deltas


# ===========================================================================
# 3.1 Operations on RG-modules
# ===========================================================================


def section_3_1():
    # Proposition 3.1.2 (p. 50): lambda = coefficient of 1.
    for name, q in [('S3', 2), ('S3', 3), ('A4', 2), ('A4', 4), ('D8', 2),
                    ('Q8', 2), ('C3xC3', 3), ('A4', 3)]:
        Gr = group(name)
        F = GF(q)
        Bm = matrix(F, Gr.n, Gr.n,
                    lambda x, y: 1 if Gr.mul[x][y] == 0 else 0)
        check(Bm.is_symmetric() and Bm.det() != 0,
              'Prop 3.1.2 (p. 50): lambda(ab) is a symmetric non-degenerate '
              'form on GF(%d)%s' % (q, name))
        reg = regular(Gr, F)
        for X, d, k in summand_classes(reg):
            soc = mtx('BasisSocle')(X)
            rad = mtx('BasisRadical')(X)
            S = mtx('InducedActionSubmodule')(X, soc)
            Q = mtx('InducedActionFactorModule')(X, rad)
            check(mtx('IsomorphismModules')(S, Q) != FAIL,
                  'Prop 3.1.2 (p. 50): Soc(P) ~ P/Rad(P) for a projective '
                  'indecomposable GF(%d)%s-module of dimension %d'
                  % (q, name, d))

    # The Hopf algebra RG (p. 52), on random elements of GF(3)S3.
    Gr = group('S3')
    F = GF(3)
    n = Gr.n

    def mult(a, b):
        c = [F(0)] * n
        for x in range(n):
            for y in range(n):
                c[Gr.mul[x][y]] += a[x] * b[y]
        return c

    def Delta(a):     # element of F[G x G], index x*n + y
        c = [F(0)] * (n * n)
        for x in range(n):
            c[x * n + x] += a[x]
        return c

    def mult2(a, b):
        c = [F(0)] * (n * n)
        for x1 in range(n):
            for y1 in range(n):
                if a[x1 * n + y1]:
                    for x2 in range(n):
                        for y2 in range(n):
                            c[Gr.mul[x1][x2] * n + Gr.mul[y1][y2]] += \
                                a[x1 * n + y1] * b[x2 * n + y2]
        return c

    def eta(a):
        c = [F(0)] * n
        for x in range(n):
            c[Gr.inv[x]] += a[x]
        return c
    ok = True
    for _ in range(20):
        a = [F.random_element() for _ in range(n)]
        b = [F.random_element() for _ in range(n)]
        ok &= Delta(mult(a, b)) == mult2(Delta(a), Delta(b))
        ok &= eta(mult(a, b)) == mult(eta(b), eta(a))
        ok &= eta(eta(a)) == a
        # sum mu_i eta(nu_i) = epsilon(a) 1
        s = [F(0)] * n
        for x in range(n):
            for y in range(n):
                s[Gr.mul[x][Gr.inv[y]]] += Delta(a)[x * n + y]
        ok &= s == [sum(a)] + [F(0)] * (n - 1)
    check(ok, 'p. 52: Delta is an algebra map, eta an anti-automorphism with '
          'eta^2 = 1, sum mu_i eta(nu_i) = epsilon(lambda) 1 (20 random '
          'pairs in GF(3)S3)')

    # Grouplike elements (p. 52): GF(5)C4 and GF(5)(C2 x C2).
    F = GF(5)
    found = {}
    for name in ['C4', 'C2xC2']:
        Gr = group(name)
        n = Gr.n
        likes, idem, chars = [], 0, 0
        for a in itertools.product(F, repeat=n):
            if all(c == 0 for c in a):
                continue
            # Delta(a) = a (x) a  <=>  a_x a_y = 0 (x != y), a_x^2 = a_x
            if all(a[x] * a[y] == (a[x] if x == y else 0)
                   for x in range(n) for y in range(n)):
                likes.append(a)
        for a in itertools.product(F, repeat=n):
            sq = [F(0)] * n
            for x in range(n):
                for y in range(n):
                    sq[Gr.mul[x][y]] += a[x] * a[y]
            idem += (list(a) == sq)
        for vals in itertools.product([v for v in F if v != 0],
                                      repeat=len(Gr.gens)):
            chi = {0: F(1)}
            frontier = [0]
            good = True
            while frontier and good:
                new = []
                for x in frontier:
                    for s, v in zip(Gr.gens, vals):
                        y = Gr.mul[x][s]
                        if y in chi:
                            good &= chi[y] == chi[x] * v
                        else:
                            chi[y] = chi[x] * v
                            new.append(y)
                frontier = new
            if good:
                good = all(chi[Gr.mul[x][y]] == chi[x] * chi[y]
                           for x in range(n) for y in range(n))
            chars += good
        check(len(likes) == n and all(sorted(a) == [0] * (n - 1) + [1]
                                      for a in likes),
              'p. 52: the grouplike elements of GF(5)%s are exactly the '
              'group elements' % name)
        check(idem == 16 and chars == 4,
              'p. 52: GF(5)%s ~ GF(5)^4 as algebras (16 idempotents, 4 '
              'algebra maps to GF(5))' % name)
        found[name] = max(Gr.order_of(g) for g in Gr.all)
    check(found['C4'] == 4 and found['C2xC2'] == 2,
          'p. 52: same group algebra GF(5)^4, different groups of '
          'grouplikes (C4, C2 x C2)')

    # Hom_k(M, N) ~ M* (x) N, M** ~ M (p. 52); Prop 3.1.5 (p. 53).
    cases = []
    Gr = group('S3')
    for q in [2, 3]:
        F = GF(q)
        cases.append((Gr, F, [trivial(Gr, F), sign(Gr, F),
                              perm_module(Gr, F, Gr.closure([Gr.el('(1,2)')])),
                              regular(Gr, F)]))
    Gr = group('A4')
    F = GF(2)
    cases.append((Gr, F, [trivial(Gr, F),
                          perm_module(Gr, F, Gr.closure([Gr.el('(1,2,3)')])),
                          perm_module(Gr, F,
                                      Gr.closure([Gr.el('(1,2)(3,4)')]))]))
    for Gr, F, mods in cases:
        for M in mods:
            check(isomorphic(dual(dual(M)), M),
                  'p. 52: M** ~ M (%s over GF(%d), dim %d)'
                  % (Gr.name, F.order(), M.dim))
            for N in mods[:3]:
                check(isomorphic(hom_module(M, N), tensor(dual(M), N)),
                      'p. 52: Hom_k(M, N) ~ M* (x) N (%s over GF(%d))'
                      % (Gr.name, F.order()))
            # Proposition 3.1.5: Lambda (x) M, induced -> diagonal action
            reg = regular(Gr, F)
            ind = Mod(Gr, Gr.all, F, Gr.n * M.dim,
                      {g: reg.mats[g].tensor_product(identity_matrix(F, M.dim))
                       for g in Gr.all})
            diag = tensor(reg, M)
            Phi = zero_matrix(F, Gr.n * M.dim)
            for x in range(Gr.n):
                Phi.set_block(x * M.dim, x * M.dim, M.mats[x])
            check(Phi.is_invertible() and is_hom(ind, diag, Phi),
                  'Prop 3.1.5 (p. 53): lambda (x) m -> sum mu_i (x) nu_i m is '
                  'an isomorphism from the induced to the diagonal module '
                  '(%s over GF(%d), dim M = %d)' % (Gr.name, F.order(), M.dim))

    # Cyclic p-groups: Jordan blocks J_a, a = 1..q.
    for q, p in [(2, 2), (3, 3), (4, 2), (5, 5), (8, 2), (9, 3)]:
        Gr = group('C%d' % q)
        F = GF(p)
        J = {a: jordan_block_module(Gr, F, a) for a in range(1, q + 1)}
        # Omega(J_a) = J_(q-a): kernel of kC_q -> J_a
        omega_ok = True
        for a in range(1, q):
            reg = regular(Gr, F)
            top = vector(F, [1] + [0] * (a - 1))
            Pi = matrix(F, [J[a].mats[x] * top for x in range(q)]).transpose()
            K = Pi.right_kernel().basis_matrix().transpose()
            omega_ok &= jordan_type(submodule(reg, K)) == [q - a]
        check(omega_ok, 'p. 66: Omega(J_a) = J_(q-a) for C_%d over GF(%d)'
              % (q, p))
        tri, multi, cor, proj = True, True, True, True
        for a in range(1, q + 1):
            for b in range(1, q + 1):
                T = jordan_type(tensor(J[a], J[b]))
                ones = T.count(1)
                expect = 1 if (a == b and b % p != 0) else 0
                tri &= (ones > 0) == (expect == 1)
                multi &= ones <= 1
                if a < q:
                    # Corollary 3.1.6: Omega(J_a) (x) J_b ~ Omega(J_a (x) J_b)
                    # (+) projective
                    left = [s for s in jordan_type(tensor(J[q - a], J[b]))
                            if s != q]
                    right = sorted([q - s for s in T if s != q], reverse=True)
                    cor &= left == right
            # Proposition 3.1.10 equivalences
            Ja = J[a]
            props = [jordan_type(Ja) == [q],
                     set(jordan_type(tensor(Ja, dual(Ja)))) == {q},
                     set(jordan_type(tensor(Ja, Ja))) == {q},
                     jordan_type(dual(Ja)) == [q]]
            proj &= len(set(props)) == 1 and props[0] == (a == q)
        check(tri, 'Thm 3.1.9 (p. 54): k | J_a (x) J_b iff J_a ~ J_b* and '
              'p does not divide b (C_%d, GF(%d), all a, b)' % (q, p))
        check(multi, 'Thm 3.1.9 (p. 54): the multiplicity of k is at most '
              'one (C_%d)' % q)
        check(cor, 'Cor 3.1.6 (p. 53): Omega(J_a) (x) J_b ~ Omega(J_a (x) '
              'J_b) (+) projective (C_%d, all a < q, b)' % q)
        check(proj, 'Prop 3.1.10 (p. 55): J_a projective <=> J_a (x) J_a* '
              '<=> J_a (x) J_a <=> J_a* projective <=> a = q (C_%d)' % q)

    # Theorem 3.1.9 for the six indecomposable GF(3)S3-modules.
    Gr = group('S3')
    F = GF(3)
    k, sg = trivial(Gr, F), sign(Gr, F)
    mods = [k, sg]
    for X, d, m in summand_classes(regular(Gr, F)):
        P = gap_mats_to_mod(Gr, F, X)
        mods.append(P)
        soc = mtx('BasisSocle')(X)
        mods.append(gap_mats_to_mod(
            Gr, F, mtx('InducedActionFactorModule')(X, soc)))
    check(sorted(M.dim for M in mods) == [1, 1, 2, 2, 3, 3],
          'GF(3)S3: k, sign, two uniserial modules of length 2 and the two '
          'projective indecomposables')
    ok = True
    for M in mods:
        for N in mods:
            mlt = trivial_multiplicity(tensor(M, N))
            expect = 1 if (isomorphic(M, dual(N)) and N.dim % 3 != 0) else 0
            ok &= mlt == expect
    check(ok, 'Thm 3.1.9 (p. 54): multiplicity of k in M (x) N is 1 iff '
          'M ~ N* and 3 does not divide dim N, else 0 (all 36 pairs of '
          'indecomposable GF(3)S3-modules)')

    # Theorem 3.1.9 for D8 over GF(2): k, Omega(k), Omega^-1(k), Omega^2(k)
    # and the transitive permutation modules.
    Gr = group('D8')
    F = GF(2)
    k = trivial(Gr, F)
    reg = regular(Gr, F)
    aug = matrix(F, [[1] * Gr.n])
    Om = submodule(reg, aug.right_kernel().basis_matrix().transpose())
    Omi = quotient_module(reg, matrix(F, [[1]] * Gr.n))
    R2 = Resolution(k, 2)
    Om2 = R2.omega(2)
    mods = [k, Om, Omi]
    for H in subgroups(Gr):
        if 1 < len(H) < Gr.n:
            mods.append(perm_module(Gr, F, H))
    check(isomorphic(dual(Om), Omi) and not isomorphic(Om, Omi),
          'D8, GF(2): Omega(k)* ~ Omega^-1(k), not ~ Omega(k)')
    ok = True
    for M in mods:
        for N in mods:
            mlt = trivial_multiplicity(tensor(M, N))
            expect = 1 if (isomorphic(M, dual(N)) and N.dim % 2 != 0) else 0
            ok &= mlt == expect
    check(ok, 'Thm 3.1.9 (p. 54): multiplicity of k in M (x) N for k, '
          'Omega(k), Omega^-1(k) and 4 permutation modules of D8 over '
          'GF(2) (all pairs)')
    check(trivial_multiplicity(tensor(Om2, dual(Om2))) == 1 and
          Om2.dim % 2 == 1,
          'Thm 3.1.9 (p. 54): k is a summand of Omega~^2(k) (x) '
          'Omega~^2(k)* with multiplicity one (D8, GF(2))')

    # Propositions 3.1.7, 3.1.8 (pp. 53-54) and 3.1.10 (p. 55).
    tests = []
    Gr = group('S3')
    for q in [2, 3]:
        F = GF(q)
        tests.append((Gr, F, [trivial(Gr, F), sign(Gr, F),
                              perm_module(Gr, F, Gr.closure([Gr.el('(1,2)')])),
                              perm_module(Gr, F,
                                          Gr.closure([Gr.el('(1,2,3)')]))]))
    Gr = group('A4')
    F = GF(2)
    tests.append((Gr, F, [trivial(Gr, F),
                          perm_module(Gr, F, Gr.closure([Gr.el('(1,2,3)')])),
                          perm_module(Gr, F,
                                      Gr.closure([Gr.el('(1,2)(3,4)')]))]))
    Gr = group('D8')
    tests.append((Gr, F, [trivial(Gr, F)] +
                  [perm_module(Gr, F, H) for H in subgroups(Gr)
                   if len(H) == 2][:2]))
    for Gr, F, mods in tests:
        tag = '%s over GF(%d)' % (Gr.name, F.order())
        ok7 = ok8 = ok10 = True
        for M, N in itertools.product(mods, repeat=2):
            ok7 &= fixed_dim(hom_module(M, N)) == len(hom_space(M, N))
            # Proposition 3.1.10: the two maps of the proof
            d = M.dim
            inc = zero_matrix(F, d * d * d, d)
            for j in range(d):
                for i in range(d):
                    # m_j -> sum_i m_i (x) m'_i (x) m_j
                    inc[(i * d + i) * d + j, j] = 1
            ev = zero_matrix(F, d, d * d * d)
            for i in range(d):
                for j in range(d):
                    # m_i (x) m'_j (x) m_j -> m_i m'_j(m_j) = m_i
                    ev[i, (i * d + j) * d + j] = 1
            T3 = tensor(M, dual(M), M)
            ok10 &= (ev * inc == identity_matrix(F, d)
                     and is_hom(M, T3, inc) and is_hom(T3, M, ev))
        for M1, M2, M3 in itertools.product(mods, repeat=3):
            ok8 &= len(hom_space(tensor(M1, M2), M3)) == \
                len(hom_space(M2, hom_module(M1, M3)))
        check(ok7, 'Prop 3.1.7 (p. 53): dim Hom_G(R, Hom_R(M, N)) = '
              'dim Hom_G(M, N) (%s, all pairs)' % tag)
        check(ok8, 'Prop 3.1.8 (i) (p. 53): dim Hom_G(M1 (x) M2, M3) = '
              'dim Hom_G(M2, Hom(M1, M3)) (%s, all triples)' % tag)
        check(ok10, 'Prop 3.1.10 (p. 55): m -> sum m_i (x) m_i\' (x) m -> m '
              'are G-maps composing to 1 (%s)' % tag)
        M1, M2, M3 = mods[1], mods[2], mods[0]
        e1 = ext_dims(tensor(M1, M2), M3, 2)
        e2 = ext_dims(M2, hom_module(M1, M3), 2)
        e3 = ext_dims(M1, mods[2], 2)
        e4 = ext_dims(trivial(Gr, F), hom_module(M1, mods[2]), 2)
        check(e1 == e2 and e3 == e4,
              'Prop 3.1.8 (ii), (iii) (p. 53): Ext^n dimensions, n <= 2 '
              '(%s: %s, %s)' % (tag, e1, e3))


# ===========================================================================
# 3.2 Cup products
# ===========================================================================


def section_3_2():
    # The complexes M = (0 -> M' -> M_0), N = (0 -> N' -> N_0) for
    # zeta = eta = [0 -> k -> J_2 -> k -> 0] over GF(3)C3 (m = n = 1).
    Gr = group('C3')
    F = GF(3)
    k = trivial(Gr, F)
    J2 = jordan_block_module(Gr, F, 2)
    # J_2 has basis e0 (top), e1 = (x - 1) e0 (socle)
    iota = matrix(F, [[0], [1]])       # k -> J2
    eps = matrix(F, [[1, 0]])          # J2 -> k
    check(is_hom(k, J2, iota) and is_hom(J2, k, eps) and
          (eps * iota).is_zero(), 'p. 58: 0 -> k -> J_2 -> k -> 0 over '
          'GF(3)C3')
    # tensor complex: C_2 = k(x)k, C_1 = k(x)J2 (+) J2(x)k, C_0 = J2(x)J2
    I1, I2 = identity_matrix(F, 1), identity_matrix(F, 2)
    d1 = block_matrix([[iota.tensor_product(I2),
                        I2.tensor_product(iota)]], subdivide=False)
    d2 = block_matrix([[-I1.tensor_product(iota)],
                       [iota.tensor_product(I1)]], subdivide=False)
    C0 = tensor(J2, J2)
    C1 = direct_sum(tensor(k, J2), tensor(J2, k))
    C2 = tensor(k, k)
    check(is_hom(C1, C0, d1) and is_hom(C2, C1, d2) and (d1 * d2).is_zero(),
          'p. 56: the tensor product of the complexes is a complex of '
          'Lambda-modules')
    # homology: M (x) N = k in degree 0, zero elsewhere (Corollary 2.7.2)
    h0 = C0.dim - d1.rank()
    h1 = C1.dim - d1.rank() - d2.rank()
    h2 = C2.dim - d2.rank()
    check((h0, h1, h2) == (1, 0, 0),
          'p. 56: homology of the tensor product is M (x) N in degree 0, '
          'zero elsewhere (Corollary 2.7.2: H_n = sum H_i (x) H_j)')
    # Corollary 2.7.3 would need one of the two complexes to be exact:
    check(J2.dim - iota.rank() == 1, 'p. 56: the truncated complex '
          '0 -> k -> J_2 is not exact (H_0 = k), so Corollary 2.7.3 (one '
          'factor exact) does not apply to it')
    # Proposition 3.2.1, p. 58: the map phi to the Yoneda composite
    # 0 -> k(x)k -> M_0 (x) N' -> M (x) N_0 -> k(x)k -> 0
    b1 = iota.tensor_product(I1)                     # k(x)k -> J2(x)k
    b2 = eps.tensor_product(I1)                      # J2(x)k -> k(x)k = M(x)N'
    b2 = I1.tensor_product(iota) * b2                # -> k(x)J2 = M (x) N_0
    b3 = I1.tensor_product(eps)                      # k(x)J2 -> k(x)k
    phi0 = eps.tensor_product(I2)                    # J2(x)J2 -> k(x)J2
    phi1 = block_matrix([[zero_matrix(F, 2, 2), I2]], subdivide=False)
    phi2 = I1                                        # k(x)k -> k(x)k
    epsMN = eps.tensor_product(eps)
    check(phi0 * d1 == b2 * phi1 and phi1 * d2 == b1 * phi2 and
          b3 * phi0 == epsMN and (b2 * b1).is_zero() and (b3 * b2).is_zero(),
          'Prop 3.2.1 (p. 58): the maps phi_i of the proof give a map of '
          '2-fold extensions (m = n = 1, GF(3)C3)')
    check(is_hom(C0, tensor(k, J2), phi0) and
          is_hom(C1, tensor(J2, k), phi1),
          'Prop 3.2.1 (p. 58): phi_0, phi_1 are module maps')

    # Graded commutativity (pp. 56-57) with Alexander-Whitney cochains.
    for name, p in [('C3xC3', 3), ('C2xC2', 2)]:
        Gr = group(name)
        F = GF(p)
        B = Bar(Gr, trivial(Gr, F))
        Z1 = B.cocycles(1).basis()
        check(len(Z1) == 2 and B.h_dim(1) == 2,
              'H^1(%s, GF(%d)) = Hom(G, GF(%d)) has dimension 2'
              % (name, p, p))
        x1, x2 = Z1
        x12, x21 = B.cup(x1, 1, x2, 1), B.cup(x2, 1, x1, 1)
        check(B.is_coboundary(x12 + x21, 2) and
              not B.is_coboundary(x12, 2),
              'p. 57: x1 x2 = -x2 x1 != 0 in H^2(%s, GF(%d))' % (name, p))
        sq = [B.is_coboundary(B.cup(x, 1, x, 1), 2) for x in (x1, x2)]
        check(all(sq) if p == 3 else not any(sq),
              'p. 57: x^2 %s in H^2(%s, GF(%d))'
              % ('= 0' if p == 3 else '!= 0', name, p))
    Gr = group('C3')
    F = GF(3)
    B = Bar(Gr, trivial(Gr, F))
    x = B.nonzero_class(1)
    y = B.nonzero_class(2)
    xy, yx = B.cup(x, 1, y, 2), B.cup(y, 2, x, 1)
    check(B.is_coboundary(xy - yx, 3) and not B.is_coboundary(xy, 3),
          'p. 57: x y = y x != 0 in H^3(C3, GF(3)) (degrees 1, 2)')


# ===========================================================================
# 3.3 Induction and restriction
# ===========================================================================


def section_3_3():
    cases = []
    G = group('S4')
    F2, F3 = GF(2), GF(3)
    D8 = G.closure([G.el('(1,2,3,4)'), G.el('(1,3)')])
    S3 = G.closure([G.el('(1,2,3)'), G.el('(1,2)')])
    V4 = G.closure([G.el('(1,2)(3,4)'), G.el('(1,3)(2,4)')])
    C4 = G.closure([G.el('(1,2,3,4)')])
    A4 = G.closure([G.el('(1,2,3)'), G.el('(1,2)(3,4)')])
    C2 = G.closure([G.el('(1,2)')])
    C3 = G.closure([G.el('(1,2,3)')])
    C2b = G.closure([G.el('(1,3)')])
    for F in (F2, F3):
        cases += [
            (G, D8, S3, sign(G, F, S3)),
            (G, D8, S3, perm_module(G, F, C2, S3)),
            (G, S3, S3, perm_module(G, F, C3, S3)),
            (G, V4, C4, regular(G, F, C4)),
            (G, A4, D8, sign(G, F, D8)),
            (G, C2, C2b, trivial(G, F, C2b)),
        ]
    H = group('A4')
    cases += [(H, H.closure([H.el('(1,2,3)')]), H.closure([H.el('(1,2,4)')]),
               regular(H, F2, H.closure([H.el('(1,2,4)')]))),
              (H, H.closure([H.el('(1,2)(3,4)')]),
               H.closure([H.el('(1,3)(2,4)'), H.el('(1,2)(3,4)')]),
               trivial(H, F3, H.closure([H.el('(1,3)(2,4)'),
                                         H.el('(1,2)(3,4)')])))]
    Q = group('Q8')
    Qs = [h for h in subgroups(Q) if len(h) == 4]
    cases += [(Q, Qs[0], Qs[1], regular(Q, F2, Qs[1])),
              (Q, Qs[0], Qs[0],
               perm_module(Q, F2, Q.intersect(Qs[0], Qs[1]), Qs[0]))]
    Dg = group('D8')
    D2s = [h for h in subgroups(Dg) if len(h) == 2]
    cases += [(Dg, D2s[0], D2s[-1], regular(Dg, F2, D2s[-1])),
              (Dg, D2s[1], D2s[-1], trivial(Dg, F2, D2s[-1]))]
    nmack = 0
    for Gr, H, K, M in cases:
        tag = '%s, |H| = %d, |K| = %d, dim M = %d, GF(%d)' % (
            Gr.name, len(H), len(K), M.dim, M.F.order())
        dc = Gr.double_cosets(H, K)
        sizes = [len(set(Gr.m(h, g, k) for h in H for k in K)) for g in dc]
        check(all(s == len(H) * len(K) //
                  len(Gr.intersect(H, Gr.conj_subgroup(g, K)))
                  for s, g in zip(sizes, dc)) and sum(sizes) == Gr.n,
              'p. 61: RG = sum R(HgK), |HgK| = |H||K|/|H cap gK| (%s)' % tag)
        L = restrict(induce(M), H)
        parts = []
        for g in dc:
            I = Gr.intersect(H, Gr.conj_subgroup(g, K))
            parts.append(induce(restrict(conjugate(M, g), I), H))
        R = direct_sum(*parts)
        check(isomorphic(L, R),
              'Thm 3.3.4 (p. 61): M up^G down_H ~ sum_HgK '
              '(gM) down_(H cap gK) up^H (%s)' % tag)
        nmack += 1
        # Corollary 3.3.5 with N an RH-module
        N = trivial(Gr, M.F, H)
        Mi, Ni = induce(M), induce(N)
        p1, p2, d3, d4 = [], [], 0, 0
        for g in dc:
            I = Gr.intersect(H, Gr.conj_subgroup(g, K))
            gM = restrict(conjugate(M, g), I)
            NI = restrict(N, I)
            p1.append(induce(tensor(gM, NI)))
            p2.append(induce(hom_module(gM, NI)))
            # (iii): gM (x)_(R I) N = coinvariants of gM' (x) N, gM' the
            # right module m h = h^-1 m: dim = dim - dim span (h - 1)
            T = tensor(gM, NI)
            gens = Gr.gens_of(I)
            if gens:
                A = block_matrix([[T.mats[s] - identity_matrix(T.F, T.dim)
                                   for s in gens]], subdivide=False)
                d3 += T.dim - A.rank()
            else:
                d3 += T.dim
            d4 += len(hom_space(gM, NI))
        if Mi.dim * Ni.dim <= 48:
            check(isomorphic(tensor(Mi, Ni), direct_sum(*p1)),
                  'Cor 3.3.5 (i) (p. 61) (%s)' % tag)
            check(isomorphic(hom_module(Mi, Ni), direct_sum(*p2)),
                  'Cor 3.3.5 (ii) (p. 61) (%s)' % tag)
        T = tensor(Mi, Ni)
        A = block_matrix([[T.mats[s] - identity_matrix(T.F, T.dim)
                           for s in Gr.gens_of(Gr.all)]], subdivide=False)
        check(T.dim - A.rank() == d3,
              'Cor 3.3.5 (iii) (p. 61, corrected: gM down_(H cap gK)): '
              'dimensions (%s)' % tag)
        check(len(hom_space(Mi, Ni)) == d4,
              'Cor 3.3.5 (iv) (p. 62): dimensions (%s)' % tag)

    # Nakayama relations, exterior trace, Eckmann-Shapiro, Prop 3.3.3,
    # induction = co-induction (pp. 60-61).
    G = group('S4')
    for F in (F2, F3):
        for H in (D8, S3, A4):
            Ms = [trivial(G, F), sign(G, F), perm_module(G, F, S3)]
            Ns = [trivial(G, F, H), sign(G, F, H)]
            for M in Ms:
                for N in Ns:
                    tag = '|H| = %d, GF(%d)' % (len(H), F.order())
                    MH = restrict(M, H)
                    check(len(hom_space(N, MH)) == len(hom_space(induce(N), M))
                          and len(hom_space(MH, N)) ==
                          len(hom_space(M, induce(N))),
                          'Prop 3.3.1 (p. 60): Nakayama relations, '
                          'dimensions (S4, %s)' % tag)
                    check(isomorphic(induce(tensor(N, MH)),
                                     tensor(induce(N), M)) and
                          isomorphic(induce(hom_module(N, MH)),
                                     hom_module(induce(N), M)),
                          'Prop 3.3.3 (p. 61) (S4, %s)' % tag)
            for N in Ns:
                check(isomorphic(induce(N), coinduce(N)),
                      'p. 60: N up^G ~ N Up^G (S4, |H| = %d, GF(%d))'
                      % (len(H), F.order()))
    # exterior trace map (exercise p. 61) is the Nakayama isomorphism
    Gr = group('S3')
    F = GF(3)
    H = Gr.closure([Gr.el('(1,2)')])
    for M in [regular(Gr, F), perm_module(Gr, F, H), sign(Gr, F)]:
        N = sign(Gr, F, H)
        Ni = induce(N)
        reps, where = Gr.left_cosets(H)
        Bs = hom_space(restrict(M, H), N)
        imgs = []
        for phi in Bs:
            # hat Tr(phi)(m) = sum_g g (x) phi(g^-1 m)
            X = zero_matrix(F, Ni.dim, M.dim)
            for i, t in enumerate(reps):
                X.set_block(i * N.dim, 0, phi * M.mats[Gr.inv[t]])
            imgs.append(X)
        check(all(is_hom(M, Ni, X) for X in imgs) and
              matrix(F, [X.list() for X in imgs]).rank() == len(Bs) ==
              len(hom_space(M, Ni)),
              'Exercise p. 61: the exterior trace map is an isomorphism '
              'Hom_H(M down_H, N) -> Hom_G(M, N up^G) (S3, dim M = %d)'
              % M.dim)
    # Eckmann-Shapiro (Cor 3.3.2) and Cor 3.3.5 (vi), n <= 2
    Gr = group('S3')
    for q in (2, 3):
        F = GF(q)
        for Hgen in ['(1,2)', '(1,2,3)']:
            H = Gr.closure([Gr.el(Hgen)])
            N = trivial(Gr, F, H)
            for M in [trivial(Gr, F), sign(Gr, F), regular(Gr, F)]:
                # Ext^n_H(N, M down_H) with H-resolution of N
                HG = FinGroup(*_subgroup_table(Gr, H))
                NH = transport(N, HG)
                MH = transport(restrict(M, H), HG)
                a = ext_dims(NH, MH, 2)
                b = ext_dims(induce(N), M, 2)
                check(a == b, 'Cor 3.3.2 (p. 61): Ext^n_H(N, M down_H) = '
                      'Ext^n_G(N up^G, M), n <= 2 (S3, |H| = %d, GF(%d), '
                      'dims %s)' % (len(H), q, a))
    Gr = group('S3')
    F = GF(2)
    H = Gr.closure([Gr.el('(1,2)')])
    K = Gr.closure([Gr.el('(1,3)')])
    M, N = trivial(Gr, F, K), trivial(Gr, F, H)
    lhs = ext_dims(induce(M), induce(N), 2)
    rhs = [0, 0, 0]
    for g in Gr.double_cosets(H, K):
        I = Gr.intersect(H, Gr.conj_subgroup(g, K))
        IG = FinGroup(*_subgroup_table(Gr, I))
        e = ext_dims(transport(restrict(conjugate(M, g), I), IG),
                     transport(restrict(N, I), IG), 2)
        rhs = [u + v for u, v in zip(rhs, e)]
    check(lhs == rhs, 'Cor 3.3.5 (vi) (p. 62): dim Ext^n_G(M up, N up) = '
          'sum dim Ext^n_(H cap gK), n <= 2 (S3, two subgroups of order 2, '
          'GF(2): %s)' % lhs)
    return nmack


def _subgroup_table(Gr, H):
    pos = {h: i for i, h in enumerate(H)}
    mul = [[pos[Gr.mul[a][b]] for b in H] for a in H]
    inv = [pos[Gr.inv[a]] for a in H]
    gens = [pos[s] for s in Gr.gens_of(H)]
    return mul, inv, gens, 'sub'


def transport(M, HG):
    """A module of a subgroup H of Gr as a module of the group HG built by
    _subgroup_table (same ordering of H)."""
    return Mod(HG, HG.all, M.F, M.dim,
               {i: M.mats[h] for i, h in enumerate(M.H)})


# ===========================================================================
# 3.4 Standard resolutions
# ===========================================================================


def lc_add(d, key, c):
    v = d.get(key, 0) + c
    if v:
        d[key] = v
    elif key in d:
        del d[key]


def section_3_4():
    for name in ['C3', 'S3']:
        Gr = group(name)
        N = Gr.n
        top = 3 if name == 'C3' else 2

        def bd(t):          # homogeneous boundary
            out = {}
            for i in range(len(t)):
                lc_add(out, t[:i] + t[i + 1:], (-1) ** i)
            return out

        def apply(f, v):
            out = {}
            for t, c in v.items():
                for s, e in f(t).items():
                    lc_add(out, s, c * e)
            return out
        ok_dd = ok_h = True
        for n in range(1, top + 1):
            for t in itertools.product(range(N), repeat=n + 1):
                ok_dd &= apply(bd, bd(t)) == {} if n >= 1 else True
                # id = d_(n+1) h_n + h_(n-1) d_n
                h = lambda s: {(0,) + s: 1}
                lhs = apply(bd, h(t))
                for s, c in apply(h, bd(t)).items():
                    lc_add(lhs, s, c)
                ok_h &= lhs == {t: 1}
        check(ok_dd, 'p. 63: d_n d_(n+1) = 0 for the standard resolution '
              '(%s, n <= %d)' % (name, top))
        check(ok_h, 'p. 63: id = d_(n+1) h_n + h_(n-1) d_n, h_n(g_0..g_n) '
              '= (1, g_0, ..., g_n) (%s, 1 <= n <= %d)' % (name, top))

        # bar notation (p. 63)
        def bar_to_hom(g0, bars):
            t = [g0]
            for b in bars:
                t.append(Gr.mul[t[-1]][b])
            return tuple(t)

        def hom_to_bar(t):
            return t[0], tuple(Gr.mul[Gr.inv[t[i]]][t[i + 1]]
                               for i in range(len(t) - 1))
        ok_b = ok_db = True
        for n in range(1, top + 1):
            for bars in itertools.product(range(N), repeat=n):
                t = bar_to_hom(0, bars)
                ok_b &= hom_to_bar(t) == (0, bars)
                # printed bar boundary formula
                exp = {}
                lc_add(exp, (bars[0], bars[1:]), 1)
                for i in range(1, n):
                    nb = bars[:i - 1] + (Gr.mul[bars[i - 1]][bars[i]],) \
                        + bars[i + 1:]
                    lc_add(exp, (0, nb), (-1) ** i)
                lc_add(exp, (0, bars[:n - 1]), (-1) ** n)
                got = {}
                for s, c in bd(t).items():
                    lc_add(got, hom_to_bar(s), c)
                ok_db &= got == exp
        check(ok_b, 'p. 63: (g_0, ..., g_n) = g_0 [g_0^-1 g_1 | ...] and '
              '[g_1|...|g_n] = (1, g_1, g_1 g_2, ...) are inverse (%s)' % name)
        check(ok_db, 'p. 63: the boundary formula in bar notation (%s, '
              'n <= %d)' % (name, top))

        # Alexander-Whitney (p. 64)
        def AW(t):
            out = {}
            for j in range(len(t)):
                lc_add(out, (t[:j + 1], t[j:]), 1)
            return out

        def d_tensor(pair):
            a, b = pair
            out = {}
            for s, c in bd(a).items():
                if len(s):
                    lc_add(out, (s, b), c)
            for s, c in bd(b).items():
                if len(s):
                    lc_add(out, (a, s), (-1) ** (len(a) - 1) * c)
            return out
        ok_c = ok_a = ok_bar = ok_g = True
        for n in range(1, top + 1):
            for t in itertools.product(range(N), repeat=n + 1):
                lhs = apply(AW, {s: c for s, c in bd(t).items()})
                rhs = apply(d_tensor, AW(t))
                ok_c &= lhs == rhs
                # co-associativity
                l1, l2 = {}, {}
                for (a, b), c in AW(t).items():
                    for (a1, a2), e in AW(a).items():
                        lc_add(l1, (a1, a2, b), c * e)
                    for (b1, b2), e in AW(b).items():
                        lc_add(l2, (a, b1, b2), c * e)
                ok_a &= l1 == l2
                g = random.randrange(N)
                gt = tuple(Gr.mul[g][x] for x in t)
                ok_g &= AW(gt) == {(tuple(Gr.mul[g][x] for x in a),
                                    tuple(Gr.mul[g][x] for x in b)): c
                                   for (a, b), c in AW(t).items()}
            for bars in itertools.product(range(N), repeat=n):
                t = bar_to_hom(0, bars)
                exp = {}
                for j in range(n + 1):
                    pre = 0
                    for b in bars[:j]:
                        pre = Gr.mul[pre][b]
                    lc_add(exp, ((0, bars[:j]), (pre, bars[j:])), 1)
                got = {}
                for (a, b), c in AW(t).items():
                    lc_add(got, (hom_to_bar(a), hom_to_bar(b)), c)
                ok_bar &= got == exp
        check(ok_c, 'p. 64: the Alexander-Whitney map is a chain map (%s, '
              'n <= %d)' % (name, top))
        check(ok_a and ok_g, 'p. 64: Alexander-Whitney is strictly '
              'co-associative and G-equivariant (%s)' % name)
        check(ok_bar, 'p. 64: Alexander-Whitney in bar notation (%s)' % name)

    # The coboundary formula (p. 64) equals composition with d_(n+1), for
    # nontrivial modules of S3.
    Gr = group('S3')
    for F, M in [(GF(3), sign(Gr, GF(3))),
                 (GF(2), submodule(perm_module(Gr, GF(2),
                                               Gr.closure([Gr.el('(1,2)')])),
                                   matrix(GF(2), [[1, 0], [1, 1], [0, 1]])))]:
        B = Bar(Gr, M)
        ok = True
        d = M.dim
        for n in range(0, 3):
            alpha = vector(F, [F.random_element()
                               for _ in range(Gr.n ** n * d)])
            got = B.delta(n) * alpha
            # (alpha o d)(1, g_1, g_1 g_2, ...) with alpha G-equivariant on
            # homogeneous tuples: alpha(g0, ..) = g0 alpha[g0^-1 g1 | ...]
            for bars in itertools.product(range(Gr.n), repeat=n + 1):
                t = [0]
                for b in bars:
                    t.append(Gr.mul[t[-1]][b])
                acc = vector(F, [0] * d)
                for i in range(n + 2):
                    s = t[:i] + t[i + 1:]
                    g0 = s[0]
                    bb = tuple(Gr.mul[Gr.inv[s[j]]][s[j + 1]]
                               for j in range(len(s) - 1))
                    r = B.index(bb)
                    acc += (-1) ** i * (M.mats[g0] *
                                        alpha[r * d:(r + 1) * d])
                r = B.index(bars)
                ok &= got[r * d:(r + 1) * d] == acc
        check(ok, 'p. 64: delta^n alpha(g_1..g_(n+1)) as printed = alpha o '
              'd_(n+1) (S3, dim M = %d, n <= 2)' % d)

    # Inflation (p. 64, corrected: resolutions of R).  Printed reading:
    # resolutions of M compute Ext(M, M): G/N = C2, R = ZZ, M = ZZ/2.
    deltas, ints = cyclic_with_Zm(2, 2, 3, GF(2))
    d1 = ints[1]
    check(exact_Z(ints[1:], onto=False) and
          canon(d1.nrows() - d1.rank(), [d for d in d1.elementary_divisors()
                                         if d not in (0, 1)]) == canon(0, [2]),
          'P (x) (ZZ -2-> ZZ) is a ZZ C2-free resolution of ZZ/2')
    ext1 = deltas[1].ncols() - deltas[1].rank() - deltas[0].rank()
    C2g = group('C2')
    h1 = Bar(C2g, trivial(C2g, GF(2))).h_dim(1)
    check(h1 == 1 and ext1 == 2, 'p. 64: H^1(C2, ZZ/2) = ZZ/2, '
          'Ext^1_(ZZ C2)(ZZ/2, ZZ/2) = (ZZ/2)^2')
    refuted(ext1 == h1, 'p. 64 (printed: resolutions of M): '
            'Ext^1_(ZZ C2)(ZZ/2, ZZ/2) has order 4, not |H^1(C2, ZZ/2)| = 2')
    # the coset map rho is a chain map over the identity of R (homogeneous
    # standard resolutions of G and G/N)
    G = group('D8')
    Z = [x for x in G.all if all(G.mul[x][y] == G.mul[y][x] for y in G.all)]
    Q, pi = G.quotient(tuple(sorted(Z)))
    ok = True
    for t in itertools.product(G.all, repeat=3):
        img = tuple(pi[x] for x in t)
        for i in range(3):
            s = t[:i] + t[i + 1:]
            ok &= tuple(pi[x] for x in s) == img[:i] + img[i + 1:]
        g = random.randrange(G.n)
        ok &= tuple(pi[G.mul[g][x]] for x in t) == \
            tuple(Q.mul[pi[g]][y] for y in img)
    check(ok, 'p. 64: the coset map rho : Q -> P is a G-chain map (D8 -> '
          'D8/Z)')
    # Five-term exact sequence (exercise p. 65), trivial and one nontrivial M
    cases = []
    D8 = group('D8')
    for N in subgroups(D8):
        if 1 < len(N) < 8 and D8.is_normal(N):
            cases.append((D8, N, GF(2), None))
    Q8 = group('Q8')
    for N in subgroups(Q8):
        if 1 < len(N) < 8:
            cases.append((Q8, N, GF(2), None))
    A4 = group('A4')
    cases.append((A4, A4.closure([A4.el('(1,2)(3,4)'), A4.el('(1,3)(2,4)')]),
                  GF(2), None))
    S3 = group('S3')
    C3 = S3.closure([S3.el('(1,2,3)')])
    cases.append((S3, C3, GF(3), None))
    cases.append((S3, C3, GF(3), 'sign'))
    C9 = group('C9')
    cases.append((C9, C9.closure([C9.power(C9.gens[0], 3)]), GF(3), None))
    nfive = 0
    for G, N, F, kind in cases:
        M = sign(G, F) if kind == 'sign' else trivial(G, F)
        Q, pi = G.quotient(N)
        # M^N = M here (N acts trivially on the modules used)
        assert all(M.mats[x] == identity_matrix(F, M.dim) for x in N)
        MQ = Mod(Q, Q.all, F, M.dim, {})
        for x in G.all:
            MQ.mats[pi[x]] = M.mats[x]
        BG, BQ = Bar(G, M), Bar(Q, MQ)
        NG = FinGroup(*_subgroup_table(G, N))
        BN = Bar(NG, transport(restrict(M, N), NG))

        def inflate(c, n):
            out = []
            for t in itertools.product(range(G.n), repeat=n):
                out.append(c[BQ.index(tuple(pi[x] for x in t))])
            return vector(F, out)

        def restrict1(c):
            return vector(F, [c[x] for x in N])
        h1Q, h1G, h2Q = BQ.h_dim(1), BG.h_dim(1), BQ.h_dim(2)
        Z1Q = BQ.cocycles(1).basis()
        Z1G = BG.cocycles(1).basis()
        infl1 = [inflate(c, 1) for c in Z1Q]
        # injectivity of inf on H^1 (B^1(Q) = 0 for trivial action; in
        # general compare modulo coboundaries)
        rk_inf1 = (BG.delta(0).augment(dmatrix(F, infl1).transpose()).rank()
                   - BG.delta(0).rank()) if infl1 else 0
        # kernel of res on H^1(G): classes whose restriction is a coboundary
        # N acts trivially on M, so B^1(N, M) = 0 and H^1(N, M) = Z^1(N, M)
        check(BN.delta(0).is_zero(), 'B^1(N, M) = 0 for N acting trivially')
        resZ = [restrict1(c) for c in Z1G]
        rk_res = matrix(F, resZ).rank() if resZ else 0
        dim_ker_res = h1G - rk_res
        # H^1(N, M)^(G/N), action (g f)(x) = g f(g^-1 x g)
        Z1N = BN.cocycles(1).basis()
        npos = {x: i for i, x in enumerate(N)}

        def act(g, f):
            return vector(F, [(M.mats[g] * vector(
                F, [f[npos[G.m(G.inv[g], x, g)]]]))[0] for x in N])
        if Z1N:
            cond = block_matrix([[matrix(F, [act(g, f) - f
                                             for f in Z1N]).transpose()]
                                 for g in G.gens], subdivide=False)
            fixed = cond.right_kernel().dimension()
        else:
            fixed = 0
        inside = all(act(g, r) == r for r in resZ for g in G.gens)
        # kernel of inf on H^2
        Z2Q = BQ.cocycles(2).basis()
        BG1 = BG.delta(1)
        infl2 = dmatrix(F, [inflate(c, 2) for c in Z2Q]).transpose()
        rk_inf2 = BG1.augment(infl2).rank() - BG1.rank()
        ker_inf2 = h2Q - rk_inf2
        tag = '%s, |N| = %d, GF(%d)%s' % (G.name, len(N), F.order(),
                                          ', sign' if kind else '')
        check(rk_inf1 == h1Q, 'Exercise p. 65: inf on H^1 is injective (%s)'
              % tag)
        check(rk_inf1 == dim_ker_res,
              'Exercise p. 65: exact at H^1(G, M) (%s)' % tag)
        check(inside, 'p. 65: the image of restriction lies in the G/N-fixed '
              'points (%s)' % tag)
        check(fixed - rk_res == ker_inf2,
              'Exercise p. 65: dim H^1(N)^(G/N) - dim res = dim Ker(inf on '
              'H^2) (%s: %d - %d = %d)' % (tag, fixed, rk_res, ker_inf2))
        nfive += 1
    return nfive


# ===========================================================================
# Small abelian groups as tables (for projections and products)
# ===========================================================================


def abelian_group(orders, name):
    els = list(itertools.product(*[range(o) for o in orders]))
    pos = {e: i for i, e in enumerate(els)}
    mul = [[pos[tuple((a + b) % o for a, b, o in zip(x, y, orders))]
            for y in els] for x in els]
    inv = [pos[tuple((-a) % o for a, o in zip(x, orders))] for x in els]
    gens = [pos[tuple(1 if j == i else 0 for j in range(len(orders)))]
            for i in range(len(orders))]
    Gr = FinGroup(mul, inv, gens, name, els=els)
    return Gr


def cyclic_with_Zm(n, m, top, R):
    """Free resolution of ZZ/m (trivial) over ZZ C_n: P (x) (ZZ -m-> ZZ),
    generators a_k = e_k (x) z_0, b_k = e_(k-1) (x) z_1; cochain matrices
    delta^k (k < top) with trivial coefficients in R, and the integer
    matrices of the augmented complex (to check exactness)."""
    def gens(k):
        return [('a', k)] + ([('b', k)] if k >= 1 else [])

    def d(g):
        """list of (generator, coefficient vector in Z[C_n])"""
        kind, k = g
        out = []
        if kind == 'a' and k >= 1:
            out.append((('a', k - 1), cyc_D(k, n)))
        if kind == 'b':
            if k >= 2:
                out.append((('b', k - 1), cyc_D(k - 1, n)))
            v = [0] * n
            v[0] = (-1) ** (k - 1) * m
            out.append((('a', k - 1), v))
        return out
    deltas = []
    for k in range(top):
        src, tgt = gens(k), gens(k + 1)
        D = zero_matrix(R, len(tgt), len(src))
        for r, g in enumerate(tgt):
            for h, v in d(g):
                D[r, src.index(h)] += sum(v)
        deltas.append(D)
    ints = []
    eps = zero_matrix(ZZ, 1, n)
    ints.append(matrix(ZZ, [[1] * n]))      # a_0 -> ZZ/m: not used for Z
    for k in range(1, top + 1):
        src, tgt = gens(k), gens(k - 1)
        A = zero_matrix(ZZ, len(tgt) * n, len(src) * n)
        for s, g in enumerate(src):
            for h, v in d(g):
                A.set_block(tgt.index(h) * n, s * n, regular_Z_matrix(v, n))
        ints.append(A)
    return deltas, ints


# ===========================================================================
# 3.5 Cyclic and abelian groups
# ===========================================================================


def H_cyclic_Z(n, i):
    """Corollary 3.5.2 with M = ZZ: ZZ, 0, ZZ/n, 0, ZZ/n, ..."""
    if i == 0:
        return canon(1, [])
    return canon(0, []) if i % 2 else canon(0, [n])


def H_cyclic_Zp(n, p, i):
    """Corollary 3.5.2 with M = ZZ/p, p | n: ZZ/p in every degree."""
    return canon(0, [p])


def section_3_5():
    results = {}
    # Proposition 3.5.1 (p. 65): exact over ZZ (degrees <= 6), n = 1..8
    for n in range(1, 9):
        T = regular_Z_matrix(cyc_D(1, n), n)
        Nm = regular_Z_matrix(cyc_D(2, n), n)
        ds = [matrix(ZZ, [[1] * n])] + [T if k % 2 else Nm
                                         for k in range(1, 8)]
        check(exact_Z(ds), 'Prop 3.5.1 (p. 65): ... -N-> R(Z/%d) -T-> '
              'R(Z/%d) -> R is exact over ZZ (degrees <= 6)' % (n, n))

    # Corollary 3.5.2 (p. 65) against bar cochains.
    def formula_dims(M):
        Gr = M.Gr
        x = Gr.gens[0]
        I = identity_matrix(M.F, M.dim)
        T = I - M.mats[x]
        Nm = sum(M.mats[Gr.power(x, i)] for i in range(Gr.n))
        fix = T.right_kernel().dimension()
        return [fix,
                Nm.right_kernel().dimension() - T.rank(),
                fix - Nm.rank(),
                Nm.right_kernel().dimension() - T.rank()]
    cases = []
    for n, p in [(4, 2), (3, 3), (2, 3), (6, 2), (6, 3), (5, 5), (4, 3)]:
        Gr = group('C%d' % n)
        F = GF(p)
        cases.append(trivial(Gr, F))
        cases.append(regular(Gr, F))
        if n % p == 0:
            cases.append(jordan_block_module(Gr, F, 2))
        if n % 2 == 0:
            cases.append(Mod(Gr, Gr.all, F, 1,
                             {g: matrix(F, [[(-1) ** (i % 2)]])
                              for i, g in enumerate(
                                  [Gr.power(Gr.gens[0], j)
                                   for j in range(n)])}))
    for M in cases:
        B = Bar(M.Gr, M)
        top = 3 if M.Gr.n * M.dim <= 6 else 2
        got = [B.h_dim(r) for r in range(top + 1)]
        exp = formula_dims(M)[:top + 1]
        check(got == exp, 'Cor 3.5.2 (p. 65): H^r(Z/%d, M) by the formulas '
              '= by bar cochains, r <= %d (GF(%d), dim M = %d: %s)'
              % (M.Gr.n, top, M.F.order(), M.dim, got))
    for n in (2, 3, 4):
        Gr = group('C%d' % n)
        B = Bar(Gr, trivial(Gr, ZZ))
        deltas = [B.delta(k) for k in range(4)]
        got = [cohomology_Z(deltas, k) for k in range(4)]
        check(got == [H_cyclic_Z(n, k) for k in range(4)],
              'Cor 3.5.2 (p. 65): H^r(Z/%d, ZZ) = ZZ, 0, ZZ/%d, 0 (bar '
              'cochains over ZZ, r <= 3)' % (n, n))
    Gr = group('C2')
    Zm = Mod(Gr, Gr.all, ZZ, 1, {0: matrix(ZZ, [[1]]),
                                 Gr.gens[0]: matrix(ZZ, [[-1]])})
    B = Bar(Gr, Zm)
    deltas = [B.delta(k) for k in range(4)]
    check([cohomology_Z(deltas, k) for k in range(4)] ==
          [canon(0, []), canon(0, [2]), canon(0, []), canon(0, [2])],
          'Cor 3.5.2 (p. 65): H^r(Z/2, ZZ^-) = 0, ZZ/2, 0, ZZ/2')

    # Corollary 3.5.3 (p. 65): A4 over GF(3), H = C2 x C2, G/H = C3.
    G = group('A4')
    F = GF(3)
    H = G.closure([G.el('(1,2)(3,4)'), G.el('(1,3)(2,4)')])
    perm = perm_module(G, F, H)                  # R(G/H)
    xg = G.el('(1,2,3)')
    reps, where = G.left_cosets(H)
    # right multiplication by (1 - x) on R(G/H): t_i H -> t_i x H
    Tm = identity_matrix(F, 3)
    for i, t in enumerate(reps):
        j = where[G.mul[t][xg]][0]
        Tm[j, i] -= 1
    check(is_hom(perm, perm, Tm), 'Cor 3.5.3 (p. 65): T is a map of '
          'RG-modules on R(G/H)')
    inc = matrix(F, [[1]] * 3)
    aug = matrix(F, [[1] * 3])
    for M in [trivial(G, F), perm_module(G, F, G.closure([xg])),
              perm_module(G, F, H)]:
        I = identity_matrix(F, M.dim)
        a = I.tensor_product(inc)
        b = I.tensor_product(Tm)
        c = I.tensor_product(aug)
        mid = tensor(M, perm)
        exact = (b * a).is_zero() and (c * b).is_zero() and \
            a.rank() == M.dim and c.rank() == M.dim and \
            a.rank() + b.rank() == mid.dim and b.rank() + c.rank() == mid.dim
        check(exact and is_projective(mid, 3),
              'Cor 3.5.3 (p. 65-66): 0 -> M -> M (x) R(G/H) -> M (x) R(G/H) '
              '-> M -> 0 exact, middle terms projective (A4, GF(3), dim M = '
              '%d)' % M.dim)
        O2 = Resolution(M, 2).omega(2)

        def nonproj(X):
            out = []
            for Y, d, k in summand_classes(X):
                Ym = gap_mats_to_mod(G, F, Y)
                if not is_projective(Ym, 3):
                    out.append((Ym, k))
            return out
        a1, a2 = nonproj(O2), nonproj(M)
        ok = sorted((Y.dim, k) for Y, k in a1) == \
            sorted((Y.dim, k) for Y, k in a2)
        for Y, k in a1:
            ok &= any(isomorphic(Y, Z) and k == l for Z, l in a2)
        check(ok, 'Cor 3.5.3 (p. 65): Omega~^2(M) (+) proj ~ M (+) proj '
              '(A4, GF(3), dim M = %d)' % M.dim)

    # p. 66: projective cover of k, Omega(k), Omega^2(k) for Z/n over GF(p).
    for n, p in [(2, 2), (3, 3), (4, 2), (6, 2), (6, 3), (8, 2), (9, 3),
                 (10, 2), (12, 2), (12, 3)]:
        Gr = group('C%d' % n)
        F = GF(p)
        ps = p ** ZZ(n).valuation(p)
        k = trivial(Gr, F)
        Pk = None
        for X, d, mlt in summand_classes(regular(Gr, F)):
            Xm = gap_mats_to_mod(Gr, F, X)
            rad = mtx('BasisRadical')(X)
            top = gap_mats_to_mod(Gr, F,
                                  mtx('InducedActionFactorModule')(X, rad))
            if isomorphic(top, k):
                Pk = Xm
        R2 = Resolution(k, 2)
        Om = R2.omega(1)
        Om1 = [Y for Y, d, mlt in summand_classes(Om)
               for _ in range(mlt)]
        nonp = [gap_mats_to_mod(Gr, F, Y) for Y in Om1]
        nonp = [Y for Y in nonp if not is_projective(Y, p)]
        ok = Pk is not None and Pk.dim == ps and len(nonp) == 1 and \
            nonp[0].dim == ps - 1
        if ok and ps > 2:
            Y = nonp[0]
            # uniserial with trivial composition factors: x - 1 nilpotent of
            # rank dim - 1 and the p'-part acting trivially
            X = Y.mats[Gr.gens[0]] - identity_matrix(F, Y.dim)
            ok &= X.rank() == Y.dim - 1 and (X ** Y.dim).is_zero()
        check(ok, 'p. 66: for Z/%d over GF(%d) the projective cover of k has '
              'dimension p^s = %d and Omega(k) is uniserial of length %d '
              'with trivial factors' % (n, p, ps, ps - 1))
        O2 = R2.omega(2)
        cls = [gap_mats_to_mod(Gr, F, Y) for Y, d, mlt in summand_classes(O2)]
        cls = [Y for Y in cls if not is_projective(Y, p)]
        check(len(cls) == 1 and isomorphic(cls[0], k),
              'p. 66: Omega^2(k) ~ k for Z/%d over GF(%d)' % (n, p))

    # Proposition 3.5.5 (p. 67) by the Cartan-Eilenberg diagonal: on the
    # periodic resolution every cochain is a cocycle and none is a
    # coboundary (p | n); f_r u f_s = (-1)^(rs) aug(Delta_rs) f_(r+s).
    for n in range(2, 13):
        for p in [2, 3, 5, 7, 11]:
            if n % p:
                continue
            ps = p ** ZZ(n).valuation(p)
            npairs = n * (n - 1) // 2
            x2 = GF(p)(-npairs)
            check((x2 != 0) == (ps == 2),
                  'Prop 3.5.5 (p. 67): x^2 = %s y in H^2(Z/%d, GF(%d)), '
                  'nonzero iff p^s = 2' % (x2, n, p))
    # Corollary 3.5.4 (p. 66): with sigma = f_2, f_r u sigma = (-1)^(2r)
    # aug(Delta_(r,2)) f_(r+2) = f_(r+2), so cup with sigma is the identity
    # M -> M on the periodic cochains in degrees r > 0, and sigma^k = f_(2k)
    # generates H^(2k)(Z/n, R) = R/nR.
    Pq = PolynomialRing(ZZ, 'x,y')
    xq, yq = Pq.gens()
    for r in range(6):
        Drs = Pq(1) if r % 2 == 0 else yq     # Delta_(r,2), s = 2 even
        check(Drs(1, 1) == 1, 'Cor 3.5.4 (p. 66): aug(Delta_(%d,2)) = 1' % r)
    for n in (2, 3, 4, 6):
        check(H_cyclic_Z(n, 2) == canon(0, [n]) and n > 1,
              'Cor 3.5.4: sigma^k generates H^(2k)(Z/%d, ZZ) = ZZ/%d != 0'
              % (n, n))
    for n, p in [(3, 2), (4, 3), (5, 2)]:
        Gr = group('C%d' % n)
        check(Bar(Gr, trivial(Gr, GF(p))).h_dim(2) == 0,
              'Cor 3.5.4: if n is invertible in R then H^2(Z/n, R) = 0, so '
              'sigma = 0 (Z/%d, GF(%d))' % (n, p))
    for n, p in [(2, 2), (3, 3), (4, 2), (5, 5), (6, 2), (6, 3), (8, 2),
                 (9, 3)]:
        Gr = group('C%d' % n)
        F = GF(p)
        B = Bar(Gr, trivial(Gr, F))
        ps = p ** ZZ(n).valuation(p)
        x = B.nonzero_class(1)
        y = B.nonzero_class(2)
        x2 = B.is_coboundary(B.cup(x, 1, x, 1), 2)
        xy = B.is_coboundary(B.cup(x, 1, y, 2), 3)
        y2 = B.is_coboundary(B.cup(y, 2, y, 2), 4) if n <= 9 else False
        dims = [B.h_dim(r) for r in range(1, 4)]
        check(dims == [1, 1, 1], 'p. 66: H^r(Z/%d, GF(%d)) is one '
              'dimensional, r = 1, 2, 3' % (n, p))
        check(x2 == (ps > 2) and not xy and not y2,
              'Prop 3.5.5 (p. 67): in H*(Z/%d, GF(%d)) (Alexander-Whitney): '
              'x^2 %s, xy != 0, y^2 != 0'
              % (n, p, '= 0' if ps > 2 else '!= 0'))

    # The diagonal approximation Delta_rs (p. 67).
    def delta_ok(n, T_sign, strict, oo_sign=1, mmax=6):
        P = PolynomialRing(ZZ, 'x,y')
        x0, y0 = P.gens()
        A = P.quotient([x0 ** n - 1, y0 ** n - 1])
        x, y = A(x0), A(y0)

        def D(m, z):
            if m % 2:
                return (z - 1) if T_sign > 0 else (1 - z)
            return sum(z ** i for i in range(n))
        S = sum(x ** i * y ** j for i in range(n)
                for j in range(i + (1 if strict else 0), n))

        def Dl(r, s):
            if r % 2 == 0:
                return A(1)
            return y if s % 2 == 0 else oo_sign * S
        for m in range(1, mmax + 1):
            for r1 in range(m):
                s1 = m - 1 - r1
                lhs = D(m, x * y) * Dl(r1, s1)
                rhs = Dl(r1 + 1, s1) * D(r1 + 1, x) + \
                    (-1) ** r1 * Dl(r1, s1 + 1) * D(s1 + 1, y)
                if lhs != rhs:
                    return False
        return True
    for n in range(2, 9):
        check(delta_ok(n, +1, True),
              'p. 67 (corrected i < j): Delta_rs is a chain map for the '
              'resolution with T = x - 1 (Cartan-Eilenberg), Z/%d, total '
              'degree <= 6' % n)
        refuted(delta_ok(n, +1, False),
                'p. 67 (printed i <= j): Delta_rs is a chain map, Z/%d' % n)
        refuted(delta_ok(n, -1, False),
                'p. 67 (printed i <= j) with T = 1 - x, Z/%d' % n)
        refuted(delta_ok(n, -1, True),
                'p. 67: i < j with T = 1 - x of Prop. 3.5.1 needs a sign, '
                'Z/%d' % n)
        check(delta_ok(n, -1, True, oo_sign=-1),
              'p. 67: with T = 1 - x the odd-odd component is '
              '-sum_(i<j) x^i (x) x^j (Z/%d)' % n)

    # Theorem 3.5.6 (Kuenneth, p. 67).
    for a, b in [(2, 2), (2, 4), (3, 3), (2, 3), (4, 6), (3, 9)]:
        Zm = product_resolution_Z_matrices(a, b, 5)
        check(exact_Z(Zm), 'Thm 3.5.6 proof (p. 67): P (x)_R Q is a free '
              'resolution of ZZ over ZZ(C%d x C%d) (degrees <= 4)' % (a, b))
        pr = product_resolution(a, b, 8)
        deltas = trivial_cochains(pr, 8)
        Gg = libgap.AbelianGroup([a, b])
        for n in range(7):
            H = cohomology_Z(deltas, n)
            results[(a, b, n)] = H
            tens = ab_sum(*[ab_tensor(H_cyclic_Z(a, i), H_cyclic_Z(b, n - i))
                            for i in range(n + 1)])
            torp = ab_sum(*[ab_tor(H_cyclic_Z(a, i),
                                   H_cyclic_Z(b, n + 1 - i))
                            for i in range(n + 2)])
            torm = ab_sum(*[ab_tor(H_cyclic_Z(a, i),
                                   H_cyclic_Z(b, n - 1 - i))
                            for i in range(n)])
            check(ab_sum(tens, torp) == H,
                  'Thm 3.5.6 (p. 67, corrected i + j = n + 1): '
                  'H^%d(C%d x C%d, ZZ) = %s' % (n, a, b, H))
            if n in (3, 5) and gcd(a, b) > 1:
                refuted(ab_sum(tens, torm) == H,
                        'Thm 3.5.6 (printed i + j = n - 1): H^%d(C%d x C%d, '
                        'ZZ)' % (n, a, b))
        check(results[(a, b, 2)] == canon(0, list(Gg.AbelianInvariants())),
              'H^2(C%d x C%d, ZZ) ~ Hom(G, QQ/ZZ) (GAP AbelianInvariants)'
              % (a, b))
        check(results[(a, b, 3)] ==
              canon(0, list(Gg.AbelianInvariantsMultiplier())),
              'H^3(C%d x C%d, ZZ) ~ H_2(G, ZZ) = M(G) (GAP '
              'AbelianInvariantsMultiplier)' % (a, b))
    # coefficients: M1 = ZZ, M2 = ZZ/p (R-projective M1): holds;
    # M1 = M2 = ZZ/p (no hypothesis): fails.
    for p in (2, 3):
        pr = product_resolution(p, p, 8)
        dF = trivial_cochains(pr, 8, R=GF(p))
        for n in range(7):
            dim = dF[n].ncols() - dF[n].rank() - (dF[n - 1].rank() if n else 0)
            check(dim == n + 1, 'H^%d(C%d x C%d, GF(%d)) has dimension %d '
                  '(Remark p. 67: k[x1,x2] or Lambda (x) k[y1,y2])'
                  % (n, p, p, p, n + 1))
            ok_free = ab_sum(
                *[ab_tensor(H_cyclic_Z(p, i), H_cyclic_Zp(p, p, n - i))
                  for i in range(n + 1)],
                *[ab_tor(H_cyclic_Z(p, i), H_cyclic_Zp(p, p, n + 1 - i))
                  for i in range(n + 2)])
            check(ab_order(ok_free) == p ** dim and exponent(ok_free) == p,
                  'Thm 3.5.6 (corrected, M1 = ZZ projective over R): '
                  'H^%d(C%d x C%d, ZZ (x) ZZ/%d)' % (n, p, p, p))
            bad = ab_sum(
                *[ab_tensor(H_cyclic_Zp(p, p, i), H_cyclic_Zp(p, p, n - i))
                  for i in range(n + 1)],
                *[ab_tor(H_cyclic_Zp(p, p, i), H_cyclic_Zp(p, p, n + 1 - i))
                  for i in range(n + 2)])
            refuted(ab_order(bad) == p ** dim,
                    'Thm 3.5.6 without a hypothesis on M1, M2: M1 = M2 = '
                    'ZZ/%d, n = %d (order %d vs %d)'
                    % (p, n, ab_order(bad), p ** dim))

    # Remark and Corollary 3.5.7 (pp. 67-68).
    for orders, p, top in [((2, 2, 2), 2, 5), ((3, 3, 3), 3, 4)]:
        Gr = abelian_group(orders, 'E')
        R = Resolution(trivial(Gr, GF(p)), top + 1)
        s = len(orders)
        check(R.ext_dims(trivial(Gr, GF(p)), top) ==
              [binomial(n + s - 1, s - 1) for n in range(top + 1)],
              'Cor 3.5.7 (p. 67-68): dim H^n((Z/%d)^%d, GF(%d)) = '
              'binom(n + %d, %d), n <= %d' % (p, s, p, s - 1, s - 1, top))
    E = abelian_group((2, 2), 'V4')
    B = Bar(E, trivial(E, GF(2)))
    x1, x2 = B.cocycles(1).basis()
    deg2 = [B.cup(x1, 1, x1, 1), B.cup(x1, 1, x2, 1), B.cup(x2, 1, x2, 1)]
    check(B.h_dim(2) == 3 and B.independent_mod_coboundaries(deg2, 2),
          'Cor 3.5.7 (i) (p. 67): x1^2, x1 x2, x2^2 form a basis of '
          'H^2((Z/2)^2, GF(2))')
    deg3 = [B.cup(c, 2, x, 1) for c in deg2[:2] for x in (x1, x2)]
    deg3 = [deg3[0], deg3[1], deg3[3], B.cup(deg2[2], 2, x2, 1)]
    check(B.h_dim(3) == 4 and B.independent_mod_coboundaries(deg3, 3),
          'Cor 3.5.7 (i): x1^3, x1^2 x2, x1 x2^2, x2^3 form a basis of '
          'H^3((Z/2)^2, GF(2))')
    E = abelian_group((2, 2, 2), 'E8')
    B = Bar(E, trivial(E, GF(2)))
    xs = B.cocycles(1).basis()
    deg2 = [B.cup(xs[i], 1, xs[j], 1) for i in range(3) for j in range(i, 3)]
    check(B.h_dim(2) == 6 and B.independent_mod_coboundaries(deg2, 2),
          'Cor 3.5.7 (i): the 6 monomials of degree 2 form a basis of '
          'H^2((Z/2)^3, GF(2))')
    E = abelian_group((3, 3), 'E9')
    F = GF(3)
    B = Bar(E, trivial(E, F))
    C3 = abelian_group((3,), 'C3')
    BC = Bar(C3, trivial(C3, F))
    yc = BC.nonzero_class(2)
    xs = []
    ys = []
    for coord in range(2):
        xs.append(vector(F, [E.els[g][coord] for g in E.all]))
        ys.append(vector(F, [yc[BC.index((E.els[g][coord], E.els[h][coord]))]
                             for g in E.all for h in E.all]))
    check(all(B.delta(1) * x == 0 for x in xs) and
          all(B.delta(2) * y == 0 for y in ys),
          'Cor 3.5.7 (ii): x_i in H^1, y_i (inflated from the factors) in '
          'H^2 are cocycles')
    check(all(B.is_coboundary(B.cup(x, 1, x, 1), 2) for x in xs),
          'Cor 3.5.7 (ii) (p. 68): x_i^2 = 0 in H^2((Z/3)^2, GF(3))')
    check(B.h_dim(2) == 3 and B.independent_mod_coboundaries(
        [B.cup(xs[0], 1, xs[1], 1)] + ys, 2),
        'Cor 3.5.7 (ii): x1 x2, y1, y2 form a basis of H^2((Z/3)^2, GF(3))')
    check(B.h_dim(3) == 4 and B.independent_mod_coboundaries(
        [B.cup(x, 1, y, 2) for x in xs for y in ys], 3),
        'Cor 3.5.7 (ii): x_i y_j form a basis of H^3((Z/3)^2, GF(3))')
    return results


# ===========================================================================
# 3.6 Relative projectivity and transfer
# ===========================================================================


def tr(Gr, H, Mp, M, phi, ambient=None):
    """Tr_(H, ambient)(phi) for phi : M' -> M (matrices of the modules)."""
    ambient = Gr.all if ambient is None else ambient
    reps, _ = Gr.left_cosets(H, ambient)
    out = zero_matrix(M.F, M.dim, Mp.dim)
    for t in reps:
        out += M.mats[t] * phi * Mp.mats[Gr.inv[t]]
    return out


def section_3_6(kun):
    # Lemma 3.6.3 (iii)-(vi) (p. 69), S4 and A4.
    G = group('S4')
    for F in (GF(2), GF(3)):
        S3 = G.closure([G.el('(1,2,3)'), G.el('(1,2)')])
        C2 = G.closure([G.el('(1,2)')])
        D8 = G.closure([G.el('(1,2,3,4)'), G.el('(1,3)')])
        V4 = G.closure([G.el('(1,3)(2,4)'), G.el('(1,2)(3,4)')])
        M1 = perm_module(G, F, S3)
        M2 = direct_sum(sign(G, F), perm_module(G, F, D8))
        alpha = random_hom(restrict(M1, C2), restrict(M2, C2))
        lhs = tr(G, S3, M1, M2, tr(G, C2, M1, M2, alpha, S3))
        check(lhs == tr(G, C2, M1, M2, alpha),
              'Lemma 3.6.3 (iii) (p. 69): Tr_(K,G) Tr_(H,K) = Tr_(H,G) '
              '(S4, GF(%d))' % F.order())
        for H, K in [(D8, S3), (S3, S3), (V4, C2), (D8, D8)]:
            beta = random_hom(restrict(M1, K), restrict(M2, K))
            rhs = zero_matrix(F, M2.dim, M1.dim)
            for g in G.double_cosets(H, K):
                I = G.intersect(H, G.conj_subgroup(g, K))
                gb = M2.mats[g] * beta * M1.mats[G.inv[g]]
                rhs += tr(G, I, M1, M2, gb, H)
            check(tr(G, K, M1, M2, beta) == rhs,
                  'Lemma 3.6.3 (iv) (p. 69): Tr_(K,G)(alpha) = sum_HgK '
                  'Tr_(H cap gK, H)(g alpha) (S4, |H| = %d, |K| = %d, '
                  'GF(%d))' % (len(H), len(K), F.order()))
            a = random_hom(restrict(M2, H), restrict(M2, H))
            b = random_hom(restrict(M2, K), restrict(M2, K))
            rhs = zero_matrix(F, M2.dim, M2.dim)
            for g in G.double_cosets(H, K):
                I = G.intersect(H, G.conj_subgroup(g, K))
                gb = M2.mats[g] * b * M2.mats[G.inv[g]]
                rhs += tr(G, I, M2, M2, a * gb)
            check(tr(G, H, M2, M2, a) * tr(G, K, M2, M2, b) == rhs,
                  'Lemma 3.6.3 (v) (p. 69) (S4, |H| = %d, |K| = %d, GF(%d))'
                  % (len(H), len(K), F.order()))
        # (vi): K <= H <= G, M_1 an RG-module, M_2 an RH-module
        K, H = C2, S3
        Mb = restrict(M2, H)
        Mi = induce(Mb)
        a = random_hom(restrict(M1, K), restrict(Mb, K))
        reps, where = G.left_cosets(H)
        i0 = where[0][0]
        inc = zero_matrix(F, Mi.dim, Mb.dim)
        inc.set_block(i0 * Mb.dim, 0, identity_matrix(F, Mb.dim))
        inner = tr(G, K, restrict(M1, H), Mb, a, H)
        hat = zero_matrix(F, Mi.dim, M1.dim)
        for i, t in enumerate(reps):
            hat.set_block(i * Mb.dim, 0, inner * M1.mats[G.inv[t]])
        check(hat == tr(G, K, M1, Mi, inc * a),
              'Lemma 3.6.3 (vi) (p. 70): hat Tr_(H,G) Tr_(K,H)(alpha) = '
              'Tr_(K,G)(i o alpha) (S4, GF(%d))' % F.order())

    # Higman's criterion (Proposition 3.6.4, p. 70): (v) <=> (vii).
    nh = 0
    for name, q, p in [('S3', 2, 2), ('S3', 3, 3), ('A4', 2, 2), ('D8', 2, 2),
                       ('A4', 3, 3)]:
        Gr = group(name)
        F = GF(q)
        mods = [trivial(Gr, F)]
        mods += [perm_module(Gr, F, H) for H in subgroups(Gr)
                 if 1 < len(H) < Gr.n][:3]
        if name == 'S3':
            mods.append(sign(Gr, F))
        for H in subgroups(Gr):
            if len(H) == Gr.n:
                continue
            for M in mods[:4]:
                MH = restrict(M, H)
                E = hom_space(MH, MH)
                imgs = [tr(Gr, H, M, M, e) for e in E]
                idv = identity_matrix(F, M.dim).list()
                vii = matrix(F, [X.list() for X in imgs]).rank() == \
                    matrix(F, [X.list() for X in imgs] + [idv]).rank()
                v = is_summand(M, induce(MH))
                check(v == vii, 'Prop 3.6.4 (p. 70): M | M down_H up^G iff '
                      '1_M in Im Tr_(H,G) (%s, GF(%d), |H| = %d, dim M = %d:'
                      ' %s)' % (name, q, len(H), M.dim, v))
                nh += 1
                if (Gr.n // len(H)) % p:
                    check(v and tr(Gr, H, M, M, identity_matrix(F, M.dim)) ==
                          (Gr.n // len(H)) * identity_matrix(F, M.dim),
                          'Cor 3.6.9, 3.6.10 (p. 72): Tr_(H,G)(1/|G:H|) = 1 '
                          'when |G : H| is invertible (%s, |H| = %d)'
                          % (name, len(H)))

    # Corollaries 3.6.11, 3.6.12 (Maschke) and the Remark (p. 72).
    Gr = group('S3')
    for q in (5, 7):
        F = GF(q)
        mods = [regular(Gr, F),
                perm_module(Gr, F, Gr.closure([Gr.el('(1,2)')])),
                tensor(regular(Gr, F), sign(Gr, F))]
        ok = all(all(mtx('IsIrreducible')(X) for X, d, k in summand_classes(M))
                 for M in mods)
        check(ok, 'Cor 3.6.11, 3.6.12 (p. 72): every GF(%d)S3-module is '
              'semisimple' % q)
    F = GF(7)
    M = perm_module(Gr, F, Gr.closure([Gr.el('(1,2)')]))
    ones = matrix(F, [[1], [1], [1]])
    lam = matrix(F, [[3, 5, F(1) - 8]])
    rho = ones * lam
    check(rho * rho == rho and rho * ones == ones, 'Remark p. 72: rho is a '
          'linear projection onto M_1 = <(1,1,1)>')
    S = sum(M.mats[g] * rho * M.mats[Gr.inv[g]] for g in Gr.all)
    rho1 = S / F(Gr.n)
    check(rho1 * rho1 == rho1 and is_hom(M, M, rho1) and rho1 * ones == ones
          and rho1.rank() == 1,
          'Remark p. 72 (author\'s correction): rho\' = (1/|G|) sum g rho '
          'g^-1 is a G-invariant projection onto M_1 (S3, GF(7))')
    refuted(S * S == S, 'Remark p. 72 (printed rho\' = sum g rho g^-1): a '
            'projection (S3, GF(7))')

    # Transfer in cohomology (p. 73, corrected) and Lemma 3.6.16 (iv).
    for name, q, Hs in [('S3', 2, ['(1,2)', '(1,2,3)']),
                        ('A4', 2, ['(1,2,3)']),
                        ('S3', 3, ['(1,2)'])]:
        Gr = group(name)
        F = GF(q)
        k = trivial(Gr, F)
        R = Resolution(k, 3)
        targets = [k] if name != 'S3' or q != 2 else \
            [k, submodule(perm_module(Gr, F, Gr.closure([Gr.el('(1,2)')])),
                          matrix(F, [[1, 0], [1, 1], [0, 1]]))]
        for Hg in Hs:
            H = Gr.closure([Gr.el(Hg)])
            for Mp in targets:
                for n in (1, 2):
                    Pn = free_module(Gr, F, R.ranks[n])
                    Pn1 = free_module(Gr, F, R.ranks[n + 1])
                    D = R.D[n + 1]
                    a = random_hom(restrict(Pn, H), restrict(Mp, H))
                    lhs = tr(Gr, H, Pn, Mp, a) * D
                    rhs = tr(Gr, H, Pn1, Mp, a * D)
                    check(lhs == rhs and is_hom(Pn, Mp, tr(Gr, H, Pn, Mp, a)),
                          'p. 73: Tr(alpha) o d_(n+1) = Tr(alpha o d_(n+1)) '
                          '(%s, GF(%d), |H| = %d, dim M\' = %d, n = %d)'
                          % (name, q, len(H), Mp.dim, n))
                    refuted(Mp.dim == Pn.dim,
                            'p. 73 (printed d_n o Tr(alpha)): the composite '
                            'of alpha : P_n -> M\' with d_n : P_n -> P_(n-1) '
                            'is defined')
    # Lemma 3.6.16 (iv) on cochains
    for name, q, Hg, Kg in [('S3', 2, ['(1,2)'], ['(1,3)']),
                            ('S4', 2, ['(1,2,3,4)', '(1,3)'],
                             ['(1,2,3)', '(1,2)']),
                            ('A4', 2, ['(1,2,3)'], ['(1,2)(3,4)',
                                                    '(1,3)(2,4)'])]:
        Gr = group(name)
        F = GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        K = Gr.closure([Gr.el(s) for s in Kg])
        k = trivial(Gr, F)
        R = Resolution(k, 2)
        for n in (1, 2):
            Pn = free_module(Gr, F, R.ranks[n])
            a = random_hom(restrict(Pn, K), restrict(k, K))
            lhs = tr(Gr, K, Pn, k, a)
            rhs = zero_matrix(F, 1, Pn.dim)
            notsub = False
            for g in Gr.double_cosets(H, K):
                gK = Gr.conj_subgroup(g, K)
                I = Gr.intersect(H, gK)
                notsub |= not set(I) <= set(K)
                ga = k.mats[g] * a * Pn.mats[Gr.inv[g]]
                check(is_hom(restrict(Pn, gK), restrict(k, gK), ga),
                      'Lemma 3.6.16 (iv): g alpha is a map of R(gK)-modules')
                rhs += tr(Gr, I, Pn, k, ga, H)
            check(lhs == rhs, 'Lemma 3.6.16 (iv) (p. 73, corrected '
                  'res_(gK, H cap gK)): res_(G,H) Tr_(K,G)(alpha) = sum '
                  'Tr_(H cap gK, H) res(g alpha) on cochains (%s, n = %d)'
                  % (name, n))
            if name == 'S3':
                refuted(not notsub, 'Lemma 3.6.16 (iv) (printed res_(K, H cap '
                        'gK)): H cap gK <= K for every double coset (S3, '
                        'H = <(1,2)>, K = <(1,3)>)')
    # Proposition 3.6.17, first sentence, on cochains
    Gr = group('S4')
    F = GF(3)
    k = trivial(Gr, F)
    R = Resolution(k, 2)
    D8 = Gr.closure([Gr.el('(1,2,3,4)'), Gr.el('(1,3)')])
    P2 = free_module(Gr, F, R.ranks[2])
    a = random_hom(P2, k)
    check(tr(Gr, D8, P2, k, a) == 3 * a,
          'Prop 3.6.17 (p. 73): Tr_(H,G) res_(G,H) = |G : H| on cochains '
          '(S4, H = D8)')
    # second sentence (corrected: M projective over R)
    ok = all(exponent(H) == 1 or (a * b) % exponent(H) == 0
             for (a, b, n), H in kun.items() if n > 0)
    check(ok, 'Prop 3.6.17 (p. 73, corrected: M = ZZ projective over ZZ): '
          '|G| H^n(C_a x C_b, ZZ) = 0 for n > 0 (6 groups, n <= 6)')
    deltas, ints = cyclic_with_Zm(2, 3, 5, ZZ)
    d1 = ints[1]
    check(exact_Z(ints[1:], onto=False) and
          canon(d1.nrows() - d1.rank(), [d for d in d1.elementary_divisors()
                                         if d not in (0, 1)]) == canon(0, [3]),
          'ZZ C2-free resolution of ZZ/3: P (x) (ZZ -3-> ZZ) has H_0 = ZZ/3 '
          'and is exact in degrees 1..3')
    E1 = cohomology_Z(deltas, 1)
    check(E1 == canon(0, [3]), 'Ext^1_(ZZ C2)(ZZ/3, ZZ) ~ ZZ/3')
    refuted(exponent(E1) == 1 or 2 % exponent(E1) == 0,
            'Prop 3.6.17 (printed, no hypothesis on M): |G| = 2 annihilates '
            'Ext^1_(ZZ C2)(ZZ/3, ZZ)')
    # Corollary 3.6.18 (p. 73)
    Gr = group('C3')
    check(ext_dims(trivial(Gr, GF(2)), trivial(Gr, GF(2)), 4) ==
          [1, 0, 0, 0, 0], 'Cor 3.6.18 (p. 73): H^n(C3, GF(2)) = 0 for n > 0')
    Gr = group('S3')
    F = GF(5)
    for M in [trivial(Gr, F), sign(Gr, F),
              perm_module(Gr, F, Gr.closure([Gr.el('(1,2)')]))]:
        for N in [trivial(Gr, F), sign(Gr, F), regular(Gr, F)]:
            check(ext_dims(M, N, 2)[1:] == [0, 0],
                  'Cor 3.6.18 (p. 73): Ext^n_(GF(5)S3)(M, N) = 0, n = 1, 2')
    # Corollary 3.6.19 (p. 74) with M = k (R-projective)
    for name, p, Ngen, top in [('S3', 2, ['(1,2)'], 6),
                               ('A4', 3, ['(1,2,3)'], 6),
                               ('S5', 5, ['(1,2,3,4,5)', '(2,3,5,4)'], 8)]:
        Gr = group(name)
        F = GF(p)
        N = Gr.closure([Gr.el(s) for s in Ngen])
        P = Gr.closure([Gr.el(Ngen[0])])
        check(Gr.n % (len(P) * p) != 0, 'P = <%s> is a Sylow %d-subgroup of %s'
              % (Ngen[0], p, name))
        ti = all(len(Gr.intersect(P, Gr.conj_subgroup(g, P))) in (1, len(P))
                 for g in Gr.all)
        check(ti and set(P) <= set(N) and
              all(Gr.conj_subgroup(g, P) == P for g in N) and
              len([g for g in Gr.all if Gr.conj_subgroup(g, P) == P]) ==
              len(N), 'Cor 3.6.19: P is a T.I. Sylow %d-subgroup of %s with '
              'normaliser of order %d' % (p, name, len(N)))
        NG = FinGroup(*_subgroup_table(Gr, N))
        a = ext_dims(trivial(Gr, F), trivial(Gr, F), top)
        b = ext_dims(trivial(NG, F), trivial(NG, F), top)
        check(a == b, 'Cor 3.6.19 (p. 74): H^n(%s, GF(%d)) ~ H^n(N_G(P), '
              'GF(%d)), n <= %d (%s)' % (name, p, p, top, a))
    # the Example (p. 74-75): H*(S_p, k), H*(S_p, sign), p = 3, 5
    for p, top in [(3, 8), (5, 8)]:
        Gr = group('S%d' % p)
        F = GF(p)
        R = Resolution(trivial(Gr, F), top + 1)
        triv = R.ext_dims(trivial(Gr, F), top)
        sgn = R.ext_dims(sign(Gr, F), top)
        q = 2 * (p - 1)
        exp_t = [1 if (n % q == 0 or n % q == q - 1) else 0
                 for n in range(top + 1)]
        exp_s = [1 if (n % q == p - 1 or n % q == p - 2) else 0
                 for n in range(top + 1)]
        check(triv == exp_t, 'Example p. 74: H^n(S_%d, GF(%d)) has basis '
              'y^(k(p-1)), x y^(k(p-1)-1): dims %s, n <= %d'
              % (p, p, triv, top))
        check(sgn == exp_s, 'Example p. 75: H^n(S_%d, sign) has basis '
              'y^((2k+1)(p-1)/2), x y^((2k+1)(p-1)/2 - 1): dims %s'
              % (p, sgn))
        # h acts on H^1(P, k) = Hom(P, k) by a primitive (p-1)-th root
        g = Gr.el('(%s)' % ','.join(str(i) for i in range(1, p + 1)))
        h = None
        for c in Gr.all:
            for s in range(2, p):
                if Gr.conj(c, g) == Gr.power(g, s) and \
                        Gr.order_of(c) == p - 1:
                    h, sh = c, s
        check(h is not None and GF(p)(sh).multiplicative_order() == p - 1,
              'Example p. 74: N_G(P) = <g, h | h g h^-1 = g^s>, s a '
              'primitive root mod %d' % p)
        # f(g^j) = j; (h f)(g^j) = f(h^-1 g^j h) = s^-1 j
        hinv = Gr.inv[h]
        scal = None
        for j in range(1, p):
            gj = Gr.power(g, j)
            c = Gr.m(hinv, gj, h)
            jj = [i for i in range(p) if Gr.power(g, i) == c][0]
            sc = GF(p)(jj) / GF(p)(j)
            scal = sc if scal is None else scal
            assert sc == scal
        check(scal.multiplicative_order() == p - 1,
              'Example p. 74: h acts on H^1(P, k) by a primitive (p-1)-th '
              'root of unity (s or s^-1, S_%d)' % p)

    # Corollary 3.6.19 needs M projective over R: R = ZZ_(2), G = S3, P = C2,
    # M = M' = V (2-dimensional over GF(2)).  Ext over ZZ_(2) G of these
    # 2-torsion modules = Ext over ZZ G (flat base change), computed here.
    G = group('S3')
    F2 = GF(2)
    S = G.all
    P = G.closure([G.el('(1,2)')])
    V = submodule(perm_module(G, F2, P), matrix(F2, [[1, 0], [1, 1], [0, 1]]))
    n = G.n
    v = vector(F2, [1, 0])
    check(matrix(F2, [V.mats[g] * v for g in S]).rank() == 2 and
          mtx('IsIrreducible')(gap_module(V)),
          'V is simple and cyclic (generated by v)')
    A = matrix(F2, [list(V.mats[g] * v) for g in range(n)]).transpose()
    gens = [2 * vector(ZZ, [1 if i == j else 0 for i in range(n)])
            for j in range(n)]
    gens += [vector(ZZ, [ZZ(int(c)) for c in w])
             for w in A.right_kernel().basis()]
    L = matrix(ZZ, gens).hermite_form()
    L = L.matrix_from_rows([i for i in range(L.nrows())
                            if not L.row(i).is_zero()])
    Kb = L.rows()
    Lt = L.transpose()
    Kmats = {}
    for g in S:
        imgs = []
        for b in Kb:
            w = [0] * n
            for x in range(n):
                w[G.mul[g][x]] += b[x]
            imgs.append(w)
        X = Lt.solve_right(matrix(ZZ, imgs).transpose())
        Kmats[g] = X.change_ring(F2)
    Kbar = Mod(G, S, F2, n, Kmats)

    def ext1(H):
        KH, VH = restrict(Kbar, H), restrict(V, H)
        Z = hom_space(KH, VH)
        rreps, seen = [], set()
        for x in range(n):
            if x not in seen:
                rreps.append(x)
                seen |= {G.mul[h][x] for h in H}
        cob = []
        for r in rreps:
            for w in identity_matrix(F2, 2).columns():
                vals = {G.mul[h][r]: VH.mats[h] * w for h in H}
                cols = []
                for b in Kb:
                    acc = vector(F2, [0, 0])
                    for x in range(n):
                        if b[x] % 2 and x in vals:
                            acc += vals[x]
                    cols.append(acc)
                cob.append(matrix(F2, cols).transpose())
        assert all(is_hom(KH, VH, X) for X in cob)
        Zs = matrix(F2, [X.list() for X in Z]).row_space()
        Bs = matrix(F2, [X.list() for X in cob]).row_space()
        assert Bs.is_subspace(Zs)
        return Zs, Bs
    ZG_, BG_ = ext1(S)
    ZP_, BP_ = ext1(P)
    dG = ZG_.dimension() - BG_.dimension()
    dP = ZP_.dimension() - BP_.dimension()
    img = (ZG_ + BP_).dimension() - BP_.dimension()
    check((dG, dP, img) == (1, 2, 1),
          'Ext^1_(ZZ S3)(V, V) = GF(2), Ext^1_(ZZ C2)(V, V) = GF(2)^2, '
          'restriction has rank 1')
    refuted(img == dP, 'Cor 3.6.19 (printed, no hypothesis on M): '
            'res_(G, N_G(P)) : Ext^1_(R S3)(V, V) -> Ext^1_(R C2)(V, V) is '
            'onto (R = ZZ_(2), P = N_G(P) = C2 a T.I. Sylow 2-subgroup, '
            '|G : P| = 3 invertible)')
    return nh


# ===========================================================================
# 3.7 Low degree cohomology
# ===========================================================================


def regular_perm_group(mul):
    n = len(mul)
    return PermutationGroup([[mul[g][x] + 1 for x in range(n)]
                             for g in range(n)], domain=list(range(1, n + 1)))


def section_3_7():
    # Proposition 3.7.2 (p. 75): complements in M x| G.
    cases = []
    C2 = group('C2')
    S3 = group('S3')
    C3 = group('C3')
    C4 = group('C4')
    F2, F3 = GF(2), GF(3)
    swap = matrix(F2, [[0, 1], [1, 0]])
    rot = matrix(F2, [[0, 1], [1, 1]])
    cases.append((C2, trivial(C2, F2)))
    cases.append((C2, from_gens(C2, F2, 2, {C2.gens[0]: swap})))
    cases.append((C3, from_gens(C3, F2, 2, {C3.gens[0]: rot})))
    cases.append((S3, submodule(perm_module(S3, F2,
                                            S3.closure([S3.el('(1,2)')])),
                                matrix(F2, [[1, 0], [1, 1], [0, 1]]))))
    cases.append((C2, from_gens(C2, F3, 1, {C2.gens[0]: matrix(F3, [[-1]])})))
    cases.append((C2, from_gens(C2, F2, 2,
                                {C2.gens[0]: identity_matrix(F2, 2)})))
    cases.append((C4, trivial(C4, F2)))
    cases.append((S3, sign(S3, F3)))
    for G, M in cases:
        F = M.F
        p = F.order()
        Ms = [vector(F, v) for v in itertools.product(F, repeat=M.dim)]
        for v in Ms:
            v.set_immutable()
        mpos = {v: i for i, v in enumerate(Ms)}
        els = [(m, g) for g in G.all for m in Ms]
        pos = {(mpos[m], g): i for i, (m, g) in enumerate(els)}

        def prod(a, b):
            (m1, g1), (m2, g2) = a, b
            m = m1 + M.mats[g1] * m2
            m.set_immutable()
            return (m, G.mul[g1][g2])
        mul = [[pos[(mpos[prod(a, b)[0]], prod(a, b)[1])] for b in els]
               for a in els]
        PG = libgap(regular_perm_group(mul))
        Msub = PG.Subgroup([PG.GeneratorsOfGroup()[pos[(mpos[m], 0)]]
                            for m in Ms])
        ncl = len(PG.ComplementClassesRepresentatives(Msub))
        B = Bar(G, M)
        h1 = B.h_dim(1)
        check(ncl == p ** h1, 'Prop 3.7.2 (p. 75): |H^1(%s, M)| = %d = '
              'number of conjugacy classes of complements (dim M = %d, '
              'GF(%d))' % (G.name, p ** h1, M.dim, p))
        # the conjugation formula beta' - beta = (1 - g)(m - beta[g'])
        Z1 = B.cocycles(1)
        ok = True
        for beta in Z1:
            bv = [beta[i * M.dim:(i + 1) * M.dim] for i in range(G.n)]
            for m in Ms:
                for gp in G.all:
                    c = (m, gp)
                    ci = (-(M.mats[G.inv[gp]] * m), G.inv[gp])
                    for g in G.all:
                        el = prod(prod(c, (bv[g], g)), ci)
                        # el is the conjugate; its G-part:
                        h = el[1]
                        # beta'(h) = M-part of el; compare formula at h
                        lhs = el[0] - bv[h]
                        rhs = (identity_matrix(F, M.dim) - M.mats[h]) * \
                            (m - bv[gp])
                        ok &= lhs == rhs
        check(ok, 'Prop 3.7.2 proof (p. 75): conjugating by (m, g\') gives '
              'beta\'[g] - beta[g] = (1 - g)(m - beta[g\']) (%s, dim M = %d)'
              % (G.name, M.dim))

    # Proposition 3.7.3 (p. 76): extensions of C2 x C2 by GF(2).
    V4 = abelian_group((2, 2), 'V4')
    F = GF(2)
    M = trivial(V4, F)
    B = Bar(V4, M)
    n = V4.n

    def ext_group(alpha):
        els = [(m, g) for g in range(n) for m in range(2)]
        pos = {e: i for i, e in enumerate(els)}
        mul = [[pos[((m1 + m2 + int(alpha[g1 * n + g2])) % 2,
                     V4.mul[g1][g2])]
                for (m2, g2) in els] for (m1, g1) in els]
        return mul

    def assoc(mul):
        N = len(mul)
        return all(mul[mul[a][b]][c] == mul[a][mul[b][c]]
                   for a in range(N) for b in range(N) for c in range(N))
    Z2 = B.cocycles(2)
    B2 = B.delta(1).column_space()
    comp = [z for z in Z2.basis()]
    # a complement of B^2 in Z^2
    reps = []
    W = B2
    for z in comp:
        if z not in W:
            reps.append(z)
            W = W + Z2.span([z])
    check(len(reps) == 3 and B.h_dim(2) == 3, 'H^2(C2 x C2, GF(2)) has '
          'order 8')
    counts = {}
    for coeffs in itertools.product(F, repeat=3):
        alpha = sum((c * r for c, r in zip(coeffs, reps)), Z2.zero())
        mul = ext_group(alpha)
        check(assoc(mul), 'Prop 3.7.3 (p. 76): a 2-cocycle gives an '
              'associative multiplication')
        idg = tuple(int(c) for c in libgap(regular_perm_group(mul)).IdGroup())
        counts[idg] = counts.get(idg, 0) + 1
        if all(c == 0 for c in coeffs):
            check(idg == (8, 5), 'Prop 3.7.3: the zero class is the split '
                  'extension C2 x C2 x C2')
    check(counts == {(8, 5): 1, (8, 2): 3, (8, 3): 3, (8, 4): 1},
          'Prop 3.7.3 (p. 76): the 8 classes of H^2(C2 x C2, GF(2)) give '
          'C2^3 (1), C4 x C2 (3), D8 (3), Q8 (1)')
    bad = 0
    for _ in range(20):
        alpha = vector(F, [F.random_element() for _ in range(n * n)])
        if B.delta(2) * alpha != 0:
            bad += 1
            check(not assoc(ext_group(alpha)), 'Prop 3.7.3: a non-cocycle '
                  'gives a non-associative multiplication')
    check(bad > 0, 'Prop 3.7.3: some random 2-cochains are not cocycles')
    # cohomologous cocycles: (m, g) -> (m + beta(g), g) is an isomorphism
    ok = True
    for _ in range(10):
        alpha = reps[0] + reps[2]
        beta = vector(F, [F.random_element() for _ in range(n)])
        alpha2 = alpha + B.delta(1) * beta
        m1, m2 = ext_group(alpha2), ext_group(alpha)
        els = [(m, g) for g in range(n) for m in range(2)]
        pos = {e: i for i, e in enumerate(els)}
        phi = [pos[((m + int(beta[g])) % 2, g)] for (m, g) in els]
        ok &= all(phi[m1[a][b]] == m2[phi[a]][phi[b]]
                  for a in range(8) for b in range(8))
    check(ok, 'Prop 3.7.3 proof (p. 76): alpha + delta beta and alpha give '
          'isomorphic extensions via (m, g) -> (m + beta(g), g)')
    # C3 x C3 by GF(3): 27 classes
    E = abelian_group((3, 3), 'E9')
    F = GF(3)
    BE = Bar(E, trivial(E, F))
    check(BE.h_dim(2) == 3, 'H^2(C3 x C3, GF(3)) has order 27')
    Z2 = BE.cocycles(2)
    W = BE.delta(1).column_space()
    reps = []
    for z in Z2.basis():
        if z not in W:
            reps.append(z)
            W = W + Z2.span([z])
    ids = {}
    for coeffs in itertools.product(F, repeat=3):
        alpha = sum((c * r for c, r in zip(coeffs, reps)), Z2.zero())
        els = [(m, g) for g in range(9) for m in range(3)]
        pos = {e: i for i, e in enumerate(els)}
        mul = [[pos[((m1 + m2 + int(alpha[g1 * 9 + g2])) % 3, E.mul[g1][g2])]
                for (m2, g2) in els] for (m1, g1) in els]
        idg = tuple(int(c) for c in libgap(regular_perm_group(mul)).IdGroup())
        ids[idg] = ids.get(idg, 0) + 1
    check(sum(ids.values()) == 27 and all(i[0] == 27 for i in ids),
          'Prop 3.7.3: the 27 classes of H^2(C3 x C3, GF(3)) give groups of '
          'order 27 (%s)' % sorted(ids.items()))
    # Corollary 3.7.4 (p. 77)
    for name, q, M in [('C3', 2, 'rot'), ('S3', 5, 'sign'), ('C5', 2, 'triv'),
                       ('A4', 5, 'perm')]:
        Gr = group(name)
        F = GF(q)
        if M == 'rot':
            Mm = from_gens(Gr, F, 2, {Gr.gens[0]: matrix(F, [[0, 1], [1, 1]])})
        elif M == 'sign':
            Mm = sign(Gr, F)
        elif M == 'perm':
            Mm = perm_module(Gr, F, Gr.closure([Gr.el('(1,2,3)')]))
        else:
            Mm = trivial(Gr, F)
        check(ext_dims(trivial(Gr, F), Mm, 2)[2] == 0,
              'Cor 3.7.4 (p. 77): H^2(%s, M) = 0, |G| invertible in GF(%d)'
              % (name, q))

    # Proposition 3.7.5 (p. 77), corrected kernel ZZ/m with m | |G|_p'.
    ok_div, counter = True, []
    for q in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27, 32, 49, 64]:
        F = GF(q)
        p = F.characteristic()
        units = [a for a in F if a != 0]
        for N in range(1, 31):
            onto = len(set(a ** N for a in units)) == q - 1
            ker = len([a for a in units if a ** N == 1])
            Np = N // p ** ZZ(N).valuation(p)
            ok_div &= Np % ker == 0
            if onto and ker != Np:
                counter.append((q, N))
    check(ok_div, 'Prop 3.7.5 proof (corrected): the kernel of x -> x^|G| on '
          'GF(q)^x has order m dividing |G|_p\' (q <= 64, |G| <= 30)')
    refuted((8, 3) not in counter and (2, 3) not in counter,
            'Prop 3.7.5 proof (printed ZZ/|G|_p\'): the kernel is ZZ/3 for '
            '|G| = 3 and k = GF(8) or GF(2), where every element has a cube '
            'root')
    roots = [r for r, e in PolynomialRing(AA, 't')('t^3 - 1').roots()]
    check(roots == [1], 'Prop 3.7.5: in RR (algebraic reals) every element '
          'has a cube root and 1 is the only cube root of unity, so the '
          'kernel is ZZ/1, not ZZ/3')
    # Pauli matrices: a projective representation of C2 x C2
    X = matrix(QQ, [[0, 1], [1, 0]])
    Zm = matrix(QQ, [[1, 0], [0, -1]])
    Gp = libgap.Group([libgap(X), libgap(Zm)])
    scal = [g for g in Gp.AsList()
            if libgap(g).IsDiagonalMat() and g[0][0] == g[1][1]]
    check(Gp.Size() == 8 and len(scal) == 2 and X * Zm == -Zm * X,
          'Prop 3.7.5, Cor 3.7.6: lifts of C2 x C2 -> PGL_2 generate a finite '
          'group of order 8 meeting the scalars in {+-1}')
    # Remark (i): <QQ^x, sqrt 2> (corrected)
    P = PolynomialRing(QQ, 't')
    t = P.gen()
    check(not QQ(2).is_square() and (2 * t ** 2 - 1).roots(QQ) == [],
          'Remark (i) (p. 77, corrected <QQ^x, sqrt 2>): sqrt 2 not in QQ, '
          '(q sqrt 2)^2 = 2q^2 != 1, so the only elements of finite order '
          'are +-1 in QQ^x and no finite G^ has G~ = G^.QQ^x')
    refuted(QQ(0).is_unit(), 'Remark (i) (printed <QQ, sqrt 2>): QQ lies in '
            'the multiplicative group')

    # Exercise (p. 78): H^1(G, R) = Hom(G, R^+).
    for name in ['C4', 'C2xC2', 'S3', 'D8', 'Q8', 'A4']:
        Gr = group(name)
        inv = [int(d) for d in libgap(Gr.sage).AbelianInvariants()]
        for q in (2, 3):
            B = Bar(Gr, trivial(Gr, GF(q)))
            homs = 1
            for d in inv:
                homs *= gcd(d, q)
            check(q ** B.h_dim(1) == homs and B.delta(0).is_zero(),
                  'Exercise p. 78: |H^1(%s, GF(%d))| = |Hom(G, GF(%d)^+)| = %d'
                  % (name, q, q, homs))
        # R = ZZ/4: count 1-cocycles = homomorphisms by brute force
        cnt = 0
        for vals in itertools.product(range(4), repeat=len(Gr.gens)):
            f = {0: 0}
            frontier, good = [0], True
            while frontier and good:
                new = []
                for x in frontier:
                    for s, v in zip(Gr.gens, vals):
                        y = Gr.mul[x][s]
                        if y in f:
                            good &= f[y] == (f[x] + v) % 4
                        else:
                            f[y] = (f[x] + v) % 4
                            new.append(y)
                frontier = new
            good = good and all(f[Gr.mul[x][y]] == (f[x] + f[y]) % 4
                                for x in Gr.all for y in Gr.all)
            cnt += good
        homs = 1
        for d in inv:
            homs *= gcd(d, 4)
        check(cnt == homs, 'Exercise p. 78: |Hom(%s, ZZ/4)| = %d factors '
              'through G^ab' % (name, homs))

    # The example before Theorem 3.7.8 (p. 78).
    ok = True
    for i in range(3, 13):
        x = 2 ** (i - 1) + 1
        lifts = [y for y in range(x, 2 ** (i + 1), 2 ** i)
                 if (y * y) % 2 ** (i + 1) == 1]
        ok &= (x * x) % 2 ** i == 1 and lifts == []
    check(ok, 'p. 78: (2^(i-1) + 1) is a representation of C2 over ZZ/2^i '
          'that does not lift to ZZ/2^(i+1), 3 <= i <= 12')
    check(3 % 4 == 4 - 1 and ((2 ** 0 + 1) % 2 == 0),
          'p. 78: for i = 2 the matrix (3) = (-1) lifts, for i = 1 (2) is '
          'not invertible: the example needs i >= 3 ("i arbitrarily large")')

    # Theorem 3.7.8 (p. 79): the kernels in the corrected diagram (plain
    # integer arithmetic on n x n matrices stored as tuples).
    def mmul(A, B, n_, N):
        return tuple(sum(A[i * n_ + k] * B[k * n_ + j] for k in range(n_)) % N
                     for i in range(n_) for j in range(n_))

    def ident(n_):
        return tuple(1 if i == j else 0 for i in range(n_) for j in range(n_))

    def det_unit(A, n_, p):
        d = A[0] if n_ == 1 else A[0] * A[3] - A[1] * A[2]
        return d % p != 0

    for p, r, nn in [(2, 1, 1), (2, 1, 2), (3, 1, 1), (2, 2, 1), (3, 1, 2),
                     (5, 1, 1)]:
        a = 2 * r + 1
        I = ident(nn)
        ok = True
        for N, lo in [(a + r + 1, a), (a + 1, a - r)]:
            q = p ** N
            Ys = list(itertools.product(range(p ** (N - lo)), repeat=nn * nn))
            ker = set()
            for Y in Ys:
                K = tuple((I[i] + p ** lo * Y[i]) % q for i in range(nn * nn))
                ok &= det_unit(K, nn, p)
                ker.add(K)
            # every matrix = 1 mod p^lo is of this form, and they are distinct
            ok &= len(ker) == len(Ys) == p ** ((r + 1) * nn * nn)
            sample = Ys if len(Ys) <= 81 else random.sample(Ys, 81)
            for X in sample:
                for Y in sample[:20]:
                    KX = tuple((I[i] + p ** lo * X[i]) % q
                               for i in range(nn * nn))
                    KY = tuple((I[i] + p ** lo * Y[i]) % q
                               for i in range(nn * nn))
                    S = tuple((I[i] + p ** lo * (X[i] + Y[i])) % q
                              for i in range(nn * nn))
                    ok &= mmul(KX, KY, nn, q) == S
        # vertical map: 1 + p^a X (mod p^(a+r+1)) reduces mod p^(a+1) to
        # 1 + p^(a-r) Y with Y = p^r X (mod p^(r+1))
        for X in itertools.product(range(p ** (r + 1)), repeat=nn * nn):
            red = tuple((I[i] + p ** a * X[i]) % p ** (a + 1)
                        for i in range(nn * nn))
            Y = tuple((p ** r * X[i]) % p ** (r + 1) for i in range(nn * nn))
            ok &= red == tuple((I[i] + p ** (a - r) * Y[i]) % p ** (a + 1)
                               for i in range(nn * nn))
        check(ok, 'Thm 3.7.8 (p. 79, corrected p^(r+1)): the kernels of '
              'GL_n(Z/p^(a+r+1)) -> GL_n(Z/p^a) and GL_n(Z/p^(a+1)) -> '
              'GL_n(Z/p^(a-r)) are 1 + p^a X, 1 + p^(a-r) Y with X, Y in '
              'M_n(Z/p^(r+1)) = End(M~/p^(r+1)M~), abelian, and the vertical '
              'map is p^r (p = %d, r = %d, n = %d)' % (p, r, nn))
        refuted(p ** ((r + 1) * nn * nn) == p ** ((r - 1) * nn * nn),
                'Thm 3.7.8 (printed p^(r-1)): the kernel has the order of '
                'End(M~/p^(r-1)M~) (p = %d, r = %d, n = %d)' % (p, r, nn))
    # the conclusion of Theorem 3.7.8 exhaustively: C2 (r = 1, a = 3,
    # n = 1, 2) and C4 (r = 2, a = 5, n = 1)
    for order, p, r, nn in [(2, 2, 1, 1), (2, 2, 1, 2), (4, 2, 2, 1)]:
        a = 2 * r + 1
        I = ident(nn)

        def reps_mod(q):
            out = []
            for A in itertools.product(range(q), repeat=nn * nn):
                if not det_unit(A, nn, p):
                    continue
                P_ = I
                for _ in range(order):
                    P_ = mmul(P_, A, nn, q)
                if P_ == I:
                    out.append(A)
            return out
        low = p ** (a - r)
        top = set(tuple(c % low for c in A) for A in reps_mod(p ** (a + 1)))
        ok = all(tuple(c % low for c in A) in top for A in reps_mod(p ** a))
        check(ok, 'Thm 3.7.8 (p. 79): every representation of C%d over '
              'ZZ/%d (n = %d) agrees mod %d with one over ZZ/%d'
              % (order, p ** a, nn, low, p ** (a + 1)))


def main():
    section_3_1()
    section_3_2()
    nmack = section_3_3()
    section_3_4()
    kun = section_3_5()
    section_3_6(kun)
    section_3_7()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
