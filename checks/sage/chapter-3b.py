"""Exact checks of Chapter 3, Sections 3.8-3.15 (Sage, with GAP via libgap).

Benson, *Representations and Cohomology I*, second edition (1998),
Chapter 3 "Modules for group algebras", Sections 3.8-3.15, printed
pp. 79-98.  Our files: content/03-08-stable-elements.typ ...
content/03-15-tensor-induction.typ.  (Sections 3.1-3.7 are checked in
chapter-3a.py; this script does not import it.)

Everything below is an exact computation over finite fields, ZZ/p^a, ZZ
or QQ for small groups: cyclic groups, C2 x C2, C2^3, C4 x C2, C3 x C3,
D8, Q8, S3, A4, S4, A5, D10, C3 : C4, GL(3, 2), all groups of order
p^k <= 32, 81, 125, 49 and 13 of the 267 groups of order 64 (GAP small
groups library), with explicit modules given by matrices, linear algebra,
and the GAP MeatAxe (through libgap) for decompositions and isomorphism
tests of modules.  Expected values are the book's statements and formulas,
read off the printed pages (the page and our label are named in each
message); the chapter files are not parsed.  Where the printed text was
corrected, the printed reading is kept as a refuted check next to the
corrected one.

Checked here (by section):

3.8 (pp. 79-80)
  * Proposition 3.8.2 on cochains of one free resolution of k: res_(G,H)
    is injective with image the stable elements (Definition 3.8.1), for
    H a Sylow p-subgroup and M' = k, sign, w (GF(4)), the 2-dimensional
    module of S4 (15 pairs (G, p) among S3, A4, S4, A5, C3 : C4, D10,
    degrees <= 3 or 4), and for M' = R_H up^G with H not a Sylow subgroup
    (S4, D8; S3, C2; A4, C3; S4, C2 x C2); stability for all g equals
    stability for double coset representatives.  Without the hypothesis
    (k over GF(3) is not projective relative to C2 in S3) restriction kills
    H^3(S3, GF(3)).
  * The proof (corrected first display): Tr_(H,G)(theta res(alpha)) =
    Tr_(H,G)(theta) alpha = alpha (Lemma 3.6.16 (ii)) on cocycles, theta
    from Higman's criterion; the printed res(alpha) theta (Lemma 3.6.16
    (i)) composes theta in End_RH(M') after alpha's source M and is
    refuted for M = k != M'.  The converse: the first line of the display
    exactly (Mackey formula on cochains) and res Tr(theta beta) = beta
    modulo coboundaries for stable beta.
  * Definition 3.8.3 (literally) and Proposition 3.8.4 for N_G(P), P an
    abelian Sylow subgroup: S4 (p = 3), A5 (p = 2, 3, 5), A4 (3), S3 (2),
    C3 : C4 (2), GL(3, 2) (7); the steps K1, K2 of the proof.  D8 does not
    control 2-fusion in S4 and H^1 differs.  The Remark: C2 controls
    2-fusion in C6 but H^n(C6, w) = 0 != H^n(C2, w) = k, the element of
    order 3 acting on it by w.

3.9 (pp. 81-83)
  * Relatively H-projective resolutions (Definition 3.9.2: exact, onto M,
    terms relatively H-projective by Higman, pieces H-split) for 10 pairs
    (G, H); relative cohomology H^n(G, H, k) independent of the resolution
    (a second one with a free summand), H = 1 gives Ext_RG, H normal gives
    H^n(G/H, k); the natural map Ext_(G,H) -> Ext_RG is zero in degree 2
    for C4 relative to C2 (not injective, p. 82).
  * Theorem 3.9.3: chain maps over 1_k, a second one, and a homotopy with
    the corrected f_n - f'_n = d'_(n+1) h_n + h_(n-1) d_n; the printed
    d_(n+1) h_n does not compose.  The corrected display (Hom(X_0, M')):
    H^0 = Hom_RG(M, M').
  * Lemma 3.9.1 (relative Schanuel) as module isomorphisms (4 cases, 3
    pairs each); Lemma 3.9.4 (relative horseshoe) built explicitly for 4
    H-split sequences, exact, H-split; both long exact sequences of p. 83
    exact (ranks of all maps, the connecting maps by the snake lemma).

3.10, 3.11 (pp. 83-84)
  * For all indecomposable summands of the transitive permutation modules
    and of Omega^1(k), Omega^2(k) and other modules of 14 pairs (group,
    field) among S3, C4, C2 x C2, D8, Q8, A4, S4, C3 : C4, A5: the minimal
    subgroups D with M relatively D-projective form one conjugacy class of
    p-subgroups (Proposition 3.10.2 (i), (iii)); the sources are conjugate
    under N_G(D) (ii); trivial source iff summand of a permutation module
    (Lemma 3.11.2); the Mackey decompositions of the proof of 3.10.2 as
    printed (module isomorphisms).
  * Lemma 3.11.2, proof (corrected index D g H): R_H up^G down_D ~
    sum_(DgH) R_(D cap gH) up^D for 5 triples; the printed index H g D does
    not determine D cap gH (S4, H = <(12)>, D = D8: orders 1 and 2 in the
    double coset H D), and for the first representatives found even the
    dimension is wrong.
  * Theorem 3.11.3 (Scott) for all pairs of subgroup classes of S3, A4, S4,
    D8, A5 (index <= 30): the orbit matrices are a ZZ-basis of the integral
    G-maps, their number is that of the double cosets H2 g H1, they
    reduce to a basis over GF(p).
    Corollary 3.11.4: idempotents of End_kG(k[G/H]) lift to idempotents
    over ZZ/p^4 commuting with G, two lifts are conjugate by a unit,
    homomorphisms between the summands lift (6 permutation modules).

3.12 (pp. 85-87)
  * The sets X and Y (X in Y, D not in Y) and Theorem 3.12.2 (i)-(iv),
    Lemma 3.12.1 (i), (ii) module by module for 14 pairs (D, H >= N_G(D))
    in S4, S3, D8, A4, A5, GL(3, 2) and all indecomposable RH-modules with
    vertex D that are summands of S up^H for S = k, Jordan blocks of cyclic
    D, Omega(k) for D = C2 x C2; g is a bijection on trivial source modules
    with vertex D; (v) as an isomorphism of the quotients by the
    X-transfers (4 pairs per case).
  * Theorem 3.12.3: for the summands of permutation modules and the Green
    correspondents, V down_H with a summand of vertex D implies vertex D and
    V ~ g(M); the proof: e = Tr_(D,H)(alpha) is the idempotent of M,
    Tr_(D,G)(alpha) = sum_(HgD) Tr_(H cap gD, H)(g alpha) (Lemma 3.6.3 (iv)
    with K = D, an identity in End_R(V)) = e mod (V, V)^H_Y, a unit.

3.13 (pp. 87-91)
  * Mackey (M up^G down_N), the inertia group (contains N C_G(N), cosets),
    Proposition 3.13.2 for all indecomposable summands of permutation
    modules of N in 11 pairs (G, N).
  * E = End(M up^G) for inertial M (8 cases): E = sum E_g with dim E_g =
    dim End_kN(M); E_g E_g' = E_(g'g) for composition (the printed
    E_g E_g' = E_(gg') holds for maps written on the right; it fails as
    composition for G/N = S3); E_1 local, J(E_1) E_g = E_g J(E_1) of
    codimension one; J(E_1) E nilpotent of codimension |G : N|, equal to
    J(E) for p' quotients; E / J(E) = k for p-group quotients.
  * Theorem 3.13.3 (Green): M up^G absolutely indecomposable (End/J = k,
    GAP radical) for all absolutely indecomposable M in the lists, 9 pairs
    (G, N) with G/N a p-group; refuted for A4 / V4 (C3, p = 2).  Central
    p'-extensions of C_p split (all groups of order p m <= 84).
  * p. 90: J_a (2 <= a <= p) of Z/p does not extend to Z/p^n (p = 2, 3, 5,
    n = 2, 3, every Jordan type of the generator); for decomposable M the
    claim fails (J_2 + J_1 extends to J_3 of Z/4), but the M of the section
    is indecomposable.
  * pp. 90-91 (corrected): K is the kernel of the reduction modulo
    J End_kN(M), i.e. 1 + J: K = 1 iff End = k, elements of p-power order
    (C3, GF(3), J_2: all 6 units); with the printed determinant map K
    contains -1 (GF(5)S3, End = k; C3, J_2).
  * Theorem 3.13.4 (i) for D8 over GF(3), N = Z(D8): the pullback hat(G)
    of order 16, M_0 ~ hat(M) (x) V, M up^G = M_0 + M_0.

3.14 (pp. 91-96)
  * Lemma 3.14.1 (composition factors of kP; the orbit count of the proof
    for every m in every listed module with at most 81 elements),
    decomposition and Cartan matrices, Soc(kP), non-projective
    indecomposables kill Soc(kP), transitive permutation modules,
    Propositions 3.14.2-3.14.4 and Corollary 3.14.5 for 10 p-groups;
    Proposition 3.14.3 for 13 pairs (G, p).
  * Jennings' theorem for every group of order p^k <= 32 (p = 2), 81, 125,
    49 and 13 groups of order 64: F_r = Gamma_r (the book's definition of
    Gamma_r, and GAP's JenningsSeries), F_1 = P, F_2 = Phi(P),
    [F_r, F_s] <= F_(r+s), F_r^p <= F_(pr), Gamma_r / Gamma_(r+1)
    elementary abelian and central, the Poincare series, the radical length
    1 + sum (p - 1) r n_r, |P| = p^(sum n_r), dim J/J^2 = n_1, the symmetry;
    and for orders <= 32, 27 and 8 groups of order 81: Soc^i(kP) =
    J^(l-i)(kP)
    (Corollary 3.14.7) and the PBW basis prod (g_j - 1)^(a_j) of weight >= i
    spans J^i.  The identities of p. 93 in F_p P for all g, h (5 groups);
    Philip Hall's identity in the free group of rank 3.

3.15 (pp. 96-98)
  * The wreath embedding i (homomorphism for the printed product,
    injective, conjugate for other representatives) for 6 pairs; the action
    on M^n and M up^G = i^*(M^n).
  * Definition 3.15.1 and Proposition 3.15.2 for 5 pairs (G, H): (i) by the
    explicit shuffle of factors, independence of the representatives
    (explicit conjugation), (ii), (iii) (orbit sums induced from proper
    stabilisers containing the core), (iv) (stabilisers K >= core(H'),
    K cap H <= H'), (v) Mackey formula; (vi) (Dress) for 3 X-split
    non-split sequences, with the filtration U_j of the proof, and refuted
    without R X.

Not established: none of the general theorems is proved here.  Every
check concerns the listed groups, fields, modules and degrees only;
resolutions are truncated at the stated degree; MeatAxe isomorphism tests
are exact for the given modules (larger modules compared by their
indecomposable summands, Krull-Schmidt).  Not checked: the Yoneda product
and the non-Noetherian Ext^*_(G,H)(R, R) (p. 82), the exercise after
Proposition 3.10.2, the restricted Lie algebra axioms (p. 94), the twisted
group algebra of p. 89 beyond dimensions and radicals, Theorem 3.13.4 (ii).
Nothing here compares our Typst text with the printed book.

Run with:  sage -python checks/sage/chapter-3b.py
"""
import itertools
import random

from sage.all import (
    GF, QQ, ZZ, AlternatingGroup, CyclicPermutationGroup, DihedralGroup,
    IntegerModRing,
    PermutationGroup, PolynomialRing, QuaternionGroup, SymmetricGroup,
    VectorSpace, block_matrix, libgap, set_random_seed, vector,
)
from sage.all import identity_matrix as _identity_matrix
from sage.all import matrix as dmatrix
from sage.all import zero_matrix as _zero_matrix

SCOPE = 'chapter-3b'
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
    elif name == 'A5':
        G = AlternatingGroup(5)
    elif name == 'C4xC2':
        G = PermutationGroup(['(1,2,3,4)', '(5,6)'])
    elif name == 'D10':
        G = DihedralGroup(5)
    elif name == 'GL32':
        # GL(3, 2) = PSL(2, 7), as permutations of the 7 points of the
        # Fano plane (lines {i, i+1, i+3} mod 7)
        G = PermutationGroup(['(1,2,3,4,5,6,7)', '(2,3,5)(4,7,6)',
                              '(3,7)(5,6)'])
        assert G.order() == 168
    elif name == 'C3:C4':
        G = PermutationGroup(['(1,2,3)', '(1,2)(4,5,6,7)'])
        assert G.order() == 12
    elif name.startswith('C'):
        G = CyclicPermutationGroup(int(name[1:]))
    return FinGroup.from_sage(G, name)


