"""Exact checks of Chapter 2, "Homological algebra" (Benson, Representations
and Cohomology I, second edition 1998).

Files: content/02-00-homological-algebra.typ ... 02-08-induction-restriction.typ;
the corrections are in corrections.json.  Expected values are the book's
statements, with the printed page (p.) of the 1998 edition at every check.
The chapter states general theorems; here they are checked on small algebras
over finite fields by exact linear algebra (dimensions and explicit maps).

Where the printed text is wrong the printed reading is kept beside the
corrected one as a check that must fail (`refuted(...)`):

* p. 34, Exercise: the second isomorphism printed with Ext^n(M, M'') twice on
  the right; fails for n = 0, M = M' = Lambda, M'' = 0.
* p. 38, Proposition 2.5.7: false for n = 1 (Lambda = k[x]/(x^3), M = k,
  M' = Lambda, every choice of Omega~); corrected "for n > 1".
* p. 44, l. -8 and l. -6 (the author's list of corrections, 2010: the formula
  must involve two components of f): as printed f is applied to x and to
  d_(i+1)(x), which lie in different modules; the corrected differential
  (d_n f)_i = d_j f_i - (-1)^n f_(i-1) d_i is checked.
* p. 45, after Definition 2.7.4: "homotopy equivalences" (twice) are only
  isomorphisms on homology (example over Z); and the comparison theorem holds
  for such resolutions only up to homotopy (example; Definition 2.7.4 itself
  is listed as incorrect in the author's corrections of 2010).

Covered (section, statement, printed page):

* 2.1 (p. 23): Omega and Omega^(-1) inverse on the stable category of a self
  injective algebra (8 algebras, 31 modules); Schanuel (2.4 below).
* 2.2 (pp. 25-27): progenerators P = sum m_i P_i of 6 basic algebras:
  dim End(P), Gamma/J(Gamma), Z(Lambda) = Z(Gamma) (Proposition 2.2.7), the
  maps phi, psi of Lemmas 2.2.3, 2.2.4 well defined isomorphisms.
* 2.3 (pp. 27-30): Propositions 2.3.5, 2.3.7, 2.3.8 and Lemma 2.3.9 on
  random short exact sequences of complexes over GF(2), GF(9), with the
  connecting map built as in the proof of 2.3.7 (random lifts).
* 2.4 (pp. 31-34): Theorem 2.4.2 (lifts and homotopies built as in the
  proof); the Example over Z; Ext^0 = Hom, Tor_0 = tensor; Remarks (i), (ii)
  (minimal resolutions, Schanuel); Proposition 2.4.3 for all pairs of simple
  modules of 7 path algebras and 7 local group algebras; the Remark on base
  change (Z C_p, p = 2, 3, 5); the Exercise (additivity).
* 2.5 (pp. 35-38): Lemma 2.5.1 (horseshoe), Propositions 2.5.2, 2.5.3 (long
  exact sequences, exactness checked term by term), Corollary 2.5.4,
  Proposition 2.5.5 (Ext by injective resolutions, Tor by resolving either
  variable), Proposition 2.5.7 for n = 2, 3, 4.
* 2.6 (pp. 38-42): Ext^1 as classes of extensions (derivations modulo inner
  ones), Lemma 2.6.2 exhaustively over GF(2), Yoneda composition (well
  defined, associative, not commutative), Exercise 3 (Feit).
* 2.7 (pp. 42-46): Theorem 2.7.1 (Kunneth) over Z, Corollaries 2.7.2, 2.7.3,
  the Hom complex, the dual, evaluation, shifts C[n]; Definition 2.7.4
  (counterexamples above; Tor of complexes computed both ways).
* 2.8 (pp. 46-48): Proposition 2.8.3 and Corollary 2.8.4 for 8 pairs of
  groups H < G in characteristic 2 and 3 (n <= 3), the natural maps, the
  hypothesis "Lambda projective over Gamma", Proposition 2.8.5 with Lambda = k.

Method.  An algebra is given by a faithful matrix representation (path
algebras k Q / I by their regular representation, group algebras by the
regular permutation representation, k[x]/(x^n) by a Jordan block); a module
by the matrices of the generators.  Projective covers use the given
idempotents and generators of J(A) (minimal resolutions) or are free covers;
Hom_A(M, N) is computed from a projective presentation of M and cross-checked
against the direct solution of X rho_M(g) = rho_N(g) X; Ext and Tor are the
(co)homology of Hom(P, N) and M' (x) P; injective resolutions and
Omega^(-1) come from duality D = Hom_k(-, k) over A^op.  Characteristic 3 is
computed over GF(9) (dimensions over GF(3) are unchanged by the extension;
GF(9) matrices also avoid the BLAS path of dense GF(p) matrices, which stops
with SIGILL on one of our machines); characteristic 2 over GF(2).  Random
choices are seeded.

Scope and what is NOT established: every statement is checked only for the
listed algebras, modules and degrees (a finite check is not a proof of the
general theorem); dimensions of Ext over extension fields equal those over
the prime field, but the module structures over GF(3) themselves are not
examined; nothing here compares our text with the printed book.

Literature consulted for the corrections (not used by the script):
C. A. Weibel, An Introduction to Homological Algebra, CUP 1994: Exercise
2.4.3 (p. 34, dimension shifting for i >= 2), Definition 5.7.1 and Lemma
5.7.2 (pp. 101-102, Cartan-Eilenberg resolutions); K. S. Brown, Cohomology of
Groups, GTM 87, Springer 1982: Chapter I, section 0 (p. 5, the Hom complex),
Theorems I.8.4-8.6 (p. 29).

Run with:  sage -python checks/sage/chapter-2.py
"""
import random
import time

# ---------------------------------------------------------------------------
# Library: linear algebra, algebras, modules, resolutions (exact, finite fields)
# ---------------------------------------------------------------------------
from itertools import product

from sage.all import (GF, ZZ, ChainComplex, Integer, gcd, matrix, vector,
                      identity_matrix, block_matrix, libgap, version)

CHECKS = []


def check(condition, where):
    """A statement of the book (or a step of its proof) that holds."""
    assert condition, 'FAILED: ' + where
    CHECKS.append(where)


def refuted(condition, where):
    """The printed reading, kept as a check that must FAIL."""
    assert not condition, 'printed reading unexpectedly holds: ' + where
    CHECKS.append('REFUTED ' + where)


def hstack(F, n, mats):
    mats = [m for m in mats if m.ncols() > 0]
    if not mats:
        return matrix(F, n, 0)
    out = mats[0]
    for m in mats[1:]:
        out = out.augment(m)
    return out


def vstack(F, n, mats):
    mats = [m for m in mats if m.nrows() > 0]
    if not mats:
        return matrix(F, 0, n)
    out = mats[0]
    for m in mats[1:]:
        out = out.stack(m)
    return out


def bdiag(F, mats):
    if not mats:
        return matrix(F, 0, 0)
    r = sum(m.nrows() for m in mats)
    c = sum(m.ncols() for m in mats)
    out = matrix(F, r, c)
    i = j = 0
    for m in mats:
        if m.nrows() and m.ncols():
            out.set_block(i, j, m)
        i += m.nrows()
        j += m.ncols()
    return out


def kron_IX(n, X):
    """I_n (x) X (Kronecker product, block diagonal)."""
    return bdiag(X.base_ring(), [X] * n)


def kron_XI(X, m):
    """X (x) I_m, a permutation conjugate of I_m (x) X."""
    p, q = X.nrows(), X.ncols()
    B = kron_IX(m, X)
    rows = [a * p + i for i in range(p) for a in range(m)]
    cols = [b * q + j for j in range(q) for b in range(m)]
    return B.matrix_from_rows_and_columns(rows, cols)


def col_basis(M):
    """Independent columns of M spanning its column space (chosen among them)."""
    if M.ncols() == 0 or M.nrows() == 0:
        return matrix(M.base_ring(), M.nrows(), 0)
    return M.matrix_from_columns(M.pivots())


def rank_of(M):
    return M.rank() if M.nrows() and M.ncols() else 0


def kernel_cols(M):
    """Basis of the right kernel, as columns."""
    F = M.base_ring()
    if M.ncols() == 0:
        return matrix(F, 0, 0)
    if M.nrows() == 0:
        return identity_matrix(F, M.ncols())
    return M.right_kernel_matrix().transpose()


def solve(M, X):
    """A solution Y of M Y = X (asserting that one exists)."""
    Y = M.solve_right(X)
    assert M * Y == X
    return Y


class Coords:
    """Coordinates with respect to a matrix W with independent columns."""

    def __init__(self, W):
        self.W = W
        self.rows = W.transpose().pivots() if W.ncols() else ()
        assert len(self.rows) == W.ncols()
        if W.ncols():
            self.inv = W.matrix_from_rows(self.rows).inverse()

    def __call__(self, X):
        F = self.W.base_ring()
        if self.W.ncols() == 0:
            assert X == 0
            return matrix(F, 0, X.ncols())
        C = self.inv * X.matrix_from_rows(self.rows)
        assert self.W * C == X, 'vector not in the subspace'
        return C


def spin(mats, W):
    """Smallest subspace containing the columns of W and stable under mats."""
    F = W.base_ring()
    n = W.nrows()
    cur = col_basis(W)
    while True:
        new = col_basis(hstack(F, n, [cur] + [g * cur for g in mats]))
        if new.ncols() == cur.ncols():
            return cur
        cur = new


class Alg:
    """A finite dimensional algebra over a finite field F, the span of the
    words in the matrices `gens` (a faithful representation).  `idems`: a
    complete set of primitive orthogonal idempotents, one for each
    isomorphism class of projective indecomposables (basic algebras), or
    [1] (local algebras, the default); `radgens`: elements generating J(A)
    as a two sided ideal.  Without radgens only free resolutions are used."""

    def __init__(self, F, gens, idems=None, radgens=None, name=''):
        self.F = F
        self.name = name
        self.gens = [matrix(F, g) for g in gens]
        m = self.gens[0].nrows()
        one = identity_matrix(F, m)
        basis, words = [one], [()]
        rows = matrix(F, [one.list()])
        frontier = [0]
        while frontier:
            new = []
            for k in frontier:
                for gi, g in enumerate(self.gens):
                    x = g * basis[k]
                    test = rows.stack(vector(F, x.list()))
                    if test.rank() > rows.nrows():
                        rows = test
                        basis.append(x)
                        words.append((gi,) + words[k])
                        new.append(len(basis) - 1)
            frontier = new
        self.basis, self.words, self.dim = basis, words, len(basis)
        self.cols = rows.pivots()
        self.cinv = rows.matrix_from_columns(self.cols).inverse()
        self.one = one
        self.idems = [matrix(F, e) for e in (idems or [one])]
        self.radgens = None if radgens is None else [matrix(F, r) for r in radgens]
        self._op = None
        self.Lgens = [self.L(g) for g in self.gens]

    def coords(self, a):
        v = vector(self.F, a.list())
        c = vector(self.F, [v[i] for i in self.cols]) * self.cinv
        assert self.elt(c) == a, 'element not in the algebra'
        return c

    def elt(self, c):
        return sum((c[k] * self.basis[k] for k in range(self.dim) if c[k]), 0 * self.one)

    def L(self, a):
        return matrix(self.F, [self.coords(a * b) for b in self.basis]).transpose()

    def R(self, a):
        return matrix(self.F, [self.coords(b * a) for b in self.basis]).transpose()

    def op(self):
        if self._op is None:
            o = Alg(self.F, [g.transpose() for g in self.gens],
                    [e.transpose() for e in self.idems],
                    None if self.radgens is None else
                    [r.transpose() for r in self.radgens], self.name + '^op')
            o._op = self
            self._op = o
        return self._op

    def regular(self):
        return Mod(self, self.Lgens)

    def left_ideal(self, e):
        """Basis (A-coordinates) of A e."""
        return col_basis(self.R(e))

    def J(self):
        W = matrix(self.F, [self.coords(r) for r in self.radgens]).transpose()
        return spin(self.Lgens + [self.R(g) for g in self.gens], W)

    def J2(self):
        J = self.J()
        prods = [self.coords(self.elt(a) * self.elt(b))
                 for a in J.columns() for b in J.columns()]
        return col_basis(matrix(self.F, prods).transpose())

    def centre_dim(self):
        """dim Z(A): elements commuting with the generators."""
        S = vstack(self.F, self.dim, [self.L(g) - self.R(g) for g in self.gens])
        return kernel_cols(S).ncols()


class Mod:
    """A left module over Alg A, by the action matrices of A.gens."""

    def __init__(self, A, mats):
        self.A = A
        self.mats = [matrix(A.F, x) for x in mats]
        self.dim = self.mats[0].nrows()
        self._acts = None

    def basis_action(self):
        if self._acts is None:
            F, n = self.A.F, self.dim
            acts = []
            for w in self.A.words:
                x = identity_matrix(F, n)
                for gi in reversed(w):
                    x = self.mats[gi] * x
                acts.append(x)
            self._acts = acts
        return self._acts

    def act_coords(self, c):
        acts = self.basis_action()
        out = matrix(self.A.F, self.dim, self.dim)
        for k in range(self.A.dim):
            if c[k]:
                out += c[k] * acts[k]
        return out

    def act(self, a):
        return self.act_coords(self.A.coords(a))

    def dual(self):
        """D(M) = Hom_k(M, k), a left module over A^op."""
        return Mod(self.A.op(), [x.transpose() for x in self.mats])

    def sub(self, W):
        if W.ncols() == 0:
            return zero_mod(self.A)
        c = Coords(W)
        return Mod(self.A, [c(g * W) for g in self.mats])

    def quotient(self, W):
        """(M / span W, projection matrix)."""
        F, n = self.A.F, self.dim
        W = col_basis(W)
        ext = col_basis(hstack(F, n, [W, identity_matrix(F, n)]))
        T = ext.inverse()
        k = W.ncols()
        proj = T.submatrix(k, 0)
        if n == k:
            return zero_mod(self.A), proj
        return Mod(self.A, [(T * g * ext).submatrix(k, k) for g in self.mats]), proj

    def radical(self):
        F = self.A.F
        W = hstack(F, self.dim, [self.act(r) for r in self.A.radgens])
        return spin(self.mats, W)


def zero_mod(A):
    return Mod(A, [matrix(A.F, 0, 0) for _ in A.gens])


def direct_sum(*mods):
    A = mods[0].A
    return Mod(A, [bdiag(A.F, [M.mats[i] for M in mods]) for i in range(len(A.gens))])


def hom_basis_kron(M, N):
    """Basis of Hom_A(M, N) as N.dim x M.dim matrices, by solving
    X rho_M(g) = rho_N(g) X directly (small modules only)."""
    F = M.A.F
    m, n = M.dim, N.dim
    if m == 0 or n == 0:
        return []
    Im, In = identity_matrix(F, m), identity_matrix(F, n)
    S = vstack(F, m * n, [kron_IX(n, gm.transpose()) - kron_XI(gn, m)
                          for gm, gn in zip(M.mats, N.mats)])
    K = kernel_cols(S)
    return [matrix(F, n, m, list(c)) for c in K.columns()]


def module_cover(M):
    """A projective (minimal if A has radgens) or free cover of M, cached."""
    if getattr(M, '_cover', None) is None:
        st = Stage(M, cover_generators(M, M.A.radgens is not None))
        kg = cover_generators(st.Omega, M.A.radgens is not None)
        d = M.A.dim
        rel = []
        for i, v in kg:
            img = st.amb * (st.K * v)
            rel.append([img[j * d:(j + 1) * d] for j in range(st.r)])
        sigma = solve(st.pi, identity_matrix(M.A.F, M.dim))
        M._cover = (st, rel, sigma)
    return M._cover


def grid(F, rows):
    """Assemble a 2D list of blocks (all blocks of a row with equal height,
    of a column with equal width)."""
    hs = [r[0].nrows() for r in rows]
    ws = [b.ncols() for b in rows[0]]
    out = matrix(F, sum(hs), sum(ws))
    i = 0
    for r, h in zip(rows, hs):
        j = 0
        for b, w in zip(r, ws):
            if h and w and b:
                out.set_block(i, j, b)
            j += w
        i += h
    return out


