"""Exact checks of Chapter 5, Sections 5.1-5.11 (Sage, with GAP via libgap).

Benson, *Representations and Cohomology I*, second edition (1998),
Chapter 5 "Representation rings and Burnside rings", the introduction and
Sections 5.1-5.11, printed pp. 171-200.  Our files:
content/05-00-representation-rings.typ ... content/05-11-non-singularity.typ.

Everything is exact: integers, rationals, the universal cyclotomic field
(character values), finite fields; GAP through libgap for subgroup lattices,
character tables (CTblLib for A5, S5, L3(2) = PSL(2,7) with their groups
stored), Brauer tables, tables of marks and the MeatAxe (modules over finite
fields given by matrices, decompositions, isomorphism tests).  Modules of
cyclic p-groups are Jordan blocks; their tensor products, Hom spaces and
induced modules are computed by ranks over GF(p) in GAP.  Expected values
are the book's statements, tables and formulas, read off the printed pages
(page and label named in each message); where the printed text is
corrected, the printed reading is kept as a refuted check.

Checked here (by section):

5.1-5.3 (pp. 172-177), section_5_1_to_5_3 and section_cyclic_green_rings
  * a(G) commutative, associative, identity J_1 (GF(p)C_q, q <= 9); res a
    ring homomorphism and ind(x.res y) = ind(x).y for C_q > C_(q/p).
  * The author's added sentence (p. 173): K_0(GF(p)C_p) = ZZ[P] with
    P (x) P ~ p.P has no identity (p = 2, 3, 5).
  * 5.2 for S3, D8, Q8, A4, S4, A5, SL(2,3), C3:C4, S3xC3, PSL(2,7), C7:C3,
    S5: number of irreducibles = number of classes, sum of squares, the
    character table is non-singular (Lemma 5.2.2, Proposition 5.2.3),
    orthogonality, products of characters are characters; dim Hom between
    permutation modules = number of double cosets.
  * Lemma 5.3.1: the printed proof is refuted (freeness on <g'>: C4 and
    C4 x C3 with p = 3, dimension 2 resp. 6 not divisible by 4; the
    decomposition on <g>: S3 x C3 and S3 x C3 x C7 with p = 7, dimension
    3 resp. 21 against 1 + 6r resp. 7 + 6r).  The corrected count
    t_y(x) = |{z : z^-1 y z = g}| for every p'-element g and p-regular y of
    the 12 groups and primes of MODULAR (induced characters), and with the
    Brauer characters of the induced modules over GF(4), GF(9), GF(16) for
    S3, A4, S4, A5 and over GF(7), GF(9) for the counterexamples.
  * Brauer tables of the 12 groups at 27 pairs (G, p): Corollary 5.3.5,
    Theorem 5.3.3 (non-singular Brauer table), decomposition matrices,
    C = D^T D non-singular with det a power of p (Corollary 5.3.6,
    Corollary 5.7.2, Theorem 5.9.3), elementary divisors of C powers of p
    dividing |G|_p, (dim P).1 and |G|_p.1 in Im(c) (proof of 5.9.3),
    projective indecomposables with independent Brauer characters,
    e = c^-1(1) has Brauer character 1, d surjective (Corollary 5.6.5).
  * Proposition 5.3.4: t_g(F(M)) = t_(g^p)(M) and "F(M) ~ M iff M is
    defined over GF(p)" for the absolutely irreducible modules over
    GF(p^f) of A5, A4, S4, SL(2,3), C7:C3, PSL(2,7), C3:C4.
5.4 (pp. 177-183), section_5_4
  * The Example (p. 178): every entry of the multiplication table of
    b(S3) from orbits of products of G-sets; the four ring homomorphisms
    (the printed table) are all solutions of its relations and are the f_H.
  * Burnside's table of marks of A4 (p. 179) by counting fixed points and
    against GAP's TableOfMarks; the matrix congruence of p. 180 (second
    matrix from its description, moduli |N_G(H) : H|, unitriangular).
  * For all 74 groups of order <= 24, A5, S5, SL(2,5), PSL(2,7): table of
    marks lower triangular with diagonal |N_G(H) : H|, cokernel of order
    prod |N_G(H) : H|; Lemma 5.4.1 (first 40 groups); Theorem 5.4.6 (the
    congruences, with the author's corrected subscripts, define the image)
    and the p-primary form; Theorem 5.4.7 (i), (ii) and Corollary 5.4.8
    (i), (ii) (classes of H^(infinity), of O^p(H); exhaustively over all
    idempotents for <= 12 resp. <= 9 classes); soluble iff 0, 1 only.
  * f_H multiplicative on products of G-sets (S3, A4, D8, Q8, D12,
    S3 x C3, S4); Theorem 5.4.2 (all ring homomorphisms are f_H) for S3,
    A4, D8 by solving the relations.
  * Lemma 5.4.9 (i)-(iii) (Mackey formula) with G-sets and Theorem 5.4.10
    (i), (ii) for S3, D8, Q8, A4, S4, S3 x C3, A5; Corollary 5.4.11 for
    A(GF(p)C_q) with H = C_(q/p).
5.5, 5.6 (pp. 183-190), section_5_5_and_5_6_trivial_source and
section_5_6_characters
  * Trivial source modules (MeatAxe: summands of all F[G/H]) of S3 (p = 2,
    3), A4 (2, 3), S4 (2, 3), D8, C3:C4 (2, 3), A5 (5), S3 x C3 (3): their
    number equals the number of classes of pairs (H, g) (Corollary 5.5.5);
    the species table s_(H,g) computed from the definition is non-singular
    (Proposition 5.5.4); s_(H,g) multiplicative on tensor products (of
    dimension <= 64); s_(H,g)(k[X]) = |X^H| (the map lambda of p. 188).
  * Conlon's theorem 5.6.8 in a(G, Triv) (and that every maximal class of
    p-hypo-elementary subgroups is needed, p. 189), Corollary 5.6.9,
    Dress' theorem 5.6.11 over ZZ and over ZZ_(q) for every q.
  * Artin (5.6.1) over QQ and R(G)[|G|^-1] (p. 187), the diagram of its
    proof (phi(e_H) is the indicator of the generators of conjugates of H),
    Proposition 5.6.3, Theorem 5.6.4 in characteristic 0 for 18 groups and
    with Brauer characters for the 27 pairs (G, p); Witt-Berman (5.6.7) for
    k = CC and k = RR (Frobenius-Schur indicators).  Definition 5.6.6 as
    corrected (eps of order |O^q(H)|): the CC-elementary subgroups are
    the direct products of a q-group and a cyclic q'-group (p. 188); read
    with eps of order |H| and every integer t (the author's condition with
    the printed |H|) only the cyclic subgroups qualify and Witt-Berman
    fails for V4, C2^3, C2^4, Q8, D8 (refuted).  "phi kills the idempotent
    iff H_0 is non-cyclic" (p. 186): true in characteristic 0, refuted in
    characteristic 2 for S3, q = 3; the corrected "if" for all p.
5.8 (pp. 191-194)
  * GF(p)C_q (q <= 9), S3 (p = 3), A4 (3), C3:C4 (3), D10 (5): A(kG) has
    no non-zero nilpotents (trace form of the Green ring non-degenerate;
    Theorem 5.8.7), A(G; p) is an ideal and A(G)/A(G; p) is reduced
    (Lemma 5.8.3, Theorem 5.8.5), Proposition 5.8.1 for C_q (the printed
    statement without "indecomposable" refuted by M = J_1 + J_(p-1)),
    Lemma 5.8.6 (uniserial, indecomposable on D, A(H; p) = Im(ind)).
5.9 (pp. 194-196), section_5_9
  * The Moebius identity for d <= 60; in characteristic 0 the eps^j
    eigenspaces of M^(x n) (n = 2..6) for the irreducibles of 9 groups are
    modules, agree for equal orders of eps^j, and psi^n(M) has character
    chi(g^n) (Proposition 5.9.2).  For GF(p)C_p (p = 2, 3, 5, 7): the
    eigenspaces of J_m^(x n) of the same order are isomorphic, psi^n is
    multiplicative (5.9.1 (ii)), psi^2 psi^2 = psi^4 (p = 5),
    psi^2 psi^3 = psi^6 (p = 7, m <= 3) (the author's 5.9.1 (iii)).
    Proposition 5.9.2 with modules over GF(4), GF(9), GF(16) of S3, A4,
    A5, S4.  Proposition 5.9.4 (the Brauer lift; R(KG)^psi -> R(kG)^psi
    bijective, = R(k_0 G) from the irreducible GF(q)-modules) for 12 pairs
    and q = p, p^2; the closing remark (g -> t_(g_p')(M) is a generalised
    character).
5.10, 5.11 (pp. 196-200), section_cyclic_green_rings and
section_forms_and_duality
  * For C_q (q <= 9), S3, A4, C3:C4, D10 (all indecomposables; the
    projective indecomposables are uniserial) and 16 test modules of
    GF(2)V4: Lemma 5.10.2 (rank of the trace = multiplicity of P_k in
    M* (x) N = (u.[M], [N]), symmetric), Lemma 5.10.3 (u v = 1),
    Proposition 5.10.4 (i)-(iii), Lemma 5.10.5 and the Schanuel
    isomorphism of its proof (V4 > C2: the displayed sequences give
    res(v) = v, the corrected "second"), Proposition 5.10.6 (C_q > C_(q/p),
    V4 > C2).  The printed proof of Lemma 5.10.2 with Hom_kG(M, N) refuted.
  * Theorem 5.11.1: tau_0 is the dual basis (from the inverse of the
    Hom matrix: [N] - [Rad N] for N projective, [N] + [Omega^2 N] - [E]
    with dim E = dim N + dim Omega^2 N otherwise); Theorem 5.11.3 (corrected
    sequence 0 -> Omega N -> X -> Omega^-1 N -> 0): tau_1 = u.tau_0 =
    [X] - [Omega^-1 N] - [Omega N], [S] for P_S; Corollary 5.11.2.  For V4:
    the duality for k, P, the E's (d = 1) and W (d = 2) on 16 test modules;
    the printed last sentence of 5.11.1 refuted (x = [W] in GF(2)V4,
    x = [S] in GF(2)C3: (x, tau_0 x) = 2 = d), the printed sequence of
    5.11.3 refuted (dim Omega^3 k = 7 != 3 = dim Omega^-1 k, and the
    duality fails), and "u.tau_0[N] = ... + [Omega^-1(E)] without working
    modulo projectives" (p. 200) refuted for N = k (u.tau_0[k] has the
    summand P).

Literature for the corrected readings: Curtis-Reiner, Methods of
Representation Theory I (1981), Lemma (21.28) (Brauer character of
an induced module) and Section 21A (K-elementary subgroups,
u x u^-1 = x^t for some t in Im(K)).

What is NOT established.  No general theorem of the chapter is proved:
every check concerns the listed groups, primes, fields and modules.  The
almost split sequences of V4 used for tau_0 and tau_1 (0 -> Omega^2 k ->
2 Omega k -> k -> 0, the tubes of rank one, Proposition 4.12.7) are taken
from the theory, not computed; the checks show that the dualities hold with
them on the 16 test modules only.  For S3, A4, C3:C4, D10 the middle terms
of almost split sequences are derived from Theorem 5.11.1 itself (so the
check there is the non-singularity and the shape of tau_0, tau_1).
Definition 5.6.6 in characteristic p is not tested (the theorems are
checked for k = CC, RR only).  Theorem 5.7.1 is checked only for X a point
(the Cartan matrices).  Nothing here compares our text with the printed
book.

Run with:  sage -python checks/sage/chapter-5.py
"""
import itertools

from sage.all import (
    QQ, ZZ, PolynomialRing, UniversalCyclotomicField, factor, gcd, libgap,
    matrix, moebius, prod, vector,
)

SCOPE = 'chapter-5'
COUNT = [0]
UCF = UniversalCyclotomicField()


def check(cond, what):
    """One check of a statement of the book; fails loudly."""
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    """The printed reading, kept beside the corrected one: it must fail."""
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


def ilist(L):
    return [int(x) for x in L]


def imat(L):
    return matrix(ZZ, [[int(x) for x in row] for row in L])


def nonneg_int(x):
    """x (in the universal cyclotomic field) is an integer >= 0."""
    return x.is_rational() and QQ(x) in ZZ and QQ(x) >= 0


def cyc(x):
    """A GAP cyclotomic as an element of Sage's universal cyclotomic field."""
    return UCF(x.sage()) if hasattr(x, 'sage') else UCF(x)


# ===========================================================================
# GAP functions.  Groups are permutation or pc groups of GAP; subgroups are
# listed by representatives of their conjugacy classes, sorted by order.
# ===========================================================================

gap('BensonCh5 := 0')
gap(r'''BensonCh5 := rec(
  classes := function(G)
    local cl;
    cl := List(ConjugacyClassesSubgroups(G), Representative);
    SortBy(cl, Size);
    return cl;
  end,

  # M[i][j] = f_(H_j)(G/H_i) = number of cosets x H_i fixed by H_j, counted
  # directly: t H_i (t^-1 a right transversal element) is fixed by K iff
  # t K t^-1 <= H_i.
  marks := function(G, reps)
    local n, M, i, j, T, H, K;
    n := Length(reps);
    M := NullMat(n, n);
    for i in [1 .. n] do
      H := reps[i];
      T := RightTransversal(G, H);
      for j in [1 .. n] do
        K := reps[j];
        M[i][j] := Number(T, t -> ForAll(GeneratorsOfGroup(K),
                                         k -> t * k * t^-1 in H));
      od;
    od;
    return M;
  end,

  whichclass := function(G, reps, L)
    local i;
    for i in [1 .. Length(reps)] do
      if Size(reps[i]) = Size(L) and IsConjugate(G, reps[i], L) then
        return i;
      fi;
    od;
    return fail;
  end,

  # H_j conjugate to a subgroup of H_i (tested on conjugates of H_j)
  subconj := function(G, reps, i, j)
    local H, K;
    H := reps[i]; K := reps[j];
    return ForAny(RightTransversal(G, Normalizer(G, K)),
                  t -> IsSubset(H, K^t));
  end,

  normindex := function(G, H)
    return Index(Normalizer(G, H), H);
  end,

  # c[class] = #{k in N : <H, k> in class} / |H| for N = N_G(H), or for the
  # preimage N of a Sylow p-subgroup of N_G(H)/H; returns [c, |N : H|].
  congruence := function(G, reps, i, p)
    local H, N, hom, c, k, j;
    H := reps[i];
    N := Normalizer(G, H);
    if p <> 0 then
      hom := NaturalHomomorphismByNormalSubgroup(N, H);
      N := PreImage(hom, SylowSubgroup(Image(hom), p));
    fi;
    c := List(reps, x -> 0);
    for k in N do
      j := BensonCh5.whichclass(G, reps, ClosureGroup(H, k));
      c[j] := c[j] + 1;
    od;
    return [c / Size(H), Index(N, H)];
  end,

  # pairs [i, j, |K : H|] with H = H_i normal in K = <H, k>, k in N_G(H),
  # K/H cyclic and K <> H (K in the class j)
  cyclic_edges := function(G, reps)
    local E, i, H, k, K;
    E := [];
    for i in [1 .. Length(reps)] do
      H := reps[i];
      for k in Normalizer(G, H) do
        K := ClosureGroup(H, k);
        if Size(K) > Size(H) then
          AddSet(E, [i, BensonCh5.whichclass(G, reps, K), Index(K, H)]);
        fi;
      od;
    od;
    return E;
  end,

  perfect_residuum_class := function(G, reps)
    return List(reps, H -> BensonCh5.whichclass(G, reps, PerfectResiduum(H)));
  end,

  # O^p(H): generated by the p'-elements of H
  Op_class := function(G, reps, p)
    return List(reps, H -> BensonCh5.whichclass(G, reps,
      Subgroup(H, Filtered(AsList(H), x -> Order(x) mod p <> 0))));
  end,

  # the G-set G/H_i x G/H_j (right cosets) decomposed into orbits: counts
  # of the classes of the stabilisers
  # X acting on (X/U) x (Y/V) (right cosets, Y >= X), as a homomorphism to
  # a permutation group on [1 .. a + b]; returns [hom, a, b]
  pairaction := function(X, U, Y, V)
    local act, a, b, imgs;
    # FactorCosetAction needs a proper subgroup
    act := function(A, W)
      local f;
      if Index(A, W) = 1 then return x -> (); fi;
      f := FactorCosetAction(A, W);
      return x -> Image(f, x);
    end;
    a := Index(X, U); b := Index(Y, V);
    imgs := List(GeneratorsOfGroup(X), x -> act(X, U)(x) *
      PermList(Concatenation([1 .. a], ListPerm(act(Y, V)(x), b) + a)));
    return [GroupHomomorphismByImages(X, Group(imgs, ()),
                                      GeneratorsOfGroup(X), imgs), a, b];
  end,

  # orbits of X on (X/U) x (Y/V): counts of the G-classes of stabilisers
  pairorbits := function(G, reps, X, U, Y, V)
    local pa, phi, im, c, o, st, l;
    pa := BensonCh5.pairaction(X, U, Y, V);
    phi := pa[1]; im := Image(phi);
    c := List(reps, x -> 0);
    for o in Orbits(im, Cartesian([1 .. pa[2]], pa[2] + [1 .. pa[3]]),
                    OnPairs) do
      st := PreImage(phi, Stabilizer(im, o[1], OnPairs));
      l := BensonCh5.whichclass(G, reps, st);
      c[l] := c[l] + 1;
    od;
    return c;
  end,

  # the G-set G/H_i x G/H_j decomposed into orbits
  product := function(G, reps, i, j)
    return BensonCh5.pairorbits(G, reps, G, reps[i], G, reps[j]);
  end,

  # Lemma 5.4.9 (ii): ind_(H,G)(H/L x res(G/K)) and G/L x G/K, both as
  # lists of counts of G-classes of stabilisers
  frobenius := function(G, reps, H, L, K)
    return [BensonCh5.pairorbits(G, reps, H, L, G, K),
            BensonCh5.pairorbits(G, reps, G, L, G, K)];
  end,

  # Lemma 5.4.9 (iii) for a = [K/L]: the H-orbits of G/L (stabilisers
  # H cap x L x^-1) against the right hand side of the Mackey formula
  # (J = H cap gKg^-1 acting on gK/gL); lists of stabilisers.
  mackey := function(G, H, K, L)
    local lhs, rhs, x, g, J, Kg, Lg, y;
    lhs := List(DoubleCosetRepsAndSizes(G, H, L),
                d -> Intersection(H, L^(d[1]^-1)));
    rhs := [];
    for g in List(DoubleCosetRepsAndSizes(G, H, K), d -> d[1]) do
      Kg := K^(g^-1); Lg := L^(g^-1);
      J := Intersection(H, Kg);
      for y in List(DoubleCosetRepsAndSizes(Kg, J, Lg), d -> d[1]) do
        Add(rhs, Intersection(J, Lg^(y^-1)));
      od;
    od;
    return [lhs, rhs];
  end,

  classcount := function(H, hreps, Ls)
    local c, L, j;
    c := List(hreps, x -> 0);
    for L in Ls do
      j := BensonCh5.whichclass(H, hreps, L);
      c[j] := c[j] + 1;
    od;
    return c;
  end
)''')
B = gap('BensonCh5')


