"""Exact checks of Chapter 1 "Background material from rings and modules" (Sage).

Run: sage -python checks/sage/chapter-1.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-1: N checks".

Book: D. J. Benson, Representations and Cohomology I, second edition,
Cambridge Studies in Advanced Mathematics 30 (1998), printed pp. 1-19, with
the author's "Comments and corrections" (8 September 2010).  Pages are the
printed pages; labels are those of content/01-*.typ.

Chapter 1 is general theory and prints almost no numbers.  Its statements
are checked on concrete algebras: group algebras over finite fields (S3,
A4, S4, A5, D8, Q8, V4, cyclic groups; over F2, F3, F4, F5, F9), the
triangular algebras T2 (over F3; the path algebra of 1 -> 2) and T3 (over
F2), the Nakayama algebra N (cyclic quiver with two vertices, paths of
length 2 zero; over F2, F3), the self-injective algebra QF = e Mat_3(N) e
(e = diag(e1, e1, e2), over F2) which is not Frobenius, group algebras over
Q, group rings over Z/p^k, and number fields.  The expected values are
what the statements predict; the module-theoretic data are computed
independently with the MeatAxe of GAP (libgap): Rad(M) as the intersection
of the kernels of all homomorphisms to simple modules (= of the maximal
submodules), Soc(M) as the sum of the simple submodules (MTX.BasisSocle),
composition factors, homomorphism spaces, isomorphism tests,
decompositions.  The printed readings that are wrong are kept as refuted
checks (`refuted`) beside the corrected ones: Proposition 1.2.5 without
its hypothesis (Z, Z/4: the author's counterexample), the claim that every
annihilator of a module is primitive, and the last sentence of the proof
of Theorem 1.7.3 before the author's correction.

What is checked, by section:

section_1_1 (pp. 1-3): lem:modular-law on all triples of subspaces of F2^3
  and F2^4; th:zassenhaus on all quadruples V <= U, V' <= U' in F2^3 (the
  three quotients, the kernel identity and the surjectivity of the
  proof); th:jordan-holder: all composition series of the regular F3S3-,
  F2V4- and F2C4-modules have the same factors; uniserial modules (F2C4,
  the PIMs of F3S3: one composition series, a chain of submodules); the
  Exercise on distributive submodule lattices (distributive iff no
  subquotient S + S) on nine modules.
section_1_2 (pp. 3-5): def:socle-radical, last paragraph as corrected (M
  of finite length: socle length = radical length = n, Rad^(n-j) M <=
  Soc^j M) and second paragraph (completely reducible iff Rad M = 0) on the
  PIMs, simples, regular module, Rad P and P/Soc P of 16 algebras; the
  paragraph after it: Lambda/ann(S) = End_Delta(S) for every simple S (so
  ann(S) is primitive), the printed "every annihilator is primitive"
  refuted by the regular module of six algebras, J = intersection of the
  ann(S); J two-sided, nilpotent (th:artinian-ring (i)), dim Lambda/J =
  sum n_i^2 dim Delta_i for 16 algebras; J = intersection of the maximal
  left ideals = of the maximal right ideals = {x : 1 - axb is a unit for
  all a, b}, exhaustively for F2S3, F2V4, F2C4, T3, N (F2), M2(F2), and
  J = {x : 1 - ax a unit for all a} for F3S3 (lem:radical-unit);
  prop:radical-of-module: the printed form refuted (Z, Z/4), the author's
  form checked on all 72 modules Z/d1 + Z/d2 + Z/d3 of order <= 64 over
  Z/8, Z/9, Z/12, Z/16; prop:surjective-mod-radical-square over all
  subrings of F3S3, F2C4, F2V4, F3C3, T3 (and J in place of J^2 fails
  for each).
section_1_3 (pp. 5-7): th:wedderburn-artin, th:semisimple-endomorphisms:
  QS3 = Q + Q + Mat_2(Q), QC3 = Q + Q(zeta_3), QQ8 = Q^4 + (-1,-1)_Q
  (central idempotents from the factorization of the minimal polynomial
  of a generator of the centre; the quaternion component is a division
  ring, split by Q(i): Exercise); F2C3, F2C7, F3Q8, F5S3, F4C3: J = 0, the
  Delta_i, n_i = dim_(Delta_i^op) S_i, dim = sum n_i^2 dim Delta_i, every
  Delta_i commutative (Remarks (i), (ii)); End(S + S + T) =
  Mat_2(Delta_S) + Delta_T semisimple (F3S3, F2A4); lem:idempotent-hom
  (i), (ii) for all e_i of 1 = sum e_i in F3S3, F4A4, F2A4, N, T2, QF;
  prop:skolem-noether: all automorphisms of M2(Fq), q = 2, 3, 5, are inner
  (exhaustive).
section_1_4 (pp. 7-9): lem:fitting for every endomorphism of the regular
  modules of F3S3, F2V4, N, T3, F2A4; lem:indecomposable-local and
  def:local-ring: End(P) = e Lambda e is local with quotient Delta, for
  all PIMs of eight algebras; th:krull-schmidt: two decompositions of the
  regular modules of F3S4, F2A4, F4A5, QF agree, n_i = dim_(Delta^op) S_i;
  the Exercise: for O = Z[sqrt(-5)] (class number 2) I + I = O + O with
  I = (2, 1 + sqrt(-5)) not principal, and class numbers of 14 imaginary
  quadratic fields.
section_1_5 (pp. 9-11): the projective cover of k for F3S3, and
  lem:schanuel for F3S3 (P_k -> k, F3S3 -> k) and F2V4 (L -> k, L + L -> k).
section_1_6 (pp. 11-12): def:frobenius-symmetric: twelve group algebras
  are symmetric (the Remark), and for F2S3 Ker(lam) contains no nonzero
  one-sided ideal (all ideals); prop:frobenius-self-injective (i) for F3S3,
  F4A4, N; th:symmetric-socle on all 25 PIMs of 12 group algebras; N is
  Frobenius but not symmetric and Soc P is not P/Rad P; T2 is neither
  Frobenius nor self-injective; QF is self-injective and not Frobenius
  (Gram determinant zero identically); Exercises 2, 3 on nine algebras;
  Exercise 4 for Mat_2(F2V4), Mat_2(F3S3).
section_1_7 (pp. 12-15): th:idempotent-refinement: the displayed identity
  in Z[a], the a^p variant (p <= 13), the lifting step on all elements of
  F3S3 and F2A4 idempotent modulo J, all idempotents of F3S3 lifted to
  (Z/27)S3, and the conjugacy part in the author's corrected form on all
  pairs e1, g e1 g^-1 != e1 in (Z/27)S3 (the printed "1 - nu = f2 mu +
  mu f1 - 2 f2 mu f1 in N" refuted); prop:conjugate-idempotents
  exhaustively for F2S3, F3S3, F2A4; cor:idempotent-refinement: F3S4 ->
  (Z/27)S4, F2A4 -> (Z/8)A4; lem:hom-projective-simple,
  lem:multiplicity-projective, lem:multiplicity-injective (I_S the dual of
  a right PIM) on the modules of eight algebras; th:landrock for all S,
  T, n on 13 algebras over splitting fields; def:cartan-matrix (c_ij =
  dim_(Delta_i) Hom(P_i, P_j) = [P_j : S_i] on 12 algebras, = dim e_i L e_j
  for F3S3), symmetric for group algebras over splitting fields,
  non-singular with determinant a power of p for group algebras (as the
  text announces), F2A4 over F2: [[2, 2], [1, 3]], N and QF: singular,
  T2: not symmetric; lem:rosenberg exhaustively (pairs and triples of
  two-sided ideals) for F2S3, F3S3, T3, N, F2V4, and its failure without
  e Lambda e local.
section_1_8 (pp. 15-17): lem:block-decomposition-unique for 18 algebras
  (2^s central idempotents, s the number of blocks; s against GAP's
  PrimeBlocks for 12 of them; A5 at p = 3: two blocks over F3, three over
  F9), modules and the composition factors of PIMs in one block;
  prop:central-idempotents-lift with I = J^2 for eight algebras (the lifts
  are central), I = J fails for F3S3; prop:simple-projective-injective
  (the block is Mat_n(Delta), n^2 dim Delta, the only simple module) for
  the simple projective-injective modules of eight algebras, and for T2
  a simple projective non-injective module shares its block; the Exercise
  for Z/n (n <= 400) and 16 rings F_p[x]/(f).
section_1_9 (pp. 17-19): the introduction (only 8 of the 16 idempotents
  of F5C4 lift to Z_(5)C4, all 16 lift to Z_5 C4 as Teichmueller sums,
  mod 5^10); lem:lattice-form and Remark (iii) (two Z-forms of the
  2-dimensional representation of S3 with non-isomorphic reductions mod 3
  and the same composition factors); th:idempotent-refinement-p-adic (i)
  (compatible lifts of the idempotents of F3S3 to Z/3^8), (ii) (F3S4 ->
  Z/3^6), (iii) as corrected by the author (every idempotent lift of a
  primitive central idempotent is central, the lifts agree and are the
  block idempotents: S3 mod 2^12, A5 mod 2^8, S4 mod 3^6, A5 mod 5^5; the
  class sums span Z(kG), so the dropped hypothesis holds for group
  algebras; an order with Z(L) -> Z(L/pL) not onto); prop:decomposition-
  numbers: C = D^T D with D from the reductions of integral forms
  (Definition 1.9.5) for S3, S4 (p = 2, 3) and A4 (p = 2 over F4, p = 3),
  D against GAP's Brauer tables, and C = D^T D for A5 (p = 2, 3, 5) with
  GAP's D; Remark (iv) (T2); Remark (v) with the author's dim_K
  (Z_3 C3 and Z_2 A4: multiplicities in the lifts and c_ij).

What these checks do NOT establish.  Each check is an exact computation
for the listed algebras, modules, rings and parameters (exhaustive where
so stated) or a polynomial identity in the written variables; none proves
a general theorem of Chapter 1.  The general steps formalized in Lean are
recorded with their limits in checks/lean-proofs.json.  The p-adic
statements are checked modulo p^k for the stated k, with Q_p replaced by
character computations where noted.  The counterexample to the printed
last paragraph of Definition 1.2.1 (the ring of eventually constant
sequences) is infinite and is argued in a comment.  The Exercises of
Section 1.2, the Exercises of Sections 1.5 (Broue) and 1.6 (Exercise 1),
Lemmas 1.5.2, 1.5.4, 1.9.2, Theorem 1.9.3 and the Eckmann-Schoepf theorem are not
checked, nor is the infinite-dimensional case of Proposition 1.3.6.
Nothing here compares our text with the printed book.
"""
import itertools
import random

from sage.all import (
    GF, QQ, ZZ, Integer, Partitions, Permutation, PolynomialRing,
    QuadraticField, QuaternionAlgebra, SymmetricGroupRepresentation, Zp, Qp,
    block_matrix, divisors, factor, identity_matrix, libgap, matrix,
    prod, set_random_seed, vector, zero_matrix,
)

COUNT = [0]


def check(condition, label):
    """The book's statement (or our corrected reading) holds."""
    assert bool(condition), label
    COUNT[0] += 1


def refuted(condition, label):
    """The printed reading must fail: it is kept as a refuted check."""
    assert not bool(condition), 'printed reading unexpectedly holds: ' + label
    COUNT[0] += 1


random.seed(20261104)
set_random_seed(20261104)

# ---------------------------------------------------------------------------
# GAP (MeatAxe) helpers.  MeatAxe modules are row modules: an element x acts
# on row vectors by v -> v m(x), and m(xy) = m(y) m(x).

GAPF = libgap.eval(r'''rec(
  radical := function(M, simples)
    local d, F, K, S, h, N;
    d := MTX.Dimension(M); F := MTX.Field(M);
    if d = 0 then return []; fi;
    K := IdentityMat(d, F);
    for S in simples do
      for h in MTX.BasisModuleHomomorphisms(M, S) do
        N := NullspaceMat(h);
        if Length(N) = 0 then return []; fi;
        K := SumIntersectionMat(K, N)[2];
        if Length(K) = 0 then return []; fi;
      od;
    od;
    return SemiEchelonMat(K).vectors;
  end,
  radseries := function(M, simples, radical)
    local d, F, B, series, cur, rb;
    d := MTX.Dimension(M); F := MTX.Field(M);
    B := IdentityMat(d, F); series := [B]; cur := M;
    while Length(B) > 0 do
      rb := radical(cur, simples);
      if Length(rb) = 0 then B := [];
      else
        B := SemiEchelonMat(rb * B).vectors;
        cur := MTX.InducedActionSubmodule(M, B);
      fi;
      Add(series, B);
    od;
    return series;
  end,
  socseries := function(M)
    local d, F, S, series, ia, cur, comp, sb;
    d := MTX.Dimension(M); F := MTX.Field(M);
    S := []; series := [[]];
    while Length(S) < d do
      if Length(S) = 0 then cur := M; comp := IdentityMat(d, F);
      else
        ia := MTX.InducedAction(M, S);
        if RankMat(Concatenation(ia[4]{[1..Length(S)]}, S)) <> Length(S) then
          Error("unexpected basis change");
        fi;
        cur := ia[2]; comp := ia[4]{[Length(S)+1..d]};
      fi;
      sb := MTX.BasisSocle(cur);
      S := SemiEchelonMat(Concatenation(S, sb * comp)).vectors;
      Add(series, S);
    od;
    return series;
  end,
  sub := function(M, A)
    if Length(A) = 0 then
      return GModuleByMats(List(MTX.Generators(M), g -> NullMat(0, 0)), 0,
                           MTX.Field(M));
    fi;
    return MTX.InducedActionSubmodule(M, SemiEchelonMat(A).vectors);
  end,
  quot := function(M, A, B)
    local sub, Ae, coords;
    if Length(A) = Length(B) then
      return GModuleByMats(List(MTX.Generators(M), g -> NullMat(0, 0)), 0,
                           MTX.Field(M));
    fi;
    Ae := SemiEchelonMat(A).vectors;
    sub := MTX.InducedActionSubmodule(M, Ae);
    if Length(B) = 0 then return sub; fi;
    coords := SemiEchelonMat(List(B, v -> SolutionMat(Ae, v))).vectors;
    return MTX.InducedActionFactorModule(sub, coords);
  end,
  mult := function(q, simples)
    local res, c, i;
    res := List(simples, s -> 0);
    if MTX.Dimension(q) = 0 then return res; fi;
    for c in MTX.CompositionFactors(q) do
      i := PositionProperty(simples, s -> MTX.Dimension(s) = MTX.Dimension(c)
             and MTX.IsomorphismModules(s, c) <> fail);
      res[i] := res[i] + 1;
    od;
    return res;
  end,
  iso := function(A, B)
    if MTX.Dimension(A) <> MTX.Dimension(B) then return false; fi;
    if MTX.Dimension(A) = 0 then return true; fi;
    return MTX.IsomorphismModules(A, B) <> fail;
  end,
  homdim := function(A, B)
    if MTX.Dimension(A) = 0 or MTX.Dimension(B) = 0 then return 0; fi;
    return Length(MTX.BasisModuleHomomorphisms(A, B));
  end,
  dsum := function(A, B)
    return GModuleByMats(List([1..Length(MTX.Generators(A))], i ->
      DirectSumMat(MTX.Generators(A)[i], MTX.Generators(B)[i])), MTX.Field(A));
  end,
  dual := function(A)
    return GModuleByMats(List(MTX.Generators(A), TransposedMat), MTX.Field(A));
  end,
  dims := function(L) return List(L, Length); end
)''')


def mtx(name):
    return libgap.eval('MTX.' + name)


MDIM = mtx('Dimension')


def mdim(M):
    return int(MDIM(M))


def mm(A, B):
    """A * B.  Over prime fields of odd characteristic the product goes
    through sparse matrices: on some machines the BLAS kernel used by Sage
    for dense GF(p) products raises an illegal instruction."""
    F = A.base_ring()
    if F.characteristic() != 2 and F.is_prime_field():
        return (A.sparse_matrix() * B.sparse_matrix()).dense_matrix()
    return A * B


def mpow(A, k):
    R = identity_matrix(A.base_ring(), A.nrows())
    for _ in range(k):
        R = mm(R, A)
    return R