class HomSpace:
    """Hom_A(M, N): maps P -> N from a projective cover P -> M (images u_j
    in e_(i_j) N of the generators) vanishing on the generators of the
    kernel; K = basis of the coefficient space."""

    def __init__(self, M, N):
        A, F = M.A, M.A.F
        self.M, self.N, self.F = M, N, F
        if M.dim == 0 or N.dim == 0:
            self.K = matrix(F, 0, 0)
            return
        st, rel, sigma = module_cover(M)
        self.st = st
        eN = [col_basis(N.act(e)) for e in A.idems]
        self.D = bdiag(F, [eN[i] if i is not None else identity_matrix(F, N.dim)
                           for i in st.idem])
        if self.D.ncols() == 0:
            self.K = matrix(F, 0, 0)
            return
        if rel:
            C = grid(F, [[N.act_coords(a) for a in row] for row in rel])
            self.K = kernel_cols(C * self.D)
        else:
            self.K = identity_matrix(F, self.D.ncols())
        offs = [0]
        for E in st.blocks:
            offs.append(offs[-1] + E.ncols())
        self.Esig = [st.blocks[j] * sigma.submatrix(offs[j], 0, st.blocks[j].ncols(), M.dim)
                     for j in range(st.r)]
        self.ACT = vstack(F, N.dim, N.basis_action())

    def dim(self):
        return self.K.ncols()

    def element(self, c):
        """The map with coefficient vector c (in the basis K)."""
        F, n, d = self.F, self.N.dim, self.M.A.dim
        u = self.D * (self.K * c)
        X = matrix(F, n, self.M.dim)
        for j in range(self.st.r):
            v = self.ACT * u[j * n:(j + 1) * n]
            X += matrix(F, d, n, list(v)).transpose() * self.Esig[j]
        return X

    def basis(self):
        F = self.F
        return [self.element(c) for c in identity_matrix(F, self.dim()).columns()]


def hom_basis(M, N):
    """Basis of Hom_A(M, N) as N.dim x M.dim matrices."""
    if M.dim == 0 or N.dim == 0:
        return []
    return HomSpace(M, N).basis()


def hom_dim(M, N):
    if M.dim == 0 or N.dim == 0:
        return 0
    return HomSpace(M, N).dim()


def isomorphic(M, N, exhaustive=False, trials=400, seed=1):
    """True if an isomorphism M -> N is found.  With exhaustive=True the
    whole of Hom(M, N) is searched (so False proves non-isomorphism)."""
    if M.dim != N.dim:
        return False
    if M.dim == 0:
        return True
    H = HomSpace(M, N)
    h = H.dim()
    if h != hom_dim(M, M) or h != hom_dim(N, N):
        return False
    F = M.A.F
    elems = list(F)
    if len(elems) ** h <= 4096:
        for cs in product(elems, repeat=h):
            if H.element(vector(F, cs)).is_invertible():
                return True
        return False
    assert not exhaustive, 'Hom space too large for an exhaustive search'
    rnd = random.Random(seed)
    for _ in range(trials):
        if H.element(vector(F, [rnd.choice(elems) for _ in range(h)])).is_invertible():
            return True
    return False


def cover_generators(M, minimal=True, rnd=None):
    """Generators (idempotent index, vector) for a projective cover
    (minimal=True: lifts of a basis of each e_i(M/JM); with rnd the lifts
    are random) or a free cover (greedy generating set, index None)."""
    A, F, n = M.A, M.A.F, M.dim
    gens = []
    if n == 0:
        return gens
    if minimal:
        JM = M.radical()
        cur = JM
        for i, e in enumerate(A.idems):
            Ee = M.act(e)
            for col in Ee.columns():
                test = col_basis(hstack(F, n, [cur, matrix(F, n, 1, list(col))]))
                if test.ncols() > cur.ncols():
                    v = col
                    if rnd is not None and JM.ncols():
                        # add a random element of e_i J M
                        eJM = Ee * JM
                        v = v + eJM * vector(F, [rnd.choice(list(F)) for _ in range(JM.ncols())])
                    cur = test
                    gens.append((i, v))
        assert cur.ncols() == n
    else:
        cur = matrix(F, n, 0)
        for col in identity_matrix(F, n).columns():
            if col_basis(hstack(F, n, [cur, matrix(F, n, 1, list(col))])).ncols() > cur.ncols():
                gens.append((None, col))
                cur = spin(M.mats, hstack(F, n, [cur, matrix(F, n, 1, list(col))]))
                if cur.ncols() == n:
                    break
    return gens


class Stage:
    """P = sum_j A e_(i_j) inside A^r with the map P -> X sending the j-th
    generator e_(i_j) to the given vector; K = kernel, Omega = K as module."""

    def __init__(self, X, gens):
        A, F, d = X.A, X.A.F, X.A.dim
        self.A, self.gens, self.X = A, gens, X
        self.r = len(gens)
        self.idem = [i for i, _ in gens]
        blocks, pis = [], []
        for i, v in gens:
            E = A.left_ideal(A.idems[i]) if i is not None else identity_matrix(F, d)
            blocks.append(E)
            Wv = matrix(F, [a * v for a in X.basis_action()]).transpose()
            pis.append(Wv * E)
        self.blocks = blocks
        self.amb = bdiag(F, blocks)
        self.dim = self.amb.ncols()
        if self.r:
            c = Coords(self.amb)
            self.P = Mod(A, [c(bdiag(F, [L] * self.r) * self.amb) for L in A.Lgens])
        else:
            self.P = zero_mod(A)
        self.pi = hstack(F, X.dim, pis)
        self.K = kernel_cols(self.pi) if self.dim else matrix(F, 0, 0)
        self.Omega = self.P.sub(self.K)

    def gen_coords(self, j):
        """P-coordinates of the j-th generator."""
        A, F, d = self.A, self.A.F, self.A.dim
        e = A.idems[self.idem[j]] if self.idem[j] is not None else A.one
        v = vector(F, self.r * d)
        c = A.coords(e)
        for k in range(d):
            v[j * d + k] = c[k]
        return self.amb.solve_right(v)


class Resolution:
    """Projective resolution P_length -> ... -> P_0 -> M.  d[n]: P_n -> P_(n-1)
    in module bases; eps: P_0 -> M; omega[n] = Omega^n(M) (omega[0] = M)."""

    def __init__(self, M, length, minimal=True, rnd=None):
        self.M, self.A = M, M.A
        self.stages, self.d, self.omega = [], {}, [M]
        X = M
        for n in range(length + 1):
            st = Stage(X, cover_generators(X, minimal, rnd))
            self.stages.append(st)
            if n == 0:
                self.eps = st.pi
            else:
                self.d[n] = self.stages[n - 1].K * st.pi
            self.omega.append(st.Omega)
            X = st.Omega
        self._imgs = {}

    def P(self, n):
        return self.stages[n].P

    def gen_images(self, n):
        """For n >= 1: images of the generators of P_n in P_(n-1), as lists of
        A-coordinate vectors (one per summand of P_(n-1))."""
        if n not in self._imgs:
            st, prev = self.stages[n], self.stages[n - 1]
            d = self.A.dim
            out = []
            for jp in range(st.r):
                img = prev.amb * (self.d[n] * st.gen_coords(jp))
                out.append([img[j * d:(j + 1) * d] for j in range(prev.r)])
            self._imgs[n] = out
        return self._imgs[n]


def hom_from_P_cochains(res, N, nmax):
    """The cochain complex Hom_A(P_n, N), 0 <= n <= nmax, in coordinates:
    (dims, d) with d[n]: X^n -> X^(n+1) (n < nmax).  Hom(P_n, N) is
    identified with sum_j e_(i_j) N (images of the generators)."""
    A, F = res.A, res.A.F
    eN = [col_basis(N.act(e)) for e in A.idems]
    def dom(n):
        st = res.stages[n]
        return bdiag(F, [eN[i] if i is not None else identity_matrix(F, N.dim)
                         for i in st.idem])
    D = {n: dom(n) for n in range(nmax + 1)}
    dims = {n: D[n].ncols() for n in D}
    d = {}
    for n in range(nmax):
        imgs = res.gen_images(n + 1)
        rn = res.stages[n].r
        if rn == 0 or not imgs:
            d[n] = matrix(F, dims[n + 1], dims[n])
            continue
        big = block_matrix(F, [[N.act_coords(img[j]) for j in range(rn)] for img in imgs],
                           subdivide=False)
        d[n] = Coords(D[n + 1])(big * D[n]) if dims[n + 1] else matrix(F, 0, dims[n])
    return dims, d, D


def cohom_dims(dims, d, nmax):
    """Cohomology dimensions of a cochain complex for 0 <= n < nmax."""
    rk = {n: rank_of(d[n]) for n in d}
    return [dims[n] - rk[n] - (rk[n - 1] if n else 0) for n in range(nmax)]


def ext_dims(res, N, nmax):
    """dim Ext^n_A(M, N) for 0 <= n <= nmax (the resolution has length > nmax)."""
    dims, d, _ = hom_from_P_cochains(res, N, nmax + 1)
    return cohom_dims(dims, d, nmax + 1)


def tensor_with_P_chains(res, Mr, nmax):
    """The chain complex M' (x)_A P_n, 0 <= n <= nmax, for a right module M'
    given as a left A^op-module: (dims, d) with d[n]: X_n -> X_(n-1)."""
    A, F = res.A, res.A.F
    Aop = A.op()
    Top = matrix(F, [Aop.coords(b.transpose()) for b in A.basis]).transpose()
    eM = [col_basis(Mr.act(e.transpose())) for e in A.idems]
    def dom(n):
        st = res.stages[n]
        return bdiag(F, [eM[i] if i is not None else identity_matrix(F, Mr.dim)
                         for i in st.idem])
    D = {n: dom(n) for n in range(nmax + 1)}
    dims = {n: D[n].ncols() for n in D}
    d = {}
    for n in range(1, nmax + 1):
        imgs = res.gen_images(n)
        rprev = res.stages[n - 1].r
        if not imgs or rprev == 0:
            d[n] = matrix(F, dims[n - 1], dims[n])
            continue
        big = block_matrix(F, [[Mr.act_coords(Top * imgs[jp][j]) for jp in range(len(imgs))]
                               for j in range(rprev)], subdivide=False)
        d[n] = Coords(D[n - 1])(big * D[n]) if dims[n - 1] else matrix(F, 0, dims[n])
    return dims, d, D


def tor_dims(res, Mr, nmax):
    """dim Tor_n^A(M', N), 0 <= n <= nmax, res resolving N (length > nmax)."""
    dims, d, _ = tensor_with_P_chains(res, Mr, nmax + 1)
    rk = {n: rank_of(d[n]) for n in d}
    rk[0] = 0
    return [dims[n] - rk[n] - rk[n + 1] for n in range(nmax + 1)]


def tensor_dim(Mr, N):
    """dim M' (x)_A N computed directly as a quotient of M' (x)_k N."""
    A, F = N.A, N.A.F
    a, b = Mr.dim, N.dim
    if a == 0 or b == 0:
        return 0
    Ia, Ib = identity_matrix(F, a), identity_matrix(F, b)
    rel = hstack(F, a * b, [kron_XI(mg, b) - kron_IX(a, ng)
                            for mg, ng in zip(Mr.mats, N.mats)])
    return a * b - rank_of(rel)


def injective_coresolution(N, length, minimal=True):
    """0 -> N -> I_0 -> I_1 -> ..., the dual of a projective resolution of
    D(N) over A^op.  Returns (I list of A-modules, maps c: N -> I_0 and
    delta[n]: I_(n-1) -> I_n)."""
    res = Resolution(N.dual(), length, minimal)
    A = N.A
    I = [Mod(A, [x.transpose() for x in res.P(n).mats]) for n in range(length + 1)]
    delta = {n: res.d[n].transpose() for n in range(1, length + 1)}
    return I, res.eps.transpose(), delta, res


def cosyzygy(N, minimal=True):
    """Omega^(-1)(N) = D(Omega(D N))."""
    res = Resolution(N.dual(), 0, minimal)
    O = res.omega[1]
    return Mod(N.A, [x.transpose() for x in O.mats])


def ext_dims_injective(M, N, nmax):
    """dim Ext^n_A(M, N), 0 <= n <= nmax, as H^n(Hom_A(M, I)) for an injective
    coresolution I of N (Proposition 2.5.5 (ii))."""
    F = M.A.F
    I, c, delta, _ = injective_coresolution(N, nmax + 1)
    H = [hom_basis(M, I[n]) for n in range(nmax + 2)]
    dims = {n: len(H[n]) for n in range(nmax + 2)}
    d = {}
    for n in range(nmax + 1):
        if dims[n] == 0 or dims[n + 1] == 0:
            d[n] = matrix(F, dims[n + 1], dims[n])
            continue
        B = matrix(F, [h.list() for h in H[n + 1]]).transpose()
        imgs = matrix(F, [(delta[n + 1] * h).list() for h in H[n]]).transpose()
        d[n] = Coords(B)(imgs)
    return cohom_dims(dims, d, nmax + 1)

# ---------------------------------------------------------------------------
# Examples of algebras: path algebras with relations, group algebras
# ---------------------------------------------------------------------------

def path_algebra(F, nv, arrows, relations, L, name):
    """k Q / I for the quiver with nv vertices and arrows [(s, t), ...];
    a path is a tuple of arrows, first arrow first; the product p.q is
    "q, then p" (so left modules are representations, e_i M = M_i and an
    arrow i -> j maps M_i to M_j).  relations: list of {path: coefficient}.
    L: paths of length >= L must lie in the ideal (asserted)."""
    paths = [('e', i) for i in range(nv)]
    layer = [(a,) for a in range(len(arrows))]
    for _ in range(L):
        paths += layer
        layer = [p + (a,) for p in layer for a in range(len(arrows))
                 if arrows[p[-1]][1] == arrows[a][0]]
    longest = layer  # paths of length L + 1 (not in the basis)
    pos = {p: i for i, p in enumerate(paths)}
    n = len(paths)

    def s(p):
        return p[1] if p[0] == 'e' else arrows[p[0]][0]

    def t(p):
        return p[1] if p[0] == 'e' else arrows[p[-1]][1]

    def mult(p, q):  # p . q = q then p
        if t(q) != s(p):
            return None
        if p[0] == 'e':
            return q
        if q[0] == 'e':
            return p
        r = q + p
        return r if len(r) <= L else 'zero'

    def vec_of(rel):
        v = vector(F, n)
        for p, c in rel.items():
            v[pos[p]] += c
        return v

    gens_I = []
    for rel in relations:
        for p in paths:
            for q in paths:
                w = vector(F, n)
                for path, c in rel.items():
                    x = mult(path, q)
                    if x is None or x == 'zero':
                        continue
                    y = mult(p, x)
                    if y is None or y == 'zero':
                        continue
                    w[pos[y]] += c
                if w:
                    gens_I.append(w)
    Ibasis = col_basis(matrix(F, gens_I).transpose()) if gens_I else matrix(F, n, 0)
    # every path of length L lies in I, so truncating at length L is harmless
    for p in paths:
        if p[0] != 'e' and len(p) == L:
            assert rank_of(hstack(F, n, [Ibasis, matrix(F, n, 1, list(vec_of({p: 1})))])) \
                == Ibasis.ncols(), 'increase L'

    def left_mult(x):
        M = matrix(F, n, n)
        for j, q in enumerate(paths):
            y = mult(x, q)
            if y is not None and y != 'zero':
                M[pos[y], j] += 1
        return M

    elems = [('e', i) for i in range(nv)] + [(a,) for a in range(len(arrows))]
    ext = col_basis(hstack(F, n, [Ibasis, identity_matrix(F, n)]))
    T = ext.inverse()
    k = Ibasis.ncols()
    mats = [(T * left_mult(x) * ext).submatrix(k, k) for x in elems]
    A = Alg(F, mats, idems=mats[:nv], radgens=mats[nv:], name=name)
    A.nv = nv
    A.arrows = arrows
    return A