class Burnside:
    """b(G) through the table of marks M (rows G/H_i, columns f_(H_j))."""

    def __init__(self, G, name):
        self.G, self.name = G, name
        self.reps = B['classes'](G)
        self.n = len(self.reps)
        self.M = imat(B['marks'](G, self.reps))
        self.sizes = [int(H.Size()) for H in self.reps]
        self.d = [int(B['normindex'](G, H)) for H in self.reps]
        self.order = int(G.Size())

    def coords(self, marks):
        """Coefficients in the basis [G/H_i] of the element with the given
        marks (a vector over QQ)."""
        return vector(QQ, marks) * self.M.change_ring(QQ).inverse()

    def which(self, L):
        return int(B['whichclass'](self.G, self.reps, L))


def small_groups(maxorder):
    out = []
    for n in range(2, maxorder + 1):
        for i in range(1, int(libgap.NumberSmallGroups(n)) + 1):
            out.append((libgap.SmallGroup(n, i), 'SmallGroup(%d,%d)' % (n, i)))
    return out


# ===========================================================================
# Section 5.4: G-sets and the Burnside ring
# ===========================================================================


def section_5_4():
    # ---- The Example: b(S3), p. 178 --------------------------------------
    S3 = Burnside(libgap.SymmetricGroup(3), 'S3')
    check(S3.sizes == [1, 2, 3, 6],
          'Example p. 178: S3 has four classes of subgroups, 1, C2, C3, S3, '
          'so G/H has 6, 3, 2, 1 points (c, b, a, 1)')
    # basis of the book: 1 = G/S3 (1 point), a = G/C3 (2), b = G/C2 (3),
    # c = G/1 (6); our class indices 3, 2, 1, 0.
    name = {3: '1', 2: 'a', 1: 'b', 0: 'c'}
    idx = {v: k for k, v in name.items()}
    printed = {  # the multiplication table of p. 178, row x column
        ('1', '1'): {'1': 1}, ('1', 'a'): {'a': 1}, ('1', 'b'): {'b': 1},
        ('1', 'c'): {'c': 1},
        ('a', 'a'): {'a': 2}, ('a', 'b'): {'c': 1}, ('a', 'c'): {'c': 2},
        ('b', 'b'): {'b': 1, 'c': 1}, ('b', 'c'): {'c': 3},
        ('c', 'c'): {'c': 6},
    }
    for x, y in itertools.product('1abc', repeat=2):
        key = (x, y) if (x, y) in printed else (y, x)
        got = ilist(B['product'](S3.G, S3.reps, idx[x] + 1, idx[y] + 1))
        exp = [0] * 4
        for z, m in printed[key].items():
            exp[idx[z]] = m
        check(got == exp,
              'Example p. 178: %s.%s = %s in b(S3) (orbits of the product of '
              'the G-sets)' % (x, y, printed[key]))
    # The ring homomorphisms b(S3) -> CC: all solutions of the relations of
    # the table (f(1) = 1).
    R = PolynomialRing(QQ, 'fa,fb,fc')
    fa, fb, fc = R.gens()
    f = {'1': R(1), 'a': fa, 'b': fb, 'c': fc}
    rels = []
    for (x, y), val in printed.items():
        rels.append(f[x] * f[y] - sum(m * f[z] for z, m in val.items()))
    I = R.ideal(rels)
    check(I.dimension() == 0 and I.vector_space_dimension() == 4,
          'Example p. 178: the relations of the table define 4 points '
          '(counted with multiplicity) in CC^3')
    sols = sorted((int(s[fc]), int(s[fb]), int(s[fa]), 1)
                  for s in I.variety(QQ))
    printed_cols = sorted([(6, 3, 2, 1), (0, 1, 0, 1), (0, 0, 2, 1),
                           (0, 0, 0, 1)])
    check(sols == printed_cols,
          'Example p. 178: the four homomorphisms (columns of the table, '
          'values on c, b, a, 1) are (6,3,2,1), (0,1,0,1), (0,0,2,1), '
          '(0,0,0,1), and they are all of them')
    for j, H in enumerate(['1', 'C2', 'C3', 'S3']):
        col = tuple(int(S3.M[idx[z], j]) for z in 'cba1')
        check(col in printed_cols,
              'p. 178: the column of the table %s is f_H for H = %s (fixed '
              'points of H)' % (col, H))
    check(sorted(tuple(int(S3.M[idx[z], j]) for z in 'cba1')
                 for j in range(4)) == printed_cols,
          'p. 178: the table of homomorphisms is the table of the f_H')

    # ---- A4: Burnside's table of marks, p. 179 --------------------------
    A4 = Burnside(libgap.AlternatingGroup(4), 'A4')
    printed_tom = matrix(ZZ, [[12, 0, 0, 0, 0], [6, 2, 0, 0, 0],
                              [4, 0, 1, 0, 0], [3, 3, 0, 3, 0],
                              [1, 1, 1, 1, 1]])
    check(A4.sizes == [1, 2, 3, 4, 12],
          'Remark p. 179: subgroups of A4 up to conjugacy 1, C2, C3, V4, A4')
    check(A4.M == printed_tom,
          'Remark p. 179: Burnside\'s table of marks of A4 (fixed points '
          'counted)')
    tom = libgap.TableOfMarks(libgap.AlternatingGroup(4))
    marks, subs = tom.MarksTom(), tom.SubsTom()
    T = matrix(ZZ, 5, 5)
    for i in range(5):
        for j, m in zip(ilist(subs[i]), ilist(marks[i])):
            T[i, j - 1] = m
    check(ilist(tom.OrdersTom()) == [1, 2, 3, 4, 12] and T == printed_tom,
          'Remark p. 179: the table of marks of A4 equals GAP\'s '
          'TableOfMarks')

    # ---- Fixed point homomorphisms, Lemma 5.4.1, Theorem 5.4.2 ----------
    groups = small_groups(24) + [
        (libgap.AlternatingGroup(5), 'A5'), (libgap.SymmetricGroup(5), 'S5'),
        (libgap.eval('SL(2,5)'), 'SL(2,5)'),
        (libgap.eval('PSL(2,7)'), 'PSL(2,7)'),
    ]
    data = [Burnside(G, name) for G, name in groups]
    for Bg in data:
        n, M = Bg.n, Bg.M
        tri = all(M[i, j] == 0 for i in range(n) for j in range(i + 1, n))
        check(tri and all(M[i, i] == Bg.d[i] for i in range(n)),
              '%s: with subgroups in non-decreasing order the matrix of '
              'sum f_H is lower triangular with diagonal |N_G(H) : H| '
              '(p. 179)' % Bg.name)
        check(abs(M.det()) == prod(Bg.d)
              and prod(M.elementary_divisors()) == prod(Bg.d),
              '%s: the cokernel of sum f_H : b(G) -> ZZ^n has order '
              'prod |N_G(H) : H| = %d (p. 179)' % (Bg.name, prod(Bg.d)))
    for Bg in data[:40]:
        ok = all((Bg.M[i, j] != 0)
                 == bool(B['subconj'](Bg.G, Bg.reps, i + 1, j + 1))
                 for i in range(Bg.n) for j in range(Bg.n))
        check(ok, '%s: Lemma 5.4.1, f_H(G/K) != 0 iff H is conjugate to a '
              'subgroup of K' % Bg.name)
    # f_H multiplicative on G-sets: products of transitive G-sets decomposed
    # into orbits
    for Bg in [S3, A4] + [b for b in data if b.name in (
            'SmallGroup(8,3)', 'SmallGroup(8,4)', 'SmallGroup(12,4)',
            'SmallGroup(24,12)', 'SmallGroup(18,3)')]:
        ok = True
        for i, j in itertools.combinations_with_replacement(range(Bg.n), 2):
            c = vector(ZZ, ilist(B['product'](Bg.G, Bg.reps, i + 1, j + 1)))
            lhs = c * Bg.M
            rhs = vector(ZZ, [Bg.M[i, l] * Bg.M[j, l] for l in range(Bg.n)])
            ok = ok and lhs == rhs
        check(ok, '%s: |(X x Y)^H| = |X^H| |Y^H| for all transitive X, Y '
              '(orbits of X x Y), so each f_H is a ring homomorphism '
              '(p. 178)' % Bg.name)
    # every ring homomorphism is some f_H: A4 and D8 by solving the
    # relations of the multiplication table
    for Bg in [A4] + [b for b in data if b.name == 'SmallGroup(8,3)']:
        n = Bg.n
        R = PolynomialRing(QQ, n, 'x')
        X = R.gens()
        rels = [X[n - 1] - 1]
        for i, j in itertools.combinations_with_replacement(range(n), 2):
            c = ilist(B['product'](Bg.G, Bg.reps, i + 1, j + 1))
            rels.append(X[i] * X[j] - sum(c[l] * X[l] for l in range(n)))
        I = R.ideal(rels)
        pts = sorted(tuple(int(s[x]) for x in X) for s in I.variety(QQ))
        cols = sorted(tuple(int(Bg.M[i, j]) for i in range(n))
                      for j in range(n))
        check(I.vector_space_dimension() == n and pts == cols,
              '%s: Theorem 5.4.2, the ring homomorphisms b(G) -> CC are '
              'exactly the %d maps f_H' % (Bg.name, n))

    # ---- the congruences: the matrix example of p. 180 ------------------
    printed_C = matrix(ZZ, [[1, 0, 0, 0, 0], [3, 1, 0, 0, 0],
                            [8, 0, 1, 0, 0], [0, 1, 0, 1, 0],
                            [0, 0, 0, 2, 1]])
    printed_mod = [12, 2, 1, 3, 1]
    P = printed_tom * printed_C
    check(all(P[i, j] % printed_mod[j] == 0
              for i in range(5) for j in range(5)),
          'p. 180: (table of marks of A4)(second matrix) = 0 mod '
          '(12 2 1 3 1), column by column')
    check(A4.d == printed_mod,
          'p. 180: the moduli 12, 2, 1, 3, 1 are |N_G(H) : H|')
    Cg = matrix(QQ, 5, 5)
    for i in range(5):
        c, _ = B['congruence'](A4.G, A4.reps, i + 1, 0)
        for j in range(5):
            Cg[j, i] = c[j].sage()
    check(Cg == printed_C,
          'p. 180: entry (K, H) of the second matrix = sum over the '
          'conjugates of K containing H normally with K/H cyclic of the '
          'number of generators of K/H')
    check(all((printed_C[j, i] != 0) == bool(printed_C[j, i]) for i in
              range(5) for j in range(5)) and all(
              printed_C[i, i] == 1 for i in range(5)) and all(
              printed_C[i, j] == 0 for i in range(5) for j in range(i + 1, 5)),
          'p. 180: the second matrix is lower triangular with ones on the '
          'diagonal (the congruences are independent)')

    # ---- Theorem 5.4.6 (Dress), p-primary components --------------------
    for Bg in data:
        n, M = Bg.n, Bg.M
        cong, pcong = [], []
        for i in range(n):
            c, m = B['congruence'](Bg.G, Bg.reps, i + 1, 0)
            cong.append(([QQ(x.sage()) for x in c], int(m)))
            for p in factor(Bg.d[i]) if Bg.d[i] > 1 else []:
                c, m = B['congruence'](Bg.G, Bg.reps, i + 1, int(p[0]))
                pcong.append(([QQ(x.sage()) for x in c], int(m)))
        check(all(c[i] == 1 and all(c[j] == 0 for j in range(i))
                  for i, (c, _) in enumerate(cong))
              and all(cong[i][1] == Bg.d[i] for i in range(n))
              and all(x in ZZ for c, _ in cong for x in c),
              '%s: the congruence for H has coefficient 1 at H, 0 at smaller '
              'classes, integer coefficients and modulus |N_G(H) : H|'
              % Bg.name)
        for label, cs in (('Theorem 5.4.6', cong),
                          ('the p-primary congruences (p. 181)', pcong)):
            sat = all(sum(M[r, j] * c[j] for j in range(n)) % m == 0
                      for r in range(n) for c, m in cs)
            # index in ZZ^n of {v : v.c = 0 mod m for all (c, m)}
            gens = [vector(ZZ, c) for c, _ in cs]
            mods = [m for _, m in cs]
            A = matrix(ZZ, [[g[j] for g in gens] for j in range(n)])
            Dm = matrix.diagonal(ZZ, mods) if mods else matrix(ZZ, 0, 0)
            # |image of ZZ^n in sum ZZ/m| = prod m / [ZZ^k : span(A, D)]
            ed = matrix(ZZ, A.rows() + Dm.rows()).elementary_divisors()
            image = prod(mods) // prod(ed[:len(mods)]) if mods else 1
            check(sat and image == prod(Bg.d),
                  '%s: %s, the image of b(G) is the subgroup of ZZ^%d given '
                  'by the congruences (both of index %d)'
                  % (Bg.name, label, n, prod(Bg.d)))

    # ---- Theorem 5.4.7, Corollary 5.4.8 (Dress): idempotents ------------
    for Bg in data:
        n, M = Bg.n, Bg.M
        Minv = M.change_ring(QQ).inverse()
        edges = [ilist(e) for e in B['cyclic_edges'](Bg.G, Bg.reps)]

        def components(es):
            parent = list(range(n))

            def find(a):
                while parent[a] != a:
                    a = parent[a]
                return a
            for i, j, _ in es:
                parent[find(i - 1)] = find(j - 1)
            comp = {}
            for i in range(n):
                comp.setdefault(find(i), []).append(i)
            return sorted(comp.values())

        comps = components(edges)
        prime_edges = [e for e in edges if ZZ(e[2]).is_prime()]
        check(components(prime_edges) == comps,
              '%s: H normal in H\' with cyclic quotient and with quotient of '
              'prime order generate the same relation' % Bg.name)
        ok_int = all(all(x in ZZ for x in vector(QQ, [1 if i in c else 0
                                                      for i in range(n)])
                         * Minv) for c in comps)
        ok_cong = all(all((M[r, i - 1] - M[r, j - 1]) % p == 0
                          for r in range(n)) for i, j, p in prime_edges)
        check(ok_int and ok_cong,
              '%s: Theorem 5.4.7 (i), each union of classes closed under '
              'H normal in H\' with cyclic quotient gives an idempotent of '
              'b(G); |X^H| = |X^H\'| mod p for index p, so no other '
              'idempotent lies in b(G) (%d primitive idempotents)'
              % (Bg.name, len(comps)))
        if n <= 12:
            allidem = []
            for bits in itertools.product([0, 1], repeat=n):
                v = vector(QQ, bits) * Minv
                if all(x in ZZ for x in v):
                    allidem.append(bits)
            unions = set()
            for sel in itertools.product([0, 1], repeat=len(comps)):
                bits = [0] * n
                for s, c in zip(sel, comps):
                    for i in c:
                        bits[i] = s
                unions.add(tuple(bits))
            check(set(allidem) == unions,
                  '%s: Theorem 5.4.7 (i) exhaustively: the %d idempotents '
                  'of B(G) lying in b(G) are the unions of the classes'
                  % (Bg.name, len(allidem)))
        res = ilist(B['perfect_residuum_class'](Bg.G, Bg.reps))
        byres = {}
        for i in range(n):
            byres.setdefault(res[i], []).append(i)
        check(sorted(byres.values()) == comps,
              '%s: Corollary 5.4.8 (i), the classes are given by the perfect '
              'subgroup H^(infinity) up to conjugacy' % Bg.name)
        check((len(comps) == 1) == bool(Bg.G.IsSolvableGroup()),
              '%s: Corollary 5.4.8 (i), G soluble iff 0 and 1 are the only '
              'idempotents of b(G) (%s)'
              % (Bg.name, 'soluble' if len(comps) == 1 else 'not soluble'))
        for p in sorted(set(int(q) for q, _ in factor(Bg.order))):
            pcomps = components([e for e in edges if e[2] == p])
            ok_int = all(all(x.denominator() % p != 0 for x in vector(
                QQ, [1 if i in c else 0 for i in range(n)]) * Minv)
                for c in pcomps)
            ok_cong = all(all((M[r, i - 1] - M[r, j - 1]) % p == 0
                              for r in range(n))
                          for i, j, q in edges if q == p)
            op = ilist(B['Op_class'](Bg.G, Bg.reps, p))
            byop = {}
            for i in range(n):
                byop.setdefault(op[i], []).append(i)
            check(ok_int and ok_cong and sorted(byop.values()) == pcomps,
                  '%s, p = %d: Theorem 5.4.7 (ii) and Corollary 5.4.8 (ii), '
                  'the primitive idempotents of b(G)_(p) are the sums over '
                  'a class of O^p(H) (%d of them)' % (Bg.name, p, len(pcomps)))
            if n <= 9:
                found = set()
                for bits in itertools.product([0, 1], repeat=n):
                    v = vector(QQ, bits) * Minv
                    if all(x.denominator() % p != 0 for x in v):
                        found.add(bits)
                check(len(found) == 2 ** len(pcomps),
                      '%s, p = %d: exhaustively 2^%d idempotents in b(G)_(p)'
                      % (Bg.name, p, len(pcomps)))

    # ---- Lemma 5.4.9, Theorem 5.4.10 -------------------------------------
    for Bg in [b for b in data if b.name in (
            'SmallGroup(6,1)', 'SmallGroup(8,3)', 'SmallGroup(8,4)',
            'SmallGroup(12,3)', 'SmallGroup(24,12)', 'SmallGroup(18,3)',
            'A5')]:
        G, reps = Bg.G, Bg.reps
        for H in list(reps)[:-1]:
            hreps = B['classes'](H)
            for L in hreps:
                for K in reps:
                    lhs, rhs = B['frobenius'](G, reps, H, L, K)
                    check(lhs == rhs,
                          '%s: Lemma 5.4.9 (ii), ind(a.res(b)) = ind(a).b '
                          'for a = H/L, b = G/K' % Bg.name)
            for K in reps:
                for L in B['classes'](K):
                    lhs, rhs = B['mackey'](G, H, K, L)
                    check(B['classcount'](H, hreps, lhs)
                          == B['classcount'](H, hreps, rhs),
                          '%s: Lemma 5.4.9 (iii), Mackey formula for '
                          'res_(G,H) ind_(K,G)(K/L)' % Bg.name)
        # Theorem 5.4.10
        for i, H in enumerate(reps):
            BH = Burnside(H, 'H')
            fus = [Bg.which(L) for L in BH.reps]
            eH = vector(QQ, [0] * (BH.n - 1) + [1]) * \
                BH.M.change_ring(QQ).inverse()
            marks = sum((eH[l] * Bg.M[fus[l] - 1] for l in range(BH.n)),
                        vector(QQ, [0] * Bg.n))
            exp = vector(QQ, [Bg.d[i] if j == i else 0 for j in range(Bg.n)])
            check(marks == exp,
                  '%s: Theorem 5.4.10 (i), ind_(H,G)(e_H) = |N_G(H) : H| e_H '
                  'for |H| = %d' % (Bg.name, Bg.sizes[i]))
            if Bg.sizes[i] < Bg.order:
                check(marks[Bg.n - 1] == 0,
                      '%s: Lemma 5.4.9 (i), no G-fixed point on an induced '
                      'G-set' % Bg.name)
            # (ii): Im(ind) is spanned by the e_K with K <=_G H, Ker(res)
            # by the others
            inside = set(f - 1 for f in fus)
            Ind = matrix(QQ, [Bg.M[f - 1] for f in fus])
            check(Ind.rank() == len(inside)
                  and all(Ind[r, j] == 0 for r in range(BH.n)
                          for j in range(Bg.n) if j not in inside),
                  '%s: Theorem 5.4.10 (ii), B(G) = Im(ind_(H,G)) + '
                  'Ker(res_(G,H)), dimensions %d + %d'
                  % (Bg.name, len(inside), Bg.n - len(inside)))



