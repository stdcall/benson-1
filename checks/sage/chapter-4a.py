"""Exact checks of Chapter 4, introduction and Sections 4.1-4.7 (Sage, GAP).

Benson, *Representations and Cohomology I*, second edition (1998),
Chapter 4 "Methods from the representations of algebras", Sections 4.1
"Representations of quivers" ... 4.7 "Path algebras of finite type",
printed pp. 99-128.  Our files: content/04-00-representations-algebras.typ
... content/04-07-path-algebras-finite-type.typ and the diagrams of 4.1,
4.3, 4.5.  (Sections 4.8-4.18 are checked in another script.)

Everything below is exact: linear algebra over finite fields, ZZ and QQ,
representations of quivers given by matrices, and the GAP MeatAxe (through
libgap) for modules of V4 = C2 x C2 and A4.  Expected values are the
book's statements, matrices and numbers read off the printed pages (page
and our label in each message); where the printed text was corrected, the
printed reading is kept as a refuted check beside the corrected one.
Values the book does not print (orders of Weyl groups, numbers of roots,
Coxeter numbers) are taken from Humphreys, Reflection Groups and Coxeter
Groups (1990), 2.11 Table 2 and 3.18 Table 2.

Conventions.  Representations of quivers are handled with column vectors:
the matrix of a map V_x -> V_y has dim V_y rows.  The MeatAxe acts on row
vectors (v -> v A); the kV4- and A4-modules of Section 4.3 are given to it
with the printed matrices, and Theorem 4.3.2 (ii), (iii), Theorem 4.3.3 and
the Remark after it are consistent in this (row vector) reading, while the
proof of Theorem 4.3.2 works with column vectors.  A labelled graph is a
list of edges (x, y, a, b), a = _x d_y, b = _y d_x (Definition 4.1.9), the
Cartan matrix c_xy = 2 delta_xy - sum _x d_y (Definition 4.5.3); x => y
is the edge (2, 1) (p. 116).

Checked here (by section):

4.1 (pp. 99-105)
  * Path algebras kQ of 9 acyclic quivers over GF(2), GF(3): the e_x are
    orthogonal idempotents with sum 1, associativity, kQ is finite
    dimensional; P_x = kQ e_x has the paths beginning at x, e_y u = u =
    u e_x; kQ_(m) is a two-sided ideal and the products of m paths of
    length >= 1 span it, so kQ_(1) = J(kQ) and kQ_(m) = J^m;
    e_x kQ_(m)/kQ_(m+1) has the paths of length m ending at x; a path
    induces injective maps with independent images.  4 quivers with
    oriented cycles have paths of every length <= 6.
  * Theorem 4.1.4: 120 random submodules of free kQ-modules (6 quivers,
    GF(2), GF(3)) are projective (their dimension vector is that of the
    projective cover); rad P_x is the sum of the P_y alpha.
  * Definition 4.1.6, Proposition 4.1.7: the Ext-quiver of kQ is Q
    (e_j J e_i / e_j J^2 e_i); kV4: dim Ext^1(k, k) = dim J/J^2 = 2; the map
    k<a, b> -> kV4 is onto, in degrees <= 3 its kernel is the ideal of
    a^2, b^2, ab - ba and meets the paths of length <= 1 in 0; GF(3)S3:
    idempotents e_+-, J of dimensions 4, 2, 0, Ext-quiver k <-> sgn, the
    map from its path algebra is onto with kernel in length >= 2.
  * Example after Definition 4.1.8 (corrected to kQ/I): on the linear
    quiver 0 -> ... -> 5, the projectives (kQ/kQ_(2)) e_x are exact
    complexes k -> k; of the 161 complexes over GF(2) with five dimension
    vectors between zeros the exact ones are exactly the projective
    modules; as printed (kQ) the projective kQ e_0 is not a complex.
  * Remark (ii) after Corollary 4.1.11, p = 2, 3: dimension p^2, J =
    (epsilon), Lambda/J = k(x^(1/p)), every lift z of y has z^p = x +
    epsilon (10 random lifts each): no splitting.
4.2 (pp. 106-107)
  * Lemma 4.2.2: for every arrow i -> j of 6 quivers the right
    multiplication by the arrow embeds P_j in J P_i, not in J^2 P_i.
  * Lemma 4.2.3 (corrected P_1 > P_2 > ... > P_1): P_j is a proper
    submodule of P_i for an arrow i -> j; the printed P_i < P_j refuted
    (dim P_i > dim P_j).
  * Lemma 4.2.1 on kA3/J^2; Proposition 4.2.4 for the upper triangular
    matrices T_n(GF(3)) = kA_n, n <= 5.
4.3 (pp. 107-114)
  * kV4/Soc = Lambda with the printed products; dim Ext^1(S_i, S_j) for the
    Kronecker quiver; only S_2 has V_2 != Im a + Im b; End(Lambda) and End
    of its representation differ (dimensions 3, 1).
  * Theorem 4.3.2 (Kronecker): the listed indecomposables (27 over GF(2)
    with dimensions <= 4, 29 over GF(3) and 47 over GF(4) with dimensions
    <= 3) have local End (k, or k[T]/(p^e) for case (i)) and are pairwise
    non-isomorphic, and for every dimension vector in these ranges
    sum 1/|Aut M| over their sums = q^(2 d1 d2)/|GL(d1)||GL(d2)|, so the
    list is complete there; q + 1 of dimension (1, 1).  The printed
    matrices of (ii) give dim V_2 = dim V_1 + 1 when they act on row
    vectors.  A companion matrix (all monic f of degree <= 4 over GF(2),
    <= 3 over GF(3)) is indecomposable iff f is a prime power.
  * The proof of Theorem 4.3.2: the corrected dim V_1 = n + 1,
    dim V_2 = n (E_lambda(n), n <= 5, has a kernel vector of minimal degree
    n, its transpose none: the printed n, n + 1 refuted); on 300 random
    representations (GF(2), GF(3), dim V_1 > dim V_2; 197 with n >= 1):
    independence of v_0..v_n and a v_1..a v_n, the block form (in the
    bases v_0.., a v_1.. the block E has rows (lambda, 1), the printed
    E_lambda(n) after reversing both bases), the printed pairing of the
    bar and underbar fits the former, the elimination gives
    x_i A' - x_(i+1) B' = d_(i+1) - c_i (i <= n - 1, so the printed last
    entry d_(n+1, m-1) - c_(n, m-1) does not exist), the matrix has
    n m rows and (n - 1)(m - 1) columns (printed (n - 1)(m - 1) x n m
    refuted), it has full column rank iff A' + lambda B' has no column
    kernel vector of degree <= n - 2 (there is none of degree <= n - 1),
    X and Y exist and block diagonalise; the printed row-vector step is
    refuted (a row vector u with u M = 0 always exists, no column vector
    of degree n - 1 does, and the printed v'(lambda) does not satisfy
    v'(lambda)(A' + lambda B') = 0).  The corrected last step: E_lambda(n)
    maps the vectors of degree <= n - 1 bijectively onto those of degree
    <= n (n <= 6, GF(2), GF(3), QQ); on 80 examples (n = 2..4, a planted
    kernel vector) a column vector u with M u = 0 gives (A' + lambda B')
    u(lambda) = 0, deg u(lambda) <= n - 2, and with E w = -(C + lambda D)
    u(lambda), deg w <= n - 1, (w, u) is annihilated by a + lambda b.
  * Theorem 4.3.3 by the MeatAxe over GF(2) (dimensions <= 9) and GF(4)
    (<= 7): the printed matrices satisfy the relations, the modules are
    indecomposable and pairwise non-isomorphic, (iv) = (v) iff n = 0, one
    module of dimension 2n for each point of P^1 of degree dividing n;
    Remark: (iv) = Omega^-n(k), (v) = Omega^n(k) (row vectors); the
    numbers 1, 4, 6, 17 of isomorphism classes of kV4-modules of dimension
    1-4 over GF(2) (orbits of GL_N(2) on pairs of matrices) are those of
    the sums of the listed modules.
  * A4 (p. 112), GF(4) and GF(16): t acts on P^1 by alpha -> 1/(1 - alpha)
    with fixed points omega, omegabar; V_(n, alpha) induced is
    indecomposable for non-fixed alpha (n <= 2 over GF(4), n = 1 over
    GF(16)); for alpha = omega, omegabar it has three summands W, W (x)
    omega, W (x) omegabar restricting to V_(n, alpha) (n <= 3); Omega^(+-n)
    of the three simples restrict to Omega^(+-n)(k) and are distinct
    (n <= 2); the printed matrices of "W_(n, omega)(1)" give an
    indecomposable A4-module restricting to V_(n, omegabar), a summand of
    V_(n, omegabar) induced and not of V_(n, omega) induced (n <= 3):
    corrected label W_(n, omegabar)(1).
  * Linear relations: Proposition 4.3.5, Corollary 4.3.6, C' <= C'' and
    the automorphism phi of C''/C' for all 3104 relations on GF(2)^2,
    GF(2)^3, GF(3)^2 (U, W found by search); only S_1 has
    Ker a cap Ker b != 0.
  * Butler (pp. 113-114): the idempotents e_i of QV4; for 7 reduced four
    subspace systems over GF(2) the lattice M gives back V and the V_i;
    of the 46 indecomposable four subspace systems with dim V <= 3 over
    GF(2) exactly five are not reduced, all with dim V = 1.
4.4 (pp. 114-116)
  * Theorem 4.4.4 (i): the GF(2)C_2-, GF(2)C_4-, GF(3)C_3-, GF(3)C_9-modules
    of dimension <= 4 (<= 3 for C_9) are the sums of the Jordan blocks of
    size <= p^n (conjugacy classes of GL_N(q)).
4.5 (pp. 116-120)
  * The printed numbers of every Euclidean diagram (series up to 10
    vertices) are additive; E~_8 with the printed 1 is not (2 at the
    branch vertex, -4 at the end of the branch), with 3 it is; the
    numbers of the infinite diagrams are additive on truncations; Cartan
    matrix of F4; B2 = C2, A3 = D3 and no other coincidence among the
    Dynkin and Euclidean diagrams with <= 9 vertices; opposites of
    Euclidean diagrams are Euclidean, T^op is valued by N/f_x.
  * Lemma 4.5.2 for all 19 097 connected labelled graphs in the families:
    trees on <= 5 vertices with labels (a, b), ab <= 4 (13 385); graphs
    with cycles on 3, 4 vertices and double edges with labels (1, 1),
    (1, 2), (2, 1), (2, 2) (5 712).  For the 13 817 valued ones,
    Proposition 4.6.3 (i)-(iii) and Theorem 4.5.8 (i)-(iii): the 25
    Dynkin ones are positive definite with a subadditive non-additive
    function (n = 1 C^-1) and no additive one; the 35 Euclidean ones are
    semidefinite and not definite, additive on T and T^op; for the 13 757
    others a v >= 0 with (v, v) < 0 and a u >= 0 with C u < 0 (no
    subadditive function) are exhibited.
  * Lemma 4.5.6 for every finite Dynkin diagram with <= 8 vertices;
    Proposition 4.5.7 (the folding of B, C, D_infinity as linear forms,
    the induction for A_infinity^infinity on 200 sequences).
4.6 (pp. 120-124)
  * Reflections have order 2, preserve the form and fix the hyperplane
    (Dynkin <= 8, Euclidean <= 7 vertices); Lemma 4.6.2 for all labels
    (a, b), a, b <= 4, and all pairs in the Dynkin diagrams <= 6 vertices.
  * Proposition 4.6.3: the three printed expressions for the norm agree
    identically, null space = <n> (Euclidean, <= 9 vertices); (ii) as
    printed ("semidefinite") refuted by every Dynkin diagram <= 8
    vertices, corrected "semidefinite and not definite" holds.
  * Proposition 4.6.4, Definition 4.6.7, Lemma 4.6.8 for every finite
    Dynkin diagram with <= 8 vertices: |W|, |Phi| (Humphreys), no fixed
    vector, Phi = -Phi closed under the w_v, (i)-(iv) for every root and
    pair of roots, rho commutes with the reflections; W finite on
    R^T/<n> for the Euclidean diagrams <= 9 vertices.
  * Coxeter transformations of the Dynkin diagrams (all orders for <= 6
    vertices, 120 random orders otherwise): order h of Humphreys' table,
    no fixed point, sum c^i = 0, no root stays positive (Lemma 4.6.9);
    conjugate in W for <= 5 vertices (Exercise).  Euclidean (all orders
    for <= 6 vertices, 60 random otherwise): c^h = 1 + n partial_c,
    partial_c != 0, partial_c c = partial_c, partial_c(n) = 0 (the printed
    splitting R^T = Ker(partial_c) (+) <n> refuted); Lemma 4.6.6 on the
    basis vectors.
4.7 (pp. 124-128)
  * Definition 4.7.2 for all 156 orientations of the connected graphs on
    3 and 4 vertices; s_1 ... s_n Q = Q.
  * The corrected display for dim W_y on the modulation GF(2), GF(4) of
    B_2 (the printed coefficient refuted); the k-dimensions of p. 125.
  * Theorem 4.7.6 (Gabriel) for 12 Dynkin quivers (A1-A5, D4, D5, E6) over
    GF(2), GF(3) (not E6), GF(4) (A2, A3, D4): the modules (C^-)^(m-1)
    S_n^- ... S_(i+1)^- (S_i) of the proof are bricks, one for each
    positive root, with dimension vector c^(-m+1) w_n ... w_(i+1)(v_i),
    and sum 1/|Aut M| = q^(dim Rep d)/|GL(d)| for every d below the
    highest root (+1 for A_n, n <= 4, and D4 over GF(2)), so they are all
    the indecomposables there.  Proposition 4.7.3 (S_y killed, not S_x)
    and Lemma 4.7.5 on all of them over GF(2); the converse root
    combinatorics for every Dynkin diagram with <= 8 vertices.
  * Proposition 4.7.1: the null roots satisfy sum n_x^2 f_x = sum n_x n_y
    _y d_x f_x; D~4 has q + 4 indecomposables of dimension (2; 1, 1, 1, 1)
    over GF(2), GF(3).

Not established: none of the general theorems is proved here.  Every
check concerns the listed quivers, fields, graphs, dimensions and modules
only.  Representations of quivers are compared by exact Hom spaces,
modules of groups by the MeatAxe.  Nothing here compares our Typst text
with the printed book.

Run with:  sage -python checks/sage/chapter-4a.py
"""
import itertools
import random

from sage.all import (
    GF, QQ, ZZ, AlternatingGroup, FractionField, PolynomialRing, factorial,
    gcd, lcm, libgap, prod, set_random_seed, vector,
)
from sage.all import identity_matrix as _identity_matrix
from sage.all import matrix as dmatrix

SCOPE = 'chapter-4a'
COUNT = [0]
random.seed(20261104)
set_random_seed(20261104)


# Products of dense matrices over finite rings of odd characteristic go
# through the local OpenBLAS build, which stops with SIGILL on some
# machines; such matrices are created sparse (exact all the same).  Ranks
# and kernels are computed on dense copies (no products).
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


def sp(A):
    return A.sparse_matrix() if _sparse(A.base_ring()) else A


def rank(A):
    return A.dense_matrix().rank() if A.nrows() and A.ncols() else 0


def check(cond, what):
    """One check of a statement of the book; fails loudly."""
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    """The printed reading, kept beside the corrected one: it must fail."""
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gl_order(m, q):
    return prod([q ** m - q ** i for i in range(m)])
# ===========================================================================
# Labelled graphs (Definitions 4.1.9, 4.5.1, 4.5.3, 4.5.4)
# ===========================================================================
#
# A labelled graph on the vertices 0..n-1 is a list of edges (x, y, a, b)
# with a = _x d_y and b = _y d_x (Definition 4.1.9); several edges may join
# the same two vertices.  The book's double and triple arrows x => y stand
# for the labels (2, 1) and (3, 1) of the edge x - y (p. 116).

S1 = (1, 1)


def chain(*values, start=0):
    """The path start - start+1 - ... with the given labels."""
    return [(start + k, start + k + 1, a, b)
            for k, (a, b) in enumerate(values)]