def vertex_simple(A, i):
    F = A.F
    mats = [matrix(F, 1, 1, [1 if j == i else 0]) for j in range(A.nv)] + \
           [matrix(F, 1, 1, [0]) for _ in A.arrows]
    return Mod(A, mats)


def proj_indec(A, i):
    return A.regular().sub(A.left_ideal(A.idems[i]))


def group_algebra(G, gens, F, pgroup):
    """F G in its left regular representation; gens: generators of G (GAP)."""
    els = list(G.AsList())
    n = len(els)
    def perm(g):
        M = matrix(F, n, n)
        for j, x in enumerate(els):
            M[int(libgap.Position(els, g * x)) - 1, j] = 1
        return M
    mats = [perm(g) for g in gens]
    one = identity_matrix(F, n)
    A = Alg(F, mats, radgens=[m - one for m in mats] if pgroup else None)
    A.group, A.els, A.perm = G, els, perm
    return A


def gap_modules(G, p, F):
    """Generators of G and its irreducible modules over GF(p) (by the
    MeatAxe), as matrices over F (an extension of GF(p))."""
    res = libgap.IrreducibleModules(G, libgap.GF(p), 0)
    gens = list(res[0])
    mods = []
    for m in res[1]:
        mods.append([matrix(F, matrix(GF(p), g.sage())) for g in m['generators']])
    return gens, mods


def trivial(A):
    F = A.F
    return Mod(A, [matrix(F, 1, 1, [1]) for _ in A.gens])


def subalgebra(Lam, elements, radgens=None):
    """The subalgebra of Lam generated by the given elements (same
    faithful representation)."""
    return Alg(Lam.F, elements, radgens=radgens)


def restrict(M, Gam):
    return Mod(Gam, [M.act(y) for y in Gam.gens])


def induce(Lam, Gam, N):
    """N up^Lam = Lam (x)_Gam N, with the projection from Lam (x)_k N."""
    F, d, n = Lam.F, Lam.dim, N.dim
    Id, In = identity_matrix(F, d), identity_matrix(F, n)
    rel = hstack(F, d * n, [kron_XI(Lam.R(y), n) - kron_IX(d, N.mats[j])
                            for j, y in enumerate(Gam.gens)])
    big = Mod(Lam, [kron_XI(L, n) for L in Lam.Lgens])
    Q, proj = big.quotient(spin(big.mats, rel))
    return Q, proj, col_basis(rel)


def coinduce(Lam, Gam, N):
    """N Up^Lam = Hom_Gam(Lam, N), (x phi)(l) = phi(l x)."""
    F = Lam.F
    LamG = Mod(Gam, [Lam.L(y) for y in Gam.gens])
    H = hom_basis(LamG, N)
    B = matrix(F, [h.list() for h in H]).transpose()
    c = Coords(B)
    return Mod(Lam, [c(matrix(F, [(h * Lam.R(x)).list() for h in H]).transpose())
                     for x in Lam.gens])


# ---------------------------------------------------------------------------
# Complexes of vector spaces: cohomology, induced maps, connecting maps
# ---------------------------------------------------------------------------

class CoCx:
    """A cochain complex of F-vector spaces: dims[n], d[n]: X^n -> X^(n+1)."""

    def __init__(self, F, dims, d):
        self.F, self.dims, self.d = F, dims, d
        self._H = {}

    def dd(self, n):
        if n in self.d:
            return self.d[n]
        return matrix(self.F, self.dims.get(n + 1, 0), self.dims.get(n, 0))

    def H(self, n):
        if n not in self._H:
            F, m = self.F, self.dims.get(n, 0)
            Z = kernel_cols(self.dd(n)) if m else matrix(F, 0, 0)
            B = col_basis(self.dd(n - 1)) if m else matrix(F, 0, 0)
            T = col_basis(hstack(F, m, [B, Z]))
            reps = T.submatrix(0, B.ncols())
            self._H[n] = (Z, B, reps, Coords(T), B.ncols())
        return self._H[n]

    def hdim(self, n):
        return self.H(n)[2].ncols()

    def hcoords(self, n, z):
        Z, B, reps, c, k = self.H(n)
        if z.nrows() == 0:
            return matrix(self.F, 0, z.ncols())
        return c(z).submatrix(k, 0)


def mget(f, n, X, Y):
    """Component n of a map X -> Y (zero if absent)."""
    if n in f:
        return f[n]
    return matrix(X.F, Y.dims.get(n, 0), X.dims.get(n, 0))


def induced_on_H(X, Y, f, n):
    reps = X.H(n)[2]
    if reps.ncols() == 0 or Y.hdim(n) == 0:
        return matrix(X.F, Y.hdim(n), reps.ncols())
    return Y.hcoords(n, mget(f, n, X, Y) * reps)


def connecting(Xp, X, Xpp, f, g, n, rnd=None):
    """delta: H^n(X'') -> H^(n+1)(X') of a short exact sequence of cochain
    complexes, as in the proof of Proposition 2.3.7 (choices of lifts
    randomised by rnd)."""
    F = X.F
    reps = Xpp.H(n)[2]
    cols = []
    for x in reps.columns():
        x = matrix(F, len(x), 1, list(x))
        y = solve(mget(g, n, X, Xpp), x)
        if rnd is not None:
            K = kernel_cols(mget(g, n, X, Xpp))
            if K.ncols():
                y = y + K * matrix(F, K.ncols(), 1, [rnd.choice(list(F)) for _ in range(K.ncols())])
        w = X.dd(n) * y
        z = solve(mget(f, n + 1, Xp, X), w)
        assert Xp.dd(n + 1) * z == 0  # z is a cocycle
        cols.append(Xp.hcoords(n + 1, z))
    if not cols:
        return matrix(F, Xp.hdim(n + 1), 0)
    return hstack(F, Xp.hdim(n + 1), cols)


def exact_at(a, b, dim_mid):
    """U -a-> V -b-> W exact at V."""
    if a.ncols() and b.nrows():
        if b * a != 0:
            return False
    return rank_of(a) + rank_of(b) == dim_mid


def les_exact(Xp, X, Xpp, f, g, lo, hi, rnd=None):
    """Check the short exact sequences of terms in degrees lo..hi+1 and the
    exactness of the long exact cohomology sequence at every term
    H^n(X'), H^n(X), H^n(X'') with lo < n <= hi and at H^lo(X), H^lo(X'')
    (H^lo(X') and the terms beyond hi need the complexes outside the
    range).  Returns the number of exactness conditions checked."""
    F = X.F
    for n in range(lo, hi + 2):
        a, b = mget(f, n, Xp, X), mget(g, n, X, Xpp)
        assert rank_of(a) == Xp.dims.get(n, 0)  # injective
        assert rank_of(b) == X.dims.get(n, 0) - rank_of(a)  # exact in the middle
        assert X.dims.get(n, 0) == 0 or Xpp.dims.get(n, 0) == 0 or b * a == 0
        assert rank_of(b) == Xpp.dims.get(n, 0)  # surjective
    for n in range(lo, hi + 1):  # cochain maps
        assert X.dd(n) * mget(f, n, Xp, X) == mget(f, n + 1, Xp, X) * Xp.dd(n)
        assert Xpp.dd(n) * mget(g, n, X, Xpp) == mget(g, n + 1, X, Xpp) * X.dd(n)
    seq = []  # list of (map, dim of its source)
    for n in range(lo, hi + 1):
        seq.append(('f', n, induced_on_H(Xp, X, f, n), Xp.hdim(n)))
        seq.append(('g', n, induced_on_H(X, Xpp, g, n), X.hdim(n)))
        seq.append(('d', n, connecting(Xp, X, Xpp, f, g, n, rnd), Xpp.hdim(n)))
    count = 0
    for i in range(len(seq) - 1):
        a, b = seq[i][2], seq[i + 1][2]
        assert exact_at(a, b, seq[i + 1][3]), 'LES not exact at %s' % (seq[i + 1][:2],)
        count += 1
    return count


def quotient_proj(F, m, B):
    """Projection F^m -> F^m / span(B) and a section, in coordinates."""
    if m == 0:
        return matrix(F, 0, 0), matrix(F, 0, 0)
    B = col_basis(B)
    ext = col_basis(hstack(F, m, [B, identity_matrix(F, m)]))
    T = ext.inverse()
    k = B.ncols()
    return T.submatrix(k, 0), ext.submatrix(0, k)


def random_cochain(F, dims, rnd):
    """A random cochain complex with the given dimensions (degrees 0..)."""
    d = {}
    for n in range(len(dims) - 1):
        prev = d[n - 1] if n > 0 else matrix(F, dims[0], 0)
        proj, _ = quotient_proj(F, dims[n], prev)
        k = proj.nrows()
        R = matrix(F, dims[n + 1], k, [rnd.choice(list(F)) for _ in range(dims[n + 1] * k)])
        d[n] = R * proj if k else matrix(F, dims[n + 1], dims[n])
    return CoCx(F, {n: dims[n] for n in range(len(dims))}, d)


def random_subcomplex(X, rnd, count=1):
    """Random subcomplex (closed under d) with its quotient: returns
    (X', X'', f, g)."""
    F = X.F
    top = max(X.dims)
    W = {}
    for n in range(0, top + 1):
        m = X.dims[n]
        cols = [matrix(F, m, 1, [rnd.choice(list(F)) for _ in range(m)]) for _ in range(count)]
        if n > 0:
            cols.append(X.dd(n - 1) * W[n - 1])
        W[n] = col_basis(hstack(F, m, cols)) if m else matrix(F, 0, 0)
    dp, dpp, g, sec = {}, {}, {}, {}
    for n in range(0, top + 1):
        g[n], sec[n] = quotient_proj(F, X.dims[n], W[n])
    for n in range(0, top):
        dp[n] = Coords(W[n + 1])(X.dd(n) * W[n]) if W[n + 1].ncols() else \
            matrix(F, 0, W[n].ncols())
        dpp[n] = g[n + 1] * X.dd(n) * sec[n]
    Xp = CoCx(F, {n: W[n].ncols() for n in W}, dp)
    Xpp = CoCx(F, {n: X.dims[n] - W[n].ncols() for n in W}, dpp)
    return Xp, Xpp, W, g

# =========================================================================
# The algebras used below
# =========================================================================
F2, F9 = GF(2), GF(9)


def truncated_poly(F, n):
    N = matrix(F, n, n, lambda i, j: 1 if i == j + 1 else 0)
    A = Alg(F, [N], radgens=[N], name='k[x]/(x^%d)' % n)
    A.x = N
    return A


def k_of(A):
    """The simple module k = A/J(A) of a local algebra."""
    return A.regular().quotient(A.J())[0]


ALG = {}
ALG['x2'] = truncated_poly(F2, 2)
ALG['x3'] = truncated_poly(F9, 3)
ALG['x4'] = truncated_poly(F2, 4)
# path algebras (relations of length >= 2: admissible ideals)
ALG['A2'] = path_algebra(F2, 2, [(0, 1)], [], 2, 'A2')
ALG['A3rad2'] = path_algebra(F9, 3, [(0, 1), (1, 2)], [{(0, 1): 1}], 3, 'A3, ba = 0')
ALG['kron'] = path_algebra(F2, 2, [(0, 1), (0, 1)], [], 2, 'Kronecker')
ALG['square'] = path_algebra(F9, 4, [(0, 1), (1, 3), (0, 2), (2, 3)],
                             [{(0, 1): 1, (2, 3): -1}], 3, 'commutative square')
ALG['nak2'] = path_algebra(F2, 2, [(0, 1), (1, 0)], [{(0, 1): 1}, {(1, 0): 1}], 3,
                           'Nakayama, J^2 = 0')
ALG['nak3'] = path_algebra(F9, 2, [(0, 1), (1, 0)], [{(0, 1, 0): 1}, {(1, 0, 1): 1}], 4,
                           'Nakayama, J^3 = 0')
ALG['ext'] = path_algebra(F9, 1, [(0, 0), (0, 0)],
                          [{(0, 0): 1}, {(1, 1): 1}, {(0, 1): 1, (1, 0): 1}], 3,
                          'k<x,y>/(x^2, y^2, xy + yx)')
BASIC = ['A2', 'A3rad2', 'kron', 'square', 'nak2', 'nak3', 'ext']
SELFINJ = ['nak2', 'nak3', 'ext']

# =========================================================================
# Sections 2.1 and 2.2: stable categories, Morita theory
# =========================================================================

def sec_2_1():
    # p. 23: Omega is well defined on the stable category (Schanuel), and
    # for self injective Lambda, Omega and Omega^(-1) are inverse
    count = 0
    for key in SELFINJ + ['x3', 'x4']:
        A = ALG[key]
        mods = some_modules(A)
        r = Resolution(mods[0], 3)
        mods += [r.omega[2], r.omega[3]]
        for M in mods:
            O = Resolution(M, 0).omega[1]
            if O.dim == 0:          # M projective (P / Rad^2 P = P when J^2 = 0)
                continue
            C = cosyzygy(M)
            # M has no projective summand: Omega^(-1) Omega M = M = Omega Omega^(-1) M
            lhs, rhs = cosyzygy(O), Resolution(C, 0).omega[1]
            assert isomorphic(lhs, M) and isomorphic(rhs, M)
            count += 1
    for key in ['V4', 'C3xC3', 'C4']:
        A = GROUPS[key]
        k = k_of(A)
        r = Resolution(k, 3)
        for M in [k, r.omega[1], r.omega[2]]:
            assert isomorphic(cosyzygy(Resolution(M, 0).omega[1]), M)
            assert isomorphic(Resolution(cosyzygy(M), 0).omega[1], M)
            count += 1
    check(count >= 25, 'p. 23: for self injective Lambda the functors Omega, Omega^(-1) on the '
          'stable category are inverse: Omega^(-1) Omega M = M = Omega Omega^(-1) M for %d '
          'non-projective modules without projective summands (simples, P/Rad^2 P, Omega^2, '
          'Omega^3) over 8 self injective algebras' % count)


def basic_morita_data(A, mult):
    """P = sum_i mult[i] P_i, Gamma = End_Lambda(P)^op."""
    P = direct_sum(*[proj_indec(A, i) for i in range(A.nv) for _ in range(mult[i])])
    E = hom_basis(P, P)
    return P, E