# ===========================================================================
# Characters, Brauer characters and modules over finite fields (GAP)
# ===========================================================================

gap('BensonCh5R := 0')
gap(r'''BensonCh5R := rec(
  # the matrix of g in the MeatAxe module M of G (generators of G)
  # the matrices of elts in the MeatAxe module M of G, whose generator
  # matrices belong to the generators gens of G
  matsof := function(G, gens, M, elts)
    local mats, hom;
    mats := MTX.Generators(M);
    hom := GroupHomomorphismByImagesNC(G, Group(mats), gens, mats);
    return List(elts, g -> Image(hom, g));
  end,

  brauer := function(G, M, elts)
    return List(BensonCh5R.matsof(G, GeneratorsOfGroup(G), M, elts),
                BrauerCharacterValue);
  end,

  brauer_gens := function(G, gens, M, elts)
    return List(BensonCh5R.matsof(G, gens, M, elts), BrauerCharacterValue);
  end,

  pregular := function(tbl, p)
    return Filtered([1 .. NrConjugacyClasses(tbl)],
                    i -> OrdersClassRepresentatives(tbl)[i] mod p <> 0);
  end,

  # Lemma 5.3.1 with characters: for g of order n prime to p, the values
  # of x = sum_j E(n)^-j Ind(lambda_j) (lambda_j(g^m) = E(n)^(jm)) on the
  # p-regular classes, and |C_G(g)| [y ~ g]
  separating := function(G, g, p)
    local tbl, n, H, tH, cls, expo, x, j, lam, regs, i, y;
    tbl := CharacterTable(G);
    n := Order(g);
    H := Subgroup(G, [g]);
    tH := CharacterTable(H);
    cls := List(ConjugacyClasses(tH), Representative);
    expo := List(cls, h -> First([0 .. n - 1], m -> g^m = h));
    x := 0 * TrivialCharacter(tbl);
    for j in [1 .. n] do
      lam := ClassFunction(tH, List(expo, m -> E(n)^(j * m)));
      x := x + E(n)^(-j) * InducedClassFunction(lam, G);
    od;
    regs := BensonCh5R.pregular(tbl, p);
    return [List(regs, i -> ValuesOfClassFunction(x)[i]),
            List(regs, function(i)
              y := Representative(ConjugacyClasses(tbl)[i]);
              if IsConjugate(G, y, g) then
                return Size(Centralizer(G, g));
              fi;
              return 0;
            end)];
  end,

  # the same with modules over GF(q): M_j : g -> Z(q)^(j(q-1)/n), induced to
  # G, Brauer character values at the p-regular class representatives
  separating_modular := function(G, g, q)
    local n, H, regs, x, j, M, I, cl;
    n := Order(g);
    H := Subgroup(G, [g]);
    cl := List(ConjugacyClasses(G), Representative);
    regs := Filtered(cl, y -> Order(y) mod Characteristic(GF(q)) <> 0);
    x := List(regs, y -> 0);
    for j in [1 .. n] do
      M := GModuleByMats([[[Z(q)^(j * (q - 1) / n)]]], GF(q));
      I := InducedGModule(G, H, M);
      x := x + E(n)^(-j) * BensonCh5R.brauer(G, I, regs);
    od;
    return [x, List(regs, function(y)
              if IsConjugate(G, y, g) then
                return Size(Centralizer(G, g));
              fi;
              return 0;
            end), MTX.Dimension(I)];
  end,

  # Brauer table of G at p, through the library table where needed
  brauer_table := function(G, libname, p)
    local t;
    if libname = "" then
      t := CharacterTable(G);
    else
      # a fresh copy of G: the table of G itself may already exist
      t := CharacterTableWithStoredGroup(Group(GeneratorsOfGroup(G)),
                                         CharacterTable(libname));
    fi;
    return [t, t mod p];
  end,

  # the Frobenius twist of a module (entries to the p-th power)
  frobenius_twist := function(M, p)
    return GModuleByMats(List(MTX.Generators(M),
      m -> List(m, r -> List(r, x -> x^p))), MTX.Field(M));
  end
)''')
R = gap('BensonCh5R')


def cycl(L):
    return [cyc(x) for x in L]


# ===========================================================================
# Sections 5.1-5.3
# ===========================================================================

ORDINARY = [
    ('SymmetricGroup(3)', 'S3'), ('DihedralGroup(8)', 'D8'),
    ('QuaternionGroup(8)', 'Q8'), ('AlternatingGroup(4)', 'A4'),
    ('SymmetricGroup(4)', 'S4'), ('AlternatingGroup(5)', 'A5'),
    ('SL(2,3)', 'SL(2,3)'), ('SmallGroup(12,1)', 'C3:C4'),
    ('DirectProduct(SymmetricGroup(3), CyclicGroup(3))', 'S3xC3'),
    ('PSL(2,7)', 'PSL(2,7)'), ('SmallGroup(21,1)', 'C7:C3'),
    ('SymmetricGroup(5)', 'S5'),
]

# (group, library table or "", primes)
MODULAR = [
    ('SymmetricGroup(3)', '', [2, 3]), ('AlternatingGroup(4)', '', [2, 3]),
    ('SymmetricGroup(4)', '', [2, 3]), ('DihedralGroup(8)', '', [2]),
    ('QuaternionGroup(8)', '', [2]), ('SL(2,3)', '', [2, 3]),
    ('SmallGroup(12,1)', '', [2, 3]), ('SmallGroup(21,1)', '', [3, 7]),
    ('DirectProduct(SymmetricGroup(3), CyclicGroup(3))', '', [2, 3]),
    ('AlternatingGroup(5)', 'A5', [2, 3, 5]),
    ('PSL(2,7)', 'L3(2)', [2, 3, 7]), ('SymmetricGroup(5)', 'S5', [2, 3, 5]),
]


def section_5_1_to_5_3():
    # ---- 5.2 ordinary character theory -----------------------------------
    for src, name in ORDINARY:
        G = gap(src)
        tbl = G.CharacterTable()
        irr = [cycl(chi.ValuesOfClassFunction()) for chi in tbl.Irr()]
        h = int(tbl.NrConjugacyClasses())
        sizes = ilist(tbl.SizesConjugacyClasses())
        cent = ilist(tbl.SizesCentralizers())
        order = int(G.Size())
        check(len(irr) == h and sum(chi[0] ** 2 for chi in irr) == order,
              '%s: Lemma 5.2.1, %d irreducible characters = number of '
              'conjugacy classes, sum of squares of degrees = |G|' % (name, h))
        X = matrix(UCF, irr)
        check(X.det() != 0,
              '%s: Proposition 5.2.3, the t_g are linearly independent: '
              'sum t_g : A(G) -> CC^%d is an isomorphism (character table '
              'non-singular)' % (name, h))

        def inner(a, b):
            return sum(sizes[i] * a[i] * b[i].conjugate()
                       for i in range(h)) / order
        check(all(inner(irr[i], irr[j]) == (1 if i == j else 0)
                  for i in range(h) for j in range(h))
              and all(sum(chi[a] * chi[b].conjugate() for chi in irr)
                      == (cent[a] if a == b else 0)
                      for a in range(h) for b in range(h)),
              '%s: the orthogonality relations (p. 171)' % name)
        prods = all(nonneg_int(inner([irr[i][c] * irr[j][c]
                                      for c in range(h)], irr[k]))
                    for i in range(h) for j in range(i, h) for k in range(h))
        check(prods, '%s: t_g(M (x) N) = t_g(M) t_g(N): products of '
              'irreducible characters are characters (non-negative integer '
              'multiplicities)' % name)
    # (M, N) = dim Hom for permutation modules: double cosets
    for src, name in ORDINARY[:6]:
        G = gap(src)
        reps = B['classes'](G)
        tbl = G.CharacterTable()
        perm = [gap('function(G, H) return InducedClassFunction('
                    'TrivialCharacter(H), G); end')(G, H) for H in reps]
        ok = all(int(gap('ScalarProduct')(perm[i], perm[j]))
                 == len(G.DoubleCosetRepsAndSizes(reps[i], reps[j]))
                 for i in range(len(reps)) for j in range(len(reps)))
        check(ok, '%s: the inner product of permutation characters is '
              'dim Hom(CC[G/H], CC[G/K]) = |H\\G/K| (p. 171)' % name)

    # ---- Lemma 5.3.1: printed proof refuted, corrected count -------------
    # (1) the freeness claim: G = C4 = <a>, g = a^2, g' = a, and the same in
    # G = C4 x C3 with p = 3 dividing |G|.
    for src, gens, p, q in (('CyclicGroup(IsPermGroup, 4)', 'G.1^2', 3, 9),
                            ('DirectProduct(CyclicGroup(IsPermGroup, 4), '
                             'CyclicGroup(IsPermGroup, 3))', 'G.1^2', 3, 9)):
        G = gap(src)
        g = gap('function(G) return %s; end' % gens)(G)
        g1 = G.GeneratorsOfGroup()[0]
        x, exp, dim = R['separating_modular'](G, g, q)
        not_conj = not any(bool(G.IsConjugate(g1, g ** m))
                           for m in range(int(g.Order())))
        check(not_conj, 'Lemma 5.3.1 (p. 175): in %s with p = %d, g\' = a is '
              'not conjugate to an element of <g>, g = a^2' % (src, p))
        refuted(int(dim) % int(g1.Order()) == 0,
                'proof of Lemma 5.3.1 (p. 175): M_j induced to G and '
                'restricted to <g\'> is free (dimension %d, |<g\'>| = %d; G = '
                '%s, p = %d)' % (int(dim), int(g1.Order()), src, p))
        check(cycl(x) == [UCF(e) for e in ilist(exp)],
              'Lemma 5.3.1 corrected proof: t_y(x) = |{z : z^-1 y z = g}| for '
              'all p-regular y (Brauer characters of the induced modules over '
              'GF(%d); %s)' % (q, src))
    # (2) the decomposition of M_j induced and restricted to <g>:
    # G = S3 x C3 (x C7), g = ((1,2), c) of order 6, k = GF(7)
    for src in ('DirectProduct(SymmetricGroup(3), '
                'CyclicGroup(IsPermGroup, 3))',
                'DirectProduct(SymmetricGroup(3), CyclicGroup(IsPermGroup, 3),'
                ' CyclicGroup(IsPermGroup, 7))'):
        G = gap(src)
        gs = G.GeneratorsOfGroup()
        g = gs[1] * gs[2]
        n = int(g.Order())
        H = G.Subgroup([g])
        nn = int(G.Normalizer(H).Index(H))
        x, exp, dim = R['separating_modular'](G, g, 7)
        refuted((int(dim) - nn) % n == 0,
                'proof of Lemma 5.3.1 (p. 175): M_j induced to G restricted '
                'to <g> is the sum of the |N_G<g> : <g>| = %d conjugates of '
                'M_j and a free module (dimension %d, |g| = %d; %s, p = 7)'
                % (nn, int(dim), n, src))
        check(cycl(x) == [UCF(e) for e in ilist(exp)],
              'Lemma 5.3.1 corrected proof: t_y(x) = |{z : z^-1 y z = g}| '
              '(%s, GF(7), g of order 6)' % src)
    # (3) the lemma itself, by induced characters, for every p'-element g
    # of the groups and primes below (and by modules over finite fields for
    # the small groups)
    for src, lib, primes in MODULAR:
        G = gap(src)
        tbl = G.CharacterTable()
        clreps = [c.Representative() for c in tbl.ConjugacyClasses()]
        for p in primes:
            for g in clreps:
                if int(g.Order()) % p == 0:
                    continue
                vals, exp = R['separating'](G, g, p)
                check(cycl(vals) == [UCF(e) for e in ilist(exp)],
                      '%s, p = %d: Lemma 5.3.1, t_y(x) = |C_G(g)| if y ~ g, 0 '
                      'otherwise, for g of order %d (induced characters)'
                      % (src, p, int(g.Order())))
    for src, p, q in (('SymmetricGroup(3)', 2, 4), ('SymmetricGroup(3)', 3, 9),
                      ('AlternatingGroup(4)', 2, 4),
                      ('AlternatingGroup(4)', 3, 9),
                      ('SymmetricGroup(4)', 3, 9), ('SymmetricGroup(4)', 2, 4),
                      ('AlternatingGroup(5)', 2, 16)):
        G = gap(src)
        for c in G.ConjugacyClasses():
            g = c.Representative()
            if int(g.Order()) % p == 0:
                continue
            x, exp, _ = R['separating_modular'](G, g, q)
            check(cycl(x) == [UCF(e) for e in ilist(exp)],
                  '%s over GF(%d): Lemma 5.3.1 with modules, g of order %d'
                  % (src, q, int(g.Order())))

    # ---- 5.3 Brauer characters, Cartan matrices --------------------------
    for src, lib, primes in MODULAR:
        G = gap(src)
        order = int(G.Size())
        for p in primes:
            t, bt = R['brauer_table'](G, lib, p)
            regs = ilist(R['pregular'](t, p))
            ibr = [cycl(b.ValuesOfClassFunction()) for b in bt.Irr()]
            irr = [cycl(c.ValuesOfClassFunction()) for c in t.Irr()]
            ell = len(ibr)
            name = '%s, p = %d' % (src if not lib else lib, p)
            check(ell == len(regs),
                  '%s: Corollary 5.3.5, %d irreducible Brauer characters = '
                  'number of p-regular classes' % (name, ell))
            Bm = matrix(UCF, ibr)
            check(Bm.det() != 0,
                  '%s: Theorem 5.3.3, the t_g (g p-regular) are linearly '
                  'independent on R(kG): the Brauer table is non-singular'
                  % name)
            D = imat(bt.DecompositionMatrix())
            fus = ilist(gap('GetFusionMap')(bt, t))
            ok = all(vector(UCF, [chi[f - 1] for f in fus])
                     == sum((D[i, j] * vector(UCF, ibr[j])
                             for j in range(ell)), vector(UCF, [0] * ell))
                     for i, chi in enumerate(irr))
            check(ok and all(x >= 0 for x in D.list()),
                  '%s: restrictions of the ordinary characters to the '
                  'p-regular classes are non-negative integer combinations '
                  'of the Brauer characters (decomposition matrix)' % name)
            C = D.transpose() * D
            det = C.det()
            pp = p ** ZZ(order).valuation(p)
            check(det != 0 and det == p ** ZZ(det).valuation(p),
                  '%s: Corollary 5.3.6, the Cartan matrix C = D^T D is '
                  'non-singular, det C = %d is a power of p (Corollary 5.7.2, '
                  'Theorem 5.9.3)' % (name, det))
            ed = C.elementary_divisors()
            check(all(e == p ** ZZ(e).valuation(p) for e in ed)
                  and pp % ed[-1] == 0,
                  '%s: the cokernel of the Cartan homomorphism is a p-group '
                  'annihilated by |G|_p = %d (elementary divisors %s; proof '
                  'of Theorem 5.9.3)' % (name, pp, ed))
            # proof of Theorem 5.9.3: (dim P).1 and |G|_p.1 lie in Im(c)
            triv = [j for j in range(ell) if all(v == 1 for v in ibr[j])][0]
            L = C.transpose().row_module()  # Im(c), basis the simples
            e1 = vector(ZZ, [1 if j == triv else 0 for j in range(ell)])
            dims = [sum(C[i, j] * ibr[i][0] for i in range(ell))
                    for j in range(ell)]
            check(all(ZZ(QQ(dm)) * e1 in L for dm in dims) and pp * e1 in L,
                  '%s: proof of Theorem 5.9.3, (dim P).1 in Im(c) for every '
                  'projective indecomposable P, and |G|_p.1 in Im(c)' % name)
            check(all(x == 1 for x in D.transpose().elementary_divisors()),
                  '%s: Corollary 5.6.5, the decomposition map R(KG) -> R(kG) '
                  'is surjective (elementary divisors of D all 1)' % name)
            Phi = [sum((D[i, j] * vector(UCF, [irr[i][f - 1] for f in fus])
                        for i in range(len(irr))), vector(UCF, [0] * ell))
                   for j in range(ell)]
            check(matrix(UCF, Phi).det() != 0,
                  '%s: Corollary 5.3.6, projective indecomposables have '
                  'linearly independent Brauer characters' % name)
            Ci = C.change_ring(QQ).inverse()
            e = sum((Ci[j, triv] * Phi[j] for j in range(ell)),
                    vector(UCF, [0] * ell))
            check(all(v == 1 for v in e),
                  '%s: Corollary 5.3.6, e = c^-1(1) has Brauer character 1, '
                  'so e^2 = e in A(G, 1)' % name)

    # ---- Proposition 5.3.4: Frobenius twists and fields of definition ----
    for src, p, f in (('AlternatingGroup(5)', 2, 2),
                      ('AlternatingGroup(4)', 2, 2),
                      ('AlternatingGroup(4)', 3, 2), ('SymmetricGroup(4)', 3, 2),
                      ('SL(2,3)', 3, 2), ('SmallGroup(21,1)', 2, 3),
                      ('PSL(2,7)', 2, 3), ('SmallGroup(12,1)', 3, 2)):
        G = gap(src)
        regs = [c.Representative() for c in G.ConjugacyClasses()
                if int(c.Representative().Order()) % p != 0]
        absirr = gap('function(G, q) local L; L := IrreducibleModules(G, '
                     'GF(q), 0); return [L[1], Filtered(L[2], '
                     'MTX.IsAbsolutelyIrreducible)]; end')
        gb, big = absirr(G, p ** f)
        gs, small = absirr(G, p)
        chars_small = sorted(str(R['brauer_gens'](G, gs, M, regs))
                             for M in small)
        stable = []
        for M in big:
            FM = R['frobenius_twist'](M, p)
            v = R['brauer_gens'](G, gb, M, regs)
            vF = R['brauer_gens'](G, gb, FM, regs)
            vp = R['brauer_gens'](G, gb, M, [g ** p for g in regs])
            check(vF == vp,
                  '%s over GF(%d): Proposition 5.3.4, t_g(F(M)) = t_(g^p)(M) '
                  '(dim M = %d)' % (src, p ** f, int(M['dimension'])))
            if gap('MTX.IsomorphismModules')(M, FM) != gap('fail'):
                stable.append(str(v))
        check(sorted(stable) == chars_small,
              '%s, p = %d: Proposition 5.3.4, the absolutely irreducible '
              'GF(%d)-modules with F(M) ~ M are exactly those defined over '
              'GF(%d) (%d of %d)' % (src, p, p ** f, p, len(stable), len(big)))

    # ---- 5.1: K_0 has no identity in general (author's sentence) ---------
    for p in (2, 3, 5):
        P = gap('function(p) local x; x := IdentityMat(p, GF(p)); '
                'return PermutationMat(CycleFromList([1 .. p]), p, GF(p)); '
                'end')(p)
        PP = gap('KroneckerProduct')(P, P)
        # P (x) P has p^2 = p * p dimensions and is free: P (x) P ~ p.P
        rk = int(gap('function(X, n) return RankMat(X - X^0); end')(PP, p * p))
        check(rk == p * p - p,
              'p. 173: over GF(%d)C%d the projective P = kG has P (x) P ~ '
              '%d.P (fixed points of dimension %d)' % (p, p, p, p))
        refuted(any(m * p == 1 for m in range(-p * p, p * p)),
                'p. 173 (author\'s sentence): K_0(GF(%d)C%d) = ZZ[P] with '
                '[P][P] = %d[P] has an identity m[P] (needs m %d = 1)'
                % (p, p, p, p))