def subspace_matrices(F, m):
    """The reduced echelon matrices of all subspaces of F^m."""
    elems = list(F)
    for k in range(m + 1):
        for piv in itertools.combinations(range(m), k):
            free = [(r, j) for r in range(k) for j in range(piv[r] + 1, m)
                    if j not in piv]
            for vals in itertools.product(elems, repeat=len(free)):
                M = matrix(F, k, m)
                for r in range(k):
                    M[r, piv[r]] = 1
                for (r, j), a in zip(free, vals):
                    M[r, j] = a
                yield M


def rad(M, simples):
    """Rad(M): the intersection of the kernels of all homomorphisms to
    simple modules (= of the maximal submodules)."""
    return GAPF['radical'](M, simples)


def radseries(M, simples):
    return GAPF['radseries'](M, simples, GAPF['radical'])


def gmod(mats, F):
    return libgap.GModuleByMats([libgap(m) for m in mats], libgap(F))


def to_sage(B, F, n):
    rows = list(B)
    if len(rows) == 0:
        return matrix(F, 0, n)
    return matrix(F, B.sage(ring=F))


def to_gap(S):
    """A Sage subspace (or matrix of rows) as a GAP list of row vectors."""
    M = S.basis_matrix() if hasattr(S, 'basis_matrix') else S
    if M.nrows() == 0:
        return libgap([])
    return libgap(M)


def ilist(L):
    return [int(a) for a in L]


# ---------------------------------------------------------------------------
# Finite-dimensional algebras by left multiplication matrices.


class Alg:
    """A unital algebra over F with basis b_0..b_(d-1); L[i] is the matrix
    of y -> b_i y (column convention).  gens generate it as an algebra."""

    def __init__(self, F, L, one, gens, name):
        self.F = F
        self.L = [matrix(F, m) for m in L]
        self.d = len(self.L)
        self.one = vector(F, one)
        self.gens = [vector(F, g) for g in gens]
        self.name = name
        self.V = F ** self.d
        self.cache = {}
        self.is_group = False

    def e(self, i):
        v = vector(self.F, self.d)
        v[i] = 1
        return v

    def lmat(self, x):
        M = matrix(self.F, self.d, self.d)
        for i in range(self.d):
            if x[i] != 0:
                M += x[i] * self.L[i]
        return M

    def mul(self, x, y):
        if self.is_group:
            z = [self.F(0)] * self.d
            nx = [(i, a) for i, a in enumerate(x) if a != 0]
            ny = [(j, b) for j, b in enumerate(y) if b != 0]
            for i, a in nx:
                row = self.mt[i]
                for j, b in ny:
                    z[row[j]] += a * b
            return vector(self.F, z)
        return self.lmat(x) * y

    def rmat(self, x):
        return matrix(self.F, [self.L[j] * x for j in range(self.d)]).transpose()

    def opposite(self):
        B = Alg(self.F, [self.rmat(self.e(i)) for i in range(self.d)],
                self.one, self.gens, self.name + '^op')
        return B

    def module_mats(self, xs):
        return [self.lmat(x).transpose() for x in xs]

    def regular(self):
        if 'reg' not in self.cache:
            self.cache['reg'] = gmod(self.module_mats(self.gens), self.F)
        return self.cache['reg']

    def submodule(self, S):
        """The left ideal S (a subspace) as a MeatAxe module."""
        return GAPF['sub'](self.regular(), to_gap(S))

    def center(self):
        K = block_matrix([[self.lmat(g) - self.rmat(g)] for g in self.gens],
                         subdivide=False)
        return K.right_kernel()

    def span_mul(self, X, Y):
        return self.V.subspace([self.mul(x, y) for x in X.basis()
                                for y in Y.basis()])

    def is_left_ideal(self, S):
        return all(self.mul(g, v) in S for g in self.gens for v in S.basis())

    def is_right_ideal(self, S):
        return all(self.mul(v, g) in S for g in self.gens for v in S.basis())

    def allmats(self, M):
        """Row-convention matrices of all basis elements on the module M."""
        gm = [matrix(self.F, g.sage(ring=self.F)) if mdim(M) > 0 else
              matrix(self.F, 0, 0) for g in mtx('Generators')(M)]
        n = mdim(M)
        if self.is_group:
            mats = [None] * self.d
            mats[self.id] = identity_matrix(self.F, n)
            queue = [self.id]
            while queue:
                h = queue.pop(0)
                for s, gi in enumerate(self.gen_idx):
                    k = self.mt[gi][h]
                    if mats[k] is None:
                        mats[k] = mm(mats[h], gm[s])
                        queue.append(k)
            return mats
        assert len(gm) == self.d
        return gm

    def act(self, mats, x):
        n = mats[0].nrows()
        M = matrix(self.F, n, n)
        for i in range(self.d):
            if x[i] != 0:
                M += x[i] * mats[i]
        return M

    # -- the radical, simple modules and PIMs -----------------------------
    def data(self):
        """Simple modules, PIMs (as left ideals with their tops), J."""
        if 'data' in self.cache:
            return self.cache['data']
        R = self.regular()
        cf = mtx('CollectedFactors')(R)
        simples = [c[0] for c in cf]
        mults = [int(c[1]) for c in cf]
        J = to_sage(rad(R, simples), self.F, self.d).row_space()
        dec = mtx('Indecomposition')(R)
        pims = []
        for pair in dec:
            S = to_sage(pair[0], self.F, self.d).row_space()
            P = self.submodule(S)
            top = GAPF['quot'](P, libgap.IdentityMat(mdim(P), libgap(self.F)),
                               rad(P, simples))
            t = [i for i, s in enumerate(simples) if GAPF['iso'](s, top)]
            assert len(t) == 1
            pims.append((S, P, t[0]))
        ends = [len(list(mtx('BasisModuleEndomorphisms')(s))) for s in simples]
        D = dict(simples=simples, mults=mults, J=J, pims=pims, ends=ends)
        # one PIM of each type, indexed by its top
        rep = {}
        for S, P, t in pims:
            rep.setdefault(t, (S, P))
        D['P'] = [rep[i][1] for i in range(len(simples))]
        D['Pspace'] = [rep[i][0] for i in range(len(simples))]
        self.cache['data'] = D
        return D

    def idempotents_from_pims(self):
        """1 = sum e_i with Lambda e_i the summands of the decomposition."""
        D = self.data()
        B = block_matrix([[S.basis_matrix()] for S, P, t in D['pims']],
                         subdivide=False)
        c = B.solve_left(self.one)
        es, k = [], 0
        for S, P, t in D['pims']:
            m = S.dimension()
            es.append(c[k:k + m] * S.basis_matrix())
            k += m
        return es

    def cartan(self):
        D = self.data()
        r = len(D['simples'])
        C = matrix(ZZ, r, r)
        for j in range(r):
            m = ilist(GAPF['mult'](D['P'][j], D['simples']))
            for i in range(r):
                C[i, j] = m[i]
        return C

    def elements(self, S=None):
        S = self.V if S is None else S
        return list(S)

    def quotient(self, I):
        """The algebra Lambda/I for a two-sided ideal I; B.proj maps L to
        L/I (coordinates on the non-pivot columns of I), B.proj.lift back."""
        proj = Projection(self.F, self.d, I)
        m = len(proj.free)
        lifts = [proj.lift(vector(self.F, [int(a == b) for b in range(m)]))
                 for a in range(m)]
        L = [matrix(self.F, [proj(self.mul(lifts[i], lifts[j]))
                             for j in range(m)]).transpose() for i in range(m)]
        B = Alg(self.F, L, proj(self.one), [proj(g) for g in self.gens],
                self.name + '/I')
        B.proj = proj
        return B


class Projection:
    """F^d -> F^d / I, by reduction modulo the reduced echelon basis of I."""

    def __init__(self, F, d, I):
        self.F, self.d = F, d
        self.E = I.echelonized_basis_matrix()
        self.piv = list(self.E.pivots())
        self.free = [j for j in range(d) if j not in self.piv]

    def __call__(self, v):
        v = vector(self.F, v)
        for r, p in enumerate(self.piv):
            if v[p] != 0:
                v = v - v[p] * self.E.row(r)
        return vector(self.F, [v[j] for j in self.free])

    def lift(self, q):
        v = vector(self.F, self.d)
        for a, j in zip(q, self.free):
            v[j] = a
        return v


def group_algebra(G, F, name):
    els = list(G.AsSSortedList())
    n = len(els)
    deg = max(int(libgap.LargestMovedPoint(G)), 1)
    tup = [tuple(int(a) for a in libgap.ListPerm(g, deg)) for g in els]
    idx = {t: i for i, t in enumerate(tup)}

    def pmul(a, b):  # GAP: i^(ab) = (i^a)^b
        return tuple(b[a[i] - 1] for i in range(deg))
    mt = [[idx[pmul(tup[i], tup[j])] for j in range(n)] for i in range(n)]
    L = []
    for i in range(n):
        M = matrix(F, n, n)
        for j in range(n):
            M[mt[i][j], j] = 1
        L.append(M)
    ident = idx[tuple(range(1, deg + 1))]
    gen_idx = [idx[tuple(int(a) for a in libgap.ListPerm(g, deg))]
               for g in G.GeneratorsOfGroup()]
    one = [0] * n
    one[ident] = 1
    gens = []
    for gi in gen_idx:
        v = [0] * n
        v[gi] = 1
        gens.append(v)
    A = Alg(F, L, one, gens, name)
    A.is_group = True
    A.els, A.mt, A.tup, A.idx, A.group, A.id = els, mt, tup, idx, G, ident
    A.gen_idx = gen_idx
    A.inv = [mt[i].index(ident) for i in range(n)]
    A.deg = deg
    return A


def struct_algebra(F, d, table, one, name):
    """Algebra with basis 0..d-1 and products table[(i, j)] = {k: c}."""
    L = []
    for i in range(d):
        M = matrix(F, d, d)
        for j in range(d):
            for k, c in table.get((i, j), {}).items():
                M[k, j] += c
        L.append(M)
    gens = [[int(a == b) for b in range(d)] for a in range(d)]
    return Alg(F, L, one, gens, name)


def matrix_algebra(F, basis, one_mat, name):
    basis = [matrix(F, b) for b in basis]
    d = len(basis)
    B = matrix(F, [b.list() for b in basis])
    assert B.rank() == d

    def coords(M):
        return B.solve_left(vector(F, matrix(F, M).list()))
    L = [matrix(F, [coords(mm(basis[i], basis[j])) for j in range(d)]).transpose()
         for i in range(d)]
    gens = [[int(a == b) for b in range(d)] for a in range(d)]
    A = Alg(F, L, coords(one_mat), gens, name)
    A.basis_mats = basis
    A.coords = coords
    return A


def nakayama(F):
    """The cyclic quiver 1 -> 2 -> 1 (arrows a in e2 L e1, b in e1 L e2)
    with all paths of length 2 zero; basis e1, e2, a, b."""
    t = {(0, 0): {0: 1}, (1, 1): {1: 1}, (1, 2): {2: 1}, (2, 0): {2: 1},
         (0, 3): {3: 1}, (3, 1): {3: 1}}
    return struct_algebra(F, 4, t, [1, 1, 0, 0], 'N')


def triangular(F, n):
    basis = []
    for i in range(n):
        for j in range(i, n):
            M = matrix(F, n, n)
            M[i, j] = 1
            basis.append(M)
    return matrix_algebra(F, basis, identity_matrix(F, n), 'T%d' % n)


def qf_not_frobenius(F):
    """e Mat_3(N) e with e = diag(e1, e1, e2): self-injective, Morita
    equivalent to the Nakayama algebra N, with simple modules of
    dimensions 2 and 1."""
    N = nakayama(F)
    reg = [N.L[i] for i in range(4)]       # x -> L_x is an embedding of N
    pos = [0, 0, 1]                        # e1, e1, e2
    corner = {(0, 0): 0, (1, 1): 1, (1, 0): 2, (0, 1): 3}  # e_i N e_j
    basis = []
    for r in range(3):
        for s in range(3):
            E = matrix(F, 3, 3)
            E[r, s] = 1
            basis.append(E.tensor_product(reg[corner[(pos[r], pos[s])]]))
    one = sum((matrix(F, 3, 3, {(r, r): 1}).tensor_product(reg[pos[r]])
               for r in range(3)), matrix(F, 12, 12))
    return matrix_algebra(F, basis, one, 'QF')


def product_algebra(A, B):
    d = A.d + B.d
    L = [block_matrix([[A.L[i], zero_matrix(A.F, A.d, B.d)],
                       [zero_matrix(A.F, B.d, A.d), zero_matrix(A.F, B.d, B.d)]],
                      subdivide=False) for i in range(A.d)]
    L += [block_matrix([[zero_matrix(A.F, A.d, A.d), zero_matrix(A.F, A.d, B.d)],
                        [zero_matrix(A.F, B.d, A.d), B.L[i]]], subdivide=False)
          for i in range(B.d)]
    gens = [[int(a == b) for b in range(d)] for a in range(d)]
    one = list(A.one) + list(B.one)
    return Alg(A.F, L, one, gens, A.name + 'x' + B.name)


# ---------------------------------------------------------------------------
# The algebras.

S3 = libgap.SymmetricGroup(3)
A4 = libgap.AlternatingGroup(4)
S4 = libgap.SymmetricGroup(4)
A5 = libgap.AlternatingGroup(5)
V4 = libgap.Group(libgap.eval('(1,2)'), libgap.eval('(3,4)'))
C4 = libgap.CyclicGroup(libgap.IsPermGroup, 4)
C3 = libgap.CyclicGroup(libgap.IsPermGroup, 3)
C7 = libgap.CyclicGroup(libgap.IsPermGroup, 7)
D8 = libgap.DihedralGroup(libgap.IsPermGroup, 8)
Q8 = libgap.Image(libgap.IsomorphismPermGroup(libgap.QuaternionGroup(8)))
F4 = GF(4, 'z')
F9 = GF(9, 'w')

ALG = {}


def alg(key):
    if key not in ALG:
        G, F, name = {
            'F2S3': (S3, GF(2), 'F2S3'), 'F3S3': (S3, GF(3), 'F3S3'),
            'F2A4': (A4, GF(2), 'F2A4'), 'F4A4': (A4, F4, 'F4A4'),
            'F3A4': (A4, GF(3), 'F3A4'), 'F2S4': (S4, GF(2), 'F2S4'),
            'F3S4': (S4, GF(3), 'F3S4'), 'F4A5': (A5, F4, 'F4A5'),
            'F2A5': (A5, GF(2), 'F2A5'), 'F3A5': (A5, GF(3), 'F3A5'),
            'F9A5': (A5, F9, 'F9A5'), 'F5A5': (A5, GF(5), 'F5A5'),
            'F2V4': (V4, GF(2), 'F2V4'), 'F2C4': (C4, GF(2), 'F2C4'),
            'F3C3': (C3, GF(3), 'F3C3'), 'F2D8': (D8, GF(2), 'F2D8'),
            'F2Q8': (Q8, GF(2), 'F2Q8'), 'F2C3': (C3, GF(2), 'F2C3'),
            'F2C7': (C7, GF(2), 'F2C7'), 'F3Q8': (Q8, GF(3), 'F3Q8'),
            'F5S3': (S3, GF(5), 'F5S3'), 'F4C3': (C3, F4, 'F4C3'),
        }[key]
        ALG[key] = group_algebra(G, F, name)
    return ALG[key]