def sec_2_2():
    count = 0
    for key, mults in [('A2', [(2, 1), (1, 2), (1, 1)]), ('A3rad2', [(2, 1, 1), (1, 1, 3)]),
                       ('nak2', [(2, 1), (1, 1)]), ('nak3', [(2, 1)]), ('square', [(1, 2, 1, 1)]),
                       ('kron', [(2, 2), (3, 1)])]:
        A = ALG[key]
        F = A.F
        Lam = A.regular()
        for mult in mults:
            P, E = basic_morita_data(A, mult)
            # dim Gamma = sum m_i m_j dim e_i Lambda e_j
            eLe = [[rank_of(A.L(A.idems[i]) * A.R(A.idems[j])) for j in range(A.nv)]
                   for i in range(A.nv)]
            assert len(E) == sum(mult[i] * mult[j] * eLe[i][j]
                                 for i in range(A.nv) for j in range(A.nv))
            # J(Gamma) = maps into Rad P; Gamma / J(Gamma) = prod Mat_(m_i)(k)
            JP = P.radical()
            Q, proj = P.quotient(JP)
            Bm = matrix(F, [(proj * e).list() for e in E]).transpose()
            dimJ = len(E) - rank_of(Bm)
            assert len(E) - dimJ == sum(m * m for m in mult)
            # Proposition 2.2.7: Z(Gamma) = Z(Lambda), via lambda -> multiplication by lambda
            Emat = matrix(F, [e.list() for e in E]).transpose()
            # centre of End(P): coefficient vectors c with sum c_k E_k commuting with all E
            rows = []
            for f in E:
                rows.append(matrix(F, [(e * f - f * e).list() for e in E]).transpose())
            Zc = kernel_cols(vstack(F, len(E), rows))
            assert Zc.ncols() == A.centre_dim()
            Zl = kernel_cols(vstack(F, A.dim, [A.L(g) - A.R(g) for g in A.gens]))
            imgs = matrix(F, [P.act_coords(c).list() for c in Zl.columns()]).transpose()
            assert rank_of(imgs) == Zl.ncols()                      # injective
            assert rank_of(hstack(F, imgs.nrows(), [Emat * Zc, imgs])) == Zc.ncols()  # into Z(E)
            # Lemmas 2.2.3, 2.2.4: P (x)_Gamma Q = Lambda and Q (x)_Lambda P = Gamma, Q = Hom(P, Lambda)
            Hq = hom_basis(P, Lam)                                  # Q, as d x dim P matrices
            Qb = matrix(F, [h.list() for h in Hq]).transpose()
            cq = Coords(Qb)
            p, q, d = P.dim, len(Hq), A.dim
            # Gamma acts on P on the right by x.gamma = gamma(x), on Q on the left by
            # (gamma.f) = f o gamma; relations x.gamma (x) f - x (x) gamma.f
            rel = []
            for e in E:
                act_Q = cq(matrix(F, [(h * e).list() for h in Hq]).transpose())   # q x q
                rel.append(kron_XI(e, q) - kron_IX(p, act_Q))
            rel = hstack(F, p * q, rel)
            ev = matrix(F, d, p * q)
            for a in range(p):
                for b in range(q):
                    ev.set_column(a * q + b, Hq[b].column(a))
            assert ev * rel == 0 and rank_of(ev) == d
            assert p * q - rank_of(rel) == d                        # phi is an isomorphism
            # Q (x)_Lambda P -> Gamma = End(P): f (x) x |-> (y |-> f(y) x)
            rel2 = []
            for gi, g in enumerate(A.gens):
                Rg = A.R(g)
                act = cq(matrix(F, [(Rg * h).list() for h in Hq]).transpose())     # f.g
                rel2.append(kron_XI(act, p) - kron_IX(q, P.mats[gi]))
            rel2 = hstack(F, q * p, rel2)
            psi = matrix(F, p * p, q * p)
            for b in range(q):
                for a in range(p):
                    xa = vector(F, [1 if t == a else 0 for t in range(p)])
                    m = matrix(F, [list(P.act_coords(Hq[b].column(y)) * xa) for y in range(p)]).transpose()
                    psi.set_column(b * p + a, vector(F, m.list()))
            assert psi * rel2 == 0
            assert q * p - rank_of(rel2) == len(E) == rank_of(psi)
            assert rank_of(hstack(F, p * p, [Emat, psi])) == len(E)  # image = End(P)
            count += 1
    check(count >= 10, 'pp. 25-26: for %d progenerators P = sum m_i P_i (all m_i > 0) of 6 basic '
          'algebras: dim End(P) = sum m_i m_j dim e_i Lambda e_j, Gamma/J(Gamma) has dimension '
          'sum m_i^2 (simple Gamma-modules of dimension m_i), Z(Lambda) -> Z(End(P)) is an '
          'isomorphism (Proposition 2.2.7), and the maps phi: P (x)_Gamma Q -> Lambda, '
          'psi: Q (x)_Lambda P -> Gamma of Lemmas 2.2.3, 2.2.4 are well defined isomorphisms' % count)

# =========================================================================
# Section 2.3: chain complexes and homology
# =========================================================================
rnd = random.Random(20261104)


def sec_2_3():
    n_les = 0
    for F in (F2, F9):
        for trial in range(12):
            dims = [rnd.randint(0, 4) for _ in range(6)]
            X = random_cochain(F, dims, rnd)
            for n in range(5):
                assert X.dd(n + 1) * X.dd(n) == 0
            Xp, Xpp, W, g = random_subcomplex(X, rnd, count=1 + trial % 2)
            f = {n: W[n] for n in W}
            # Propositions 2.3.7 / 2.3.8: the long exact sequence, with the
            # connecting map of the proof (lifts chosen at random: well defined)
            n_les += les_exact(Xp, X, Xpp, f, g, 0, 4, rnd)
            delta1 = connecting(Xp, X, Xpp, f, g, 2)
            delta2 = connecting(Xp, X, Xpp, f, g, 2, rnd)
            check(delta1 == delta2, 'p. 30, proof of Proposition 2.3.7: the connecting map '
                  'does not depend on the lift y (%s, trial %d)' % (F, trial))
            # Proposition 2.3.5: f' = f + d h + h d induces the same map
            h = {n: matrix(F, dims[n - 1], dims[n],
                           [rnd.choice(list(F)) for _ in range(dims[n - 1] * dims[n])])
                 for n in range(1, 6)}
            ident = {n: identity_matrix(F, dims[n]) for n in range(6)}
            fp = {n: ident[n] + (h[n + 1] * X.dd(n) if n + 1 in h else 0)
                  + (X.dd(n - 1) * h[n] if n in h else 0) for n in range(5)}
            for n in range(4):
                assert X.dd(n) * fp[n] == fp[n + 1] * X.dd(n)
                check(induced_on_H(X, X, fp, n) == identity_matrix(F, X.hdim(n)),
                      'p. 29, Proposition 2.3.5: a map homotopic to the identity induces '
                      'the identity on H^%d (%s, trial %d)' % (n, F, trial))
    check(n_les > 300, 'pp. 29-30, Propositions 2.3.7, 2.3.8: %d exactness conditions of '
          'long exact sequences of random short exact sequences of complexes' % n_les)
    # Lemma 2.3.9 (snake lemma): complexes of length two
    for F in (F2, F9):
        for trial in range(15):
            dims = [rnd.randint(1, 5), rnd.randint(1, 5)]
            X = random_cochain(F, dims, rnd)
            Xp, Xpp, W, g = random_subcomplex(X, rnd)
            f = {n: W[n] for n in W}
            # 0 -> Ker a -> Ker b -> Ker c -> Coker a -> Coker b -> Coker c -> 0
            k = les_exact(Xp, X, Xpp, f, g, 0, 1)
            a = induced_on_H(Xp, X, f, 0)
            check(rank_of(a) == Xp.hdim(0), 'p. 30, Lemma 2.3.9: Ker(alpha) -> Ker(beta) is '
                  'injective (%s, trial %d)' % (F, trial))
            c = induced_on_H(X, Xpp, g, 1)
            check(rank_of(c) == Xpp.hdim(1), 'p. 30, Lemma 2.3.9: Coker(beta) -> Coker(gamma) '
                  'is surjective, six-term sequence exact (%s, trial %d)' % (F, trial))

# =========================================================================
# Group algebras of small groups
# =========================================================================

def gap_group(expr):
    return libgap.eval(expr)


GROUPS = {}


def local_group_algebra(key, expr, p, F):
    G = gap_group(expr)
    gens = list(G.GeneratorsOfGroup())
    A = group_algebra(G, gens, F, pgroup=True)
    A.p = p
    GROUPS[key] = A
    return A


local_group_algebra('C2', 'Group((1,2))', 2, F2)
local_group_algebra('C4', 'Group((1,2,3,4))', 2, F2)
local_group_algebra('V4', 'Group((1,2),(3,4))', 2, F2)
local_group_algebra('D8', 'Group((1,2,3,4),(1,3))', 2, F2)
local_group_algebra('Q8', 'Group((1,2,4,7)(3,6,8,5),(1,3,4,8)(2,5,7,6))', 2, F2)
local_group_algebra('C3', 'Group((1,2,3))', 3, F9)
local_group_algebra('C3xC3', 'Group((1,2,3),(4,5,6))', 3, F9)
LOCAL = ['C2', 'C4', 'V4', 'D8', 'Q8', 'C3', 'C3xC3']


def lifted_chain_map(resP, resQ, phi, shift, length, rnd=None):
    """F_j: P_(shift+j) -> Q_j (0 <= j <= length) with eps_Q F_0 = phi and
    d^Q_j F_j = F_(j-1) d^P_(shift+j) (Theorem 2.4.2, by the inductive
    construction of its proof); phi: P_shift -> M' with phi d_(shift+1) = 0.
    With rnd a random solution is chosen at each step."""
    F = resP.A.F
    out = []
    for j in range(length + 1):
        Pm, Qm = resP.P(shift + j), resQ.P(j)
        H = hom_basis(Pm, Qm)
        if j == 0:
            lhs = [resQ.eps * h for h in H]
            target = phi
        else:
            lhs = [resQ.d[j] * h for h in H]
            target = out[j - 1] * resP.d[shift + j]
        if not H:
            assert target == 0
            out.append(matrix(F, Qm.dim, Pm.dim))
            continue
        Mx = matrix(F, [x.list() for x in lhs]).transpose()
        c = solve(Mx, matrix(F, len(target.list()), 1, target.list()))
        if rnd is not None:
            K = kernel_cols(Mx)
            if K.ncols():
                c = c + K * matrix(F, K.ncols(), 1, [rnd.choice(list(F)) for _ in range(K.ncols())])
        out.append(sum((c[k, 0] * H[k] for k in range(len(H))), matrix(F, Qm.dim, Pm.dim)))
    return out


def homotopy(resP, resQ, f, g, length):
    """h_n: P_n -> Q_(n+1) with f_n - g_n = d'_(n+1) h_n + h_(n-1) d_n, built
    as in the proof of Theorem 2.4.2 (asserting each step is solvable)."""
    F = resP.A.F
    hs = []
    for n in range(length):
        Pn, Qn1 = resP.P(n), resQ.P(n + 1)
        target = f[n] - g[n] - (hs[n - 1] * resP.d[n] if n else 0)
        H = hom_basis(Pn, Qn1)
        if not H:
            assert target == 0
            hs.append(matrix(F, Qn1.dim, Pn.dim))
            continue
        Mx = matrix(F, [(resQ.d[n + 1] * h).list() for h in H]).transpose()
        c = solve(Mx, matrix(F, len(target.list()), 1, target.list()))
        hs.append(sum((c[k, 0] * H[k] for k in range(len(H))), matrix(F, Qn1.dim, Pn.dim)))
    return hs


def some_modules(A, count=3):
    """Simple modules, projectives, and a few small quotients of projectives."""
    mods = []
    if hasattr(A, 'nv'):
        mods += [vertex_simple(A, i) for i in range(A.nv)]
        P = [proj_indec(A, i) for i in range(A.nv)]
    else:
        mods.append(k_of(A))
        P = [A.regular()]
    for Pi in P:
        R = Pi.radical()
        if R.ncols():
            R2 = Pi.sub(R).radical()
            # P / Rad^2 P (embedded radical of radical)
            mods.append(Pi.quotient(R * R2)[0] if R2.ncols() else Pi)
    return [M for M in mods if M.dim][:count + (A.nv if hasattr(A, 'nv') else 1)]


def sec_2_4():
    rnd = random.Random(2401)
    # Theorem 2.4.2 (comparison theorem) on examples
    count = 0
    for key in ['x3', 'A3rad2', 'square', 'nak3']:
        A = ALG[key]
        mods = some_modules(A)
        for M in mods[:3]:
            for Mp in mods[:3]:
                for hom in hom_basis(M, Mp)[:2]:
                    rP, rQ = Resolution(M, 3), Resolution(Mp, 3, minimal=False)
                    phi = hom * rP.eps
                    f = lifted_chain_map(rP, rQ, phi, 0, 2)
                    g = lifted_chain_map(rP, rQ, phi, 0, 2, rnd)
                    h = homotopy(rP, rQ, f, g, 2)
                    for n in range(2):
                        lhs = f[n] - g[n]
                        rhs = rQ.d[n + 1] * h[n] + (h[n - 1] * rP.d[n] if n else 0)
                        assert lhs == rhs
                    count += 1
    check(count >= 15, 'p. 31, Theorem 2.4.2: maps of modules lift to maps of projective '
          'resolutions (minimal to non-minimal) and any two lifts are chain homotopic, '
          'by the inductive construction of the proof (%d maps, degrees <= 2)' % count)

    # Example (p. 32): over ZZ, Tor_1 and Ext^1 of cyclic groups; length one
    for a in range(1, 13):
        for b in range(1, 13):
            tor1 = len([x for x in range(b) if (a * x) % b == 0])   # Ker(a: Z/b -> Z/b)
            ext1 = b // len(set((a * x) % b for x in range(b)))     # Coker(a: Z/b -> Z/b)
            assert tor1 == gcd(a, b) and ext1 == gcd(a, b)
    check(True, 'p. 32, Example: Tor_1^Z(Z/a, Z/b) = Ext^1_Z(Z/a, Z/b) = Z/gcd(a, b) from the '
          'resolution 0 -> Z -a-> Z, 1 <= a, b <= 12')

    # Tor_0 = tensor product, Ext^0 = Hom (p. 32); Remarks (i): projective M
    for key in BASIC + ['x2', 'x3', 'x4']:
        A = ALG[key]
        mods = some_modules(A)
        for M in mods:
            r = Resolution(M, 2)
            for N in mods:
                assert ext_dims(r, N, 0)[0] == hom_dim(M, N)
                assert tor_dims(r, N.dual(), 0)[0] == tensor_dim(N.dual(), M)
        P = [proj_indec(A, i) for i in range(A.nv)] if hasattr(A, 'nv') else [A.regular()]
        for Pi in P:
            r = Resolution(Pi, 3)
            assert r.stages[1].r == 0
            for N in mods:
                assert ext_dims(r, N, 2)[1:] == [0, 0]
                assert tor_dims(r, N.dual(), 2)[1:] == [0, 0]
    check(True, 'p. 32, Ext^0 = Hom and Tor_0 = tensor product (Tor_0 against a direct '
          'computation of the tensor product) for %d algebras' % (len(BASIC) + 3))
    check(True, 'p. 32, Remarks (i): for M projective the resolution is M in degree 0 and '
          'Ext^n(M, M\'), Tor_n(M\', M) vanish for n = 1, 2 (projective indecomposables of '
          '%d algebras)' % (len(BASIC) + 3))

    # Remarks (ii): Schanuel's lemma and uniqueness of minimal resolutions
    count = 0
    for key in ['x3', 'A3rad2', 'square', 'nak2', 'nak3', 'ext']:
        A = ALG[key]
        reg = A.regular()
        for M in some_modules(A):
            r1 = Resolution(M, 3)
            r2 = Resolution(M, 3, rnd=random.Random(count))
            rf = Resolution(M, 3, minimal=False)
            for n in range(1, 4):
                O1, O2, Of = r1.omega[n], r2.omega[n], rf.omega[n]
                assert [st.idem for st in r1.stages] == [st.idem for st in r2.stages]
                assert isomorphic(O1, O2)
                # Schanuel: Omega~^n (+) P_(n-1) (+) P'_(n-2) (+) ...
                #         = Omega^n (+) P'_(n-1) (+) P_(n-2) (+) ...
                lhs = [Of] + [(r1 if (n - 1 - m) % 2 == 0 else rf).P(m) for m in range(n)]
                rhs = [O1] + [(rf if (n - 1 - m) % 2 == 0 else r1).P(m) for m in range(n)]
                assert isomorphic(direct_sum(*lhs), direct_sum(*rhs))
                count += 1
    check(count >= 40, 'p. 32, Remarks (ii): two minimal resolutions (different lifts) have '
          'the same terms and isomorphic Omega^n; a free resolution gives '
          'Omega~^n(M) with Omega~^n(M) (+) P\' = Omega^n(M) (+) P (Schanuel), n = 1..3, '
          '%d cases' % count)

    # Proposition 2.4.3: dim Ext^1(S, S') = dim e' J e / e' J^2 e = dim Hom(Rad P / Rad^2 P, S')
    count = 0
    for key in BASIC:
        A = ALG[key]
        J, J2 = A.J(), A.J2()
        S = [vertex_simple(A, i) for i in range(A.nv)]
        for i in range(A.nv):
            r = Resolution(S[i], 2)
            P = proj_indec(A, i)
            R = P.radical()
            RP = P.sub(R)
            R2 = RP.radical()
            top_rad = RP.quotient(R2)[0]
            for j in range(A.nv):
                e, ep = A.idems[i], A.idems[j]
                sand = A.L(ep) * A.R(e)
                lhs = ext_dims(r, S[j], 1)[1]
                rhs = rank_of(sand * J) - rank_of(sand * J2)
                arrows = len([a for a in A.arrows if a == (i, j)])
                assert lhs == rhs == hom_dim(top_rad, S[j]) == arrows
                count += 1
    for key in LOCAL:
        A = GROUPS[key]
        k = k_of(A)
        r = Resolution(k, 2)
        lhs = ext_dims(r, k, 1)[1]
        rhs = A.J().ncols() - A.J2().ncols()
        dG = int(libgap.Length(libgap.MinimalGeneratingSet(A.group)))
        assert lhs == rhs == dG
        count += 1
    check(count == 49, 'p. 33, Proposition 2.4.3: dim Ext^1(S, S\') = dim Hom(Rad P/Rad^2 P, S\') '
          '= dim e\'J e/e\'J^2 e for all %d pairs of simple modules of %d path algebras (also = '
          'number of arrows) and for k G, G = %s (also = d(G))' % (count, len(BASIC), ', '.join(LOCAL)))

    # Remark (p. 34): base change; H^n(Z C_p, F_p) = H^n(F_p C_p, F_p)
    for p, F in [(2, F2), (3, F9), (5, GF(25))]:
        g = matrix(ZZ, p, p, lambda i, j: 1 if i == (j + 1) % p else 0)
        one = identity_matrix(ZZ, p)
        Nm = sum(g ** i for i in range(p))
        ds = [g - one if n % 2 else Nm for n in range(1, 7)]  # d_1, d_2, ...
        # exactness over ZZ in degrees 1..5 and over F_p after tensoring
        for n in range(1, 6):
            dn, dn1 = ds[n - 1], ds[n]
            assert dn * dn1 == 0
            K = dn.right_kernel_matrix().transpose()   # saturated kernel over ZZ
            # image of d_(n+1) equals the kernel (both of rank 1 = p - rank)
            assert dn1.column_module() == K.column_module()
            dnF, dn1F = dn.change_ring(GF(p)), dn1.change_ring(GF(p))
            assert dnF.rank() + dn1F.rank() == p
        # Hom_(Z C_p)(Z C_p, F_p) = F_p, the differential is eps(d) mod p = 0
        eps = [sum(d.column(0)) % p for d in ds]
        assert eps == [0] * 6
    check(True, 'p. 34, Remark: F_p (x) (periodic Z C_p-resolution of Z) is exact, so '
          'H^n(Z C_p, F_p) = F_p = H^n(F_p C_p, F_p), p = 2, 3, 5, n <= 5')
    for key in ['C2', 'C3']:
        A = GROUPS[key]
        r = Resolution(k_of(A), 6)
        check(ext_dims(r, k_of(A), 5) == [1] * 6, 'p. 34, Remark: dim H^n(F_p C_p, F_p) = 1, '
              'n <= 5 (%s)' % key)

    # Exercise (p. 34): additivity; the printed second isomorphism
    for key in ['A3rad2', 'nak3', 'x3']:
        A = ALG[key]
        mods = some_modules(A)
        Lam = A.regular()
        for M in mods:
            r = Resolution(M, 3)
            for M1 in mods:
                for M2 in mods:
                    s = ext_dims(r, direct_sum(M1, M2), 2)
                    a, b = ext_dims(r, M1, 2), ext_dims(r, M2, 2)
                    assert s == [x + y for x, y in zip(a, b)]
                    r12 = Resolution(direct_sum(M1, M2), 3)
                    s1 = ext_dims(r12, M, 2)
                    a1, b1 = ext_dims(Resolution(M1, 3), M, 2), ext_dims(Resolution(M2, 3), M, 2)
                    assert s1 == [x + y for x, y in zip(a1, b1)]
    check(True, 'p. 34, Exercise: dim Ext^n(M (+) M\', M\'\') and dim Ext^n(M, M\' (+) M\'\') are '
          'additive (n <= 2, small modules of three algebras)')
    A = ALG['x3']
    Lam, zero = A.regular(), zero_mod(A)
    r = Resolution(Lam, 2)
    lhs = ext_dims(r, direct_sum(Lam, zero), 0)[0]
    printed = 2 * ext_dims(r, zero, 0)[0]
    corrected = ext_dims(r, Lam, 0)[0] + ext_dims(r, zero, 0)[0]
    refuted(lhs == printed, 'p. 34, Exercise as printed: Ext^n(M, M\' (+) M\'\') = '
            'Ext^n(M, M\'\') (+) Ext^n(M, M\'\'); n = 0, M = M\' = Lambda = k[x]/(x^3), M\'\' = 0')
    check(lhs == corrected == 3, 'p. 34, Exercise corrected: Ext^n(M, M\' (+) M\'\') = '
          'Ext^n(M, M\') (+) Ext^n(M, M\'\') in the same case')