# ===========================================================================
# Trivial source modules (MeatAxe)
# ===========================================================================

gap('BensonCh5T := 0')
gap(r'''BensonCh5T := rec(
  module := function(gens, mats, d, F)
    if Length(gens) = 0 then return GModuleByMats([], d, F); fi;
    return GModuleByMats(mats, F);
  end,

  permmodule := function(G, H, F)
    local n, f, gens;
    gens := GeneratorsOfGroup(G);
    n := Index(G, H);
    if n = 1 then
      return BensonCh5T.module(gens, List(gens, g -> IdentityMat(1, F)), 1, F);
    fi;
    f := FactorCosetAction(G, H);
    return BensonCh5T.module(gens,
      List(gens, g -> PermutationMat(Image(f, g), n, F)), n, F);
  end,

  summands := function(M)
    if MTX.Dimension(M) = 0 then return []; fi;
    if Length(MTX.Generators(M)) = 0 then
      return List([1 .. MTX.Dimension(M)],
                  i -> GModuleByMats([], 1, MTX.Field(M)));
    fi;
    return List(MTX.Indecomposition(M), x -> x[2]);
  end,

  iso := function(A, B)
    if MTX.Dimension(A) <> MTX.Dimension(B) then return false; fi;
    if Length(MTX.Generators(A)) = 0 then return true; fi;
    return MTX.IsomorphismModules(A, B) <> fail;
  end,

  position := function(L, M)
    return PositionProperty(L, X -> BensonCh5T.iso(X, M));
  end,

  # counts of the members of L among the indecomposable summands of M
  decompose := function(L, M)
    local c, S, i;
    c := List(L, x -> 0);
    for S in BensonCh5T.summands(M) do
      i := BensonCh5T.position(L, S);
      if i = fail then return fail; fi;
      c[i] := c[i] + 1;
    od;
    return c;
  end,

  # the indecomposable trivial source modules: summands of the F[G/H]
  tsmodules := function(G, F)
    local L, H, S;
    L := [];
    for H in BensonCh5.classes(G) do
      for S in BensonCh5T.summands(BensonCh5T.permmodule(G, H, F)) do
        if BensonCh5T.position(L, S) = fail then Add(L, S); fi;
      od;
    od;
    return L;
  end,

  restrict := function(G, H, M)
    local gH;
    gH := GeneratorsOfGroup(H);
    return BensonCh5T.module(gH,
      BensonCh5R.matsof(G, GeneratorsOfGroup(G), M, gH),
      MTX.Dimension(M), MTX.Field(M));
  end,

  induce := function(G, H, M)
    local R, F;
    F := MTX.Field(M);
    if Size(H) = 1 then
      R := BensonCh5T.permmodule(G, H, F);
      return BensonCh5T.module(GeneratorsOfGroup(G),
        List(MTX.Generators(R), m -> KroneckerProduct(m,
          IdentityMat(MTX.Dimension(M), F))),
        Index(G, H) * MTX.Dimension(M), F);
    fi;
    return InducedGModule(G, H, M);
  end,

  ppart_free := function(h, p)
    local o, v, r;
    o := Order(h);
    v := p^Valuation(o, p);
    r := o / v;
    return h^ChineseRem([v, r], [0, 1]);
  end,

  # classes of pairs (H, g), H p-hypo-elementary, g a generator of
  # H/O_p(H): triples [H, O_p(H), h] with h a p'-element of H over g
  pairs := function(G, p)
    local res, H, P, hom, Q, gq, N, act, o;
    res := [];
    for H in BensonCh5.classes(G) do
      P := PCore(H, p);
      hom := NaturalHomomorphismByNormalSubgroup(H, P);
      Q := Image(hom);
      if IsCyclic(Q) then
        gq := Filtered(AsList(Q), x -> Order(x) = Size(Q));
        N := Normalizer(G, H);
        act := function(x, n)
          return Image(hom, PreImagesRepresentative(hom, x)^n);
        end;
        for o in Orbits(N, gq, act) do
          Add(res, [H, P, BensonCh5T.ppart_free(
            PreImagesRepresentative(hom, o[1]), p)]);
        od;
      fi;
    od;
    return res;
  end,

  # s_(H, g)(M) for the pairs
  species := function(G, prs, M)
    local val, pr, H, P, h, S, R, v, gH;
    val := [];
    for pr in prs do
      H := pr[1]; P := pr[2]; h := pr[3];
      if Size(H) = 1 then
        Add(val, MTX.Dimension(M));
        continue;
      fi;
      gH := GeneratorsOfGroup(H);
      R := BensonCh5T.restrict(G, H, M);
      v := 0;
      for S in BensonCh5T.summands(R) do
        if ForAll(BensonCh5R.matsof(H, gH, S, GeneratorsOfGroup(P)),
                  m -> m = m^0) then
          v := v + BrauerCharacterValue(
            BensonCh5R.matsof(H, gH, S, [h])[1]);
        fi;
      od;
      Add(val, v);
    od;
    return val;
  end,

  is_hypo := function(H, p)
    return IsCyclic(H / PCore(H, p));
  end,

  # H/O_p(H) is q-hyperelementary: O^q of it is cyclic
  is_dress := function(H, p, q)
    local Q;
    Q := H / PCore(H, p);
    return IsCyclic(Subgroup(Q, Filtered(AsList(Q),
                                         x -> Order(x) mod q <> 0)));
  end
)''')
T = gap('BensonCh5T')


TRIVIAL_SOURCE = [  # (group, name, p, field)
    ('SymmetricGroup(3)', 'S3', 2, 4), ('SymmetricGroup(3)', 'S3', 3, 3),
    ('AlternatingGroup(4)', 'A4', 2, 4), ('AlternatingGroup(4)', 'A4', 3, 3),
    ('SymmetricGroup(4)', 'S4', 3, 9), ('SymmetricGroup(4)', 'S4', 2, 4),
    ('DihedralGroup(8)', 'D8', 2, 2), ('SmallGroup(12,1)', 'C3:C4', 3, 9),
    ('SmallGroup(12,1)', 'C3:C4', 2, 4), ('AlternatingGroup(5)', 'A5', 5, 25),
    ('DirectProduct(SymmetricGroup(3), CyclicGroup(3))', 'S3xC3', 3, 3),
]


def section_5_5_and_5_6_trivial_source():
    for src, name, p, q in TRIVIAL_SOURCE:
        G = gap(src)
        F = libgap.GF(q)
        Lm = T['tsmodules'](G, F)
        prs = T['pairs'](G, p)
        nts, npr = int(Lm.Length()), int(prs.Length())
        tag = '%s, p = %d, GF(%d)' % (name, p, q)
        check(nts == npr,
              '%s: Corollary 5.5.5, the %d classes of pairs (H, g) (H '
              'p-hypo-elementary, g a generator of H/O_p(H)) are as many as '
              'the indecomposable trivial source modules (rank of '
              'a(G, Triv))' % (tag, npr))
        # rows: the modules, columns: the pairs (H, g)
        S = matrix(UCF, [cycl(T['species'](G, prs, M)) for M in Lm])
        check(S.det() != 0,
              '%s: Proposition 5.5.4 and Corollary 5.5.5, the species table '
              '(s_(H,g)(M)) is non-singular: sum s_(H,g) : A(G, Triv) -> '
              'CC^%d is an isomorphism' % (tag, npr))
        dims = [int(M['dimension']) for M in Lm]
        for i in range(nts):
            for j in range(i, nts):
                if dims[i] * dims[j] > 64:
                    continue
                TP = gap('function(A, B) return TensorProductGModule(A, B); '
                         'end')(Lm[i], Lm[j])
                c = T['decompose'](Lm, TP)
                check(c != gap('fail'),
                      '%s: a tensor product of trivial source modules is a '
                      'trivial source module' % tag)
                c = ilist(c)
                check(all(S[i, k] * S[j, k] == sum(c[l] * S[l, k]
                                                   for l in range(nts))
                          for k in range(npr)),
                      '%s: s_(H,g)(M (x) N) = s_(H,g)(M) s_(H,g)(N) (the '
                      's_(H,g) are ring homomorphisms)' % tag)
        # on permutation modules the species are the marks f_H (the map
        # lambda of the diagram on p. 188)
        Bg = Burnside(G, name)
        ok = True
        for i, H in enumerate(Bg.reps):
            c = ilist(T['decompose'](Lm, T['permmodule'](G, H, F)))
            row = sum((c[l] * S.row(l) for l in range(nts)),
                      vector(UCF, [0] * npr))
            for k in range(npr):
                Hk = prs[k][0]
                ok = ok and row[k] == UCF(Bg.M[i, Bg.which(Hk) - 1])
        check(ok, '%s: s_(H,g)(k[X]) = |X^H| for every transitive X, so '
              'epsilon_H goes to sum_g epsilon_(H,g) for H p-hypo-elementary '
              '(diagram p. 188)' % tag)
        if 2 ** ZZ(int(G.Size())).valuation(2) == int(G.Size()) and p == 2:
            check(nts == Bg.n,
                  '%s: for a p-group the trivial source modules are the '
                  'k[G/H] and the pairs are the classes of subgroups' % tag)

        # ---- Conlon's and Dress' induction theorems in a(G, Triv) ------
        triv = [l for l in range(nts) if dims[l] == 1 and all(
            S[l, k] == 1 for k in range(npr))][0]
        hypo, dress = [], {}
        rows = {}
        for H in Bg.reps:
            LH = T['tsmodules'](H, F)
            vecs = []
            for M in LH:
                c = T['decompose'](Lm, T['induce'](G, H, M))
                vecs.append(vector(ZZ, ilist(c)))
            rows[Bg.which(H)] = vecs
        primes = sorted(set(int(r) for r, _ in factor(int(G.Size()))))
        for i, H in enumerate(Bg.reps):
            if bool(T['is_hypo'](H, p)):
                hypo.append(i + 1)
            for r in primes:
                if bool(T['is_dress'](H, p, r)):
                    dress.setdefault(r, []).append(i + 1)
        e = vector(ZZ, [1 if l == triv else 0 for l in range(nts)])

        def span(idx, ring=QQ):
            vs = [v for i in idx for v in rows[i]]
            return matrix(ring, vs).row_module() if vs else None
        Vh = span(hypo)
        check(Vh is not None and e in Vh,
              '%s: Conlon\'s induction theorem 5.6.8, 1 lies in the sum of '
              'the images of induction from the %d classes of '
              'p-hypo-elementary subgroups (A(G, Triv))' % (tag, len(hypo)))
        maximal = [i for i in hypo if not any(
            j != i and Bg.M[j - 1, i - 1] != 0 for j in hypo)]
        for i in maximal:
            Vm = span([j for j in hypo if j != i])
            refuted(Vm is not None and e in Vm,
                    '%s: Conlon\'s theorem without the class of the maximal '
                    'p-hypo-elementary subgroup of order %d (p. 189: all '
                    'maximal classes are needed)' % (tag, Bg.sizes[i - 1]))
        if Bg.n not in hypo:
            # Corollary 5.6.9 on A(G, Triv): restriction to the
            # p-hypo-elementary subgroups is injective
            cols = []
            for M in Lm:
                v = []
                for i in hypo:
                    H = Bg.reps[i - 1]
                    LH = T['tsmodules'](H, F)
                    v += ilist(T['decompose'](LH, T['restrict'](G, H, M)))
                cols.append(v)
            check(matrix(ZZ, cols).rank() == nts,
                  '%s: Corollary 5.6.9, sum of res_(G,H) over the '
                  'p-hypo-elementary H is injective on A(G, Triv)' % tag)
        allD = sorted(set(i for r in dress for i in dress[r]))
        VD = span(allD, ZZ)
        check(e in VD,
              '%s: Dress\' induction theorem 5.6.11, 1 is a ZZ-combination '
              'of modules induced from (p, q)-Dress subgroups' % tag)
        for r in primes:
            V = span(dress.get(r, []), QQ)
            sol = None
            if V is not None and e in V:
                A = matrix(QQ, [v for i in dress[r] for v in rows[i]])
                sol = A.solve_left(e)
                # the lattice of solutions: is there one without r in the
                # denominators?  Use the ZZ_(r)-span via Smith form.
                Mz = matrix(ZZ, A)
                D, U, W = Mz.smith_form()
                # e in ZZ_(r)-span iff e W = x D has a solution with
                # denominators prime to r
                eW = vector(QQ, e) * W.change_ring(QQ)
                ok = True
                for k in range(W.ncols()):
                    dk = D[k, k] if k < min(D.nrows(), D.ncols()) else 0
                    if dk == 0:
                        ok = ok and eW[k] == 0
                    else:
                        ok = ok and (eW[k] / dk).denominator() % r != 0
                sol = ok
            check(sol is True,
                  '%s: Theorem 5.6.11 with S = {%d}, 1 in the ZZ_(%d)-span '
                  'of modules induced from (p, %d)-Dress subgroups'
                  % (tag, r, r, r))



# ===========================================================================
# Cyclic p-groups: Jordan blocks (GAP linear algebra over GF(p))
# ===========================================================================