def sylow(Gr, p):
    P = libgap(Gr.sage).SylowSubgroup(p)
    return tuple(sorted(Gr.idx[Gr.sage(x)] for x in P.AsList()))




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
    """M ~ N: MeatAxe isomorphism test for small modules; for larger ones
    (where the test can be slow) by the Krull-Schmidt theorem, comparing the
    indecomposable summands with multiplicities."""
    if M.dim != N.dim:
        return False
    if M.dim == 0:
        return True
    if M.dim <= 24:
        return mtx('IsomorphismModules')(gap_module(M), gap_module(N)) != FAIL
    a, b = summand_classes(M), summand_classes(N)
    iso = mtx('IsomorphismModules')
    if sorted((d, k) for X, d, k in a) != sorted((d, k) for X, d, k in b):
        return False
    used = set()
    for X, d, k in a:
        hit = [j for j, (Y, e, l) in enumerate(b) if j not in used and
               e == d and l == k and iso(X, Y) != FAIL]
        if not hit:
            return False
        used.add(hit[0])
    return True


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
    mats = [matrix(F, [[F(c.sage(ring=F)) for c in row] for row in A])
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




def right_cosets(Gr, H):
    """Representatives y of the right cosets H y and x -> (h, y) with
    x = h y."""
    reps, where = [], {}
    for x in Gr.all:
        if x in where:
            continue
        reps.append(x)
        for h in H:
            where[Gr.mul[h][x]] = (h, x)
    return reps, where


def subspace(F, dim, vecs):
    return VectorSpace(F, dim).subspace([vector(F, v) for v in vecs])


# ===========================================================================
# Cochains Hom(F_n, M) on one free resolution F of k over F G
# ===========================================================================


class Cochains:
    """Hom_k(F_n, M) for the free resolution F -> k of Resolution, as
    d x (|G| r_n) matrices (column (i, x) is the value on x e_i), flattened
    row by row.  Restriction to a subgroup is the identity on these
    coordinates; Hom_H(F_n, M) is a subspace."""

    def __init__(self, Gr, F, nmax):
        self.Gr, self.F = Gr, F
        self.res = Resolution(trivial(Gr, F), nmax + 1)
        self.D = [sp(D) for D in self.res.D]
        self.r = self.res.ranks
        self._cache = {}

    def width(self, n):
        return self.Gr.n * self.r[n]

    def vec(self, phi):
        return vector(self.F, phi.list())

    def mat(self, M, n, v):
        return matrix(self.F, M.dim, self.width(n), list(v))

    def hom_basis(self, H, M, n):
        """Basis of Hom_H(F_n, M): phi(h y e_i) = h m for right coset
        representatives y."""
        key = ('hom', H, id(M), n)
        if key in self._cache:
            return self._cache[key]
        Gr, F, d = self.Gr, self.F, M.dim
        reps, where = right_cosets(Gr, H)
        out = []
        for i in range(self.r[n]):
            for y in reps:
                for c in range(d):
                    phi = zero_matrix(F, d, self.width(n))
                    for x in Gr.all:
                        h, yy = where[x]
                        if yy == y:
                            col = M.mats[h].column(c)
                            for a in range(d):
                                if col[a]:
                                    phi[a, i * Gr.n + x] = col[a]
                    out.append(phi)
        self._cache[key] = out
        return out

    def delta(self, phi, n):
        """phi o D_(n+1) : F_(n+1) -> M."""
        return phi * self.D[n + 1]

    def cocycles(self, H, M, n):
        key = ('Z', H, id(M), n)
        if key in self._cache:
            return self._cache[key]
        B = self.hom_basis(H, M, n)
        W = dmatrix(self.F, [self.vec(self.delta(b, n)) for b in B])
        K = W.left_kernel().basis()
        Bv = [self.vec(b) for b in B]
        Z = subspace(self.F, M.dim * self.width(n),
                     [sum((c * v for c, v in zip(k, Bv)),
                          vector(self.F, M.dim * self.width(n)))
                      for k in K])
        self._cache[key] = Z
        return Z

    def coboundaries(self, H, M, n):
        key = ('B', H, id(M), n)
        if key in self._cache:
            return self._cache[key]
        A = M.dim * self.width(n)
        if n == 0:
            S = subspace(self.F, A, [])
        else:
            S = subspace(self.F, A, [self.vec(self.delta(b, n - 1))
                                     for b in self.hom_basis(H, M, n - 1)])
        self._cache[key] = S
        return S

    def h_dim(self, H, M, n):
        return (self.cocycles(H, M, n).dimension()
                - self.coboundaries(H, M, n).dimension())

    def conj(self, g, M, n, v):
        """(g phi)(b) = g phi(g^-1 b) on flattened cochains."""
        Gr = self.Gr
        phi = M.mats[g] * self.mat(M, n, v)
        gi = Gr.inv[g]
        cols = [i * Gr.n + Gr.mul[gi][x] for i in range(self.r[n])
                for x in Gr.all]
        return self.vec(phi.matrix_from_columns(cols))

    def transfer(self, H, K, M, n, v):
        """Tr_(H, K)(phi) = sum over left cosets t H in K of t phi."""
        reps, _ = self.Gr.left_cosets(H, K)
        out = vector(self.F, M.dim * self.width(n))
        for t in reps:
            out += self.conj(t, M, n, v)
        return out

    def stable(self, H, M, n, gs=None):
        """The stable cocycles: z in Z_H with z - g z in B_(H cap gH) for all
        g (Definition 3.8.1 on cochains); contains B_H."""
        Gr, F = self.Gr, self.F
        Z = self.cocycles(H, M, n)
        Zb = Z.basis()
        if not Zb:
            return Z
        gs = Gr.all if gs is None else gs
        rows = []
        for g in gs:
            K = Gr.intersect(H, Gr.conj_subgroup(g, H))
            Bk = self.coboundaries(K, M, n)
            C = Bk.complement().basis()
            if not C:
                continue
            Cm = dmatrix(F, C)
            diffs = dmatrix(F, [z - self.conj(g, M, n, z) for z in Zb])
            rows.append((Cm, diffs))
        if not rows:
            return Z
        # coefficient vectors c with sum c_j (1 - g) z_j orthogonal to C
        cols = [sp(diffs) * sp(Cm).transpose() for Cm, diffs in rows]
        W = block_matrix([cols], subdivide=False).dense_matrix()
        K = W.left_kernel().basis()
        return subspace(F, len(Zb[0]),
                        [sum((c * z for c, z in zip(k, Zb)), 0 * Zb[0])
                         for k in K])


def omega_module(Gr, F):
    """A 1-dimensional F G-module for a group G with G / O^3... = C3: the
    elements of order prime to 3 generate a normal subgroup N with G / N
    cyclic of order 3 (A4, C6); a fixed generator of G / N acts by a
    primitive cube root of unity w (F = GF(4))."""
    w = F.multiplicative_generator() ** ((F.order() - 1) // 3)
    N = Gr.closure([x for x in Gr.all if Gr.order_of(x) % 3])
    assert Gr.n == 3 * len(N) and Gr.is_normal(N)
    g0 = [x for x in Gr.all if x not in N][0]
    Ns = set(N)
    mats = {}
    for x in Gr.all:
        for i in range(3):
            if Gr.mul[x][Gr.inv[Gr.power(g0, i)]] in Ns:
                mats[x] = matrix(F, [[w ** i]])
    M = Mod(Gr, Gr.all, F, 1, mats)
    assert all(mats[Gr.mul[a][b]] == mats[a] * mats[b]
               for a in Gr.all for b in Gr.all)
    return M


def omega_module_on(Gr, F, N):
    """omega_module for a subgroup N with a normal subgroup of index 3
    generated by the elements of order prime to 3 (C3, A4, C6)."""
    N0 = Gr.closure([x for x in N if Gr.order_of(x) % 3])
    assert len(N) == 3 * len(N0)
    w = F.multiplicative_generator() ** ((F.order() - 1) // 3)
    g0 = [x for x in N if x not in set(N0)][0]
    S0 = set(N0)
    mats = {}
    for x in N:
        for i in range(3):
            if Gr.mul[x][Gr.inv[Gr.power(g0, i)]] in S0:
                mats[x] = matrix(F, [[w ** i]])
    assert all(mats[Gr.mul[a][b]] == mats[a] * mats[b] for a in N for b in N)
    return Mod(Gr, N, F, 1, mats)


def gap_subgroup(Gr, H):
    gens = [Gr.els[h] for h in Gr.gens_of(H)] or [Gr.els[0]]
    return libgap(Gr.sage).Subgroup([libgap(g) for g in gens])


def from_gap_subgroup(Gr, K):
    return tuple(sorted(Gr.idx[Gr.sage(x)] for x in K.AsList()))


def is_p_power(n, p):
    while n % p == 0:
        n //= p
    return n == 1


def all_subgroups(Gr, H=None, p=None):
    """All subgroups of H (default G), or all p-subgroups if p is given."""
    Hg = gap_subgroup(Gr, Gr.all if H is None else H)
    out = []
    for c in Hg.ConjugacyClassesSubgroups():
        if p is not None and not is_p_power(int(c.Representative().Size()),
                                            p):
            continue
        for K in c.AsList():
            out.append(from_gap_subgroup(Gr, K))
    return sorted(out, key=len)


def normalizer(Gr, H):
    S = set(H)
    return tuple(g for g in Gr.all
                 if all(Gr.conj(g, h) in S for h in H))


def controls_fusion(Gr, H, p):
    """Definition 3.8.3, checked literally."""
    P = sylow(Gr, p)
    if not any(set(Gr.conj_subgroup(g, P)) <= set(H) for g in Gr.all):
        return False
    Hs = set(H)
    for K1 in all_subgroups(Gr, H, p):
        for g in Gr.all:
            K2 = set(Gr.conj(g, k) for k in K1)
            if not K2 <= Hs:
                continue
            if not any(all(Gr.conj(g, k) == Gr.conj(h, k) for k in K1)
                       for h in H):
                return False
    return True


def tr(Gr, H, Mp, M, phi, ambient=None):
    """Tr_(H, ambient)(phi) for phi : M' -> M (matrices of the modules)."""
    ambient = Gr.all if ambient is None else ambient
    reps, _ = Gr.left_cosets(H, ambient)
    out = zero_matrix(M.F, M.dim, Mp.dim)
    for t in reps:
        out += M.mats[t] * phi * Mp.mats[Gr.inv[t]]
    return out


def higman_theta(Gr, H, M, ambient=None):
    """theta in End_H(M) with Tr_(H, ambient)(theta) = 1, or None
    (Higman's criterion, Proposition 3.6.4 (vii))."""
    F = M.F
    MH = restrict(M, H)
    E = hom_space(MH, MH)
    T = [tr(Gr, H, M, M, e, ambient) for e in E]
    A = dmatrix(F, [t.list() for t in T])
    one = vector(F, identity_matrix(F, M.dim).list())
    try:
        c = A.solve_left(one)
    except ValueError:
        return None
    return sum((ci * e for ci, e in zip(c, E)), zero_matrix(F, M.dim))


def s4_two_dim(Gr, F):
    """The 2-dimensional module of S4 through S4 / V4 = S3: the sum-zero
    vectors of the permutation module on the cosets of D8."""
    D8 = Gr.closure([Gr.el('(1,2,3,4)'), Gr.el('(1,3)')])
    X = perm_module(Gr, F, D8)
    return submodule(X, matrix(F, [[1, 0], [-1, 1], [0, -1]]))


# ===========================================================================
# 3.8 Stable elements
# ===========================================================================


def stable_case(C, H, M, n, label, dbl=None):
    """Proposition 3.8.2 in degree n: injectivity and image = stable."""
    Gr = C.Gr
    S = C.stable(H, M, n, dbl)
    B = C.coboundaries(H, M, n)
    ZG = C.cocycles(Gr.all, M, n)
    BG = C.coboundaries(Gr.all, M, n)
    hg = ZG.dimension() - BG.dimension()
    check(ZG.intersection(B) == BG,
          'Prop 3.8.2 (p. 79): res_(G,H) is injective on H^%d (%s)'
          % (n, label))
    check(ZG + B == S and S.dimension() - B.dimension() == hg,
          'Prop 3.8.2 (p. 79): the image of res_(G,H) in degree %d is the '
          'set of stable elements (%s; dim %d)' % (n, label, hg))
    return S, B, ZG, hg


def section_3_8():
    # Proposition 3.8.2 (p. 79) with M = k and H = P a Sylow p-subgroup
    # (k is projective relative to P), coefficients M' = k or a non-trivial
    # module ("the same description may be applied to H^n(G, M)", p. 80).
    cases = [('S3', 2, 2, 'k', 4), ('S3', 3, 3, 'k', 4),
             ('S3', 3, 3, 'sign', 4), ('A4', 2, 2, 'k', 3),
             ('A4', 4, 2, 'w', 3), ('A4', 3, 3, 'k', 4), ('S4', 2, 2, 'k', 3),
             ('S4', 2, 2, '2-dim', 3), ('S4', 3, 3, 'k', 4),
             ('S4', 3, 3, 'sign', 4), ('A5', 2, 2, 'k', 3),
             ('A5', 3, 3, 'k', 4), ('A5', 5, 5, 'k', 4),
             ('C3:C4', 2, 2, 'k', 4), ('D10', 5, 5, 'k', 4)]
    dims = {}
    for name, q, p, mod, N in cases:
        Gr, F = group(name), GF(q)
        P = sylow(Gr, p)
        M = {'k': trivial, 'sign': sign, 'w': omega_module,
             '2-dim': s4_two_dim}[mod](Gr, F)
        C = Cochains(Gr, F, N)
        dbl = Gr.double_cosets(P, P)
        for n in range(N + 1):
            label = '%s, P Sylow, M\' = %s, GF(%d)' % (name, mod, q)
            S, B, ZG, hg = stable_case(C, P, M, n, label, dbl)
            dims[(name, q, mod, n)] = hg
            if name == 'S3' and n == 2:
                check(C.stable(P, M, n) == S, 'Def 3.8.1 (p. 79): stability '
                      'for all g in G is stability for the double coset '
                      'representatives (%s)' % label)
    # (H^n(S3, GF(3)) = k in degrees 0, 3, 4 and 0 in degrees 1, 2: the
    # Example after Corollary 3.6.19, checked in chapter-3a.py.)
    check([dims[('S3', 3, 'k', n)] for n in range(5)] == [1, 0, 0, 1, 1],
          'Example p. 74: H^n(S3, GF(3)), n <= 4')
    check([dims[('S3', 3, 'sign', n)] for n in range(5)] == [0, 1, 1, 0, 0],
          'Example p. 75: H^n(S3, sign), n <= 4')

    # The hypothesis matters: k is not projective relative to C2 in S3
    # over GF(3), and res_(S3, C2) kills H^3(S3, GF(3)) = k.
    Gr, F = group('S3'), GF(3)
    C2 = Gr.closure([Gr.el('(1,2)')])
    k = trivial(Gr, F)
    C = Cochains(Gr, F, 3)
    check(higman_theta(Gr, C2, k) is None, 'Prop 3.6.4: GF(3) is not '
          'projective relative to C2 in S3')
    ZG, BH = C.cocycles(Gr.all, k, 3), C.coboundaries(C2, k, 3)
    refuted(ZG.intersection(BH) == C.coboundaries(Gr.all, k, 3),
            'Prop 3.8.2 without its hypothesis: res_(S3, C2) injective on '
            'H^3(S3, GF(3))')

    # M' projective relative to a subgroup H which is not a Sylow subgroup:
    # M' = R_H up^G.  Also the proof: theta in End_RH(M') with
    # Tr_(H,G)(theta) = 1; the first display (corrected) and the converse.
    for name, q, Hgens, N in [('S4', 2, ['(1,2,3,4)', '(1,3)'], 3),
                              ('S3', 3, ['(1,2)'], 4),
                              ('A4', 2, ['(1,2,3)'], 3),
                              ('S4', 3, ['(1,2)', '(3,4)'], 2)]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hgens])
        Mp = perm_module(Gr, F, H)
        theta = higman_theta(Gr, H, Mp)
        check(theta is not None, 'Prop 3.6.4 (p. 70): R_H up^G is '
              'projective relative to H (%s, |H| = %d)' % (name, len(H)))
        C = Cochains(Gr, F, N)
        dbl = Gr.double_cosets(H, H)
        for n in range(N + 1):
            label = '%s, |H| = %d, M\' = R_H up^G, GF(%d)' % (name, len(H), q)
            S, B, ZG, hg = stable_case(C, H, Mp, n, label, dbl)
            # first display, corrected: Tr_(H,G)(theta res(alpha)) =
            # Tr_(H,G)(theta) alpha = alpha (Lemma 3.6.16 (ii))
            ok = True
            for z in ZG.basis():
                tz = C.vec(theta * C.mat(Mp, n, z))
                ok = ok and C.transfer(H, Gr.all, Mp, n, tz) == z
            check(ok, 'Prop 3.8.2, proof (p. 80, corrected first display): '
                  'Tr_(H,G)(theta res_(G,H)(alpha)) = alpha on cocycles '
                  '(%s, n = %d)' % (label, n))
            # the printed res(alpha) theta: theta : M' -> M' cannot follow
            # alpha's source M = k (dim 1) when dim M' > 1
            refuted(Mp.dim == 1, 'Prop 3.8.2, proof (p. 80, '
                    'printed): res(alpha) theta is a composite for theta in '
                    'End_RH(M\'), M = k (%s)' % label)
            # converse: first line of the display exactly (Mackey formula on
            # cochains), last line modulo coboundaries
            for beta in S.basis()[:4]:
                tb = C.vec(theta * C.mat(Mp, n, beta))
                lhs = C.transfer(H, Gr.all, Mp, n, tb)
                rhs = 0 * lhs
                for g in dbl:
                    I = Gr.intersect(H, Gr.conj_subgroup(g, H))
                    rhs += C.transfer(I, H, Mp, n, C.conj(g, Mp, n, tb))
                check(lhs == rhs, 'Prop 3.8.2, proof (p. 80): res Tr(theta '
                      'beta) = sum_HgH Tr res(g(theta beta)) on cochains '
                      '(%s, n = %d)' % (label, n))
                check(lhs - beta in B, 'Prop 3.8.2, proof (p. 80): '
                      'res_(G,H) Tr_(H,G)(theta beta) = beta for stable beta '
                      '(%s, n = %d)' % (label, n))

    # Definition 3.8.3 and Proposition 3.8.4 (p. 80): H controls p-fusion
    # => res_(G,H) : H^n(G, k) -> H^n(H, k) is an isomorphism.
    for name, p, N in [('S4', 3, 4), ('A5', 2, 3), ('A5', 3, 4),
                       ('A5', 5, 4), ('A4', 3, 4), ('S3', 2, 4),
                       ('C3:C4', 2, 4), ('GL32', 7, 2)]:
        # H = N_G(P) for an abelian Sylow subgroup P (Burnside)
        Gr, F = group(name), GF(p)
        H = normalizer(Gr, sylow(Gr, p))
        check(controls_fusion(Gr, H, p), 'Def 3.8.3 (p. 80): H controls '
              '%d-fusion in %s (|H| = %d)' % (p, name, len(H)))
        C = Cochains(Gr, F, N)
        k = trivial(Gr, F)
        for n in range(N + 1):
            ZG, BG = C.cocycles(Gr.all, k, n), C.coboundaries(Gr.all, k, n)
            BH = C.coboundaries(H, k, n)
            check(ZG.intersection(BH) == BG and
                  ZG.dimension() - BG.dimension() == C.h_dim(H, k, n),
                  'Prop 3.8.4 (p. 80): res : H^%d(%s, GF(%d)) -> H^%d(H, '
                  'GF(%d)) is an isomorphism (|H| = %d)'
                  % (n, name, p, n, p, len(H)))
        # the proof: K1 = g^-1 S g cap S, K2 = S cap gS, gK1 = K2, and h
        S = sylow(Gr, p)
        ok = True
        for g in Gr.all:
            K1 = Gr.intersect(Gr.conj_subgroup(Gr.inv[g], S), S)
            K2 = Gr.intersect(S, Gr.conj_subgroup(g, S))
            ok = ok and Gr.conj_subgroup(g, K1) == K2
        check(ok, 'Prop 3.8.4, proof (p. 80): g K1 g^-1 = K2 (%s)' % name)
    # without control of fusion: D8 in S4 (p = 2); res is not onto in
    # degree 1 (dimensions 1 and 2).
    Gr, F = group('S4'), GF(2)
    D8 = Gr.closure([Gr.el('(1,2,3,4)'), Gr.el('(1,3)')])
    refuted(controls_fusion(Gr, D8, 2), 'Def 3.8.3: D8 controls 2-fusion in '
            'S4')
    C = Cochains(Gr, F, 1)
    k = trivial(Gr, F)
    check((C.h_dim(Gr.all, k, 1), C.h_dim(D8, k, 1)) == (1, 2),
          'H^1(S4, GF(2)) = k, H^1(D8, GF(2)) = k^2: res is not an '
          'isomorphism without control of fusion')

    # Remark (p. 80): C_G(K1) need not act trivially on Ext^n_(RK1)(M1, M2).
    # G = C6, p = 2, H = P = C2 controls 2-fusion; M2 = w (GF(4), the
    # element of order 3 acts by w): H^1(C6, w) = 0, H^1(C2, w) = k, and
    # the element c of order 3 (centralising C2) acts on it by w.
    Gr, F = group('C6'), GF(4)
    P = sylow(Gr, 2)
    check(controls_fusion(Gr, P, 2), 'Remark p. 80: C2 controls 2-fusion '
          'in C6')
    W = omega_module(Gr, F)
    C = Cochains(Gr, F, 2)
    for n in (1, 2):
        check(C.h_dim(Gr.all, W, n) == 0 and C.h_dim(P, W, n) == 1,
              'Remark p. 80: H^%d(C6, w) = 0, H^%d(C2, w) = k' % (n, n))
        z = [v for v in C.cocycles(P, W, n).basis()
             if v not in C.coboundaries(P, W, n)][0]
        c = [x for x in Gr.all if Gr.order_of(x) == 3][0]
        w = W.mats[c][0, 0]
        check(w != 1 and C.conj(c, W, n, z) - w * z in
              C.coboundaries(P, W, n), 'Remark p. 80: an element of '
              'C_G(K1) acts on H^%d(C2, w) by w != 1' % n)


# ===========================================================================
# Linear algebra helpers for maps of modules
# ===========================================================================


def solve_hom(basis, target_fn, rhs):
    """Find f = sum c_j basis_j with target_fn(f) = rhs (target_fn linear),
    or None."""
    F = rhs.base_ring()
    if not basis:
        return None if not rhs.is_zero() else None
    A = dmatrix(F, [vector(F, target_fn(b).list()) for b in basis])
    try:
        c = A.solve_left(vector(F, rhs.list()))
    except ValueError:
        return None
    return sum((ci * b for ci, b in zip(c, basis)), 0 * basis[0])


def colspace_basis(A):
    """Basis matrix (columns) of the column space of A."""
    A = A.dense_matrix() if hasattr(A, 'dense_matrix') else A
    return A.column_space().basis_matrix().transpose()


def kernel_cols(A):
    """Columns spanning the right kernel of A."""
    F = A.base_ring()
    K = kernel_basis(A)
    if not K:
        return dmatrix(F, A.ncols(), 0)
    return dmatrix(F, K).transpose()


def epsilon(N, H):
    """The natural surjection N down_H up^G -> N, t_i (x) n -> t_i n."""
    Gr = N.Gr
    reps, _ = Gr.left_cosets(H)
    X = induce(restrict(N, H))
    E = zero_matrix(N.F, N.dim, X.dim)
    for i, t in enumerate(reps):
        E.set_block(0, i * N.dim, N.mats[t])
    return X, E


def h_section(X, Y, e, H):
    """An R H-map s : Y -> X with e s = 1 (e : X -> Y onto), or None."""
    Gr = X.Gr
    basis = hom_space(restrict(Y, H), restrict(X, H))
    return solve_hom(basis, lambda s: e * s, identity_matrix(Y.F, Y.dim))


class RelRes:
    """A relatively H-projective resolution of a G-module M:
    X_n = K_(n-1) down_H up^G (+ free summands if extra), with
    eps_0 : X_0 -> M and d_n : X_n -> X_(n-1) (matrices)."""

    def __init__(self, M, H, N, extra=0):
        Gr, F = M.Gr, M.F
        self.M, self.H, self.X, self.d = M, H, [], []
        K, Kb = M, None          # K_(n-1) and its basis in X_(n-1)
        for n in range(N + 1):
            X, E = epsilon(K, H)
            if extra and n == 0:
                # add a free module kG mapping onto a random vector of M
                Fr = regular(Gr, F)
                v = vector(F, [F.random_element() for _ in range(K.dim)])
                f = matrix(F, [list(K.mats[x] * v) for x in Gr.all]) \
                    .transpose() if K.dim else zero_matrix(F, 0, Gr.n)
                X = direct_sum(X, Fr)
                E = E.augment(f)
            self.X.append(X)
            # the map to X_(n-1) (or to M) is Kb E
            self.d.append(E if Kb is None else sp(Kb) * E)
            Bk = kernel_cols(E)
            K = submodule(X, Bk)
            Kb = Bk

    def check_resolution(self):
        """Exact, augmented onto M, each piece H-split."""
        ok = self.d[0].rank() == self.M.dim
        for n in range(1, len(self.X)):
            ok = ok and (self.d[n - 1] * self.d[n]).is_zero() and \
                self.d[n].rank() == self.X[n - 1].dim - self.d[n - 1].rank()
        return ok

    def hom_complex(self, Mp, nmax):
        return hom_complex(self, Mp, nmax)


def coords(basis, X):
    """Coordinates of X in the basis (list of matrices)."""
    F = X.base_ring()
    A = dmatrix(F, [vector(F, b.list()) for b in basis])
    return A.solve_left(vector(F, X.list()))


def map_matrix(src_basis, tgt_basis, fn, F):
    """Matrix (columns = coordinates) of a linear map between spaces of
    maps given by bases."""
    if not src_basis or not tgt_basis:
        return dmatrix(F, len(tgt_basis), len(src_basis))
    A = dmatrix(F, [vector(F, b.list()) for b in tgt_basis])
    cols = [A.solve_left(vector(F, fn(b).list())) for b in src_basis]
    return dmatrix(F, cols).transpose()


def hom_complex(X, Mp, nmax):
    """Bases of Hom_G(X_n, M') and the coboundaries delta^n (composition
    with d_(n+1)) as matrices."""
    bases = [hom_space(Xn, Mp) for Xn in X.X[:nmax + 2]]
    deltas = [map_matrix(bases[n], bases[n + 1],
                         lambda b, n=n: sp(b) * sp(X.d[n + 1]), Mp.F)
              for n in range(nmax + 1)]
    return bases, deltas


def cohom_dims(deltas):
    out = []
    for n in range(len(deltas)):
        prev = deltas[n - 1].rank() if n else 0
        out.append(deltas[n].ncols() - deltas[n].rank() - prev)
    return out


def map_rank_on_cohomology(f, dA_prev, dA, dB_prev, dB):
    """Rank of the map H(A) -> H(B) induced by the cochain map f (matrix,
    coordinates) in one degree; d*_prev are the incoming coboundaries."""
    F = f.base_ring()
    ZA = dA.right_kernel()
    BB = dB_prev.column_space() if dB_prev is not None else \
        VectorSpace(F, f.nrows()).subspace([])
    img = BB + VectorSpace(F, f.nrows()).subspace(
        [f * z for z in ZA.basis()])
    return img.dimension() - BB.dimension()


def les_ranks(dA, dB, dC, f, g, top):
    """For a degreewise exact sequence 0 -> A -> B -> C -> 0 of cochain
    complexes (coboundaries dX[n] : X^n -> X^(n+1) as matrices, cochain maps
    f[n], g[n]), check exactness of the long exact cohomology sequence up to
    H^top: returns True/False.  The connecting map is the snake lemma
    construction."""
    F = f[0].base_ring()
    hA, hB, hC = cohom_dims(dA), cohom_dims(dB), cohom_dims(dC)
    ok = True
    for n in range(top + 1):
        ok = ok and (sp(g[n]) * sp(f[n])).is_zero()
        ok = ok and f[n].rank() == f[n].ncols() and \
            g[n].rank() == g[n].nrows() and \
            f[n].rank() + g[n].rank() == g[n].ncols()
    r1, r2, r3 = [], [], []
    for n in range(top + 1):
        pa = dA[n - 1] if n else None
        pb = dB[n - 1] if n else None
        pc = dC[n - 1] if n else None
        r1.append(map_rank_on_cohomology(f[n], pa, dA[n], pb, dB[n]))
        r2.append(map_rank_on_cohomology(g[n], pb, dB[n], pc, dC[n]))
        # connecting map H^n(C) -> H^(n+1)(A)
        imgs = []
        for c in dC[n].right_kernel().basis():
            b = g[n].solve_right(c)
            db = dB[n] * b
            imgs.append(f[n + 1].solve_right(db))
        BA = dA[n].column_space()
        img = BA + VectorSpace(F, dA[n].nrows()).subspace(imgs)
        r3.append(img.dimension() - BA.dimension())
    ok = ok and r1[0] == hA[0]
    for n in range(top + 1):
        ok = ok and hB[n] == r1[n] + r2[n] and hC[n] == r2[n] + r3[n]
        if n < top:
            ok = ok and hA[n + 1] == r3[n] + r1[n + 1]
    return ok, (hA[:top + 1], hB[:top + 1], hC[:top + 1])


def chain_lift(X, Y, phi, nmax):
    """A chain map f_n : X_n -> Y_n (G-maps) over phi : M -> M' between
    relative resolutions (Theorem 3.9.3), or None."""
    fs = []
    for n in range(nmax + 1):
        basis = hom_space(X.X[n], Y.X[n])
        if n == 0:
            rhs = sp(phi) * sp(X.d[0])
        else:
            rhs = sp(fs[-1]) * sp(X.d[n])
        f = solve_hom(basis, lambda b, n=n: sp(Y.d[n]) * sp(b), rhs)
        if f is None:
            return None
        fs.append(f)
    return fs


def homotopy(X, Y, f, f2, nmax):
    """h_n : X_n -> Y_(n+1) with f_n - f'_n = d'_(n+1) h_n + h_(n-1) d_n."""
    hs = []
    for n in range(nmax):
        basis = hom_space(X.X[n], Y.X[n + 1])
        rhs = sp(f[n] - f2[n])
        if n:
            rhs = rhs - sp(hs[-1]) * sp(X.d[n])
        h = solve_hom(basis, lambda b, n=n: sp(Y.d[n + 1]) * sp(b), rhs)
        if h is None:
            return None
        hs.append(h)
    return hs


# ===========================================================================
# 3.9 Relative cohomology
# ===========================================================================


def section_3_9():
    # (G, q, generators of H, n_max, n_max for the comparison theorem)
    cases = [('C4', 2, ['(1,3)(2,4)'], 5, 3),
             ('S3', 2, ['(1,2,3)'], 5, 3),
             ('S3', 3, ['(1,2)'], 3, 2),
             ('D8', 2, ['(1,3)(2,4)', '(1,3)'], 4, 3),
             ('D8', 2, ['(1,2,3,4)'], 4, 3),
             ('D8', 2, ['(1,3)'], 2, 1),
             ('A4', 2, ['(1,2)(3,4)', '(1,3)(2,4)'], 3, 2),
             ('A4', 3, ['(1,2)(3,4)', '(1,3)(2,4)'], 2, 1),
             ('C2xC2', 2, ['(1,2)'], 5, 3),
             ('C9', 3, ['(1,4,7)(2,5,8)(3,6,9)'], 4, 2)]
    rel = {}
    for name, q, Hgens, N, N2 in cases:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hgens])
        M = trivial(Gr, F)
        label = '%s, |H| = %d, GF(%d)' % (name, len(H), q)
        # the natural surjection M down_H up^G -> M splits on H (p. 81)
        X0, E = epsilon(M, H)
        check(h_section(X0, M, E, H) is not None, 'p. 81: M down_H up^G -> '
              'M splits on restriction to H (%s)' % label)
        X = RelRes(M, H, N + 1)
        check(X.check_resolution(), 'Def 3.9.2 (p. 81): relatively '
              'H-projective resolution (exact, onto M) (%s)' % label)
        check(higman_theta(Gr, H, X.X[1]) is not None, 'Def 3.9.2 (ii) '
              '(p. 81): X_1 = K down_H up^G is projective relative to H '
              '(Higman) (%s)' % label)
        # pieces split on H: X_n -> Im(d_n) has an H-section
        ok = True
        for n in range(1, N + 1):
            Bim = colspace_basis(X.d[n])
            Kn = submodule(X.X[n - 1], Bim)
            e = Bim.solve_right(X.d[n].dense_matrix()) if q == 2 else \
                sp(Bim).solve_right(X.d[n])
            ok = ok and h_section(X.X[n], Kn, e, H) is not None
        check(ok, 'Def 3.9.2 (iii) (p. 81): each 0 -> X_(n+1)/Ker -> X_n '
              '-> Im -> 0 splits on H (%s)' % label)
        bases, deltas = X.hom_complex(M, N)
        hrel = cohom_dims(deltas)
        rel[label] = hrel
        # independence of the resolution: X_0 with a free summand added
        Y = RelRes(M, H, N2 + 1, extra=1)
        check(Y.check_resolution(), 'Def 3.9.2: second relatively '
              'H-projective resolution (%s)' % label)
        hY = cohom_dims(Y.hom_complex(M, N2)[1])
        check(hY == hrel[:N2 + 1], 'p. 81: Ext^n_(G,H)(k, k) independent of '
              'the relatively H-projective resolution, n <= %d (%s: %s)'
              % (N2, label, hY))
        # H^0(G, H, k) = Hom_G(k, k) (corrected display: Hom(X_0, M'))
        check(hrel[0] == 1, 'p. 81 (corrected display): H^0 of '
              'Hom_RG(X, M\') is Hom_RG(M, M\') (%s)' % label)
        # Theorem 3.9.3: chain maps over 1_k and homotopies
        f = chain_lift(X, Y, identity_matrix(F, 1), N2)
        check(f is not None, 'Thm 3.9.3 (p. 81): the identity of k '
              'extends to a chain map X -> Y (%s)' % label)
        # a second lift: f + d' h_0 in degree 0, f + h_0 d in degree 1
        h0 = random_hom(X.X[0], Y.X[1])
        f2 = [f[0] + sp(Y.d[1]) * sp(h0)]
        if N2 >= 1:
            f2.append(f[1] + sp(h0) * sp(X.d[1]))
        f2 += f[2:]
        check(all((sp(Y.d[n]) * sp(f2[n]) - sp(f2[n - 1]) * sp(X.d[n]))
                  .is_zero() for n in range(1, N2 + 1)) and
              (sp(Y.d[0]) * sp(f2[0]) - sp(X.d[0])).is_zero(),
              'Thm 3.9.3: a second chain map f\' over 1_k (%s)' % label)
        hs = homotopy(X, Y, f, f2, N2)
        check(hs is not None, 'Thm 3.9.3 (p. 81, corrected): f_n - f\'_n = '
              'd\'_(n+1) h_n + h_(n-1) d_n with h_n : X_n -> Y_(n+1), '
              'n < %d (%s)' % (N2, label))
        refuted(X.X[1].dim == Y.X[1].dim, 'Thm 3.9.3 (p. 81, printed): '
                'd_(n+1) h_n (d_(n+1) : X_(n+1) -> X_n after h_n : X_n -> '
                'Y_(n+1)) is a composite (%s)' % label)
    # the natural map Ext^n_(G,H) -> Ext^n_RG need not be injective (p. 82):
    # C4 relative to C2 over GF(2), degree 2.
    Gr, F = group('C4'), GF(2)
    H = Gr.closure([Gr.el('(1,3)(2,4)')])
    k = trivial(Gr, F)
    X = RelRes(k, H, 4)
    nat = natural_map_ranks(X, k, 3)
    hr = cohom_dims(X.hom_complex(k, 3)[1])
    check(hr == [1, 1, 1, 1] and nat == [1, 1, 0, 0],
          'p. 82: Ext^n_(C4,C2)(k, k) -> Ext^n_(kC4)(k, k) has ranks 1, 1, '
          '0, 0 (n <= 3): not injective in degree 2')
    for name, q, Hg in [('D8', 2, ['(1,3)']), ('S3', 2, ['(1,2,3)']),
                        ('A4', 2, ['(1,2)(3,4)', '(1,3)(2,4)'])]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        k = trivial(Gr, F)
        X = RelRes(k, H, 3)
        nat = natural_map_ranks(X, k, 2)
        hr = cohom_dims(X.hom_complex(k, 2)[1])
        check(all(a <= b for a, b in zip(nat, hr)) and nat[0] == 1,
              'p. 82: the natural map Ext_(G,H) -> Ext_RG (%s, |H| = %d, '
              'ranks %s of %s)' % (name, len(H), nat, hr))

    # Lemma 3.9.1 (relative Schanuel): 0 -> M_i -> X_i -> M -> 0 H-split,
    # X_i projective relative to H => M_1 + X_2 ~ M_2 + X_1.
    for name, q, Hg, mod in [('D8', 2, ['(1,3)'], 'k'),
                             ('S4', 2, ['(1,2,3,4)', '(1,3)'], 'k'),
                             ('S4', 3, ['(1,2)', '(3,4)'], 'sign'),
                             ('A4', 2, ['(1,2,3)'], 'k')]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        M = trivial(Gr, F) if mod == 'k' else sign(Gr, F)
        X1, E1 = epsilon(M, H)
        X2 = direct_sum(X1, X1)
        E2 = E1.augment(sp(E1) * sp(random_hom(X1, X1)))
        X3 = direct_sum(X1, regular(Gr, F))
        v = vector(F, [1] * M.dim)
        E3 = E1.augment(matrix(F, [list(M.mats[x] * v)
                                   for x in Gr.all]).transpose())
        mods = []
        for X, E in [(X1, E1), (X2, E2), (X3, E3)]:
            check(h_section(X, M, E, H) is not None and E.rank() == M.dim,
                  'Lemma 3.9.1: H-split surjection (%s)' % name)
            mods.append((submodule(X, kernel_cols(E)), X))
        for (Ma, Xa), (Mb, Xb) in [(mods[0], mods[1]), (mods[0], mods[2]),
                                   (mods[1], mods[2])]:
            check(isomorphic(direct_sum(Ma, Xb), direct_sum(Mb, Xa)),
                  'Lemma 3.9.1 (p. 81): M_1 + X_2 ~ M_2 + X_1 (%s, |H| = '
                  '%d, M = %s, dims %d, %d)' % (name, len(H), mod, Ma.dim,
                                                Mb.dim))

    # Lemma 3.9.4 (relative horseshoe) and the two long exact sequences
    # (p. 83) for H-split 0 -> M' -> M -> M'' -> 0.
    for name, q, Hg, kind, N in [('C2xC2', 2, ['(1,2)'], 'perm', 3),
                                 ('D8', 2, ['(1,2)(3,4)', '(1,3)(2,4)'],
                                  'perm', 3),
                                 ('D8', 2, ['(1,2,3,4)'], 'res', 3),
                                 ('S3', 3, ['(1,2)'], 'res', 2)]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        k = trivial(Gr, F)
        label = '%s, |H| = %d, GF(%d)' % (name, len(H), q)
        if kind == 'perm':
            # 0 -> k -> k[G/H] -> k -> 0, inflated from G/H
            M = perm_module(Gr, F, H)
            i = matrix(F, [[1]] * M.dim)
            pi = matrix(F, [[1] * M.dim])
            Mp, Mpp = k, k
        else:
            # 0 -> K -> k down_H up^G -> k -> 0
            M, pi = epsilon(k, H)
            i = kernel_cols(pi)
            Mp, Mpp = submodule(M, i), k
        check(is_hom(Mp, M, i) and is_hom(M, Mpp, pi) and
              (sp(pi) * sp(i)).is_zero() and i.rank() == Mp.dim and
              pi.rank() == Mpp.dim and Mp.dim + Mpp.dim == M.dim and
              h_section(M, Mpp, pi, H) is not None,
              'p. 82: an H-split short exact sequence (%s)' % label)
        X1, X2 = RelRes(Mp, H, N + 1), RelRes(Mpp, H, N + 1)
        X = horseshoe(M, i, pi, X1, X2, N + 1)
        check(X is not None and X.check_resolution(), 'Lemma 3.9.4 (p. 82):'
              ' the relative horseshoe: X1 + X2 resolves M (%s)' % label)
        ok = True
        for n in range(1, N + 2):
            Bim = colspace_basis(X.d[n])
            Kn = submodule(X.X[n - 1], Bim)
            e = sp(Bim).solve_right(sp(X.d[n])) if q != 2 else \
                Bim.solve_right(X.d[n].dense_matrix())
            ok = ok and h_section(X.X[n], Kn, e, H) is not None
        check(ok, 'Lemma 3.9.4: the horseshoe resolution is H-split (%s)'
              % label)
        for M0 in [k] + ([sign(Gr, F)] if name == 'S3' else []):
            # first sequence: Hom(-, M0) of the horseshoe
            bA, dA = hom_complex(X2, M0, N)
            bB, dB = hom_complex(X, M0, N)
            bC, dC = hom_complex(X1, M0, N)
            # f : precompose with X -> X2, g : restrict to X1
            f = [map_matrix(bA[n], bB[n], lambda b, n=n: zero_matrix(
                F, M0.dim, X1.X[n].dim).augment(b), F)
                for n in range(N + 1)]
            g = [map_matrix(bB[n], bC[n], lambda b, n=n:
                            b.matrix_from_columns(range(X1.X[n].dim)), F)
                 for n in range(N + 1)]
            ok, dims = les_ranks(dA, dB, dC, f, g, N - 1)
            check(ok, 'p. 83: the long exact sequence 0 -> Hom(M\'\', M0) '
                  '-> ... -> Ext^n_(G,H)(M, M0) -> Ext^n_(G,H)(M\', M0) -> '
                  'Ext^(n+1)_(G,H)(M\'\', M0) is exact, n <= %d (%s; dims '
                  '%s)' % (N - 1, label, dims))
        # second sequence: Hom(Z, -) for a relative resolution Z of M0 = k
        Z = RelRes(k, H, N + 1)
        bA, dA = hom_complex(Z, Mp, N)
        bB, dB = hom_complex(Z, M, N)
        bC, dC = hom_complex(Z, Mpp, N)
        f = [map_matrix(bA[n], bB[n], lambda b: sp(i) * sp(b), F)
             for n in range(N + 1)]
        g = [map_matrix(bB[n], bC[n], lambda b: sp(pi) * sp(b), F)
             for n in range(N + 1)]
        ok, dims = les_ranks(dA, dB, dC, f, g, N - 1)
        check(ok, 'p. 83: the long exact sequence 0 -> Hom(M0, M\') -> ... '
              '-> Ext^n_(G,H)(M0, M\'\') -> Ext^(n+1)_(G,H)(M0, M\') is '
              'exact, n <= %d (%s; dims %s)' % (N - 1, label, dims))

    # H = 1: relative cohomology is ordinary cohomology
    for name, q, N in [('C2', 2, 5), ('C4', 2, 3), ('C3', 3, 4),
                       ('S3', 3, 1)]:
        Gr, F = group(name), GF(q)
        M = trivial(Gr, F)
        X = RelRes(M, (0,), N + 1)
        h = cohom_dims(X.hom_complex(M, N)[1])
        check(h == ext_dims(M, M, N), 'p. 81: Ext_(G,1) = Ext_RG over a '
              'field (%s, GF(%d), n <= %d)' % (name, q, N))
    # H normal: X_n = k[G/H], H^n(G, H, k) = H^n(G/H, k); values
    check(rel['C4, |H| = 2, GF(2)'] == [1] * 6 and
          rel['C2xC2, |H| = 2, GF(2)'] == [1] * 6 and
          rel['D8, |H| = 4, GF(2)'] == [1] * 5 and
          rel['S3, |H| = 3, GF(2)'] == [1] * 6 and
          rel['A4, |H| = 4, GF(2)'] == [1, 0, 0, 0] and
          rel['A4, |H| = 4, GF(3)'] == [1, 1, 1],
          'H normal: H^n(G, H, k) = H^n(G/H, k) (C2: k; C3 over GF(2): 0; '
          'C3 over GF(3): k), relative resolution inflated from G/H')
    return rel