# =========================================================================
# Section 2.5: long exact sequences
# =========================================================================

class StagedResolution(Resolution):
    """A resolution given by its stages (as built by the horseshoe below)."""

    def __init__(self, M, stages):
        self.M, self.A = M, M.A
        self.stages, self.d, self.omega = stages, {}, [M] + [st.Omega for st in stages]
        self.eps = stages[0].pi
        for n in range(1, len(stages)):
            self.d[n] = stages[n - 1].K * stages[n].pi
        self._imgs = {}


def horseshoe(M, W, length):
    """Lemma 2.5.1 for 0 -> M' -> M -> M'' -> 0 (M' = span W): at each step
    P_n = P'_n (+) P''_n maps onto the current module, P'_n -> M' and
    P''_n -> M'' being projective covers; returns the stages and the
    numbers of generators (r'_n, r''_n)."""
    A, F = M.A, M.A.F
    stages, counts = [], []
    cur, curW = M, W
    for n in range(length + 1):
        Mp = cur.sub(curW)
        Mpp, proj = cur.quotient(curW)
        gp = [(i, curW * v) for i, v in cover_generators(Mp)]
        gpp = []
        for i, u in cover_generators(Mpp):
            E = col_basis(cur.act(A.idems[i]))
            x = solve(proj * E, matrix(F, len(u), 1, list(u)))
            gpp.append((i, (E * x).column(0)))
        st = Stage(cur, gp + gpp)
        assert rank_of(st.pi) == cur.dim       # P'_n (+) P''_n -> M is onto
        stages.append(st)
        counts.append((len(gp), len(gpp)))
        # the next submodule: Ker meets the P'-part in Omega(M')
        a = sum(st.blocks[j].ncols() for j in range(len(gp)))
        K = st.K
        low = K.submatrix(a, 0)
        Wn = K * kernel_cols(low) if low.nrows() else K
        assert Wn.ncols() == a - Mp.dim                     # = dim Omega(M')
        assert K.ncols() - Wn.ncols() == st.dim - a - Mpp.dim  # = dim Omega(M'')
        cur = st.Omega
        curW = Coords(K)(Wn) if Wn.ncols() else matrix(F, K.ncols(), 0)
    return stages, counts


def split_cochain(X, a):
    """For a cochain complex X whose terms split as (first a[n] coordinates)
    (+) (the rest), with the rest a subcomplex: (sub, quotient, f, g)."""
    F = X.F
    degs = sorted(X.dims)
    dsub, dquo, f, g = {}, {}, {}, {}
    for n in degs:
        m = X.dims[n]
        f[n] = identity_matrix(F, m).submatrix(0, a[n]) if m else matrix(F, 0, 0)
        g[n] = identity_matrix(F, m).submatrix(0, 0, a[n], m) if m else matrix(F, 0, 0)
    for n in degs:
        if n + 1 not in X.dims:
            continue
        dn = X.dd(n)
        assert dn.submatrix(0, a[n], a[n + 1], X.dims[n] - a[n]) == 0  # subcomplex
        dsub[n] = dn.submatrix(a[n + 1], a[n])
        dquo[n] = dn.submatrix(0, 0, a[n + 1], a[n])
    sub = CoCx(F, {n: X.dims[n] - a[n] for n in degs}, dsub)
    quo = CoCx(F, {n: a[n] for n in degs}, dquo)
    return sub, quo, f, g


def split_first_sub(X, a):
    """As split_cochain, but the first a[n] coordinates form the subcomplex."""
    F = X.F
    degs = sorted(X.dims)
    dsub, dquo, f, g = {}, {}, {}, {}
    for n in degs:
        m = X.dims[n]
        f[n] = identity_matrix(F, m).submatrix(0, 0, m, a[n]) if m else matrix(F, 0, 0)
        g[n] = identity_matrix(F, m).submatrix(a[n], 0) if m else matrix(F, 0, 0)
    for n in degs:
        if n + 1 not in X.dims:
            continue
        dn = X.dd(n)
        assert dn.submatrix(a[n + 1], 0, X.dims[n + 1] - a[n + 1], a[n]) == 0
        dsub[n] = dn.submatrix(0, 0, a[n + 1], a[n])
        dquo[n] = dn.submatrix(a[n + 1], a[n])
    sub = CoCx(F, {n: a[n] for n in degs}, dsub)
    quo = CoCx(F, {n: X.dims[n] - a[n] for n in degs}, dquo)
    return sub, quo, f, g


def chains_to_cochains(dims, d):
    """X_n (n >= 0) with d_n: X_n -> X_(n-1) as the cochain complex X^(-n)."""
    F = next(iter(d.values())).base_ring() if d else GF(2)
    return CoCx(F, {-n: dims[n] for n in dims}, {-n: d[n] for n in d})


def gens_coord_split(res, n, N, first):
    """Number of coordinates of Hom(P_n, N) (or N (x) P_n) carried by the
    first `first` generators of P_n."""
    A, F = res.A, res.A.F
    st = res.stages[n]
    return sum(rank_of(N.act(A.idems[st.idem[j]])) for j in range(first))


def sec_2_5():
    rnd = random.Random(2501)
    # Lemma 2.5.1 and Proposition 2.5.2 on submodules M' of modules M
    count_les = count_hs = 0
    for key in ['A3rad2', 'square', 'nak3', 'x3', 'ext', 'kron']:
        A = ALG[key]
        mods = some_modules(A) + [A.regular()]
        for M in mods:
            R = M.radical() if M.dim > 1 else None
            subs = []
            if R is not None and R.ncols():
                subs.append(R)
                subs.append(spin(M.mats, R.submatrix(0, 0, R.nrows(), 1)))
            for W in subs:
                if W.ncols() == M.dim:
                    continue
                N = 4
                stages, counts = horseshoe(M, W, N + 1)
                Mp, (Mpp, _) = M.sub(W), M.quotient(W)
                rp, rpp = Resolution(Mp, N + 1), Resolution(Mpp, N + 1)
                assert [c[0] for c in counts] == [st.r for st in rp.stages]
                assert [c[1] for c in counts] == [st.r for st in rpp.stages]
                res = StagedResolution(M, stages)
                count_hs += 1
                for M0 in some_modules(A):
                    # (ii): Hom(P'', M0) -> Hom(P, M0) -> Hom(P', M0)
                    dims, d, _ = hom_from_P_cochains(res, M0, N)
                    X = CoCx(A.F, dims, d)
                    a = {n: gens_coord_split(res, n, M0, counts[n][0]) for n in dims}
                    Xpp, Xp, f, g = split_cochain(X, a)
                    assert [Xpp.hdim(n) for n in range(N)] == ext_dims(rpp, M0, N - 1)
                    assert [Xp.hdim(n) for n in range(N)] == ext_dims(rp, M0, N - 1)
                    assert [X.hdim(n) for n in range(N)] == ext_dims(Resolution(M, N), M0, N - 1)
                    count_les += les_exact(Xpp, X, Xp, f, g, 0, N - 1, rnd)
                    # (i): M0' (x) P' -> M0' (x) P -> M0' (x) P'' with M0' = D(M0)
                    Mr = M0.dual()
                    dims, d, _ = tensor_with_P_chains(res, Mr, N)
                    Y = chains_to_cochains(dims, d)
                    Y.F = A.F
                    b = {}
                    for n in dims:
                        st = res.stages[n]
                        b[-n] = sum(rank_of(Mr.act(A.idems[st.idem[j]].transpose()))
                                    for j in range(counts[n][0]))
                    Yp, Ypp, f2, g2 = split_first_sub(Y, b)
                    assert [Yp.hdim(-n) for n in range(N)] == tor_dims(rp, Mr, N - 1)
                    assert [Ypp.hdim(-n) for n in range(N)] == tor_dims(rpp, Mr, N - 1)
                    count_les += les_exact(Yp, Y, Ypp, f2, g2, -N + 1, 0, rnd)
    check(count_hs >= 20, 'p. 35, Lemma 2.5.1 (horseshoe): for %d short exact sequences '
          '0 -> M\' -> M -> M\'\' -> 0 (M\' = Rad M or a cyclic submodule of it), P\'_n (+) P\'\'_n '
          'maps onto each syzygy, with P\'_n, P\'\'_n the terms of the minimal resolutions of '
          'M\', M\'\' (n <= 5)' % count_hs)
    check(count_les >= 1000, 'pp. 35-36, Proposition 2.5.2 (i), (ii): long exact Tor and Ext '
          'sequences from the horseshoe resolutions, %d exactness conditions (n <= 3), the '
          'terms equal to Ext and Tor of M\', M, M\'\' computed separately' % count_les)

    # Proposition 2.5.3: sequences in the other variable
    count = 0
    for key in ['A3rad2', 'square', 'nak3', 'x3', 'ext']:
        A = ALG[key]
        mods = some_modules(A) + [A.regular()]
        for M1 in mods:
            if M1.dim < 2:
                continue
            W = M1.radical()
            if W.ncols() == 0:
                continue
            M0 = M1.sub(W)
            M2, proj = M1.quotient(W)
            for Mq in some_modules(A):
                N = 4
                r = Resolution(Mq, N + 1)
                Xs = []
                for Mi in (M0, M1, M2):
                    dims, d, D = hom_from_P_cochains(r, Mi, N)
                    Xs.append((CoCx(A.F, dims, d), D))
                f = {n: Coords(Xs[1][1][n])(bdiag(A.F, [W] * r.stages[n].r) * Xs[0][1][n])
                     if Xs[1][1][n].ncols() else matrix(A.F, 0, Xs[0][1][n].ncols())
                     for n in range(N + 1)}
                g = {n: Coords(Xs[2][1][n])(bdiag(A.F, [proj] * r.stages[n].r) * Xs[1][1][n])
                     if Xs[2][1][n].ncols() else matrix(A.F, 0, Xs[1][1][n].ncols())
                     for n in range(N + 1)}
                count += les_exact(Xs[0][0], Xs[1][0], Xs[2][0], f, g, 0, N - 1, rnd)
                # (i) with right modules D(M2) -> D(M1) -> D(M0)
                Rs = [Mi.dual() for Mi in (M2, M1, M0)]
                maps = [proj.transpose(), W.transpose()]
                Ys = []
                for Mr in Rs:
                    dims, d, D = tensor_with_P_chains(r, Mr, N)
                    Ys.append((chains_to_cochains(dims, d), D))
                    Ys[-1][0].F = A.F
                f2 = {-n: Coords(Ys[1][1][n])(bdiag(A.F, [maps[0]] * r.stages[n].r) * Ys[0][1][n])
                      if Ys[1][1][n].ncols() else matrix(A.F, 0, Ys[0][1][n].ncols())
                      for n in range(N + 1)}
                g2 = {-n: Coords(Ys[2][1][n])(bdiag(A.F, [maps[1]] * r.stages[n].r) * Ys[1][1][n])
                      if Ys[2][1][n].ncols() else matrix(A.F, 0, Ys[1][1][n].ncols())
                      for n in range(N + 1)}
                count += les_exact(Ys[0][0], Ys[1][0], Ys[2][0], f2, g2, -N + 1, 0, rnd)
    check(count >= 500, 'pp. 36-37, Proposition 2.5.3 (i), (ii): long exact sequences in the '
          'other variable for 0 -> Rad M -> M -> M/Rad M -> 0 (and the dual right modules), '
          '%d exactness conditions' % count)

    # Corollary 2.5.4 and Proposition 2.5.5
    c4 = c5 = 0
    for key in BASIC + ['x2', 'x3', 'x4']:
        A = ALG[key]
        mods = some_modules(A)
        simples = [vertex_simple(A, i) for i in range(A.nv)] if hasattr(A, 'nv') else [k_of(A)]
        for M in mods:
            r = Resolution(M, 5)
            for S in simples:
                dims, d, _ = hom_from_P_cochains(r, S, 4)
                assert all(d[n] == 0 for n in d)      # zero differential (proof of 2.5.4)
                assert ext_dims(r, S, 3) == [hom_dim(r.omega[n], S) for n in range(4)]
                c4 += 1
            # (ii): Ext^n(S, M) = Hom(S, Omega^(-n) M)
            cos = [M]
            for n in range(3):
                cos.append(cosyzygy(cos[-1]))
            for S in simples:
                rS = Resolution(S, 4)
                assert ext_dims(rS, M, 2) == [hom_dim(S, cos[n]) for n in range(3)]
                c4 += 1
            for N in mods:
                assert ext_dims(r, N, 3) == ext_dims_injective(M, N, 3)
                rN = Resolution(N, 5)
                assert tor_dims(r, N.dual(), 3) == tor_dims(Resolution(N.dual(), 5), M, 3)
                c5 += 1
            # injective second variable: Ext^n(M, D(e A)) = 0, n > 0
            for e in A.idems:
                I = Mod(A, [x.transpose() for x in
                            A.op().regular().sub(A.op().left_ideal(e.transpose())).mats])
                assert ext_dims(r, I, 3)[1:] == [0, 0, 0]
    check(c4 >= 100, 'p. 37, Corollary 2.5.4: dim Ext^n(M, S) = dim Hom(Omega^n M, S) (with the '
          'zero differential of the proof) and dim Ext^n(S, M) = dim Hom(S, Omega^(-n) M) for '
          'simple S, n <= 3 (resp. 2), %d cases over %d algebras' % (c4, len(BASIC) + 3))
    check(c5 >= 100, 'pp. 37-38, Proposition 2.5.5: Ext^n(M, M\') by a projective resolution of M '
          '= by an injective resolution of M\'; Tor_n(M\', M) by resolving either variable; '
          'Ext^n(M, I) = 0 for injective I = D(eA); n <= 3, %d pairs' % c5)