gap('BensonCh5C := 0')
gap(r'''BensonCh5C := rec(
  # unipotent Jordan block: the generator x of C_q acting on J_m
  J := function(m, F)
    local X, i;
    X := IdentityMat(m, F);
    for i in [1 .. m - 1] do X[i][i + 1] := One(F); od;
    return X;
  end,

  # counts c[1 .. q] of Jordan blocks of the unipotent matrix X
  jtype := function(X, q)
    local n, Y, Z, r, i, ge, c;
    n := Length(X);
    if n = 0 then return List([1 .. q], i -> 0); fi;
    Y := X - X^0; Z := X^0; r := [n];
    for i in [1 .. q + 1] do Z := Z * Y; Add(r, RankMat(Z)); od;
    ge := List([1 .. q + 1], i -> r[i] - r[i + 1]);
    c := List([1 .. q], i -> ge[i] - ge[i + 1]);
    return c;
  end,

  tensor := function(a, b, q, F)
    return BensonCh5C.jtype(KroneckerProduct(BensonCh5C.J(a, F),
                                             BensonCh5C.J(b, F)), q);
  end,

  # dim Hom between modules given by the matrices A (on M) and B (on N)
  homdim := function(A, B)
    local a, b, F;
    a := Length(A); b := Length(B);
    F := DefaultField(A[1]);
    return a * b - RankMat(KroneckerProduct(IdentityMat(a, F), B)
                           - KroneckerProduct(TransposedMat(A),
                                              IdentityMat(b, F)));
  end,

  # rank of sum_(i < q) x^i acting on Hom_k(M, N): f -> B^i f A^-i
  trrank := function(A, B, q)
    local S, i;
    S := 0 * KroneckerProduct(A, B);
    for i in [0 .. q - 1] do
      S := S + KroneckerProduct(TransposedMat(A^(-i)), B^i);
    od;
    return RankMat(S);
  end,

  # the module of C_q (generator x) induced from C_(q/s) = <x^s> acting by Y
  induced := function(Y, s)
    local m, F, X, i;
    m := Length(Y); F := DefaultField(Y[1]);
    X := NullMat(s * m, s * m, F);
    for i in [1 .. s - 1] do
      X{[(i - 1) * m + 1 .. i * m]}{[i * m + 1 .. (i + 1) * m]} :=
        IdentityMat(m, F);
    od;
    X{[(s - 1) * m + 1 .. s * m]}{[1 .. m]} := Y;
    return X;
  end,

  # psi^n on J_m for n prime to p: Jordan types of the eigenspaces of the
  # cyclic permutation t of the n tensor factors of J_m^(x n), over GF(q)
  # with n | q - 1; eps = Z(q)^((q-1)/n); returns [type of eps^j, j = 1..n]
  eigen := function(m, n, p, q)
    local F, X, Xn, perm, P, idx, j, a, e, eps, Pr, B, res, i, Xr, sols,
          dim;
    F := GF(q);
    X := BensonCh5C.J(m, F);
    Xn := X;
    for i in [2 .. n] do Xn := KroneckerProduct(Xn, X); od;
    dim := m^n;
    # t: e_(i_1) x ... x e_(i_n) -> e_(i_n) x e_(i_1) x ... x e_(i_(n-1))
    perm := List([0 .. dim - 1], function(k)
      local digs, kk, r;
      digs := []; kk := k;
      for r in [1 .. n] do Add(digs, kk mod m); kk := QuoInt(kk, m); od;
      digs := Reversed(digs);               # i_1 .. i_n
      digs := Concatenation([digs[n]], digs{[1 .. n - 1]});
      return Sum([1 .. n], r -> digs[r] * m^(n - r)) + 1;
    end);
    P := PermutationMat(PermList(perm), dim, F);
    eps := Z(q)^((q - 1) / n);
    res := [];
    for j in [1 .. n] do
      Pr := Sum([0 .. n - 1], a -> eps^(-j * a) * P^a);
      B := BaseMat(Pr);
      if Length(B) = 0 then
        Add(res, List([1 .. p], i -> 0));
      else
        # the action of x on the eigenspace (row space B; row convention)
        Xr := List(B, v -> SolutionMat(B, v * Xn));
        Add(res, BensonCh5C.jtype(Xr, p));
      fi;
    od;
    return res;
  end
)''')
CY = gap('BensonCh5C')


class GreenCyclic:
    """The Green ring a(kC_q), q = p^n, basis J_1, ..., J_q (Jordan blocks),
    structure constants computed from Jordan types over GF(p)."""

    def __init__(self, p, q):
        self.p, self.q = p, q
        self.F = libgap.GF(p)
        self.N = {}
        for a in range(1, q + 1):
            for b in range(a, q + 1):
                c = vector(ZZ, ilist(CY['tensor'](a, b, q, self.F)))
                self.N[a, b] = self.N[b, a] = c
        self.one = self.e(1)

    def e(self, a):
        return vector(QQ, [1 if i == a else 0 for i in range(1, self.q + 1)])

    def mul(self, x, y):
        r = vector(QQ, [0] * self.q)
        for a in range(1, self.q + 1):
            if x[a - 1] == 0:
                continue
            for b in range(1, self.q + 1):
                if y[b - 1] != 0:
                    r += x[a - 1] * y[b - 1] * self.N[a, b]
        return r

    def L(self, x):
        return matrix(QQ, [self.mul(x, self.e(b)) for b in
                           range(1, self.q + 1)]).transpose()


def reduced(L_list):
    """A commutative QQ-algebra with the multiplication matrices L_list of a
    basis has no non-zero nilpotents iff its trace form is non-degenerate."""
    n = len(L_list)
    T = matrix(QQ, n, n, lambda i, j: (L_list[i] * L_list[j]).trace())
    return T.det() != 0