class LGraph:
    def __init__(self, n, edges, name=''):
        self.n, self.edges, self.name = n, list(edges), name

    def cartan(self):
        """c_xy = 2 delta_xy - sum over edges x - y of _x d_y (Def. 4.5.3)."""
        c = [[2 if x == y else 0 for y in range(self.n)]
             for x in range(self.n)]
        for x, y, a, b in self.edges:
            c[x][y] -= a
            c[y][x] -= b
        return matrix(ZZ, c)

    def valuation(self):
        """Positive integers f_x with _x d_y f_y = _y d_x f_x on every edge
        (Definition 4.1.9), normalised to have gcd 1; None if none exist."""
        f = [None] * self.n
        f[0] = QQ(1)
        changed = True
        while changed:
            changed = False
            for x, y, a, b in self.edges:
                if f[x] is not None and f[y] is None:
                    f[y] = f[x] * b / a
                    changed = True
                elif f[y] is not None and f[x] is None:
                    f[x] = f[y] * a / b
                    changed = True
        if any(v is None for v in f):
            return None
        if any(a * f[y] != b * f[x] for x, y, a, b in self.edges):
            return None
        den = lcm([v.denominator() for v in f])
        f = [ZZ(v * den) for v in f]
        g = gcd(f)
        return [v // g for v in f]

    def sym(self):
        """The symmetrised Cartan matrix c~_xy = c_xy f_y."""
        f = self.valuation()
        c = self.cartan()
        return matrix(QQ, self.n, self.n,
                      lambda x, y: c[x, y] * f[y])

    def op(self):
        return LGraph(self.n, [(x, y, b, a) for x, y, a, b in self.edges],
                      self.name + '^op')

    def adjacency(self):
        """For each ordered pair (x, y), x != y, the list of labels
        (_x d_y, _y d_x) of the edges x - y."""
        adj = {}
        for x, y, a, b in self.edges:
            adj.setdefault((x, y), []).append((a, b))
            adj.setdefault((y, x), []).append((b, a))
        return adj


def is_connected(n, edges):
    seen, todo = {0}, [0]
    while todo:
        v = todo.pop()
        for x, y, a, b in edges:
            for s, t in ((x, y), (y, x)):
                if s == v and t not in seen:
                    seen.add(t)
                    todo.append(t)
    return len(seen) == n


def smaller(T1, T2, strict=False):
    """Is T1 smaller than T2 (p. 117): an injective morphism of graphs
    rho with _x d_y <= _rho(x) d_rho(y) on every edge?  The edges of T1
    between two vertices are mapped injectively to edges of T2 between their
    images.  With strict=True, rho must not be an isomorphism."""
    n1, n2 = T1.n, T2.n
    if n1 > n2:
        return False
    A1, A2 = T1.adjacency(), T2.adjacency()

    def edge_ok(l1, l2):
        # an injective assignment of the edges l1 to the edges l2 with
        # componentwise larger labels (lists of length <= 2 here)
        for perm in itertools.permutations(range(len(l2)), len(l1)):
            if all(l1[i][0] <= l2[p][0] and l1[i][1] <= l2[p][1]
                   for i, p in enumerate(perm)):
                return True
        return False

    order = sorted(range(n1), key=lambda v: -len(
        [1 for (x, y) in A1 if x == v]))
    rho = {}

    def extend(k):
        if k == n1:
            if not strict:
                return True
            if n1 < n2:
                return True
            # same number of vertices: rho is bijective; an isomorphism iff
            # it carries the edges onto the edges with equal labels
            same = len(T1.edges) == len(T2.edges) and all(
                sorted(A1.get((x, y), [])) == sorted(
                    A2.get((rho[x], rho[y]), []))
                for x in range(n1) for y in range(n1) if x != y)
            return not same
        v = order[k]
        for w in range(n2):
            if w in rho.values():
                continue
            ok = True
            for u, rw in rho.items():
                l1 = A1.get((v, u), [])
                if l1 and not edge_ok(l1, A2.get((w, rw), [])):
                    ok = False
                    break
            if ok:
                rho[v] = w
                if extend(k + 1):
                    return True
                del rho[v]
        return False

    return extend(0)


def isomorphic_lg(T1, T2):
    return (T1.n == T2.n and len(T1.edges) == len(T2.edges)
            and sorted(sorted((a, b)) for _, _, a, b in T1.edges)
            == sorted(sorted((a, b)) for _, _, a, b in T2.edges)
            and smaller(T1, T2) and smaller(T2, T1))


# The finite Dynkin diagrams of Definition 4.5.1 (i) with n vertices, as
# printed on p. 116 (B_n: the double arrow points to the end vertex).
def dynkin(name, n=None):
    if name == 'A':
        return LGraph(n, chain(*[S1] * (n - 1)), 'A%d' % n)
    if name == 'B':
        return LGraph(n, chain((1, 2), *[S1] * (n - 2)), 'B%d' % n)
    if name == 'C':
        return LGraph(n, chain((2, 1), *[S1] * (n - 2)), 'C%d' % n)
    if name == 'D':
        return LGraph(n, chain(*[S1] * (n - 2)) + [(1, n - 1, 1, 1)],
                      'D%d' % n)
    if name == 'E':
        return LGraph(n, chain(*[S1] * (n - 2)) + [(2, n - 1, 1, 1)],
                      'E%d' % n)
    if name == 'F4':
        return LGraph(4, chain(S1, (2, 1), S1), 'F4')
    if name == 'G2':
        return LGraph(2, chain((3, 1)), 'G2')


def dynkin_list(maxn):
    out = []
    for n in range(1, maxn + 1):
        out.append(dynkin('A', n))
        if n >= 2:
            out += [dynkin('B', n), dynkin('C', n)]
        if n >= 3:
            out.append(dynkin('D', n))
        if n in (6, 7, 8):
            out.append(dynkin('E', n))
    out += [dynkin('F4'), dynkin('G2')]
    return [T for T in out if T.n <= maxn]


# The Euclidean diagrams of Definition 4.5.1 (iii) with n + 1 vertices and
# the numbers printed at their vertices (pp. 116-117), except E~_8, whose
# printed number at the end of the vertical branch is 1 (see E8_PRINTED).
def euclidean(name, n=None):
    if name == 'A':
        edges = chain(*[S1] * n) if n > 1 else []
        edges = edges + [(0, n, 1, 1)] if n > 1 else [(0, 1, 1, 1)] * 2
        return LGraph(n + 1, edges, '~A%d' % n), [1] * (n + 1)
    if name == 'A11':
        return LGraph(2, [(0, 1, 1, 4)], '~A11'), [2, 1]
    if name == 'A12':
        return LGraph(2, [(0, 1, 2, 2)], '~A12'), [1, 1]
    if name == 'B':
        return (LGraph(n + 1, chain((1, 2), *[S1] * (n - 2), (2, 1)),
                       '~B%d' % n), [1] * (n + 1))
    if name == 'C':
        return (LGraph(n + 1, chain((2, 1), *[S1] * (n - 2), (1, 2)),
                       '~C%d' % n), [1] + [2] * (n - 1) + [1])
    if name == 'D':
        edges = chain(*[S1] * (n - 2)) + [(1, n - 1, 1, 1),
                                          (n - 3, n, 1, 1)]
        return (LGraph(n + 1, edges, '~D%d' % n),
                [1] + [2] * (n - 3) + [1, 1, 1])
    if name == 'BC':
        return (LGraph(n + 1, chain((1, 2), *[S1] * (n - 2), (1, 2)),
                       '~BC%d' % n), [2] * n + [1])
    if name == 'BD':
        edges = chain((1, 2), *[S1] * (n - 2)) + [(n - 2, n, 1, 1)]
        return LGraph(n + 1, edges, '~BD%d' % n), [2] * (n - 1) + [1, 1]
    if name == 'CD':
        edges = chain((2, 1), *[S1] * (n - 2)) + [(n - 2, n, 1, 1)]
        return (LGraph(n + 1, edges, '~CD%d' % n),
                [1] + [2] * (n - 2) + [1, 1])
    if name == 'E6':
        return (LGraph(7, chain(*[S1] * 4) + [(2, 5, 1, 1), (5, 6, 1, 1)],
                       '~E6'), [1, 2, 3, 2, 1, 2, 1])
    if name == 'E7':
        return (LGraph(8, chain(*[S1] * 6) + [(3, 7, 1, 1)], '~E7'),
                [1, 2, 3, 4, 3, 2, 1, 2])
    if name == 'E8':
        return (LGraph(9, chain(*[S1] * 7) + [(5, 8, 1, 1)], '~E8'),
                [1, 2, 3, 4, 5, 6, 4, 2, 3])
    if name == 'F41':
        return LGraph(5, chain(S1, S1, (1, 2), S1), '~F41'), [1, 2, 3, 2, 1]
    if name == 'F42':
        return LGraph(5, chain(S1, S1, (2, 1), S1), '~F42'), [1, 2, 3, 4, 2]
    if name == 'G21':
        return LGraph(3, chain(S1, (1, 3)), '~G21'), [1, 2, 1]
    if name == 'G22':
        return LGraph(3, chain(S1, (3, 1)), '~G22'), [1, 2, 3]


E8_PRINTED = [1, 2, 3, 4, 5, 6, 4, 2, 1]

# smallest members of the series for which the picture makes sense
SERIES_MIN = {'A': 1, 'B': 2, 'C': 2, 'D': 4, 'BC': 2, 'BD': 3, 'CD': 3}


def euclidean_list(maxv):
    """All Euclidean diagrams with at most maxv vertices (A~_0, a loop, is
    left out: Definition 4.6.1 excludes loops)."""
    out = []
    for s, m in SERIES_MIN.items():
        for n in range(m, maxv):
            out.append(euclidean(s, n))
    for s in ('A11', 'A12', 'E6', 'E7', 'E8', 'F41', 'F42', 'G21', 'G22'):
        T, marks = euclidean(s)
        if T.n <= maxv:
            out.append((T, marks))
    return out


def is_additive(T, marks):
    c = T.cartan()
    return all(sum(marks[x] * c[x, y] for x in range(T.n)) == 0
               for y in range(T.n))


def posdef(S):
    return all(S.matrix_from_rows_and_columns(list(range(k)),
                                              list(range(k))).det() > 0
               for k in range(1, S.nrows() + 1))


def possemidef(S):
    n = S.nrows()
    for k in range(1, n + 1):
        for I in itertools.combinations(range(n), k):
            if S.matrix_from_rows_and_columns(list(I), list(I)).det() < 0:
                return False
    return True


def reflections(T):
    """The matrices of w_x on coordinates: w_x(v) = v - (sum_y a_y c_yx) v_x
    for v = sum a_y v_y, since (v, v_x) = sum_y a_y c_yx f_x and
    (v_x, v_x) = 2 f_x (Definition 4.6.1)."""
    c = T.cartan()
    out = []
    for x in range(T.n):
        W = _identity_matrix(ZZ, T.n)
        for y in range(T.n):
            W[x, y] -= c[y, x]
        out.append(W)
    return out


def roots(T):
    """The images of the basis vectors under W(T) (Definition 4.6.7)."""
    Ws = reflections(T)
    start = [tuple(1 if i == x else 0 for i in range(T.n))
             for x in range(T.n)]
    seen = set(start)
    todo = list(start)
    while todo:
        v = vector(ZZ, todo.pop())
        for W in Ws:
            u = tuple(W * v)
            if u not in seen:
                seen.add(u)
                todo.append(u)
                if len(seen) > 5000:
                    raise ValueError('root system too large')
    return sorted(seen)


def is_positive(v):
    return all(a >= 0 for a in v) and any(a != 0 for a in v)


def coxeter(Ws, order):
    c = _identity_matrix(ZZ, len(Ws))
    for x in order:
        c = c * Ws[x]
    return c


def matrix_order(c, bound=400):
    I = _identity_matrix(c.base_ring(), c.nrows())
    P = c
    for k in range(1, bound + 1):
        if P == I:
            return k
        P = P * c
    return None


# Humphreys (1990), 2.11 Table 2 and 3.18 Table 2: |W|, |Phi|, h.
def humphreys_data(T):
    name, n = T.name, T.n
    if name.startswith('A'):
        return factorial(n + 1), n * (n + 1), n + 1
    if name.startswith('B') or name.startswith('C'):
        return 2 ** n * factorial(n), 2 * n * n, 2 * n
    if name.startswith('D'):
        return 2 ** (n - 1) * factorial(n), 2 * n * (n - 1), 2 * (n - 1)
    return {'E6': (51840, 72, 12), 'E7': (2903040, 126, 18),
            'E8': (696729600, 240, 30), 'F4': (1152, 48, 12),
            'G2': (12, 12, 6)}[name]


def perron_vector(S):
    """A non-negative integral approximation of an eigenvector for the
    smallest eigenvalue of the symmetric matrix S (exactness of whatever is
    concluded from it is checked by the caller)."""
    from sage.all import RDF
    ev = S.change_ring(RDF).eigenvectors_right()
    lam, vecs, _ = min(ev, key=lambda t: t[0])
    v = vecs[0]
    if sum(v) < 0:
        v = -v
    m = max(abs(a) for a in v)
    return vector(ZZ, [max(0, int(round(float(1000 * a / m)))) for a in v])


def section_4_5_and_4_6():
    # ---------------- 4.5: the diagrams and their numbers ----------------
    for T, marks in euclidean_list(10):
        check(is_additive(T, marks),
              'Def 4.5.1 (iii), proof of Lemma 4.5.5 (i) (pp. 116-117, '
              'def:dynkin-euclidean): the printed numbers on %s form an '
              'additive function' % T.name)
        check(T.valuation() is not None,
              'Def 4.5.1 (iii): %s is a valued graph' % T.name)
    E8t, E8marks = euclidean('E8')
    refuted(is_additive(E8t, E8_PRINTED),
            'Def 4.5.1 (iii) (p. 117): the printed 1 at the end of the '
            'vertical branch of E~_8 gives an additive function')
    c = E8t.cartan()
    check(sum(E8_PRINTED[x] * c[x, 5] for x in range(9)) == 2
          and sum(E8_PRINTED[x] * c[x, 8] for x in range(9)) == -4
          and sum(E8marks[x] * c[x, 5] for x in range(9)) == 0
          and sum(E8marks[x] * c[x, 8] for x in range(9)) == 0,
          'E~_8 (p. 117): with the printed 1, sum_x n_x c_xy is 2 at the '
          'branch vertex (6) and 2 - 6 = -4 < 0 at the end of the branch '
          '(not even subadditive); with 3 both are 0')
    # infinite Dynkin diagrams, truncated (the cut vertex is not checked)
    N = 12
    inf = [
        ('A_inf', LGraph(N, chain(*[S1] * (N - 1))), list(range(1, N + 1)),
         [N - 1]),
        ('B_inf', LGraph(N, chain((1, 2), *[S1] * (N - 2))), [1] * N,
         [N - 1]),
        ('C_inf', LGraph(N, chain((2, 1), *[S1] * (N - 2))),
         [1] + [2] * (N - 1), [N - 1]),
        ('D_inf', LGraph(N + 1, chain(*[S1] * (N - 1)) + [(1, N, 1, 1)]),
         [1] + [2] * (N - 1) + [1], [N - 1]),
        ('A_inf^inf', LGraph(N, chain(*[S1] * (N - 1))), [1] * N,
         [0, N - 1]),
    ]
    for name, T, marks, cut in inf:
        cc = T.cartan()
        check(all(sum(marks[x] * cc[x, y] for x in range(T.n)) == 0
                  for y in range(T.n) if y not in cut),
              'Def 4.5.1 (ii), Prop 4.5.7 (pp. 116, 119): the printed '
              'numbers on %s are additive (%d vertices)' % (name, T.n))
    check(dynkin('F4').cartan() == matrix(ZZ, [[2, -1, 0, 0], [-1, 2, -2, 0],
                                               [0, -1, 2, -1], [0, 0, -1, 2]]),
          'Cartan matrix of F4 printed after Def 4.5.3 (p. 118)')
    # coincidences in the lists (p. 117)
    check(isomorphic_lg(dynkin('B', 2), dynkin('C', 2))
          and isomorphic_lg(dynkin('A', 3), dynkin('D', 3)),
          'p. 117: B2 = C2 and A3 = D3')
    dl = dynkin_list(9)
    pairs = 0
    for T1, T2 in itertools.combinations(dl, 2):
        if T1.n == T2.n and {T1.name, T2.name} not in ({'B2', 'C2'},
                                                       {'A3', 'D3'}):
            pairs += 1
            check(not isomorphic_lg(T1, T2),
                  'p. 117: no further duplication (%s, %s)'
                  % (T1.name, T2.name))
    el = [T for T, _ in euclidean_list(9)]
    for T1, T2 in itertools.combinations(el, 2):
        if T1.n == T2.n:
            pairs += 1
            check(not isomorphic_lg(T1, T2),
                  'Def 4.5.1 (iii): %s and %s are different'
                  % (T1.name, T2.name))
    for T, marks in euclidean_list(9):
        To = T.op()
        check(any(isomorphic_lg(To, E) for E in el if E.n == T.n),
              'proof of Lemma 4.5.5 (iii): the opposite of %s is Euclidean'
              % T.name)
        f, fo = T.valuation(), To.valuation()
        Nn = lcm(f)
        check(fo == [Nn // v for v in f] or
              len(set(fo[i] * f[i] for i in range(T.n))) == 1,
              'Def 4.5.4: T^op is valued by N/f_x (%s)' % T.name)
        # Lemma 4.5.5 (ii) hypothesis for T^op: an additive function on
        # T^op is a positive n' with sum_y c_xy n'_y = 0
        K = T.cartan().right_kernel().basis()
        check(len(K) == 1 and (all(a > 0 for a in K[0])
                               or all(a < 0 for a in K[0])),
              'Lemma 4.5.5 (ii), (iii): T^op of %s admits an additive '
              'function' % T.name)
    # Proposition 4.5.7 (ii): the folding scheme, as linear forms
    R = PolynomialRing(QQ, ['n0', 'm0', 'n1', 'n2', 'n3'])
    n0, m0, n1, n2, n3 = R.gens()
    # B_inf: subadditivity at 0, 1 is 2n0 - 2n1 >= 0, -n0 + 2n1 - n2 >= 0
    check((2 * n0 - n1 - n1) == (2 * n0 - 2 * n1)
          and (2 * n1 - n0 - n2) == (-n0 + 2 * n1 - n2),
          'Prop 4.5.7 (ii): folding B_inf to A_inf^inf (middle n0)')
    # C_inf: at 0, 1: 2n0 - n1, -2n0 + 2n1 - n2; middle 2n0
    check((2 * (2 * n0) - 2 * n1) == 2 * (2 * n0 - n1)
          and (2 * n1 - 2 * n0 - n2) == (-2 * n0 + 2 * n1 - n2),
          'Prop 4.5.7 (ii): folding C_inf to A_inf^inf (middle 2 n0)')
    # D_inf: at 0, 0', 1: 2n0 - n1, 2m0 - n1, 2n1 - n0 - m0 - n2
    check((2 * (n0 + m0) - 2 * n1) == (2 * n0 - n1) + (2 * m0 - n1)
          and (2 * n1 - (n0 + m0) - n2) == (2 * n1 - n0 - m0 - n2),
          'Prop 4.5.7 (ii): folding D_inf to A_inf^inf (middle n0 + n0\')')
    # the induction of the proof for A_inf^inf on random concave sequences
    for _ in range(200):
        seq = [QQ(random.randint(50, 80))]
        d = QQ(random.randint(-3, 3))
        for j in range(15):
            seq.append(seq[-1] + d)
            d -= QQ(random.randint(0, 2))
        j = random.randint(1, 15)
        if seq[j - 1] < seq[j]:
            for r in range(j + 1):
                assert seq[j - r] <= seq[j] - r * (seq[j] - seq[j - 1])
    check(True, 'Prop 4.5.7 (ii): n_(j-r) <= n_j - r (n_j - n_(j-1)) on 200 '
          'random subadditive sequences')
    # Lemma 4.5.6: each finite Dynkin diagram is strictly smaller than a
    # Euclidean one, and the restriction is subadditive, not additive
    eul = euclidean_list(10)
    for D in dynkin_list(8):
        found = None
        for E, marks in eul:
            if E.n == D.n + 1 and smaller(D, E, strict=True):
                found = (E, marks)
                break
        check(found is not None,
              'proof of Prop 4.6.3: %s is strictly smaller than a '
              'Euclidean diagram' % D.name)
        E, marks = found
        # an explicit embedding: restrict the additive function
        rho = _embedding(D, E)
        cD = D.cartan()
        vals = [sum(marks[rho[x]] * cD[x, y] for x in range(D.n))
                for y in range(D.n)]
        check(all(v >= 0 for v in vals) and any(v > 0 for v in vals),
              'Lemma 4.5.6: the additive function of %s restricted to %s '
              'is subadditive, not additive' % (E.name, D.name))

    # ------- Lemma 4.5.2, Proposition 4.6.3, Theorem 4.5.8 (finite) -------
    stats = _classify_small_graphs()

    # ---------------------- 4.6: reflections, roots ----------------------
    for T in dynkin_list(8) + [E for E, _ in euclidean_list(7)]:
        Ws = reflections(T)
        S = T.sym()
        for x, W in enumerate(Ws):
            WQ = W.change_ring(QQ)
            ok = (W * W == 1 and WQ.transpose() * S * WQ == S
                  and rank(W - 1) == 1
                  and (W - 1).change_ring(QQ).column_space()
                  == span_basis(T.n, x)
                  and all(W * k == k for k in
                          dmatrix(QQ, [list(S.row(x))]).right_kernel()
                          .basis()))
            check(ok, 'Def 4.6.1 (p. 120): w_x has order 2, preserves '
                  '( , ), fixes the hyperplane perpendicular to v_x '
                  '(%s, x = %d)' % (T.name, x))
    # Lemma 4.6.2 on two-vertex graphs (a, b) and non-adjacent pairs
    expect = {0: 2, 1: 3, 2: 4, 3: 6}
    for a in range(1, 5):
        for b in range(1, 5):
            T = LGraph(2, [(0, 1, a, b)])
            Ws = reflections(T)
            P = Ws[0] * Ws[1]
            c = T.cartan()
            m = c[0, 1] * c[1, 0]
            if m in expect:
                check(matrix_order(P, 12) == expect[m],
                      'Lemma 4.6.2: w_x w_y has order %d for c_xy c_yx = '
                      '%d' % (expect[m], m))
            else:
                cp = P.charpoly()
                xx = cp.parent().gen()
                if m == 4:
                    # unipotent and not 1: infinite order
                    infinite = cp == (xx - 1) ** 2 and P != 1
                else:
                    # an eigenvalue which is not a root of unity
                    infinite = any(not f.is_cyclotomic()
                                   for f, _ in cp.factor())
                check(infinite,
                      'Lemma 4.6.2: w_x w_y has infinite order for '
                      'c_xy c_yx = %d' % m)
    for T in dynkin_list(6):
        Ws = reflections(T)
        c = T.cartan()
        for x, y in itertools.combinations(range(T.n), 2):
            m = c[x, y] * c[y, x]
            check(matrix_order(Ws[x] * Ws[y], 12) == expect[m],
                  'Lemma 4.6.2 in %s (x = %d, y = %d)' % (T.name, x, y))

    # Proposition 4.6.3: the norm identity for Euclidean diagrams
    for T, marks in euclidean_list(9):
        n = T.n
        R = PolynomialRing(QQ, ['a%d' % i for i in range(n)])
        a = R.gens()
        c = T.cartan()
        f = T.valuation()
        S = T.sym()
        lhs = sum(a[x] * a[y] * S[x, y] for x in range(n) for y in range(n))
        line1 = (2 * sum(a[x] ** 2 * f[x] for x in range(n))
                 + sum(a[x] * a[y] * c[x, y] * f[y]
                       for x in range(n) for y in range(n) if x != y))
        line2 = (-QQ(1) / 2 * sum(
            a[x] ** 2 * marks[y] * c[y, x] * f[x] / marks[x]
            + a[y] ** 2 * marks[x] * c[x, y] * f[y] / marks[y]
            for x in range(n) for y in range(n) if x != y)
            + sum(a[x] * a[y] * c[x, y] * f[y]
                  for x in range(n) for y in range(n) if x != y))
        line3 = -QQ(1) / 2 * sum(
            marks[x] * marks[y] * c[x, y] * f[y]
            * (a[x] / marks[x] - a[y] / marks[y]) ** 2
            for x in range(n) for y in range(n) if x != y)
        check(lhs == line1 == line2 == line3,
              'proof of Prop 4.6.3 (p. 121): the three expressions for the '
              'norm agree identically (%s)' % T.name)
        K = S.right_kernel().basis()
        check(len(K) == 1 and vector(QQ, marks) in S.right_kernel(),
              'Prop 4.6.3 (ii): the null vectors of %s are the multiples of '
              'the printed n' % T.name)
    for D in dynkin_list(8):
        S = D.sym()
        isE = any(isomorphic_lg(D, E) for E, _ in euclidean_list(9))
        printed = possemidef(S)       # the printed right-hand side of (ii)
        refuted(printed == isE,
                'Prop 4.6.3 (ii) as printed ("semidefinite"): %s is '
                'positive semidefinite but not Euclidean' % D.name)
        check((possemidef(S) and not posdef(S)) == isE,
              'Prop 4.6.3 (ii) corrected (semidefinite and not definite) '
              'for %s' % D.name)

    # Proposition 4.6.4, Definition 4.6.7, Lemma 4.6.8: root systems
    for T in dynkin_list(8):
        Ws = reflections(T)
        Phi = roots(T)
        order_W, nroots, h = humphreys_data(T)
        check(len(Phi) == nroots,
              'Def 4.6.7: |Phi(%s)| = %d (Humphreys 2.11 Table 2)'
              % (T.name, nroots))
        idx = {v: i for i, v in enumerate(Phi)}
        perms = [libgap.PermList([idx[tuple(W * vector(ZZ, v))] + 1
                                  for v in Phi]) for W in Ws]
        check(libgap.Group(perms).Size() == order_W,
              'Prop 4.6.4 (i): W(%s) is finite of order %d (Humphreys 2.11 '
              'Table 2)' % (T.name, order_W))
        fixed = dmatrix(ZZ, sum([list(W - 1) for W in Ws], []))
        check(fixed.right_kernel().dimension() == 0,
              'Prop 4.6.4 (i): no non-zero vector of R^%s is fixed by W'
              % T.name)
        S = T.sym()
        Phiset = set(Phi)
        ok_i = all(tuple(-a for a in v) in Phiset for v in Phi)
        ok_int = True
        ok_refl = True
        for v in Phi:
            vv = vector(QQ, v)
            nv = vv * S * vv
            for u in Phi:
                uu = vector(QQ, u)
                k = 2 * (uu * S * vv) / nv
                if k not in ZZ:
                    ok_int = False
                if tuple(uu - k * vv) not in Phiset:
                    ok_refl = False
        check(ok_i and ok_int and ok_refl,
              'Def 4.6.7, Lemma 4.6.8 (i): Phi(%s) = -Phi, the reflections '
              'w_v permute Phi, 2(u, v)/(v, v) is an integer' % T.name)
        ok_ii = True
        for v, u in itertools.combinations(Phi, 2):
            vv, uu = vector(QQ, v), vector(QQ, u)
            if rank(dmatrix(QQ, [v, u])) < 2:
                continue
            p = vv * S * uu
            if p > 0:
                if not (uu * S * uu == 2 * p or vv * S * vv == 2 * p):
                    ok_ii = False
                if tuple(vv - uu) not in Phiset:
                    ok_ii = False
        check(ok_ii, 'Lemma 4.6.8 (ii): for all pairs of roots of %s with '
              '(v, v\') > 0' % T.name)
        ok_iii = all(is_positive(Ws[x] * vector(ZZ, v)) or
                     tuple(v) == tuple(1 if i == x else 0
                                       for i in range(T.n))
                     for v in Phi if is_positive(v) for x in range(T.n))
        ok_iv = all(is_positive(v) or is_positive([-a for a in v])
                    for v in Phi)
        check(ok_iii and ok_iv,
              'Lemma 4.6.8 (iii), (iv) for every root of %s' % T.name)
        # rho: R^T -> R^(T^op) commutes with the reflections (proof of (iii))
        f = T.valuation()
        rho = dmatrix(ZZ, T.n, T.n, lambda i, j: f[i] if i == j else 0)
        Wo = reflections(T.op())
        check(all(rho * Ws[x] == Wo[x] * rho for x in range(T.n)),
              'proof of Lemma 4.6.8 (iii): rho commutes with the reflections '
              '(%s)' % T.name)

        # Coxeter transformations (Def 4.6.5, Lemma 4.6.9)
        orders = (list(itertools.permutations(range(T.n))) if T.n <= 6
                  else [random.sample(range(T.n), T.n) for _ in range(120)])
        seen = {}
        ok = True
        for o in orders:
            c = coxeter(Ws, o)
            key = tuple(c.list())
            if key in seen:
                continue
            seen[key] = c
            hh = matrix_order(c, 60)
            tot = sum([c ** i for i in range(hh)], 0 * c)
            if not (hh == h and (c - 1).det() != 0 and tot == 0):
                ok = False
            # Lemma 4.6.9 (ii) for the roots: some c^m(v) is not positive
            for v in Phi:
                w = vector(ZZ, v)
                for m in range(hh + 1):
                    if not is_positive(w):
                        break
                    w = c * w
                else:
                    ok = False
        check(ok, 'Def 4.6.5, Lemma 4.6.9: every Coxeter transformation of '
              '%s (%d orders, %d distinct) has order h = %d (Humphreys 3.18 '
              'Table 2), no non-zero fixed point, sum_(i<h) c^i = 0, and no '
              'root stays positive' % (T.name, len(orders), len(seen), h))
        if T.n <= 5:
            G = libgap.Group(perms)
            cs = list(seen.values())

            def perm_of(c):
                return libgap.PermList([idx[tuple(c * vector(ZZ, v))] + 1
                                        for v in Phi])
            p0 = perm_of(cs[0])
            check(all(libgap.IsConjugate(G, p0, perm_of(cc)) for cc in cs),
                  'Exercise after Def 4.6.5: the %d Coxeter transformations '
                  'of the tree %s are conjugate in W' % (len(cs), T.name))

    # Euclidean: W(T) finite on R^T/<n>, Coxeter number and defect
    for T, marks in euclidean_list(9):
        Ws = reflections(T)
        nvec = vector(ZZ, marks)
        check(all(W * nvec == nvec for W in Ws),
              'Prop 4.6.4 (ii): W(%s) fixes n' % T.name)
        x0 = marks.index(1)

        def norm(v):
            return tuple(vector(ZZ, v) - v[x0] * nvec)
        start = [norm([1 if i == x else 0 for i in range(T.n)])
                 for x in range(T.n)]
        seen = set(start)
        todo = list(start)
        while todo and len(seen) <= 3000:
            v = vector(ZZ, todo.pop())
            for W in Ws:
                u = norm(W * v)
                if u not in seen:
                    seen.add(u)
                    todo.append(u)
        check(len(seen) <= 3000,
              'Prop 4.6.4 (ii): the basis vectors of %s have finitely many '
              'images in R^T/<n> (%d)' % (T.name, len(seen)))
        orders = (list(itertools.permutations(range(T.n))) if T.n <= 6
                  else [random.sample(range(T.n), T.n) for _ in range(60)])
        done = set()
        ok = True
        hs = set()
        direct = False
        for o in orders:
            c = coxeter(Ws, o)
            key = tuple(c.list())
            if key in done:
                continue
            done.add(key)
            P, hh = c, 1
            while True:
                D = P - 1
                if all(D[i, j] * marks[k] == D[k, j] * marks[i]
                       for i in range(T.n) for k in range(T.n)
                       for j in range(T.n)):
                    break
                P, hh = P * c, hh + 1
                assert hh < 500
            hs.add(hh)
            phi = vector(QQ, [D[x0, j] / marks[x0] for j in range(T.n)])
            # c^h = 1 + n phi, phi(n) = 0, phi != 0, phi c = phi
            if not (P == 1 + dmatrix(QQ, T.n, 1, list(nvec))
                    * dmatrix(QQ, 1, T.n, list(phi))
                    and phi * nvec == 0 and phi != 0
                    and phi * c == phi):
                ok = False
            # the printed splitting R^T = Ker(partial_c) (+) <n> is direct
            # iff partial_c(n) != 0
            if phi * nvec != 0:
                direct = True
            # Lemma 4.6.6 on the basis vectors
            for x in range(T.n):
                v = vector(ZZ, [1 if i == x else 0 for i in range(T.n)])
                d = phi[x]
                if d == 0:
                    if P * v != v:
                        ok = False
                else:
                    k = 1
                    while True:
                        w = (P ** k) * v if d < 0 else (P ** k).inverse() * v
                        if any(a < 0 for a in w):
                            break
                        k += 1
                        assert k < 100
        check(ok, 'Def 4.6.5, Lemma 4.6.6 for %s (%d Coxeter '
              'transformations, h in %s): c^h(v) = v + partial_c(v) n with '
              'partial_c != 0, c-invariant; v_x has finitely many images iff '
              'partial_c(v_x) = 0, otherwise c^(kh)(v_x) has a negative '
              'coordinate' % (T.name, len(done), sorted(hs)))
        refuted(direct,
                'Def 4.6.5 (p. 122) as printed: R^T = Ker(partial_c) (+) <n> '
                'for %s (but partial_c(n) = 0, so n lies in the kernel)'
                % T.name)
        # Proposition 4.7.1: the inequality for the null root
        f = T.valuation()
        lhs = sum(marks[x] ** 2 * f[x] for x in range(T.n))
        rhs = sum(marks[x] * marks[y] * b * f[x] for x, y, a, b in T.edges)
        check(lhs == rhs and vector(QQ, marks) * T.sym() * vector(
            QQ, marks) == 2 * (lhs - rhs),
            'proof of Prop 4.7.1 (pp. 124-125): sum n_x^2 f_x = sum over '
            'edges n_x n_y _y d_x f_x for the null root of %s, and '
            '(v, v) = 2 (difference)' % T.name)
    return stats


def span_basis(n, x):
    return (QQ ** n).subspace([[1 if i == x else 0 for i in range(n)]])


def _embedding(T1, T2):
    """An explicit injective morphism T1 -> T2 with larger labels."""
    A1, A2 = T1.adjacency(), T2.adjacency()
    for img in itertools.permutations(range(T2.n), T1.n):
        if all(any(all(l[i][0] <= m[p][0] and l[i][1] <= m[p][1]
                       for i, p in enumerate(perm))
                   for perm in itertools.permutations(range(len(m)), len(l)))
               for (x, y), l in A1.items()
               for m in [A2.get((img[x], img[y]), [])]):
            return img
    return None


def _classify_small_graphs():
    """Lemma 4.5.2, Proposition 4.6.3 and Theorem 4.5.8 (i)-(iii) for every
    connected labelled graph of the stated families."""
    from sage.all import graphs
    L8 = [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 2), (1, 4), (4, 1)]
    L4 = [(1, 1), (1, 2), (2, 1), (2, 2)]
    family = []
    for n in range(1, 6):
        for G in graphs.trees(n):
            E = G.edges(labels=False)
            for labs in itertools.product(L8, repeat=len(E)):
                family.append(LGraph(n, [(x, y, a, b) for (x, y), (a, b)
                                         in zip(E, labs)]))
    ntrees = len(family)
    for n in (3, 4):
        for G in graphs(n):
            if not G.is_connected() or G.is_tree():
                continue
            E = G.edges(labels=False)
            for labs in itertools.product(L4, repeat=len(E)):
                family.append(LGraph(n, [(x, y, a, b) for (x, y), (a, b)
                                         in zip(E, labs)]))
    for l1 in L4:
        for l2 in L4:
            family.append(LGraph(2, [(0, 1) + l1, (0, 1) + l2]))
    dyn = dynkin_list(5)
    euc = [E for E, _ in euclidean_list(5)]
    counts = {'dynkin': 0, 'euclidean': 0, 'other': 0, 'not valued': 0}
    for T in family:
        isD = any(isomorphic_lg(T, D) for D in dyn if D.n == T.n)
        isE = any(isomorphic_lg(T, E) for E in euc if E.n == T.n)
        smallerE = any(smaller(E, T) for E in euc if E.n <= T.n)
        assert isD != smallerE, 'Lemma 4.5.2 fails for %s' % (T.edges,)
        f = T.valuation()
        if f is None:
            counts['not valued'] += 1
            continue
        S = T.sym()
        C = T.cartan()
        pd = posdef(S)
        psd = possemidef(S)
        assert pd == isD, 'Prop 4.6.3 (i) fails for %s' % (T.edges,)
        assert (psd and not pd) == isE, 'Prop 4.6.3 (ii) fails'
        if isD:
            counts['dynkin'] += 1
            nn = vector(QQ, [1] * T.n) * C.inverse()
            assert all(a > 0 for a in nn), 'Thm 4.5.8: no subadditive'
            assert C.det() != 0          # no additive function
        elif isE:
            counts['euclidean'] += 1
            K = C.left_kernel().basis()
            assert len(K) == 1 and (all(a > 0 for a in K[0])
                                    or all(a < 0 for a in K[0]))
            Kop = C.right_kernel().basis()   # additive on T^op
            assert len(Kop) == 1 and (all(a > 0 for a in Kop[0])
                                      or all(a < 0 for a in Kop[0]))
        else:
            counts['other'] += 1
            v = perron_vector(S)
            if not (v * S * v < 0):
                v = None
                for cand in itertools.product(range(4), repeat=T.n):
                    w = vector(ZZ, cand)
                    if w * S * w < 0:
                        v = w
                        break
            assert v is not None and all(a >= 0 for a in v), \
                'Prop 4.6.3 (iii) fails'
            u = vector(ZZ, [f[i] * v[i] for i in range(T.n)])
            assert all(a < 0 for a in C * u), 'Thm 4.5.8: witness'
    check(True, 'Lemma 4.5.2 for %d labelled graphs (%d trees on <= 5 '
          'vertices, labels ab <= 4; graphs with cycles on <= 4 vertices, '
          'labels in (1,1), (1,2), (2,1), (2,2); double edges): Dynkin '
          'xor a Euclidean diagram is smaller' % (len(family), ntrees))
    check(True, 'Prop 4.6.3 (i)-(iii), Thm 4.5.8 (i)-(iii) for the %d valued '
          'ones: %d Dynkin (positive definite, subadditive non-additive '
          'function, no additive one), %d Euclidean (semidefinite and not '
          'definite, additive on T and T^op), %d others (v >= 0 integral '
          'with (v, v) < 0, u >= 0 with C u < 0, so no subadditive '
          'function); %d not valued'
          % (len(family) - counts['not valued'], counts['dynkin'],
             counts['euclidean'], counts['other'], counts['not valued']))
    return counts


# ===========================================================================
# 4.1, 4.2: path algebras
# ===========================================================================


class PathAlgebra:
    """kQ for a quiver on the vertices 0..n-1 with arrows (s, t).  A path
    is (start, end, arrows in the order of traversal); the product p.q is
    "q followed by p" (composition in reverse order, p. 99), defined iff q
    ends where p starts.  Paths of length > maxlen are left out (only for
    quivers with oriented cycles)."""

    def __init__(self, n, arrows, F, maxlen=None):
        self.n, self.arrows, self.F = n, list(arrows), F
        paths = [(x, x, ()) for x in range(n)]
        frontier, length = list(paths), 0
        while frontier and (maxlen is None or length < maxlen):
            new = [(s, b, p + (i,)) for (s, t, p) in frontier
                   for i, (a, b) in enumerate(self.arrows) if a == t]
            paths += new
            frontier = new
            length += 1
            assert maxlen is not None or length <= 60, 'oriented cycle'
        self.paths = paths
        self.index = {p: i for i, p in enumerate(paths)}
        self.dim = len(paths)

    @staticmethod
    def length(p):
        return len(p[2])

    def mul(self, p, q):
        """p.q = q followed by p, or None."""
        if q[1] != p[0]:
            return None
        r = (q[0], p[1], q[2] + p[2])
        return r if r in self.index else None

    def lmul(self, p, u, r=1):
        """p.u for u in (kQ)^r, a list of r*dim field elements."""
        out = [self.F(0)] * (r * self.dim)
        for blk in range(r):
            off = blk * self.dim
            for j, q in enumerate(self.paths):
                c = u[off + j]
                if c:
                    pq = self.mul(p, q)
                    if pq is not None:
                        out[off + self.index[pq]] += c
        return out

    def vec(self, p):
        v = [self.F(0)] * self.dim
        v[self.index[p]] = self.F(1)
        return v


def has_cycle(n, arrows):
    out = {x: [b for a, b in arrows if a == x] for x in range(n)}
    state = [0] * n

    def dfs(v):
        state[v] = 1
        for w in out[v]:
            if state[w] == 1 or (state[w] == 0 and dfs(w)):
                return True
        state[v] = 2
        return False
    return any(state[v] == 0 and dfs(v) for v in range(n))


def span_dim(F, vecs, ncols):
    vecs = [v for v in vecs if any(v)]
    if not vecs:
        return 0
    return dmatrix(F, vecs).rank()


def row_basis(F, vecs, ncols):
    vecs = [v for v in vecs if any(v)]
    if not vecs:
        return []
    return [list(r) for r in dmatrix(F, vecs).row_space().basis()]


QUIVERS = {
    'A1': (1, []),
    'A3 linear': (3, [(0, 1), (1, 2)]),
    'A3 alternating': (3, [(0, 1), (2, 1)]),
    'A4 linear': (4, [(0, 1), (1, 2), (2, 3)]),
    'D4 subspace': (4, [(1, 0), (2, 0), (3, 0)]),
    'Kronecker': (2, [(0, 1), (0, 1)]),
    'D~4 four subspace': (5, [(1, 0), (2, 0), (3, 0), (4, 0)]),
    'A~3 acyclic': (4, [(0, 1), (1, 2), (0, 3), (3, 2)]),
    'diamond with double arrow': (3, [(0, 1), (0, 1), (1, 2), (0, 2)]),
}
CYCLIC = {
    'one loop': (1, [(0, 0)]),
    'free algebra on two letters': (1, [(0, 0), (0, 0)]),
    'oriented triangle': (3, [(0, 1), (1, 2), (2, 0)]),
    'A~1 with a 2-cycle': (2, [(0, 1), (1, 0)]),
}


def section_4_1_and_4_2():
    # ---------------- path algebras: dimensions, ideals ------------------
    for name, (n, arrows) in CYCLIC.items():
        A = PathAlgebra(n, arrows, GF(2), maxlen=6)
        lens = set(A.length(p) for p in A.paths)
        check(has_cycle(n, arrows) and lens == set(range(7)),
              'p. 99: kQ for the quiver with oriented cycle "%s" has paths '
              'of every length <= 6 (infinite dimensional)' % name)
    for name, (n, arrows) in QUIVERS.items():
        for F in (GF(2), GF(3)):
            A = PathAlgebra(n, arrows, F)
            check(not has_cycle(n, arrows)
                  and max(A.length(p) for p in A.paths) < n,
                  'p. 99: kQ is finite dimensional (%s: dim %d) without '
                  'oriented cycles' % (name, A.dim))
            P = A.paths
            ok_assoc = all(
                (A.mul(A.mul(p, q), r) if A.mul(p, q) is not None else None)
                == (A.mul(p, A.mul(q, r)) if A.mul(q, r) is not None
                    else None)
                for p in P for q in P for r in P)
            es = [(x, x, ()) for x in range(n)]
            ok_idem = all(A.mul(es[x], es[y]) == (es[x] if x == y else None)
                          for x in range(n) for y in range(n))
            ok_one = all(sum(1 for e in es if A.mul(e, p) == p) == 1
                         and sum(1 for e in es if A.mul(p, e) == p) == 1
                         for p in P)
            check(ok_assoc and ok_idem and ok_one,
                  'p. 99: kQ is associative, the e_x are orthogonal '
                  'idempotents with sum 1 (%s over GF(%d))'
                  % (name, F.order()))
            # P_x = kQ e_x: paths beginning at x; e_y u = u = u e_x
            ok = all(set(A.mul(p, es[x]) for p in P
                         if A.mul(p, es[x]) is not None)
                     == set(p for p in P if p[0] == x) for x in range(n))
            ok = ok and all(A.mul(es[b], (a, b, (i,))) == (a, b, (i,))
                            == A.mul((a, b, (i,)), es[a])
                            for i, (a, b) in enumerate(arrows))
            check(ok, 'p. 100: P_x = kQ e_x has the paths beginning at x, '
                  'and e_y u = u = u e_x for an arrow x -> y (%s)' % name)
            # kQ_(m) is a two-sided ideal; kQ_(m) = J^m; layers
            maxl = max(A.length(p) for p in P)
            ok = True
            for m in range(0, maxl + 2):
                ideal = set(p for p in P if A.length(p) >= m)
                for p in P:
                    for q in ideal:
                        for r in (A.mul(p, q), A.mul(q, p)):
                            if r is not None and r not in ideal:
                                ok = False
                # J^m: spanned by the products of m paths of length >= 1
                if m >= 1:
                    J1 = [p for p in P if A.length(p) >= 1]
                    Jm = set(J1)
                    for _ in range(m - 1):
                        Jm = set(A.mul(p, q) for p in Jm for q in J1
                                 if A.mul(p, q) is not None)
                    if Jm != ideal:
                        ok = False
            ok = ok and not any(A.length(p) > maxl for p in P)
            check(ok, 'Def 4.1.3 and p. 101: kQ_(m) is a two-sided ideal, '
                  'J = kQ_(1) is nilpotent with kQ/J = k^n, so J(kQ) = '
                  'kQ_(1) and kQ_(m) = J^m (%s)' % name)
            # e_x kQ_(m)/kQ_(m+1): paths of length m ending at x; maps
            ok = True
            for m in range(maxl + 1):
                for x in range(n):
                    layer = [p for p in P if A.length(p) == m
                             and A.mul(es[x], p) == p]
                    if set(layer) != set(p for p in P if A.length(p) == m
                                         and p[1] == x):
                        ok = False
            for u in P:
                if A.length(u) == 0:
                    continue
                x, y, mm = u[0], u[1], A.length(u)
                for m in range(maxl + 1):
                    src = [p for p in P if A.length(p) == m and p[1] == x]
                    imgs = [A.mul(u, p) for p in src]
                    if any(i is None or A.length(i) != m + mm
                           for i in imgs) or len(set(imgs)) != len(imgs):
                        ok = False
            # images for distinct paths x -> y of the same length are
            # independent
            for x in range(n):
                for y in range(n):
                    for mm in range(1, maxl + 1):
                        us = [u for u in P if u[0] == x and u[1] == y
                              and A.length(u) == mm]
                        imgs = [A.mul(u, p) for u in us for p in P
                                if p[1] == x]
                        if len(set(imgs)) != len(imgs):
                            ok = False
            check(ok, 'p. 101: e_x kQ_(m)/kQ_(m+1) has the paths of length '
                  'm ending at x; a path x -> y induces injective maps with '
                  'independent images (%s)' % name)
    # ---------------- Theorem 4.1.4: hereditary --------------------------
    nsub = 0
    for name in ('A3 linear', 'A3 alternating', 'A4 linear', 'D4 subspace',
                 'Kronecker', 'D~4 four subspace'):
        n, arrows = QUIVERS[name]
        for F in (GF(2), GF(3)):
            A = PathAlgebra(n, arrows, F)
            es = [(x, x, ()) for x in range(n)]
            Pdims = [[sum(1 for p in A.paths if p[0] == x and p[1] == y)
                      for y in range(n)] for x in range(n)]
            # rad P_x = sum over arrows x -> y of P_y alpha
            check(all(sum(Pdims[x]) - 1 == sum(sum(Pdims[b])
                                               for a, b in arrows if a == x)
                      for x in range(n)),
                  'Thm 4.1.4: rad P_x is the direct sum of the P_y alpha, '
                  'alpha: x -> y (%s)' % name)
            for trial in range(10):
                r = random.choice([1, 2])
                s = random.choice([1, 2, 3])
                gens = [[F.random_element() for _ in range(r * A.dim)]
                        for _ in range(s)]
                U = row_basis(F, [A.lmul(p, g, r) for p in A.paths
                                  for g in gens], r * A.dim)
                JU = row_basis(F, [A.lmul(p, u, r) for p in A.paths
                                   if A.length(p) >= 1 for u in U],
                               r * A.dim)
                dU = [span_dim(F, [A.lmul(es[x], u, r) for u in U], 0)
                      for x in range(n)]
                dJU = [span_dim(F, [A.lmul(es[x], u, r) for u in JU], 0)
                       for x in range(n)]
                top = [dU[x] - dJU[x] for x in range(n)]
                cover = [sum(top[x] * Pdims[x][y] for x in range(n))
                         for y in range(n)]
                check(cover == dU,
                      'Thm 4.1.4 (p. 101): a random submodule of (kQ)^%d '
                      '(%s, GF(%d), dimension vector %s) is projective'
                      % (r, name, F.order(), dU))
                nsub += 1
    # -------------- Definition 4.1.6: Ext-quiver of kQ --------------------
    for name, (n, arrows) in QUIVERS.items():
        A = PathAlgebra(n, arrows, GF(2))
        for i in range(n):
            for j in range(n):
                eJe = [p for p in A.paths if p[0] == i and p[1] == j
                       and A.length(p) >= 1]
                eJ2e = [p for p in eJe if A.length(p) >= 2]
                narr = sum(1 for a, b in arrows if (a, b) == (i, j))
                if len(eJe) - len(eJ2e) != narr:
                    raise AssertionError('Def 4.1.6 for ' + name)
        check(True, 'Def 4.1.6, Prop 4.1.7: the Ext-quiver of kQ is Q '
              '(dim e_j J e_i / e_j J^2 e_i = arrows i -> j; %s)' % name)
    _group_algebra_ext_quivers()
    _chain_complex_example()
    _inseparable_example()
    # ---------------- Section 4.2 ----------------------------------------
    for name in ('A3 linear', 'A3 alternating', 'A4 linear', 'D4 subspace',
                 'Kronecker', 'D~4 four subspace'):
        n, arrows = QUIVERS[name]
        A = PathAlgebra(n, arrows, GF(2))
        ok_222 = True
        ok_223 = True
        printed_223 = True
        for k, (i, j) in enumerate(arrows):
            alpha = (i, j, (k,))
            Pj = [p for p in A.paths if p[0] == j]
            Pi = [p for p in A.paths if p[0] == i]
            img = [A.mul(p, alpha) for p in Pj]
            # right multiplication by alpha: a module map P_j -> P_i
            if any(q is None or q[0] != i for q in img) or len(set(img)) \
                    != len(img):
                ok_222 = False
            if not all(A.length(q) >= 1 for q in img) or alpha not in img:
                ok_222 = False
            if not all(A.mul(u, p) is None or A.mul(A.mul(u, p), alpha)
                       == A.mul(u, A.mul(p, alpha))
                       for u in A.paths for p in Pj):
                ok_222 = False
            if not len(Pj) < len(Pi):
                ok_223 = False
            if len(Pi) > len(Pj):          # P_i cannot lie in P_j
                printed_223 = False
        check(ok_222, 'Lemma 4.2.2: for every arrow i -> j of %s, P_j embeds '
              'in J P_i, not in J^2 P_i (right multiplication by the arrow)'
              % name)
        check(ok_223, 'Lemma 4.2.3 (corrected): an arrow i -> j gives P_j a '
              'proper submodule of P_i (%s)' % name)
        refuted(printed_223 and arrows,
                'Lemma 4.2.3 as printed (P_i in P_j for an arrow i -> j): '
                'dim P_i > dim P_j (%s)' % name)
    # Lemma 4.2.1 on kA3/J^2: I = J^2 != 0 and the quotient is not hereditary
    A = PathAlgebra(3, [(0, 1), (1, 2)], GF(2))
    J2 = [p for p in A.paths if A.length(p) >= 2]
    # in Lambda = kQ/J^2 the paths of length <= 1 remain
    rad0 = [p for p in A.paths if p[0] == 0 and A.length(p) == 1]
    P1 = [p for p in A.paths if p[0] == 1 and A.length(p) <= 1]
    check(len(J2) == 1 and len(rad0) == 1 and rad0[0][1] == 1
          and len(P1) == 2,
          'Lemma 4.2.1: for kA3 and I = J^2 = kQ_(2) != 0, Lambda = kQ/I has '
          'rad(Lambda e_0) = S_1 of dimension 1 while Lambda e_1 has '
          'dimension 2: Lambda is not hereditary')
    # Proposition 4.2.4: T_n(k) = kA_n
    for nn in range(1, 6):
        F = GF(3)
        basis = [(i, j) for i in range(nn) for j in range(i, nn)]
        # Ext-quiver of T_n: arrows x_i -> x_j iff i = j + 1
        arrows = [(j + 1, j) for j in range(nn - 1)]
        A = PathAlgebra(nn, arrows, F)
        # path from a to b (a > b) <-> E_(b, a); trivial path e_x <-> E_xx

        def image(p):
            return (p[1], p[0])
        ok = len(A.paths) == len(basis) and sorted(
            image(p) for p in A.paths) == sorted(basis)
        for p in A.paths:
            for q in A.paths:
                pq = A.mul(p, q)
                (a, b), (c, d) = image(p), image(q)
                prodE = (a, d) if b == c else None
                if (image(pq) if pq is not None else None) != prodE:
                    ok = False
        check(ok, 'Prop 4.2.4: the upper triangular %dx%d matrices form the '
              'path algebra of their Ext-quiver A_%d' % (nn, nn, nn))
    return nsub


def _group_elements_table(G):
    els = list(G)
    idx = {g: i for i, g in enumerate(els)}
    mul = [[idx[a * b] for b in els] for a in els]
    return els, idx, mul


def _ga_mul(F, mul, u, v):
    n = len(u)
    out = [F(0)] * n
    for i in range(n):
        if u[i]:
            for j in range(n):
                if v[j]:
                    out[mul[i][j]] += u[i] * v[j]
    return out


def _group_algebra_ext_quivers():
    from sage.all import PermutationGroup, SymmetricGroup
    # kV4 over GF(2)
    F = GF(2)
    G = PermutationGroup(['(1,2)', '(3,4)'])
    els, idx, mul = _group_elements_table(G)
    n = len(els)
    one = [F(0)] * n
    one[idx[G.identity()]] = F(1)

    def el(g):
        v = [F(0)] * n
        v[idx[G(g)]] = F(1)
        return v
    x, y = G('(1,2)'), G('(3,4)')
    X = [a - b for a, b in zip(el(x), one)]
    Y = [a - b for a, b in zip(el(y), one)]
    J = row_basis(F, [[a - b for a, b in zip(el(g), one)] for g in els], n)
    J2 = row_basis(F, [_ga_mul(F, mul, u, v) for u in J for v in J], n)
    soc = J2
    check(len(J) == 3 and len(J2) == 1,
          'Section 4.3 (p. 107): dim_k Ext^1_kV4(k, k) = dim J/J^2 = 2')
    sq = [_ga_mul(F, mul, X, X), _ga_mul(F, mul, Y, Y),
          _ga_mul(F, mul, X, Y)]
    check(all(span_dim(F, soc + [s], n) == 1 for s in sq)
          and span_dim(F, [one, X, Y] + soc, n) == 4,
          'p. 107: Lambda = kV4/Soc(kV4) has basis 1, x - 1, y - 1 and '
          '(x - 1)^2 = (y - 1)^2 = (x - 1)(y - 1) = 0')
    # k<a, b> -> kV4: words of length <= 3
    words = [w for L in range(4) for w in itertools.product('ab', repeat=L)]
    wi = {w: i for i, w in enumerate(words)}

    def img(w):
        v = one
        for c in w:
            v = _ga_mul(F, mul, v, X if c == 'a' else Y)
        return v
    M = dmatrix(F, [img(w) for w in words])
    rels = []
    # the ideal generated by a^2, b^2, ab - ba in degrees <= 3
    for u_len in range(2):
        for v_len in range(2 - u_len):
            for u in itertools.product('ab', repeat=u_len):
                for v in itertools.product('ab', repeat=v_len):
                    for r in (['aa'], ['bb'], ['ab', 'ba']):
                        vec = [F(0)] * len(words)
                        for k, mono in enumerate(r):
                            w = u + tuple(mono) + v
                            vec[wi[w]] += F(1) if k == 0 else F(-1)
                        rels.append(vec)
    Rk = dmatrix(F, rels)
    ker = M.left_kernel()
    check(M.rank() == 4 and Rk.row_space() == ker
          and all(ker.dimension() == len(words) - 4 for _ in [0])
          and dmatrix(F, [img(w) for w in words if len(w) <= 1]).rank()
          == 3,
          'p. 107: k<a, b> -> kV4, a -> x - 1, b -> y - 1, is onto; in '
          'degrees <= 3 its kernel is the ideal of a^2, b^2, ab - ba and '
          'meets the paths of length <= 1 in 0 (Prop 4.1.7)')
    # GF(3)S3: the Ext-quiver k <-> sgn from idempotents
    F = GF(3)
    G = SymmetricGroup(3)
    els, idx, mul = _group_elements_table(G)
    n = len(els)

    def el3(g, c=1):
        v = [F(0)] * n
        v[idx[G(g)]] = F(c)
        return v

    def add(*vs):
        return [sum(c) for c in zip(*vs)]
    one = el3('()')
    t = el3('(1,2)')
    x3 = el3('(1,2,3)')
    ep = [F(2) * a for a in add(one, t)]          # (1 + t)/2
    em = [F(2) * a for a in add(one, [-a for a in t])]
    check(_ga_mul(F, mul, ep, ep) == ep and _ga_mul(F, mul, em, em) == em
          and _ga_mul(F, mul, ep, em) == [F(0)] * n and add(ep, em) == one,
          'Def 4.1.6 for GF(3)S3: e_+ = (1 + t)/2, e_- = (1 - t)/2 are '
          'orthogonal idempotents with sum 1')
    gen = add(one, [-a for a in x3])
    J = row_basis(F, [_ga_mul(F, mul, _ga_mul(F, mul, el3(g), gen), el3(h))
                      for g in els for h in els], n)
    J2 = row_basis(F, [_ga_mul(F, mul, u, v) for u in J for v in J], n)
    J3 = row_basis(F, [_ga_mul(F, mul, u, v) for u in J2 for v in J], n)
    check(len(J) == 4 and len(J2) == 2 and len(J3) == 0,
          'GF(3)S3: J = (1 - x) of dimension 4, J^2 of dimension 2, J^3 = 0')
    es = {'+': ep, '-': em}
    dims = {}
    for i in '+-':
        for j in '+-':
            A1 = [_ga_mul(F, mul, _ga_mul(F, mul, es[j], u), es[i])
                  for u in J]
            A2 = [_ga_mul(F, mul, _ga_mul(F, mul, es[j], u), es[i])
                  for u in J2]
            dims[i, j] = span_dim(F, A1 + A2, n) - span_dim(F, A2, n)
    check(dims == {('+', '+'): 0, ('+', '-'): 1, ('-', '+'): 1,
                   ('-', '-'): 0},
          'Def 4.1.6: the Ext-quiver of GF(3)S3 has one arrow k -> sgn and '
          'one arrow sgn -> k, no loops')
    # Prop 4.1.7: the path algebra of k <-> sgn onto GF(3)S3
    a = [_ga_mul(F, mul, _ga_mul(F, mul, em, u), ep) for u in J]
    a = next(v for v in a if span_dim(F, J2 + [v], n) > len(J2))
    b = [_ga_mul(F, mul, _ga_mul(F, mul, ep, u), em) for u in J]
    b = next(v for v in b if span_dim(F, J2 + [v], n) > len(J2))
    Q = PathAlgebra(2, [(0, 1), (1, 0)], F, maxlen=3)   # 0 = k, 1 = sgn

    def phi(p):
        v = ep if p[0] == 0 else em
        for k in p[2]:
            v = _ga_mul(F, mul, a if k == 0 else b, v)
        return v
    check(span_dim(F, [phi(p) for p in Q.paths], n) == 6
          and span_dim(F, J2 + [phi(p) for p in Q.paths
                                if Q.length(p) <= 1], n) == 6,
          'Prop 4.1.7 for GF(3)S3: the map from the path algebra of its '
          'Ext-quiver is onto; e_+, e_-, the two arrows stay independent '
          'modulo J^2, so the kernel lies in the paths of length >= 2')


def _chain_complex_example():
    """Example after Definition 4.1.8, on the finite linear quiver
    0 -> 1 -> ... -> 5 (Lambda = kQ/kQ_(2))."""
    F = GF(2)
    n = 6
    # P_x of Lambda: k at x and x + 1 with the identity; of kQ: k at x..5
    A = PathAlgebra(n, [(v, v + 1) for v in range(n - 1)], F)
    for x in range(1, 4):
        # Lambda e_x: the paths of length <= 1 beginning at x
        Px = [p for p in A.paths if p[0] == x and A.length(p) <= 1]
        check(sorted(p[1] for p in Px) == [x, x + 1]
              and all(A.mul(q, p) is None or A.length(A.mul(q, p)) >= 2
                      for p in Px for q in A.paths if A.length(q) == 1
                      and A.length(p) == 1),
              'Example after Def 4.1.8 (corrected kQ/I): the projective '
              'Lambda e_%d is k at %d and %d with the identity map and zero '
              'composites: an exact complex 0 -> k -> k -> 0' % (x, x, x + 1))
    P0 = [p for p in A.paths if p[0] == 0]
    path02 = (0, 2, (0, 1))
    refuted(path02 not in P0,
            'Example after Def 4.1.8 as printed (kQ-modules are complexes): '
            'in the projective kQ e_0 the composite of the maps at 0 -> 1 -> '
            '2 sends e_0 to the path 0 -> 1 -> 2, not 0')
    # exhaustive: complexes 0 -> M1 -> M2 -> M3 -> M4 -> 0 over GF(2)
    total = 0
    for dv in [(1, 1, 1, 1), (1, 2, 1, 0), (1, 2, 2, 1), (2, 2, 1, 1),
               (1, 1, 2, 2)]:
        d1, d2, d3, d4 = dv
        sizes = [(d2, d1), (d3, d2), (d4, d3)]
        for entries in itertools.product(*[itertools.product(
                F, repeat=r * c) for r, c in sizes]):
            maps = [dmatrix(F, r, c, list(e))
                    for (r, c), e in zip(sizes, entries)]
            if not ((maps[1] * maps[0]).is_zero()
                    and (maps[2] * maps[1]).is_zero()):
                continue
            total += 1
            rk = [m.rank() for m in maps]
            dimsM = [d1, d2, d3, d4]
            exact = (rk[0] == d1 and d2 - rk[1] == rk[0]
                     and d3 - rk[2] == rk[1] and rk[2] == d4)
            # top at vertex v: M_v / image of the incoming map
            top = [d1, d2 - rk[0], d3 - rk[1], d4 - rk[2]]
            cover = [top[0], top[0] + top[1], top[1] + top[2],
                     top[2] + top[3]]
            proj = cover == dimsM and top[3] == 0
            assert exact == proj, (dv, maps)
    check(total > 0, 'Example after Def 4.1.8 (corrected kQ/I): of the %d '
          'complexes over GF(2) with dimension vectors (1,1,1,1), (1,2,1,0), '
          '(1,2,2,1), (2,2,1,1), (1,1,2,2) between zeros, the exact ones are '
          'exactly the projective Lambda-modules' % total)


def _inseparable_example():
    """Remark (ii) after Corollary 4.1.11."""
    for p in (2, 3):
        K = FractionField(PolynomialRing(GF(p), 'x'))
        x = K.gen()
        R = PolynomialRing(K, ['y', 'e'], order='lex')
        y, e = R.gens()
        I = R.ideal([e ** p, y ** p - x - e])
        check(I.vector_space_dimension() == p ** 2,
              'Remark (ii) after Cor 4.1.11: Lambda has dimension p^2 = %d'
              % p ** 2)
        Y = PolynomialRing(K, 'Y').gen()
        check((Y ** p - x).is_irreducible() and I.reduce(e ** p) == 0,
              'Remark (ii): epsilon is nilpotent and Lambda/(epsilon) = '
              'k[y]/(y^p - x) is a field, so J(Lambda) = (epsilon) and '
              'Lambda/J is inseparable of degree p (p = %d)' % p)
        ok = True
        for _ in range(10):
            f = sum(PolynomialRing(GF(p), 'x').random_element(3)(x)
                    * y ** i * e ** j for i in range(p) for j in range(p))
            z = y + e * f
            if I.reduce(z ** p) != I.reduce(x + e) or I.reduce(z ** p - x) \
                    == 0:
                ok = False
        check(ok, 'Remark (ii): every lift z = y + epsilon f of y has '
              'z^p = x + epsilon != x (10 random f, p = %d), so '
              'Lambda -> Lambda/J does not split' % p)


# ===========================================================================
# Representations of quivers (column vectors), Hom, reflection functors
# ===========================================================================


class QRep:
    """A representation of the quiver with vertices 0..n-1 and arrows
    (s, t): a space k^dims[x] at each vertex and for each arrow a matrix
    with dims[t] rows and dims[s] columns."""

    def __init__(self, n, arrows, F, dims, maps):
        self.n, self.arrows, self.F = n, list(arrows), F
        self.dims = list(dims)
        self.maps = []
        for (s, t), A in zip(self.arrows, maps):
            if hasattr(A, 'nrows'):
                assert (A.nrows(), A.ncols()) == (self.dims[t], self.dims[s])
                A = A.list()
            A = matrix(F, self.dims[t], self.dims[s], A)
            self.maps.append(A)

    def dimvec(self):
        return tuple(self.dims)

    def is_zero(self):
        return sum(self.dims) == 0


def simple_rep(n, arrows, F, x):
    dims = [1 if v == x else 0 for v in range(n)]
    return QRep(n, arrows, F, dims,
                [matrix(F, dims[t], dims[s], 0) for s, t in arrows])


def direct_sum_rep(*Ms):
    M0 = Ms[0]
    dims = [sum(M.dims[x] for M in Ms) for x in range(M0.n)]
    maps = []
    for a, (s, t) in enumerate(M0.arrows):
        B = matrix(M0.F, dims[t], dims[s], 0)
        r = c = 0
        for M in Ms:
            A = M.maps[a]
            for i in range(A.nrows()):
                for j in range(A.ncols()):
                    if A[i, j]:
                        B[r + i, c + j] = A[i, j]
            r += M.dims[t]
            c += M.dims[s]
        maps.append(B)
    return QRep(M0.n, M0.arrows, M0.F, dims, maps)


def _hom_system(M, N):
    """The linear map f -> (f_t M_a - N_a f_s)_a from the sum of the
    Hom(M_x, N_x) to the sum of the Hom(M_s, N_t): its kernel is
    Hom(M, N); for a quiver without relations its cokernel is Ext^1(M, N)
    (the standard resolution of a representation; used here only for the
    simple modules, Definition 4.1.6)."""
    F = M.F
    off, k = [], 0
    for x in range(M.n):
        off.append(k)
        k += N.dims[x] * M.dims[x]
    entries, r = {}, 0
    for a, (s, t) in enumerate(M.arrows):
        Ma, Na = M.maps[a], N.maps[a]
        for i in range(N.dims[t]):
            for j in range(M.dims[s]):
                for kk in range(M.dims[t]):
                    c = Ma[kk, j]
                    if c:
                        key = (r, off[t] + i * M.dims[t] + kk)
                        entries[key] = entries.get(key, F(0)) + c
                for kk in range(N.dims[s]):
                    c = Na[i, kk]
                    if c:
                        key = (r, off[s] + kk * M.dims[s] + j)
                        entries[key] = entries.get(key, F(0)) - c
                r += 1
    return dmatrix(F, r, k, entries), off


def hom_dim(M, N):
    A, _ = _hom_system(M, N)
    return A.ncols() - (A.rank() if A.nrows() and A.ncols() else 0)


def ext1_dim(M, N):
    A, _ = _hom_system(M, N)
    return A.nrows() - (A.rank() if A.nrows() and A.ncols() else 0)


def hom_basis(M, N):
    A, off = _hom_system(M, N)
    if A.ncols() == 0:
        return []
    if A.nrows() == 0:
        K = _identity_matrix(M.F, A.ncols()).rows()
    else:
        K = A.right_kernel_matrix().rows()
    out = []
    for v in K:
        out.append([dmatrix(M.F, N.dims[x], M.dims[x],
                            list(v[off[x]:off[x] + N.dims[x] * M.dims[x]]))
                    for x in range(M.n)])
    return out


def is_iso_rep(M, N, tries=60):
    if M.dims != N.dims or M.arrows != N.arrows:
        return False
    B = hom_basis(M, N)
    if not B:
        return sum(M.dims) == 0

    def invertible(f):
        return all(f[x].is_invertible() for x in range(M.n))
    if len(B) == 1:
        return invertible(B[0])
    F = M.F
    q = F.order()
    if q ** len(B) <= 4096:
        for coeffs in itertools.product(F, repeat=len(B)):
            f = [sum((c * b[x] for c, b in zip(coeffs, B)),
                     0 * B[0][x]) for x in range(M.n)]
            if invertible(f):
                return True
        return False
    for _ in range(tries):
        cs = [F.random_element() for _ in B]
        f = [sum((c * b[x] for c, b in zip(cs, B)), 0 * B[0][x])
             for x in range(M.n)]
        if invertible(f):
            return True
    raise ValueError('isomorphism test inconclusive')


def _kernel_cols(A, F, ncols):
    """A matrix whose columns are a basis of the right kernel of A."""
    if A.nrows() == 0:
        return _identity_matrix(F, ncols)
    K = A.dense_matrix().right_kernel_matrix()
    return K.transpose()


def _left_kernel_rows(A, F, nrows):
    if A.ncols() == 0:
        return _identity_matrix(F, nrows)
    return A.dense_matrix().transpose().right_kernel_matrix()


def S_plus(M, y):
    """Reflection functor at the sink y (p. 125): W_y = Ker(phi), the
    arrows at y reversed, the new maps the components of W_y -> sum."""
    F = M.F
    assert all(s != y for s, t in M.arrows), 'not a sink'
    ins = [a for a, (s, t) in enumerate(M.arrows) if t == y]
    blocks = [M.dims[M.arrows[a][0]] for a in ins]
    tot = sum(blocks)
    phi = dmatrix(F, M.dims[y], tot, 0)
    c = 0
    for a, w in zip(ins, blocks):
        for i in range(M.dims[y]):
            for j in range(w):
                phi[i, c + j] = M.maps[a][i, j]
        c += w
    K = _kernel_cols(phi, F, tot)
    wy = K.ncols()
    dims = list(M.dims)
    dims[y] = wy
    arrows, maps = [], []
    c = 0
    starts = {}
    for a, w in zip(ins, blocks):
        starts[a] = c
        c += w
    for a, (s, t) in enumerate(M.arrows):
        if t == y:
            arrows.append((y, s))
            st = starts[a]
            maps.append(dmatrix(F, M.dims[s], wy,
                                [[K[st + i, j] for j in range(wy)]
                                 for i in range(M.dims[s])]))
        else:
            arrows.append((s, t))
            maps.append(M.maps[a])
    return QRep(M.n, arrows, F, dims, maps)


def S_minus(W, y):
    """Reflection functor at the source y: V_y = Coker(psi)."""
    F = W.F
    assert all(t != y for s, t in W.arrows), 'not a source'
    outs = [a for a, (s, t) in enumerate(W.arrows) if s == y]
    blocks = [W.dims[W.arrows[a][1]] for a in outs]
    tot = sum(blocks)
    psi = dmatrix(F, tot, W.dims[y], 0)
    r = 0
    for a, w in zip(outs, blocks):
        for i in range(w):
            for j in range(W.dims[y]):
                psi[r + i, j] = W.maps[a][i, j]
        r += w
    P = _left_kernel_rows(psi, F, tot)      # rows: the projection
    vy = P.nrows()
    dims = list(W.dims)
    dims[y] = vy
    arrows, maps = [], []
    starts, r = {}, 0
    for a, w in zip(outs, blocks):
        starts[a] = r
        r += w
    for a, (s, t) in enumerate(W.arrows):
        if s == y:
            arrows.append((t, y))
            st = starts[a]
            maps.append(dmatrix(F, vy, W.dims[t],
                                [[P[i, st + j] for j in range(W.dims[t])]
                                 for i in range(vy)]))
        else:
            arrows.append((s, t))
            maps.append(W.maps[a])
    return QRep(W.n, arrows, F, dims, maps)


def reflect_arrows(arrows, y):
    return [(t, s) if y in (s, t) else (s, t) for s, t in arrows]


def admissible_ordering(n, arrows):
    """x_1, ..., x_n with x_i a sink of s_(i+1) ... s_n Q (Def. 4.7.2), or
    None."""
    order, cur, left = [], list(arrows), set(range(n))
    while left:
        sinks = [v for v in sorted(left) if all(s != v for s, t in cur)]
        if not sinks:
            return None
        v = sinks[0]
        order.insert(0, v)
        cur = reflect_arrows(cur, v)
        left.remove(v)
    return order


def is_admissible(n, arrows, order):
    for i in range(n - 1, -1, -1):
        cur = list(arrows)
        for j in range(n - 1, i, -1):
            cur = reflect_arrows(cur, order[j])
        if any(s == order[i] for s, t in cur):
            return False
    return True


def gabriel_indecomposables(n, arrows, F):
    """The representations (C^-)^(m-1) S_n^- ... S_(i+1)^- (S_i) of the proof
    of Theorem 4.7.6, for an admissible ordering x_1..x_n of Q."""
    order = admissible_ordering(n, arrows)
    reps = []
    for i in range(n):
        cur = list(arrows)
        for j in range(n - 1, i, -1):
            cur = reflect_arrows(cur, order[j])
        V = simple_rep(n, cur, F, order[i])
        for j in range(i + 1, n):
            V = S_minus(V, order[j])
        assert V.arrows == list(arrows)
        m = 1
        while not V.is_zero():
            reps.append((i, m, V))
            for j in range(n):
                V = S_minus(V, order[j])
            assert V.arrows == list(arrows)
            m += 1
            assert m < 100
    return order, reps


def C_plus(V, order):
    for j in range(len(order) - 1, -1, -1):
        V = S_plus(V, order[j])
    return V


def C_minus(V, order):
    for j in range(len(order)):
        V = S_minus(V, order[j])
    return V


def multisets(items, target, start=0):
    """Multisets (as dicts index -> multiplicity) of the vectors items[i]
    with sum target (vectors of non-negative integers)."""
    if all(t == 0 for t in target):
        yield {}
        return
    for i in range(start, len(items)):
        v = items[i]
        if any(a > b for a, b in zip(v, target)):
            continue
        rest = tuple(b - a for a, b in zip(v, target))
        for m in multisets(items, rest, i):
            m = dict(m)
            m[i] = m.get(i, 0) + 1
            yield m


def mass_formula(reps, resid, q, d, homcache, arrows):
    """sum over the multisets M of the reps with dimension vector d of
    1/|Aut M|, |Aut M| = q^(dim End M) prod_i |GL_(m_i)(q^r_i)| /
    q^(r_i m_i^2) (End(rep_i) local with residue field of q^r_i elements),
    and the expected q^(dim Rep d) / |GL(d)|."""
    dims = [tuple(R.dims) for R in reps]
    total = QQ(0)
    for ms in multisets(dims, tuple(d)):
        dimend = 0
        for i, mi in ms.items():
            for j, mj in ms.items():
                if (i, j) not in homcache:
                    homcache[i, j] = hom_dim(reps[i], reps[j])
                dimend += mi * mj * homcache[i, j]
        aut = QQ(q) ** dimend
        for i, mi in ms.items():
            Q = q ** resid[i]
            aut *= QQ(gl_order(mi, Q)) / QQ(Q) ** (mi * mi)
        total += 1 / aut
    rep_dim = sum(d[s] * d[t] for s, t in arrows)
    expect = QQ(q) ** rep_dim / prod([gl_order(dx, q) for dx in d])
    return total, expect


# ===========================================================================
# 4.3: the Kronecker quiver and the Klein four group
# ===========================================================================

KRON = [(0, 1), (0, 1)]          # a, b: V_1 -> V_2 (vertices 0, 1)


def companion(F, f):
    """The companion matrix of the monic polynomial f (rational canonical
    form of k[T]/(f))."""
    d = f.degree()
    C = dmatrix(F, d, d, 0)
    for i in range(1, d):
        C[i, i - 1] = 1
    for i in range(d):
        C[i, d - 1] = -f[i]
    return C


def kron(F, a, b):
    a = dmatrix(F, a)
    return QRep(2, KRON, F, [a.ncols(), a.nrows()], [a, b])


def kron_list(F, D):
    """The indecomposables of Theorem 4.3.2 with dim V_1, dim V_2 <= D, read
    with column vectors: (ii)/(iii) give the dimensions (n, n + 1) and
    (n + 1, n) (with transposed matrices, see the docstring), (i) the
    regular ones at the points of P^1(k).  Each entry: (rep, r, label),
    End(rep)/rad of q^r elements."""
    out = []
    for n in range(D + 1):
        A = dmatrix(F, n, n + 1, lambda i, j: 1 if j == i else 0)
        B = dmatrix(F, n, n + 1, lambda i, j: 1 if j == i + 1 else 0)
        if n + 1 <= D:
            out.append((kron(F, A, B), 1, 'E(%d)' % n))          # (n+1, n)
            out.append((kron(F, A.transpose(), B.transpose()), 1,
                        'E(%d)^T' % n))                          # (n, n+1)
    R = PolynomialRing(F, 'lam')
    for N in range(1, D + 1):
        for d in range(1, N + 1):
            if N % d:
                continue
            e = N // d
            for p in R.polynomials(of_degree=d):
                if p.is_monic() and p.is_irreducible():
                    out.append((kron(F, _identity_matrix(F, N),
                                     companion(F, p ** e)), d,
                                'reg(%s, %d)' % (p, e)))
        lam = R.gen()
        out.append((kron(F, companion(F, lam ** N), _identity_matrix(F, N)),
                    1, 'reg(inf, %d)' % N))
    return out


def section_4_3():
    stats = {}
    # ------------- Kronecker quiver: Ext and the simple S_2 -------------
    F = GF(2)
    S = [simple_rep(2, KRON, F, x) for x in range(2)]
    check([[ext1_dim(S[i], S[j]) for j in range(2)] for i in range(2)]
          == [[0, 2], [0, 0]],
          'p. 107: dim Ext^1_kQ(S_i, S_j) = 2 for i = 1, j = 2 and 0 '
          'otherwise (Kronecker quiver)')
    # ------------- Theorem 4.3.2: completeness by the mass formula --------
    for q, D in ((2, 4), (3, 3), (4, 3)):
        F = GF(q, 'w') if q == 4 else GF(q)
        lst = kron_list(F, D)
        reps = [r for r, _, _ in lst]
        resid = [r for _, r, _ in lst]
        homcache = {}
        # End of each indecomposable: k for E(n), E(n)^T; k[J] of
        # dimension deg(p) e for the regular ones (local, residue q^deg p)
        ok = True
        for i, (R, r, lab) in enumerate(lst):
            h = hom_dim(R, R)
            homcache[i, i] = h
            if lab.startswith('E') and h != 1:
                ok = False
            if lab.startswith('reg') and h != R.dims[0]:
                ok = False
        check(ok, 'Thm 4.3.2 over GF(%d): End of each listed '
              'indecomposable is k (cases (ii), (iii)) or k[J] = '
              'k[T]/(p^e) (case (i)), local' % q)
        # distinct entries are non-isomorphic: same dimension vector only
        # for regular ones at different points, and then Hom = 0
        ok = True
        for i, j in itertools.combinations(range(len(lst)), 2):
            if reps[i].dims == reps[j].dims:
                homcache[i, j] = hom_dim(reps[i], reps[j])
                if homcache[i, j] != 0:
                    ok = False
        check(ok, 'Thm 4.3.2 over GF(%d): the %d listed indecomposables '
              'with dim <= %d are pairwise non-isomorphic' % (q, len(lst), D))
        nd = 0
        for d1 in range(D + 1):
            for d2 in range(D + 1):
                if d1 + d2 == 0:
                    continue
                tot, exp = mass_formula(reps, resid, q, (d1, d2), homcache,
                                        KRON)
                check(tot == exp,
                      'Thm 4.3.2 (Kronecker) over GF(%d), dimension vector '
                      '(%d, %d): sum 1/|Aut M| over the sums of listed '
                      'indecomposables = q^(2 d1 d2)/|GL(d1)||GL(d2)|, so '
                      'the list is complete' % (q, d1, d2))
                nd += 1
        n11 = sum(1 for R in reps if R.dims == [1, 1])
        check(n11 == q + 1,
              'Thm 4.3.2 (i), Thm 4.4.4: q + 1 = %d indecomposables of '
              'dimension (1, 1) over GF(%d), parametrised by P^1' % (q + 1, q))
        stats[q] = (len(lst), nd)
    # the printed matrices of (ii): consistent when they act on row vectors
    F = GF(3)
    for n in range(1, 5):
        A = dmatrix(F, n, n + 1, lambda i, j: 1 if j == i else 0)
        B = dmatrix(F, n, n + 1, lambda i, j: 1 if j == i + 1 else 0)
        row = kron(F, A.transpose(), B.transpose())
        col = kron(F, A, B)
        check(row.dims == [n, n + 1] and col.dims == [n + 1, n]
              and hom_dim(row, row) == 1,
              'Thm 4.3.2 (ii), n = %d: the printed n x (n+1) matrices give '
              'dim V_2 = dim V_1 + 1 when they act on row vectors (with '
              'column vectors they give case (iii))' % n)
    # rational canonical forms: indecomposable iff a prime power
    for F, dmax in ((GF(2), 4), (GF(3), 3)):
        R = PolynomialRing(F, 'lam')
        mtx_ind = mtx('IsIndecomposable')
        ok = True
        cnt = 0
        for dd in range(1, dmax + 1):
            for f in R.polynomials(of_degree=dd):
                if not f.is_monic():
                    continue
                cnt += 1
                M = gmod([companion(F, f)], F)
                pp = len(f.factor()) == 1
                if bool(mtx_ind(M)) != pp:
                    ok = False
        check(ok, 'Thm 4.3.2 (i), Def 4.4.1: a rational canonical form '
              '(companion matrix, %d monic f of degree <= %d over GF(%d)) '
              'is indecomposable iff f is a power of an irreducible '
              'polynomial' % (cnt, dmax, F.order()))
    # Lambda-modules and representations with V_2 = Im(a) + Im(b) (p. 108)
    F = GF(2)
    ok = True
    for R, _, lab in kron_list(F, 4):
        a, b = R.maps
        if R.dims[1]:
            imab = dmatrix(F, R.dims[1], 2 * R.dims[0],
                           [list(a.row(i)) + list(b.row(i))
                            for i in range(R.dims[1])]).rank()
        else:
            imab = 0
        if (imab != R.dims[1]) != (R.dims == [0, 1]):
            ok = False
    check(ok, 'p. 108: among the listed indecomposable representations of '
          'the Kronecker quiver (dimensions <= 4, GF(2)) only S_2 has '
          'V_2 != Im(a) + Im(b)')
    lam_mod = gmod(v4_case_iv(F, 1), F)          # Lambda = kV4/Soc
    nend = len(mtx('BasisModuleEndomorphisms')(lam_mod))
    rep = kron(F, dmatrix(F, 1, 2, [1, 0]).transpose(),
               dmatrix(F, 1, 2, [0, 1]).transpose())
    check(nend == 3 and hom_dim(rep, rep) == 1,
          'p. 108: endomorphism rings are not preserved: End(Lambda) has '
          'dimension 3, End of the corresponding representation (1, 2) '
          'dimension 1')
    _kronecker_proof()
    _klein_four_modules()
    _a4_modules()
    _linear_relations()
    _butler()
    return stats


# ---------------------------------------------------------------------------
# The proof of Theorem 4.3.2 (pp. 109-110)
# ---------------------------------------------------------------------------


def _min_kernel(F, a, b, nmax=8):
    """Minimal n and v_0..v_n (columns) with a v_0 = 0, a v_i = b v_(i-1),
    b v_n = 0, i.e. (a + lambda b) sum (-1)^i v_i lambda^i = 0."""
    N1 = a.ncols()
    for n in range(nmax + 1):
        rows = []
        # unknowns: v_0..v_n, each N1 entries
        nv = (n + 1) * N1

        def blockrow(i_a, i_b):
            r = []
            for row in range(a.nrows()):
                v = [F(0)] * nv
                if i_a is not None:
                    for j in range(N1):
                        v[i_a * N1 + j] += a[row, j]
                if i_b is not None:
                    for j in range(N1):
                        v[i_b * N1 + j] -= b[row, j]
                r.append(v)
            return r
        rows += blockrow(0, None)
        for i in range(1, n + 1):
            rows += blockrow(i, i - 1)
        rows += [[-c for c in r] for r in blockrow(None, n)]
        K = dmatrix(F, len(rows), nv, rows).right_kernel()
        if K.dimension() > 0:
            v = K.basis()[0]
            return n, [vector(F, v[i * N1:(i + 1) * N1]) for i in range(n + 1)]
    return None, None


def _pencil_kernel_degree(F, A, B, maxdeg):
    """Is there a non-zero column vector u(lambda) of degree <= maxdeg with
    (A + lambda B) u = 0?"""
    if maxdeg < 0 or A.ncols() == 0:
        return False
    q = A.ncols()
    nv = (maxdeg + 1) * q
    rows = []
    for k in range(maxdeg + 2):             # coefficient of lambda^k
        for r in range(A.nrows()):
            v = [F(0)] * nv
            if k <= maxdeg:
                for j in range(q):
                    v[k * q + j] += A[r, j]
            if k >= 1:
                for j in range(q):
                    v[(k - 1) * q + j] += B[r, j]
            rows.append(v)
    if not rows:
        return True
    return dmatrix(F, rows).right_kernel().dimension() > 0


def E_lambda(F, n, printed=True):
    """E_lambda(n) as a pair (constant term, coefficient of lambda): rows
    (1, lambda) as printed on p. 109, or (lambda, 1) (bases v_0.., a v_1..)."""
    one = dmatrix(F, n, n + 1, lambda i, j: 1 if j == i else 0)
    lam = dmatrix(F, n, n + 1, lambda i, j: 1 if j == i + 1 else 0)
    return (one, lam) if printed else (lam, one)


def _kronecker_proof():
    # (a) the printed goal dim V_1 = n, dim V_2 = n + 1 is impossible: an
    # indecomposable with these dimensions has no kernel vector at all,
    # while E(n) (dimensions (n + 1, n)) has minimal degree n
    for F in (GF(2), GF(3)):
        for n in range(0, 6):
            A, B = E_lambda(F, n)
            m_col, _ = _min_kernel(F, A, B, nmax=n + 2)
            m_dual, _ = _min_kernel(F, A.transpose(), B.transpose(),
                                    nmax=n + 2)
            check(m_col == n and m_dual is None,
                  'proof of Thm 4.3.2 (corrected dim V_1 = n + 1, '
                  'dim V_2 = n): a + lambda b = E_lambda(%d) has a kernel '
                  'vector of minimal degree n, its transpose (dim V_1 = n, '
                  'dim V_2 = n + 1) none (GF(%d))' % (n, F.order()))
    refuted(any(_min_kernel(GF(2), *[X.transpose() for X in
                                    E_lambda(GF(2), n)], nmax=n + 2)[0]
                == n for n in range(1, 6)),
            'proof of Thm 4.3.2 as printed (p. 109): dim V_1 = n, '
            'dim V_2 = n + 1 with a kernel vector of degree n')
    # (b) E_lambda(n) maps polynomial vectors of degree <= n - 1
    # bijectively onto those of degree <= n (the corrected last step)
    for F in (GF(2), GF(3), QQ):
        for n in range(1, 7):
            for printed in (True, False):
                E0, E1 = E_lambda(F, n, printed)
                # unknowns w_k (k <= n - 1), n + 1 entries each
                rows = []
                for k in range(n + 1):
                    for r in range(n):
                        v = [F(0)] * (n * (n + 1))
                        if k <= n - 1:
                            for j in range(n + 1):
                                v[k * (n + 1) + j] += E0[r, j]
                        if k >= 1:
                            for j in range(n + 1):
                                v[(k - 1) * (n + 1) + j] += E1[r, j]
                        rows.append(v)
                Msq = dmatrix(F, rows)
                assert Msq.is_square()
                if Msq.rank() < Msq.nrows():
                    raise AssertionError('E_lambda(n) not bijective')
        check(True, 'corrected end of the proof of Thm 4.3.2 (p. 110): '
              'E_lambda(n) (rows (1, lambda) or (lambda, 1)) is a bijection '
              'from the vectors of degree <= n - 1 onto those of degree '
              '<= n, n <= 6, over %s' % F)
    # (b') the corrected last step: a column vector u in the kernel of M
    # (n block rows, A' on the diagonal, -B' below) gives u(lambda) =
    # sum (-1)^(i-1) u_i lambda^(i-1) with (A' + lambda B') u(lambda) = 0,
    # and w(lambda) of degree <= n - 1 with E w = -(C + lambda D) u(lambda)
    # makes (w, u) a kernel vector of the whole matrix
    for F in (GF(2), GF(3)):
        for trial in range(40):
            n = random.randint(2, 4)
            # A' + lambda B' with a planted kernel vector of degree n - 2:
            # E(n - 2) (rows (lambda, 1)) plus a random block
            Ae, Be = E_lambda(F, n - 2, printed=False)
            pr, qr = random.randint(0, 2), random.randint(0, 2)
            Ar = dmatrix(F, pr, qr, [F.random_element()
                                     for _ in range(pr * qr)])
            Br = dmatrix(F, pr, qr, [F.random_element()
                                     for _ in range(pr * qr)])
            A1 = dmatrix(F, Ae.nrows() + pr, Ae.ncols() + qr, 0)
            B1m = dmatrix(F, Ae.nrows() + pr, Ae.ncols() + qr, 0)
            A1.set_block(0, 0, Ae)
            B1m.set_block(0, 0, Be)
            A1.set_block(Ae.nrows(), Ae.ncols(), Ar)
            B1m.set_block(Ae.nrows(), Ae.ncols(), Br)
            p, qq = A1.nrows(), A1.ncols()
            Mm = dmatrix(F, n * p, (n - 1) * qq, 0)
            for j in range(n - 1):
                for r in range(p):
                    for c in range(qq):
                        Mm[j * p + r, j * qq + c] = A1[r, c]
                        Mm[(j + 1) * p + r, j * qq + c] = -B1m[r, c]
            K = Mm.right_kernel()
            assert K.dimension() > 0
            u = next(iter(K.basis()))
            us = [u[i * qq:(i + 1) * qq] for i in range(n - 1)]
            # coefficients of u(lambda), and (A' + lambda B') u(lambda) = 0
            ucoef = [(-1) ** i * us[i] for i in range(n - 1)]
            ok = True
            for k in range(n):
                tot = vector(F, [0] * p)
                if k < n - 1:
                    tot += _mv(F, A1, ucoef[k])
                if k >= 1:
                    tot += _mv(F, B1m, ucoef[k - 1])
                if tot != 0:
                    ok = False
            E0, E1 = E_lambda(F, n, printed=False)
            C = dmatrix(F, n, qq, [F.random_element() for _ in range(n * qq)])
            Dm = dmatrix(F, n, qq, [F.random_element()
                                    for _ in range(n * qq)])
            # right-hand side -(C + lambda D) u(lambda), degree <= n - 1
            rhs = []
            for k in range(n):
                t = vector(F, [0] * n)
                if k < n - 1:
                    t -= _mv(F, C, ucoef[k])
                if k >= 1:
                    t -= _mv(F, Dm, ucoef[k - 1])
                rhs.append(t)
            # unknowns w_0..w_(n-1) in F^(n+1); equations: coefficients of
            # lambda^0..lambda^n of E0 w + lambda E1 w
            rows, b = [], []
            for k in range(n + 1):
                for r in range(n):
                    v = [F(0)] * (n * (n + 1))
                    if k <= n - 1:
                        for j in range(n + 1):
                            v[k * (n + 1) + j] += E0[r, j]
                    if k >= 1:
                        for j in range(n + 1):
                            v[(k - 1) * (n + 1) + j] += E1[r, j]
                    rows.append(v + [-(rhs[k][r] if k < n else 0)])
            sol = dmatrix(F, rows).right_kernel()
            sv = next(v for v in sol.basis() if v[-1] != 0)
            w = [vector(F, [sv[k * (n + 1) + j] / sv[-1]
                            for j in range(n + 1)]) for k in range(n)]
            # (E C + lambda D; 0 A' + lambda B') (w; u) = 0, coefficientwise
            for k in range(n + 1):
                top = vector(F, [0] * n)
                if k < n:
                    top += _mv(F, E0, w[k])
                if k >= 1:
                    top += _mv(F, E1, w[k - 1])
                if k < n - 1:
                    top += _mv(F, C, ucoef[k])
                if 1 <= k <= n - 1:
                    top += _mv(F, Dm, ucoef[k - 1])
                if top != 0:
                    ok = False
            check(ok and u != 0,
                  'corrected end of the proof of Thm 4.3.2 (p. 110): a '
                  'column vector u with M u = 0 gives (A\' + lambda B\') '
                  'u(lambda) = 0, deg u <= n - 2, and with E w = -(C + '
                  'lambda D) u, deg w <= n - 1, the vector (w, u) is '
                  'annihilated by a + lambda b (GF(%d), n = %d)'
                  % (F.order(), n))
    # (c) random representations: the whole argument
    cnt = 0
    vprime_fails = 0
    for F in (GF(2), GF(3)):
        for trial in range(150):
            N2 = random.randint(1, 4)
            N1 = random.randint(N2 + 1, N2 + 2)
            a = dmatrix(F, N2, N1, [F.random_element() for _ in
                                    range(N1 * N2)])
            b = dmatrix(F, N2, N1, [F.random_element() for _ in
                                    range(N1 * N2)])
            n, v = _min_kernel(F, a, b)
            av = [a * x for x in v[1:]] if F.characteristic() == 2 else \
                [a.sparse_matrix() * x for x in v[1:]]
            check(n is not None and dmatrix(F, v).rank() == n + 1
                  and (n == 0 or dmatrix(F, av).rank() == n),
                  'proof of Thm 4.3.2: v_0..v_n and a v_1..a v_n are '
                  'linearly independent (random (a, b), GF(%d), dims (%d, '
                  '%d), n = %d)' % (F.order(), N1, N2, n))
            # bases: v_0..v_n, completed; a v_1..a v_n, completed
            B1 = _complete(F, [list(x) for x in v], N1)
            B2 = _complete(F, [list(x) for x in av], N2)
            P1, P2 = dmatrix(F, B1).transpose(), dmatrix(F, B2).transpose()
            P2i = P2.inverse()
            a2 = _mm(F, _mm(F, P2i, a), P1)
            b2 = _mm(F, _mm(F, P2i, b), P1)
            p, qq = N2 - n, N1 - n - 1
            E0, E1 = a2[:n, :n + 1], b2[:n, :n + 1]
            ok = (a2[n:, :n + 1].is_zero() and b2[n:, :n + 1].is_zero()
                  and (E0, E1) == E_lambda(F, n, printed=False))
            rev1 = list(range(n, -1, -1))
            rev2 = list(range(n - 1, -1, -1))
            ok = ok and (E0.matrix_from_rows_and_columns(rev2, rev1),
                         E1.matrix_from_rows_and_columns(rev2, rev1)) \
                == E_lambda(F, n)
            check(ok, 'proof of Thm 4.3.2 (p. 109): in the bases v_0..v_n, '
                  'a v_1..a v_n the matrix is (E C+lD; 0 A\'+lB\') with E '
                  'of rows (lambda, 1); reversing both bases gives the '
                  'printed E_lambda(n)')
            C, Dm = a2[:n, n + 1:], b2[:n, n + 1:]
            A1, B1m = a2[n:, n + 1:], b2[n:, n + 1:]
            # the pairing: E Y = Ybar + lambda Yunder for E of rows
            # (lambda, 1) (as printed), = Yunder + lambda Ybar for the
            # printed E_lambda(n)
            Y = dmatrix(F, n + 1, qq, [F.random_element()
                                       for _ in range((n + 1) * qq)])
            Ybar, Yund = Y[1:, :], Y[:n, :]
            Ep0, Ep1 = E_lambda(F, n)
            check(_mm(F, E0, Y) == Ybar and _mm(F, E1, Y) == Yund
                  and _mm(F, Ep0, Y) == Yund and _mm(F, Ep1, Y) == Ybar,
                  'proof of Thm 4.3.2 (p. 110): the printed pairing '
                  'X A\' + C + Ybar = 0, X B\' + D + Yunder = 0 fits the '
                  'bases v_0.., a v_1.. (for the printed E_lambda(n) the '
                  'bar and underbar are exchanged)')
            if n == 0:
                continue
            # the matrix M of the elimination: n block rows, n - 1 block
            # columns, A' on the diagonal, -B' below
            Mm = dmatrix(F, n * p, (n - 1) * qq, 0)
            for j in range(n - 1):
                for r in range(p):
                    for c in range(qq):
                        Mm[j * p + r, j * qq + c] = A1[r, c]
                        Mm[(j + 1) * p + r, j * qq + c] = -B1m[r, c]
            # elimination: X M = (d_(i+1) - c_i) iff Y exists
            Xr = dmatrix(F, n, p, [F.random_element() for _ in
                                   range(n * p)])
            xrow = vector(F, Xr.list())
            lhs = xrow * Mm.sparse_matrix() if _sparse(F) else xrow * Mm
            rhs_needed = vector(F, sum([list(Dm.row(i + 1) - C.row(i))
                                        for i in range(n - 1)], []))
            XA = _mm(F, Xr, A1)
            XB = _mm(F, Xr, B1m)
            Ysol_ok = all(-(XA.row(i) + C.row(i)) == -(XB.row(i + 1)
                                                       + Dm.row(i + 1))
                          for i in range(n - 1))
            check(Ysol_ok == (lhs == rhs_needed) and Dm.nrows() == n,
                  'proof of Thm 4.3.2 (p. 110): eliminating Y gives '
                  'x_i A\' - x_(i+1) B\' = d_(i+1) - c_i (i <= n - 1); D has '
                  'n rows, so the printed last entry d_(n+1, m-1) - '
                  'c_(n, m-1) does not exist')
            check(Mm.nrows() == n * p and Mm.ncols() == (n - 1) * qq,
                  'proof of Thm 4.3.2: the matrix has n m rows and '
                  '(n - 1)(m - 1) columns (m = dim V_2 - n = %d, '
                  'm - 1 -> dim V_1 - n - 1 = %d)' % (p, qq))
            if (n - 1) * qq != n * p and (n - 1) * qq > 0:
                refuted(Mm.nrows() == (n - 1) * qq,
                        'proof of Thm 4.3.2 as printed: a (n - 1)(m - 1) x '
                        'n m matrix')
            # full column rank <=> no column kernel vector of A' + l B' of
            # degree <= n - 2; there is none of degree <= n - 1
            fcr = (Mm.rank() == Mm.ncols())
            check(fcr == (not _pencil_kernel_degree(F, A1, B1m, n - 2))
                  and not _pencil_kernel_degree(F, A1, B1m, n - 1) and fcr,
                  'proof of Thm 4.3.2 (corrected): M has full column rank, '
                  'i.e. A\' + lambda B\' has no column kernel vector of '
                  'degree <= n - 2 (none even of degree <= n - 1)')
            # solve and block diagonalise
            if Mm.ncols():
                # x M = rhs via the kernel of (M^T | -rhs) (no products)
                aug = dmatrix(F, [list(Mm.column(j)) + [-rhs_needed[j]]
                                  for j in range(Mm.ncols())])
                sol = next(v for v in aug.right_kernel().basis()
                           if v[-1] != 0)
                xs = vector(F, [c / sol[-1] for c in sol[:-1]])
            else:
                xs = vector(F, [0] * (n * p))
            lhs = xs * Mm.sparse_matrix() if _sparse(F) else xs * Mm
            check(lhs == rhs_needed,
                  'proof of Thm 4.3.2: the solution x of x M = '
                  '(d_(i+1) - c_i) '
                  'exists (full column rank)')
            X = dmatrix(F, n, p, list(xs))
            XA, XB = _mm(F, X, A1), _mm(F, X, B1m)
            Y = dmatrix(F, n + 1, qq, 0)
            for i in range(n):
                for c in range(qq):
                    Y[i + 1, c] = -(XA[i, c] + C[i, c])
            for c in range(qq):
                Y[0, c] = -(XB[0, c] + Dm[0, c])
            ok = (XA + C + _mm(F, E0, Y)).is_zero() and \
                (XB + Dm + _mm(F, E1, Y)).is_zero()
            check(ok, 'proof of Thm 4.3.2: X, Y with X(A\' + lambda B\') + '
                  '(C + lambda D) + E Y = 0 exist (block diagonalisation)')
            # the printed step: a row vector u with u M = 0 always exists
            # (n m > (n - 1)(m - 1)), but there is no column vector of
            # degree n - 1 annihilated by a + lambda b
            if Mm.nrows() > Mm.ncols():
                lk = Mm.transpose().right_kernel()
                exists_u = lk.dimension() > 0
                exists_col = _min_kernel(F, a, b, nmax=n - 1)[0] is not None
                refuted((not exists_u) or exists_col,
                        'proof of Thm 4.3.2 as printed (p. 110): a row vector '
                        'u != 0 with u M = 0 (it exists, '
                        'n m > (n - 1)(m - 1)) '
                        'gives a column vector of degree n - 1 annihilated by '
                        'a + lambda b (there is none, n being minimal)')
                # the printed v'(lambda) = sum (-1)^(i-1) u_i lambda^(i-1)
                bad = False
                for u in lk.basis():
                    us = [u[i * p:(i + 1) * p] for i in range(n)]
                    for kdeg in range(n + 1):
                        coef = vector(F, [0] * qq)
                        if kdeg < n:
                            coef += (-1) ** kdeg * (
                                us[kdeg] * A1.sparse_matrix() if _sparse(F)
                                else us[kdeg] * A1)
                        if kdeg >= 1:
                            coef += (-1) ** (kdeg - 1) * (
                                us[kdeg - 1] * B1m.sparse_matrix()
                                if _sparse(F) else us[kdeg - 1] * B1m)
                        if coef != 0:
                            bad = True
                vprime_fails += bad
            cnt += 1
    check(cnt > 0, 'proof of Thm 4.3.2: %d random singular cases with '
          'n >= 1 worked through' % cnt)
    refuted(vprime_fails == 0,
            'proof of Thm 4.3.2 as printed: for u with u M = 0 the printed '
            'v\'(lambda) satisfies v\'(lambda)(A\' + lambda B\') = 0 (fails '
            'in %d of the cases)' % vprime_fails)


def _mv(F, A, v):
    """A v without dense products in odd characteristic."""
    if A.ncols() == 0:
        return vector(F, [0] * A.nrows())
    return (A.sparse_matrix() * v) if _sparse(F) else A * v


def _mm(F, A, B):
    if _sparse(F):
        return (A.sparse_matrix() * B.sparse_matrix()).dense_matrix()
    return A * B


def _complete(F, vecs, N):
    basis = [list(v) for v in vecs]
    for i in range(N):
        e = [F(0)] * N
        e[i] = F(1)
        if dmatrix(F, basis + [e]).rank() > len(basis):
            basis.append(e)
    assert len(basis) == N
    return basis


# ---------------------------------------------------------------------------
# kV4-modules and A4-modules with the MeatAxe (row vectors, as printed)
# ---------------------------------------------------------------------------

_GAPF = {}


def mtx(name):
    key = 'MTX.' + name
    if key not in _GAPF:
        _GAPF[key] = libgap.eval(key)
    return _GAPF[key]


FAIL = libgap.eval('fail')


def gmod(mats, F):
    return libgap.GModuleByMats([libgap(dmatrix(F, A)) for A in mats],
                                libgap.GF(F.order()))


def iso(M, N):
    return mtx('IsomorphismModules')(M, N) != FAIL


def blk(F, A, B, C, D):
    """The block matrix (A B; C D)."""
    return dmatrix(F, [list(A.row(i)) + list(B.row(i))
                       for i in range(A.nrows())]
                   + [list(C.row(i)) + list(D.row(i))
                      for i in range(C.nrows())])


def zero(F, r, c):
    return dmatrix(F, r, c, 0)


def ident(F, n):
    return _identity_matrix(F, n)


def v4_case_ii(F, J):
    n = J.nrows()
    I, Z = ident(F, n), zero(F, n, n)
    return [blk(F, I, I, Z, I), blk(F, I, J, Z, I)]


def v4_case_iii(F, n):
    R = PolynomialRing(F, 'lam')
    J0 = companion(F, R.gen() ** n)
    I, Z = ident(F, n), zero(F, n, n)
    return [blk(F, I, J0, Z, I), blk(F, I, I, Z, I)]


def v4_case_iv(F, n):
    A = dmatrix(F, n, n + 1, lambda i, j: 1 if j == i else 0)
    B = dmatrix(F, n, n + 1, lambda i, j: 1 if j == i + 1 else 0)
    return [blk(F, ident(F, n), A, zero(F, n + 1, n), ident(F, n + 1)),
            blk(F, ident(F, n), B, zero(F, n + 1, n), ident(F, n + 1))]


def v4_case_v(F, n):
    A = dmatrix(F, n + 1, n, lambda i, j: 1 if i == j else 0)
    B = dmatrix(F, n + 1, n, lambda i, j: 1 if i == j + 1 else 0)
    return [blk(F, ident(F, n + 1), A, zero(F, n, n + 1), ident(F, n)),
            blk(F, ident(F, n + 1), B, zero(F, n, n + 1), ident(F, n))]


def v4_regular(F):
    # right regular representation of V4 = {1, x, y, xy}
    els = [(0, 0), (1, 0), (0, 1), (1, 1)]

    def R(g):
        return dmatrix(F, 4, 4, lambda i, j: 1 if tuple(
            (els[i][k] + g[k]) % 2 for k in range(2)) == els[j] else 0)
    return [R((1, 0)), R((0, 1))]


def indec_rcf(F, n):
    """The indecomposable rational canonical forms of size n."""
    R = PolynomialRing(F, 'lam')
    out = []
    for d in range(1, n + 1):
        if n % d:
            continue
        for p in R.polynomials(of_degree=d):
            if p.is_monic() and p.is_irreducible():
                out.append(companion(F, p ** (n // d)))
    return out


def omega_v4(F, mats):
    """Omega of a kV4-module given by the matrices of x, y (row vectors):
    the kernel of its projective cover kV4^d -> M (d = dim M/Rad M)."""
    reg = v4_regular(F)
    dim = mats[0].nrows()
    I = ident(F, dim)
    rad = dmatrix(F, [list(r) for A in mats for r in (A - I).rows()])
    radsp = rad.row_space()
    gens = []
    for i in range(dim):
        e = vector(F, [1 if j == i else 0 for j in range(dim)])
        if e not in radsp + (F ** dim).subspace(gens):
            gens.append(e)
    d = len(gens)
    els = [ident(F, dim), mats[0], mats[1], mats[0] * mats[1]]
    # phi: kV4^d -> M, basis (i, g) -> gens[i] g
    phi = dmatrix(F, [list(gens[i] * g) for i in range(d) for g in els])
    K = phi.left_kernel().basis_matrix()
    # the action on K: K * blockdiag(R_g) = A_g K
    out = []
    for Rg in reg:
        BD = dmatrix(F, 4 * d, 4 * d, 0)
        for i in range(d):
            BD.set_block(4 * i, 4 * i, Rg)
        KR = K * BD
        out.append(K.solve_left(KR))
    return out


def dual_v4(mats):
    return [A.transpose() for A in mats]


def _klein_four_modules():
    for F, nmax in ((GF(2), 4), (GF(4, 'w'), 3)):
        q = F.order()
        ind = mtx('IsIndecomposable')
        mods = {}       # dimension -> list of (label, gap module, mats)
        mods.setdefault(4, []).append(('(i)', gmod(v4_regular(F), F),
                                       v4_regular(F)))
        for n in range(1, nmax + 1):
            for J in indec_rcf(F, n):
                m = v4_case_ii(F, J)
                mods.setdefault(2 * n, []).append(('(ii)', gmod(m, F), m))
            m = v4_case_iii(F, n)
            mods.setdefault(2 * n, []).append(('(iii)', gmod(m, F), m))
        for n in range(0, nmax + 1):
            for lab, m in (('(iv)', v4_case_iv(F, n)),
                           ('(v)', v4_case_v(F, n))):
                if n == 0 and lab == '(v)':
                    continue
                mods.setdefault(2 * n + 1, []).append((lab, gmod(m, F), m))
        ok_rel = all(A * A == 1 for L in mods.values() for _, _, m in L
                     for A in m) and all(m[0] * m[1] == m[1] * m[0]
                                         for L in mods.values()
                                         for _, _, m in L)
        check(ok_rel, 'Thm 4.3.3 over GF(%d): the printed matrices satisfy '
              'x^2 = y^2 = 1, xy = yx' % q)
        ok_ind = all(ind(M) for L in mods.values() for _, M, _ in L)
        ok_iso = all(not iso(L[i][1], L[j][1]) for L in mods.values()
                     for i, j in itertools.combinations(range(len(L)), 2))
        ntot = sum(len(L) for L in mods.values())
        check(ok_ind and ok_iso,
              'Thm 4.3.3 over GF(%d): the %d listed modules of dimension '
              '<= %d are indecomposable and pairwise non-isomorphic'
              % (q, ntot, 2 * nmax + 1))
        check(iso(gmod(v4_case_iv(F, 0), F), gmod(v4_case_v(F, 0), F))
              and all(not iso(gmod(v4_case_iv(F, n), F),
                              gmod(v4_case_v(F, n), F))
                      for n in range(1, nmax + 1)),
              'Thm 4.3.3 (iv), (v): isomorphic iff n = 0 (GF(%d))' % q)
        # counts: dimension 2n: points of P^1 of degree d, e = n/d
        R = PolynomialRing(F, 'lam')
        for n in range(1, nmax + 1):
            pts = sum(len([p for p in R.polynomials(of_degree=d)
                           if p.is_monic() and p.is_irreducible()])
                      + (1 if d == 1 else 0)
                      for d in range(1, n + 1) if n % d == 0)
            check(len(mods[2 * n]) - (1 if n == 2 else 0) == pts,
                  'Thm 4.3.3 (ii), (iii): %d modules of dimension %d over '
                  'GF(%d), one for each point of P^1 of degree dividing %d'
                  % (pts, 2 * n, q, n))
        # Remark: (iv) = Omega^-n(k), (v) = Omega^n(k)
        k = [ident(F, 1), ident(F, 1)]
        om, omi = k, k
        ok = True
        for n in range(1, nmax + 1):
            om = omega_v4(F, om)
            omi = dual_v4(omega_v4(F, dual_v4(omi)))
            if not (iso(gmod(om, F), gmod(v4_case_v(F, n), F))
                    and iso(gmod(omi, F), gmod(v4_case_iv(F, n), F))):
                ok = False
            if n == 1:
                # column reading (transposed matrices): roles exchanged
                tr = gmod(dual_v4(v4_case_iv(F, 1)), F)
                colswap = iso(tr, gmod(om, F))
        check(ok and colswap,
              'Remark after Thm 4.3.3: the modules (iv) are Omega^-n(k) and '
              '(v) are Omega^n(k), n <= %d, GF(%d) (with row vectors; read '
              'with column vectors (iv) would be Omega^n(k))' % (nmax, q))
        # correspondence with the Kronecker list (cases (iv), (v) <-> (ii),
        # (iii)) and with Lambda = kV4/Soc: V_2 = Im(x-1) + Im(y-1)
        for n in range(1, nmax + 1):
            m = v4_case_iv(F, n)
            I = ident(F, 2 * n + 1)
            rad = dmatrix(F, [list(r) for A in m for r in (A - I).rows()])
            check(rad.rank() == n + 1,
                  'proof of Thm 4.3.3: the module (iv) for n = %d has '
                  'V_2 = Im(x - 1) + Im(y - 1) of dimension n + 1 (case (ii) '
                  'of Thm 4.3.2, row vectors)' % n)
    _v4_orbit_count()


def _v4_orbit_count():
    """Isomorphism classes of kV4-modules of dimension N <= 4 over GF(2):
    orbits of GL_N(2) on pairs of commuting X, Y with X^2 = Y^2 = 1, against
    the sums of the modules of Theorem 4.3.3."""
    # indecomposables over GF(2) by dimension (Thm 4.3.3): 1: k; 2: 3;
    # 3: 2; 4: kV4 and 4 of type (ii)/(iii)
    ind = {1: 1, 2: 3, 3: 2, 4: 5}

    def nsums(N):
        # number of multisets of indecomposables of total dimension N
        from sage.all import Partitions
        tot = 0
        for part in Partitions(N):
            mult = {}
            for p in part:
                mult[p] = mult.get(p, 0) + 1
            t = 1
            for p, m in mult.items():
                from sage.all import binomial
                t *= binomial(ind[p] + m - 1, m)
            tot += t
        return tot

    def mul(A, B, N):
        out = []
        for i in range(N):
            r = 0
            for k in range(N):
                if (A[i] >> k) & 1:
                    r ^= B[k]
            out.append(r)
        return tuple(out)
    for N in range(1, 5):
        I = tuple(1 << i for i in range(N))
        allm = itertools.product(range(1 << N), repeat=N)
        invol = [A for A in allm if mul(A, A, N) == I]
        pairs = [(A, B) for A in invol for B in invol
                 if mul(A, B, N) == mul(B, A, N)]
        G = libgap.GL(N, 2)
        gens = []
        for g in list(G.GeneratorsOfGroup()):
            rows = [[int(str(c) == 'Z(2)^0') for c in row] for row in g]
            rowsi = [[int(str(c) == 'Z(2)^0') for c in row]
                     for row in g.Inverse()]
            gens.append((tuple(sum(rows[i][k] << k for k in range(N))
                               for i in range(N)),
                         tuple(sum(rowsi[i][k] << k for k in range(N))
                               for i in range(N))))
        seen = set()
        orbits = 0
        for pr in pairs:
            if pr in seen:
                continue
            orbits += 1
            seen.add(pr)
            todo = [pr]
            while todo:
                A, B = todo.pop()
                for g, gi in gens:
                    img = (mul(mul(gi, A, N), g, N), mul(mul(gi, B, N), g, N))
                    if img not in seen:
                        seen.add(img)
                        todo.append(img)
        check(orbits == nsums(N),
              'Thm 4.3.3 over GF(2): %d isomorphism classes of kV4-modules '
              'of dimension %d (orbits on %d pairs of matrices) = sums of '
              'the listed indecomposables' % (orbits, N, len(pairs)))


# ---------------------------------------------------------------------------
# A4 (p. 112)
# ---------------------------------------------------------------------------


def _a4_group():
    G = AlternatingGroup(4)
    x, y = G('(1,2)(3,4)'), G('(1,3)(2,4)')
    t = next(g for g in G if g.order() == 3 and g * x * g ** -1 == x * y
             and g * y * g ** -1 == x)
    return G, x, y, t


def a4_mats(G, gens, gmats, F):
    """Matrices of all elements of G from those of the generators (a
    homomorphism; consistency is asserted)."""
    one = G.identity()
    dim = gmats[0].nrows()
    mats = {one: ident(F, dim)}
    todo = [one]
    while todo:
        g = todo.pop()
        for s, A in zip(gens, gmats):
            h = g * s
            Mh = mats[g] * A
            if h in mats:
                assert mats[h] == Mh, 'not a representation'
            else:
                mats[h] = Mh
                todo.append(h)
    return mats


def induce_v4_a4(F, vm, G, x, y, t):
    """V up to A4 for a V4-module V (matrices of x, y; right modules):
    basis v (x) r, r in {1, t, t^2}; (v (x) r) g = v h (x) r' with
    r g = h r'."""
    reps = [G.identity(), t, t * t]
    Hm = {G.identity(): ident(F, vm[0].nrows()), x: vm[0], y: vm[1],
          x * y: vm[0] * vm[1]}
    d = vm[0].nrows()

    def act(g):
        M = dmatrix(F, 3 * d, 3 * d, 0)
        for i, r in enumerate(reps):
            for j, r2 in enumerate(reps):
                h = r * g * r2 ** -1
                if h in Hm:
                    M.set_block(i * d, j * d, Hm[h])
        return M
    return [act(x), act(y), act(t)]


def omega_a4(F, mats, G, gens):
    """Omega of an A4-module (matrices of the generators x, y, t): the
    kernel of the free cover kA4^d -> M, minus its projective summands."""
    allm = a4_mats(G, gens, mats, F)
    els = sorted(allm, key=str)
    dim = mats[0].nrows()
    d = dim
    gensM = [vector(F, [1 if j == i else 0 for j in range(dim)])
             for i in range(dim)]
    phi = dmatrix(F, [list(gensM[i] * allm[g]) for i in range(d)
                      for g in els])
    K = phi.left_kernel().basis_matrix()
    idx = {g: i for i, g in enumerate(els)}
    out = []
    for s in gens:
        Rg = dmatrix(F, 12, 12, lambda i, j: 1 if idx[els[i] * s] == j
                     else 0)
        BD = dmatrix(F, 12 * d, 12 * d, 0)
        for i in range(d):
            BD.set_block(12 * i, 12 * i, Rg)
        out.append(K.solve_left(K * BD))
    M = gmod(out, F)
    # strip projective summands (dimension 4, projective restriction)
    keep = []
    for summand in mtx('Indecomposition')(M):
        X = summand[1]
        Xm = [dmatrix(F, [[c.sage(ring=F) for c in row] for row in A])
              for A in libgap.eval('x -> x.generators')(X)]
        if Xm[0].nrows() % 4 == 0 and _v4_free(F, Xm[:2]):
            continue
        keep.append(Xm)
    assert len(keep) == 1
    return keep[0]


def dual_a4(m):
    """The dual module: g -> transpose of the matrix of g^-1 (x, y are
    involutions)."""
    return [m[0].transpose(), m[1].transpose(), m[2].inverse().transpose()]


def _v4_free(F, xy):
    """Is the restriction to V4 free?  (dim of fixed points of the norm)"""
    X, Y = xy
    I = ident(F, X.nrows())
    N = (X + I) * (Y + I)
    return N.rank() * 4 == X.nrows()


def _a4_modules():
    G, x, y, t = _a4_group()
    for F, nmax in ((GF(4, 'w'), 3), (GF(16, 'z'), 1)):
        q = F.order()
        w = F.multiplicative_generator() ** ((q - 1) // 3)   # omega
        wb = w ** 2
        pts = list(F) + ['inf']

        def V(n, alpha):
            if alpha == 'inf':
                return v4_case_iii(F, n)
            R = PolynomialRing(F, 'lam')
            return v4_case_ii(F, companion(F, (R.gen() - alpha) ** n))

        def f(alpha):
            if alpha == 'inf':
                return F(0)
            if alpha == 1:
                return 'inf'
            return 1 / (1 - alpha)
        # the action of t on P^1: V^t (x acts as t x t^-1 = xy, y as
        # t y t^-1 = x) is V_(1, f(alpha))
        ok = True
        for alpha in pts:
            m = V(1, alpha)
            conj = gmod([m[0] * m[1], m[0]], F)
            img = [b for b in pts if iso(conj, gmod(V(1, b), F))]
            if img != [f(alpha)]:
                ok = False
        fixed = [a for a in pts if f(a) == a]
        check(ok and sorted(map(str, fixed)) == sorted(map(str, [w, wb])),
              'p. 112: t acts on P^1(GF(%d)) by alpha -> 1/(1 - alpha); the '
              'fixed points are omega, omegabar' % q)
        ind = mtx('IsIndecomposable')
        ok = True
        cnt = 0
        for n in range(1, nmax + 1 if q == 4 else 2):
            for alpha in pts:
                if alpha in (w, wb) or (q == 4 and n > 2):
                    continue
                Wm = induce_v4_a4(F, V(n, alpha), G, x, y, t)
                a4_mats(G, [x, y, t], Wm, F)
                if not ind(gmod(Wm, F)):
                    ok = False
                cnt += 1
        check(ok, 'p. 112: W_(n, alpha) = V_(n, alpha) induced to A4 is '
              'indecomposable for the %d non-fixed alpha in P^1(GF(%d)), '
              'n <= %d' % (cnt, q, 2 if q == 4 else 1))
        if q != 4:
            continue
        # the three simples k, omega, omegabar of A4
        one = ident(F, 1)
        simples = {c: [one, one, c * one] for c in (F(1), w, wb)}
        for n in range(1, nmax + 1):
            for alpha in (w, wb):
                Wm = induce_v4_a4(F, V(n, alpha), G, x, y, t)
                summ = mtx('Indecomposition')(gmod(Wm, F))
                parts = [[dmatrix(F, [[c.sage(ring=F) for c in row]
                                      for row in A])
                          for A in libgap.eval('x -> x.generators')(s[1])]
                         for s in summ]
                P0 = parts[0]
                tw = [[P0[0], P0[1], c * P0[2]] for c in (F(1), w, wb)]
                ok = (len(parts) == 3
                      and all(any(iso(gmod(P, F), gmod(T, F)) for P in parts)
                              for T in tw)
                      and all(not iso(gmod(tw[i], F), gmod(tw[j], F))
                              for i, j in itertools.combinations(range(3), 2))
                      and all(iso(gmod(P[:2], F), gmod(V(n, alpha), F))
                              for P in parts))
                check(ok, 'p. 112: for alpha = %s, V_(%d, alpha) induced '
                      'to A4 has three summands W, W (x) omega, W (x) '
                      'omegabar, each restricting to V_(%d, alpha)'
                      % ('omega' if alpha == w else 'omegabar', n, n))
            # the printed matrices of W_(n, omega)(1)
            N = dmatrix(F, n, n, lambda i, j: 1 if i == j + 1 else 0)
            Xm = wb * ident(F, n) + w * N
            Ym = w * ident(F, n) + wb * N
            I, Z = ident(F, n), zero(F, n, n)
            exps = [n - 2 * k for k in range(1, n + 1)] + \
                [n - 2 * k for k in range(0, n)]
            T = dmatrix(F, 2 * n, 2 * n,
                        lambda i, j: w ** exps[i] if i == j else 0)
            Wp = [blk(F, I, Xm, Z, I), blk(F, I, Ym, Z, I), T]
            a4_mats(G, [x, y, t], Wp, F)        # an A4-module
            Wg = gmod(Wp, F)
            res = gmod(Wp[:2], F)
            ind_up = {}
            for alpha in (w, wb):
                Wm = induce_v4_a4(F, V(n, alpha), G, x, y, t)
                ind_up[alpha] = any(
                    iso(Wg, s[1]) for s in mtx('Indecomposition')(
                        gmod(Wm, F)))
            check(ind(Wg) and iso(res, gmod(V(n, wb), F))
                  and ind_up[wb] and T ** 3 == 1,
                  'p. 112, n = %d: the printed matrices of "W_(n, omega)(1)" '
                  'define an indecomposable A4-module restricting to '
                  'V_(n, omegabar), a summand of V_(n, omegabar) induced '
                  '(corrected label W_(n, omegabar)(1))' % n)
            refuted(iso(res, gmod(V(n, w), F)) or ind_up[w],
                    'p. 112 as printed (n = %d): the matrices give a summand '
                    'W_(n, omega)(1) of V_(n, omega) induced' % n)
        # Omega^(+-n) of the three simples: restrictions Omega^(+-n)(k),
        # pairwise non-isomorphic
        for n in (1, 2):
            for sign in (1, -1):
                res_ok, mods = True, []
                for c, sm in simples.items():
                    m = sm
                    for _ in range(n):
                        if sign == 1:
                            m = omega_a4(F, m, G, [x, y, t])
                        else:
                            m = dual_a4(omega_a4(F, dual_a4(m), G,
                                                 [x, y, t]))
                    mods.append(m)
                    target = v4_case_v(F, n) if sign == 1 else \
                        v4_case_iv(F, n)
                    if not iso(gmod(m[:2], F), gmod(target, F)):
                        res_ok = False
                check(res_ok and all(not iso(gmod(mods[i], F),
                                             gmod(mods[j], F))
                                     for i, j in itertools.combinations(
                                         range(3), 2)),
                      'p. 112: Omega^(%s%d) of the simples k, omega, '
                      'omegabar of A4 restrict to Omega^(%s%d)(k) of V4 and '
                      'are pairwise non-isomorphic'
                      % ('' if sign == 1 else '-', n,
                         '' if sign == 1 else '-', n))


# ---------------------------------------------------------------------------
# Linear relations (Definition 4.3.4 - Corollary 4.3.6), Butler
# ---------------------------------------------------------------------------


def _subspaces(F, m):
    """All subspaces of F^m as sets of tuples (grown one vector at a time;
    Sage's subspaces(m) of F^m multiplies dense matrices)."""
    out = []
    for k in range(m + 1):
        for piv in itertools.combinations(range(m), k):
            # free entries of a reduced row echelon form with these pivots
            free = [(i, j) for i in range(k) for j in range(piv[i] + 1, m)
                    if j not in piv]
            for vals in itertools.product(F, repeat=len(free)):
                rows = [[F(0)] * m for _ in range(k)]
                for i in range(k):
                    rows[i][piv[i]] = F(1)
                for (i, j), c in zip(free, vals):
                    rows[i][j] = c
                out.append(frozenset(
                    tuple(sum((c * r[j] for c, r in zip(cs, rows)), F(0))
                          for j in range(m))
                    for cs in itertools.product(F, repeat=k)))
    return out


def _linear_relations():
    total = 0
    for F, m in ((GF(2), 2), (GF(2), 3), (GF(3), 2)):
        Vs = _subspaces(F, m)
        V = frozenset(tuple(v) for v in (F ** m))
        zerov = tuple(F(0) for _ in range(m))

        def image(C, U):
            return frozenset(c[m:] for c in C if c[:m] in U)

        def inverse(C):
            return frozenset(c[m:] + c[:m] for c in C)

        def primes(C):
            cur, prev = frozenset([zerov]), None
            while cur != prev:
                prev, cur = cur, cur | image(C, cur)
            C1 = cur
            cur, prev = V, None
            while cur != prev:
                prev, cur = cur, image(C, cur) & cur
            C2 = cur
            return C1, C2

        def add(U, W):
            return frozenset(tuple(a + b for a, b in zip(u, w))
                             for u in U for w in W)
        for C in _subspaces(F, 2 * m):
            total += 1
            C1, C2 = primes(C)
            assert C1 <= C2, "C' <= C''"
            found = False
            for U in Vs:
                if not (U & C1 == frozenset([zerov]) and add(U, C1) == C2):
                    continue
                CU = frozenset(c for c in C if c[:m] in U and c[m:] in U)
                # graph of an automorphism of U
                if not (len(CU) == len(U)
                        and frozenset(c[:m] for c in CU) == U
                        and frozenset(c[m:] for c in CU) == U):
                    continue
                for W in Vs:
                    if not (U & W == frozenset([zerov]) and add(U, W) == V):
                        continue
                    CW = frozenset(c for c in C if c[:m] in W
                                   and c[m:] in W)
                    if add(CU, CW) != C:
                        continue
                    # regular part of C cap (W x W) on W is zero
                    cur, prev = frozenset([zerov]), None
                    while cur != prev:
                        prev, cur = cur, cur | image(CW, cur)
                    W1 = cur
                    cur, prev = W, None
                    while cur != prev:
                        prev, cur = cur, image(CW, cur) & cur
                    if W1 != cur:
                        continue
                    # Corollary 4.3.6
                    D1, D2 = primes(inverse(C))
                    if not (U & D1 == frozenset([zerov])
                            and add(U, D1) == D2):
                        continue
                    found = True
                    break
                if found:
                    break
            assert found, 'Prop 4.3.5 fails'
            # the automorphism phi of C''/C': for x in a coset K, the
            # non-empty (Cx cap C'') + C' are one and the same coset
            # (Cx is empty when x has no image under C)
            cos = {}
            for v in C2:
                key = frozenset(add(frozenset([v]), C1))
                img = frozenset(add(image(C, frozenset([v])) & C2, C1))
                cos.setdefault(key, set())
                if img:
                    cos[key].add(img)
            assert all(len(s) == 1 for s in cos.values())
            imgs = [next(iter(s)) for s in cos.values()]
            assert all(i in cos for i in imgs)       # each image a coset
            assert len(set(imgs)) == len(cos)
    check(True, 'Prop 4.3.5, Cor 4.3.6 (pp. 112-113): for each of the %d '
          'linear relations C on GF(2)^2, GF(2)^3, GF(3)^2: C\' <= C\'\', '
          'there are U, W with V = U + W, C = (C cap UxU) + (C cap WxW), '
          'C cap UxU the graph of an automorphism, C\' + U = C\'\' (direct), '
          'zero regular part on W, (C^-1)\' + U = (C^-1)\'\'; phi is a '
          'well defined permutation of C\'\'/C\' (x ranging over the '
          'elements of a coset with C x non-empty)' % total)
    # only S_1 has Ker a cap Ker b != 0 (from the Kronecker list)
    F = GF(3)
    ok = True
    for R, _, lab in kron_list(F, 3):
        a, b = R.maps
        K = dmatrix(F, [list(r) for r in a.rows()] + [list(r) for r in
                                                       b.rows()]) \
            if R.dims[1] else None
        dimK = R.dims[0] if K is None else R.dims[0] - K.rank()
        if (dimK > 0) != (R.dims == [1, 0]):
            ok = False
    check(ok, 'p. 112: among the indecomposable representations of the '
          'Kronecker quiver (dimensions <= 3, GF(3)) only S_1 has '
          'Ker(a) cap Ker(b) != 0')


def _butler():
    # the idempotents e_i of QV4
    signs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    els = [(0, 0), (1, 0), (0, 1), (1, 1)]

    def e(s):
        return [QQ(s[0] ** g[0] * s[1] ** g[1]) / 4 for g in els]

    def mulv(u, v):
        out = [QQ(0)] * 4
        for i, g in enumerate(els):
            for j, h in enumerate(els):
                k = els.index(((g[0] + h[0]) % 2, (g[1] + h[1]) % 2))
                out[k] += u[i] * v[j]
        return out
    es = [e(s) for s in signs]
    check(all(mulv(es[i], es[j]) == (es[j] if i == j else [0] * 4)
              for i in range(4) for j in range(4))
          and [sum(c) for c in zip(*es)] == [1, 0, 0, 0]
          and es[1] == [QQ(1) / 4, QQ(1) / 4, -QQ(1) / 4, -QQ(1) / 4],
          'p. 113: e_i e_j = delta_ij e_j, e_1 + ... + e_4 = 1, a typical '
          'one (1 + x - y - xy)/4')
    # reduced four subspace systems over GF(2) -> M -> back
    F = GF(2)
    systems = [
        (1, [[1], [1], [1], [1]]),
        (1, [[1], [1], [], []]),
        (1, [[1], [1], [1], []]),
        (2, [[1, 0], [0, 1], [1, 1], [1, 0]]),
        (2, [[1, 0], [0, 1], [1, 1], []]),
        (2, [[1, 0, 0, 1], [0, 1], [1, 1], [1, 0]]),
        (3, [[1, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 0, 1]]),
    ]
    for m, subs in systems:
        Vi = [dmatrix(F, len(s) // m, m, s) if s else dmatrix(F, 0, m, [])
              for s in subs]
        Vi = [A.row_space().basis_matrix() if A.nrows() else A for A in Vi]
        # reduced: V is the sum of any three
        for trip in itertools.combinations(range(4), 3):
            assert dmatrix(F, sum([list(Vi[i].rows()) for i in trip],
                                  [])).rank() == m
        dims = [A.nrows() for A in Vi]
        Ntot = sum(dims)
        # iota: GF(2)^Ntot -> V, block i by the basis of V_i
        iota = dmatrix(F, sum([list(A.rows()) for A in Vi], []))
        kerbar = iota.left_kernel().basis_matrix()
        Lgen = [list(map(ZZ, r)) for r in kerbar.rows()] + \
            [[2 if j == i else 0 for j in range(Ntot)] for i in range(Ntot)]
        Mlat = dmatrix(ZZ, Lgen).row_module()

        def block(i):
            st = sum(dims[:i])
            return list(range(st, st + dims[i]))

        def proj(vecs, i):
            bl = block(i)
            return [[v[j] if j in bl else 0 for j in range(Ntot)]
                    for v in vecs]
        Mb = Mlat.basis()
        # V4 acts by the sign characters on the blocks: M is a lattice
        ok = True
        for g in els[1:]:
            act = []
            for v in Mb:
                w = list(v)
                for i in range(4):
                    s = signs[i][0] ** g[0] * signs[i][1] ** g[1]
                    for j in block(i):
                        w[j] *= s
                act.append(w)
            if not all(vector(ZZ, w) in Mlat for w in act):
                ok = False
        eM = [dmatrix(ZZ, proj(Mb, i)).row_module() if dims[i] else None
              for i in range(4)]
        estar = dmatrix(ZZ, sum([proj(Mb, i) for i in range(4)], [])) \
            .row_module()

        def lg(index):
            return ZZ(index).exact_log(2)
        idxV = Mlat.index_in(estar)
        dV = lg(idxV)
        dVi = []
        for i in range(4):
            if dims[i] == 0:
                dVi.append(0)
                continue
            S = (eM[i] + Mlat)
            dVi.append(lg(Mlat.index_in(S)))
        ok = ok and dV == m and dVi == dims
        # e_* M = M + e_i M + e_j M + e_k M for any three
        for trip in itertools.combinations(range(4), 3):
            S = Mlat
            for i in trip:
                if dims[i]:
                    S = S + eM[i]
            if S != estar:
                ok = False
        # sums of pairs have the dimensions of V_i + V_j
        for i, j in itertools.combinations(range(4), 2):
            S = Mlat
            for k in (i, j):
                if dims[k]:
                    S = S + eM[k]
            want = dmatrix(F, list(Vi[i].rows()) + list(Vi[j].rows())) \
                .rank() if dims[i] + dims[j] else 0
            if lg(Mlat.index_in(S)) != want:
                ok = False
        check(ok, 'Butler (pp. 113-114): the RV4-lattice M of the reduced '
              'four subspace system (dim V = %d, dims %s) gives back '
              'e_*M/M = V, (e_i M + M)/M = V_i with the same sums, and '
              'e_*M = M + any three e_i M' % (m, dims))
    _four_subspace_systems()


def _four_subspace_systems():
    """Indecomposable four subspace systems with dim V <= 3 over GF(2): all
    reduced except five, all with dim V = 1 (p. 114)."""
    nonred = []
    total = 0
    for m in range(1, 4):
        def mul(A, B):
            out = []
            for i in range(m):
                r = 0
                for k in range(m):
                    if (A[i] >> k) & 1:
                        r ^= B[k]
                out.append(r)
            return tuple(out)

        def apply(A, v):          # row vector v (bitmask) times A
            r = 0
            for k in range(m):
                if (v >> k) & 1:
                    r ^= A[k]
            return r
        # all subspaces of GF(2)^m as frozensets of bitmasks
        vecs = list(range(1 << m))
        subs = set()
        for gens in itertools.chain.from_iterable(
                itertools.combinations(vecs[1:], k) for k in range(m + 1)):
            span = {0}
            for g in gens:
                span |= {s ^ g for s in span}
            subs.add(frozenset(span))
        subs = sorted(subs, key=lambda s: (len(s), sorted(s)))

        def basis_of(S):
            b, span = [], {0}
            for v in sorted(S):
                if v not in span:
                    b.append(v)
                    span |= {s ^ v for s in span}
            return b
        bases = {S: basis_of(S) for S in subs}
        allM = [tuple(r) for r in itertools.product(range(1 << m), repeat=m)]
        GL = [A for A in allM if len({apply(A, v) for v in vecs}) == 1 << m]
        seen = set()
        reps = []
        for tup in itertools.product(subs, repeat=4):
            if tup in seen:
                continue
            reps.append(tup)
            seen |= {tuple(frozenset(apply(A, v) for v in S) for S in tup)
                     for A in GL}
        for tup in reps:
            # End = matrices A with V_i A <= V_i; indecomposable iff the
            # only idempotents are 0 and 1
            nidem = 0
            for A in allM:
                if mul(A, A) == A and all(apply(A, v) in S for S in tup
                                          for v in bases[S]):
                    nidem += 1
            if nidem != 2:
                continue
            total += 1
            span3 = all(len(frozenset(a ^ b ^ c for a in tup[i]
                                      for b in tup[j] for c in tup[k]))
                        == 1 << m
                        for i, j, k in itertools.combinations(range(4), 3))
            if not span3:
                nonred.append((m, [len(S) for S in tup]))
    check(len(nonred) == 5 and all(m == 1 for m, _ in nonred),
          'p. 114: of the %d indecomposable four subspace systems with '
          'dim V <= 3 over GF(2), exactly five are not reduced (dim V = 1: '
          'all V_i = 0, or one V_i = V)' % total)


# ===========================================================================
# 4.4 and 4.7
# ===========================================================================


def section_4_4():
    # Theorem 4.4.4 (i): kC_(p^n) has p^n indecomposables (Jordan blocks):
    # the modules of dimension N are the conjugacy classes of X in GL_N(q)
    # with X^(p^n) = 1; they correspond to the partitions of N into parts
    # <= p^n
    from sage.all import Partitions
    for m, q, Nmax in ((2, 2, 4), (4, 2, 4), (3, 3, 4), (9, 3, 3)):
        for N in range(1, Nmax + 1):
            G = libgap.GL(N, q)
            cl = [c for c in G.ConjugacyClasses()
                  if (m % int(c.Representative().Order())) == 0]
            parts = Partitions(N, max_part=m).cardinality()
            check(len(cl) == parts,
                  'Thm 4.4.4 (i): GF(%d)C_%d has %d modules of dimension %d '
                  '(sums of the %d Jordan blocks)' % (q, m, parts, N, m))


GABRIEL_QUIVERS = [
    ('A1', 1, []),
    ('A2', 2, [(0, 1)]),
    ('A3 linear', 3, [(0, 1), (1, 2)]),
    ('A3 sink', 3, [(0, 1), (2, 1)]),
    ('A3 source', 3, [(1, 0), (1, 2)]),
    ('A4 linear', 4, [(0, 1), (1, 2), (2, 3)]),
    ('A4 alternating', 4, [(0, 1), (2, 1), (2, 3)]),
    ('A5 linear', 5, [(0, 1), (1, 2), (2, 3), (3, 4)]),
    ('D4 subspace', 4, [(1, 0), (2, 0), (3, 0)]),
    ('D4 mixed', 4, [(1, 0), (0, 2), (0, 3)]),
    ('D5', 5, [(0, 1), (4, 1), (1, 2), (2, 3)]),
    ('E6', 6, [(0, 1), (1, 2), (3, 2), (4, 3), (5, 2)]),
]


def underlying(n, arrows):
    return LGraph(n, [(s, t, 1, 1) for s, t in arrows])


def section_4_7():
    # Definition 4.7.2: admissible orderings exist iff no oriented cycle
    from sage.all import graphs
    tested = 0
    for n in (3, 4):
        for G in graphs(n):
            if not G.is_connected():
                continue
            E = G.edges(labels=False)
            for orient in itertools.product((0, 1), repeat=len(E)):
                arrows = [(x, y) if o == 0 else (y, x)
                          for (x, y), o in zip(E, orient)]
                exists = any(is_admissible(n, arrows, list(p))
                             for p in itertools.permutations(range(n)))
                assert exists == (not has_cycle(n, arrows))
                if exists:
                    o = admissible_ordering(n, arrows)
                    assert is_admissible(n, arrows, o)
                    cur = list(arrows)
                    for v in o:
                        cur = reflect_arrows(cur, v)
                    assert cur == arrows
                tested += 1
    check(True, 'Def 4.7.2: for all %d orientations of the connected graphs '
          'on 3 and 4 vertices, an admissible ordering exists iff there is '
          'no oriented cycle; then s_1 ... s_n Q = Q' % tested)

    # the corrected dimension display (p. 126) on a modulation of B_2:
    # Delta_x = GF(2), Delta_y = GF(4), _y M_x = GF(4), so _x d_y = 1,
    # _y d_x = 2, f_x = 1, f_y = 2; an arrow x -> y, y a sink
    F4 = GF(4, 'w')
    T = LGraph(2, [(0, 1, 1, 2)])          # x = 0, y = 1, (_x d_y, _y d_x)
    Ws = reflections(T)
    ok_c, ok_p = True, True
    for nx in range(0, 5):
        for ny in range(0, nx + 1):
            # a GF(4)-linear surjection GF(4) (x) GF(2)^nx = GF(4)^nx ->
            # GF(4)^ny; W_y = its kernel
            phi = dmatrix(F4, ny, nx, lambda i, j: 1 if i == j else 0)
            wy = nx - phi.rank()
            new = Ws[1] * vector(ZZ, [nx, ny])
            if not (wy == 1 * nx - ny and new[1] == wy and new[0] == nx):
                ok_c = False
            if wy != 2 * 1 * nx - ny:
                ok_p = False
    check(ok_c, 'p. 126 (corrected): dim_(Delta_y) W_y = sum _x d_y '
          'dim V_x - dim V_y = w_y on dimension vectors (GF(2), GF(4) '
          'modulation of B_2, all n_x <= 4, n_y <= n_x)')
    refuted(ok_p, 'p. 126 as printed: dim W_y = sum _y d_x f_x dim V_x - '
            'dim V_y')
    # k-dimensions on p. 125: GL_(Delta_x)(V_x) has dimension n_x^2 f_x,
    # Hom_(Delta_y)(_y M_x (x) V_x, V_y) has dimension n_x n_y _y d_x f_x
    check(all(2 * nx * ny == nx * ny * 2 * 1 and 2 * ny * ny == ny ** 2 * 2
              for nx in range(4) for ny in range(4)),
          'proof of Prop 4.7.1 (p. 125): Hom_GF(4)(GF(4)^nx, GF(4)^ny) has '
          'GF(2)-dimension nx ny _y d_x f_x = 2 nx ny; GL_ny(GF(4)) has '
          'dimension ny^2 f_y')

    # Theorem 4.7.6 (Gabriel) and the reflection functors
    results = []
    for name, n, arrows in GABRIEL_QUIVERS:
        T = underlying(n, arrows)
        Ws = reflections(T)
        Phi = roots(T)
        pos = sorted(v for v in Phi if is_positive(v))
        maxc = [max(v[x] for v in pos) for x in range(n)]
        fields = [GF(2)]
        if n <= 5:
            fields.append(GF(3))
        if name in ('A3 linear', 'A3 sink', 'D4 subspace', 'A2'):
            fields.append(GF(4, 'w'))
        for F in fields:
            q = F.order()
            order, reps = gabriel_indecomposables(n, arrows, F)
            check(is_admissible(n, arrows, order),
                  'Def 4.7.2: admissible ordering of %s' % name)
            dims = [tuple(R.dims) for _, _, R in reps]
            check(sorted(dims) == pos,
                  'Thm 4.7.6 (Gabriel), %s over GF(%d): the modules '
                  '(C^-)^(m-1) S_n^- ... S_(i+1)^- (S_i) of the proof have '
                  'the %d positive roots as dimension vectors, each once'
                  % (name, q, len(pos)))
            homcache = {}
            for k, (_, _, R) in enumerate(reps):
                homcache[k, k] = hom_dim(R, R)
            check(all(homcache[k, k] == 1 for k in range(len(reps))),
                  'Thm 4.7.6, %s over GF(%d): each is indecomposable '
                  '(End = k)' % (name, q))
            # their dimension vectors are c^(-m+1) w_n ... w_(i+1) (v_i)
            ok = True
            c = coxeter(Ws, order)
            for i, m, R in reps:
                v = vector(ZZ, [1 if x == order[i] else 0 for x in range(n)])
                for j in range(i + 1, n):
                    v = Ws[order[j]] * v
                v = (c.inverse() ** (m - 1)) * v
                if tuple(v) != tuple(R.dims):
                    ok = False
            check(ok, 'proof of Thm 4.7.6: the dimension vector is '
                  'c^(-m+1) w_n ... w_(i+1) (v_i) (%s, GF(%d))' % (name, q))
            # mass formula: completeness for all d in the box
            extra = 1 if (name.startswith('A') and n <= 4) or (
                name == 'D4 subspace' and q == 2) else 0
            box = [range(maxc[x] + 1 + extra) for x in range(n)]
            nd = 0
            rs = [R for _, _, R in reps]
            resid = [1] * len(rs)
            for d in itertools.product(*box):
                if sum(d) == 0:
                    continue
                tot, exp = mass_formula(rs, resid, q, d, homcache, arrows)
                assert tot == exp, ('mass formula', name, q, d)
                nd += 1
            check(True, 'Thm 4.7.6 (Gabriel), %s over GF(%d): for all %d '
                  'dimension vectors d <= %s the sums of these modules '
                  'satisfy sum 1/|Aut M| = q^(dim Rep d)/|GL(d)|: every '
                  'representation is such a sum' % (name, q, nd,
                                                    [r.stop - 1 for r in box]))
            results.append((name, q, len(pos), nd))
            if q != 2:
                continue
            # Proposition 4.7.3 and Lemma 4.7.5
            sinks = [y for y in range(n) if all(s != y for s, t in arrows)]
            ok = True
            for y in sinks:
                Sy = simple_rep(n, arrows, F, y)
                if not S_plus(Sy, y).is_zero():
                    ok = False
                for x in range(n):
                    if x != y and S_plus(simple_rep(n, arrows, F, x),
                                         y).is_zero():
                        ok = False
                for _, _, R in reps:
                    if R.dims == Sy.dims:
                        continue
                    W = S_plus(R, y)
                    if not (hom_dim(W, W) == 1 and tuple(W.dims) == tuple(
                            Ws[y] * vector(ZZ, R.dims))
                            and is_iso_rep(S_minus(W, y), R)):
                        ok = False
            check(ok and sinks, 'Prop 4.7.3 (corrected S_y) for %s: at each '
                  'sink y, S_y^+ kills S_y (and no other simple), sends '
                  'every other indecomposable V to an indecomposable with '
                  'dimension vector w_y(dim V), and S_y^- S_y^+ V = V' % name)
            ok = True
            for _, _, R in reps:
                W = C_plus(R, order)
                if W.is_zero():
                    continue
                if not (tuple(W.dims) == tuple(c * vector(ZZ, R.dims))
                        and is_iso_rep(C_minus(W, order), R)):
                    ok = False
            check(ok, 'Lemma 4.7.5 for %s: C^+ V = 0, or C^- C^+ V = V and '
                  'C^+ acts on dimension vectors as c = w_1 ... w_n' % name)
    # the root combinatorics of the proof for every finite Dynkin diagram:
    # for each positive root v the first non-positive vector in the
    # sequence w_i ... w_n c^(m-1)(v) comes from w_(i+1) ... w_n c^(m-1)(v)
    # = v_i (Lemma 4.6.8 (iii))
    for T in dynkin_list(8):
        Ws = reflections(T)
        order = list(range(T.n))
        ok = True
        Phi = roots(T)
        for v in Phi:
            if not is_positive(v):
                continue
            w = vector(ZZ, v)
            done = False
            for m in range(1, 40):
                for i in range(T.n - 1, -1, -1):
                    u = Ws[order[i]] * w
                    if not is_positive(u):
                        if tuple(w) != tuple(1 if x == order[i] else 0
                                             for x in range(T.n)):
                            ok = False
                        done = True
                        break
                    w = u
                if done:
                    break
            if not done:
                ok = False
        check(ok, 'proof of Thm 4.7.6 (converse): every positive root of %s '
              'is c^(-m+1) w_n ... w_(i+1)(v_i) (reflections in the order '
              'x_1..x_n)' % T.name)
    _euclidean_counts()
    return results


def _euclidean_counts():
    """Proposition 4.7.1: D~4 (four subspace quiver) has q + 4
    indecomposables of dimension vector (2; 1, 1, 1, 1) over GF(q)."""
    for q in (2, 3):
        F = GF(q)
        V2 = [tuple(v) for v in (F ** 2)]
        pts = list(itertools.product(V2, repeat=4))
        units = [c for c in F if c != 0]

        def act(g, cs, P):
            gs = g.sparse_matrix() if q % 2 else g
            return tuple(tuple(cs[i] * (gs * vector(F, P[i])))
                         for i in range(4))
        gens = [dmatrix(F, [[1, 1], [0, 1]]), dmatrix(F, [[0, 1], [1, 0]])]
        if q == 3:
            gens.append(dmatrix(F, [[2, 0], [0, 1]]))
        seen = set()
        orbits = []
        for P in pts:
            if P in seen:
                continue
            orb = {P}
            todo = [P]
            while todo:
                Q = todo.pop()
                for g in gens:
                    R = act(g, [F(1)] * 4, Q)
                    if R not in orb:
                        orb.add(R)
                        todo.append(R)
                for i in range(4):
                    for u in units:
                        cs = [F(1)] * 4
                        cs[i] = u
                        R = act(dmatrix(F, [[1, 0], [0, 1]]), cs, Q)
                        if R not in orb:
                            orb.add(R)
                            todo.append(R)
            seen |= orb
            orbits.append(P)
        arrows = [(1, 0), (2, 0), (3, 0), (4, 0)]
        nind = 0
        for P in orbits:
            R = QRep(5, arrows, F, [2, 1, 1, 1, 1],
                     [dmatrix(F, 2, 1, list(P[i])) for i in range(4)])
            if _is_indecomposable_rep(R):
                nind += 1
        check(nind == q + 4,
              'Prop 4.7.1: the four subspace quiver D~4 has q + 4 = %d '
              'indecomposables of dimension vector (2; 1, 1, 1, 1) over '
              'GF(%d) (%d orbits): their number grows with q'
              % (q + 4, q, len(orbits)))


def _is_indecomposable_rep(R):
    """End(R) local: no idempotents but 0, 1 (by enumeration)."""
    B = hom_basis(R, R)
    F = R.F
    if len(B) == 1:
        return True
    cnt = 0
    for coeffs in itertools.product(F, repeat=len(B)):
        f = [sum((c * b[x] for c, b in zip(coeffs, B)), 0 * B[0][x])
             for x in range(R.n)]
        fs = [sp(m) for m in f]
        if all(fs[x] * fs[x] == fs[x] for x in range(R.n)):
            cnt += 1
    return cnt == 2


def main():
    section_4_5_and_4_6()
    section_4_1_and_4_2()
    section_4_3()
    section_4_4()
    section_4_7()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