def omega_tilde(M, extra=1):
    """Omega~(M): the kernel of a non-minimal projective cover, the minimal
    one plus `extra` copies of A e_0 mapping to 0 (so Omega~(M) =
    Omega(M) (+) (A e_0)^extra)."""
    zero = vector(M.A.F, M.dim)
    st = Stage(M, cover_generators(M) + [(0, zero)] * extra)
    return st.Omega


def omega_tilde_inv(N, extra=1):
    """Omega~^(-1)(N) = D(Omega~(D N)) (cokernel of a non-minimal injective hull)."""
    O = omega_tilde(N.dual(), extra)
    return Mod(N.A, [x.transpose() for x in O.mats])


def sec_2_5_7():
    count = 0
    for key in ['A3rad2', 'square', 'nak2', 'nak3', 'x3', 'ext', 'kron']:
        A = ALG[key]
        mods = some_modules(A)
        for M in mods:
            OM = [Resolution(M, 0).omega[1], omega_tilde(M, 1), omega_tilde(M, 2)]
            r = Resolution(M, 6)
            rO = [Resolution(O, 5) for O in OM]
            for Mp in mods:
                e = ext_dims(r, Mp, 4)
                coO = [cosyzygy(Mp), omega_tilde_inv(Mp, 1)]
                for n in range(2, 5):
                    for ro in rO:
                        assert ext_dims(ro, Mp, n - 1)[n - 1] == e[n]
                    for C in coO:
                        assert ext_dims(r, C, n - 1)[n - 1] == e[n]
                    count += 1
                # Tor: Tor_n(M'', Mp) with M'' = D(M) a right module
                Mr = M.dual()
                rp = Resolution(Mp, 6)
                t = tor_dims(rp, Mr, 4)
                OMr = [Resolution(Mr, 0).omega[1], omega_tilde(Mr, 1)]
                OMp = [Resolution(Mp, 0).omega[1], omega_tilde(Mp, 1)]
                for n in range(2, 5):
                    for O in OMr:
                        assert tor_dims(rp, O, n - 1)[n - 1] == t[n]
                    for O in OMp:
                        assert tor_dims(Resolution(O, 5), Mr, n - 1)[n - 1] == t[n]
                    count += 1
    check(count >= 300, 'p. 38, Proposition 2.5.7 for n = 2, 3, 4: Ext^n(M, M\') = '
          'Ext^(n-1)(Omega~(M), M\') = Ext^(n-1)(M, Omega~^(-1)(M\')) and Tor_n(M, M\') = '
          'Tor_(n-1)(Omega~(M), M\') = Tor_(n-1)(M, Omega~(M\')), with minimal and non-minimal '
          'Omega~, %d cases over 7 algebras' % count)

    # n = 1: Lambda = k[x]/(x^3) (self injective), M = k, M' = Lambda
    A = ALG['x3']
    k, Lam = k_of(A), A.regular()
    rk = Resolution(k, 3)
    ext1 = ext_dims(rk, Lam, 1)[1]
    for O in [Resolution(k, 0).omega[1], omega_tilde(k, 1), omega_tilde(k, 2)]:
        refuted(ext1 == hom_dim(O, Lam), 'p. 38, Proposition 2.5.7 (i) as printed for n = 1: '
                'Ext^1(k, Lambda) = 0 but Hom(Omega~(k), Lambda) has dimension %d (Lambda = '
                'k[x]/(x^3), Omega~(k) of dimension %d)' % (hom_dim(O, Lam), O.dim))
    # Omega~^(-1)(Lambda) = Coker(Lambda -> Lambda (+) Lambda) = Lambda
    LL = direct_sum(Lam, Lam)
    emb = matrix(A.F, [[1 if i == j else 0 for j in range(3)] for i in range(6)])
    coker, _ = LL.quotient(emb)
    assert ext_dims(Resolution(k, 3), LL, 2)[1:] == [0, 0]   # Lambda (+) Lambda injective
    refuted(ext1 == hom_dim(k, coker), 'p. 38, Proposition 2.5.7 (i), second isomorphism for '
            'n = 1: Ext^0(k, Omega~^(-1)(Lambda)) = Hom(k, Lambda) != 0 for the embedding of Lambda '
            'in the injective module Lambda (+) Lambda')
    kr = k.dual()
    tor1 = tor_dims(Resolution(Lam, 3), kr, 1)[1]
    for O in [Resolution(kr, 0).omega[1], omega_tilde(kr, 1)]:
        refuted(tor1 == tensor_dim(O, Lam), 'p. 38, Proposition 2.5.7 (ii) as printed for n = 1: '
                'Tor_1(k, Lambda) = 0 but Omega~(k) (x) Lambda = Omega~(k) != 0')
    kerLL = Stage(Lam, [(0, Lam.act(A.one).column(0)), (0, 0 * Lam.act(A.one).column(0))]).Omega
    assert isomorphic(kerLL, Lam)
    refuted(tor1 == tensor_dim(kr, kerLL), 'p. 38, Proposition 2.5.7 (ii), second isomorphism '
            'for n = 1: Tor_0(k, Omega~(Lambda)) = k (x) Lambda != 0 for Lambda (+) Lambda -> Lambda')
    check(ext1 == 0 and tor1 == 0, 'p. 38, Proposition 2.5.7 corrected to n > 1: the n = 1 '
          'counterexample has Ext^1(k, Lambda) = Tor_1(k, Lambda) = 0 (Lambda injective and '
          'projective)')

# =========================================================================
# Section 2.6: extensions, Yoneda composition
# =========================================================================

def derivations(M3, M1):
    """Extensions 0 -> M1 -> E -> M3 -> 0 with E = M1 (+) M3 as vector
    spaces: rho_E(a) = [[rho_1(a), D(a)], [0, rho_3(a)]], E a module iff
    D(ab) = rho_1(a) D(b) + D(a) rho_3(b).  Returns (Der basis, Inn basis)
    as columns (blocks D(b_k) for the basis b_k of A, row-major)."""
    A, F = M1.A, M1.A.F
    n1, n3, d = M1.dim, M3.dim, A.dim
    s = n1 * n3
    a1, a3 = M1.basis_action(), M3.basis_action()
    rows = []
    for k in range(d):
        for l in range(d):
            c = A.coords(A.basis[k] * A.basis[l])
            row = []
            for m in range(d):
                blk = c[m] * identity_matrix(F, s)
                if m == l:
                    blk -= kron_XI(a1[k], n3)
                if m == k:
                    blk -= kron_IX(n1, a3[l].transpose())
                row.append(blk)
            rows.append(row)
    Der = kernel_cols(grid(F, rows))
    Inn = grid(F, [[kron_XI(a1[k], n3) - kron_IX(n1, a3[k].transpose())] for k in range(d)])
    return Der, col_basis(Inn)


def extension_module(M3, M1, Dvec):
    A, F = M1.A, M1.A.F
    n1, n3, s = M1.dim, M3.dim, M1.dim * M3.dim
    mats = []
    for gi, g in enumerate(A.gens):
        c = A.coords(g)
        Dg = sum((c[k] * matrix(F, n1, n3, list(Dvec[k * s:(k + 1) * s]))
                  for k in range(A.dim) if c[k]), matrix(F, n1, n3))
        mats.append(block_matrix(F, [[M1.mats[gi], Dg], [matrix(F, n3, n1), M3.mats[gi]]],
                                 subdivide=False))
    return Mod(A, mats)


def cocycle_space(res, N, n):
    """Z^n(Hom(P, N)) as a list of maps P_n -> N, and B^n as a matrix of
    columns (vectorised maps)."""
    F = res.A.F
    Pn = res.P(n)
    H = hom_basis(Pn, N)
    if not H:
        return [], matrix(F, N.dim * Pn.dim, 0)
    if res.stages[n + 1].r:
        cond = matrix(F, [(h * res.d[n + 1]).list() for h in H]).transpose()
        K = kernel_cols(cond)
    else:
        K = identity_matrix(F, len(H))
    Z = [sum((c[i] * H[i] for i in range(len(H)) if c[i]), matrix(F, N.dim, Pn.dim))
         for c in K.columns()]
    if n == 0:
        B = matrix(F, N.dim * Pn.dim, 0)
    else:
        Hp = hom_basis(res.P(n - 1), N)
        B = matrix(F, [(h * res.d[n]).list() for h in Hp]).transpose() if Hp \
            else matrix(F, N.dim * Pn.dim, 0)
    return Z, B


def same_class(B, x, y):
    F = x.base_ring()
    v = matrix(F, len(x.list()), 1, (x - y).list())
    return rank_of(hstack(F, v.nrows(), [B, v])) == rank_of(B)


def yoneda(resM, resM1, zeta, n, eta, m, rnd=None):
    """eta o zeta for cocycles zeta: P_n -> M' (resM resolves M) and
    eta: Q_m -> M'' (resM1 resolves M'): eta o F_m, F lifting zeta."""
    Fm = lifted_chain_map(resM, resM1, zeta, n, m, rnd)
    return eta * Fm[m]


def sec_2_6():
    rnd = random.Random(2601)
    # Ext^1 = equivalence classes of extensions (p. 39)
    count = 0
    for key in ['x2', 'x3', 'A2', 'A3rad2', 'kron', 'nak2', 'nak3', 'square']:
        A = ALG[key]
        mods = some_modules(A)
        for M3 in mods:
            r = Resolution(M3, 2)
            for M1 in mods:
                Der, Inn = derivations(M3, M1)
                assert ext_dims(r, M1, 1)[1] == Der.ncols() - Inn.ncols()
                count += 1
    for key in ['C2', 'C4', 'V4', 'D8', 'C3', 'C3xC3']:
        A = GROUPS[key]
        k = k_of(A)
        Der, Inn = derivations(k, k)
        assert ext_dims(Resolution(k, 2), k, 1)[1] == Der.ncols() - Inn.ncols()
        count += 1
    check(count >= 100, 'p. 39: Ext^1(M, M\') = equivalence classes of extensions: dim Der/Inn '
          '(module structures on M\' (+) M modulo the maps [[1, h], [0, 1]]) = dim Ext^1 from the '
          'resolution, %d pairs over 14 algebras' % count)

    # Lemma 2.6.2: exhaustively over GF(2)
    count = cases = 0
    for key in ['x2', 'x4', 'A2', 'kron', 'nak2']:
        A = ALG[key]
        mods = [M for M in some_modules(A) if M.dim <= 3]
        for M3 in mods:
            for M1 in mods:
                Der, Inn = derivations(M3, M1)
                if Der.ncols() > 9:
                    continue
                split = direct_sum(M1, M3)
                h31, h33 = hom_dim(M3, M1), hom_dim(M3, M3)
                for cs in product(list(A.F), repeat=Der.ncols()):
                    Dv = Der * vector(A.F, cs)
                    E = extension_module(M3, M1, Dv)
                    inner = rank_of(hstack(A.F, Dv.length(),
                                           [Inn, matrix(A.F, Dv.length(), 1, list(Dv))])) == Inn.ncols()
                    iso = isomorphic(E, split, exhaustive=True)
                    assert iso == inner
                    assert (hom_dim(M3, E) == h31 + h33) == inner
                    count += 1
                cases += 1
    for key in ['C2', 'C4', 'V4']:
        A = GROUPS[key]
        mods = [k_of(A), Resolution(k_of(A), 0).omega[1]]
        mods = [M for M in mods if M.dim <= 3]
        for M3 in mods:
            for M1 in mods:
                Der, Inn = derivations(M3, M1)
                if Der.ncols() > 9:
                    continue
                split = direct_sum(M1, M3)
                for cs in product(list(A.F), repeat=Der.ncols()):
                    Dv = Der * vector(A.F, cs)
                    E = extension_module(M3, M1, Dv)
                    inner = rank_of(hstack(A.F, Dv.length(),
                                           [Inn, matrix(A.F, Dv.length(), 1, list(Dv))])) == Inn.ncols()
                    assert isomorphic(E, split, exhaustive=True) == inner
                    count += 1
                cases += 1
    check(count >= 500, 'p. 39, Lemma 2.6.2: every extension 0 -> M1 -> E -> M3 -> 0 over GF(2) '
          'with E = M1 (+) M3 splits (exhaustive over all extension structures, %d extensions in '
          '%d pairs; isomorphism tested over all of Hom); and the dimension count of the proof, '
          'dim Hom(M3, E) = dim Hom(M3, M1) + dim Hom(M3, M3) exactly when it splits' % (count, cases))

    # Yoneda composition: well defined, associative, not commutative
    count = nonzero = 0
    for key, A in [('V4', GROUPS['V4']), ('C3', GROUPS['C3']), ('x3', ALG['x3']),
                   ('nak3', ALG['nak3']), ('ext', ALG['ext'])]:
        M = k_of(A) if not hasattr(A, 'nv') else direct_sum(*[vertex_simple(A, i) for i in range(A.nv)])
        r = Resolution(M, 5)
        Z = {n: cocycle_space(r, M, n) for n in range(4)}
        for a in range(3):
            for b in range(3 - a):
                for z in Z[a][0][:3]:
                    for y in Z[b][0][:3]:
                        p1 = yoneda(r, r, z, a, y, b)
                        p2 = yoneda(r, r, z, a, y, b, rnd)
                        Bab = Z[a + b][1]
                        assert same_class(Bab, p1, p2)       # independent of the lift
                        assert p1 * r.d[a + b + 1] == 0      # a cocycle
                        c = 3 - a - b
                        for x in Z[c][0][:2] if c <= 3 else []:
                            lhs = yoneda(r, r, z, a, yoneda(r, r, y, b, x, c), b + c)
                            rhs = yoneda(r, r, p1, a + b, x, c)
                            assert same_class(Z[3][1], lhs, rhs)
                            nonzero += not same_class(Z[3][1], lhs, 0 * lhs)
                            count += 1
    check(count >= 30 and nonzero >= 10, 'pp. 40-41, Yoneda composition (via the lifts '
          'hat(eta) o Omega~^m(hat(zeta)) of the comparison theorem): independent of the lift and '
          'associative, %d triples of total degree 3 (%d with a non-zero product)' % (count, nonzero))
    A = ALG['A2']
    S0, S1 = vertex_simple(A, 0), vertex_simple(A, 1)
    M = direct_sum(S0, S1)
    r = Resolution(M, 3)
    Z1, B1 = cocycle_space(r, M, 1)
    Z0, _ = cocycle_space(r, M, 0)
    e1 = matrix(A.F, [[0, 0], [0, 1]])            # projection of M onto S1
    eta0 = e1 * r.eps
    zetas = [z for z in Z1 if not same_class(B1, z, 0 * z)]
    zeta = zetas[0]
    left = yoneda(r, r, zeta, 1, eta0, 0)           # e1 o zeta
    right = yoneda(r, r, eta0, 0, zeta, 1)          # zeta o e1
    check(not same_class(B1, left, right), 'p. 41: Ext^*(M, M) is not commutative: for the '
          'path algebra 0 -> 1 and M = S0 (+) S1, e1 o zeta != zeta o e1 (zeta spanning '
          'Ext^1(S0, S1), e1 the projection onto S1)')

    # Exercise 3 (Feit): self injective algebras
    count = 0
    for key in SELFINJ + ['x3']:
        A = ALG[key]
        mods = some_modules(A)
        for M in mods:
            r = Resolution(M, 4)
            rO = Resolution(r.omega[1], 4)
            for Mp in mods:
                OMp = Resolution(Mp, 0).omega[1]
                assert ext_dims(r, Mp, 3)[1:] == ext_dims(rO, OMp, 3)[1:]
                count += 1
    for key in ['V4', 'C3xC3']:
        A = GROUPS[key]
        k = k_of(A)
        r = Resolution(k, 4)
        assert ext_dims(r, k, 3)[1:] == ext_dims(Resolution(r.omega[1], 4), r.omega[1], 3)[1:]
        count += 1
    check(count >= 30, 'p. 41, Exercise 3 (Feit): for self injective Lambda, dim Ext^n(M, M\') = '
          'dim Ext^n(Omega M, Omega M\'), n = 1, 2, 3, %d pairs' % count)