def section_cyclic_green_rings():
    out = {}
    for p, q in ((2, 2), (3, 3), (2, 4), (5, 5), (7, 7), (2, 8), (3, 9)):
        Gr = GreenCyclic(p, q)
        out[q] = Gr
        tag = 'GF(%d)C%d' % (p, q)
        rng = range(1, q + 1)
        check(all(sum(Gr.N[a, b][i] * (i + 1) for i in range(q)) == a * b
                  for a in rng for b in rng),
              '%s: J_a (x) J_b has dimension ab' % tag)
        check(all(Gr.mul(Gr.mul(Gr.e(a), Gr.e(b)), Gr.e(c))
                  == Gr.mul(Gr.e(a), Gr.mul(Gr.e(b), Gr.e(c)))
                  for a in rng for b in rng for c in rng)
              and all(Gr.mul(Gr.one, Gr.e(a)) == Gr.e(a) for a in rng),
              'Section 5.1: %s, a(G) is a commutative associative ring with '
              'identity [k] = J_1' % tag)
        Ls = [Gr.L(Gr.e(a)) for a in rng]
        check(reduced(Ls),
              '%s: Theorem 5.8.7 (Green, O\'Reilly), A(kG) has no non-zero '
              'nilpotent elements (trace form non-degenerate)' % tag)
        # Section 5.8 with A(G; p) = span of the J_m with p | m
        div = [m for m in rng if m % p == 0]
        check(all(all(Gr.N[a, m][i] == 0 for i in range(q)
                       if (i + 1) % p != 0) for a in rng for m in div),
              '%s: Proposition 5.8.1 (corrected: M indecomposable), every '
              'summand of J_m (x) J_b has dimension divisible by p when '
              'p | m; Lemma 5.8.3, A(G; p) is an ideal' % tag)
        # printed Proposition 5.8.1 without "indecomposable": M = J_1 + J_(p-1)
        M = Gr.e(1) + Gr.e(p - 1)
        refuted(all(x == 0 for i, x in enumerate(Gr.mul(M, Gr.one))
                    if (i + 1) % p != 0),
                '%s: printed Proposition 5.8.1 (M not assumed '
                'indecomposable): M = J_1 + J_(p-1) has dimension p but '
                'M (x) k has the summand k' % tag)
        nd = [m for m in rng if m % p != 0]
        Lq = []
        for a in nd:
            La = Gr.L(Gr.e(a))
            Lq.append(matrix(QQ, [[La[i - 1, j - 1] for j in nd] for i in nd]))
        check(reduced(Lq),
              '%s: Theorem 5.8.5, A(G)/A(G; p) has no non-zero nilpotent '
              'elements' % tag)
        # forms of Section 5.10: (J_a, J_b), <J_a, J_b>
        Jm = {a: CY['J'](a, Gr.F) for a in rng}
        hom = {(a, b): int(CY['homdim'](Jm[a], Jm[b])) for a in rng
               for b in rng}
        tr = {(a, b): int(CY['trrank'](Jm[a], Jm[b], q)) for a in rng
              for b in rng}
        u = Gr.e(q) - Gr.e(q - 1)
        v = Gr.e(q) - Gr.e(q - 1)
        check(Gr.mul(u, v) == Gr.one,
              '%s: Lemma 5.10.3, u v = 1 (u = v = J_q - J_(q-1))' % tag)

        def form(x, y, f):
            return sum(x[a - 1] * y[b - 1] * f[a, b] for a in rng for b in rng)
        for a in rng:
            for b in rng:
                ii = tr[a, b]
                iii = Gr.N[a, b][q - 1]  # J_a* = J_a: multiplicity of J_q
                ua = Gr.mul(u, Gr.e(a))
                iv = form(ua, Gr.e(b), hom)
                check(ii == iii == iv == max(0, a + b - q),
                      '%s: Lemma 5.10.2, <J_%d, J_%d> = rank of the trace = '
                      'multiplicity of P_k in Hom_k = (u.[M], [N]) = %d'
                      % (tag, a, b, ii))
        check(all(hom[a, b] == min(a, b) for a in rng for b in rng),
              '%s: (J_a, J_b) = dim Hom = min(a, b)' % tag)
        E = [Gr.e(a) for a in rng]
        ok = True
        for x in E:
            for y in E:
                ok = ok and form(x, y, hom) == form(Gr.mul(v, x), y, tr) \
                    == form(x, Gr.mul(u, y), tr)
                ok = ok and form(x, y, tr) == form(Gr.mul(u, x), y, hom) \
                    == form(x, Gr.mul(v, y), hom)
                ok = ok and form(x, y, hom) == form(y, Gr.mul(Gr.mul(v, v), x),
                                                    hom) \
                    == form(Gr.mul(Gr.mul(u, u), y), x, hom)
        check(ok, '%s: Proposition 5.10.4 (i)-(iii) on all pairs of '
              'indecomposables' % tag)
        # printed proof of Lemma 5.10.2 with Hom_kG(M, N) (trivial action):
        # (ii) would be the multiplicity of P_k in a trivial module
        if q > 1:
            refuted(all(tr[a, b] == 0 for a in rng for b in rng),
                    '%s: proof of Lemma 5.10.2 as printed (N replaced by '
                    'Hom_kG(M, N), a trivial module, in which P_k never '
                    'occurs)' % tag)
        # Theorem 5.11.1: tau_0[J_m] = 2 J_m - J_(m-1) - J_(m+1) (m < q),
        # J_q - J_(q-1) (Rad J_q = J_(q-1)); Omega^2 J_m = J_m
        for m in rng:
            if m < q:
                t0 = 2 * Gr.e(m) - Gr.e(m + 1) - (Gr.e(m - 1) if m > 1 else 0)
            else:
                t0 = Gr.e(q) - Gr.e(q - 1)
            check(all(form(Gr.e(a), t0, hom) == (1 if a == m else 0)
                      for a in rng),
                  '%s: Theorem 5.11.1, ([N\'], tau_0[J_%d]) = delta'
                  % (tag, m))
            # Theorem 5.11.3: Omega(J_m) = Omega^-1(J_m) = J_(q-m)
            if m < q:
                n1 = q - m
                X = Gr.e(n1 + 1) + (Gr.e(n1 - 1) if n1 > 1 else 0)
                t1 = X - 2 * Gr.e(n1)
            else:
                t1 = Gr.e(1)
            check(t1 == Gr.mul(u, t0)
                  and all(form(Gr.e(a), t1, tr) == (1 if a == m else 0)
                          for a in rng),
                  '%s: Theorem 5.11.3, tau_1[J_%d] = u.tau_0[J_%d] and '
                  '<[N\'], tau_1[J_%d]> = delta' % (tag, m, m, m))
        # Corollary 5.11.2: the Hom matrix is invertible
        check(matrix(ZZ, q, q, lambda i, j: hom[i + 1, j + 1]).det() != 0,
              '%s: Corollary 5.11.2, modules are determined by the '
              'dimensions dim Hom(M, -)' % tag)

    # Restriction, induction and Lemma 5.8.6 for C_(p^2) > C_p
    for p, q in ((2, 4), (2, 8), (3, 9)):
        G, H = out[q], out[q // p]
        tag = 'GF(%d)C%d > C%d' % (p, q, q // p)
        F = G.F
        res = {a: vector(QQ, ilist(CY['jtype'](CY['J'](a, F) ** p, q // p)))
               for a in range(1, q + 1)}
        ind = {c: vector(QQ, ilist(CY['jtype'](CY['induced'](CY['J'](c, F), p),
                                               q)))
               for c in range(1, q // p + 1)}
        check(all(ind[c] == G.e(p * c) for c in ind),
              '%s: ind J_c = J_(pc), so Im(ind_(H_1, H)) = A(H; p) (Lemma '
              '5.8.6)' % tag)

        def Res(x):
            return sum((x[a - 1] * res[a] for a in range(1, q + 1)),
                       vector(QQ, [0] * (q // p)))

        def Ind(x):
            return sum((x[c - 1] * ind[c] for c in range(1, q // p + 1)),
                       vector(QQ, [0] * q))
        ok = all(Res(G.mul(G.e(a), G.e(b))) == H.mul(res[a], res[b])
                 for a in range(1, q + 1) for b in range(1, q + 1))
        check(ok, '%s: res is a ring homomorphism (Section 5.1)' % tag)
        ok = all(Ind(H.mul(H.e(c), res[b])) == G.mul(ind[c], G.e(b))
                 for c in range(1, q // p + 1) for b in range(1, q + 1))
        check(ok, '%s: ind(x.res(y)) = ind(x).y, the image of induction is '
              'an ideal (Section 5.1)' % tag)
        uG = G.e(q) - G.e(q - 1)
        uH = H.e(q // p) - H.e(q // p - 1)
        check(Res(uG) == uH,
              '%s: Lemma 5.10.5, res(u_kG) = u_kH (= res(v_kG) = v_kH)' % tag)
        Fh = {}
        for a in range(1, q + 1):
            for b in range(1, q + 1):
                Fh[a, b] = int(CY['homdim'](CY['J'](a, F), CY['J'](b, F)))
        fH = {(a, b): min(a, b) for a in range(1, q // p + 1)
              for b in range(1, q // p + 1)}
        tH = {(a, b): max(0, a + b - q // p) for a in range(1, q // p + 1)
              for b in range(1, q // p + 1)}
        tG = {(a, b): max(0, a + b - q) for a in range(1, q + 1)
              for b in range(1, q + 1)}

        def fm(x, y, f, n):
            return sum(x[a - 1] * y[b - 1] * f[a, b] for a in range(1, n + 1)
                       for b in range(1, n + 1))
        ok = all(fm(H.e(c), Res(G.e(b)), fH, q // p)
                 == fm(ind[c], G.e(b), Fh, q)
                 and fm(Res(G.e(b)), H.e(c), fH, q // p)
                 == fm(G.e(b), ind[c], Fh, q)
                 and fm(H.e(c), Res(G.e(b)), tH, q // p)
                 == fm(ind[c], G.e(b), tG, q)
                 for c in range(1, q // p + 1) for b in range(1, q + 1))
        check(ok, '%s: Proposition 5.10.6 (i), (ii)' % tag)
        # Corollary 5.4.11: A(kG) = Im(ind_(H,G)) + Ker(res_(G,H)), product 0
        Im = matrix(QQ, [ind[c] for c in ind]).row_module()
        Rm = matrix(QQ, [res[a] for a in range(1, q + 1)])
        Ker = Rm.left_kernel()
        check(Im.dimension() + Ker.dimension() == q
              and Im.intersection(Ker).dimension() == 0
              and all(G.mul(x, y) == 0 for x in Im.basis()
                      for y in Ker.basis()),
              '%s: Corollary 5.4.11, A(kG) = Im(ind) + Ker(res) as a direct '
              'sum of ideals with zero product' % tag)
    return out


# ===========================================================================
# Section 5.9: psi operations
# ===========================================================================

gap(r'''BensonCh5R.eigenmodules := function(M, n, q)
  # the eps^j eigenspaces (j = 1 .. n) of the cyclic permutation t of the
  # tensor factors of M^(x n), as kG-modules, eps = Z(q)^((q-1)/n)
  local F, gens, mats, d, dim, perm, P, eps, res, j, Pr, B, T, a;
  F := GF(q);
  gens := MTX.Generators(M);
  d := MTX.Dimension(M);
  mats := List(gens, function(g)
    local X, i;
    X := g;
    for i in [2 .. n] do X := KroneckerProduct(X, g); od;
    return X * One(F);
  end);
  dim := d^n;
  perm := List([0 .. dim - 1], function(k)
    local digs, kk, r;
    digs := []; kk := k;
    for r in [1 .. n] do Add(digs, kk mod d); kk := QuoInt(kk, d); od;
    digs := Reversed(digs);
    digs := Concatenation([digs[n]], digs{[1 .. n - 1]});
    return Sum([1 .. n], r -> digs[r] * d^(n - r)) + 1;
  end);
  P := PermutationMat(PermList(perm), dim, F);
  T := GModuleByMats(mats, F);
  eps := Z(q)^((q - 1) / n);
  res := [];
  for j in [1 .. n] do
    Pr := Sum([0 .. n - 1], a -> eps^(-j * a) * P^a);
    B := BaseMat(Pr);
    if Length(B) = 0 then
      Add(res, fail);
    else
      Add(res, MTX.InducedActionSubmodule(T, B));
    fi;
  od;
  return res;
end''')


def section_5_9(green):
    # Ramanujan sums: sum over j prime to d of e^(2 pi i j/d) = mu(d)
    check(all(sum(UCF.zeta(d) ** j for j in range(1, d + 1) if gcd(j, d) == 1)
              == moebius(d) for d in range(1, 61)),
          'p. 194: sum_(1 <= j <= d, (j, d) = 1) e^(2 pi i j/d) = mu(d) for '
          'd <= 60')
    # ---- characteristic zero: Adams operations from the eigenspaces ----
    for src, name in ORDINARY[:9]:
        G = gap(src)
        tbl = G.CharacterTable()
        h = int(tbl.NrConjugacyClasses())
        sizes = ilist(tbl.SizesConjugacyClasses())
        order = int(G.Size())
        irr = [cycl(c.ValuesOfClassFunction()) for c in tbl.Irr()]
        pm = {k: ilist(tbl.PowerMap(k)) for k in range(1, 13)}

        def pw(chi, k):
            return [chi[pm[k][c] - 1] for c in range(h)]

        def inner(a, b):
            return sum(sizes[i] * a[i] * b[i].conjugate()
                       for i in range(h)) / order
        ok = True
        for n in range(2, 7):
            z = UCF.zeta(n)
            for chi in irr:
                # character of the eps^j eigenspace of t on M^(x n):
                # (1/n) sum_a eps^(-ja) chi_(M^n)(t^a g), and t^a has
                # gcd(a, n) cycles of length n/gcd(a, n)
                tr = {}
                for a in range(n):
                    dd = gcd(a, n) if a else n
                    tr[a] = [x ** dd for x in pw(chi, n // dd)]
                eig = {}
                for j in range(1, n + 1):
                    eig[j] = [sum(z ** (-j * a) * tr[a][c] for a in range(n))
                              / n for c in range(h)]
                ok = ok and all(nonneg_int(inner(eig[j], e)) for j in eig
                                for e in irr)
                ok = ok and all(eig[j] == eig[j2] for j in eig for j2 in eig
                                if gcd(j, n) == gcd(j2, n))
                psi = [sum(z ** j * eig[j][c] for j in eig) for c in range(h)]
                mob = [sum(moebius(d) * eig[n // d][c] for d in
                           ZZ(n).divisors()) for c in range(h)]
                ok = ok and psi == pw(chi, n) == mob
        check(ok, '%s: Section 5.9 in characteristic 0, n = 2..6: the '
              'eigenspaces are modules, those of the same order d agree, and '
              'psi^n(M) = sum_d mu(d)[M^(x n)]_d has t_g(psi^n M) = '
              't_(g^n)(M) (Proposition 5.9.2)' % name)

    # ---- characteristic p: kC_p, Jordan blocks -------------------------
    for p, ns, f in ((3, (2,), 1), (5, (2, 4), 1), (7, (2, 3, 6), 1),
                     (2, (3,), 2)):
        q = p ** f
        Gr = green[p]
        rng = range(1, p + 1)
        psi = {}
        for n in ns:
            for m in rng:
                if m ** n > 800:
                    continue
                types = [vector(QQ, ilist(t)) for t in
                         CY['eigen'](m, n, p, q)]
                byorder = {}
                for j in range(1, n + 1):
                    d = n // gcd(j, n)
                    byorder.setdefault(d, []).append(types[j - 1])
                check(all(len(set(tuple(t) for t in v)) == 1
                          for v in byorder.values()),
                      'GF(%d)C%d: the eps^j eigenspaces of J_%d^(x %d) with '
                      'the same order of eps^j are isomorphic (p. 194)'
                      % (q, p, m, n))
                psi[n, m] = sum((moebius(d) * byorder[d][0]
                                 for d in ZZ(n).divisors()),
                                vector(QQ, [0] * p))
                check(sum((i + 1) * psi[n, m][i] for i in range(p)) == m,
                      'GF(%d)C%d: t_1(psi^%d(J_%d)) = dim J_%d (Proposition '
                      '5.9.2 at g = 1)' % (q, p, n, m, m))
        for n in ns:
            have = [m for m in rng if (n, m) in psi]

            def Psi(x, n=n):
                return sum((x[m - 1] * psi[n, m] for m in rng),
                           vector(QQ, [0] * p))
            if len(have) == p:
                ok = all(Psi(Gr.mul(Gr.e(a), Gr.e(b)))
                         == Gr.mul(psi[n, a], psi[n, b])
                         for a in rng for b in rng)
                check(ok, 'GF(%d)C%d: Proposition 5.9.1 (ii), psi^%d(M (x) N) '
                      '= psi^%d(M) psi^%d(N) on all pairs of Jordan blocks'
                      % (q, p, n, n, n))
        for m1, m2 in ((2, 2), (2, 3)):
            n = m1 * m2
            if n not in ns or m1 not in ns or m2 not in ns:
                continue
            if not all((m1, m) in psi and (m2, m) in psi for m in rng):
                continue
            for m in rng:
                if (n, m) not in psi:
                    continue
                inner_ = psi[m2, m]
                comp = sum((inner_[l - 1] * psi[m1, l] for l in rng),
                           vector(QQ, [0] * p))
                check(comp == psi[n, m],
                      'GF(%d)C%d: Proposition 5.9.1 (iii) (author\'s '
                      'addition), psi^%d psi^%d (J_%d) = psi^%d (J_%d)'
                      % (q, p, m1, m2, m, n, m))

    # ---- Proposition 5.9.2 with p'-elements: modules over finite fields --
    for src, p, q, n in (('SymmetricGroup(3)', 2, 4, 3),
                         ('SymmetricGroup(3)', 3, 9, 2),
                         ('SymmetricGroup(3)', 3, 9, 4),
                         ('AlternatingGroup(4)', 2, 4, 3),
                         ('AlternatingGroup(4)', 3, 9, 2),
                         ('AlternatingGroup(5)', 2, 16, 3),
                         ('AlternatingGroup(5)', 2, 16, 5),
                         ('SymmetricGroup(4)', 3, 9, 2)):
        G = gap(src)
        F = libgap.GF(q)
        regs = [c.Representative() for c in G.ConjugacyClasses()
                if int(c.Representative().Order()) % p != 0]
        gG = G.GeneratorsOfGroup()
        mods = [(gG, M) for M in T['tsmodules'](G, F)]
        irrm = gap('function(G, F) return IrreducibleModules(G, F, 0); end')(
            G, F)
        mods += [(irrm[0], M) for M in irrm[1]]
        for gens, M in mods:
            if int(M['dimension']) ** n > 700:
                continue
            eig = R['eigenmodules'](M, n, q)
            vals = [cycl(R['brauer_gens'](G, gens, E, regs))
                    if E != gap('fail') else [UCF(0)] * len(regs)
                    for E in eig]
            psi = [sum(UCF.zeta(n) ** j * vals[j - 1][c]
                       for j in range(1, n + 1)) for c in range(len(regs))]
            target = cycl(R['brauer_gens'](G, gens, M,
                                           [g ** n for g in regs]))
            check(psi == target,
                  '%s over GF(%d): Proposition 5.9.2, t_g(psi^%d(M)) = '
                  't_(g^%d)(M) (dim M = %d)'
                  % (src, q, n, n, int(M['dimension'])))



# ===========================================================================
# Sections 5.8, 5.10, 5.11 with the MeatAxe: forms, u, v, tau_0, tau_1
# ===========================================================================

gap('BensonCh5M := 0')
gap(r'''BensonCh5M := rec(
  hom := function(A, B)
    return Length(MTX.BasisModuleHomomorphisms(A, B));
  end,

  # rank of sum_g g on Hom_k(A, B) (right modules: Y -> A(g)^-1 Y B(g))
  trrank := function(G, A, B)
    local el, MA, MB, S, i;
    el := AsList(G);
    MA := BensonCh5R.matsof(G, GeneratorsOfGroup(G), A, el);
    MB := BensonCh5R.matsof(G, GeneratorsOfGroup(G), B, el);
    S := Sum([1 .. Length(el)], i -> KroneckerProduct(TransposedMat(MB[i]),
                                                      MA[i]^-1));
    return RankMat(S);
  end,

  # d(N) = dim End(N)/J(End(N))
  dEnd := function(N)
    local E, A;
    E := MTX.BasisModuleEndomorphisms(N);
    A := Algebra(MTX.Field(N), E);
    return Dimension(A) - Dimension(RadicalOfAlgebra(A));
  end,

  dsum := function(L, F)
    return GModuleByMats(List([1 .. Length(MTX.Generators(L[1]))],
      i -> DirectSumMat(List(L, M -> MTX.Generators(M)[i]))), F);
  end,

  regular := function(G, F)
    return BensonCh5T.permmodule(G, TrivialSubgroup(G), F);
  end,

  pims := function(G, F)
    local L, S;
    L := [];
    for S in BensonCh5T.summands(BensonCh5M.regular(G, F)) do
      if BensonCh5T.position(L, S) = fail then Add(L, S); fi;
    od;
    return L;
  end,

  # non-projective part of the kernel of a projective cover: Omega(M)
  omega := function(G, M, F)
    local R, homs, chosen, stack, r, h, test, s, K, sub, pims, out, S;
    if not IsBound(BensonCh5M.pimcache) then BensonCh5M.pimcache := []; fi;
    R := BensonCh5M.regular(G, F);
    homs := MTX.BasisModuleHomomorphisms(R, M);
    chosen := []; r := 0;
    for h in homs do
      test := Concatenation(List(Concatenation(chosen, [h]), x -> x));
      if RankMat(test) > r then
        Add(chosen, h); r := RankMat(test);
      fi;
      if r = MTX.Dimension(M) then break; fi;
    od;
    stack := Concatenation(chosen);
    s := Length(chosen);
    K := NullspaceMat(stack);
    if Length(K) = 0 then return fail; fi;
    sub := MTX.InducedActionSubmodule(
      BensonCh5M.dsum(List([1 .. s], i -> R), F), K);
    pims := First(BensonCh5M.pimcache, x -> IsIdenticalObj(x[1], G)
                                            and x[2] = F);
    if pims = fail then
      pims := [G, F, BensonCh5M.pims(G, F)];
      Add(BensonCh5M.pimcache, pims);
    fi;
    pims := pims[3];
    out := Filtered(BensonCh5T.summands(sub),
                    S -> BensonCh5T.position(pims, S) = fail);
    if Length(out) = 0 then return fail; fi;
    return BensonCh5M.dsum(out, F);
  end,

  omegainv := function(G, M, F)
    local O;
    O := BensonCh5M.omega(G, DualGModule(M), F);
    if O = fail then return fail; fi;
    return DualGModule(O);
  end,

  # all quotients P/Rad^i(P) of the projective indecomposables
  pimquotients := function(G, F)
    local out, P, B, chain, cur, rb, i;
    out := [];
    for P in BensonCh5M.pims(G, F) do
      B := IdentityMat(MTX.Dimension(P), F);
      chain := [];
      while Length(B) > 0 do
        cur := MTX.InducedActionSubmodule(P, B);
        rb := MTX.BasisRadical(cur);
        if Length(rb) = 0 then B := []; else B := rb * B; fi;
        if Length(B) > 0 then Add(chain, B); fi;
      od;
      Add(out, P);
      for B in chain do
        Add(out, MTX.InducedActionFactorModule(P, B));
      od;
    od;
    return out;
  end,

  # submodule lattice is a chain: the module is uniserial
  uniserial := function(M)
    local subs, i, j;
    subs := MTX.BasesSubmodules(M);
    return ForAll(subs, a -> ForAll(subs, b -> Length(a) = 0
      or Length(b) = 0
      or RankMat(Concatenation(a, b)) = Maximum(Length(a), Length(b))));
  end,

  # 2n-dimensional modules of V4 = <a, b>: a -> 1 + (0 0; A 0),
  # b -> 1 + (0 0; B 0)
  Emod := function(A, B, F)
    local n, Z, I, mk;
    n := Length(A);
    Z := NullMat(n, n, F); I := IdentityMat(2 * n, F);
    mk := X -> I + Concatenation(List(Z, r -> Concatenation(r, Z[1] * 0)),
                                 List(X, r -> Concatenation(r, Z[1] * 0)));
    return GModuleByMats([mk(A), mk(B)], F);
  end
)''')
MX = gap('BensonCh5M')


def nakayama_green(src, p, q):
    """All indecomposables (quotients of the projective indecomposables) of
    a group whose blocks are uniserial, with tensor structure constants."""
    G = gap(src)
    F = libgap.GF(q)
    L = list(MX['pimquotients'](G, F))
    uniq = []
    for M in L:
        if not any(bool(T['iso'](M, X)) for X in uniq):
            uniq.append(M)
    L = sorted(uniq, key=lambda M: int(M['dimension']))
    Lg = libgap(L)
    n = len(L)
    N = {}
    for i in range(n):
        for j in range(i, n):
            TP = gap('TensorProductGModule')(L[i], L[j])
            c = T['decompose'](Lg, TP)
            assert c != gap('fail')
            N[i, j] = N[j, i] = vector(QQ, ilist(c))
    return G, F, L, Lg, N


def section_forms_and_duality():
    # ---- groups with uniserial blocks: all indecomposables ---------------
    for src, name, p, q, sub in (
            ('SymmetricGroup(3)', 'S3', 3, 3, '(1,2)'),
            ('AlternatingGroup(4)', 'A4', 3, 3, None),
            ('SmallGroup(12,1)', 'C3:C4', 3, 9, None),
            ('DihedralGroup(10)', 'D10', 5, 5, None)):
        G, F, L, Lg, N = nakayama_green(src, p, q)
        n = len(L)
        tag = '%s over GF(%d)' % (name, q)
        dims = [int(M['dimension']) for M in L]
        Pims = MX['pims'](G, F)
        proj = [any(bool(T['iso'](M, P)) for P in Pims) for M in L]
        nproj = sum(proj)
        P0 = libgap.SylowSubgroup(G, p)
        check(all(bool(MX['uniserial'](P)) for P in Pims)
              and all(bool(MX['uniserial'](M)) for M in L),
              '%s: the %d projective indecomposables are uniserial (so kG is '
              'a Nakayama algebra and its %d indecomposable modules are the '
              'quotients P/Rad^i P)' % (tag, nproj, n))
        if bool(G.IsNormal(P0)) and bool((G / P0).IsCyclic()):
            # p-hypo-elementary: Lemma 5.8.6
            check(all(bool(MX['uniserial'](M)) for M in L)
                  and all(len(T['summands'](T['restrict'](G, P0, M))) == 1
                          for M in L),
                  '%s: Lemma 5.8.6, every indecomposable is uniserial and '
                  'stays indecomposable on restriction to D = O_p(H)' % tag)
        one = vector(QQ, [1 if (dims[i] == 1 and all(
            m == m ** 0 for m in L[i]['generators'])) else 0
            for i in range(n)])

        def mul(x, y):
            r = vector(QQ, [0] * n)
            for i in range(n):
                for j in range(n):
                    if x[i] and y[j]:
                        r += x[i] * y[j] * N[i, j]
            return r
        E = [vector(QQ, [1 if j == i else 0 for j in range(n)])
             for i in range(n)]
        Ls = [matrix(QQ, [mul(E[i], E[j]) for j in range(n)]).transpose()
              for i in range(n)]
        check(reduced(Ls),
              '%s: Theorem 5.8.7 (Green, O\'Reilly), A(kG) has no non-zero '
              'nilpotent elements' % tag)
        div = [i for i in range(n) if dims[i] % p == 0]
        nd = [i for i in range(n) if dims[i] % p != 0]
        Lq = [matrix(QQ, [[Ls[a][i, j] for j in nd] for i in nd]) for a in nd]
        check(all(N[a, b][c] == 0 for a in range(n) for b in div
                  for c in nd) and reduced(Lq),
              '%s: Lemma 5.8.3 and Theorem 5.8.5, A(G; p) is an ideal and '
              'A(G)/A(G; p) has no non-zero nilpotent elements' % tag)
        if sub is not None:
            H = G.Subgroup([gap(sub)])
            img = []
            for M in T['tsmodules'](H, F):
                img.append(vector(QQ, ilist(T['decompose'](
                    Lg, T['induce'](G, H, M)))))
            span = matrix(QQ, img).row_module()
            check(span == matrix(QQ, [E[i] for i in div]).row_module(),
                  '%s: Lemma 5.8.6, A(H; p) = Im(ind_(H_1, H)) with H_1 of '
                  'index p' % tag)
        # forms
        Hm = matrix(ZZ, n, n, lambda i, j: int(MX['hom'](L[i], L[j])))
        Sm = matrix(ZZ, n, n, lambda i, j: int(MX['trrank'](G, L[i], L[j])))
        d = [int(MX['dEnd'](M)) for M in L]
        check(all(x == 1 for x in d),
              '%s: the indecomposables are absolutely indecomposable, '
              'd(N) = 1' % tag)
        triv = [i for i in range(n) if one[i]][0]
        Pk = [i for i in range(n) if proj[i] and int(MX['hom'](L[i], L[triv]))
              > 0][0]
        Om = MX['omega'](G, L[triv], F)
        Oi = MX['omegainv'](G, L[triv], F)
        iOm = [i for i in range(n) if bool(T['iso'](L[i], Om))][0]
        iOi = [i for i in range(n) if bool(T['iso'](L[i], Oi))][0]
        u = E[Pk] - E[iOi]
        v = E[Pk] - E[iOm]
        check(mul(u, v) == one, '%s: Lemma 5.10.3, u v = 1' % tag)
        dual = [[i for i in range(n) if bool(T['iso'](
            L[i], gap('DualGModule')(L[j])))][0] for j in range(n)]
        ok = True
        for a in range(n):
            for b in range(n):
                mult = N[dual[a], b][Pk]
                ua = mul(u, E[a])
                iii = sum(ua[i] * Hm[i, b] for i in range(n))
                ok = ok and Sm[a, b] == mult == iii == Sm[b, a]
        check(ok, '%s: Lemma 5.10.2, <[M], [N]> = rank of sum g on Hom_k = '
              'multiplicity of P_k in M* (x) N = (u.[M], [N]), symmetric, '
              'all pairs' % tag)

        def f(x, y, Mt):
            return (x * Mt * y)
        ok = all(f(x, y, Hm) == f(mul(v, x), y, Sm) == f(x, mul(u, y), Sm)
                 and f(x, y, Sm) == f(mul(u, x), y, Hm) == f(x, mul(v, y), Hm)
                 and f(x, y, Hm) == f(y, mul(mul(v, v), x), Hm)
                 == f(mul(mul(u, u), y), x, Hm) for x in E for y in E)
        check(ok, '%s: Proposition 5.10.4 (i)-(iii), all pairs' % tag)
        # Theorem 5.11.1: tau_0 = the dual basis for ( , )
        tau0 = [Hm.change_ring(QQ).solve_right(E[j] * d[j]) for j in range(n)]
        Om2 = {}
        for j in range(n):
            if proj[j]:
                rad = gap('function(M) local b; b := MTX.BasisRadical(M); '
                          'if Length(b) = 0 then return fail; fi; return '
                          'MTX.InducedActionSubmodule(M, b); end')(L[j])
                c = vector(QQ, [0] * n) if rad == gap('fail') else \
                    vector(QQ, ilist(T['decompose'](Lg, rad)))
                check(tau0[j] == E[j] - c,
                      '%s: Section 5.11, tau_0[N] = [N] - [Rad N] for N '
                      'projective (dim %d)' % (tag, dims[j]))
            else:
                O1 = MX['omega'](G, L[j], F)
                O2 = MX['omega'](G, O1, F)
                k2 = [i for i in range(n) if bool(T['iso'](L[i], O2))][0]
                Om2[j] = k2
                Emid = E[j] + E[k2] - tau0[j]
                check(all(x >= 0 for x in Emid)
                      and sum(Emid[i] * dims[i] for i in range(n))
                      == dims[j] + dims[k2],
                      '%s: Theorem 5.11.1, tau_0[N] = [N] + [Omega^2 N] - [E] '
                      'with E a module of dimension dim N + dim Omega^2 N '
                      '(dim N = %d)' % (tag, dims[j]))
        # Theorem 5.11.3: tau_1 = dual basis for < , >
        check(Sm.det() != 0, '%s: < , > is non-singular' % tag)
        tau1 = [Sm.change_ring(QQ).solve_right(E[j] * d[j]) for j in range(n)]
        for j in range(n):
            check(tau1[j] == mul(u, tau0[j]),
                  '%s: tau_1[N] = u.tau_0[N] (dim N = %d)' % (tag, dims[j]))
            if proj[j]:
                top = gap('function(M) local b; b := MTX.BasisRadical(M); '
                          'if Length(b) = 0 then return M; fi; return '
                          'MTX.InducedActionFactorModule(M, b); end')(L[j])
                c = vector(QQ, ilist(T['decompose'](Lg, top)))
                check(tau1[j] == c,
                      '%s: Theorem 5.11.3, tau_1[P_S] = [S]' % tag)
            else:
                Oinv = MX['omegainv'](G, L[j], F)
                Oone = MX['omega'](G, L[j], F)
                ji = [i for i in range(n) if bool(T['iso'](L[i], Oinv))][0]
                jo = [i for i in range(n) if bool(T['iso'](L[i], Oone))][0]
                # X: middle term of the almost split sequence terminating in
                # Omega^-1(N), from Theorem 5.11.1: [X] = [M'] + [Omega^2 M']
                # - tau_0[M'] with M' = Omega^-1(N), Omega^2 M' = Omega(N)
                X = E[ji] + E[Om2[ji]] - tau0[ji]
                check(Om2[ji] == jo
                      and tau1[j] == X - E[ji] - E[jo],
                      '%s: Theorem 5.11.3 (corrected), tau_1[N] = [X] - '
                      '[Omega^-1 N] - [Omega N] with 0 -> Omega N -> X -> '
                      'Omega^-1 N -> 0 almost split (dim N = %d)'
                      % (tag, dims[j]))
        check(Hm.det() != 0,
              '%s: Corollary 5.11.2 (the matrix dim Hom(M_i, M_j) is '
              'invertible)' % tag)

    # ---- the Klein four group over GF(2) ---------------------------------
    G = gap('Group((1,2), (3,4))')
    F = libgap.GF(2)
    one, zero = libgap.Z(2) ** 0, 0 * libgap.Z(2)
    k = T['permmodule'](G, G, F)
    P = MX['regular'](G, F)
    O = {0: k}
    for i in range(1, 4):
        O[i] = MX['omega'](G, O[i - 1], F)
        O[-i] = MX['omegainv'](G, O[-i + 1], F)
    Nil = libgap([[zero, zero], [one, zero]])
    I1, I2 = libgap([[one]]), libgap.IdentityMat(2, F)
    E1 = {lam: MX['Emod'](libgap([[a]]), libgap([[b]]), F)
          for lam, (a, b) in {'0': (one, zero), '1': (one, one),
                              'oo': (zero, one)}.items()}
    E2 = {'0': MX['Emod'](I2, Nil, F), '1': MX['Emod'](I2, I2 + Nil, F),
          'oo': MX['Emod'](Nil, I2, F)}
    comp = libgap([[zero, one], [one, one]])  # x^2 + x + 1
    W = MX['Emod'](I2, comp, F)
    comp2 = libgap([[zero, one, zero, zero], [zero, zero, one, zero],
                    [zero, zero, zero, one], [one, zero, one, zero]])
    # companion matrix of (x^2 + x + 1)^2 = x^4 + x^2 + 1
    W2 = MX['Emod'](libgap.IdentityMat(4, F), comp2, F)
    test = [('k', k), ('P', P)] + [('Omega^%d k' % i, O[i])
                                    for i in (1, -1, 2, -2, 3, -3)] \
        + [('E1(%s)' % l, E1[l]) for l in E1] \
        + [('E2(%s)' % l, E2[l]) for l in E2] + [('W', W), ('W2', W2)]
    dimO = {i: int(O[i]['dimension']) for i in O}
    check(all(dimO[i] == 2 * abs(i) + 1 for i in O),
          'V4: dim Omega^n(k) = 2|n| + 1 (n = -3..3)')
    check(all(int(MX['dEnd'](M)) == (2 if nm in ('W', 'W2') else 1)
              for nm, M in test),
          'V4 over GF(2): d(N) = dim End(N)/J = 2 for the modules W, W2 of '
          'the point x^2 + x + 1 (End/J = GF(4)), d = 1 for the others')
    names = [nm for nm, _ in test]
    mods = dict(test)

    cache = {}

    def hom(a, b):
        if ('h', a, b) not in cache:
            cache['h', a, b] = int(MX['hom'](mods[a], mods[b]))
        return cache['h', a, b]

    def tr(a, b):
        if ('t', a, b) not in cache:
            cache['t', a, b] = int(MX['trrank'](G, mods[a], mods[b]))
        return cache['t', a, b]

    def homsum(x, b):
        return sum(c * hom(a, b) for a, c in x.items())

    def homsum2(a, x):
        return sum(c * hom(a, b) for b, c in x.items())

    def trsum(a, x):
        return sum(c * tr(a, b) for b, c in x.items())

    # Theorem 5.11.1: almost split sequences 0 -> Omega^2 k -> 2 Omega k ->
    # k -> 0, 0 -> E -> E2 -> E -> 0 (tubes of rank one), 0 -> Rad P -> P +
    # Rad P/Soc P -> P/Soc P -> 0 (Proposition 4.12.7)
    tau0 = {'k': {'k': 1, 'Omega^2 k': 1, 'Omega^1 k': -2},
            'P': {'P': 1, 'Omega^1 k': -1},
            'W': {'W': 2, 'W2': -1}}
    for l in E1:
        tau0['E1(%s)' % l] = {'E1(%s)' % l: 2, 'E2(%s)' % l: -1}
    for N, t0 in tau0.items():
        dN = int(MX['dEnd'](mods[N]))
        check(all(homsum2(Np, t0) == (dN if Np == N else 0) for Np in names),
              'V4: Theorem 5.11.1, ([N\'], tau_0[%s]) = d(N) delta for the %d '
              'test modules N\'' % (N, len(names)))
    # the last sentence of Theorem 5.11.1: (x, tau_0(x)) for x = [W]
    val = homsum2('W', tau0['W'])
    check(val == 2 * 1, 'V4: Theorem 5.11.1 (corrected last sentence), '
          '(x, tau_0 x) = |a|^2 d(W) = 2 for x = [W]')
    refuted(val == 1, 'V4: Theorem 5.11.1 as printed, (x, tau_0 x) = '
            'sum |a_i|^2 = 1 for x = [W]')
    G3 = gap('CyclicGroup(IsPermGroup, 3)')
    S2 = [M for M in gap('IrreducibleModules')(G3, F, 0)[1]
          if int(M['dimension']) == 2][0]
    val3 = int(MX['hom'](S2, S2))
    check(val3 == 2 and int(MX['dEnd'](S2)) == 2,
          'GF(2)C3: the 2-dimensional simple projective module S has '
          'tau_0[S] = [S] - [Rad S] = [S] and (x, tau_0 x) = dim End(S) = 2 = '
          'd(S) for x = [S]')
    refuted(val3 == 1, 'GF(2)C3: Theorem 5.11.1 as printed, (x, tau_0 x) = '
            'sum |a_i|^2 = 1 for x = [S]')
    # Lemma 5.10.2 on the test modules: rank of the trace, multiplicity of
    # P in M* (x) N, (u[M], [N])
    for a in names:
        for b in names:
            if int(mods[a]['dimension']) * int(mods[b]['dimension']) > 40:
                continue
            TP = gap('function(A, B) return TensorProductGModule('
                     'DualGModule(A), B); end')(mods[a], mods[b])
            mult = sum(1 for S in T['summands'](TP) if bool(T['iso'](S, P)))
            Pa = gap('TensorProductGModule')(P, mods[a])
            Oa = gap('TensorProductGModule')(O[-1], mods[a])
            iii = int(MX['hom'](Pa, mods[b])) - int(MX['hom'](Oa, mods[b]))
            check(tr(a, b) == mult == iii == tr(b, a),
                  'V4: Lemma 5.10.2 for M = %s, N = %s (<M, N> = %d)'
                  % (a, b, mult))
    # Lemma 5.10.3: u v = 1 in a(V4)
    terms = [(1, P, P), (-1, P, O[-1]), (-1, O[1], P), (1, O[1], O[-1])]
    tot = {}
    basis = [k, P, O[1], O[-1], O[2], O[-2]]
    BL = libgap(basis)
    for c, A, Bm in terms:
        dec = ilist(T['decompose'](BL, gap('TensorProductGModule')(A, Bm)))
        for i, x in enumerate(dec):
            tot[i] = tot.get(i, 0) + c * x
    check(tot == {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
          'V4: Lemma 5.10.3, ([P] - [Omega k])([P] - [Omega^-1 k]) = [k]')
    # Lemma 5.10.5 and its proof: res to C2 = <(1,2)>, Schanuel
    H = G.Subgroup([gap('(1,2)')])
    kH = T['permmodule'](H, H, F)
    PH = MX['regular'](H, F)
    OH = MX['omega'](H, kH, F)
    lhs = MX['dsum'](libgap([T['restrict'](G, H, O[1]), PH]), F)
    rhs = MX['dsum'](libgap([OH, T['restrict'](G, H, P)]), F)
    check(bool(T['iso'](lhs, rhs)),
          'V4 > C2: proof of Lemma 5.10.5, Schanuel for the displayed '
          'sequences: Omega(k)_kG|H + (P_k)_kH ~ Omega(k)_kH + (P_k)_kG|H, '
          'i.e. res(v_kG) = v_kH (the statement proved by these sequences)')
    HL = libgap([kH, PH])
    rv = vector(ZZ, ilist(T['decompose'](HL, T['restrict'](G, H, P)))) - \
        vector(ZZ, ilist(T['decompose'](HL, T['restrict'](G, H, O[1]))))
    ru = vector(ZZ, ilist(T['decompose'](HL, T['restrict'](G, H, P)))) - \
        vector(ZZ, ilist(T['decompose'](HL, T['restrict'](G, H, O[-1]))))
    check(rv == ru == vector(ZZ, [-1, 1]),
          'V4 > C2: Lemma 5.10.5, res(u_kG) = u_kH, res(v_kG) = v_kH')
    # Proposition 5.10.6 for V4 > C2
    Hm = {'k': kH, 'P': PH}
    ok = True
    for xa, X in Hm.items():
        IX = T['induce'](G, H, X)
        for b in names:
            if int(mods[b]['dimension']) > 5:
                continue
            RY = T['restrict'](G, H, mods[b])
            ok = ok and int(MX['hom'](X, RY)) == int(MX['hom'](IX, mods[b]))
            ok = ok and int(MX['hom'](RY, X)) == int(MX['hom'](mods[b], IX))
            ok = ok and int(MX['trrank'](H, X, RY)) == int(
                MX['trrank'](G, IX, mods[b]))
    check(ok, 'V4 > C2: Proposition 5.10.6 (i), (ii) (Frobenius reciprocity '
          'for both forms)')
    # Theorem 5.11.3 (corrected): X for N = k is P + 2k (the sequence with
    # projective middle term, Proposition 4.12.7), for N = Omega^n k,
    # n != 0, it is 2 Omega^n k, for the even-dimensional N it is E2 or W2.
    tau1 = {'k': {'P': 1, 'k': 2, 'Omega^-1 k': -1, 'Omega^1 k': -1},
            'Omega^1 k': {'Omega^1 k': 2, 'k': -1, 'Omega^2 k': -1},
            'Omega^-1 k': {'Omega^-1 k': 2, 'k': -1, 'Omega^-2 k': -1},
            'Omega^2 k': {'Omega^2 k': 2, 'Omega^1 k': -1, 'Omega^3 k': -1},
            'P': {'k': 1}, 'W': {'W2': 1, 'W': -2}}
    for l in E1:
        tau1['E1(%s)' % l] = {'E2(%s)' % l: 1, 'E1(%s)' % l: -2}
    for N, t1 in tau1.items():
        dN = int(MX['dEnd'](mods[N]))
        check(all(trsum(Np, t1) == (dN if Np == N else 0) for Np in names),
              'V4: Theorem 5.11.3 (corrected), <[N\'], tau_1[%s]> = d(N) '
              'delta for the %d test modules N\'' % (N, len(names)))
    check(all(bool(T['iso'](MX['omega'](G, E1[l], F), E1[l])) for l in E1)
          and bool(T['iso'](MX['omega'](G, W, F), W)),
          'V4: Omega(E) ~ E for the even-dimensional modules used above')
    # the printed Theorem 5.11.3: an almost split sequence terminating in
    # Omega(k) begins with Omega^2(Omega k) = Omega^3 k (Proposition
    # 4.12.8), not with Omega^-1 k
    refuted(dimO[3] == dimO[-1],
            'Theorem 5.11.3 as printed: 0 -> Omega^-1(k) -> X -> Omega(k) '
            '-> 0 almost split needs Omega^-1 k ~ Omega^3 k (dimensions %d, '
            '%d)'
            % (dimO[-1], dimO[3]))
    printed = {'Omega^2 k': 2, 'Omega^-1 k': -1, 'Omega^1 k': -1}
    refuted(trsum('k', printed) == 1,
            'Theorem 5.11.3 as printed for N = k, with X the middle term '
            '2 Omega^2 k of the almost split sequence terminating in Omega(k)')
    # p. 200: u.tau_0[k] computed in a(V4); modulo projectives it is
    # -Omega^-1(tau_0[k]) = 2[k] - [Omega^-1 k] - [Omega k], but not exactly:
    # the projective summand P of the middle term P + 2k is lost
    basis = [k, P, O[1], O[-1], O[2], O[-2], O[3], O[-3]]
    BL = libgap(basis)
    utau = vector(ZZ, [0] * len(basis))
    for c1, A1 in ((1, P), (-1, O[-1])):
        for c2, A2 in ((1, k), (1, O[2]), (-2, O[1])):
            utau += c1 * c2 * vector(ZZ, ilist(T['decompose'](
                BL, gap('TensorProductGModule')(A1, A2))))
    check(utau == vector(ZZ, [2, 1, -1, -1, 0, 0, 0, 0]),
          'V4: u.tau_0[k] = [P] + 2[k] - [Omega^-1 k] - [Omega k] = tau_1[k] '
          '(Theorem 5.11.3 with X = P + k + k)')
    refuted(utau == vector(ZZ, [2, 0, -1, -1, 0, 0, 0, 0]),
            'p. 200: u.tau_0[N] = -[Omega^-1 N] - [Omega^-1 M] + '
            '[Omega^-1 E] "without working modulo projectives", for N = k '
            '(M = Omega^2 k, E = 2 Omega k, Omega^-1 E = 2k)')



# ===========================================================================
# Section 5.6 with characters: Artin, Brauer, Witt-Berman
# ===========================================================================

gap(r'''BensonCh5R.induced_irr := function(G, H)
  # the characters induced from Irr(H), as coordinate vectors in Irr(G)
  local tG;
  tG := CharacterTable(G);
  return List(Irr(CharacterTable(H)), chi -> List(Irr(tG),
    psi -> ScalarProduct(InducedClassFunction(chi, G), psi)));
end''')
gap(r'''BensonCh5R.induced_real := function(G, H)
  # induced from the characters of real representations of H: chi
  # (indicator 1), chi + bar chi (indicator 0), 2 chi (indicator -1)
  local tG, tH, ind, out, i, chi, rc;
  tG := CharacterTable(G); tH := CharacterTable(H);
  ind := Indicator(tH, 2);
  out := [];
  for i in [1 .. Length(Irr(tH))] do
    chi := Irr(tH)[i];
    if ind[i] = 1 then rc := chi;
    elif ind[i] = -1 then rc := 2 * chi;
    else rc := chi + ComplexConjugate(chi);
    fi;
    Add(out, List(Irr(tG), psi -> ScalarProduct(InducedClassFunction(rc, G),
                                               psi)));
  od;
  return out;
end''')
gap(r'''BensonCh5R.hyper := function(H, q)
  # [true, a] if O^q(H) = <a> is cyclic, else [false]
  local O;
  O := Subgroup(H, Filtered(AsList(H), x -> Order(x) mod q <> 0));
  if IsCyclic(O) then
    if Size(O) = 1 then return [true, One(H)]; fi;
    return [true, First(AsList(O), x -> Order(x) = Size(O))];
  fi;
  return [false];
end''')


def k_elementary(H, gal_ok, literal):
    """Definition 5.6.6 for H with the Galois group of k(eps)/k given by
    gal_ok(t, m) (t a unit mod m): corrected reading (eps of order |a|, t
    modulo |a|) or the literal reading (eps of order |H|, every integer t
    with b a b^-1 = a^t)."""
    order = int(H.Size())
    primes = sorted(set(int(r) for r, _ in factor(order))) \
        if order > 1 else [2]
    for qq in primes + [nextp for nextp in (2, 3, 5, 7) if order % nextp]:
        res = R['hyper'](H, qq)
        if not bool(res[0]):
            continue
        a = res[1]
        m = int(a.Order())
        ok = True
        for b in H.GeneratorsOfGroup() if order > 1 else []:
            c = b * a * b ** -1
            tb = [t for t in range(m) if a ** t == c][0] if m > 1 else 0
            if literal:
                ts = set((tb + m * s) % order for s in range(order))
                ok = ok and all(gcd(t, order) == 1 and gal_ok(t, order)
                                for t in ts)
            else:
                ok = ok and gal_ok(tb % m, m)
        if literal:
            # b = 1 also gives every t = 1 mod m
            ts = set((1 + m * s) % order for s in range(order))
            ok = ok and all(gcd(t, order) == 1 and gal_ok(t, order)
                            for t in ts)
        if ok:
            return True
    return False


def gal_C(t, m):
    return t % m == 1 % m


def gal_R(t, m):
    return t % m in (1 % m, (-1) % m)


def lattice_contains(vecs, target, ring=ZZ):
    if not vecs:
        return False
    return vector(ring, target) in matrix(ring, vecs).row_module()


def section_5_6_characters():
    for src, name in ORDINARY + [('SmallGroup(4,2)', 'V4'),
                                 ('SmallGroup(8,5)', 'C2^3'),
                                 ('SmallGroup(16,14)', 'C2^4'),
                                 ('SmallGroup(18,4)', '(C3xC3):C2'),
                                 ('SmallGroup(24,13)', 'C2 x A4'),
                                 ('SmallGroup(20,3)', 'C5:C4')]:
        G = gap(src)
        tbl = G.CharacterTable()
        h = int(tbl.NrConjugacyClasses())
        reps = list(B['classes'](G))
        order = int(G.Size())
        one = [1 if all(x == 1 for x in cycl(chi.ValuesOfClassFunction()))
               else 0 for chi in tbl.Irr()]
        ind = {i: [vector(QQ, ilist(r)) for r in R['induced_irr'](G, H)]
               for i, H in enumerate(reps)}
        cyclic = [i for i, H in enumerate(reps) if bool(H.IsCyclic())]
        Lc = [v for i in cyclic for v in ind[i]]
        check(matrix(QQ, Lc).rank() == h,
              '%s: Theorem 5.6.1 (Artin), CC (x) R(CG) is the sum of the '
              'images of induction from cyclic subgroups' % name)
        m = 1
        while not lattice_contains(Lc, [m * x for x in one]):
            m += 1
        check(all(order % r == 0 for r, _ in factor(m)) if m > 1 else True,
              '%s: R(G)[|G|^-1] = sum over cyclic H of Im(ind) (p. 187): '
              'the least m with m.1 induced from cyclic subgroups is %d'
              % (name, m))
        # the map lambda of the diagram: phi(e_H) = 0 unless H is cyclic
        Bg = Burnside(G, name)
        permchar = gap('function(G, H) return ValuesOfClassFunction('
                       'InducedClassFunction(TrivialCharacter(H), G)); end')
        perm = [vector(UCF, cycl(permchar(G, H))) for H in Bg.reps]
        clreps = [c.Representative() for c in tbl.ConjugacyClasses()]
        cyc_of = [Bg.which(G.Subgroup([g])) for g in clreps]
        ok = all(perm[i][c] == UCF(Bg.M[i, cyc_of[c] - 1])
                 for i in range(Bg.n) for c in range(h))
        Minv = Bg.M.change_ring(QQ).inverse()
        for j in range(Bg.n):
            e = vector(QQ, [1 if l == j else 0 for l in range(Bg.n)]) * Minv
            val = sum((UCF(e[i]) * perm[i] for i in range(Bg.n)),
                      vector(UCF, [0] * h))
            exp = [UCF(1) if cyc_of[c] - 1 == j else UCF(0) for c in range(h)]
            ok = ok and list(val) == exp
        check(ok, '%s: the diagram of the proof of Theorem 5.6.1 commutes: '
              'trace on a permutation module = number of fixed points, and '
              'phi(e_H) is the indicator of the elements generating a '
              'conjugate of H (zero unless H is cyclic)' % name)
        # Brauer (Proposition 5.6.3, Theorem 5.6.4) in characteristic 0
        primes = sorted(set(int(r) for r, _ in factor(order)))
        allh = []
        for qq in primes:
            hyp = [i for i, H in enumerate(reps)
                   if bool(R['hyper'](H, qq)[0])]
            allh += hyp
            V = [v for i in hyp for v in ind[i]]
            A = matrix(ZZ, V)
            D, U, W = A.smith_form()
            eW = vector(QQ, one) * W.change_ring(QQ)
            r = min(D.nrows(), D.ncols())
            loc = all((eW[k] / D[k, k]).denominator() % qq != 0 if k < r and
                      D[k, k] != 0 else eW[k] == 0 for k in range(W.ncols()))
            check(loc, '%s: Proposition 5.6.3, 1 in the ZZ_(%d)-span of the '
                  'characters induced from %d-hyperelementary subgroups'
                  % (name, qq, qq))
        check(lattice_contains([v for i in set(allh) for v in ind[i]], one),
              '%s: Theorem 5.6.4 (Brauer), R(CG) = sum of Im(ind) over the '
              'hyperelementary subgroups' % name)
        # p. 186: phi kills the q-local idempotent sum_(O^q(H) = H_0) e_H iff
        # no H in it is cyclic (characteristic 0), resp. a cyclic p'-group
        # (characteristic p; the Brauer character of phi(e_H) at g is
        # f_<g>(e_H))
        for qq in primes:
            opc = ilist(B['Op_class'](G, Bg.reps, qq))
            comps = {}
            for i in range(Bg.n):
                comps.setdefault(opc[i], []).append(i)
            cyc_cl = [bool(H.IsCyclic()) for H in Bg.reps]
            ok0 = all((not any(cyc_cl[i] for i in c))
                      == (not cyc_cl[h0 - 1]) for h0, c in comps.items())
            check(ok0, '%s, q = %d: p. 186, in characteristic 0 phi kills '
                  'sum_(O^q(H) = H_0) e_H iff H_0 is non-cyclic' % (name, qq))
            for p in primes:
                killed = {h0: not any(cyc_cl[i] and Bg.sizes[i] % p != 0
                                      for i in c) for h0, c in comps.items()}
                check(all(killed[h0] for h0 in comps
                          if not cyc_cl[h0 - 1]),
                      '%s, q = %d, p = %d: p. 186 (corrected), phi kills '
                      'sum_(O^q(H) = H_0) e_H in R(kG) if H_0 is non-cyclic'
                      % (name, qq, p))
                if name == 'S3' and (qq, p) == (3, 2):
                    refuted(all(killed[h0] == (not cyc_cl[h0 - 1])
                                for h0 in comps),
                            'S3, q = 3, p = 2: p. 186 as printed, "phi kills '
                            'such an idempotent if and only if H_0 is '
                            'non-cyclic" (H_0 = C2 is killed in '
                            'characteristic 2)')
        # Witt-Berman (Definition 5.6.6, Theorem 5.6.7), k = CC and RR
        el_C = [i for i, H in enumerate(reps) if k_elementary(H, gal_C, False)]
        lit_C = [i for i, H in enumerate(reps) if k_elementary(H, gal_C, True)]
        direct = []
        for i, H in enumerate(reps):
            ok = False
            for qq in primes:
                Q = H.SylowSubgroup(qq)
                C = H.HallSubgroup([r for r in primes if r != qq]) \
                    if len(primes) > 1 else H.TrivialSubgroup()
                if C == gap('fail'):
                    continue
                if bool(H.IsNormal(Q)) and bool(C.IsCyclic()) and bool(
                        H.IsNormal(C)):
                    ok = True
            direct.append(ok)
        check(set(el_C) == set(i for i in range(len(reps)) if direct[i]),
              '%s: Definition 5.6.6 (corrected reading), the CC-elementary '
              'subgroups are the direct products of a q-group and a cyclic '
              'q\'-group (p. 188)' % name)
        check(lattice_contains([v for i in el_C for v in ind[i]], one),
              '%s: Theorem 5.6.7 (Witt-Berman) for k = CC with Definition '
              '5.6.6 read with eps of order |O^q(H)|' % name)
        check(set(lit_C) == set(cyclic),
              '%s: Definition 5.6.6 read literally (eps of order |H|, every '
              'integer t) makes exactly the cyclic subgroups CC-elementary'
              % name)
        if name in ('V4', 'C2^3', 'Q8', 'D8', 'C2^4'):
            refuted(lattice_contains([v for i in lit_C for v in ind[i]], one),
                    '%s: Theorem 5.6.7 for k = CC with Definition 5.6.6 read '
                    'literally (1 induced from cyclic subgroups only)' % name)
        ind_R = {i: [vector(QQ, ilist(r)) for r in R['induced_real'](G, H)]
                 for i, H in enumerate(reps)}
        tG = tbl
        indic = ilist(tG.Indicator(2))
        irrv = list(range(h))
        realbasis = []
        for i in irrv:
            v = [0] * h
            if indic[i] == 1:
                v[i] = 1
            elif indic[i] == -1:
                v[i] = 2
            else:
                v[i] = 1
                conj = int(gap('function(t, i) return Position(Irr(t), '
                               'ComplexConjugate(Irr(t)[i])); end')(tG, i + 1))
                v[conj - 1] += 1
            realbasis.append(vector(QQ, v))
        el_R = [i for i, H in enumerate(reps) if k_elementary(H, gal_R, False)]
        VR = [v for i in el_R for v in ind_R[i]]
        check(lattice_contains(VR, one)
              and all(lattice_contains(realbasis, v) for v in VR),
              '%s: Theorem 5.6.7 (Witt-Berman) for k = RR: R(RG) is spanned '
              'by induction from the %d classes of RR-elementary subgroups '
              '(b a b^-1 = a^(+-1))' % (name, len(el_R)))

    # ---- characteristic p: Brauer characters ---------------------------
    for src, lib, primes in MODULAR:
        for p in primes:
            G0 = gap(src)
            t, bt = R['brauer_table'](G0, lib, p)
            G = t.UnderlyingGroup()
            regs = ilist(R['pregular'](t, p))
            fus = ilist(gap('GetFusionMap')(bt, t))
            ibr = matrix(UCF, [cycl(b.ValuesOfClassFunction())
                               for b in bt.Irr()])
            ell = ibr.nrows()
            reps = list(B['classes'](G))
            triv = vector(UCF, [1] * ell)

            def induced_brauer(H):
                tH = H.CharacterTable()
                bH = gap('function(t, p) return t mod p; end')(tH, p)
                fH = ilist(gap('GetFusionMap')(bH, tH))
                out = []
                for beta in bH.Irr():
                    vals = [0] * int(tH.NrConjugacyClasses())
                    for k, c in enumerate(fH):
                        vals[c - 1] = beta.ValuesOfClassFunction()[k]
                    cf = gap('function(t, v, G) return ValuesOfClassFunction('
                             'InducedClassFunction(ClassFunction(t, v), G)); '
                             'end')(tH, libgap(vals), G)
                    w = vector(UCF, [cyc(cf[f - 1]) for f in fus])
                    out.append(ibr.solve_left(w))
                return out
            name = '%s, p = %d' % (lib or src, p)
            vecs = {}
            for i, H in enumerate(reps):
                if any(bool(R['hyper'](H, qq)[0]) for qq in
                       set(int(r) for r, _ in factor(int(G.Size())))):
                    vecs[i] = induced_brauer(H)
            allv = [v for i in vecs for v in vecs[i]]
            check(all(all(x.is_rational() and QQ(x) in ZZ and QQ(x) >= 0
                          for x in v) for v in allv),
                  '%s: induced Brauer characters are characters (non-negative '
                  'integer combinations of IBr)' % name)
            Z = [vector(ZZ, [ZZ(QQ(x)) for x in v]) for v in allv]
            e = vector(ZZ, [1 if all(x == 1 for x in ibr.row(j)) else 0
                            for j in range(ell)])
            check(e in matrix(ZZ, Z).row_module(),
                  '%s: Theorem 5.6.4 (Brauer) in characteristic p, R(kG) = '
                  'sum of Im(ind) over the hyperelementary subgroups' % name)
            cyc_preg = [i for i, H in enumerate(reps) if bool(H.IsCyclic())
                        and int(H.Size()) % p != 0]
            Vc = [v for i in cyc_preg for v in induced_brauer(reps[i])]
            check(matrix(UCF, Vc).rank() == ell,
                  '%s: Theorem 5.6.1 (Artin) in characteristic p, cyclic '
                  'subgroups of order prime to p suffice over CC' % name)

    # ---- Proposition 5.9.4 (the Brauer lift) and the closing remark ------
    for src, lib, p, qs in (('SymmetricGroup(3)', '', 2, (2, 4)),
                            ('AlternatingGroup(4)', '', 2, (2, 4)),
                            ('AlternatingGroup(4)', '', 3, (3,)),
                            ('SymmetricGroup(4)', '', 3, (3, 9)),
                            ('SL(2,3)', '', 3, (3, 9)),
                            ('SmallGroup(21,1)', '', 7, (7,)),
                            ('SmallGroup(21,1)', '', 3, (3,)),
                            ('AlternatingGroup(5)', 'A5', 2, (2, 4)),
                            ('AlternatingGroup(5)', 'A5', 3, (3, 9)),
                            ('AlternatingGroup(5)', 'A5', 5, (5,)),
                            ('PSL(2,7)', 'L3(2)', 2, (2, 4)),
                            ('PSL(2,7)', 'L3(2)', 7, (7,))):
        G0 = gap(src)
        t, bt = R['brauer_table'](G0, lib, p)
        G = t.UnderlyingGroup()
        name = '%s, p = %d' % (lib or src, p)
        h = int(t.NrConjugacyClasses())
        irr = [cycl(c.ValuesOfClassFunction()) for c in t.Irr()]
        ibr = [cycl(b.ValuesOfClassFunction()) for b in bt.Irr()]
        ell = len(ibr)
        fus = ilist(gap('GetFusionMap')(bt, t))
        D = imat(bt.DecompositionMatrix())
        sizes = ilist(t.SizesConjugacyClasses())
        order = int(G.Size())

        def inner(a, b):
            return sum(sizes[i] * a[i] * b[i].conjugate()
                       for i in range(h)) / order
        for qq in qs:
            pm = ilist(t.PowerMap(qq))
            # psi^q on R(KG) in the basis Irr: chi -> chi(g^q)
            Psi = matrix(QQ, [[QQ(inner([chi[pm[c] - 1] for c in range(h)],
                                        psi)) for psi in irr]
                              for chi in irr])
            check(all(x in ZZ for x in Psi.list()),
                  '%s: psi^%d maps R(KG) to itself' % (name, qq))
            fixK = (Psi - 1).change_ring(ZZ).left_kernel()
            # the induced permutation of the p-regular classes
            pos = {f: k for k, f in enumerate(fus)}
            perm = [pos[pm[f - 1]] for f in fus]
            ibrm = matrix(UCF, ibr)
            Psik = matrix(QQ, [[QQ(x) for x in ibrm.solve_left(
                vector(UCF, [beta[perm[c]] for c in range(ell)]))]
                for beta in ibr])
            fixk = (Psik - 1).change_ring(ZZ).left_kernel()
            image = [vector(ZZ, list(v * D)) for v in fixK.basis()]
            imgmod = matrix(ZZ, image).row_module() if image else None
            check(fixK.rank() == fixk.rank() and imgmod == fixk,
                  '%s: Proposition 5.9.4, d maps R(KG)^(psi^%d) onto '
                  'R(kG)^(psi^%d), injectively (ranks %d)'
                  % (name, qq, qq, fixk.rank()))
            if True:
                Gs = G
                mods = gap('function(G, q) local L; L := IrreducibleModules('
                           'G, GF(q), 0); return L; end')(Gs, qq)
                clreps = [t.ConjugacyClasses()[f - 1].Representative()
                          for f in fus]
                chars = []
                for M in mods[1]:
                    vals = cycl(R['brauer_gens'](Gs, mods[0], M, clreps))
                    coords = ibrm.solve_left(vector(UCF, vals))
                    chars.append(vector(ZZ, [ZZ(QQ(x)) for x in coords]))
                check(matrix(ZZ, chars).row_module() == fixk,
                      '%s: Proposition 5.9.4, R(kG)^(psi^%d) = R(k_0 G) for '
                      'k_0 = GF(%d) (Brauer characters of the irreducible '
                      'GF(%d)G-modules)' % (name, qq, qq, qq))
        # closing remark: g -> t_(g_p')(M) is a generalised character
        ppart = []
        for c in range(h):
            g = t.ConjugacyClasses()[c].Representative()
            o = int(g.Order())
            v = p ** ZZ(o).valuation(p)
            r = o // v
            e = libgap.ChineseRem([v, r], [0, 1])
            gp = g ** e
            classpos = gap('function(t, g) return PositionProperty('
                           'ConjugacyClasses(t), c -> g in c); end')
            ppart.append(int(classpos(t, gp)))
        pos = {f: k for k, f in enumerate(fus)}
        ok = True
        for beta in ibr:
            ext = [beta[pos[ppart[c]]] for c in range(h)]
            for chi in irr:
                x = inner(ext, chi)
                ok = ok and x.is_rational() and QQ(x) in ZZ
        check(ok, '%s: p. 196, g -> t_(g_p\')(M) is a generalised character '
              'for every simple M' % name)


def main():
    section_5_1_to_5_3()
    section_5_4()
    section_5_5_and_5_6_trivial_source()
    section_5_6_characters()
    green = section_cyclic_green_rings()
    section_5_9(green)
    section_forms_and_duality()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