class Cx:
    """A complex X_n (modules) with d_n : X_n -> X_(n-1), d_0 : X_0 -> M."""

    def __init__(self, X, d, M):
        self.X, self.d, self.M = X, d, M

    def check_resolution(self):
        ok = self.d[0].rank() == self.M.dim
        for n in range(1, len(self.X)):
            ok = ok and (sp(self.d[n - 1]) * sp(self.d[n])).is_zero() and \
                self.d[n].rank() == self.X[n - 1].dim - self.d[n - 1].rank()
        return ok


def horseshoe(M, i, pi, X1, X2, N):
    """Lemma 3.9.4: given 0 -> M' -i-> M -pi-> M'' -> 0 (H-split) and
    relatively H-projective resolutions X1 of M', X2 of M'', the resolution
    X_n = X1_n + X2_n of M with d_n = [[d1_n, l_n], [0, d2_n]]; None if a
    lift l_n does not exist."""
    F = M.F
    lam = []
    for n in range(N + 1):
        if n == 0:
            # l_0 : X2_0 -> M with pi l_0 = eps2
            l = solve_hom(hom_space(X2.X[0], M), lambda b: sp(pi) * sp(b),
                          sp(X2.d[0]))
        elif n == 1:
            # i eps1 l_1 = - l_0 d2_1
            l = solve_hom(hom_space(X2.X[1], X1.X[0]),
                          lambda b: sp(i) * sp(X1.d[0]) * sp(b),
                          -sp(lam[0]) * sp(X2.d[1]))
        else:
            l = solve_hom(hom_space(X2.X[n], X1.X[n - 1]),
                          lambda b, n=n: sp(X1.d[n - 1]) * sp(b),
                          -sp(lam[n - 1]) * sp(X2.d[n]))
        if l is None:
            return None
        lam.append(l)
    Xs, ds = [], []
    for n in range(N + 1):
        Xs.append(direct_sum(X1.X[n], X2.X[n]))
        if n == 0:
            ds.append(block_matrix([[sp(i) * sp(X1.d[0]), sp(lam[0])]],
                                   subdivide=False))
        else:
            Z = zero_matrix(F, X2.X[n - 1].dim, X1.X[n].dim)
            ds.append(block_matrix([[sp(X1.d[n]), sp(lam[n])],
                                    [Z, sp(X2.d[n])]], subdivide=False))
    return Cx(Xs, ds, M)