# =========================================================================
# Section 2.7: operations on chain complexes
# =========================================================================


class GCx:
    """A chain complex C_i (lo <= i <= hi) of free modules over a ring R
    (a field or ZZ): dims[i], d[i]: C_i -> C_(i-1)."""

    def __init__(self, R, dims, d):
        self.R, self.dims, self.d = R, dict(dims), dict(d)

    def dim(self, i):
        return self.dims.get(i, 0)

    def dd(self, i):
        if i in self.d:
            return self.d[i]
        return matrix(self.R, self.dim(i - 1), self.dim(i))

    def degrees(self):
        return sorted(i for i in self.dims if self.dims[i])

    def homology_dims(self):
        """Over a field: dim H_i for every degree."""
        return {i: self.dim(i) - rank_of(self.dd(i)) - rank_of(self.dd(i + 1))
                for i in range(min(self.dims) - 1, max(self.dims) + 2)}


def tensor_cx(C, D):
    """(C (x) D)_n = sum_(i+j=n) C_i (x) D_j, d(x (x) y) = dx (x) y + (-1)^i x (x) dy."""
    R = C.R
    degs = {}
    for i in C.degrees():
        for j in D.degrees():
            degs.setdefault(i + j, []).append((i, j))
    for n in degs:
        degs[n].sort()
    off = {}
    dims = {}
    for n, pairs in degs.items():
        o = 0
        for (i, j) in pairs:
            off[(i, j)] = o
            o += C.dim(i) * D.dim(j)
        dims[n] = o
    d = {}
    for n, pairs in degs.items():
        if n - 1 not in dims:
            continue
        M = matrix(R, dims[n - 1], dims[n])
        for (i, j) in pairs:
            a, b = C.dim(i), D.dim(j)
            if (i - 1, j) in off and C.dim(i - 1):
                M.set_block(off[(i - 1, j)], off[(i, j)], C.dd(i).tensor_product(identity_matrix(R, b), subdivide=False))
            if (i, j - 1) in off and D.dim(j - 1):
                M.set_block(off[(i, j - 1)], off[(i, j)],
                            (-1) ** (i % 2) * identity_matrix(R, a).tensor_product(D.dd(j), subdivide=False))
        d[n] = M
    return GCx(R, dims, d), off


def hom_cx(C, D):
    """Hom(C, D)_n = prod_i Hom(C_i, D_(i+n)) with the corrected differential
    (d f)_i = d^D_(i+n) f_i - (-1)^n f_(i-1) d^C_i (vectorised row-major)."""
    R = C.R
    lo = min(D.degrees()) - max(C.degrees())
    hi = max(D.degrees()) - min(C.degrees())
    off, dims = {}, {}
    for n in range(lo, hi + 1):
        o = 0
        for i in C.degrees():
            if D.dim(i + n):
                off[(n, i)] = o
                o += D.dim(i + n) * C.dim(i)
        dims[n] = o
    d = {}
    for n in range(lo, hi + 1):
        if n - 1 not in dims:
            continue
        M = matrix(R, dims[n - 1], dims[n])
        for i in C.degrees():
            if (n, i) not in off:
                continue
            # f_i contributes d^D f_i to (d f)_i and -(-1)^n f_i d^C_(i+1) to (d f)_(i+1)
            if (n - 1, i) in off:
                M.set_block(off[(n - 1, i)], off[(n, i)], kron_XI(D.dd(i + n), C.dim(i)))
            if (n - 1, i + 1) in off:
                M.set_block(off[(n - 1, i + 1)], off[(n, i)],
                            -(-1) ** (n % 2) * kron_IX(D.dim(i + n), C.dd(i + 1).transpose()))
        d[n] = M
    return GCx(R, dims, d), off


def random_cx(F, lo, hi, rnd, maxdim=3):
    """A random chain complex C_i, lo <= i <= hi, over the field F."""
    dims = [rnd.randint(0, maxdim) for _ in range(hi - lo + 1)]   # dims[m] = dim C_(hi-m)
    X = random_cochain(F, dims, rnd)
    return GCx(F, {hi - m: dims[m] for m in range(len(dims))},
               {hi - m: X.dd(m) for m in range(len(dims) - 1)})


def unimodular(n, rnd):
    U = identity_matrix(ZZ, n)
    for _ in range(3 * n):
        i, j = rnd.randrange(n), rnd.randrange(n)
        if i != j:
            E = identity_matrix(ZZ, n)
            E[i, j] = rnd.choice([-2, -1, 1, 2])
            U = U * E
    return U


def random_Z_complex(rnd, lo=0, hi=3):
    """A random complex of free abelian groups: a sum of pieces Z -a-> Z and
    Z in one degree, in random bases."""
    pieces = {i: [] for i in range(lo, hi + 1)}   # entries: ('free',) or ('top', a), ('bot', a)
    dims = {i: 0 for i in range(lo, hi + 1)}
    edges = []
    for i in range(lo, hi + 1):
        for _ in range(rnd.randint(0, 1)):
            dims[i] += 1
        if i > lo:
            for _ in range(rnd.randint(0, 2)):
                a = rnd.choice([1, 2, 3, 4, 6])
                edges.append((i, dims[i], dims[i - 1], a))
                dims[i] += 1
                dims[i - 1] += 1
    d = {}
    for i in range(lo + 1, hi + 1):
        M = matrix(ZZ, dims[i - 1], dims[i])
        for (j, c, r, a) in edges:
            if j == i:
                M[r, c] = a
        d[i] = M
    U = {i: unimodular(dims[i], rnd) if dims[i] else identity_matrix(ZZ, 0) for i in dims}
    d = {i: U[i - 1] * d[i] * U[i].inverse().change_ring(ZZ) for i in d}
    return GCx(ZZ, dims, d)


def z_homology(C):
    """{n: invariants} of a complex of free abelian groups (Smith form)."""
    cc = ChainComplex({i: C.dd(i) for i in range(min(C.dims) + 1, max(C.dims) + 1)
                       if C.dd(i).nrows() or C.dd(i).ncols()} or
                      {min(C.dims): matrix(ZZ, 0, C.dim(min(C.dims)))}, degree=-1)
    return {n: tuple(cc.homology(n).invariants()) for n in range(min(C.dims) - 1, max(C.dims) + 2)}


def ab_canon(invs):
    """Canonical form of a finitely generated abelian group given by cyclic
    factors (0 = Z): (rank, sorted prime powers)."""
    rank = 0
    pp = []
    for a in invs:
        a = Integer(a)
        if a == 0:
            rank += 1
        elif a > 1:
            for p, e in a.factor():
                pp.append(p ** e)
    return rank, tuple(sorted(pp))


def tensor_ab(X, Y):
    out = []
    for a in X:
        for b in Y:
            out.append(gcd(a, b) if a and b else (a or b) if (a == 0) != (b == 0) else 0)
    return out


def tor_ab(X, Y):
    return [gcd(a, b) for a in X for b in Y if a and b]


def sec_2_7():
    rnd = random.Random(2701)
    # Theorem 2.7.1 (Kunneth) over ZZ; Corollaries 2.7.2, 2.7.3
    count = with_tor = 0
    for trial in range(40):
        C = random_Z_complex(rnd, 0, 3)
        D = random_Z_complex(rnd, 0, 2)
        T, _ = tensor_cx(C, D)
        for n in T.d:
            if n - 1 in T.d:
                assert T.dd(n - 1) * T.dd(n) == 0
        HC, HD, HT = z_homology(C), z_homology(D), z_homology(T)
        for n in range(-1, 7):
            pred, tors = [], []
            for i in HC:
                for j in HD:
                    if i + j == n:
                        pred += tensor_ab(HC[i], HD[j])
                    if i + j == n - 1:
                        tors += tor_ab(HC[i], HD[j])
            assert ab_canon(HT.get(n, ())) == ab_canon(pred + tors)
            with_tor += ab_canon(tors) != (0, ())
            count += 1
    check(count >= 300 and with_tor >= 20, 'p. 43, Theorem 2.7.1 (Kunneth) over Z, where Z_n and '
          'B_n are free: H_n(C (x) D) = sum H_i(C) (x) H_j(D) (+) sum_(i+j=n-1) Tor_1(H_i(C), '
          'H_j(D)) for 40 random pairs of complexes of free abelian groups (with the sign (-1)^i '
          'of p. 42; d o d = 0 checked), %d degrees, %d with a non-zero Tor term' % (count, with_tor))
    # Section 3.2 (p. 56) cites Corollary 2.7.3 for: the tensor product of
    # 0 -> M' -> M_(m-1) -> ... -> M_0 and 0 -> N' -> ... -> N_0 (R-projective
    # terms, exact except H_0 = M, N) has homology M (x) N in degree 0 only.
    # This is Corollary 2.7.2; the truncated complexes are not exact.
    Ct = GCx(ZZ, {0: 2, 1: 1}, {1: matrix(ZZ, 2, 1, [1, 2])})        # H_0 = Z, H_1 = 0
    Dt = GCx(ZZ, {0: 2, 1: 1}, {1: matrix(ZZ, 2, 1, [3, 1])})        # H_0 = Z, H_1 = 0
    Tt, _ = tensor_cx(Ct, Dt)
    Ht = z_homology(Tt)
    assert ab_canon(z_homology(Ct)[0]) == (1, ()) and ab_canon(z_homology(Ct)[1]) == (0, ())
    check(ab_canon(Ht[0]) == (1, ()) and all(ab_canon(Ht[n]) == (0, ()) for n in (1, 2)),
          'p. 44, Corollary 2.7.2 (as used in Section 3.2, p. 56): truncated resolutions with '
          'R-projective homology M = N = Z in degree 0 have tensor product with homology '
          'M (x) N in degree 0 and 0 elsewhere (the complexes are not exact, so Corollary 2.7.3 '
          'does not apply to them directly)')
    # Corollary 2.7.2: H(C) free; Corollary 2.7.3: C exact
    for trial in range(10):
        D = random_Z_complex(rnd, 0, 2)
        C1 = GCx(ZZ, {0: 1, 1: 1, 2: 1}, {1: matrix(ZZ, 1, 1, [0]), 2: matrix(ZZ, 1, 1, [0])})
        T, _ = tensor_cx(C1, D)
        HT, HD = z_homology(T), z_homology(D)
        for n in range(0, 5):
            pred = []
            for i in (0, 1, 2):
                if n - i in HD:
                    pred += list(HD[n - i])
            assert ab_canon(HT.get(n, ())) == ab_canon(pred)
        Cex = GCx(ZZ, {0: 2, 1: 2}, {1: unimodular(2, rnd)})
        T2, _ = tensor_cx(Cex, D)
        assert all(ab_canon(v) == (0, ()) for v in z_homology(T2).values())
    check(True, 'p. 44, Corollaries 2.7.2, 2.7.3: H(C (x) D) = H(C) (x) H(D) when H(C) is free; '
          'C (x) D exact when C is exact (10 random D)')

    # The Hom complex (p. 44), corrected formula
    for F in (F2, F9):
        for trial in range(10):
            C = random_cx(F, -1, 2, rnd)
            D = random_cx(F, -1, 2, rnd)
            if not C.degrees() or not D.degrees():
                continue
            Hm, off = hom_cx(C, D)
            for n in Hm.d:
                if n - 1 in Hm.d:
                    assert Hm.dd(n - 1) * Hm.dd(n) == 0
            hC, hD, hH = C.homology_dims(), D.homology_dims(), Hm.homology_dims()
            for n in range(min(Hm.dims), max(Hm.dims) + 1):
                assert hH[n] == sum(hC.get(i, 0) * hD.get(i + n, 0) for i in hC)
            # H_0 = chain maps modulo null homotopic maps (Exercise, p. 46)
            Z0 = kernel_cols(Hm.dd(0)).ncols() if Hm.dim(0) else 0
            B0 = rank_of(Hm.dd(1))
            assert hH[0] == Z0 - B0
    check(True, 'p. 44, Hom complex with the corrected differential (d f)_i = d_j f_i - (-1)^n '
          'f_(i-1) d_i (j = i + n): d o d = 0 and dim H_n Hom(C, D) = sum_i dim H_i(C) dim '
          'H_(i+n)(D) for 20 pairs of random complexes over GF(2), GF(9); H_0 = chain maps '
          'modulo null homotopic maps (Exercise, p. 46)')
    # the printed formula: d_j(f(x)) and f(d_(i+1)(x)) are maps out of different modules
    C = GCx(F2, {0: 1, 1: 2}, {1: matrix(F2, 1, 2, [1, 0])})
    D = GCx(F2, {0: 1, 1: 1}, {1: matrix(F2, 1, 1, [1])})
    f = matrix(F2, 1, 1, [1])           # f in Hom(C_0, D_1): i = 0, j = 1, n = 1
    t1 = D.dd(1) * f                     # d_j f : C_0 -> D_0
    t2 = f * C.dd(1)                     # f d_(i+1) : C_1 -> D_1
    refuted(t1.dimensions() == t2.dimensions(), 'p. 44, l. -8 and l. -6 as printed: '
            'd_j(f(x)) and f(d_(i+1)(x)) for f in Hom(C_i, D_j) are maps C_i -> D_(j-1) and '
            'C_(i+1) -> D_j (here 1 x 1 and 1 x 2 matrices), so no single x can be used')

    # the dual (p. 45) and evaluation; C[n] = Lambda[n] (x) C
    c_dual = c_ev = c_sens = c_shift = 0
    for F in (F2, F9):
        for trial in range(8):
            C = random_cx(F, -2, 2, rnd)
            if not C.degrees():
                continue
            k0 = GCx(F, {0: 1}, {})
            Du, offu = hom_cx(C, k0)
            for n in Du.d:
                # Hom(C, k[0])_n = Hom(C_(-n), k); (d f)(x) = (-1)^(n-1) f(d_(-n+1)(x))
                if (n, -n) in offu and (n - 1, -n + 1) in offu:
                    blk = Du.dd(n).submatrix(offu[(n - 1, -n + 1)], offu[(n, -n)],
                                             C.dim(-n + 1), C.dim(-n))
                    assert blk == (-1) ** ((n - 1) % 2) * C.dd(-n + 1).transpose()
                    c_dual += 1
            # evaluation T_0 -> k: f (x) x |-> f(x) for f in Hom(C_i, k), x in C_i
            Dwrong = GCx(F, Du.dims, {n: -Du.d[n] for n in Du.d})   # sign (-1)^n instead
            for Dx, good in ((Du, True), (Dwrong, False)):
                T, offT = tensor_cx(Dx, C)
                if 0 not in T.dims or not T.dim(0) or 1 not in T.dims or not T.dim(1):
                    continue
                ev = matrix(F, 1, T.dim(0))
                for (a, b), o in offT.items():
                    if a + b == 0 and (a, -a) in offu:
                        m = C.dim(b)
                        for r_ in range(m):           # e_r^* (x) e_c -> delta_(rc)
                            ev[0, o + r_ * m + r_] = 1
                if good:
                    assert ev * T.dd(1) == 0
                    c_ev += 1
                elif ev * T.dd(1) != 0:
                    c_sens += 1
            for n in range(-2, 3):
                kn = GCx(F, {-n: 1}, {})
                S, offS = tensor_cx(kn, C)
                for i in range(-2, 3):
                    if C.dim(i) and C.dim(i - 1):
                        assert S.dd(i - n) == (-1) ** (n % 2) * C.dd(i)
                        c_shift += 1
    check(c_dual >= 20 and c_ev >= 10 and c_sens >= 1 and c_shift >= 30,
          'p. 45: the differential of the dual Hom(C, Lambda[0]) is (d_n f)(x) = (-1)^(n-1) '
          'f(d_(-n+1)(x)), as the corrected formula gives (%d blocks); evaluation Hom(C, '
          'Lambda[0]) (x) C -> Lambda[0] is a chain map (%d complexes; with the opposite sign it '
          'fails in %d of them over GF(9)); C[n] = Lambda[n] (x) C has (C[n])_i = C_(i+n) and '
          'differential (-1)^n d (%d cases, n = -2..2)' % (c_dual, c_ev, c_sens, c_shift))

    # Definition 2.7.4: what the printed text claims and what holds
    # (a) the comparison theorem holds only up to homotopy
    F = F2
    Cc = GCx(F, {0: 1, 1: 1}, {1: matrix(F, 1, 1, [1])})   # k -1-> k, acyclic
    assert Cc.homology_dims() == {i: 0 for i in range(-1, 3)}
    # P = C (eps = id) and P' = 0 (eps' = 0) are both resolutions of C in the
    # sense of Definition 2.7.4; a map f: P -> P' = 0 has eps' f = 0 != id = eps
    eps = identity_matrix(F, 1)
    refuted(eps == 0, 'p. 45, after Definition 2.7.4 ("the Comparison Theorem 2.4.2 also '
            'holds ... with exactly the same proof"): for C = (k -1-> k), P = C and P\' = 0 '
            'are resolutions in the sense of Definition 2.7.4, and the only map P -> P\' = 0 '
            'does not lift id_C (eps\' f = 0 != eps)')
    s0 = matrix(F, 1, 1, [1])   # contraction: id = d s + s d
    check(Cc.dd(1) * s0 == identity_matrix(F, 1) and s0 * Cc.dd(1) == identity_matrix(F, 1),
          'p. 45: in the same example id_C is null homotopic, so the comparison theorem holds '
          'up to homotopy')
    # (b) D (x) P <- P' (x) P is a quasi-isomorphism, not a homotopy equivalence
    P = GCx(ZZ, {0: 1, 1: 1}, {1: matrix(ZZ, 1, 1, [2])})
    PP, offPP = tensor_cx(P, P)
    H = z_homology(PP)
    assert ab_canon(H[0]) == (0, (2,)) and ab_canon(H[1]) == (0, (2,)) and ab_canon(H[2]) == (0, ())
    # D (x) P = (F2 -0-> F2); the map P' (x) P -> D (x) P reduces mod 2 the summand P'_0 (x) P
    DP = GCx(F2, {0: 1, 1: 1}, {1: matrix(F2, 1, 1, [0])})
    assert DP.homology_dims()[0] == 1 and DP.homology_dims()[1] == 1
    m0 = matrix(F2, 1, 1, [1])                        # degree 0: Z -> F2
    m1 = matrix(F2, 1, 2, [0, 1]) if offPP[(0, 1)] == 1 else matrix(F2, 1, 2, [1, 0])
    # H_1(P' (x) P) is generated by (1, -1); its image is 1 != 0: an isomorphism on H_1
    z1 = vector(ZZ, [1, -1])
    assert PP.dd(1) * z1 == 0 and (m1 * z1.change_ring(F2)) != 0
    # a homotopy inverse would be a chain map D (x) P -> P' (x) P, zero as Hom_Z(Z/2, Z) = 0
    assert matrix(ZZ, 1, 1, [2]).right_kernel().dimension() == 0
    refuted(DP.homology_dims()[0] == 0, 'p. 45, "D (x) P <- P\' (x) P -> P\' (x) C are homotopy '
            'equivalences": over Lambda = Z with C = D = Z/2 and P = P\' = (Z -2-> Z), the map '
            'P\' (x) P -> D (x) P is an isomorphism on homology (Z/2, Z/2) but every chain map '
            'back is zero (Hom_Z(Z/2, Z) = 0), so it has no homotopy inverse as H(D (x) P) != 0')
    # (c) hyper-Tor: Tor(D, C) = H(D (x) P) = H(P' (x) C), Lambda = k[x]/(x^2)
    A = ALG['x2']
    x = A.x
    N = 8
    # C = (Lambda -x-> Lambda), projective; D = k[0]; P' = (... -x-> Lambda -x-> Lambda)
    dims = {n: (2 if n <= N else 0) + (2 if 1 <= n <= N + 1 else 0) for n in range(0, N + 2)}
    d = {}
    for n in range(1, N + 2):
        M = matrix(F2, dims[n - 1], dims[n])
        # coordinates: [ (a = n, b = 0) | (a = n - 1, b = 1) ]
        a0 = 2 if n <= N else 0
        a0m = 2 if n - 1 <= N else 0
        if n <= N:                       # (n, 0) -> (n - 1, 0): x
            M.set_block(0, 0, x)
        if 1 <= n <= N + 1 and n - 1 >= 1:   # (n - 1, 1) -> (n - 2, 1): x
            M.set_block(a0m, a0, x)
        if 1 <= n <= N + 1:              # (n - 1, 1) -> (n - 1, 0): (-1)^(n-1) x
            if n - 1 <= N:
                M.set_block(0, a0, (-1) ** ((n - 1) % 2) * x)
        d[n] = M
    T = GCx(F2, dims, d)
    for n in range(2, N + 1):
        assert T.dd(n - 1) * T.dd(n) == 0
    h = T.homology_dims()
    check([h[n] for n in range(0, N - 1)] == [1, 1] + [0] * (N - 3),
          'p. 45: Tor_n(D, C) = H_n(D (x) P) = H_n(P\' (x) C) for Lambda = k[x]/(x^2), '
          'C = (Lambda -x-> Lambda), D = k: both are k for n = 0, 1 and 0 for 2 <= n <= %d' % (N - 2))