def ring_table(A):
    """All elements of a small algebra over a prime field as integers (base
    p digits of the coordinates), with the multiplication and addition
    tables and the set of units."""
    import numpy as np
    p = int(A.F.characteristic())
    assert A.F.is_prime_field()
    d = A.d
    n = p ** d
    X = np.array([[(c // p ** i) % p for i in range(d)] for c in range(n)],
                 dtype=np.int64)
    T = np.zeros((d, d, d), dtype=np.int64)  # b_i b_j = sum_k T[i,j,k] b_k
    for i in range(d):
        for j in range(d):
            col = A.L[i].column(j)
            for k in range(d):
                T[i, j, k] = int(col[k])
    weights = np.array([p ** i for i in range(d)], dtype=np.int64)
    XT = np.einsum('ai,ijk->ajk', X, T) % p
    P = np.einsum('bj,ajk->abk', X, XT) % p
    mul = (P @ weights).tolist()
    S = (X[:, None, :] + X[None, :, :]) % p
    add = (S @ weights).tolist()
    els = [vector(A.F, [int(a) for a in row]) for row in X]
    code = {tuple(v): i for i, v in enumerate(els)}
    one = code[tuple(A.one)]
    assert all(code[tuple(A.mul(els[a], els[b]))] == mul[a][b]
               for a, b in [(random.randrange(n), random.randrange(n))
                            for _ in range(50)])
    units = {i for i in range(n) if one in mul[i]
             and any(mul[i][j] == one and mul[j][i] == one for j in range(n))}
    return els, code, mul, add, one, units


SMALL_ALGEBRAS = ['F2S3', 'F3S3', 'F2A4', 'F4A4', 'F3A4', 'F2S4', 'F3S4',
                  'F4A5', 'F2V4', 'F2C4', 'F2D8', 'N2', 'N3', 'T2', 'T3', 'QF']


def any_alg(key):
    if key in ALG:
        return ALG[key]
    if key == 'N2':
        ALG[key] = nakayama(GF(2))
    elif key == 'N3':
        ALG[key] = nakayama(GF(3))
    elif key == 'T2':
        ALG[key] = triangular(GF(3), 2)
    elif key == 'T3':
        ALG[key] = triangular(GF(2), 3)
    elif key == 'QF':
        ALG[key] = qf_not_frobenius(GF(2))
    elif key == 'M2F2':
        basis = [matrix(GF(2), 2, 2, {(i, j): 1}) for i in range(2) for j in range(2)]
        ALG[key] = matrix_algebra(GF(2), basis, identity_matrix(GF(2), 2), 'M2F2')
    else:
        return alg(key)
    return ALG[key]


def all_subspaces(V):
    """All subspaces of an ambient space V = F^m."""
    for M in subspace_matrices(V.base_ring(), V.dimension()):
        yield V.subspace(M.rows())


def loewy_data(M, F, simples):
    n = mdim(M)
    rs = [to_sage(b, F, n).row_space() for b in radseries(M, simples)]
    ss = [to_sage(b, F, n).row_space() for b in GAPF['socseries'](M)]
    return rs, ss


def sample_modules(A):
    """PIMs, simples, the regular module, Rad P and P/Soc P."""
    D = A.data()
    mods = list(D['P']) + list(D['simples']) + [A.regular()]
    for P in D['P']:
        n = mdim(P)
        rb = rad(P, D['simples'])
        if len(list(rb)) > 0:
            mods.append(GAPF['sub'](P, rb))
            sb = mtx('BasisSocle')(P)
            mods.append(GAPF['quot'](P, libgap.IdentityMat(n, libgap(A.F)), sb))
    return mods


def right_data(A):
    """Right modules: the opposite algebra, its simple modules and PIMs."""
    if 'op' not in A.cache:
        A.cache['op'] = A.opposite()
    return A.cache['op']


def dual_index(A, i):
    """The index j of the right simple module isomorphic to S_i^*."""
    B = right_data(A)
    Sd = GAPF['dual'](A.data()['simples'][i])
    hits = [j for j, s in enumerate(B.data()['simples']) if GAPF['iso'](s, Sd)]
    assert len(hits) == 1
    return hits[0]


def injective_hull(A, i):
    """I_(S_i) = (P_(S_i^*))^*, the dual of a right PIM."""
    B = right_data(A)
    return GAPF['dual'](B.data()['P'][dual_index(A, i)])


def gram(A, lam):
    """The matrix (lam(b_i b_j))."""
    return matrix(lam.base_ring(), [lam * A.L[i].change_ring(lam.base_ring())
                                    for i in range(A.d)])


def layers(M, simples):
    """Composition multiplicities of the radical (Loewy) layers."""
    rs = radseries(M, simples)
    return [ilist(GAPF['mult'](GAPF['quot'](M, rs[i], rs[i + 1]), simples))
            for i in range(len(rs) - 1)]


class ZG:
    """The group ring (Z/m)G of the group of a group algebra A."""

    def __init__(self, A, m):
        self.A, self.m, self.d = A, m, A.d
        self.one = [0] * A.d
        self.one[A.id] = 1

    def lift(self, v):
        return [int(c) % self.m for c in v]

    def mul(self, x, y):
        z = [0] * self.d
        mt = self.A.mt
        ny = [(j, b) for j, b in enumerate(y) if b]
        for i, a in enumerate(x):
            if a:
                row = mt[i]
                for j, b in ny:
                    z[row[j]] += a * b
        return [c % self.m for c in z]

    def add(self, x, y):
        return [(a + b) % self.m for a, b in zip(x, y)]

    def sub(self, x, y):
        return [(a - b) % self.m for a, b in zip(x, y)]

    def smul(self, c, x):
        return [(c * a) % self.m for a in x]

    def g(self, i):
        v = [0] * self.d
        v[i] = 1
        return v

    def idem_step(self, a):
        a2 = self.mul(a, a)
        return self.sub(self.smul(3, a2), self.smul(2, self.mul(a2, a)))

    def make_idempotent(self, a, steps=60):
        for _ in range(steps):
            if self.mul(a, a) == a:
                return a
            a = self.idem_step(a)
        raise AssertionError('no idempotent reached')

    def is_central(self, x):
        return all(self.mul(x, self.g(gi)) == self.mul(self.g(gi), x)
                   for gi in self.A.gen_idx)

    def inverse(self, x):
        """Inverse by solving over Z/m (m a prime power), via lifting from
        the residue field: x^-1 = (1 + n + n^2 + ...) y with y x = 1 - n."""
        p = factor(self.m)[0][0]
        F = GF(p)
        Rx = self.A.rmat(vector(F, [c % p for c in x]))
        y0 = self.lift(Rx.solve_right(vector(F, [c % p for c in self.one])))
        # y0 x = 1 - n with n = 0 mod p, so n is nilpotent mod m
        n = self.sub(self.one, self.mul(y0, x))
        s, t = list(self.one), list(self.one)
        for _ in range(64):
            t = self.mul(t, n)
            if not any(t):
                break
            s = self.add(s, t)
        inv = self.mul(s, y0)
        assert self.mul(inv, x) == self.one and self.mul(x, inv) == self.one
        return inv



# ---------------------------------------------------------------------------
# Section 1.1 (pp. 1-3).


def f2_subspaces(n):
    """All subspaces of F2^n as frozensets of vectors coded as integers."""
    def span(gens):
        S = {0}
        for g in gens:
            S |= {s ^ g for s in S}
        return frozenset(S)
    subs = set()
    for k in range(n + 1):
        for gens in itertools.combinations(range(1, 2 ** n), k):
            subs.add(span(gens))
    return sorted(subs, key=len), span


def module_lattice(M, F):
    """All submodules of a MeatAxe module as Sage subspaces, with tables of
    sums and intersections (indices into the list)."""
    n = mdim(M)
    bases = mtx('BasesSubmodules')(M)
    subs = [to_sage(b, F, n).row_space() for b in bases]
    key = {S.echelonized_basis_matrix().__repr__(): i for i, S in enumerate(subs)}
    assert len(key) == len(subs)

    def find(S):
        return key[S.echelonized_basis_matrix().__repr__()]
    N = len(subs)
    plus = [[find(subs[i] + subs[j]) for j in range(N)] for i in range(N)]
    meet = [[find(subs[i].intersection(subs[j])) for j in range(N)]
            for i in range(N)]
    return subs, plus, meet


def composition_series(subs):
    """All maximal chains 0 = S_0 < ... < S_n = M of the lattice."""
    N = len(subs)
    covers = {i: [j for j in range(N) if subs[i].is_subspace(subs[j])
                  and subs[j].dimension() > subs[i].dimension()
                  and not any(subs[i].is_subspace(subs[k]) and
                              subs[k].is_subspace(subs[j]) and k not in (i, j)
                              for k in range(N))]
              for i in range(N)}
    bottom = min(range(N), key=lambda i: subs[i].dimension())
    top = max(range(N), key=lambda i: subs[i].dimension())
    chains = []

    def walk(c):
        if c[-1] == top:
            chains.append(list(c))
            return
        for j in covers[c[-1]]:
            walk(c + [j])
    walk([bottom])
    return chains


def section_1_1():
    # Lemma 1.1.2 (modular law), all triples of subspaces of F2^3 and F2^4.
    for n in (3, 4):
        subs, span = f2_subspaces(n)
        check(len(subs) == {3: 16, 4: 67}[n], 'number of subspaces of F2^%d' % n)
        ok = all(span(C | A) & B == span(C | (A & B))
                 for A in subs for B in subs for C in subs if C <= B)
        check(ok, 'Lemma 1.1.2: modular law on all subspaces of F2^%d' % n)
    # Theorem 1.1.3 (Zassenhaus), all quadruples V <= U, V' <= U' in F2^3:
    # the three quotients have equal dimension; the kernel identity and
    # the surjectivity used in the proof.
    subs, span = f2_subspaces(3)

    def dim(S):
        return len(S).bit_length() - 1
    pairs = [(U, V) for U in subs for V in subs if V <= U]
    good = 0
    for U, V in pairs:
        for U1, V1 in pairs:
            n1 = span(U | V1) & U1
            d1 = span(V | V1) & U1
            n2 = U & U1
            d2 = span((U1 & V) | (U & V1))
            n3 = span(U1 | V) & U
            d3 = span(V1 | V) & U
            assert d1 <= n1 and d2 <= n2 and d3 <= n3
            assert dim(n1) - dim(d1) == dim(n2) - dim(d2) == dim(n3) - dim(d3)
            # kernel of U & U' -> ((U + V') & U') / ((V + V') & U')
            assert (U & U1) & d1 == d2
            # the composite map is onto
            assert span((U & U1) | d1) == n1
            good += 1
    check(good == len(pairs) ** 2, 'Theorem 1.1.3 on %d quadruples' % good)

    # Theorem 1.1.4 (Jordan-Hoelder): every composition series of the regular
    # F3S3- and F2V4-modules has the same length and the same factors.
    for key in ('F3S3', 'F2V4', 'F2C4'):
        A = alg(key)
        D = A.data()
        R = A.regular()
        subs, plus, meet = module_lattice(R, A.F)
        chains = composition_series(subs)
        facts = set()
        for c in chains:
            f = [0] * len(D['simples'])
            for i, j in zip(c, c[1:]):
                q = GAPF['quot'](R, to_gap(subs[j]), to_gap(subs[i]))
                m = ilist(GAPF['mult'](q, D['simples']))
                assert sum(m) == 1, 'a covering pair has a simple quotient'
                f = [a + b for a, b in zip(f, m)]
            facts.add(tuple(f))
        check(len(facts) == 1 and list(facts.pop()) == D['mults'],
              'Theorem 1.1.4: %d composition series of %s, same factors'
              % (len(chains), key))
        # uniserial: a unique composition series
        if key == 'F2C4':
            check(len(chains) == 1, 'F2C4 is uniserial')
        else:
            check(len(chains) > 1, '%s regular module is not uniserial' % key)
    # the PIMs of F3S3 are uniserial: unique composition series, and unique
    # minimal submodule at every step
    A = alg('F3S3')
    for S, P, t in A.data()['pims']:
        subs, plus, meet = module_lattice(P, A.F)
        check(len(composition_series(subs)) == 1 and
              sorted(s.dimension() for s in subs) == [0, 1, 2, 3],
              'PIM of F3S3 uniserial (chain of submodules)')

    # Exercise (p. 2): the submodule lattice of a module of finite length is
    # distributive iff no subquotient is isomorphic to S + S, S simple.
    def exercise_distributive(M, A, label):
        D = A.data()
        subs, plus, meet = module_lattice(M, A.F)
        N = len(subs)
        dist = all(meet[plus[a][b]][c] == plus[meet[a][c]][meet[b][c]] and
                   plus[meet[a][b]][c] == meet[plus[a][c]][plus[b][c]]
                   for a in range(N) for b in range(N) for c in range(N))
        sdims = [mdim(s) for s in D['simples']]
        found = False
        for i in range(N):
            for j in range(N):
                if found or not subs[j].is_subspace(subs[i]):
                    continue
                dd = subs[i].dimension() - subs[j].dimension()
                if dd not in [2 * s for s in sdims]:
                    continue
                q = GAPF['quot'](M, to_gap(subs[i]), to_gap(subs[j]))
                if len(list(rad(q, D['simples']))) == 0:
                    m = ilist(GAPF['mult'](q, D['simples']))
                    if sorted(m)[-1] == 2 and sum(m) == 2:
                        found = True
        check(dist == (not found),
              'Exercise 1.1: %s (%d submodules) distributive=%s' % (label, N, dist))
        return dist
    A = alg('F3S3')
    D = A.data()
    k, sgn = D['simples']
    Pk = D['P'][0]
    expect = []
    expect.append(exercise_distributive(Pk, A, 'P_k of F3S3'))
    expect.append(exercise_distributive(GAPF['dsum'](k, sgn), A, 'k+sgn'))
    expect.append(exercise_distributive(GAPF['dsum'](k, k), A, 'k+k'))
    expect.append(exercise_distributive(GAPF['dsum'](Pk, sgn), A, 'P_k+sgn'))
    expect.append(exercise_distributive(GAPF['dsum'](Pk, k), A, 'P_k+k'))
    expect.append(exercise_distributive(A.regular(), A, 'F3S3'))
    for key in ('F2V4', 'F2C4', 'F2S3'):
        B = alg(key)
        expect.append(exercise_distributive(B.regular(), B, key))
    check(expect == [True, True, False, False, False, False, False, True, False],
          'Exercise 1.1: the nine lattices as expected')


# ---------------------------------------------------------------------------
# Section 1.2 (pp. 3-5).

def section_1_2():
    # Definition 1.2.1, last paragraph (as corrected: M has a composition
    # series): socle length = radical length = n and Rad^(n-j) <= Soc^j;
    # second paragraph: M completely reducible iff Rad(M) = 0.
    nmod = 0
    for key in SMALL_ALGEBRAS:
        A = any_alg(key)
        for M in sample_modules(A):
            rs, ss = loewy_data(M, A.F, A.data()['simples'])
            n = len(rs) - 1
            assert len(ss) - 1 == n, (key, 'socle length != radical length')
            assert all(rs[n - j].is_subspace(ss[j]) for j in range(n + 1))
            semisimple = (len(ss) <= 2)
            assert semisimple == (len(rs) <= 2)
            nmod += 1
    check(nmod > 100, 'Definition 1.2.1 on %d modules of %d algebras'
          % (nmod, len(SMALL_ALGEBRAS)))
    # The printed paragraph for an arbitrary ring is refuted by the ring of
    # eventually constant sequences over a field (not computed): there
    # Rad = J = 0 (the evaluation ideals are maximal and meet in 0), the
    # socle is the ideal of finitely supported sequences, with simple
    # quotient (the eventual value); socle length 2, radical length 1.

    # Paragraph after Definition 1.2.1: the annihilator of an irreducible
    # module is primitive (Lambda/ann(S) acts faithfully and irreducibly on
    # S, and is the full ring End_Delta(S): dim = n^2 dim Delta); the
    # annihilator of the regular module is 0, which is not primitive when
    # Lambda has no faithful simple module (as printed for every M).
    for key in ('F3S3', 'F2A4', 'F2S4', 'N3', 'T3', 'QF'):
        A = any_alg(key)
        D = A.data()
        anns = []
        for s, endo in zip(D['simples'], D['ends']):
            mats = A.allmats(s)
            K = matrix(A.F, [A.act(mats, A.e(i)).list() for i in range(A.d)])
            ann = K.left_kernel()
            anns.append(ann)
            ds = mdim(s)
            check(A.d - ann.dimension() == (ds // endo) ** 2 * endo,
                  '%s: Lambda/ann(S) = End_Delta(S), primitive' % key)
            check(A.is_left_ideal(ann) and A.is_right_ideal(ann),
                  '%s: annihilator is two sided' % key)
        refuted(any(a.dimension() == 0 for a in anns),
                '%s: the annihilator 0 of the regular module is primitive' % key)
        # J = intersection of the primitive ideals = Rad(Lambda_Lambda)
        inter = anns[0]
        for a in anns[1:]:
            inter = inter.intersection(a)
        check(inter == D['J'], '%s: J = intersection of annihilators of simples'
              % key)
    for key in SMALL_ALGEBRAS:
        A = any_alg(key)
        D = A.data()
        J = D['J']
        check(A.is_left_ideal(J) and A.is_right_ideal(J), '%s: J two sided' % key)
        # Lambda/J semisimple: dim = sum n_i^2 dim Delta_i
        check(A.d - J.dimension() == sum(mdim(s) ** 2 // e for s, e in
                                         zip(D['simples'], D['ends'])),
              '%s: dim Lambda/J (Wedderburn)' % key)
        # Theorem 1.2.7 (i): J is nilpotent
        P, k = J, 1
        while P.dimension() > 0:
            P = A.span_mul(P, J)
            k += 1
            assert k <= A.d + 1
        check(P.dimension() == 0, '%s: J^%d = 0' % (key, k))

    # J by maximal left and right ideals, and {x : 1 - axb unit for all a, b},
    # exhaustively on rings of at most 64 elements.
    for key in ('F2S3', 'F2V4', 'F2C4', 'T3', 'N2', 'M2F2'):
        A = any_alg(key)
        J = A.data()['J']
        lefts = [S for S in all_subspaces(A.V) if A.is_left_ideal(S)]
        rights = [S for S in all_subspaces(A.V) if A.is_right_ideal(S)]
        for ideals, side in ((lefts, 'left'), (rights, 'right')):
            proper = [S for S in ideals if S.dimension() < A.d]
            maximal = [S for S in proper if not any(S != T and S.is_subspace(T)
                                                    for T in proper)]
            inter = maximal[0]
            for T in maximal[1:]:
                inter = inter.intersection(T)
            check(inter == J, '%s: J = intersection of maximal %s ideals'
                  % (key, side))
        els, code, mul, add, one, units = ring_table(A)
        neg = {i: code[tuple(-v)] for i, v in enumerate(els)}
        n = len(els)
        qr = [x for x in range(n)
              if all(add[one][neg[mul[mul[a][x]][b]]] in units
                     for a in range(n) for b in range(n))]
        check(sorted(qr) == sorted(code[tuple(v)] for v in J),
              '%s: J = {x : 1 - axb is a unit for all a, b}' % key)
    # F3S3 (729 elements): x in J iff 1 - ax is a unit for all a.
    A = alg('F3S3')
    J = A.data()['J']
    els, code, mul, add, one, units = ring_table(A)
    neg = {i: code[tuple(-v)] for i, v in enumerate(els)}
    qr = [x for x in range(len(els))
          if all(add[one][neg[mul[a][x]]] in units for a in range(len(els)))]
    check(sorted(qr) == sorted(code[tuple(v)] for v in J),
          'F3S3: J = {x : 1 - ax is a unit for all a} (Lemma 1.2.2)')

    def radical_of(ds):
        """Rad of Z/d1 + ... + Z/dr: the intersection of the kernels of all
        homomorphisms onto some Z/p (these kernels are the maximal
        subgroups)."""
        elems = list(itertools.product(*[range(d) for d in ds]))
        kers = []
        for p in sorted({q for d in ds for q, _ in factor(d)}):
            for c in itertools.product(range(p), repeat=len(ds)):
                if any(ci and d % p for ci, d in zip(c, ds)) or not any(c):
                    continue
                kers.append(frozenset(x for x in elems if
                                      sum(ci * xi for ci, xi in zip(c, x)) % p == 0))
        return elems, frozenset.intersection(*kers)

    # Proposition 1.2.5.  As printed (no hypothesis): Lambda = Z, M = Z/4
    # (the author's counterexample).  J(Z) = 0: an integer 0 < n < 30030 is
    # prime to one of 2, 3, 5, 7, 11, 13, so it avoids a maximal ideal pZ.
    check(all(any(n % p for p in (2, 3, 5, 7, 11, 13)) for n in range(1, 30030)),
          'J(Z) = 0 (n < 30030 avoids some pZ)')
    elems, rad4 = radical_of([4])
    check(sorted(rad4) == [(0,), (2,)], 'Rad(Z/4) = 2Z/4')
    refuted(sorted(rad4) == [(0,)], 'Proposition 1.2.5 as printed: '
            'J(Z) Z/4 = 0 equals Rad(Z/4)')

    # Corrected (Lambda/J(Lambda) satisfies D.C.C.): Lambda = Z/m, all
    # modules Z/d1 + Z/d2 + Z/d3 (d_i | m, d_i > 1) of order <= 64.
    nmods = 0
    for m in (8, 9, 12, 16):
        _, Jm = radical_of([m])            # J(Z/m) = Rad of the regular module
        jm = prod(p for p, _ in factor(m))
        assert Jm == frozenset((jm * a % m,) for a in range(m))  # = jm Z/m
        for r in (1, 2, 3):
            for ds in itertools.combinations_with_replacement(
                    [d for d in divisors(m) if d > 1], r):
                if prod(ds) > 64:
                    continue
                elems, rad = radical_of(ds)
                JM = frozenset(tuple((jm * a) % d for a, d in zip(x, ds))
                               for x in elems)
                # J M = jm M, since J = jm Z/m
                assert rad == JM, (m, ds)
                nmods += 1
    check(nmods >= 30, 'Proposition 1.2.5 corrected: J M = Rad M for %d '
          'modules over Z/8, Z/9, Z/12, Z/16' % nmods)

    # Proposition 1.2.8, exhaustively over all subrings (= F_p-subalgebras,
    # they contain the prime field) of five algebras.
    for key in ('F3S3', 'F2C4', 'F2V4', 'F3C3', 'T3'):
        A = any_alg(key)
        J = A.data()['J']
        J2 = A.span_mul(J, J)
        # a complement C of F.1: subspaces containing 1 are 1 + (rows in C)
        piv = matrix(A.F, [A.one]).pivots()[0]
        C = matrix(A.F, [A.e(i) for i in range(A.d) if i != piv])
        nsub, n_fill_J = 0, 0
        for U in subspace_matrices(A.F, A.d - 1):
            W = A.V.subspace(mm(U, C).rows() + [A.one])
            if not all(A.mul(x, y) in W for x in W.basis() for y in W.basis()):
                continue
            nsub += 1
            if W + J2 == A.V:
                assert W == A.V
            if W + J == A.V and W != A.V:
                n_fill_J += 1
        check(nsub >= 2, 'Proposition 1.2.8 on all %d subrings of %s' % (nsub, key))
        check(n_fill_J > 0, '%s: a proper subring with L\' + J = L (J^2 needed)'
              % key)


# ---------------------------------------------------------------------------
# Section 1.3 (pp. 5-7).


def central_idempotents_QQ(A):
    """Primitive central idempotents of a semisimple QQ-algebra, from the
    factorization of the minimal polynomial of a generator of the centre."""
    Z = A.center()
    R = PolynomialRing(QQ, 'x')
    zb = Z.basis()
    for trial in range(20):
        z = sum((random.randint(-3, 3) * b for b in zb), A.V.zero_vector())
        powers = [A.one]
        for _ in range(Z.dimension()):
            powers.append(A.mul(powers[-1], z))
        if A.V.subspace(powers[:Z.dimension()]).dimension() == Z.dimension():
            break
    m = A.lmat(z).minpoly().change_ring(QQ)
    m = R(list(m))
    assert m.degree() == Z.dimension() and m.is_squarefree()
    facs = [f for f, _ in m.factor()]
    ids = []
    for f in facs:
        g = m // f
        # g * (g^-1 mod f) is 1 mod f and 0 mod the other factors
        h = (g * g.inverse_mod(f)) % m
        e = sum((h[k] * powers[k] for k in range(h.degree() + 1)),
                A.V.zero_vector())
        ids.append((e, f))
    return ids


def section_1_3():
    # Theorem 1.3.5 (Wedderburn-Artin) and Theorem 1.3.4 over QQ.
    # QS3 = Q + Q + Mat_2(Q): the 4-dimensional component is mapped
    # isomorphically onto Mat_2(Q) by the natural (Specht) representation.
    A = group_algebra(S3, QQ, 'QS3')
    ids = central_idempotents_QQ(A)
    check(sum((e for e, f in ids), A.V.zero_vector()) == A.one and
          all(A.mul(e, e) == e for e, f in ids) and
          all(A.mul(e1, e2) == 0 for (e1, _), (e2, _) in
              itertools.combinations(ids, 2)),
          'QS3: orthogonal central idempotents with sum 1')
    dims = sorted((A.lmat(e).rank(), f.degree()) for e, f in ids)
    check(dims == [(1, 1), (1, 1), (4, 1)], 'QS3 = Q + Q + (4-dim, centre Q)')
    rho = SymmetricGroupRepresentation([2, 1], 'specht')
    big = [e for e, f in ids if A.lmat(e).rank() == 4][0]
    images = []
    for i, g in enumerate(A.els):
        x = A.mul(big, A.e(i))
        images.append(sum((x[j] * rho.representation_matrix(
            Permutation([int(a) for a in libgap.ListPerm(A.els[j], 3)])).change_ring(QQ)
            for j in range(A.d)), matrix(QQ, 2, 2)).list())
    check(matrix(QQ, images).rank() == 4,
          'QS3: the component e QS3 maps onto Mat_2(Q) (Delta = Q, n = 2)')
    # QC3 = Q + Q(zeta_3): Delta a field of degree 2, n = 1.
    A = group_algebra(C3, QQ, 'QC3')
    ids = central_idempotents_QQ(A)
    check(sorted((A.lmat(e).rank(), f.degree()) for e, f in ids) == [(1, 1), (2, 2)],
          'QC3 = Q + Q(zeta_3)')
    # QQ8 = Q^4 + H_Q, H_Q = (-1,-1)_Q a division ring (Delta noncommutative).
    A = group_algebra(Q8, QQ, 'QQ8')
    ids = central_idempotents_QQ(A)
    check(sorted((A.lmat(e).rank(), f.degree()) for e, f in ids) ==
          [(1, 1)] * 4 + [(4, 1)], 'QQ8: four 1-dim components and one of dim 4')
    h = [e for e, f in ids if A.lmat(e).rank() == 4][0]
    order4 = [i for i in range(A.d) if A.mt[i][i] != A.id and
              A.mt[A.mt[i][i]][A.mt[i][i]] == A.id]
    gi = order4[0]
    gj = [j for j in order4 if A.mt[gi][j] != A.mt[j][gi]][0]
    I = A.mul(h, A.e(gi))
    Jq = A.mul(h, A.e(gj))
    check(A.mul(I, I) == -h and A.mul(Jq, Jq) == -h and
          A.mul(I, Jq) == -A.mul(Jq, I),
          'QQ8: the 4-dim component is the quaternion algebra (-1,-1)_Q')
    check(QuaternionAlgebra(QQ, -1, -1).is_division_algebra(),
          '(-1,-1)_Q is a division algebra (Delta = H_Q, n = 1)')
    # Exercise (p. 7): Q(i) splits it: i -> diag(i, -i), j -> [[0,1],[-1,0]].
    K = QuadraticField(-1, 'i')
    ii = K.gen()
    Mi = matrix(K, [[ii, 0], [0, -ii]])
    Mj = matrix(K, [[0, 1], [-1, 0]])
    check(Mi ** 2 == -1 and Mj ** 2 == -1 and Mi * Mj == -Mj * Mi and
          matrix(K, [m.list() for m in (identity_matrix(K, 2), Mi, Mj, Mi * Mj)]).rank() == 4,
          'Exercise 1.3: Q(i) is a splitting field for (-1,-1)_Q')

    # Semisimple group algebras over finite fields (p not dividing |G|):
    # J = 0, Lambda = sum Mat_(n_i)(Delta_i), n_i = dim_(Delta_i^op) S_i =
    # multiplicity of S_i in the regular module, Delta_i commutative
    # (Remark (i): finite division rings are fields).
    expected = {'F2C3': [(1, 1), (2, 2)], 'F2C7': [(1, 1), (3, 3), (3, 3)],
                'F3Q8': [(1, 1)] * 4 + [(2, 1)], 'F5S3': [(1, 1), (1, 1), (2, 1)],
                'F4C3': [(1, 1)] * 3}
    for key, exp in expected.items():
        A = alg(key)
        D = A.data()
        check(D['J'].dimension() == 0, '%s semisimple' % key)
        got = sorted((mdim(s), e) for s, e in zip(D['simples'], D['ends']))
        check(got == sorted(exp), '%s: simple modules and Delta_i' % key)
        check(all(m == mdim(s) // e for s, e, m in
                  zip(D['simples'], D['ends'], D['mults'])),
              '%s: multiplicity n_i = dim_(Delta^op) S_i' % key)
        check(sum((mdim(s) // e) ** 2 * e for s, e in zip(D['simples'], D['ends']))
              == A.d, '%s: dim = sum n_i^2 dim Delta_i' % key)
        for s in D['simples']:
            E = [matrix(A.F, b.sage(ring=A.F)) for b in
                 mtx('BasisModuleEndomorphisms')(s)]
            assert all(mm(x, y) == mm(y, x) for x in E for y in E)
        check(True, '%s: every Delta_i is commutative' % key)
        # number of simple components = number of primitive central idempotents
        Z = A.center()
        cid = [z for z in Z if A.mul(z, z) == z]
        check(len(cid) == 2 ** len(D['simples']),
              '%s: r = %d simple components' % (key, len(D['simples'])))
    # F3Q8: the 2-dimensional simple module is absolutely irreducible
    # (the quaternion algebra splits over F3), unlike over Q.
    check(alg('F3Q8').data()['ends'] == [1] * 5, 'F3Q8: Delta = F3 throughout')

    # Theorem 1.3.4: End(M) for M = S + S + T is Mat_2(Delta_S) + Delta_T and
    # semisimple.
    for key, (i, j) in (('F3S3', (0, 1)), ('F2A4', (1, 0))):
        A = alg(key)
        D = A.data()
        S, T = D['simples'][i], D['simples'][j]
        M = GAPF['dsum'](GAPF['dsum'](S, S), T)
        E = [matrix(A.F, b.sage(ring=A.F)) for b in mtx('BasisModuleEndomorphisms')(M)]
        check(len(E) == 4 * D['ends'][i] + D['ends'][j],
              '%s: dim End(S+S+T) = 4 dim Delta_S + dim Delta_T' % key)
        n = mdim(M)
        EA = matrix_algebra(A.F, E, identity_matrix(A.F, n), 'End')
        ED = EA.data()
        check(ED['J'].dimension() == 0, '%s: End(S+S+T) is semisimple' % key)

    # Lemma 1.3.3 on primitive idempotents of six algebras: e M = Hom(L e, M),
    # and x -> (y -> y x) is an anti-isomorphism e L e -> End(L e).
    for key in ('F3S3', 'F4A4', 'F2A4', 'N3', 'T2', 'QF'):
        A = any_alg(key)
        D = A.data()
        es = A.idempotents_from_pims()
        check(sum(es, A.V.zero_vector()) == A.one and
              all(A.mul(es[a], es[b]) == (es[a] if a == b else 0)
                  for a in range(len(es)) for b in range(len(es))),
              '%s: 1 = sum of orthogonal idempotents e_i' % key)
        for e, (S, P, t) in zip(es, D['pims']):
            Le = A.V.subspace(A.rmat(e).columns())
            assert Le == S, 'L e_i is the summand'
            Pe = A.submodule(Le)
            for M in list(D['simples']) + list(D['P']):
                mats = A.allmats(M)
                eM = A.act(mats, e).rank()
                assert eM == int(GAPF['homdim'](Pe, M)), 'Lemma 1.3.3 (i)'
            # (ii)
            corner = A.V.subspace([A.mul(A.mul(e, A.e(i)), e) for i in range(A.d)])
            B = Le.basis_matrix()

            def rho(x):
                return matrix(A.F, [B.solve_left(A.mul(y, x)) for y in B.rows()]).transpose()
            reps = [rho(x) for x in corner.basis()]
            # module endomorphisms: commute with left multiplication
            for g in A.gens:
                Lg = matrix(A.F, [B.solve_left(A.mul(g, y)) for y in B.rows()]).transpose()
                assert all(mm(Lg, r) == mm(r, Lg) for r in reps)
            assert matrix(A.F, [r.list() for r in reps]).rank() == corner.dimension()
            for x in corner.basis():
                for y in corner.basis():
                    assert rho(A.mul(x, y)) == mm(rho(y), rho(x))
            ends = len(list(mtx('BasisModuleEndomorphisms')(Pe)))
            assert ends == corner.dimension()
        check(True, '%s: Lemma 1.3.3 (i), (ii) for all %d idempotents e_i'
              % (key, len(es)))

    # Proposition 1.3.6 (Skolem-Noether) for M_2(F_q), q = 2, 3, 5: the
    # automorphisms are given by the images X, Y of E12, E21 subject to the
    # matrix-unit relations; all of them are conjugations.
    for q in (2, 3, 5):
        def mul2(a, b):
            return ((a[0] * b[0] + a[1] * b[2]) % q, (a[0] * b[1] + a[1] * b[3]) % q,
                    (a[2] * b[0] + a[3] * b[2]) % q, (a[2] * b[1] + a[3] * b[3]) % q)

        def add2(a, b):
            return tuple((x + y) % q for x, y in zip(a, b))
        allm = list(itertools.product(range(q), repeat=4))
        nil = [x for x in allm if mul2(x, x) == (0, 0, 0, 0) and x != (0, 0, 0, 0)]
        I2 = (1, 0, 0, 1)
        sols = set()
        for X in nil:
            for Y in nil:
                if add2(mul2(X, Y), mul2(Y, X)) == I2 and \
                        mul2(mul2(X, Y), X) == X and mul2(mul2(Y, X), Y) == Y:
                    sols.add((X, Y))
        GL = [g for g in allm if (g[0] * g[3] - g[1] * g[2]) % q]
        conj = set()
        for g in GL:
            det = (g[0] * g[3] - g[1] * g[2]) % q
            dinv = pow(det, q - 2, q)
            gi = ((g[3] * dinv) % q, (-g[1] * dinv) % q, (-g[2] * dinv) % q,
                  (g[0] * dinv) % q)
            conj.add((mul2(mul2(g, (0, 1, 0, 0)), gi), mul2(mul2(g, (0, 0, 1, 0)), gi)))
        check(sols == conj and len(sols) == q * (q * q - 1),
              'Proposition 1.3.6: all %d automorphisms of M_2(F_%d) are inner'
              % (len(sols), q))


# ---------------------------------------------------------------------------
# Sections 1.4 (pp. 7-9) and 1.5 (pp. 9-11).


def section_1_4():
    # Lemma 1.4.4 (Fitting) for every endomorphism of the regular module
    # (= right multiplication by an element, Lemma 1.3.3 with e = 1).
    for key in ('F3S3', 'F2V4', 'N3', 'T3', 'F2A4'):
        A = any_alg(key)
        n = 0
        for x in A.V:
            f = A.rmat(x)
            fn = mpow(f, A.d)
            im = fn.column_space()
            ker = fn.right_kernel()
            assert im.dimension() + ker.dimension() == A.d
            assert im.intersection(ker).dimension() == 0
            assert mm(fn, f).rank() == fn.rank()   # the chains have stopped
            n += 1
        check(n == A.F.order() ** A.d,
              'Lemma 1.4.4: M = Im f^n + Ker f^n for all %d endomorphisms of %s'
              % (n, key))

    # Lemma 1.4.5 and Definition 1.4.1: End(P) = e L e (P = L e a PIM) is
    # local: every element is a unit of e L e or nilpotent, the non-units
    # form an ideal, and the quotient is the division ring Delta.
    for key in ('F3S3', 'F4A4', 'F2A4', 'F2S4', 'F2V4', 'N3', 'T2', 'QF'):
        A = any_alg(key)
        D = A.data()
        for e, (S, P, t) in zip(A.idempotents_from_pims(), D['pims']):
            corner = A.V.subspace([A.mul(A.mul(e, A.e(i)), e) for i in range(A.d)])
            els = list(corner)
            units = [x for x in els if any(A.mul(x, y) == e and A.mul(y, x) == e
                                           for y in els)]
            nonunits = [x for x in els if x not in units]

            def nilpotent(x):
                y = x
                for _ in range(A.d + 1):
                    if y == 0:
                        return True
                    y = A.mul(y, x)
                return y == 0
            assert all(nilpotent(x) for x in nonunits)
            NU = A.V.subspace(nonunits)
            assert len(nonunits) == A.F.order() ** NU.dimension()  # a subspace
            assert all(A.mul(x, y) in NU and A.mul(y, x) in NU
                       for x in NU.basis() for y in corner.basis())
            assert corner.dimension() - NU.dimension() == D['ends'][t]
        check(True, '%s: End(P) local for every PIM, End(P)/rad = Delta' % key)

    # Theorem 1.4.6 (Krull-Schmidt): two decompositions of the regular module
    # (the second in a random basis) have the same summands; the PIM P_i
    # occurs n_i = dim_(Delta_i^op) S_i times (Section 1.7).
    for key in ('F3S4', 'F2A4', 'F4A5', 'QF'):
        A = any_alg(key)
        D = A.data()
        R = A.regular()
        gm = [matrix(A.F, g.sage(ring=A.F)) for g in mtx('Generators')(R)]
        while True:
            elems = list(A.F)
            g = matrix(A.F, A.d, A.d, [random.choice(elems) for _ in range(A.d ** 2)])
            if g.is_invertible():
                break
        R2 = gmod([mm(mm(g, m), g.inverse()) for m in gm], A.F)
        types = []
        for M in (R, R2):
            cnt = [0] * len(D['simples'])
            for pair in mtx('Indecomposition')(M):
                hits = [i for i, P in enumerate(D['P']) if GAPF['iso'](P, pair[1])]
                assert len(hits) == 1
                cnt[hits[0]] += 1
            types.append(cnt)
        check(types[0] == types[1] == [mdim(s) // e for s, e in
                                        zip(D['simples'], D['ends'])],
              'Theorem 1.4.6: %s = sum n_i P_i, n_i = %s' % (key, types[0]))

    # Exercise (p. 9): Krull-Schmidt for f.g. O-modules iff class number one.
    # O = Z[w], w^2 = -5: I = (2, 1 + w) is not principal, but I + I = O + O:
    # (x, y) -> (x, y) A with A = (1/2)[[1 + w, 2], [2, 1 - w]] maps a Z-basis
    # of I + I onto one of O + O.
    K = QuadraticField(-5, 'w')
    w = K.gen()
    I = K.ideal(2, 1 + w)
    check(K.class_number() == 2 and not I.is_principal(),
          'Q(sqrt(-5)): class number 2, I = (2, 1 + sqrt(-5)) not principal')
    check(I.norm() == 2 and all(a * a + 5 * b * b != 2 for a in range(-2, 3)
                                for b in range(-1, 2)),
          'no element of norm 2: I is not principal (indecomposable, not free)')
    zI = [K(2), 1 + w]                     # Z-basis of I (index 2 in Z[w])
    check(all(x in I for x in (2 * w, w - 5)) and
          matrix(QQ, [[2, 0], [1, 1]]).det() == 2, 'Z-basis {2, 1 + w} of I')
    Amat = matrix(K, [[1 + w, 2], [2, 1 - w]]) / 2
    basisIplusI = [vector(K, [x, 0]) for x in zI] + [vector(K, [0, x]) for x in zI]
    imgs = [v * Amat for v in basisIplusI]

    def zcoords(v):  # coordinates in the Z-basis (1,0),(w,0),(0,1),(0,w) of O + O
        out = []
        for c in v:
            a, b = c.list()                  # c = a + b w
            out += [a, b]
        return out
    Mz = matrix(QQ, [zcoords(v) for v in imgs])
    check(all(x in ZZ for x in Mz.list()) and abs(Mz.det()) == 1,
          'I + I = O + O (Krull-Schmidt fails for O-modules, h = 2)')
    hs = {d: QuadraticField(d, 'a').class_number()
          for d in (-1, -2, -3, -7, -11, -19, -43, -67, -163, -5, -6, -10, -15, -23)}
    check([hs[d] for d in (-1, -2, -3, -7, -11, -19, -43, -67, -163)] == [1] * 9 and
          [hs[d] for d in (-5, -6, -10, -15, -23)] == [2, 2, 2, 2, 3],
          'class numbers of Q(sqrt d) for 14 values of d')


def section_1_5():
    # Projective covers and Lemma 1.5.3 (Schanuel).  F3S3, M = k: the
    # projective cover P_k -> k with kernel Rad P_k = Omega(k), and the
    # augmentation L -> k with kernel the augmentation ideal I:
    # Omega(k) + L = P_k + I.
    A = alg('F3S3')
    D = A.data()
    k = D['simples'][0]
    k_idx = [i for i, s in enumerate(D['simples'])
             if all(m[0, 0] == 1 for m in A.allmats(s))][0]
    Pk = D['P'][k_idx]
    omega = GAPF['sub'](Pk, rad(Pk, D['simples']))
    aug = A.V.subspace([A.e(i) - A.one for i in range(A.d)])
    check(aug.dimension() == A.d - 1 and A.is_left_ideal(aug), 'augmentation ideal')
    Iaug = A.submodule(aug)
    check(GAPF['iso'](GAPF['dsum'](omega, A.regular()), GAPF['dsum'](Pk, Iaug)),
          'Lemma 1.5.3: Omega(k) + F3S3 = P_k + I (F3S3)')
    check(mdim(omega) == 2 and int(GAPF['homdim'](Pk, D['simples'][k_idx])) == 1,
          'F3S3: P_k is the projective cover of k (dim 3, Omega(k) of dim 2)')
    # F2V4, M = k: L -> k (kernel J) and L + L -> k, (x, y) -> e(x) + e(y).
    A = alg('F2V4')
    D = A.data()
    R2 = GAPF['dsum'](A.regular(), A.regular())
    V2 = A.F ** (2 * A.d)
    ker = V2.subspace([vector(A.F, list(A.e(i) - A.one) + [0] * A.d)
                       for i in range(A.d)] +
                      [vector(A.F, [0] * A.d + list(A.e(i) - A.one)) for i in range(A.d)] +
                      [vector(A.F, list(A.one) + list(A.one))])
    check(ker.dimension() == 2 * A.d - 1, 'kernel of L + L -> k')
    Kmod = GAPF['sub'](R2, to_gap(ker))
    Jmod = A.submodule(D['J'])
    check(GAPF['iso'](GAPF['dsum'](Jmod, R2), GAPF['dsum'](A.regular(), Kmod)),
          'Lemma 1.5.3: J + (L + L) = L + K (F2V4)')


# ---------------------------------------------------------------------------
# Section 1.6 (pp. 11-12).

GROUP_KEYS = ['F2S3', 'F3S3', 'F2A4', 'F4A4', 'F3A4', 'F2S4', 'F3S4', 'F4A5',
              'F2D8', 'F2V4', 'F2C4', 'F3C3']


def symbolic_gram_det(A, U):
    """det of (lam(b_i b_j)) for lam = sum t_k u_k (u_k the rows of U)."""
    R = PolynomialRing(A.F, ['t%d' % k for k in range(U.nrows())])
    lam = sum((R.gen(k) * vector(R, U.row(k)) for k in range(U.nrows())),
              vector(R, [0] * A.d))
    return gram(A, lam).det()


def self_injective(A):
    """L_L is injective iff every left PIM is an injective hull I_S."""
    D = A.data()
    hulls = [injective_hull(A, i) for i in range(len(D['simples']))]
    return all(any(GAPF['iso'](P, I) for I in hulls) for P in D['P'])


def section_1_6():
    # The Remark (Section 3.1): a group algebra is symmetric, with lam the
    # coefficient of the identity; Definition 1.6.1 (i) is the non-degeneracy
    # of (a, b) -> lam(ab).
    for key in GROUP_KEYS:
        A = alg(key)
        lam = A.e(A.id)
        G = gram(A, lam)
        check(G.is_invertible() and G == G.transpose(),
              '%s: lam(ab) non-degenerate and symmetric' % key)
    # directly on F2S3: no nonzero left or right ideal lies in Ker(lam)
    A = alg('F2S3')
    lam = A.e(A.id)
    ideals = [S for S in all_subspaces(A.V) if S.dimension() > 0 and
              (A.is_left_ideal(S) or A.is_right_ideal(S))]
    check(all(any(lam * v != 0 for v in S.basis()) for S in ideals),
          'F2S3: Ker(lam) contains no nonzero one-sided ideal (%d ideals)'
          % len(ideals))

    # Proposition 1.6.2 (i): phi(x)(y) = lam(yx) is an isomorphism
    # L_L -> (L_L)^*; the MeatAxe dual of the right regular module is then
    # isomorphic to the left regular module.
    N3 = any_alg('N3')
    lamN = vector(N3.F, [0, 0, 1, 1])        # lam(a) = lam(b) = 1
    frob = [(alg('F3S3'), alg('F3S3').e(alg('F3S3').id)),
            (alg('F4A4'), alg('F4A4').e(alg('F4A4').id)), (N3, lamN)]
    for A, lam in frob:
        phi = matrix(A.F, [[lam * A.mul(A.e(j), A.e(i)) for j in range(A.d)]
                           for i in range(A.d)]).transpose()  # column i = phi(b_i)
        ok = phi.is_invertible()
        for g in A.gens:
            for i in range(A.d):
                # gamma . f = f(- gamma): as a column, rmat(gamma)^T f
                ok = ok and (phi * A.mul(g, A.e(i)) ==
                             A.rmat(g).transpose() * (phi * A.e(i)))
        check(ok, '%s: Proposition 1.6.2 (i), phi a module isomorphism' % A.name)
        Rop = right_data(A).regular()
        check(GAPF['iso'](GAPF['dual'](Rop), A.regular()),
              '%s: (L_L)^* = L_L' % A.name)

    # Theorem 1.6.3 on all PIMs of the group algebras: Soc P = P/Rad P.
    npims = 0
    for key in GROUP_KEYS:
        A = alg(key)
        D = A.data()
        for P in D['P']:
            n = mdim(P)
            soc = GAPF['sub'](P, mtx('BasisSocle')(P))
            top = GAPF['quot'](P, libgap.IdentityMat(n, libgap(A.F)),
                               rad(P, D['simples']))
            assert sum(ilist(GAPF['mult'](soc, D['simples']))) == 1, 'Soc P simple'
            assert GAPF['iso'](soc, top)
            npims += 1
    check(npims == 25, 'Theorem 1.6.3: Soc P = P/Rad P for %d PIMs of %d '
          'group algebras' % (npims, len(GROUP_KEYS)))

    # A Frobenius algebra that is not symmetric: the Nakayama algebra N
    # (cyclic quiver with two vertices, paths of length 2 zero).  lam above
    # is non-degenerate; every symmetric lam (vanishing on [N, N]) is
    # degenerate; Soc P_1 = S_2 is not P_1/Rad P_1 = S_1.
    A = N3
    D = A.data()
    check(gram(A, lamN).is_invertible(), 'N: Frobenius')
    comm = A.V.subspace([A.mul(A.e(i), A.e(j)) - A.mul(A.e(j), A.e(i))
                         for i in range(A.d) for j in range(A.d)])
    symm = comm.basis_matrix().right_kernel()   # lam vanishing on [N, N]
    check(symbolic_gram_det(A, symm.basis_matrix()) == 0,
          'N: no symmetric non-degenerate lam (det = 0 identically)')
    for P in D['P']:
        n = mdim(P)
        soc = GAPF['sub'](P, mtx('BasisSocle')(P))
        top = GAPF['quot'](P, libgap.IdentityMat(n, libgap(A.F)), rad(P, D['simples']))
        check(not GAPF['iso'](soc, top), 'N: Soc P is not P/Rad P ("in general '
              'they are not isomorphic")')
    # the triangular algebra T2: not Frobenius (det = 0 identically), not
    # self-injective, and (L_L)^* is not L_L
    A = any_alg('T2')
    check(symbolic_gram_det(A, identity_matrix(A.F, A.d)) == 0, 'T2: not Frobenius')
    check(not self_injective(A), 'T2: not self-injective')
    check(not GAPF['iso'](GAPF['dual'](right_data(A).regular()), A.regular()),
          'T2: (L_L)^* is not L_L')
    # a self-injective algebra that is not Frobenius: QF = e Mat_3(N) e
    A = any_alg('QF')
    check(self_injective(A), 'QF: self-injective')
    check(symbolic_gram_det(A, identity_matrix(A.F, A.d)) == 0,
          'QF: not Frobenius (det = 0 identically in 9 variables)')
    check(not GAPF['iso'](GAPF['dual'](right_data(A).regular()), A.regular()),
          'QF: (L_L)^* is not L_L')

    # Exercises 2 and 3 (p. 12).
    forms = {'N3': lamN}
    for key in ('F2S3', 'F3S3', 'F2A4', 'F4A4', 'F2S4', 'N3', 'QF', 'T2', 'T3'):
        A = any_alg(key)
        D = A.data()
        socs, tops = [], []
        for P in D['P']:
            n = mdim(P)
            socs.append(GAPF['sub'](P, mtx('BasisSocle')(P)))
            tops.append(GAPF['quot'](P, libgap.IdentityMat(n, libgap(A.F)),
                                     rad(P, D['simples'])))
        crit2 = all(sum(ilist(GAPF['mult'](s, D['simples']))) == 1 for s in socs) and \
            all(not GAPF['iso'](socs[i], socs[j])
                for i in range(len(socs)) for j in range(i))
        si = self_injective(A)
        check(crit2 == si, 'Exercise 2: %s self-injective = %s' % (key, si))
        if si:
            crit3 = all(mdim(s) == mdim(t) for s, t in zip(socs, tops))
            if key in forms or A.is_group:   # a non-degenerate lam is known
                lam = forms[key] if key in forms else A.e(A.id)
                frob = gram(A, lam).is_invertible()
                assert frob
            else:
                frob = symbolic_gram_det(A, identity_matrix(A.F, A.d)) != 0
            check(crit3 == frob, 'Exercise 3: %s Frobenius = %s' % (key, frob))

    # Exercise 4: Mat_2(L) is symmetric for L = F2V4 and F3S3, with
    # lam'(X) = lam(x_11) + lam(x_22).
    for key in ('F2V4', 'F3S3'):
        A = alg(key)
        reg = [A.L[i] for i in range(A.d)]
        basis, lam2 = [], []
        for r in range(2):
            for s in range(2):
                E = matrix(A.F, 2, 2, {(r, s): 1})
                for i in range(A.d):
                    basis.append(E.tensor_product(reg[i]))
                    lam2.append(1 if (r == s and i == A.id) else 0)
        B = matrix_algebra(A.F, basis, identity_matrix(A.F, 2 * A.d), 'M2')
        G = gram(B, vector(A.F, lam2))
        check(G.is_invertible() and G == G.transpose(),
              'Exercise 4: Mat_2(%s) symmetric' % key)


# ---------------------------------------------------------------------------
# Section 1.7 (pp. 12-15).


def idempotents(A):
    return [x for x in A.V if A.mul(x, x) == x]


def section_1_7():
    # Theorem 1.7.3: the displayed identity and e - a = (a^2 - a)(1 - 2a), in
    # Z[a] (all elements involved are polynomials in a, so they commute).
    R = PolynomialRing(ZZ, 'a')
    a = R.gen()
    e = 3 * a ** 2 - 2 * a ** 3
    check(e ** 2 - e == e * (e - 1) == -(3 - 2 * a) * (1 + 2 * a) * (a ** 2 - a) ** 2,
          'Theorem 1.7.3: e^2 - e = -(3 - 2a)(1 + 2a)(a^2 - a)^2')
    check(e - a == (a ** 2 - a) * (1 - 2 * a), 'e has the image of a')
    # "if Lambda is an algebra over a field of characteristic p we can
    # instead take e_i = a^p": (a^p)^2 - a^p = (a^2 - a)^p in F_p[a].
    for p in (2, 3, 5, 7, 11, 13):
        Rp = PolynomialRing(GF(p), 'a')
        b = Rp.gen()
        check((b ** p) ** 2 - b ** p == (b ** 2 - b) ** p and
              (b ** p - b) % (b ** 2 - b) == 0,
              'a^p variant of Theorem 1.7.3, p = %d' % p)
    # The lifting step on all elements a of F3S3 and F2A4 with a^2 - a in
    # N = J (J^3 = 0): two steps a -> 3a^2 - 2a^3, and a^(p^2), are
    # idempotents congruent to a modulo J.
    for key in ('F3S3', 'F2A4'):
        A = alg(key)
        J = A.data()['J']
        p = int(A.F.characteristic())
        n = 0
        for x in A.V:
            if A.mul(x, x) - x not in J:
                continue
            y = x
            for _ in range(2):
                y2 = A.mul(y, y)
                y = 3 * y2 - 2 * A.mul(y2, y)
            assert A.mul(y, y) == y and y - x in J
            z = x
            for _ in range(2):
                zz = z
                for _ in range(p - 1):
                    zz = A.mul(zz, z)
                z = zz
            assert A.mul(z, z) == z and z - x in J
            n += 1
        check(n > 0, 'Theorem 1.7.3 (N = J): %d lifts in %s' % (n, key))

    # Theorem 1.7.3 for N = 3 L in L = (Z/27)S3 (N^3 = 0): every idempotent
    # of F3S3 lifts.
    A = alg('F3S3')
    idem3 = idempotents(A)
    Z27 = ZG(A, 27)
    lifts = {}
    for x in idem3:
        f = Z27.make_idempotent(Z27.lift(x))
        assert [c % 3 for c in f] == [int(c) for c in x]
        lifts[tuple(x)] = f
    check(len(idem3) > 2, 'all %d idempotents of F3S3 lift to (Z/27)S3' % len(idem3))

    # The conjugacy part, in the author's corrected form.  e1 = an
    # idempotent of F3S3 with e2 = g e1 g^-1 != e1 (g = a 3-cycle); f1, f2
    # lifts of e1, e2 from random starting points; mu = g.
    Z = ZG(A, 27)
    g3 = [i for i in range(A.d) if A.mt[i][i] != A.id and
          A.mt[A.mt[i][i]][i] == A.id][0]
    mu = Z.g(g3)
    mu_inv = Z.g(A.inv[g3])
    cases = 0
    for x in idem3:
        e2 = A.mul(A.mul(A.e(g3), x), A.e(A.inv[g3]))
        if e2 == x:
            continue
        f1 = Z.make_idempotent(Z.add(Z.lift(x), Z.smul(3, [random.randrange(27)
                                                           for _ in range(A.d)])))
        f2 = Z.make_idempotent(Z.add(Z.lift(e2), Z.smul(3, [random.randrange(27)
                                                            for _ in range(A.d)])))
        one = Z.one
        nu = Z.add(Z.mul(Z.mul(f2, mu), f1),
                   Z.mul(Z.mul(Z.sub(one, f2), mu), Z.sub(one, f1)))
        assert Z.mul(nu, f1) == Z.mul(f2, nu)
        bracket = Z.sub(Z.add(Z.mul(f2, mu), Z.mul(mu, f1)),
                        Z.smul(2, Z.mul(Z.mul(f2, mu), f1)))
        n_ = Z.sub(one, Z.mul(mu_inv, nu))
        assert n_ == Z.mul(mu_inv, bracket)
        assert bracket == Z.mul(Z.sub(Z.mul(f2, mu), Z.mul(mu, f1)),
                                Z.sub(one, Z.smul(2, f1)))
        assert all(c % 3 == 0 for c in n_)                   # in N
        s, t = list(one), list(one)
        for _ in range(3):
            t = Z.mul(t, n_)
            s = Z.add(s, t)
        inv = Z.mul(s, mu_inv)
        assert Z.mul(inv, nu) == one and Z.mul(nu, inv) == one
        assert Z.mul(Z.mul(nu, f1), inv) == f2
        # the printed reading: 1 - nu = f2 mu + mu f1 - 2 f2 mu f1, in N
        printed_eq = Z.sub(one, nu) == bracket
        printed_in_N = all(c % 3 == 0 for c in Z.sub(one, nu))
        if cases == 0:
            refuted(printed_eq, 'Theorem 1.7.3 as printed: 1 - nu = '
                    'f2 mu + mu f1 - 2 f2 mu f1')
            refuted(printed_in_N, 'Theorem 1.7.3 as printed: 1 - nu in N')
        assert not printed_eq
        cases += 1
    check(cases > 0, 'Theorem 1.7.3 (author\'s correction): nu f1 = f2 nu, '
          '1 - mu^-1 nu = mu^-1 (f2 mu - mu f1)(1 - 2 f1) in N, inverse '
          '(1 + n + n^2) mu^-1, for %d pairs in (Z/27)S3' % cases)

    # Proposition 1.7.2, exhaustively: e, e' are conjugate iff L e = L e'
    # and L(1 - e) = L(1 - e'); and L e = L e' already implies the second
    # (Krull-Schmidt).
    for key in ('F2S3', 'F3S3', 'F2A4'):
        A = alg(key)
        D = A.data()
        ids = [x for x in idempotents(A) if x != 0 and x != A.one]
        units = [u for u in A.V if A.lmat(u).is_invertible()]
        inv = {tuple(u): A.lmat(u).solve_right(A.one) for u in units}
        orbit_of = {}
        orbits = 0
        for x in ids:
            if tuple(x) in orbit_of:
                continue
            orb = {tuple(A.mul(A.mul(u, x), inv[tuple(u)])) for u in units}
            for y in orb:
                orbit_of[y] = orbits
            orbits += 1
        reps, cls = [], {}
        for x in ids:
            key2 = []
            for y in (x, A.one - x):
                Ly = A.submodule(A.V.subspace(A.rmat(y).columns()))
                hit = [i for i, r in enumerate(reps) if GAPF['iso'](r, Ly)]
                if not hit:
                    reps.append(Ly)
                    hit = [len(reps) - 1]
                key2.append(hit[0])
            cls[tuple(x)] = tuple(key2)
        same = all((orbit_of[tuple(x)] == orbit_of[tuple(y)]) ==
                   (cls[tuple(x)] == cls[tuple(y)]) for x in ids for y in ids)
        ks = all((cls[tuple(x)][0] == cls[tuple(y)][0]) <=
                 (cls[tuple(x)][1] == cls[tuple(y)][1]) for x in ids for y in ids)
        check(same and ks, 'Proposition 1.7.2: %s, %d idempotents, %d classes'
              % (key, len(ids), orbits))

    # Corollary 1.7.4: lifting 1 = e_1 + ... + e_n (primitive, orthogonal)
    # through the chain f'_i (f'_1 = 1, f'_i a lift of e_i + ... + e_n in
    # f'_(i-1) L f'_(i-1)), for F3S4 -> (Z/27)S4 and F2A4 -> (Z/8)A4.
    for key, m in (('F3S4', 27), ('F2A4', 8)):
        A = alg(key)
        es = A.idempotents_from_pims()
        Z = ZG(A, m)
        fp = [Z.one]
        for i in range(1, len(es)):
            tail = Z.lift(sum(es[i:], A.V.zero_vector()))
            start = Z.mul(Z.mul(fp[-1], tail), fp[-1])
            f = Z.make_idempotent(start)
            assert Z.mul(fp[-1], f) == f == Z.mul(f, fp[-1])
            fp.append(f)
        fp.append([0] * A.d)
        fs = [Z.sub(fp[i], fp[i + 1]) for i in range(len(es))]
        ok = all(Z.mul(fs[i], fs[j]) == (fs[i] if i == j else [0] * A.d)
                 for i in range(len(fs)) for j in range(len(fs)))
        ok = ok and [sum(c) % m for c in zip(*fs)] == Z.one
        ok = ok and all([c % int(A.F.characteristic()) for c in f] == Z.lift(e)
                        for f, e in zip(fs, es))
        check(ok, 'Corollary 1.7.4: %d orthogonal idempotents of %s lifted mod %d'
              % (len(es), key, m))

    # Lemmas 1.7.5, 1.7.6, 1.7.8: dim_(Delta_i) Hom(P_i, M) and
    # dim_(Delta_i) Hom(M, I_(S_i)) are the multiplicity of S_i in M.
    nmod = 0
    for key in ('F3S3', 'F4A4', 'F2A4', 'F2S4', 'F3S4', 'N3', 'T2', 'QF'):
        A = any_alg(key)
        D = A.data()
        hulls = [injective_hull(A, i) for i in range(len(D['simples']))]
        for i, I in enumerate(hulls):
            soc = GAPF['sub'](I, mtx('BasisSocle')(I))
            assert GAPF['iso'](soc, D['simples'][i]), 'Soc I_S = S'
        for M in sample_modules(A):
            mu_ = ilist(GAPF['mult'](M, D['simples']))
            for i, (P, I) in enumerate(zip(D['P'], hulls)):
                assert int(GAPF['homdim'](P, M)) == mu_[i] * D['ends'][i]
                assert int(GAPF['homdim'](M, I)) == mu_[i] * D['ends'][i]
            nmod += 1
        # Lemma 1.7.5
        for i, P in enumerate(D['P']):
            for j, S in enumerate(D['simples']):
                assert int(GAPF['homdim'](P, S)) == (D['ends'][i] if i == j else 0)
    check(nmod > 50, 'Lemmas 1.7.5, 1.7.6, 1.7.8 on %d modules of 8 algebras' % nmod)

    # Theorem 1.7.7 (Landrock) over splitting fields: the multiplicity of T
    # in the n-th Loewy layer of P_S equals that of S^* in the n-th Loewy
    # layer of the right PIM P_(T^*).
    nalg = 0
    for key in ('F2S3', 'F3S3', 'F4A4', 'F3A4', 'F2S4', 'F3S4', 'F4A5', 'F2D8',
                'F2V4', 'N3', 'T2', 'T3', 'QF'):
        A = any_alg(key)
        D = A.data()
        assert all(e == 1 for e in D['ends']), 'splitting field'
        B = right_data(A)
        DB = B.data()
        r = len(D['simples'])
        star = [dual_index(A, i) for i in range(r)]
        left = [layers(D['P'][s], D['simples']) for s in range(r)]
        right = [layers(DB['P'][j], DB['simples']) for j in range(r)]
        for s in range(r):
            for t in range(r):
                Ls = left[s]
                Rt = right[star[t]]
                for n in range(max(len(Ls), len(Rt))):
                    a_ = Ls[n][t] if n < len(Ls) else 0
                    b_ = Rt[n][star[s]] if n < len(Rt) else 0
                    assert a_ == b_, (key, s, t, n)
        nalg += 1
    check(nalg == 13, 'Theorem 1.7.7 (Landrock) for all S, T, n on 13 algebras')

    # Definition 1.7.9: c_ij = dim_(Delta_i) Hom(P_i, P_j) = [P_j : S_i];
    # over a splitting field also = dim e_i L e_j.
    cart = {}
    for key in ('F2S3', 'F3S3', 'F2A4', 'F4A4', 'F3A4', 'F2S4', 'F3S4', 'F4A5',
                'F2D8', 'N3', 'T2', 'QF'):
        A = any_alg(key)
        D = A.data()
        C = A.cartan()
        r = C.nrows()
        for i in range(r):
            for j in range(r):
                assert int(GAPF['homdim'](D['P'][i], D['P'][j])) == C[i, j] * D['ends'][i]
        cart[key] = C
    A = alg('F3S3')
    es = A.idempotents_from_pims()
    tops = [t for S, P, t in A.data()['pims']]
    ok = all(A.V.subspace([A.mul(A.mul(es[a], A.e(k)), es[b]) for k in range(A.d)]
                          ).dimension() == cart['F3S3'][tops[a], tops[b]]
             for a in range(len(es)) for b in range(len(es)))
    check(ok, 'F3S3: c_ij = dim e_i L e_j (Lemma 1.3.3)')
    check(all(cart[k].is_symmetric() for k in cart if k[0] == 'F' and k != 'F2A4'),
          'Cartan matrices of group algebras over splitting fields symmetric')
    for k in cart:
        if k[0] == 'F':
            p = int(any_alg(k).F.characteristic())
            dt = cart[k].det()
            assert dt != 0 and dt == p ** (Integer(dt).valuation(p)), (k, dt)
    check(True, 'Section 1.7: Cartan matrices of group algebras non-singular, '
          'determinant a power of p (Corollaries 5.3.6, 5.7.2)')
    D = alg('F2A4').data()
    kk = [i for i, s in enumerate(D['simples']) if mdim(s) == 1][0]
    C = cart['F2A4'].matrix_from_rows_and_columns([kk, 1 - kk], [kk, 1 - kk])
    check(C == matrix(ZZ, [[2, 2], [1, 3]]),
          'F2A4 (not split): Cartan matrix [[2, 2], [1, 3]] (rows k, W), not symmetric')
    check(cart['N3'].det() == 0 and cart['N3'] == matrix(ZZ, [[1, 1], [1, 1]]),
          'N: the Cartan matrix may be singular')
    check(not cart['T2'].is_symmetric(), 'T2: Cartan matrix not symmetric')
    check(cart['QF'] == matrix(ZZ, [[1, 1], [1, 1]]),
          'QF (Morita equivalent to N): the same singular Cartan matrix')

    # Lemma 1.7.10 (Rosenberg), exhaustively: for every idempotent e with
    # e L e local and all pairs and triples of two-sided ideals,
    # e in I1 + I2 (+ I3) implies e in some Ik.  Without locality it fails
    # (F2S3: 1 is the sum of the two block idempotents).
    for key in ('F2S3', 'F3S3', 'T3', 'N3', 'F2V4'):
        A = any_alg(key)
        bim = gmod([A.lmat(g).transpose() for g in A.gens] +
                   [A.rmat(g).transpose() for g in A.gens], A.F)
        ideals = [to_sage(b, A.F, A.d).row_space() for b in mtx('BasesSubmodules')(bim)]
        assert all(A.is_left_ideal(I) and A.is_right_ideal(I) for I in ideals)
        local = []
        for x in idempotents(A):
            if x == 0:
                continue
            corner = A.V.subspace([A.mul(A.mul(x, A.e(i)), x) for i in range(A.d)])
            els = list(corner)
            nonunits = [y for y in els if not any(A.mul(y, z) == x and A.mul(z, y) == x
                                                  for z in els)]
            if len(nonunits) == A.F.order() ** A.V.subspace(nonunits).dimension():
                local.append(x)
        for x in local:
            for I1, I2 in itertools.combinations(ideals, 2):
                if x in I1 + I2:
                    assert x in I1 or x in I2
            for I1, I2, I3 in itertools.combinations(ideals, 3):
                if x in I1 + I2 + I3:
                    assert x in I1 or x in I2 or x in I3
        check(len(local) > 0, 'Lemma 1.7.10 on %s: %d local idempotents, %d '
              'two-sided ideals' % (key, len(local), len(ideals)))
    A = alg('F2S3')
    bim = gmod([A.lmat(g).transpose() for g in A.gens] +
               [A.rmat(g).transpose() for g in A.gens], A.F)
    ideals = [to_sage(b, A.F, A.d).row_space() for b in mtx('BasesSubmodules')(bim)]
    check(not all(A.one in I1 or A.one in I2 for I1, I2 in
                  itertools.combinations(ideals, 2) if A.one in I1 + I2),
          'Lemma 1.7.10 needs e L e local (e = 1 in F2S3 fails)')


# ---------------------------------------------------------------------------
# Section 1.8 (pp. 15-17).


def central_idempotents(A, Zspace=None):
    """All idempotents of the centre (enumerated through the structure
    constants of the centre)."""
    Z = A.center() if Zspace is None else Zspace
    zb = Z.basis()
    B = Z.basis_matrix()
    k = len(zb)
    T = [[B.solve_left(A.mul(zb[i], zb[j])) for j in range(k)] for i in range(k)]
    out = []
    for c in itertools.product(list(A.F), repeat=k):
        sq = [A.F(0)] * k
        nz = [(i, a) for i, a in enumerate(c) if a != 0]
        for i, a in nz:
            for j, b in nz:
                t = T[i][j]
                ab = a * b
                for l in range(k):
                    sq[l] += ab * t[l]
        if list(sq) == list(c):
            out.append(sum((a * zb[i] for i, a in nz), A.V.zero_vector()))
    return out


def primitive_central(A, cid):
    nz = [e for e in cid if e != 0]
    return [e for e in nz if not any(f != e and A.mul(f, e) == f for f in nz)]


def section_1_8():
    # Lemma 1.8.2: the central idempotents are exactly the sums of the
    # primitive ones (2^s of them), which are orthogonal with sum 1; the number
    # of blocks s against GAP's PrimeBlocks for splitting fields.
    def gap_blocks(G, p):
        pb = libgap.PrimeBlocks(libgap.CharacterTable(G), p)
        return len(set(ilist(pb['block'])))
    expected = {'F2S3': (S3, 2), 'F3S3': (S3, 3), 'F4A4': (A4, 2), 'F3A4': (A4, 3),
                'F2S4': (S4, 2), 'F3S4': (S4, 3), 'F4A5': (A5, 2), 'F9A5': (A5, 3),
                'F5A5': (A5, 5), 'F2D8': (D8, 2), 'F3C3': (C3, 3), 'F4C3': (C3, 2)}
    blocks = {}
    for key in list(expected) + ['F2A4', 'F2A5', 'F3A5', 'F2C7', 'N3', 'T2']:
        A = any_alg(key)
        cid = central_idempotents(A)
        prim = primitive_central(A, cid)
        s = len(prim)
        check(len(cid) == 2 ** s and sum(prim, A.V.zero_vector()) == A.one and
              all(A.mul(e, f) == 0 for e, f in itertools.combinations(prim, 2)),
              'Lemma 1.8.2: %s has %d blocks, %d central idempotents'
              % (key, s, len(cid)))
        if key in expected:
            check(s == gap_blocks(*expected[key]),
                  '%s: number of blocks = number of p-blocks (GAP)' % key)
        blocks[key] = prim
        # every PIM and every simple module lies in exactly one block, and so
        # do the composition factors of a PIM
        D = A.data()
        where = {}
        for name, M in [('S%d' % i, s_) for i, s_ in enumerate(D['simples'])] + \
                [('P%d' % i, P) for i, P in enumerate(D['P'])]:
            mats = A.allmats(M)
            ranks = [A.act(mats, e).rank() for e in prim]
            assert sorted(ranks) == [0] * (s - 1) + [mdim(M)]
            where[name] = ranks.index(mdim(M))
        for i, P in enumerate(D['P']):
            m = ilist(GAPF['mult'](P, D['simples']))
            assert all(where['S%d' % j] == where['P%d' % i] for j in range(len(m)) if m[j])
        check(True, '%s: modules and composition factors of PIMs in one block' % key)
    # the field matters: 3 and 3' of A5 are Galois conjugate over F3
    check(len(blocks['F3A5']) == 2 and len(blocks['F9A5']) == 3,
          'A5, p = 3: two blocks over F3, three over F9')

    # Proposition 1.8.4 with I = J^2: the idempotents of Z(L) and of Z(L/I)
    # correspond; every idempotent lift of a central idempotent of L/I is
    # central.  With I = J instead, Z(L/J) can have more idempotents.
    PA = product_algebra(alg('F3S3'), alg('F3C3'))
    ALG['F3S3xF3C3'] = PA
    for key in ('F3S3', 'F2S4', 'F3S4', 'F4A4', 'F2A4', 'F2D8', 'F3A4', 'F3S3xF3C3'):
        A = any_alg(key)
        J = A.data()['J']
        J2 = A.span_mul(J, J)
        Q = A.quotient(J2)
        cidQ = central_idempotents(Q)
        cidL = central_idempotents(A)
        images = {tuple(Q.proj(e)) for e in cidL}
        check(len(images) == len(cidL) == len(cidQ) and
              images == {tuple(e) for e in cidQ},
              'Proposition 1.8.4: %s, %d central idempotents mod J^2' % (key, len(cidQ)))
        for e in cidQ:
            a = Q.proj.lift(e)
            for _ in range(8):
                a2 = A.mul(a, a)
                a = 3 * a2 - 2 * A.mul(a2, a)
            assert A.mul(a, a) == a and Q.proj(a) == e
            assert all(A.mul(a, g) == A.mul(g, a) for g in A.gens)
        check(True, '%s: idempotent lifts of central idempotents of L/J^2 are '
              'central' % key)
    A = alg('F3S3')
    QJ = A.quotient(A.data()['J'])
    check(len(central_idempotents(QJ)) == 4 and len(central_idempotents(A)) == 2,
          'F3S3: I = J does not suffice (4 central idempotents mod J, 2 in L)')

    # Proposition 1.8.5: a simple module that is projective and injective is
    # the only simple module of its block B, and B = Mat_n(Delta) with
    # Delta = End(M)^op, n = dim_(Delta^op) M: the action map B -> End_k(M)
    # is injective onto the commutant of End_L(M), of dimension n^2 dim Delta.
    count = 0
    for key in ('F2S3', 'F4A5', 'F2A5', 'F3A5', 'F3S4', 'F3A4', 'F5A5', 'F2C7', 'T2'):
        A = any_alg(key)
        D = A.data()
        prim = blocks.get(key) or primitive_central(A, central_idempotents(A))
        hulls = [injective_hull(A, i) for i in range(len(D['simples']))]
        for i, S in enumerate(D['simples']):
            proj = GAPF['iso'](S, D['P'][i])
            inj = GAPF['iso'](S, hulls[i])
            if not proj:
                continue
            mats = A.allmats(S)
            b = [e for e in prim if A.act(mats, e).rank() == mdim(S)][0]
            Bsp = A.V.subspace([A.mul(b, A.e(k)) for k in range(A.d)])
            others = [j for j in range(len(D['simples'])) if j != i and
                      A.act(A.allmats(D['simples'][j]), b).rank() > 0]
            if not inj:
                check(len(others) > 0, '%s: a simple projective, non-injective '
                      'module shares its block' % key)
                continue
            dl = D['ends'][i]
            n = mdim(S) // dl
            E = [matrix(A.F, x.sage(ring=A.F)) for x in mtx('BasisModuleEndomorphisms')(S)]
            images = matrix(A.F, [A.act(mats, v).list() for v in Bsp.basis()])
            ds = mdim(S)
            comm_eqs = []
            for X in E:
                rows = []
                for r in range(ds):
                    for c in range(ds):
                        # (Y X - X Y)[r, c] as a linear form in the entries of Y
                        row = [0] * (ds * ds)
                        for k in range(ds):
                            row[r * ds + k] += X[k, c]
                            row[k * ds + c] -= X[r, k]
                        rows.append(row)
                comm_eqs += rows
            commutant = matrix(A.F, comm_eqs).right_kernel()
            check(not others and Bsp.dimension() == n * n * dl and
                  images.rank() == Bsp.dimension() and
                  images.row_space() == commutant,
                  'Proposition 1.8.5: %s, simple module of dim %d, B = Mat_%d(F_%d)'
                  % (key, ds, n, A.F.order() ** dl))
            count += 1
    check(count >= 9, 'Proposition 1.8.5 on %d blocks' % count)

    # Exercise (p. 17): a commutative Artinian ring is a direct sum of local
    # rings.  Z/n, n <= 400: the primitive idempotents e give local rings
    # e Z/n of prime power order, and Z/n = sum e Z/n; F_p[x]/(f): the number
    # of idempotents is 2^(number of distinct irreducible factors).
    for n in range(2, 401):
        ids = [x for x in range(n) if (x * x - x) % n == 0]
        nz = [x for x in ids if x]
        prim = [e for e in nz if not any(f != e and (f * e) % n == f for f in nz)]
        assert len(ids) == 2 ** len(factor(n))
        orders = sorted(len({(e * y) % n for y in range(n)}) for e in prim)
        assert orders == sorted(p ** k for p, k in factor(n))
        assert sum(prim) % n == 1
    check(True, 'Exercise 1.8: Z/n, n <= 400')
    for p in (2, 3):
        Rp = PolynomialRing(GF(p), 'x')
        polys = [Rp([random.randrange(p) for _ in range(deg)] + [1])
                 for deg in (2, 3, 4, 5) for _ in range(4)]
        for f in polys:
            d = f.degree()
            els = [Rp(list(c)) for c in itertools.product(range(p), repeat=d)]
            nid = sum(1 for a in els if (a * a - a) % f == 0)
            assert nid == 2 ** len(f.factor())
    check(True, 'Exercise 1.8: F_p[x]/(f) for 16 random f, p = 2, 3')


# ---------------------------------------------------------------------------
# Section 1.9 (pp. 17-19).


def all_group_mats(A, gen_mats, R):
    """Matrices of all group elements from generator matrices (row
    convention: m(gh) = m(h) m(g)), over the ring R."""
    n = gen_mats[0].nrows()
    mats = [None] * A.d
    mats[A.id] = identity_matrix(R, n)
    queue = [A.id]
    while queue:
        h = queue.pop(0)
        for s, gi in enumerate(A.gen_idx):
            k = A.mt[gi][h]
            if mats[k] is None:
                mats[k] = mats[h] * gen_mats[s]
                queue.append(k)
    return mats


def perm_rep(A, g):
    """Row-convention matrix of g on Z^deg: e_i -> e_(i^(g^-1))."""
    gi = A.inv[A.idx[tuple(int(a) for a in libgap.ListPerm(g, A.deg))]]
    t = A.tup[gi]
    M = matrix(ZZ, A.deg, A.deg)
    for i in range(A.deg):
        M[i, t[i] - 1] = 1
    return M


def specht_forms(A, n):
    """Integral forms (Specht modules) of all ordinary irreducibles of S_n:
    generator matrices over Z (row convention)."""
    forms = []
    for part in Partitions(n):
        rho = SymmetricGroupRepresentation(part, 'specht')
        mats = [rho.representation_matrix(Permutation(
            [int(a) for a in libgap.ListPerm(g, n)])).change_ring(ZZ)
            for g in A.group.GeneratorsOfGroup()]
        forms.append((str(part), mats))
    return forms


def reduction(F, mats):
    return gmod([m.change_ring(F) for m in mats], F)


def match_perm(X, Y):
    """Is Y obtained from X by permuting rows and columns?"""
    for pr in itertools.permutations(range(X.nrows())):
        for pc in itertools.permutations(range(X.ncols())):
            if all(X[pr[i], pc[j]] == Y[i, j] for i in range(X.nrows())
                   for j in range(X.ncols())):
                return True
    return False


def section_1_9():
    # Introduction: idempotent refinement fails over Z_(5) but holds over Z_5
    # for C4.  QC4 = Q + Q + Q(i) has 8 idempotents, all with denominators
    # prime to 5 (so in Z_(5)C4), while F5C4 has 16.
    A = alg('F2C4')  # only for the group table of C4
    g = [i for i in range(A.d) if i != A.id and A.mt[A.mt[i][i]][A.mt[i][i]] == A.id
         and A.mt[i][i] != A.id][0]
    pw = [A.id]
    for _ in range(3):
        pw.append(A.mt[g][pw[-1]])
    Fq = GF(5)
    B5 = group_algebra(C4, Fq, 'F5C4')
    id5 = idempotents(B5)
    check(len(id5) == 16, 'F5C4 has 16 idempotents')

    def vec(coeffs):  # sum coeffs[k] g^k
        v = [QQ(0)] * 4
        for k, c in enumerate(coeffs):
            v[pw[k]] += c
        return v
    prims = [vec([QQ(1) / 4] * 4), vec([QQ(1) / 4, -QQ(1) / 4, QQ(1) / 4, -QQ(1) / 4]),
             vec([QQ(1) / 2, 0, -QQ(1) / 2, 0])]
    Aq = group_algebra(C4, QQ, 'QC4')
    idq = []
    for sub in itertools.product((0, 1), repeat=3):
        idq.append(sum((vector(QQ, p) for p, s in zip(prims, sub) if s),
                       vector(QQ, [0] * 4)))
    check(all(Aq.mul(e, e) == e for e in idq) and
          all(Aq.mul(e, f) == 0 for e, f in itertools.combinations(
              [vector(QQ, p) for p in prims], 2)),
          'QC4: 8 idempotents from 3 primitive central ones')
    check(len(central_idempotents_QQ(Aq)) == 3, 'QC4 has 3 simple components')
    red = {tuple(Fq(c.numerator()) / Fq(c.denominator()) for c in e) for e in idq}
    check(len(red) == 8 and red <= {tuple(x) for x in id5},
          'only 8 of the 16 idempotents of F5C4 lift to Z_(5)C4')
    # over Z/5^10 all 16 lift, to (1/4) sum_k zeta^(-jk) g^k with zeta the
    # Teichmueller lift of 2.
    m = 5 ** 10
    Z5 = ZG(B5, m)
    zeta = Zp(5, 12).teichmuller(2)
    zi = [int((zeta ** k).lift()) % m for k in range(4)]
    inv4 = pow(4, -1, m)
    prim_t = []
    for j in range(4):
        v = [0] * 4
        for k in range(4):
            v[pw[k]] = (inv4 * zi[(-j * k) % 4]) % m
        prim_t.append(v)
    lifted = set()
    for x in id5:
        f = Z5.make_idempotent(Z5.lift(x))
        assert [c % 5 for c in f] == [int(c) for c in x]
        lifted.add(tuple(f))
    sums = set()
    for r in range(5):
        for S in itertools.combinations(range(4), r):
            v = [0] * 4
            for j in S:
                v = [(a + b) % m for a, b in zip(v, prim_t[j])]
            sums.add(tuple(v))
    check(len(lifted) == 16 and lifted == sums,
          'Z5C4: all 16 idempotents lift (mod 5^10), as Teichmueller sums')

    # Lemma 1.9.1 and Remark (iii): two O-forms of the 2-dimensional
    # representation V of S3 at p = 3 (the sum-zero sublattice A of Z^3 and
    # Z^3/Z(1,1,1)) have non-isomorphic reductions with the same composition
    # factors.
    A3 = alg('F3S3')
    D3 = A3.data()
    gens = list(S3.GeneratorsOfGroup())
    perms = [perm_rep(A3, g) for g in gens]
    BA = matrix(ZZ, [[1, -1, 0], [0, 1, -1]])           # basis of A
    formA = [BA.solve_left(BA * P) for P in perms]
    formB = []
    for P in perms:                                     # images of e1, e2 mod (1,1,1)
        rows = []
        for i in range(2):
            v = P.row(i)
            rows.append([v[0] - v[2], v[1] - v[2]])
        formB.append(matrix(ZZ, rows))
    chiA = [m_.trace() for m_ in all_group_mats(A3, [f.change_ring(QQ) for f in formA], QQ)]
    chiB = [m_.trace() for m_ in all_group_mats(A3, [f.change_ring(QQ) for f in formB], QQ)]
    check(chiA == chiB and sum(c * c for c in chiA) == 6,
          'A and B are O-forms of the same irreducible V')
    MA, MB = reduction(GF(3), formA), reduction(GF(3), formB)
    check(not GAPF['iso'](MA, MB) and
          GAPF['mult'](MA, D3['simples']) == GAPF['mult'](MB, D3['simples']),
          'Remark (iii): non-isomorphic reductions, same composition factors')

    # Theorem 1.9.4 (i): the idempotents of F3S3 lift through Z/3^i, each lift
    # reducing to the previous one (i <= 8).
    for x in idempotents(A3):
        f = ZG(A3, 3).lift(x)
        for i in range(2, 9):
            Zi = ZG(A3, 3 ** i)
            fi = Zi.make_idempotent(Zi.lift(f))
            assert [c % 3 ** (i - 1) for c in fi] == [c % 3 ** (i - 1) for c in f]
            f = fi
    check(True, 'Theorem 1.9.4 (i): compatible lifts of all idempotents of F3S3 '
          'to Z/3^8')
    # (ii): lifting a complete set of primitive orthogonal idempotents of F3S4
    # to Z/3^6 S4 by the chain of Corollary 1.7.4.
    A = alg('F3S4')
    es = A.idempotents_from_pims()
    Z = ZG(A, 3 ** 6)
    fp = [Z.one]
    for i in range(1, len(es)):
        tail = Z.lift(sum(es[i:], A.V.zero_vector()))
        fp.append(Z.make_idempotent(Z.mul(Z.mul(fp[-1], tail), fp[-1])))
    fp.append([0] * A.d)
    fs = [Z.sub(fp[i], fp[i + 1]) for i in range(len(es))]
    check(all(Z.mul(fs[i], fs[j]) == (fs[i] if i == j else [0] * A.d)
              for i in range(len(fs)) for j in range(len(fs))) and
          [sum(c) % 3 ** 6 for c in zip(*fs)] == Z.one and
          all([c % 3 for c in f] == Z.lift(e) for f, e in zip(fs, es)),
          'Theorem 1.9.4 (ii): 8 primitive orthogonal idempotents of F3S4 lifted')

    # (iii), the author's corrected proof: any idempotent lift f of a
    # primitive central idempotent e of kG is central (5 random lifts each),
    # the lifts coincide, and equal the block idempotent sum of
    # (chi(1)/|G|) sum chi(g^-1) g over the characters of the block.
    for key, G, p, k in (('F2S3', S3, 2, 12), ('F2A5', A5, 2, 8),
                         ('F3S4', S4, 3, 6), ('F5A5', A5, 5, 5)):
        A = alg(key)
        m = p ** k
        Z = ZG(A, m)
        cid = central_idempotents(A)
        prim = primitive_central(A, cid)
        tbl = libgap.CharacterTable(G)
        irr = libgap.Irr(tbl)
        pb = ilist(libgap.PrimeBlocks(tbl, p)['block'])
        cls = libgap.ConjugacyClasses(tbl)
        clidx = {}
        for ci, c in enumerate(cls):
            for x in c.AsList():
                clidx[A.idx[tuple(int(a) for a in libgap.ListPerm(x, A.deg))]] = ci
        order = A.d
        closed = {}
        for b in set(pb):
            v = [0] * A.d
            for chi_i, bi in enumerate(pb):
                if bi != b:
                    continue
                chi = [libgap.Irr(tbl)[chi_i][j] for j in range(len(cls))]
                deg = int(chi[0])
                for gidx in range(A.d):
                    val = chi[clidx[A.inv[gidx]]]
                    v[gidx] = v[gidx] + QQ(deg) / order * val.sage()
            closed[b] = [int(QQ(c).numerator() * pow(int(QQ(c).denominator()), -1, m)) % m
                         for c in v]
        for e in prim:
            fs_ = []
            for _ in range(5):
                start = Z.add(Z.lift(e), Z.smul(p, [random.randrange(m) for _ in range(A.d)]))
                f = Z.make_idempotent(start)
                assert Z.is_central(f), 'lift of a central idempotent is central'
                fs_.append(f)
            assert all(f == fs_[0] for f in fs_), 'central lifts are unique'
            assert tuple(fs_[0]) in {tuple(c) for c in closed.values()}
        check(len(prim) == len(set(pb)),
              'Theorem 1.9.4 (iii): %s, %d blocks lifted to Z/%d^%d, central, unique, '
              '= the block idempotents' % (key, len(prim), p, k))
        # the hypothesis the author dropped holds for group algebras: the
        # class sums span Z(kG) (so Z(OG) -> Z(kG) is onto)
        sums = []
        for ci, c in enumerate(cls):
            v = vector(A.F, A.d)
            for gidx, cj in clidx.items():
                if cj == ci:
                    v[gidx] = 1
            sums.append(v)
        check(A.V.subspace(sums) == A.center(), '%s: class sums span Z(kG)' % key)
    # The order L = (Z_p + p M_2(Z_p)) x Z_p (p = 3): reduction is not onto
    # on centres (Z(L) = Z_p x Z_p has image of dimension 2, Z(L/pL) has
    # dimension 5), yet the central idempotents of L/pL (four) are the
    # reductions of the central idempotents (0,0), (1,0), (0,1), (1,1) of L.
    p = 3
    # O-basis 1, pE11, pE12, pE21 of the first factor, then (0, 1)
    Ebasis = [identity_matrix(ZZ, 2), p * matrix(ZZ, [[1, 0], [0, 0]]),
              p * matrix(ZZ, [[0, 1], [0, 0]]), p * matrix(ZZ, [[0, 0], [1, 0]])]
    Bz = matrix(ZZ, [b.list() for b in Ebasis])
    F = GF(p)
    table = {}
    for i in range(4):
        for j in range(4):
            c = Bz.solve_left(vector(ZZ, (Ebasis[i] * Ebasis[j]).list()))
            assert all(x in ZZ for x in c), 'closed under products'
            table[(i, j)] = {k: F(c[k]) for k in range(4) if F(c[k]) != 0}
    table[(4, 4)] = {4: F(1)}
    Lbar = struct_algebra(F, 5, table, [1, 0, 0, 0, 1], 'Lbar')
    Zbar = Lbar.center()
    image = Lbar.V.subspace([Lbar.e(0), Lbar.e(4)])
    cidbar = central_idempotents(Lbar)
    check(Zbar.dimension() == 5 and image.dimension() == 2 and len(cidbar) == 4 and
          all(c in image for c in cidbar),
          'Theorem 1.9.4 (iii) without the dropped hypothesis: an order with '
          'Z(L) -> Z(L/pL) not onto')

    # Proposition 1.9.6: C = D^T D, with D read off the reductions of integral
    # forms (Definition 1.9.5): S3 (p = 2, 3), S4 (p = 2, 3), A4 (p = 2 over
    # F4, p = 3), and against the decomposition matrices of GAP's Brauer
    # tables (also A5, p = 2, 3, 5).
    def D_from_forms(A, forms):
        D = A.data()
        rows = [ilist(GAPF['mult'](reduction(A.F, mats), D['simples']))
                for _, mats in forms]
        return matrix(ZZ, rows)
    results = {}
    for key, n in (('F2S3', 3), ('F3S3', 3), ('F2S4', 4), ('F3S4', 4)):
        A = alg(key)
        forms = specht_forms(A, n)
        for name, mats in forms:      # absolutely irreducible ordinary forms
            chi = [m_.trace() for m_ in all_group_mats(A, [x.change_ring(QQ) for x in mats], QQ)]
            assert sum(c * c for c in chi) == A.d
        Dm = D_from_forms(A, forms)
        C = A.cartan()
        check(C == Dm.transpose() * Dm, 'Proposition 1.9.6: %s, C = D^T D' % key)
        results[key] = (Dm, C)
    # A4: the 1-dimensional forms g -> zeta_3^(+-k(g)) over Z[zeta_3], and the
    # restriction of the Specht module (3,1) of S4.
    V4n = libgap.DerivedSubgroup(A4)
    hom = libgap.NaturalHomomorphismByNormalSubgroup(A4, V4n)
    img = libgap.Image(hom)
    t = libgap.MinimalGeneratingSet(img)[0]
    expo = []
    for gg in A4.GeneratorsOfGroup():
        im = libgap.Image(hom, gg)
        expo.append([k for k in range(3) if t ** k == im][0])
    rho31 = SymmetricGroupRepresentation([3, 1], 'specht')
    m31 = [rho31.representation_matrix(Permutation([int(a) for a in libgap.ListPerm(gg, 4)]))
           for gg in A4.GeneratorsOfGroup()]
    for key, zeta in (('F4A4', F4.gen()), ('F3A4', GF(3)(1))):
        A = alg(key)
        D = A.data()
        mods = [gmod([matrix(A.F, [[1]]) for _ in expo], A.F),
                gmod([matrix(A.F, [[zeta ** k]]) for k in expo], A.F),
                gmod([matrix(A.F, [[zeta ** ((-k) % 3)]]) for k in expo], A.F),
                gmod([x.change_ring(A.F) for x in m31], A.F)]
        Dm = matrix(ZZ, [ilist(GAPF['mult'](M, D['simples'])) for M in mods])
        C = A.cartan()
        check(C == Dm.transpose() * Dm, 'Proposition 1.9.6: %s, C = D^T D' % key)
        results[key] = (Dm, C)
    for key, G, p in (('F2S3', 'S3', 2), ('F3S3', 'S3', 3), ('F2S4', 'S4', 2),
                      ('F3S4', 'S4', 3), ('F4A4', 'A4', 2), ('F3A4', 'A4', 3)):
        Dg = matrix(ZZ, [ilist(r) for r in libgap.DecompositionMatrix(
            libgap.BrauerTable(libgap.CharacterTable(G), p))])
        check(match_perm(results[key][0], Dg), '%s: D agrees with GAP\'s '
              'Brauer table up to the order of rows and columns' % key)
    for key, p in (('F4A5', 2), ('F9A5', 3), ('F5A5', 5)):
        A = alg(key)
        Dg = matrix(ZZ, [ilist(r) for r in libgap.DecompositionMatrix(
            libgap.BrauerTable(libgap.CharacterTable('A5'), p))])
        Cg = Dg.transpose() * Dg
        C = A.cartan()
        ok = any(all(C[pc[i], pc[j]] == Cg[i, j] for i in range(C.nrows())
                     for j in range(C.nrows()))
                 for pc in itertools.permutations(range(C.nrows())))
        check(ok and C.is_symmetric(), 'Proposition 1.9.6: %s, C = D^T D (GAP D)' % key)

    # Remark (iv): the path algebra of 1 -> 2 over O has Cartan matrix
    # [[1, 0], [1, 1]] (not symmetric); its K-form is not semisimple.
    T = any_alg('T2')
    check(T.data()['J'].dimension() == 1 and not T.cartan().is_symmetric(),
          'Remark (iv): T2 (= path algebra of A_2), non-symmetric Cartan matrix')

    # Remark (v), with the author's dim_K: the multiplicity of V_i in Q^_j is
    # d_ij dim_k End(S_j) / dim_K End(V_i), and
    # c_ij = sum_k d_ki d_kj dim_k End(S_j) / dim_K End(V_k).
    # (a) Z_3 C3: V_1 = K, V_2 = K(zeta_3) (End of dimension 2: x^2 + x + 1 is
    # irreducible over Q_3 as -3 is not a square), k = F3, one simple module.
    check(not Qp(3, 20)(-3).is_square() and not Qp(2, 20)(-3).is_square(),
          '-3 is not a square in Q_3, Q_2: x^2 + x + 1 is irreducible there')
    A = alg('F3C3')
    D = A.data()
    gC3 = list(C3.GeneratorsOfGroup())
    zeta_mat = matrix(ZZ, [[0, 1], [-1, -1]])        # multiplication by zeta_3
    d = matrix(ZZ, [ilist(GAPF['mult'](reduction(GF(3), [matrix(ZZ, [[1]])]), D['simples'])),
                    ilist(GAPF['mult'](reduction(GF(3), [zeta_mat]), D['simples']))])
    endS, endV = D['ends'], [1, 2]
    C = A.cartan()
    mult_Q = [d[i, 0] * endS[0] / endV[i] for i in range(2)]
    check(d == matrix(ZZ, [[1], [2]]) and C == matrix(ZZ, [[3]]) and
          mult_Q == [1, 1] and C[0, 0] == sum(d[k, 0] ** 2 * endS[0] / endV[k]
                                              for k in range(2)),
          'Remark (v): Z_3 C3, KC3 = V_1 + V_2, c_11 = 1 + 4/2 = 3')
    # (b) Z_2 A4 (K = Q_2, k = F2, neither splitting): V_1 = K, V_2 = the
    # 2-dimensional form Z[zeta_3] of omega + omega-bar (End = Q_2(zeta_3)),
    # V_3 = Specht (3,1); S_1 = k, S_2 = W (End F4).  The characters of the
    # lifts Q_j are the sums over Galois orbits of the split projective
    # characters (D of F4A4).
    A = alg('F2A4')
    D = A.data()
    kk = [i for i, s in enumerate(D['simples']) if mdim(s) == 1][0]
    ww = 1 - kk
    forms = [[matrix(ZZ, [[1]]) for _ in expo], [zeta_mat ** k for k in expo], m31]
    d = matrix(ZZ, [ilist(GAPF['mult'](reduction(GF(2), f), D['simples'])) for f in forms])
    d = d.matrix_from_columns([kk, ww])
    endS = [D['ends'][kk], D['ends'][ww]]
    endV = [1, 2, 1]
    check(d == matrix(ZZ, [[1, 0], [0, 1], [1, 1]]) and endS == [1, 2],
          'Z_2 A4: d = [[1,0],[0,1],[1,1]], End(S) of dimensions 1, 2')
    # split data: rows 1, omega, omega-bar, 3; columns k, omega, omega-bar
    Dsplit = results['F4A4'][0]
    D4 = alg('F4A4').data()
    triv = [i for i, s in enumerate(D4['simples'])
            if all(m_[0, 0] == 1 for m_ in alg('F4A4').allmats(s))][0]
    others = [i for i in range(3) if i != triv]
    # projective characters, as multiplicity vectors over (1, omega, omega-bar, 3)
    Phi_k = Dsplit.column(triv)
    Phi_W = Dsplit.column(others[0]) + Dsplit.column(others[1])
    # the K-irreducibles as vectors over the same basis
    psi = [vector(ZZ, [1, 0, 0, 0]), vector(ZZ, [0, 1, 1, 0]), vector(ZZ, [0, 0, 0, 1])]
    Mpsi = matrix(ZZ, psi)
    m_k = Mpsi.solve_left(Phi_k)
    m_W = Mpsi.solve_left(Phi_W)
    formula = [[d[i, j] * endS[j] / endV[i] for j in range(2)] for i in range(3)]
    check([[m_k[i], m_W[i]] for i in range(3)] == formula,
          'Remark (v): multiplicities of V_i in the lifts Q_j (Z_2 A4)')
    C = A.cartan().matrix_from_rows_and_columns([kk, ww], [kk, ww])
    Cf = matrix(QQ, 2, 2, lambda i, j: sum(d[k, i] * d[k, j] * endS[j] / endV[k]
                                           for k in range(3)))
    check(C == Cf and C == matrix(ZZ, [[2, 2], [1, 3]]),
          'Remark (v): c_ij = sum_k d_ki d_kj dim End(S_j)/dim End(V_k) (Z_2 A4)')
    check(Cf != matrix(QQ, 2, 2, lambda i, j: sum(d[k, i] * d[k, j] for k in range(3))),
          'Remark (v): without the factor the formula fails (non-split case)')


def main():
    section_1_1()
    section_1_2()
    section_1_3()
    section_1_4()
    section_1_5()
    section_1_6()
    section_1_7()
    section_1_8()
    section_1_9()
    print(f'ok chapter-1: {COUNT[0]} checks')


if __name__ == '__main__':
    main()