def natural_map_ranks(X, Mp, N):
    """Ranks of Ext^n_(G,H)(M, M') -> Ext^n_RG(M, M'), n <= N, induced by a
    chain map from a free resolution P of M to X."""
    M = X.M
    Gr, F = M.Gr, M.F
    P = Resolution(M, N + 1)
    fs = []           # f_n as the list of images v_j of the generators e_j
    for n in range(N + 1):
        vs = []
        for j in range(P.ranks[n]):
            if n == 0:
                w = M.mats[0] * P.imgs[0][j]
            else:
                prev = fs[-1]
                w = vector(F, X.X[n - 1].dim)
                v = P.imgs[n][j]
                for i in range(P.ranks[n - 1]):
                    for x in Gr.all:
                        c = v[i * Gr.n + x]
                        if c:
                            w += c * (X.X[n - 1].mats[x] * prev[i])
            vs.append(X.d[n].dense_matrix().solve_right(w)
                      if F.characteristic() == 2 else
                      sp(X.d[n]).solve_right(w))
        fs.append(vs)
    bases, deltas = hom_complex(X, Mp, N)
    out = []
    for n in range(N + 1):
        Zrel = deltas[n].right_kernel().basis()
        imgs = []
        for z in Zrel:
            phi = sum((c * b for c, b in zip(z, bases[n])),
                      zero_matrix(F, Mp.dim, X.X[n].dim))
            imgs.append(vector(F, sum((list(phi * v) for v in fs[n]), [])))
        Bd = P.coboundary(n - 1, Mp).dense_matrix().column_space() if n \
            else VectorSpace(F, Mp.dim * P.ranks[n]).subspace([])
        img = Bd + VectorSpace(F, Mp.dim * P.ranks[n]).subspace(imgs)
        out.append(img.dimension() - Bd.dimension())
    return out


# ===========================================================================
# Vertices, sources, Green correspondence: helpers
# ===========================================================================


def subgroup_classes(Gr, A):
    """Conjugacy classes (under A) of subgroups of A: [(rep, members)]."""
    out = []
    for c in gap_subgroup(Gr, A).ConjugacyClassesSubgroups():
        mem = [from_gap_subgroup(Gr, K) for K in c.AsList()]
        out.append((from_gap_subgroup(Gr, c.Representative()), mem))
    return out


def sylow_in(Gr, A, p):
    return from_gap_subgroup(Gr, gap_subgroup(Gr, A).SylowSubgroup(p))


def projective_in(M, p):
    """M (a module for M.H) is projective iff free on a Sylow p-subgroup."""
    P = sylow_in(M.Gr, M.H, p)
    if len(P) == 1:
        return True
    Nm = sum(sp(M.mats[x]) for x in P)
    return M.dim % len(P) == 0 and Nm.rank() == M.dim // len(P)


def rel_projective(M, D, p):
    """M projective relative to D <= M.H (Higman's criterion)."""
    if len(D) == 1:
        return projective_in(M, p)
    if len(D) == len(M.H):
        return True
    return higman_theta(M.Gr, D, M, M.H) is not None


def to_mod(Gr, F, X, A):
    return gap_mats_to_mod(Gr, F, X, A)


def indecomposable_summands(M):
    """[(Mod, multiplicity)] of the indecomposable summands of M."""
    return [(to_mod(M.Gr, M.F, X, M.H), k) for X, d, k in summand_classes(M)]


def add_new(lst, M):
    if not any(isomorphic(M, N) for N in lst):
        lst.append(M)


def vertex_info(M, p, classes=None):
    """The A-classes of subgroups D with M relatively D-projective and the
    minimal ones (A = M.H)."""
    Gr = M.Gr
    classes = subgroup_classes(Gr, M.H) if classes is None else classes
    rp = [rel_projective(M, rep, p) for rep, mem in classes]
    minimal = []
    for i, (rep, mem) in enumerate(classes):
        if not rp[i]:
            continue
        if not any(rp[j] and len(classes[j][0]) < len(rep) and
                   any(set(m) <= set(rep) for m in classes[j][1])
                   for j in range(len(classes))):
            minimal.append(i)
    # relative projectivity is inherited by overgroups (consistency)
    mono = all(rp[i] for i, (rep, mem) in enumerate(classes)
               if any(rp[j] and any(set(m) <= set(rep)
                                    for m in classes[j][1])
                      for j in range(len(classes))))
    return classes, rp, minimal, mono


def maximal_subgroups(Gr, D):
    return [from_gap_subgroup(Gr, K)
            for K in gap_subgroup(Gr, D).MaximalSubgroups()] if len(D) > 1 \
        else []


def has_vertex(M, D, p):
    """Vertex of the indecomposable M is (conjugate to) the p-group D."""
    return rel_projective(M, D, p) and not any(
        rel_projective(M, E, p) for E in maximal_subgroups(M.Gr, D))


def sources(M, D):
    """Indecomposable summands S of M down_D with M | S up^(M.H)."""
    out = []
    for S, k in indecomposable_summands(restrict(M, D)):
        if is_summand(M, induce(S, M.H)):
            out.append(S)
    return out


def trivial_source(M, D):
    """M (vertex D) has the trivial module as a source."""
    kD = trivial(M.Gr, M.F, D)
    return is_summand(M, induce(kD, M.H)) and \
        is_summand(kD, restrict(M, D))


def cyclic_generator(Gr, D):
    """An element generating D, or None if D is not cyclic."""
    for x in D:
        if Gr.order_of(x) == len(D):
            return x
    return None


def jordan_on(Gr, F, c, a, D):
    """The Jordan block of size a for the cyclic group D = <c>."""
    J = identity_matrix(F, a)
    for i in range(a - 1):
        J[i + 1, i] = 1
    return from_gens(Gr, F, a, {c: J}, D)


def aug_kernel(Gr, F, D):
    """Omega(k) for D: the augmentation ideal of F D."""
    R = regular(Gr, F, D)
    B = kernel_cols(matrix(F, [[1] * R.dim]))
    return submodule(R, B)


def group_modules(Gr, F, p, extra=()):
    """Indecomposable F G-modules: summands of the transitive permutation
    modules (except the regular one when it is large) and of the extra
    modules, up to isomorphism; [(Mod, from_perm)]."""
    perm, other = [], []
    for rep, mem in subgroup_classes(Gr, Gr.all):
        if len(rep) == 1 and Gr.n > 24:
            continue
        for S, k in indecomposable_summands(perm_module(Gr, F, rep)):
            add_new(perm, S)
    for X in extra:
        for S, k in indecomposable_summands(X):
            if not any(isomorphic(S, N) for N in perm):
                add_new(other, S)
    return perm, other


# ===========================================================================
# 3.10 Vertices and sources, 3.11 Trivial source modules
# ===========================================================================