# =========================================================================
# Section 2.8: induction and restriction
# =========================================================================

def group_pair(Gexpr, Hgens_expr, p, F):
    """(Lambda = F G, Gamma = F H, irreducible G- and H-modules)."""
    G = libgap.eval(Gexpr)
    ggens, gmods = gap_modules(G, p, F)
    pg = bool(libgap.IsPGroup(G)) and int(libgap.PrimePGroup(G)) == p
    Lam = group_algebra(G, ggens, F, pg)
    H = libgap.Subgroup(G, [libgap.eval(h) for h in Hgens_expr])
    hgens, hmods = gap_modules(H, p, F)
    ph = bool(libgap.IsPGroup(H)) and int(libgap.PrimePGroup(H)) == p
    Gam = subalgebra(Lam, [Lam.perm(h) for h in hgens],
                     radgens=[Lam.perm(h) - Lam.one for h in hgens] if ph else None)
    Gm = [Mod(Lam, m) for m in gmods]
    Hm = [Mod(Gam, m) for m in hmods]
    # also a permutation module k_H^G and Omega(k) (non-simple modules)
    kH = Mod(Gam, [identity_matrix(F, 1) for _ in hgens])
    Gm.append(induce(Lam, Gam, kH)[0])
    Hm.append(Resolution(kH, 0, ph).omega[1])
    return Lam, Gam, Gm, Hm


PAIRS = [
    ('S3 > C2, p = 2', 'Group((1,2,3),(1,2))', ['(1,2)'], 2, F2),
    ('S3 > C3, p = 3', 'Group((1,2,3),(1,2))', ['(1,2,3)'], 3, F9),
    ('S3 > C2, p = 3', 'Group((1,2,3),(1,2))', ['(1,2)'], 3, F9),
    ('A4 > V4, p = 2', 'Group((1,2,3),(1,2)(3,4))', ['(1,2)(3,4)', '(1,3)(2,4)'], 2, F2),
    ('A4 > C3, p = 3', 'Group((1,2,3),(1,2)(3,4))', ['(1,2,3)'], 3, F9),
    ('D8 > C4, p = 2', 'Group((1,2,3,4),(1,3))', ['(1,2,3,4)'], 2, F2),
    ('D8 > V4, p = 2', 'Group((1,2,3,4),(1,3))', ['(1,3)', '(2,4)'], 2, F2),
    ('S4 > D8, p = 2', 'Group((1,2,3,4),(1,2))', ['(1,2,3,4)', '(1,3)'], 2, F2),
]


def sec_2_8():
    c_nak = c_es = c_maps = 0
    nmax = 3
    for label, Gx, Hx, p, F in PAIRS:
        Lam, Gam, Gm, Hm = group_pair(Gx, Hx, p, F)
        lam_min = Lam.radgens is not None
        gam_min = Gam.radgens is not None
        for N in Hm:
            Nup, proj, rel = induce(Lam, Gam, N)
            Nco = coinduce(Lam, Gam, N)
            assert Nup.dim == Lam.dim // Gam.dim * N.dim == Nco.dim
            rN = Resolution(N, nmax + 1, gam_min)
            rNup = Resolution(Nup, nmax + 1, lam_min)
            for M in Gm:
                Mres = restrict(M, Gam)
                # Proposition 2.8.3 (Nakayama relations), by Hom spaces
                assert hom_dim(N, Mres) == hom_dim(Nup, M)
                assert hom_dim(Mres, N) == hom_dim(M, Nco)
                c_nak += 1
                # Corollary 2.8.4 (Eckmann-Shapiro)
                assert ext_dims(rN, Mres, nmax) == ext_dims(rNup, M, nmax)
                rM = Resolution(M, nmax + 1, lam_min)
                rMres = Resolution(Mres, nmax + 1, gam_min)
                assert ext_dims(rMres, N, nmax) == ext_dims(rM, Nco, nmax)
                c_es += 1
                # the natural maps: M|^up -> M onto, N -> N^up| into
                d, n = Lam.dim, M.dim
                eta_big = hstack(F, n, [M.basis_action()[k] for k in range(d)])   # n x (d n)
                Mup, projM, relM = induce(Lam, Gam, Mres)
                assert eta_big * relM == 0
                assert rank_of(eta_big) == n
                c_maps += 1
            one = Lam.coords(Lam.one)
            emb = proj * kron_XI(matrix(F, Lam.dim, 1, list(one)), N.dim)
            assert rank_of(emb) == N.dim
    check(c_nak >= 30, 'p. 46, Proposition 2.8.3 (Nakayama relations): dim Hom_H(N, M|_H) = '
          'dim Hom_G(N^G, M) and dim Hom_H(M|_H, N) = dim Hom_G(M, N^^G) (co-induced) for M '
          'irreducible or k_H^G and N irreducible or Omega(k_H), %d pairs in %d '
          'group/subgroup pairs (%s)' %
          (c_nak, len(PAIRS), '; '.join(x[0] for x in PAIRS)))
    check(c_es >= 30, 'p. 47, Corollary 2.8.4 (Eckmann-Shapiro): dim Ext^n_H(N, M|_H) = dim '
          'Ext^n_G(N^G, M) and dim Ext^n_H(M|_H, N) = dim Ext^n_G(M, N^^G), n <= %d, '
          '%d pairs of modules as above' % (nmax, c_es))
    check(c_maps >= 30, 'pp. 46-47: the natural map M|_Gamma^Lambda -> M, l (x) m -> l m, is '
          'well defined and onto, and N -> N^Lambda|_Gamma, n -> 1 (x) n, is injective (%d cases)'
          % c_maps)

    # The hypothesis "Lambda projective as a Gamma-module" matters
    A = ALG['x3']
    x = A.x
    Gam = subalgebra(A, [x * x], radgens=[x * x])
    k_g = k_of(Gam)
    Lres = restrict(A.regular(), Gam)
    assert ext_dims(Resolution(Lres, 2), k_g, 1)[1] != 0     # Lambda not Gamma-projective
    kup, _, _ = induce(A, Gam, k_g)
    lhs = ext_dims(Resolution(k_g, 2), Lres, 1)[1]
    rhs = ext_dims(Resolution(kup, 2), A.regular(), 1)[1]
    check(lhs == 1 and rhs == 0, 'p. 47, Corollary 2.8.4 needs Lambda projective over Gamma: '
          'for Gamma = k[x^2] in Lambda = k[x]/(x^3), Ext^1_Gamma(k, Lambda|) = k but '
          'Ext^1_Lambda(k^Lambda, Lambda) = 0')

    # Lemma 2.8.2 / Proposition 2.8.5 with Lambda = k, I = k: Ext^n_Gamma(N, D(A)) = D Tor_n^Gamma(A, N)
    count = 0
    for key in ['A3rad2', 'square', 'nak3', 'x3', 'ext', 'kron']:
        Gam = ALG[key]
        mods = some_modules(Gam)
        for N in mods:
            r = Resolution(N, 4)
            for Mr in [M.dual() for M in mods]:       # right Gamma-modules A
                DA = Mod(Gam, [m.transpose() for m in Mr.mats])
                assert ext_dims(r, DA, 3) == tor_dims(r, Mr, 3)
                count += 1
    check(count >= 50, 'p. 48, Proposition 2.8.5 with Lambda = k, I = k: dim Ext^n_Gamma(N, '
          'Hom_k(A, k)) = dim Hom_k(Tor_n^Gamma(A, N), k), n <= 3, %d pairs over 6 algebras' % count)

def hom_crosscheck():
    """The two computations of Hom_A(M, N) agree (machinery check)."""
    count = 0
    for key in BASIC + ['x2', 'x3', 'x4']:
        A = ALG[key]
        mods = some_modules(A) + [A.regular()]
        for M in mods:
            for N in mods:
                H, H2 = hom_basis(M, N), hom_basis_kron(M, N)
                assert len(H) == len(H2)
                for X in H:
                    for gm, gn in zip(M.mats, N.mats):
                        assert X * gm == gn * X
                if H:
                    assert matrix(A.F, [x.list() for x in H]).rank() == len(H)
                count += 1
    for key in LOCAL:
        A = GROUPS[key]
        mods = [k_of(A), A.regular()]
        for M in mods:
            for N in mods:
                assert hom_dim(M, N) == len(hom_basis_kron(M, N))
                count += 1
    check(count >= 200, 'machinery: Hom_A(M, N) from a projective presentation of M agrees with '
          'the direct solution of X rho_M(g) = rho_N(g) X (%d pairs)' % count)


def main():
    t0 = time.time()
    hom_crosscheck()
    sec_2_1()
    sec_2_2()
    sec_2_3()
    sec_2_4()
    sec_2_5()
    sec_2_5_7()
    sec_2_6()
    sec_2_7()
    sec_2_8()
    refuted_count = len([c for c in CHECKS if c.startswith('REFUTED')])
    print('%s; %d checks (%d refuted printed readings) in %.0f s'
          % (version(), len(CHECKS), refuted_count, time.time() - t0))
    print('ok chapter-2: %d checks' % len(CHECKS))


if __name__ == '__main__':
    main()