def section_3_10_11():
    stats = {}
    cases = [('S3', 2, 2), ('S3', 3, 3), ('C4', 2, 2), ('C2xC2', 2, 2),
             ('D8', 2, 2), ('Q8', 2, 2), ('A4', 4, 2), ('A4', 3, 3),
             ('S4', 2, 2), ('S4', 3, 3), ('C3:C4', 3, 3), ('A5', 2, 2),
             ('A5', 3, 3), ('A5', 5, 5)]
    for name, q, p in cases:
        Gr, F = group(name), GF(q)
        k = trivial(Gr, F)
        extra = []
        if Gr.n <= 24:
            R = Resolution(k, 2)
            extra += [R.omega(1), R.omega(2)]
        if name == 'C4':
            extra.append(jordan_block_module(Gr, F, 3))
        if name in ('D8', 'S4', 'A4', 'A5'):
            D = sylow(Gr, p)
            extra.append(induce(aug_kernel(Gr, F, D)))
        perm, other = group_modules(Gr, F, p, extra)
        classes = subgroup_classes(Gr, Gr.all)
        label = '%s, GF(%d)' % (name, q)
        nv = 0
        for M in perm + other:
            cl, rp, minimal, mono = vertex_info(M, p, classes)
            check(mono, 'relative projectivity passes to overgroups (%s, '
                  'dim %d)' % (label, M.dim))
            check(len(minimal) == 1, 'Prop 3.10.2 (i) (p. 83): the vertices '
                  'of M form one conjugacy class (%s, dim %d)'
                  % (label, M.dim))
            D = cl[minimal[0]][0]
            check(is_p_power(len(D), p), 'Prop 3.10.2 (iii) (p. 83): the '
                  'vertex is a p-subgroup (%s, dim %d, |D| = %d)'
                  % (label, M.dim, len(D)))
            S = sources(M, D)
            check(len(S) >= 1, 'Def 3.10.1 (p. 83): M has a source on its '
                  'vertex (%s, dim %d)' % (label, M.dim))
            ND = normalizer(Gr, D)
            ok = all(any(isomorphic(S[0], conjugate(T, g)) for g in ND)
                     for T in S)
            check(ok, 'Prop 3.10.2 (ii) (p. 83): the sources are conjugate '
                  'under N_G(D) (%s, dim %d, %d sources)'
                  % (label, M.dim, len(S)))
            ts = trivial_source(M, D)
            # (the regular module was skipped for |G| > 24: its summands
            # are the projective modules)
            insum = M in perm or (Gr.n > 24 and projective_in(M, p))
            check(ts == insum, 'Lemma 3.11.2 (p. 84): M has trivial source '
                  'iff it is a summand of a permutation module (%s, dim %d,'
                  ' %s)' % (label, M.dim, ts))
            nv += 1
        stats[label] = (len(perm), len(other))
    # the Mackey decompositions in the proof of Proposition 3.10.2 (p. 83),
    # with the printed indexing: (i) M down_H up^G down_K up^G ~
    # sum_(HgK) M down_(H cap gK) up^G; (ii) M_0 up^G down_D ~
    # sum_(DgD) gM_0 down_(D cap gD) up^D
    for name, q, Hg, Kg in [('S4', 2, ['(1,2,3,4)', '(1,3)'], ['(1,2,3)']),
                            ('S4', 3, ['(1,2)', '(3,4)'], ['(1,2,3)',
                                                           '(1,2)']),
                            ('A5', 2, ['(1,2)(3,4)', '(1,3)(2,4)'],
                             ['(1,2,3)', '(1,2)(4,5)']),
                            ('A4', 3, ['(1,2,3)'], ['(1,2)(3,4)'])]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        K = Gr.closure([Gr.el(s) for s in Kg])
        k = trivial(Gr, F)
        for M in [k, perm_module(Gr, F, K)]:
            if M.dim * (Gr.n // len(H)) * (Gr.n // len(K)) > 72:
                continue
            lhs = induce(restrict(induce(restrict(M, H)), K))
            rhs = direct_sum(*[induce(restrict(M, Gr.intersect(
                H, Gr.conj_subgroup(g, K)))) for g in Gr.double_cosets(H, K)])
            check(isomorphic(lhs, rhs), 'Prop 3.10.2 (i), proof (p. 83): '
                  'M down_H up^G down_K up^G ~ sum_(HgK) M down_(H cap gK) '
                  'up^G, as printed (%s, |H| = %d, |K| = %d, dim M = %d)'
                  % (name, len(H), len(K), M.dim))
        D = H
        for M0 in [trivial(Gr, F, D)] + [S for S, k_ in
                                         indecomposable_summands(
                                             regular(Gr, F, D))][:2]:
            lhs = restrict(induce(M0), D)
            rhs = direct_sum(*[induce(restrict(conjugate(M0, g),
                                               Gr.intersect(
                                                   D, Gr.conj_subgroup(g, D))),
                                      D) for g in Gr.double_cosets(D, D)])
            check(isomorphic(lhs, rhs), 'Prop 3.10.2 (ii), proof (p. 83): '
                  'M_0 up^G down_D ~ sum_(DgD) gM_0 down_(D cap gD) up^D, as '
                  'printed (%s, |D| = %d, dim M_0 = %d)'
                  % (name, len(D), M0.dim))
    return stats


def orbital_maps(Gr, H1, H2):
    """The 0/1 matrices of the G-orbits on G/H2 x G/H1: a ZZ-basis of
    Hom_ZG(ZZ[G/H1], ZZ[G/H2])."""
    c1, w1 = Gr.left_cosets(H1)
    c2, w2 = Gr.left_cosets(H2)
    seen, mats = set(), []
    for a in range(len(c2)):
        for b in range(len(c1)):
            if (a, b) in seen:
                continue
            A = dmatrix(ZZ, len(c2), len(c1))
            for g in Gr.all:
                x = w2[Gr.mul[g][c2[a]]][0]
                y = w1[Gr.mul[g][c1[b]]][0]
                seen.add((x, y))
                A[x, y] = 1
            mats.append(A)
    return mats


def section_3_11():
    # Proof of Lemma 3.11.2 (p. 84): R_H up^G down_D, by the Mackey formula
    # (Theorem 3.3.4), is the sum over the double cosets D g H of
    # R_(D cap gH) up^D.  The printed index H g D does not determine the
    # summand: g and g' = (12)(1234) in the same double coset H g D give
    # D cap gH of orders 1 and 2 (S4, H = <(12)>, D = D8).
    Gr = group('S4')
    H = Gr.closure([Gr.el('(1,2)')])
    D = Gr.closure([Gr.el('(1,2,3,4)'), Gr.el('(1,3)')])
    orders = set(len(Gr.intersect(D, Gr.conj_subgroup(Gr.m(h, 0, d), H)))
                 for h in H for d in D)
    refuted(len(orders) == 1, 'Lemma 3.11.2, proof (p. 84, printed): '
            'D cap gH depends only on the double coset H g D (H g D = H D '
            'in S4, H = <(12)>, D = D8: orders %s)' % sorted(orders))
    for name, q, Hg, Dg in [('S4', 2, ['(1,2)'], ['(1,2,3,4)', '(1,3)']),
                            ('S4', 3, ['(1,2)', '(3,4)'], ['(1,2,3)']),
                            ('S4', 2, ['(1,2,3)'], ['(1,2)', '(3,4)']),
                            ('A5', 2, ['(1,2,3)', '(1,2)(4,5)'],
                             ['(1,2)(3,4)', '(1,3)(2,4)']),
                            ('A5', 5, ['(1,2,3)', '(1,2)(4,5)'],
                             ['(1,2,3,4,5)'])]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        D = Gr.closure([Gr.el(s) for s in Dg])
        lhs = restrict(perm_module(Gr, F, H), D)
        rhs = direct_sum(*[perm_module(Gr, F, Gr.intersect(
            D, Gr.conj_subgroup(g, H)), D) for g in Gr.double_cosets(D, H)])
        check(isomorphic(lhs, rhs), 'Lemma 3.11.2, proof (p. 84, '
              'corrected): R_H up^G down_D ~ sum_(DgH) R_(D cap gH) up^D '
              '(%s, |H| = %d, |D| = %d)' % (name, len(H), len(D)))
        # the printed index set H g D with the same summand, for the
        # representatives found first: not even the dimension is right
        alt = sum(len(D) // len(Gr.intersect(D, Gr.conj_subgroup(g, H)))
                  for g in Gr.double_cosets(H, D))
        if name == 'S4' and q == 2 and len(H) == 2:
            refuted(alt == lhs.dim, 'Lemma 3.11.2, proof (p. 84, printed): '
                    'dim of sum_(HgD) R_(D cap gH) up^D for the first '
                    'representatives (%d) equals |G : H| = %d'
                    % (alt, lhs.dim))

    # Theorem 3.11.3 (Scott, p. 84): Hom_OG(M_1, M_2) and Hom_kG of the
    # reductions have the same rank, the number of double cosets
    # H_2 g H_1; the orbit matrices are a ZZ-basis reducing to a basis.
    nsc = 0
    for name, q in [('S3', 2), ('S3', 3), ('A4', 2), ('A4', 3), ('S4', 2),
                    ('S4', 3), ('D8', 2), ('A5', 2), ('A5', 5)]:
        Gr, F = group(name), GF(q)
        reps = [r for r, m in subgroup_classes(Gr, Gr.all)
                if Gr.n // len(r) <= 30]
        for H1 in reps:
            for H2 in reps:
                orb = orbital_maps(Gr, H1, H2)
                nd = len(Gr.double_cosets(H2, H1))
                M1, M2 = perm_module(Gr, F, H1), perm_module(Gr, F, H2)
                ok = len(orb) == nd and all(
                    is_hom(M1, M2, matrix(F, A)) for A in orb)
                hk = len(hom_space(M1, M2))
                red = dmatrix(F, [matrix(F, A).list() for A in orb]).rank()
                check(ok and hk == nd and red == nd,
                      'Thm 3.11.3 (p. 84): Hom over ZZ and over GF(%d) have '
                      'rank |H2\\G/H1| = %d, the orbit basis reduces to a '
                      'basis (%s, |H1| = %d, |H2| = %d)'
                      % (q, nd, name, len(H1), len(H2)))
                nsc += 1
    # every integral G-map is an integer combination of the orbit matrices
    Gr = group('S4')
    H1 = Gr.closure([Gr.el('(1,2,3)'), Gr.el('(1,2)')])
    H2 = Gr.closure([Gr.el('(1,2,3,4)'), Gr.el('(1,3)')])
    orb = orbital_maps(Gr, H1, H2)
    A = dmatrix(QQ, [B.list() for B in orb])
    M1, M2 = perm_module(Gr, QQ, H1), perm_module(Gr, QQ, H2)
    hq = hom_space(M1, M2)
    check(len(hq) == len(orb), 'Thm 3.11.3: Hom_QG(Q[G/H1], Q[G/H2]) has '
          'dimension |H2\\G/H1| (S4, H1 = S3, H2 = D8)')
    return nsc


def zmat(A, R):
    """An integral (0/1 or small) matrix over ZZ/n, sparse."""
    return dmatrix(R, A.nrows(), A.ncols(),
                   {(i, j): R(ZZ(A[i, j])) for i, j in A.nonzero_positions()},
                   sparse=True)


def section_3_11_lifts():
    # Corollary 3.11.4 (p. 84): idempotents of End_kG(k[G/H]) lift to
    # idempotents of End over ZZ/p^a (a = 4) in the span of the orbit
    # matrices (a trivial source summand of the lattice mod p^a); two lifts
    # are conjugate by a unit (uniqueness); homomorphisms lift.
    nl = 0
    for name, q, Hg in [('S3', 2, ['(1,2)']), ('S4', 2, ['(1,2,3)']),
                        ('S4', 3, ['(1,2,3,4)', '(1,3)']),
                        ('A4', 2, ['(1,2)(3,4)', '(1,3)(2,4)']),
                        ('A5', 2, ['(1,2,3)', '(1,2)(4,5)']),
                        ('A5', 3, ['(1,2)(3,4)', '(1,3)(2,4)'])]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        X = perm_module(Gr, F, H)
        orb = orbital_maps(Gr, H, H)
        R = IntegerModRing(q ** 4)
        O = dmatrix(F, [matrix(F, A).list() for A in orb])
        gens = [zmat(X.mats[g], R) for g in Gr.gens]
        dec = mtx('Indecomposition')(gap_module(X))
        # rows of B: bases of the summands (the MeatAxe acts on rows; the
        # projection v -> v E with E = B^-1 P B commutes with every g)
        B = dmatrix(F, [[F(c.sage(ring=F)) for c in row]
                        for x in dec for row in x[0]])
        Bi = B.inverse()
        start, lifts = 0, []
        for x in dec:
            dmx = int(libgap.Length(x[0]))
            P = dmatrix(F, X.dim, X.dim, sparse=True)
            for r in range(start, start + dmx):
                P[r, r] = 1
            start += dmx
            e = sp(Bi) * P.change_ring(F) * sp(B)
            c = O.solve_left(vector(F, e.list()))
            ehs = []
            for shift in (0, 1):
                # two integral starting points with the same reduction
                eh = sum((R(ZZ(ci) + shift * q) * zmat(A, R)
                          for ci, A in zip(c, orb)),
                         dmatrix(R, X.dim, X.dim, sparse=True))
                for _ in range(4):
                    eh = 3 * eh * eh - 2 * eh * eh * eh
                ehs.append(eh)
            e1, e2 = ehs
            ok = all(eh * eh == eh and eh.change_ring(F) == e and
                     all(eh * g == g * eh for g in gens) for eh in ehs)
            check(ok, 'Cor 3.11.4 (i) (p. 84): the idempotent of a summand '
                  'of k[G/H] lifts to an idempotent over ZZ/%d commuting '
                  'with G (%s, |H| = %d, summand of dim %d)'
                  % (q ** 4, name, len(H), dmx))
            # uniqueness: u = e2 e1 + (1 - e2)(1 - e1) is a unit with
            # u e1 = e2 u
            one = dmatrix(R, X.dim, X.dim, 1, sparse=True)
            u = e2 * e1 + (one - e2) * (one - e1)
            check(u * e1 == e2 * u and
                  u.change_ring(F).dense_matrix().is_invertible(),
                  'Cor 3.11.4 (i): two lifts are conjugate by a unit '
                  '(%s, |H| = %d, dim %d)' % (name, len(H), dmx))
            lifts.append((e, e1))
            nl += 1
        # (ii): a homomorphism between two summands lifts: e_2 phi e_1 with
        # phi an integral combination of orbit matrices
        if len(lifts) >= 2:
            (ea, Ea), (eb, Eb) = lifts[0], lifts[1]
            for A in orb:
                phi = sp(eb) * matrix(F, A) * sp(ea)
                c = O.solve_left(vector(F, phi.list()))
                Phi = sum((R(ZZ(ci)) * zmat(B2, R) for ci, B2 in
                           zip(c, orb)), dmatrix(R, X.dim, X.dim, sparse=True))
                lift = Eb * Phi * Ea
                check(lift.change_ring(F) == phi and
                      all(lift * g == g * lift for g in gens),
                      'Cor 3.11.4 (ii) (p. 84): a map between trivial source '
                      'summands lifts (%s, |H| = %d)' % (name, len(H)))
    return nl


# ===========================================================================
# 3.12 Green correspondence
# ===========================================================================


def calX_calY(Gr, D, H):
    """The maximal members D cap gD and H cap gD (g not in H) of the sets
    X and Y of p. 85 (every member is contained in one of them)."""
    Hs = set(H)
    X, Y = set(), set()
    for g in Gr.all:
        if g in Hs:
            continue
        gD = Gr.conj_subgroup(g, D)
        X.add(Gr.intersect(D, gD))
        Y.add(Gr.intersect(H, gD))
    return sorted(X, key=len), sorted(Y, key=len)


def proj_rel_some(M, Ls, p):
    return any(rel_projective(M, L, p) for L in Ls)


def split_summand(M, S):
    """An inclusion i : S -> M and projection q : M -> S with q i = 1,
    i q an idempotent of End(M) (S an indecomposable summand of M); or
    None."""
    F = M.F
    A = hom_space(S, M)
    Bq = hom_space(M, S)
    for a in A:
        for b in Bq:
            c = sp(b) * sp(a)
            if c.dense_matrix().is_invertible():
                ci = c.dense_matrix().inverse()
                return a, sp(ci) * sp(b)
    # random combinations
    for _ in range(40):
        a = random_hom(S, M)
        b = random_hom(M, S)
        c = (sp(b) * sp(a)).dense_matrix()
        if c.is_invertible():
            return a, sp(c.inverse()) * sp(b)
    return None


def green_case(Gr, F, p, D, H, Hmods, label):
    """Theorem 3.12.2 for the indecomposable R H-modules Hmods with vertex D;
    returns the Green correspondents."""
    Xs, Ys = calX_calY(Gr, D, H)
    out = []
    for M in Hmods:
        lab = '%s, dim M = %d' % (label, M.dim)
        check(has_vertex(M, D, p), 'Thm 3.12.2: M has vertex D (%s)' % lab)
        summ = indecomposable_summands(induce(M))
        withD = [(V, k) for V, k in summ if has_vertex(V, D, p)]
        rest = [V for V, k in summ if not has_vertex(V, D, p)]
        check(len(withD) == 1 and withD[0][1] == 1, 'Thm 3.12.2 (ii) '
              '(p. 86): M up^G has a unique summand g(M) with vertex D (%s)'
              % lab)
        check(all(proj_rel_some(V, Xs, p) for V in rest), 'Thm 3.12.2 (ii),'
              ' Lemma 3.12.1 (ii) (p. 85): the other summands of M up^G are '
              'projective relative to subgroups in X (%s)' % lab)
        V = withD[0][0]
        res = indecomposable_summands(restrict(V, H))
        withD2 = [(W, k) for W, k in res if has_vertex(W, D, p)]
        rest2 = [W for W, k in res if not has_vertex(W, D, p)]
        check(len(withD2) == 1 and withD2[0][1] == 1 and
              isomorphic(withD2[0][0], M), 'Thm 3.12.2 (i), (iii) (p. 86): '
              'g(M) down_H has a unique summand f(g(M)) with vertex D, and '
              'f(g(M)) ~ M (%s)' % lab)
        check(all(proj_rel_some(W, Ys, p) for W in rest2), 'Thm 3.12.2 (i) '
              '(p. 86): the other summands of g(M) down_H are projective '
              'relative to subgroups in Y (%s)' % lab)
        # Lemma 3.12.1 (i): M up^G down_H = M + M' with M' Y-projective
        res3 = indecomposable_summands(restrict(induce(M), H))
        mult = sum(k for W, k in res3 if isomorphic(W, M))
        check(mult >= 1 and all(proj_rel_some(W, Ys, p) for W, k in res3
                                if not isomorphic(W, M)) and
              sum(k for W, k in res3 if has_vertex(W, D, p)) == 1,
              'Lemma 3.12.1 (i) (p. 85): M up^G down_H = M + M\' with M\' '
              'projective relative to subgroups in Y (%s)' % lab)
        kD = trivial(Gr, F, D)
        check(trivial_source(M, D) == trivial_source(V, D), 'Thm 3.12.2 (iv)'
              ' (p. 86): f and g preserve trivial source (%s)' % lab)
        out.append((M, V))
    return out


def endo_quotient(Gr, V1, V2, A, Ls, ambient):
    """(V1, V2)^A and its subspace sum_L Tr_(L, A)((V1, V2)^L), as vector
    spaces of flattened matrices."""
    F = V1.F
    n = V1.dim * V2.dim
    full = VectorSpace(F, n).subspace(
        [vector(F, b.list()) for b in hom_space(restrict(V1, A),
                                                 restrict(V2, A))])
    gens = []
    for L in Ls:
        for b in hom_space(restrict(V1, L), restrict(V2, L)):
            gens.append(vector(F, tr(Gr, L, V1, V2, b, ambient).list()))
    return full, VectorSpace(F, n).subspace(gens)


def section_3_12():
    cases = [('S4', 2, 2, ['(1,2)'], []),
             ('S4', 2, 2, ['(1,2)'], ['(1,3)(2,4)']),
             ('S4', 2, 2, ['(1,2,3,4)'], []),
             ('S4', 2, 2, ['(1,2)', '(3,4)'], []),
             ('S4', 3, 3, ['(1,2,3)'], []),
             ('S3', 2, 2, ['(1,2)'], []),
             ('D8', 2, 2, ['(1,3)'], []),
             ('A4', 2, 2, ['(1,2)(3,4)'], []),
             ('A4', 3, 3, ['(1,2,3)'], []),
             ('A5', 2, 2, ['(1,2)(3,4)', '(1,3)(2,4)'], []),
             ('A5', 2, 2, ['(1,2)(3,4)'], []),
             ('A5', 3, 3, ['(1,2,3)'], []),
             ('A5', 5, 5, ['(1,2,3,4,5)'], []),
             ('GL32', 7, 7, ['(1,2,3,4,5,6,7)'], [])]
    ncorr = 0
    for name, q, p, Dg, Hextra in cases:
        Gr, F = group(name), GF(q)
        D = Gr.closure([Gr.el(s) for s in Dg])
        N = normalizer(Gr, D)
        H = Gr.closure(list(Gr.gens_of(N)) + [Gr.el(s) for s in Hextra])
        label = '%s, GF(%d), |D| = %d, |H| = %d' % (name, q, len(D), len(H))
        Xs, Ys = calX_calY(Gr, D, H)
        # X is contained in Y, and D is not in Y (p. 85)
        check(all(any(set(x) <= set(y) for y in Ys) for x in Xs) and
              not any(set(D) <= set(y) for y in Ys),
              'p. 85: X is contained in Y and D is not in Y (%s)' % label)
        # indecomposable R H-modules with vertex D: summands of S up^H
        Smods = [trivial(Gr, F, D)]
        c = cyclic_generator(Gr, D)
        if len(D) > 2 and c is not None:
            Smods += [jordan_on(Gr, F, c, a, D) for a in range(2, len(D))]
        elif len(D) == 4:
            Smods.append(aug_kernel(Gr, F, D))
        Hmods = []
        for S in Smods:
            for W, k in indecomposable_summands(induce(S, H)):
                if has_vertex(W, D, p):
                    add_new(Hmods, W)
        pairs = green_case(Gr, F, p, D, H, Hmods, label)
        ncorr += len(pairs)
        # trivial source modules with vertex D: equally many for G and H
        tG = [V for V, k in indecomposable_summands(
            induce(trivial(Gr, F, D))) if has_vertex(V, D, p)]
        tH = [M for M in Hmods if trivial_source(M, D)]
        check(len(tG) == len(tH) and all(any(isomorphic(V, V2) for M, V2 in
                                             pairs) for V in tG),
              'Thm 3.12.2 (iii), (iv) (p. 86): g is a bijection between the '
              '%d trivial source modules with vertex D (%s)'
              % (len(tH), label))
        # (v): Tr_(H,G) : (f V1, f V2)^(H,X) -> (V1, V2)^(G,X) is an
        # isomorphism, for pairs of correspondents
        for (M1, V1), (M2, V2) in list(itertools.product(pairs, pairs))[:4]:
            s1 = split_summand(restrict(V1, H), M1)
            s2 = split_summand(restrict(V2, H), M2)
            a1, b1 = s1
            a2, b2 = s2
            nn = V1.dim * V2.dim
            Vs = VectorSpace(F, nn)
            emb = lambda phi: sp(a2) * sp(phi) * sp(b1)
            A = Vs.subspace([vector(F, emb(b).list())
                             for b in hom_space(M1, M2)])
            AX = Vs.subspace([vector(F, emb(tr(Gr, L, M1, M2, b, H)).list())
                              for L in Xs for b in
                              hom_space(restrict(M1, L), restrict(M2, L))])
            B, BX = endo_quotient(Gr, V1, V2, Gr.all, Xs, Gr.all)
            TrA = Vs.subspace([vector(F, tr(Gr, H, V1, V2,
                                            matrix(F, V2.dim, V1.dim,
                                                   list(v))).list())
                               for v in A.basis()])
            TrAX = Vs.subspace([vector(F, tr(Gr, H, V1, V2,
                                             matrix(F, V2.dim, V1.dim,
                                                    list(v))).list())
                                for v in AX.basis()])
            check(TrA + BX == B and TrAX.is_subspace(BX) and
                  A.dimension() - AX.dimension() ==
                  B.dimension() - BX.dimension(),
                  'Thm 3.12.2 (v) (p. 86): Tr_(H,G) induces (f(V1), '
                  'f(V2))^(H,X) ~ (V1, V2)^(G,X) (%s, dims %d, %d; quotient '
                  '%d)' % (label, V1.dim, V2.dim,
                           B.dimension() - BX.dimension()))
        # Theorem 3.12.3 (Burry-Carlson-Puig) and its proof
        perm, other = group_modules(Gr, F, p)
        for V in perm + [V for M, V in pairs]:
            Ms = [W for W, k in indecomposable_summands(restrict(V, H))
                  if has_vertex(W, D, p)]
            if Ms:
                gM = [U for U, k in indecomposable_summands(induce(Ms[0]))
                      if has_vertex(U, D, p)]
                check(has_vertex(V, D, p) and len(gM) == 1 and
                      isomorphic(V, gM[0]), 'Thm 3.12.3 (p. 87): V down_H '
                      'has a summand M with vertex D => V has vertex D and '
                      'V ~ g(M) (%s, dim V = %d)' % (label, V.dim))
        dbl = Gr.double_cosets(H, D)
        for M, V in pairs[:3]:
            a, b = split_summand(restrict(V, H), M)
            theta = higman_theta(Gr, D, M, H)
            alpha = sp(a) * sp(theta) * sp(b)
            e = tr(Gr, D, V, V, alpha, H)
            check(e * e == e and e == sp(a) * sp(b), 'Thm 3.12.3, proof '
                  '(p. 87): e = Tr_(D,H)(alpha) is the idempotent of the '
                  'summand M (%s, dim V = %d)' % (label, V.dim))
            T = tr(Gr, D, V, V, alpha)
            rhs = zero_matrix(F, V.dim)
            rest = zero_matrix(F, V.dim)
            for g in dbl:
                I = Gr.intersect(H, Gr.conj_subgroup(g, D))
                ga = sp(V.mats[g]) * alpha * sp(V.mats[Gr.inv[g]])
                term = tr(Gr, I, V, V, ga, H)
                rhs += term
                if g not in set(H):
                    rest += term
            _, VY = endo_quotient(Gr, V, V, H, Ys, H)
            check(T == rhs and vector(F, (T - e).list()) in VY and
                  vector(F, rest.list()) in VY,
                  'Thm 3.12.3, proof (p. 87): Tr_(D,G)(alpha) = sum_(HgD) '
                  'Tr_(H cap gD, H)(g alpha) = e mod (V, V)^H_Y (%s, dim V '
                  '= %d)' % (label, V.dim))
            check(T.dense_matrix().is_invertible(), 'Thm 3.12.3, proof: '
                  'Tr_(D,G)(alpha) is a unit of the local ring (V, V)^G (%s)'
                  % label)
        # the display for random alpha (Lemma 3.6.3 (iv) with K = D)
        V = pairs[0][1]
        al = random_hom(restrict(V, D), restrict(V, D))
        rhs = zero_matrix(F, V.dim)
        for g in dbl:
            I = Gr.intersect(H, Gr.conj_subgroup(g, D))
            rhs += tr(Gr, I, V, V, sp(V.mats[g]) * sp(al) *
                      sp(V.mats[Gr.inv[g]]), H)
        check(tr(Gr, D, V, V, al) == rhs, 'Thm 3.12.3, proof (p. 87): the '
              'display is Lemma 3.6.3 (iv) with K = D, an equality in '
              'End_R(V) (%s)' % label)
    return ncorr


# ===========================================================================
# 3.13 Clifford theory
# ===========================================================================


def end_algebra_radical_dim(M):
    """dim End_(F H)(M) and dim of its Jacobson radical (GAP)."""
    E = hom_space(M, M)
    if len(E) == 1:
        return 1, 0
    A = libgap.Algebra(libgap.GF(M.F.order()), [libgap(e) for e in E])
    return int(A.Dimension()), int(libgap.RadicalOfAlgebra(A).Dimension())


def abs_indecomposable(M):
    """End(M) / J(End(M)) = k (the base field)."""
    d, r = end_algebra_radical_dim(M)
    return d - r == 1


def inertia_group(M, Gr):
    """T(M) = {g : gM ~ M} for a module M of a normal subgroup N."""
    return tuple(g for g in Gr.all if isomorphic(conjugate(M, g), M))


def section_3_13():
    # Mackey (p. 87), the inertia group (p. 88), Proposition 3.13.2.
    cases = [('S4', 3, ['(1,2)(3,4)', '(1,3)(2,4)']),
             ('S4', 2, ['(1,2,3)', '(1,2)(3,4)']),
             ('S4', 3, ['(1,2,3)', '(1,2)(3,4)']),
             ('A4', 4, ['(1,2)(3,4)', '(1,3)(2,4)']),
             ('A4', 3, ['(1,2)(3,4)', '(1,3)(2,4)']),
             ('S3', 4, ['(1,2,3)']), ('S3', 3, ['(1,2,3)']),
             ('D8', 3, ['(1,3)(2,4)']), ('D8', 2, ['(1,2,3,4)']),
             ('Q8', 3, None), ('A5', 2, None)]
    for name, q, Ng in cases:
        Gr, F = group(name), GF(q)
        if Ng is None:
            N = tuple(sorted(set(x for x in Gr.all
                                 if all(Gr.mul[x][y] == Gr.mul[y][x]
                                        for y in Gr.all)))) \
                if name == 'Q8' else Gr.all
            if name == 'A5':
                continue
        else:
            N = Gr.closure([Gr.el(s) for s in Ng])
        check(Gr.is_normal(N), 'N is normal (%s)' % name)
        label = '%s, |N| = %d, GF(%d)' % (name, len(N), q)
        # indecomposable N-modules: summands of permutation modules of N
        # and of the regular module
        Nmods = []
        for rep, mem in subgroup_classes(Gr, N):
            for S, k in indecomposable_summands(perm_module(Gr, F, rep, N)):
                add_new(Nmods, S)
        if name == 'D8' and q == 3:
            # the faithful character of N = Z(D8)
            z = [x for x in N if x][0]
            Nmods.append(Mod(Gr, N, F, 1, {0: identity_matrix(F, 1),
                                           z: -identity_matrix(F, 1)}))
        if name == 'Q8':
            z = [x for x in N if x][0]
            Nmods.append(Mod(Gr, N, F, 1, {0: identity_matrix(F, 1),
                                           z: -identity_matrix(F, 1)}))
        CN = tuple(g for g in Gr.all if all(Gr.mul[g][x] == Gr.mul[x][g]
                                            for x in N))
        NCN = Gr.closure(list(N) + list(CN))
        Lreps, _ = Gr.left_cosets(N)
        for M in Nmods:
            lab = '%s, dim M = %d' % (label, M.dim)
            Mi = induce(M)
            check(isomorphic(restrict(Mi, N), direct_sum(
                *[conjugate(M, g) for g in Lreps])), 'p. 87: M up^G down_N '
                  '~ sum_(g in G/N) gM (%s)' % lab)
            T = inertia_group(M, Gr)
            check(Gr.closure(T) == T and set(NCN) <= set(T),
                  'Def 3.13.1, p. 88: T(M) is a subgroup containing '
                  'N C_G(N) (%s, |T| = %d)' % (lab, len(T)))
            Ts = set(T)
            ok = all(isomorphic(conjugate(M, g), conjugate(M, h)) ==
                     (Gr.mul[Gr.inv[g]][h] in Ts)
                     for g in Lreps for h in Lreps)
            check(ok, 'p. 88: gM ~ g\'M iff g and g\' lie in the same left '
                  'coset of T (%s)' % lab)
            # Proposition 3.13.2
            MT = induce(M, T)
            parts = indecomposable_summands(MT)
            ok = True
            for Mi_, ki in parts:
                ok = ok and len(indecomposable_summands(induce(Mi_))) == 1 \
                    and indecomposable_summands(induce(Mi_))[0][1] == 1
                ok = ok and all(isomorphic(W, M) for W, k in
                                indecomposable_summands(restrict(Mi_, N)))
            for (A, a), (B, b) in itertools.product(parts, parts):
                ok = ok and (isomorphic(induce(A), induce(B)) ==
                             isomorphic(A, B))
            check(ok, 'Prop 3.13.2 (p. 88): M up^T = sum M_i, each M_i up^G '
                  'indecomposable, M_i up^G ~ M_j up^G iff M_i ~ M_j, '
                  'M_i down_N a sum of copies of M (%s, %d summands)'
                  % (lab, len(parts)))

    # The algebra E = End_kG(M up^G) for inertial M (pp. 88-89).
    for name, q, Ng, mod in [('A4', 4, ['(1,2)(3,4)', '(1,3)(2,4)'], 'k'),
                             ('S4', 3, ['(1,2)(3,4)', '(1,3)(2,4)'], 'k'),
                             ('S4', 2, ['(1,2)(3,4)', '(1,3)(2,4)'], 'k'),
                             ('S4', 3, ['(1,2,3)', '(1,2)(3,4)'], 'W'),
                             ('D8', 3, ['(1,3)(2,4)'], 'faithful'),
                             ('D8', 2, ['(1,2,3,4)'], 'J2'),
                             ('S3', 3, ['(1,2,3)'], 'J2'),
                             ('C3:C4', 3, ['(1,2,3)'], 'J2')]:
        Gr, F = group(name), GF(q)
        N = Gr.closure([Gr.el(s) for s in Ng])
        if mod == 'k':
            M = trivial(Gr, F, N)
        elif mod == 'W':
            # the 3-dimensional simple module of A4 in characteristic 3
            V4 = Gr.closure([Gr.el('(1,2)(3,4)'), Gr.el('(1,3)(2,4)')])
            lam = Mod(Gr, V4, F, 1, {v: matrix(F, [[1 if v in (0, Gr.el(
                '(1,2)(3,4)')) else -1]]) for v in V4})
            M = induce(lam, N)
        elif mod == 'faithful':
            z = [x for x in N if x][0]
            M = Mod(Gr, N, F, 1, {0: identity_matrix(F, 1),
                                  z: -identity_matrix(F, 1)})
        else:
            M = jordan_on(Gr, F, cyclic_generator(Gr, N), 2, N)
        label = '%s, |N| = %d, GF(%d), M = %s' % (name, len(N), q, mod)
        check(len(inertia_group(M, Gr)) == Gr.n, 'M is inertial (%s)'
              % label)
        Mi = induce(M)
        reps, where = Gr.left_cosets(N)
        d, m = M.dim, len(reps)
        E = hom_space(Mi, Mi)
        dE1 = len(hom_space(M, M))
        Vs = VectorSpace(F, Mi.dim ** 2)
        Ev = Vs.subspace([vector(F, e.list()) for e in E])
        # E_t: maps sending 1 (x) M into t (x) M
        Et = []
        for j in range(m):
            cond = []
            for i in range(m):
                if i == j:
                    continue
                for r in range(d):
                    for c in range(d):
                        w = vector(F, Mi.dim ** 2)
                        w[(i * d + r) * Mi.dim + c] = 1
                        cond.append(w)
            # restrict to E
            if cond:
                C = dmatrix(F, cond)
                coef = dmatrix(F, [C * vector(F, e.list()) for e in E]) \
                    .left_kernel().basis()
            else:
                coef = identity_matrix(F, len(E)).rows()
            Et.append([sum((c * e for c, e in zip(cf, E)),
                           zero_matrix(F, Mi.dim)) for cf in coef])
        check(all(len(x) == dE1 for x in Et) and
              sum(len(x) for x in Et) == len(E), 'p. 88: E = sum_(g in G/N)'
              ' E_g with dim E_g = dim End_kN(M) (%s)' % label)
        coset = lambda x: where[x][0]
        sub = lambda L: Vs.subspace([vector(F, a.list()) for a in L])
        Ets = [sub(x) for x in Et]
        ok_rev, ok_fwd = True, True
        for a_ in range(m):
            for b_ in range(m):
                prod = sub([sp(x) * sp(y) for x in Et[a_] for y in Et[b_]])
                ab = coset(Gr.mul[reps[a_]][reps[b_]])
                ba = coset(Gr.mul[reps[b_]][reps[a_]])
                ok_rev = ok_rev and prod == Ets[ba]
                ok_fwd = ok_fwd and prod == Ets[ab]
        check(ok_rev, 'p. 88: E_g E_g\' = E_(g\'g) for composition, i.e. '
              'E_g E_g\' = E_(gg\') with maps written on the right (%s)'
              % label)
        if name in ('S4',) and len(N) == 4:
            refuted(ok_fwd, 'p. 88: E_g E_g\' = E_(gg\') with E_g = '
                    'Hom_kN(M, gM) and composition as product (%s; G/N = S3'
                    ' non-abelian)' % label)
        # J(E_1), J(E_1) E_g = E_g J(E_1) of codimension one
        E1 = Et[coset(0)]
        A1 = libgap.Algebra(libgap.GF(q), [libgap(e) for e in E1])
        J1 = [matrix(F, [[F(c.sage(ring=F)) for c in row] for row in b])
              for b in libgap.Basis(libgap.RadicalOfAlgebra(A1))] \
            if dE1 > 1 else []
        check(len(E1) - len(J1) == 1, 'p. 88: E_1 = End_kN(M) is local with '
              'E_1 / J(E_1) = k (%s)' % label)
        ok = True
        for x in Et:
            L = sub([sp(j) * sp(e) for j in J1 for e in x])
            R_ = sub([sp(e) * sp(j) for j in J1 for e in x])
            ok = ok and L == R_ and L.dimension() == len(x) - 1
        check(ok, 'p. 88: J(E_1) E_g = E_g J(E_1) has codimension one in '
              'E_g (%s)' % label)
        I = sub([sp(j) * sp(e) for j in J1 for e in E])
        # I is a nilpotent two-sided ideal, so I <= J(E)
        P_ = I
        for _ in range(Mi.dim + 1):
            if P_.dimension() == 0:
                break
            P_ = sub([sp(matrix(F, Mi.dim, Mi.dim, list(a))) *
                      sp(matrix(F, Mi.dim, Mi.dim, list(b)))
                      for a in P_.basis() for b in I.basis()])
        check(P_.dimension() == 0 and len(E) - I.dimension() == m,
              'p. 88: J(E_1) E is a nilpotent ideal (so in J(E)) of '
              'codimension |G : N| (%s)' % label)
        dimE, dimJ = end_algebra_radical_dim(Mi)
        nsum = len(summand_classes(Mi))
        p = F.characteristic()
        if (Gr.n // len(N)) % p:
            # p' quotient: the twisted group algebra is semisimple
            check(dimJ == I.dimension(), 'p. 88: J(E) = J(E_1) E when '
                  '|G : N| is prime to p (%s)' % label)
        elif is_p_power(Gr.n // len(N), p):
            check(dimE - dimJ == 1 and nsum == 1, 'Thm 3.13.3 (p. 89): '
                  'E / J(E) = k, M up^G indecomposable (%s)' % label)

    # Theorem 3.13.3 (Green's indecomposability theorem, p. 89): G / N a
    # p-group, M absolutely indecomposable => M up^G absolutely
    # indecomposable.
    ngr = 0
    for name, q, Ng in [('D8', 2, ['(1,2,3,4)']),
                        ('D8', 2, ['(1,3)(2,4)', '(1,2)(3,4)']),
                        ('Q8', 2, None), ('S4', 2, ['(1,2,3)',
                                                    '(1,2)(3,4)']),
                        ('S4', 4, ['(1,2,3)', '(1,2)(3,4)']),
                        ('C9', 3, ['(1,4,7)(2,5,8)(3,6,9)']),
                        ('S3', 4, ['(1,2,3)']),
                        ('A4', 3, ['(1,2)(3,4)', '(1,3)(2,4)']),
                        ('C3:C4', 4, ['(1,2,3)', '(4,6)(5,7)'])]:
        Gr, F = group(name), GF(q)
        if Ng is None:
            N = Gr.closure([x for x in Gr.all if Gr.order_of(x) == 4][:1])
        else:
            N = Gr.closure([Gr.el(s) for s in Ng])
        p = F.characteristic()
        check(Gr.is_normal(N) and is_p_power(Gr.n // len(N), p),
              'Thm 3.13.3: N normal, G/N a p-group (%s, |N| = %d)'
              % (name, len(N)))
        Nmods = []
        for rep, mem in subgroup_classes(Gr, N):
            for S, k in indecomposable_summands(perm_module(Gr, F, rep, N)):
                add_new(Nmods, S)
        c = cyclic_generator(Gr, N)
        if c is not None and is_p_power(len(N), p):
            for a in range(2, len(N)):
                add_new(Nmods, jordan_on(Gr, F, c, a, N))
        if len(N) == 4 and p == 2 and cyclic_generator(Gr, N) is None:
            add_new(Nmods, aug_kernel(Gr, F, N))
            add_new(Nmods, dual(aug_kernel(Gr, F, N)))
        if q == 4:
            add_new(Nmods, omega_module_on(Gr, F, N))
        for M in Nmods:
            if not abs_indecomposable(M):
                continue
            check(abs_indecomposable(induce(M)), 'Thm 3.13.3 (p. 89): M up^G'
                  ' is absolutely indecomposable (%s, |N| = %d, dim M = %d)'
                  % (name, len(N), M.dim))
            ngr += 1
    # the hypothesis: G/N = C3 is not a 2-group, k up^(A4) decomposes
    Gr, F = group('A4'), GF(4)
    N = Gr.closure([Gr.el('(1,2)(3,4)'), Gr.el('(1,3)(2,4)')])
    refuted(abs_indecomposable(induce(trivial(Gr, F, N))), 'Thm 3.13.3 '
            'without G/N a p-group: k_(V4) up^(A4) indecomposable over GF(4)')
    # "every p'-cyclic central extension of a cyclic group of order p
    # splits": every group of order p m (gcd(p, m) = 1) with a central
    # cyclic subgroup Z of order m is Z x C_p.
    ok, nz = True, 0
    for p in (2, 3, 5, 7):
        for m in range(1, 13):
            if m % p == 0:
                continue
            for i in range(1, int(libgap.NrSmallGroups(p * m)) + 1):
                G = libgap.SmallGroup(p * m, i)
                Z = G.Centre()
                for c in G.ConjugacyClassesSubgroups():
                    K = c.Representative()
                    if int(K.Size()) != m or not K.IsCyclic() or \
                            not libgap.IsSubgroup(Z, K):
                        continue
                    nz += 1
                    P = G.SylowSubgroup(p)
                    ok = ok and bool(G.IsAbelian()) and \
                        int(libgap.Intersection(P, K).Size()) == 1
    check(ok and nz > 0, 'p. 89: every p\'-cyclic central extension of a '
          'cyclic group of order p splits (%d extensions of order p m <= 84)'
          % nz)
    return ngr


def jordan_type_of(X):
    """Block sizes of a nilpotent matrix X (from the ranks of its powers)."""
    n = X.nrows()
    ranks = [n]
    P = sp(identity_matrix(X.base_ring(), n))
    while ranks[-1] > 0:
        P = P * sp(X)
        ranks.append(P.rank())
    ge = [ranks[k - 1] - ranks[k] for k in range(1, len(ranks))]
    sizes = []
    for k in range(1, len(ge) + 1):
        sizes += [k] * (ge[k - 1] - (ge[k] if k < len(ge) else 0))
    return sorted(sizes, reverse=True)


def partitions_bounded(a, top):
    if a == 0:
        yield []
        return
    for first in range(min(a, top), 0, -1):
        for rest in partitions_bounded(a - first, first):
            yield [first] + rest


def section_3_13_ext():
    # p. 90: G = Z/p^n, N = Z/p, M an indecomposable kN-module with
    # non-trivial action (a Jordan block J_a, 2 <= a <= p) does not extend:
    # a p'-central extension of the cyclic G is P x Z with P = <x> cyclic of
    # order p^n, N = <x^(p^(n-1))>, and for every Jordan type of x on a
    # module of dimension a the element x^(p^(n-1)) does not act as J_a.
    ne = 0
    for p in (2, 3, 5):
        F = GF(p)
        for n in (2, 3):
            q = p ** (n - 1)
            for a in range(2, p + 1):
                ok = True
                for lam in partitions_bounded(a, p ** n):
                    # x acting with Jordan type lam
                    X = dmatrix(F, a, a, 1, sparse=True)
                    pos = 0
                    for b in lam:
                        for r in range(b - 1):
                            X[pos + r + 1, pos + r] = 1
                        pos += b
                    Y = sp(identity_matrix(F, a))
                    for _ in range(q):
                        Y = Y * X
                    ok = ok and jordan_type_of(Y - sp(identity_matrix(F, a))) \
                        != [a]
                    ne += 1
                check(ok, 'p. 90: J_%d of Z/%d does not extend to Z/%d (or '
                      'to any p\'-central extension)' % (a, p, p ** n))
    # (the indecomposability of M matters: over GF(2), J_3 of Z/4 restricts
    # to J_2 + J_1 on Z/2)
    F = GF(2)
    X = matrix(F, [[1, 0, 0], [1, 1, 0], [0, 1, 1]])
    check(jordan_type_of(X * X - identity_matrix(F, 3)) == [2, 1],
          'p. 90: the decomposable J_2 + J_1 of Z/2 extends to Z/4 (J_3)')

    # p. 90-91: K is the kernel of (End_kN(M)^op)^x -> k^x.  Read as the
    # reduction modulo J(End_kN(M)), K = 1 + J is 1 iff End_kN(M) = k and
    # consists of p-elements; read as the determinant on M it is neither.
    # (i) N = S3, k = GF(5), M the 2-dimensional simple module: End = k,
    # det(-1) = 1, so -1 (of order 2, not a power of 5) is in the kernel.
    Gr, F = group('S3'), GF(5)
    X = perm_module(Gr, F, Gr.closure([Gr.el('(1,2)')]))
    M = submodule(X, kernel_cols(matrix(F, [[1, 1, 1]])))
    E = hom_space(M, M)
    check(len(E) == 1 and mtx('IsAbsolutelyIrreducible')(gap_module(M)),
          'p. 91: End_kN(M) = k for the 2-dimensional simple GF(5)S3-module')
    m1 = -identity_matrix(F, 2)
    refuted(not (m1.det() == 1 and m1 != identity_matrix(F, 2)),
            'p. 90-91 (printed, "determinant map"): K = 1 when End_kN(M) = k '
            '(S3, GF(5): -1 has determinant 1)')
    # (ii) N = C3, k = GF(3), M = J_2: End = k[x]/(x^2); the reduction map
    # E^x -> k^x has kernel 1 + J = {1 + c x}, all of order dividing 3; the
    # determinant kernel also contains -1, of order 2.
    Gr, F = group('C3'), GF(3)
    M = jordan_on(Gr, F, Gr.gens[0], 2, Gr.all)
    E = hom_space(M, M)
    units = []
    for cs in itertools.product(F, repeat=len(E)):
        u = sum((c * e for c, e in zip(cs, E)), zero_matrix(F, 2))
        if u.det() != 0:
            units.append(u)
    one = identity_matrix(F, 2)
    # reduction modulo J: the eigenvalue of u (E local, E / J = k)
    red = lambda u: u[0, 0]
    Kred = [u for u in units if red(u) == 1]
    Kdet = [u for u in units if u.det() == 1]
    check(len(units) == 6 and len(Kred) == 3 and
          all(sp(u) * sp(u) * sp(u) == sp(one) for u in Kred) and
          all(red(sp(u) * sp(v)) == red(u) * red(v) for u in units
              for v in units),
          'p. 90-91 (corrected): the kernel of E^x -> (E/J)^x = k^x is 1 + J, '
          'a p-group (C3, GF(3), M = J_2)')
    refuted(all(sp(u) * sp(u) * sp(u) == sp(one) for u in Kdet),
            'p. 90-91 (printed, "determinant map"): every element of K has '
            'order a power of p (C3, GF(3), M = J_2: -1 has determinant 1)')

    # Theorem 3.13.4 (p. 91), case (i), for G = D8, N = Z(D8) = <z>, k of
    # characteristic 3, M the faithful character of N: G/N = C2 x C2 with
    # the central extension hat(G/N) = D8' (Z = <z'>), hat(G) the pullback
    # in D8 x D8', M extends to the character hat(M) of hat(G) with z' -> -1,
    # and M_0 (the 2-dimensional simple module of D8, the summand of
    # M up^G = M_0 + M_0) is hat(M) (x) V, V the 2-dimensional simple module
    # of D8' (the multiplicity module).
    F = GF(3)
    Gh = PermutationGroup(['(1,2,3,4)(5,6,7,8)', '(1,3)(5,7)',
                           '(1,3)(2,4)'])
    check(Gh.order() == 16, 'Thm 3.13.4: the pullback hat(G) has order 16')
    Grh = FinGroup.from_sage(Gh, 'hatG')
    z = Grh.el('(1,3)(2,4)')
    zp = Grh.el('(5,7)(6,8)')
    r, s = Grh.el('(1,2,3,4)(5,6,7,8)'), Grh.el('(1,3)(5,7)')
    # hat(M): r, s -> 1, z -> -1 (then z' = r^2 z -> -1)
    Mh = from_gens(Grh, F, 1, {r: matrix(F, [[1]]), s: matrix(F, [[1]]),
                               z: matrix(F, [[-1]])})
    check(Mh.mats[zp] == matrix(F, [[-1]]) and Mh.mats[z] ==
          matrix(F, [[-1]]), 'Thm 3.13.4: hat(M) restricts to M on N = <z> '
          'and Z = <z\'> acts by -1')
    # V: the 2-dimensional module of D8' (second factor), M_0: of D8 (first)
    rot = matrix(F, [[0, -1], [1, 0]])
    ref = matrix(F, [[1, 0], [0, -1]])
    V = from_gens(Grh, F, 2, {r: rot, s: ref, z: identity_matrix(F, 2)})
    M0 = from_gens(Grh, F, 2, {r: rot, s: ref, z: -identity_matrix(F, 2)})
    check(V.mats[zp] == -identity_matrix(F, 2) and
          M0.mats[zp] == identity_matrix(F, 2), 'Thm 3.13.4: Z acts on V by '
          '-1 and trivially on M_0')
    check(isomorphic(M0, tensor(Mh, V)), 'Thm 3.13.4 (p. 91): M_0 ~ hat(M) '
          '(x) V as hat(G)-modules (D8, N = Z(D8), GF(3))')
    # in G = D8 itself: M up^G = M_0 + M_0, the multiplicity of M in
    # M_0 down_N is dim V = 2, and End(M up^G) = M_2(k) (twisted, non-split)
    Gr = group('D8')
    N = Gr.closure([Gr.el('(1,3)(2,4)')])
    zz = Gr.el('(1,3)(2,4)')
    Mn = Mod(Gr, N, F, 1, {0: identity_matrix(F, 1),
                           zz: -identity_matrix(F, 1)})
    parts = summand_classes(induce(Mn))
    check(len(parts) == 1 and parts[0][1] == 2 and parts[0][2] == 2,
          'p. 90: M up^G = M_0 + M_0 with M_0 of dimension 2 (D8, GF(3))')
    return ne


# ===========================================================================
# 3.14 Modules for p-groups: the group algebra of a p-group in GAP terms
# ===========================================================================


class PGroupAlgebra:
    """F_p P for a finite p-group P (a GAP group): elements as coordinate
    vectors on the element list, right and left multiplication tables."""

    def __init__(self, P, p):
        self.P, self.p, self.F = P, p, GF(p)
        self.els = list(P.AsList())
        self.n = len(self.els)
        self.idx = {str(g): i for i, g in enumerate(self.els)}
        self.one = self.idx[str(P.One())]
        self.gens = [self.idx[str(g)] for g in P.GeneratorsOfGroup()]
        mult = libgap.eval('function(L) local i, j, n; n := Length(L); '
                           'return List(L, x -> List(L, y -> '
                           'Position(L, x * y))); end')
        tab = mult(self.els)
        self.mul = [[int(v) - 1 for v in row] for row in tab]

    def unit(self, g):
        v = vector(self.F, self.n)
        v[g] = 1
        return v

    def rmul(self, v, g):
        """v * g."""
        w = vector(self.F, self.n)
        for x in v.support():
            w[self.mul[x][g]] += v[x]
        return w

    def lmul(self, g, v):
        w = vector(self.F, self.n)
        for x in v.support():
            w[self.mul[g][x]] += v[x]
        return w

    def times(self, u, v):
        w = vector(self.F, self.n)
        for x in u.support():
            for y in v.support():
                w[self.mul[x][y]] += u[x] * v[y]
        return w

    def radical_powers(self):
        """J^0, J^1, ... (subspaces) until 0; J = augmentation ideal and
        J^(i+1) = sum_s J^i (s - 1) over generators s."""
        V = VectorSpace(self.F, self.n)
        J = V.subspace([self.unit(g) - self.unit(self.one)
                        for g in range(self.n) if g != self.one])
        out = [V, J]
        while out[-1].dimension() > 0:
            cur = out[-1]
            out.append(V.subspace([self.rmul(b, s) - b for b in cur.basis()
                                   for s in self.gens]))
        return out

    def socle_series(self):
        V = VectorSpace(self.F, self.n)
        out = [V.subspace([])]
        while out[-1].dimension() < self.n:
            prev = out[-1]
            C = prev.complement().basis()
            # x with (s - 1) x in prev for every generator s
            rows = []
            for s in self.gens:
                for c in C:
                    # c . ((s - 1) x) = 0 for all c in prev-perp
                    row = vector(self.F, self.n)
                    for x in range(self.n):
                        row[x] = c[self.mul[s][x]] - c[x]
                    rows.append(row)
            if rows:
                K = dmatrix(self.F, rows).right_kernel()
            else:
                K = V
            out.append(K)
        return out

    def subgroup_list(self, K):
        return set(self.idx[str(g)] for g in K.AsList())


def jennings_by_definition(P, p):
    """Gamma_1 = P; Gamma_r generated by [Gamma_s, Gamma_t] (s + t >= r)
    and x^p (x in Gamma_s, p s >= r) (p. 93)."""
    G = [None, P]
    r = 1
    while int(G[r].Size()) > 1:
        r += 1
        gens = [P.One()]
        for s in range(1, r):
            for t in range(1, r):
                if s + t >= r:
                    gens += list(libgap.CommutatorSubgroup(
                        G[s], G[t]).GeneratorsOfGroup())
            if p * s >= r:
                gens += [x ** p for x in G[s].AsList()]
        G.append(P.Subgroup(gens))
    return G[1:]


def poincare_from_layers(Js):
    R = PolynomialRing(ZZ, 't')
    t = R.gen()
    return sum(((Js[i].dimension() - Js[i + 1].dimension()) * t ** i
                for i in range(len(Js) - 1)), R(0))


def jennings_group(P, p, label, deep=True):
    """Theorem 3.14.6 and Corollary 3.14.7 for the p-group P."""
    A = PGroupAlgebra(P, p)
    n = A.n
    Js = A.radical_powers()
    # dimension subgroups F_r = {g : g - 1 in J^r}
    one = A.unit(A.one)
    L = len(Js) - 1             # J^L = 0
    Fr = [None] + [set(g for g in range(n) if A.unit(g) - one in Js[r])
                   for r in range(1, L + 1)]
    Gam = jennings_by_definition(P, p)
    Gs = [None] + [A.subgroup_list(K) for K in Gam]
    js = [A.subgroup_list(K) for K in P.JenningsSeries()]
    top = max(len(Gs), len(Fr)) + 1
    pad = lambda S, r: S[r] if r < len(S) else {A.one}
    check(all(pad(Fr, r) == pad(Gs, r) for r in range(1, top)),
          'Thm 3.14.6 (p. 95): F_r(P) = Gamma_r(P) for all r (%s)' % label)
    check(all(pad(Gs, r) == (js[r - 1] if r - 1 < len(js) else {A.one})
              for r in range(1, top)),
          'p. 93: the Jennings series by definition agrees with GAP\'s '
          'JenningsSeries (%s)' % label)
    phi = A.subgroup_list(P.FrattiniSubgroup())
    check(Fr[1] == set(range(n)) and pad(Fr, 2) == phi, 'p. 93: F_1(P) = P '
          'and F_2(P) = Phi(P) (%s)' % label)
    # [F_r, F_s] <= F_(r+s), F_r^p <= F_(pr); Gamma_r/Gamma_(r+1)
    # elementary abelian; central series
    inv = [A.mul[x].index(A.one) for x in range(n)]
    comm = lambda g, h: A.mul[A.mul[A.mul[g][h]][inv[g]]][inv[h]]
    def pw(g, k):
        r = A.one
        for _ in range(k):
            r = A.mul[r][g]
        return r
    ok = True
    for r in range(1, top):
        for s in range(1, top):
            if r + s >= top + 2:
                continue
            ok = ok and all(comm(g, h) in pad(Fr, r + s)
                            for g in pad(Fr, r) for h in pad(Fr, s))
        ok = ok and all(pw(g, p) in pad(Fr, p * r) for g in pad(Fr, r))
    check(ok, 'p. 93: [F_r, F_s] <= F_(r+s) and F_r^p <= F_(pr) (%s)'
          % label)
    nr = []
    ok = True
    for r in range(1, top):
        Gr_, Gr1 = pad(Gs, r), pad(Gs, r + 1)
        ok = ok and Gr1 <= Gr_ and all(pw(g, p) in Gr1 and
                                       all(comm(g, h) in Gr1 for h in
                                           range(n)) for g in Gr_)
        q = len(Gr_) // len(Gr1)
        e = 0
        while p ** e < q:
            e += 1
        ok = ok and p ** e == q
        nr.append(e)
    check(ok, 'p. 93: Gamma_r / Gamma_(r+1) is elementary abelian and '
          'central (%s)' % label)
    # Poincare series and radical length
    R = PolynomialRing(ZZ, 't')
    t = R.gen()
    pred = R(1)
    for r, e in enumerate(nr, start=1):
        pred *= sum(t ** (j * r) for j in range(p)) ** e
    got = poincare_from_layers(Js)
    check(got == pred, 'Thm 3.14.6 (p. 95): sum t^i dim J^i/J^(i+1) = '
          'prod_r (1 + t^r + ... + t^((p-1)r))^(n_r) (%s: %s)'
          % (label, got))
    ll = 1 + sum((p - 1) * r * e for r, e in enumerate(nr, start=1))
    check(L == ll and p ** sum(nr) == n, 'Thm 3.14.6 (p. 95): radical '
          'length 1 + sum (p-1) r n_r = %d, |P| = p^(sum n_r) (%s)'
          % (ll, label))
    check(nr[0] == Js[1].dimension() - Js[2].dimension(), 'p. 94: psi is '
          'an isomorphism in degree one: dim J/J^2 = n_1 (%s)' % label)
    # Corollary 3.14.7: symmetric series, Soc^i = J^(l-i)
    co = got.list()
    check(co == co[::-1], 'Cor 3.14.7 (p. 95): the Poincare series is '
          'symmetric (%s)' % label)
    if deep:
        Ss = A.socle_series()
        check(len(Ss) - 1 == L and all(Ss[i] == Js[L - i]
                                       for i in range(L + 1)),
              'Cor 3.14.7 (p. 95): Soc^i(kP) = J^(l-i)(kP) for all i (%s)'
              % label)
        # PBW / Jennings basis: prod (g_j - 1)^(a_j), 0 <= a_j < p, with
        # weight >= i span J^i
        gj, wj = [], []
        for r in range(1, top):
            cur = set(pad(Gs, r + 1))
            for g in sorted(pad(Gs, r)):
                if g in cur:
                    continue
                gj.append(g)
                wj.append(r)
                # cur = <cur, g> (cur normal, so cur . <g>)
                new = set(cur)
                frontier = list(cur)
                while frontier:
                    x = frontier.pop()
                    y = A.mul[x][g]
                    if y not in new:
                        new.add(y)
                        frontier.append(y)
                cur = new
                if cur == pad(Gs, r):
                    break
        check(len(gj) == sum(nr), 'p. 95: a basis x_1, ..., x_n of Jen_*(P) '
              'from elements of the Gamma_r (%s)' % label)
        elts = []
        for a in itertools.product(range(p), repeat=len(gj)):
            v = one
            for g, k in zip(gj, a):
                for _ in range(k):
                    v = A.rmul(v, g) - v
            elts.append((sum(k * w for k, w in zip(a, wj)), v))
        V = VectorSpace(A.F, n)
        ok = all(V.subspace([v for w, v in elts if w >= i]) == Js[i]
                 for i in range(L + 1))
        check(ok, 'Thm 3.14.6 (p. 95): the products prod (g_j - 1)^(a_j), '
              '0 <= a_j < p, of weight >= i form a basis of J^i (%s)' % label)
    return nr


def section_3_14():
    # Jennings' theorem for all groups of order p^k <= 64 (p = 2), 81
    # (p = 3), 125 (p = 5), 49 (p = 7)
    njen = 0
    for p, orders in [(2, [2, 4, 8, 16, 32, 64]), (3, [3, 9, 27, 81]),
                      (5, [5, 25, 125]), (7, [7, 49])]:
        for order in orders:
            ids = range(1, int(libgap.NrSmallGroups(order)) + 1)
            if order == 64:
                ids = range(1, 268, 22)     # 13 of the 267 groups
            for i in ids:
                P = libgap.SmallGroup(order, i)
                deep = order <= 32 or order == 27 or (order == 81 and
                                                      i <= 8)
                jennings_group(P, p, 'SmallGroup(%d, %d)' % (order, i), deep)
                njen += 1
    # the identities of p. 93 in F_p P, for all g, h
    for order, i, p in [(8, 3, 2), (8, 4, 2), (16, 3, 2), (27, 3, 3),
                        (27, 4, 3)]:
        A = PGroupAlgebra(libgap.SmallGroup(order, i), p)
        one = A.unit(A.one)
        inv = [A.mul[x].index(A.one) for x in range(A.n)]
        u = A.unit
        ok = True
        for g in range(A.n):
            gm = u(g) - one
            pp = one
            for _ in range(p):
                pp = A.times(pp, gm)
            gp = A.one
            for _ in range(p):
                gp = A.mul[gp][g]
            ok = ok and u(gp) - one == pp
            ok = ok and u(inv[g]) - one == -A.times(u(inv[g]), gm)
            for h in range(A.n):
                hm = u(h) - one
                ok = ok and u(A.mul[g][h]) - one == gm + hm + A.times(gm, hm)
                ok = ok and u(A.mul[A.mul[h][g]][inv[h]]) - one == \
                    A.times(A.times(u(h), gm), u(inv[h]))
                c = A.mul[A.mul[A.mul[g][h]][inv[g]]][inv[h]]
                ok = ok and u(c) - one == A.times(
                    A.times(gm, hm) - A.times(hm, gm),
                    A.times(u(inv[g]), u(inv[h])))
        check(ok, 'p. 93: (gh - 1) = (g-1) + (h-1) + (g-1)(h-1), (g^-1 - 1) '
              '= -g^-1 (g-1), (hgh^-1 - 1) = h(g-1)h^-1, (g^p - 1) = (g-1)^p,'
              ' ([g,h] - 1) = ((g-1)(h-1) - (h-1)(g-1)) g^-1 h^-1 in F_%d '
              'SmallGroup(%d, %d)' % (p, order, i))
    # Philip Hall's identity (p. 94) in the free group on x, y, z, with
    # [a, b] = a b a^-1 b^-1 and ^y a = y a y^-1 as in the formulas above
    Fr = libgap.FreeGroup(3)
    x, y, z = Fr.GeneratorsOfGroup()
    cm = lambda a, b: a * b * a ** -1 * b ** -1
    lc = lambda g, a: g * a * g ** -1
    w = lc(y, cm(x, cm(y ** -1, z))) * lc(z, cm(y, cm(z ** -1, x))) * \
        lc(x, cm(z, cm(x ** -1, y)))
    check(w == Fr.One(), 'p. 94: Philip Hall\'s identity holds in the free '
          'group on x, y, z')
    return njen


def p_group_modules(Gr, F, p):
    """Indecomposable modules of a p-group: summands of permutation modules,
    Omega^(+-1)(k), induced augmentation ideals."""
    mods = []
    for rep, mem in subgroup_classes(Gr, Gr.all):
        for S, k in indecomposable_summands(perm_module(Gr, F, rep)):
            add_new(mods, S)
    k = trivial(Gr, F)
    R = Resolution(k, 2)
    for X in (R.omega(1), R.omega(2), dual(R.omega(1))):
        for S, m in indecomposable_summands(X):
            add_new(mods, S)
    return mods


def section_3_14_modules():
    for name, p in [('C4', 2), ('C2xC2', 2), ('D8', 2), ('Q8', 2),
                    ('C4xC2', 2), ('C2^3', 2), ('C9', 3), ('C3xC3', 3),
                    ('C8', 2), ('C5', 5)]:
        Gr, F = group(name), GF(p)
        P = Gr.all
        label = '%s, GF(%d)' % (name, p)
        reg = regular(Gr, F)
        cf = mtx('CompositionFactors')(gap_module(reg))
        gens_of_mtx = libgap.eval('x -> x.generators')
        one1 = libgap(identity_matrix(F, 1))
        check(all(int(mtx('Dimension')(c)) == 1 and
                  all(A == one1 for A in gens_of_mtx(c)) for c in cf),
              'Lemma 3.14.1 (p. 91): every composition factor of kP is the '
              'trivial module (%s)' % label)
        mods = p_group_modules(Gr, F, p)
        # Lemma 3.14.1, proof: orbits on A = F_p-span of P m, fixed points
        ok, nm = True, 0
        if True:
            for M in mods:
                if p ** M.dim > 81:
                    continue
                nm += 1
                for mv in itertools.islice(
                        (vector(F, v) for v in itertools.product(
                            F, repeat=M.dim)), 1, None):
                    S = VectorSpace(F, M.dim).subspace(
                        [M.mats[g] * mv for g in P])
                    pts = list(S)
                    fixed = [v for v in pts
                             if all(M.mats[g] * v == v for g in P)]
                    seen, sizes = set(), []
                    for v in pts:
                        key = tuple(v)
                        if key in seen:
                            continue
                        orb = set(tuple(M.mats[g] * v) for g in P)
                        seen |= orb
                        sizes.append(len(orb))
                    ok = ok and all(is_p_power(s, p) for s in sizes) and \
                        len(fixed) % p == 0 and len(fixed) > 1
            check(ok and nm > 0, 'Lemma 3.14.1, proof (pp. 91-92): orbits '
                  'on the span of P m have p-power size, the number of fixed '
                  'points is divisible by p and > 1 (%s, all m in %d modules)'
                  % (label, nm))
        # decomposition and Cartan matrices (p. 92)
        ct = libgap(Gr.sage).CharacterTable()
        bt = ct.BrauerTable(p)
        dm = libgap.DecompositionMatrix(bt)
        degs = sorted(int(c[0]) for c in ct.Irr())
        col = sorted(int(r[0]) for r in dm)
        check(int(libgap.Length(dm[0])) == 1 and col == degs and
              sum(d * d for d in degs) == Gr.n,
              'p. 92: the decomposition matrix is one column of the degrees '
              'of the ordinary irreducibles, Cartan matrix (|P|) (%s)'
              % label)
        # Soc(kP): unique minimal left ideal, spanned by the sum of the
        # elements; non-projective indecomposables have it in their kernel
        A = sum(sp(reg.mats[g]) for g in P)
        check(fixed_dim(reg) == 1 and A.rank() == 1, 'p. 92: kP has a unique'
              ' minimal left ideal Soc(kP), spanned by sum g (%s)' % label)
        ok = True
        for M in mods:
            S = sum(sp(M.mats[g]) for g in P)
            proj = projective_in(M, p)
            ok = ok and (S.is_zero() != proj)
        check(ok, 'p. 92: every non-projective indecomposable kP-module has '
              'Soc(kP) in its kernel (%s, %d modules)' % (label, len(mods)))
        ok = True
        for rep, mem in subgroup_classes(Gr, P):
            X = perm_module(Gr, F, rep)
            ok = ok and fixed_dim(X) == 1 and len(summand_classes(X)) == 1 \
                and summand_classes(X)[0][2] == 1
        check(ok, 'p. 92: transitive permutation modules of kP have a one '
              'dimensional socle and are indecomposable (%s)' % label)
        # Proposition 3.14.2: dim Ext^1(k, k) = rank of P / Phi(P)
        k = trivial(Gr, F)
        rk = 0
        frat = int(libgap(Gr.sage).FrattiniSubgroup().Size())
        while p ** rk < Gr.n // frat:
            rk += 1
        nhom = 0
        for vals in itertools.product(F, repeat=len(Gr.gens)):
            try:
                from_gens(Gr, F, 2, {s: matrix(F, [[1, v], [0, 1]])
                                     for s, v in zip(Gr.gens, vals)})
                nhom += 1
            except AssertionError:
                pass
        check(ext_dims(k, k, 1)[1] == rk and nhom == p ** rk,
              'Prop 3.14.2 (p. 92): Ext^1(k, k) = Hom(P/Phi(P), k^+) of '
              'dimension %d; the matrices (1, a(g); 0, 1) (%s)' % (rk, label))
        # Proposition 3.14.4, Corollary 3.14.5
        ok = True
        R = Resolution(k, 4)
        for M in mods:
            h = R.ext_dims(M, 3)[1:]
            proj = projective_in(M, p)
            ok = ok and (proj == (h[0] == 0) == (h[1] == 0) == (h[2] == 0))
        check(ok, 'Prop 3.14.4 (p. 93): M projective iff H^n(P, M) = 0 for '
              'some n > 0 iff for all n (n <= 3) (%s)' % label)
        ok = True
        for M, N in itertools.product(mods[:5], mods[:5]):
            e = Resolution(M, 3).ext_dims(N, 2)[1:]
            proj = projective_in(tensor(dual(M), N), p)
            ok = ok and (proj == (e[0] == 0) == (e[1] == 0))
        check(ok, 'Cor 3.14.5 (p. 93): Ext^n(M, N) = 0 (n = 1, 2) iff '
              'M* (x) N is projective (%s)' % label)
    # Proposition 3.14.3: H^1(G, k) = H^1(G / O^p(G), k)
    for name, p in [('S3', 2), ('S3', 3), ('A4', 2), ('A4', 3), ('S4', 2),
                    ('S4', 3), ('C3:C4', 2), ('C3:C4', 3), ('D10', 2),
                    ('D10', 5), ('C6', 2), ('C6', 3), ('A5', 2)]:
        Gr, F = group(name), GF(p)
        Op = Gr.closure([x for x in Gr.all if Gr.order_of(x) % p])
        Q, pi = Gr.quotient(Op)
        hG = ext_dims(trivial(Gr, F), trivial(Gr, F), 1)[1]
        hQ = ext_dims(trivial(Q, F), trivial(Q, F), 1)[1] if Q.n > 1 else 0
        check(hG == hQ and is_p_power(Q.n, p), 'Prop 3.14.3 (p. 93): '
              'H^1(G, k) = H^1(G / O^p(G), k) (%s, p = %d, dim %d)'
              % (name, p, hG))


# ===========================================================================
# 3.15 Tensor induction
# ===========================================================================


def wreath_image(Gr, H, ambient, reps=None):
    """i(g) = (pi; h_1, ..., h_n) with g g_j = g_(pi(j)) h_j (p. 97), for
    left coset representatives g_1, ..., g_n of H in ambient."""
    if reps is None:
        reps, _ = Gr.left_cosets(H, ambient)
    where = {}
    for j, t in enumerate(reps):
        for h in H:
            where[Gr.mul[t][h]] = (j, h)
    out = {}
    for g in ambient:
        pi, hs = [], []
        for t in reps:
            j, h = where[Gr.mul[g][t]]
            pi.append(j)
            hs.append(h)
        out[g] = (tuple(pi), tuple(hs))
    return out, reps


def wreath_mul(Gr, a, b):
    """(pi'; h')(pi; h) = (pi' pi; h'_(pi(1)) h_1, ..., h'_(pi(n)) h_n)."""
    pi2, h2 = a
    pi, h = b
    return (tuple(pi2[pi[j]] for j in range(len(pi))),
            tuple(Gr.mul[h2[pi[j]]][h[j]] for j in range(len(pi))))


def tensor_induce(M, ambient=None, reps=None):
    """M tensorup^ambient = i^*(M^(x)n) with (pi; h)(m_1 (x) ... (x) m_n) =
    h_(pi^-1(1)) m_(pi^-1(1)) (x) ... (Definition 3.15.1)."""
    Gr, F, d = M.Gr, M.F, M.dim
    ambient = Gr.all if ambient is None else tuple(ambient)
    img, reps = wreath_image(Gr, M.H, ambient, reps)
    n = len(reps)
    mats = {}
    for g in ambient:
        pi, hs = img[g]
        K = M.mats[hs[0]]
        for j in range(1, n):
            K = K.tensor_product(M.mats[hs[j]])
        # move factor j to position pi(j)
        Q = zero_matrix(F, d ** n)
        for c in itertools.product(range(d), repeat=n):
            src = 0
            for x in c:
                src = src * d + x
            c2 = [0] * n
            for j in range(n):
                c2[pi[j]] = c[j]
            tgt = 0
            for x in c2:
                tgt = tgt * d + x
            Q[tgt, src] = 1
        mats[g] = sp(Q) * sp(K)
    return Mod(Gr, ambient, F, d ** n, mats)


def is_module(M):
    Gr = M.Gr
    return all(sp(M.mats[Gr.mul[a][b]]) == sp(M.mats[a]) * sp(M.mats[b])
               for a in M.H for b in M.H)


def core(Gr, H, ambient=None):
    ambient = Gr.all if ambient is None else ambient
    S = set(H)
    for g in ambient:
        S &= set(Gr.conj_subgroup(g, H))
    return tuple(sorted(S))


def stabiliser_module(T, K, idxs):
    """The K-submodule of T spanned by the basis vectors idxs."""
    F = T.F
    B = dmatrix(F, T.dim, len(idxs), sparse=True)
    for c, i in enumerate(idxs):
        B[i, c] = 1
    return submodule(restrict(T, K), B)


def section_3_15():
    # The wreath product embedding and the module structures (p. 97).
    for name, Hg in [('S4', ['(1,2,3)', '(1,2)']), ('S4', ['(1,2,3,4)',
                                                        '(1,3)']),
                     ('A4', ['(1,2)(3,4)', '(1,3)(2,4)']), ('D8', ['(1,3)']),
                     ('S3', ['(1,2)']), ('A5', ['(1,2,3)', '(1,2)(4,5)'])]:
        Gr = group(name)
        H = Gr.closure([Gr.el(s) for s in Hg])
        img, reps = wreath_image(Gr, H, Gr.all)
        ok = all(img[Gr.mul[a][b]] == wreath_mul(Gr, img[a], img[b])
                 for a in Gr.all for b in Gr.all)
        check(ok and len(set(img.values())) == Gr.n, 'p. 97: i : G -> '
              'Sigma_n wr H is an injective homomorphism for the printed '
              'multiplication (%s, |H| = %d)' % (name, len(H)))
        # the printed product is associative on the image and a different
        # choice of coset representatives gives a conjugate embedding
        reps2 = [Gr.mul[t][random.choice(H)] for t in reps]
        img2, _ = wreath_image(Gr, H, Gr.all, reps2)
        u = tuple(Gr.mul[Gr.inv[t]][t2] for t, t2 in zip(reps, reps2))
        c = (tuple(range(len(reps))), u)
        cinv = (tuple(range(len(reps))), tuple(Gr.inv[x] for x in u))
        check(all(img2[g] == wreath_mul(Gr, cinv, wreath_mul(Gr, img[g], c))
                  for g in Gr.all), 'p. 97: another choice of coset '
              'representatives gives a conjugate embedding (%s)' % name)
    # (pi; h)(m_1, ..., m_n) is an action of Sigma_n wr H, and i^*(M^n) is
    # M up^G
    Gr, F = group('S4'), GF(3)
    H = Gr.closure([Gr.el('(1,2,3)'), Gr.el('(1,2)')])
    M = direct_sum(sign(Gr, F, H), trivial(Gr, F, H))
    img, reps = wreath_image(Gr, H, Gr.all)
    n, d = len(reps), M.dim

    def act(w, v):
        pi, hs = w
        pinv = [pi.index(i) for i in range(n)]
        return sum(([list(M.mats[hs[pinv[i]]] * v[pinv[i]])
                     for i in range(n)]), [])
    els = list(itertools.product(itertools.permutations(range(n)),
                                 itertools.product(H, repeat=n)))
    random.shuffle(els)
    ok = True
    for a, b in zip(els[:40], els[40:80]):
        v = [vector(F, [F.random_element() for _ in range(d)])
             for _ in range(n)]
        lhs = act(wreath_mul(Gr, a, b), v)
        mid = act(b, v)
        rhs = act(a, [vector(F, mid[i * d:(i + 1) * d]) for i in range(n)])
        ok = ok and lhs == rhs
    check(ok, 'p. 97: (pi; h)(m_1, ..., m_n) = (h_(pi^-1(1)) m_(pi^-1(1)), '
          '...) is an action of Sigma_n wr H (40 random pairs)')
    Mi = induce(M)
    ok = all(list(Mi.mats[g] * vector(F, sum((list(x) for x in v), []))) ==
             act(img[g], v) for g in Gr.all
             for v in [[vector(F, [F.random_element() for _ in range(d)])
                        for _ in range(n)]])
    check(ok, 'p. 97: M up^G = i^*(M^n) (S4, H = S3)')

    # Definition 3.15.1 and Proposition 3.15.2
    for name, q, Hg, Kg in [('S4', 2, ['(1,2,3)', '(1,2)'], ['(1,2)']),
                            ('S4', 3, ['(1,2,3,4)', '(1,3)'], ['(1,3)']),
                            ('A4', 2, ['(1,2)(3,4)', '(1,3)(2,4)'],
                             ['(1,2)(3,4)']),
                            ('D8', 2, ['(1,2,3,4)'], ['(1,3)(2,4)']),
                            ('S3', 3, ['(1,2,3)'], [])]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        Hp = Gr.closure([Gr.el(s) for s in Kg]) if Kg else (0,)
        label = '%s, |H| = %d, GF(%d)' % (name, len(H), q)
        mods = [trivial(Gr, F, H)]
        for S, k in indecomposable_summands(perm_module(Gr, F, Hp, H)):
            add_new(mods, S)
        if name in ('S4', 'S3') and q == 3:
            mods.append(sign(Gr, F, H))
        mods = [M for M in mods if M.dim ** (Gr.n // len(H)) <= 81][:3]
        T = {id(M): tensor_induce(M) for M in mods}
        check(all(is_module(X) for X in T.values()), 'Def 3.15.1 (p. 97): '
              'M tensorup^G is a module (%s)' % label)
        # independence of the coset representatives: with g'_j = g_j u_j
        # the two modules are conjugate by (x) u_j (explicitly)
        reps, _ = Gr.left_cosets(H)
        reps2 = [Gr.mul[t][random.choice(H)] for t in reps]
        n = len(reps)
        ok = True
        for M in mods:
            T2 = tensor_induce(M, reps=reps2)
            us = [Gr.mul[Gr.inv[t]][t2] for t, t2 in zip(reps, reps2)]
            Cm = M.mats[us[0]]
            for u_ in us[1:]:
                Cm = Cm.tensor_product(M.mats[u_])
            Cm = sp(Cm)
            ok = ok and all(sp(T[id(M)].mats[g]) * Cm == Cm * sp(T2.mats[g])
                            for g in Gr.gens)
        check(ok, 'p. 97: M tensorup^G does not depend on the coset '
              'representatives (conjugate by (x) u_j) (%s)' % label)
        # (i): the shuffle of tensor factors is an isomorphism
        for M1, M2 in itertools.combinations_with_replacement(mods, 2):
            if (M1.dim * M2.dim) ** n > 256:
                continue
            A1 = tensor_induce(tensor(M1, M2))
            B1 = tensor(T[id(M1)], T[id(M2)])
            a, b = M1.dim, M2.dim
            Psh = dmatrix(F, A1.dim, A1.dim, sparse=True)
            for cs in itertools.product(range(a * b), repeat=n):
                src_ = 0
                for c_ in cs:
                    src_ = src_ * (a * b) + c_
                xs, ys = 0, 0
                for c_ in cs:
                    xs = xs * a + c_ // b
                    ys = ys * b + c_ % b
                Psh[xs * b ** n + ys, src_] = 1
            check(all(Psh * sp(A1.mats[g]) == sp(B1.mats[g]) * Psh
                      for g in Gr.gens), 'Prop 3.15.2 (i) (p. 97): (M1 (x) '
                  'M2) tensorup ~ M1 tensorup (x) M2 tensorup by the shuffle '
                  'of factors (%s, dims %d, %d)' % (label, M1.dim, M2.dim))
        # (iii): (M1 + M2)^(x)n is the sum of the U_S (S = positions with a
        # factor from M1); U_all = M1 tensorup, U_empty = M2 tensorup, and
        # each orbit sum of U_S is U_S up^G from the stabiliser G_S
        img, reps = wreath_image(Gr, H, Gr.all)
        cH = core(Gr, H)
        for M1, M2 in itertools.combinations(mods, 2):
            S = direct_sum(M1, M2)
            if S.dim ** n > 256:
                continue
            TS = tensor_induce(S)
            d1, dd = M1.dim, S.dim
            cods = list(itertools.product(range(dd), repeat=n))

            def U(Sset):
                return [i for i, c in enumerate(cods)
                        if all((c[j] < d1) == (j in Sset) for j in range(n))]
            ok = True
            for Sset, Tm in [(frozenset(range(n)), T[id(M1)]),
                             (frozenset(), T[id(M2)])]:
                idx = U(Sset)
                ok = ok and all(sp(TS.mats[g]).matrix_from_rows_and_columns(
                    idx, idx) == sp(Tm.mats[g]) for g in Gr.all)
            subsets = [frozenset(c) for r in range(1, n)
                       for c in itertools.combinations(range(n), r)]
            seen, norb = set(), 0
            for Sset in subsets:
                if Sset in seen:
                    continue
                orbit = set(frozenset(img[g][0][j] for j in Sset)
                            for g in Gr.all)
                seen |= orbit
                K = tuple(g for g in Gr.all
                          if frozenset(img[g][0][j] for j in Sset) == Sset)
                ok = ok and len(K) < Gr.n and set(cH) <= set(K)
                W = sorted(i for O in orbit for i in U(O))
                Wm = stabiliser_module(TS, Gr.all, W)
                ok = ok and isomorphic(Wm, induce(stabiliser_module(
                    TS, K, U(Sset))))
                norb += 1
            check(ok, 'Prop 3.15.2 (iii) (p. 98): (M1 + M2) tensorup = M1 '
                  "tensorup + M2 tensorup + M', M' the sum of %d modules "
                  'induced from proper subgroups containing the core of H '
                  '(%s, dims %d, %d)' % (norb, label, M1.dim, M2.dim))
        # (v) Mackey formula, for K = H and the other subgroup L = Hp
        for L in (H, Hp) if len(Hp) > 1 else (H,):
            for M in mods:
                lhs = restrict(T[id(M)], L)
                pieces = []
                for g in Gr.double_cosets(L, H):
                    I = Gr.intersect(L, Gr.conj_subgroup(g, H))
                    pieces.append(tensor_induce(restrict(conjugate(M, g), I),
                                                L))
                rhs = pieces[0]
                for X in pieces[1:]:
                    rhs = tensor(rhs, X)
                check(isomorphic(lhs, rhs), 'Prop 3.15.2 (v) (p. 98): M '
                      'tensorup^G down_L ~ (x)_(L g H) (gM down_(L cap gH)) '
                      'tensorup^L (%s, |L| = %d, dim M = %d)'
                      % (label, len(L), M.dim))
        # (ii) transitivity H' <= H <= G
        if len(Hp) > 1:
            for M in [trivial(Gr, F, Hp)] + [
                    S for S, k in indecomposable_summands(
                        regular(Gr, F, Hp)) if S.dim <= 2][:2]:
                if M.dim ** (Gr.n // len(Hp)) > 81:
                    continue
                check(isomorphic(tensor_induce(tensor_induce(M, H)),
                                 tensor_induce(M)),
                      'Prop 3.15.2 (ii) (p. 97): M tensorup^H tensorup^G ~ '
                      'M tensorup^G (%s, |H\'| = %d, dim M = %d)'
                      % (label, len(Hp), M.dim))
        # (iv): M up^H tensorup^G is a sum of modules induced from
        # subgroups K containing the core of H' with K cap H <= H'
        if len(Hp) > 1 and (len(H) // len(Hp)) ** n <= 81:
            M = trivial(Gr, F, Hp)
            MH = induce(M, H)
            TMH = tensor_induce(MH)
            img, reps = wreath_image(Gr, H, Gr.all)
            j0 = [j for j, t in enumerate(reps) if t in set(H)][0]
            m = len(H) // len(Hp)
            # coordinates: tuples c (one coset of H' in H per position)
            cH, cw = Gr.left_cosets(Hp, H)
            tuples = list(itertools.product(range(m), repeat=n))
            pos = {c: i for i, c in enumerate(tuples)}

            def move(g, c):
                pi, hs = img[g]
                c2 = [0] * n
                for j in range(n):
                    c2[pi[j]] = cw[Gr.mul[hs[j]][cH[c[j]]]][0]
                return tuple(c2)
            seen, parts, ok = set(), [], True
            cHp = core(Gr, Hp)
            for c in tuples:
                if c in seen or c[j0] != cw[0][0]:
                    continue
                orbit = set(move(g, c) for g in Gr.all)
                seen |= orbit
                K = tuple(g for g in Gr.all if move(g, c) == c)
                ok = ok and set(cHp) <= set(K) and \
                    set(Gr.intersect(K, H)) <= set(Hp)
                parts.append(induce(stabiliser_module(TMH, K, [pos[c]])))
            check(len(seen) == len(tuples) and ok and
                  isomorphic(TMH, direct_sum(*parts)),
                  'Prop 3.15.2 (iv) (p. 98): k_H\' up^H tensorup^G is a sum '
                  'of modules induced from K >= core(H\') with K cap H <= H\' '
                  '(%s, |H\'| = %d, %d orbits)' % (label, len(Hp), len(parts)))

    # (vi) Dress: R X (x) M2 tensorup ~ R X (x) (M1 + M3) tensorup for an
    # X-split 0 -> M1 -> M2 -> M3 -> 0, and the filtration U_j.
    for name, q, Hg, Lg, kind in [('D8', 2, ['(1,2,3,4)'], ['(1,3)'], 'J2'),
                                  ('S3', 3, ['(1,2,3)'], ['(1,2)'], 'J2'),
                                  ('A4', 2, ['(1,2)(3,4)', '(1,3)(2,4)'],
                                   ['(1,2,3)'], 'perm')]:
        Gr, F = group(name), GF(q)
        H = Gr.closure([Gr.el(s) for s in Hg])
        L = Gr.closure([Gr.el(s) for s in Lg])
        label = '%s, |H| = %d, X = G/L, |L| = %d, GF(%d)' % (name, len(H),
                                                          len(L), q)
        if kind == 'J2':
            c = cyclic_generator(Gr, H)
            M2 = jordan_on(Gr, F, c, 2, H)
            # M1 = the socle (second basis vector), M3 = the quotient
        else:
            C = Gr.closure([Gr.el('(1,2)(3,4)')])
            P_ = perm_module(Gr, F, C, H)
            # basis adapted to 0 -> k -> k[H/C] -> k -> 0: (1,1), (1,0)
            Bm = matrix(F, [[0, 1], [1, 1]])
            M2 = Mod(Gr, H, F, 2, {h: sp(Bm.inverse()) * sp(P_.mats[h]) *
                                   sp(Bm) for h in H})
        # in the basis (e_1, e_2) of M2, M1 = <e_2>, M3 = M2 / M1
        k = trivial(Gr, F, H)
        check(all(M2.mats[h][0, 1] == 0 and M2.mats[h][0, 0] == 1 and
                  M2.mats[h][1, 1] == 1 for h in H) and
              h_section(M2, k, matrix(F, [[1, 0]]), H) is None,
              'Prop 3.15.2 (vi): 0 -> k -> M2 -> k -> 0 is a non-split '
              'sequence of R H-modules (%s)' % label)
        X = perm_module(Gr, F, L)
        RX2 = tensor(restrict(X, H), M2)
        RX3 = tensor(restrict(X, H), k)
        pr = identity_matrix(F, X.dim).tensor_product(matrix(F, [[1, 0]]))
        check(h_section(RX2, RX3, pr, H) is not None, 'Prop 3.15.2 (vi): the '
              'sequence is X-split (%s)' % label)
        T2 = tensor_induce(M2)
        T13 = tensor_induce(direct_sum(k, k))
        n = Gr.n // len(H)
        # U_j: tensors with at most j factors outside M1 = <e_2>
        Us = []
        for j in range(n + 1):
            idxs = [i for i, cc in enumerate(itertools.product(range(2),
                                                               repeat=n))
                    if sum(1 for x in cc if x == 0) <= j]
            B = dmatrix(F, T2.dim, len(idxs), sparse=True)
            for col, i in enumerate(idxs):
                B[i, col] = 1
            Us.append(B)
        ok = all(sp(T2.mats[g]) * Us[j] == Us[j] * sp(Us[j]).solve_right(
            sp(T2.mats[g]) * Us[j]) for g in Gr.gens for j in range(n + 1))
        layers = []
        for j in range(n + 1):
            Uj = submodule(T2, Us[j])
            if j == 0:
                layers.append(Uj)
            else:
                # U_(j-1) inside U_j: its basis vectors are among those of
                # U_j
                prev = set(i for i in range(T2.dim) if any(Us[j - 1][i, c]
                           for c in range(Us[j - 1].ncols())))
                cols = [c for c in range(Us[j].ncols())
                        if any(Us[j][i, c] for i in prev)]
                Bp = dmatrix(F, Us[j].ncols(), len(cols), sparse=True)
                for cc, c in enumerate(cols):
                    Bp[c, cc] = 1
                layers.append(quotient_module(Uj, Bp))
        check(ok and isomorphic(direct_sum(*layers), T13),
              'Prop 3.15.2 (vi), proof (p. 98): the U_j are submodules and '
              '(M1 + M3) tensorup ~ U_0 + U_1/U_0 + ... + U_n/U_(n-1) (%s)'
              % label)
        check(isomorphic(tensor(X, T2), tensor(X, T13)), 'Prop 3.15.2 (vi) '
              '(Dress, p. 98): R X (x) M2 tensorup ~ R X (x) (M1 + M3) '
              'tensorup (%s)' % label)
        refuted(isomorphic(T2, T13), 'Prop 3.15.2 (vi) without R X: M2 '
                'tensorup ~ (M1 + M3) tensorup (%s)' % label)


def main():
    section_3_8()
    section_3_9()
    section_3_10_11()
    section_3_11()
    section_3_11_lifts()
    section_3_12()
    section_3_13()
    section_3_13_ext()
    section_3_14()
    section_3_14_modules()
    section_3_15()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
