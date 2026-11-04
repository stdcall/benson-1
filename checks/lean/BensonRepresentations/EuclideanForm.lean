import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Logic.Relation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Additive functions and the form of a Euclidean diagram

Book: D. J. Benson, *Representations and Cohomology I*, second edition (1998),
Section 4.5, Lemma 4.5.5 (ii), and Section 4.6, the proof of
Proposition 4.6.3, pp. 119–121 of the printed book.

Notation.  The vertices of the labelled graph `T` form a finite type `ι`; the
Cartan matrix is `c : ι → ι → K` (`c x y = c_xy`, Definition 4.5.3) over a
linearly ordered field `K` (the book: `ℚ` or `ℝ`).  A function `x ↦ n x` is
subadditive if `n x > 0` and `∑ x, n x * c x y ≥ 0` for all `y`, additive if
these sums vanish (Definition 4.5.4).

* `additive_of_subadditive`: Lemma 4.5.5 (ii).  If `T^op` admits an additive
  function `n'`, i.e. `n' y > 0` and `∑ y, c x y * n' y = 0` for all `x`, then
  every subadditive function `n` on `T` is additive (the double sum
  `∑ x y, n x * c x y * n' y` vanishes and is a sum of non-negative terms).

For the form, `S x y = (v_x, v_y) = c_xy f_y` is the symmetrised Cartan matrix
(Definition 4.6.1); we assume only that `S` is symmetric and that `n` is
additive for `S`, `∑ x, n x * S x y = 0` (which follows from the additivity
of `n` for `c` on multiplying by `f_y`), with all `n x ≠ 0`.

* `norm_identity`: the identity of the proof of Proposition 4.6.3,
  `(∑ a_x v_x, ∑ a_x v_x) = -1/2 ∑_{x,y} n_x n_y S_xy (a_x/n_x - a_y/n_y)²`
  (the book sums over `x ≠ y`; the diagonal terms are zero).
* `norm_nonneg`: if moreover `S x y ≤ 0` for `x ≠ y` and `n x > 0`, the form
  is positive semidefinite.
* `ratio_eq_of_norm_zero`: for a null vector, `a_x/n_x = a_y/n_y` whenever
  `S x y < 0` (an edge `x — y`).
* `eq_smul_of_norm_zero`: if every vertex is joined to `x₀` by a chain of
  edges (`T` connected), every null vector is a multiple of `n`: the null
  space is one dimensional (Proposition 4.6.3 (ii), second sentence).

Not covered: that the printed numbers of Definition 4.5.1 (iii) are additive
(checked in `checks/sage/chapter-4a.py` for every Euclidean diagram with at
most 10 vertices, and asserted by the diagram file), the classification of
Lemma 4.5.2, the definiteness on Dynkin diagrams and part (iii) of
Proposition 4.6.3 (checked in Sage on finite families of graphs only).
-/

namespace BensonRepresentations.EuclideanForm

open Finset

variable {ι K : Type*} [Fintype ι] [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Lemma 4.5.5 (ii): an additive function on `T^op` forces every subadditive
function on `T` to be additive. -/
theorem additive_of_subadditive (c : ι → ι → K) (n n' : ι → K)
    (hn' : ∀ y, 0 < n' y) (hop : ∀ x, ∑ y, c x y * n' y = 0)
    (hsub : ∀ y, 0 ≤ ∑ x, n x * c x y) : ∀ y, ∑ x, n x * c x y = 0 := by
  have hzero : ∑ y, (∑ x, n x * c x y) * n' y = 0 := by
    calc ∑ y, (∑ x, n x * c x y) * n' y
        = ∑ y, ∑ x, n x * (c x y * n' y) := by
          refine sum_congr rfl fun y _ => ?_
          rw [sum_mul]
          exact sum_congr rfl fun x _ => by ring
      _ = ∑ x, n x * ∑ y, c x y * n' y := by
          rw [sum_comm]
          exact sum_congr rfl fun x _ => by rw [mul_sum]
      _ = 0 := by simp [hop]
  have hterm := (sum_eq_zero_iff_of_nonneg fun y _ =>
    mul_nonneg (hsub y) (hn' y).le).1 hzero
  intro y
  have := hterm y (mem_univ y)
  rcases mul_eq_zero.1 this with h | h
  · exact h
  · exact absurd h (hn' y).ne'

/-- The quadratic form `(∑ a_x v_x, ∑ a_x v_x)` of the Gram matrix `S`. -/
def form (S : ι → ι → K) (a : ι → K) : K := ∑ x, ∑ y, a x * a y * S x y

/-- The right-hand side of the display in the proof of Proposition 4.6.3. -/
def rhs (S : ι → ι → K) (n a : ι → K) : K :=
  -(1 / 2) * ∑ x, ∑ y, n x * n y * S x y * (a x / n x - a y / n y) ^ 2

theorem norm_identity (S : ι → ι → K) (n a : ι → K)
    (hsymm : ∀ x y, S x y = S y x) (hn : ∀ x, n x ≠ 0)
    (hadd : ∀ y, ∑ x, n x * S x y = 0) : form S a = rhs S n a := by
  -- each term expands into three
  have hexp : ∀ x y, n x * n y * S x y * (a x / n x - a y / n y) ^ 2
      = a x ^ 2 / n x * (S x y * n y) - 2 * (a x * a y * S x y)
        + a y ^ 2 / n y * (n x * S x y) := by
    intro x y
    field_simp [hn x, hn y]
    ring
  have h1 : ∑ x, ∑ y, a x ^ 2 / n x * (S x y * n y) = 0 := by
    refine sum_eq_zero fun x _ => ?_
    rw [← mul_sum]
    have : ∑ y, S x y * n y = 0 := by
      rw [← hadd x]
      exact sum_congr rfl fun y _ => by rw [hsymm x y, mul_comm]
    rw [this, mul_zero]
  have h3 : ∑ x, ∑ y, a y ^ 2 / n y * (n x * S x y) = 0 := by
    rw [sum_comm]
    refine sum_eq_zero fun y _ => ?_
    rw [← mul_sum, hadd y, mul_zero]
  unfold rhs form
  simp_rw [hexp, sum_add_distrib, sum_sub_distrib, h1, h3, ← mul_sum]
  ring

/-- Positive semidefiniteness (Proposition 4.6.3 (ii), first half). -/
theorem norm_nonneg (S : ι → ι → K) (n a : ι → K)
    (hsymm : ∀ x y, S x y = S y x) (hn : ∀ x, 0 < n x)
    (hadd : ∀ y, ∑ x, n x * S x y = 0) (hneg : ∀ x y, x ≠ y → S x y ≤ 0) :
    0 ≤ form S a := by
  rw [norm_identity S n a hsymm (fun x => (hn x).ne') hadd, rhs]
  have : ∑ x, ∑ y, n x * n y * S x y * (a x / n x - a y / n y) ^ 2 ≤ 0 := by
    refine sum_nonpos fun x _ => sum_nonpos fun y _ => ?_
    by_cases hxy : x = y
    · subst hxy; simp
    · have := hneg x y hxy
      have h2 : 0 ≤ (a x / n x - a y / n y) ^ 2 := sq_nonneg _
      have h3 : n x * n y * S x y ≤ 0 :=
        mul_nonpos_of_nonneg_of_nonpos (mul_pos (hn x) (hn y)).le this
      exact mul_nonpos_of_nonpos_of_nonneg h3 h2
  linarith

/-- For a null vector the ratios `a_x / n_x` agree along every edge. -/
theorem ratio_eq_of_norm_zero (S : ι → ι → K) (n a : ι → K)
    (hsymm : ∀ x y, S x y = S y x) (hn : ∀ x, 0 < n x)
    (hadd : ∀ y, ∑ x, n x * S x y = 0) (hneg : ∀ x y, x ≠ y → S x y ≤ 0)
    (h0 : form S a = 0) {x y : ι} (hxy : S x y < 0) :
    a x / n x = a y / n y := by
  rw [norm_identity S n a hsymm (fun x => (hn x).ne') hadd, rhs] at h0
  have hsum : ∑ x, ∑ y, n x * n y * S x y * (a x / n x - a y / n y) ^ 2
      = 0 := by linarith
  have hterm : ∀ x y, n x * n y * S x y * (a x / n x - a y / n y) ^ 2 ≤ 0 := by
    intro x y
    by_cases hxy : x = y
    · subst hxy; simp
    · exact mul_nonpos_of_nonpos_of_nonneg
        (mul_nonpos_of_nonneg_of_nonpos (mul_pos (hn x) (hn y)).le
          (hneg x y hxy)) (sq_nonneg _)
  have hrow := (sum_eq_zero_iff_of_nonpos fun x _ =>
    sum_nonpos fun y _ => hterm x y).1 hsum x (mem_univ x)
  have hxy0 := (sum_eq_zero_iff_of_nonpos fun y _ => hterm x y).1 hrow y
    (mem_univ y)
  have hc : n x * n y * S x y ≠ 0 :=
    (mul_neg_of_pos_of_neg (mul_pos (hn x) (hn y)) hxy).ne
  have := pow_eq_zero_iff (n := 2) (by norm_num) |>.1
    ((mul_eq_zero.1 hxy0).resolve_left hc)
  linarith

/-- In a connected graph every null vector is a multiple of `n`. -/
theorem eq_smul_of_norm_zero (S : ι → ι → K) (n a : ι → K)
    (hsymm : ∀ x y, S x y = S y x) (hn : ∀ x, 0 < n x)
    (hadd : ∀ y, ∑ x, n x * S x y = 0) (hneg : ∀ x y, x ≠ y → S x y ≤ 0)
    (x₀ : ι) (hconn : ∀ y, Relation.ReflTransGen (fun x y => S x y < 0) x₀ y)
    (h0 : form S a = 0) : ∀ y, a y = a x₀ / n x₀ * n y := by
  intro y
  have hr : a y / n y = a x₀ / n x₀ := by
    induction hconn y with
    | refl => rfl
    | tail _ hbc ih =>
      rw [← ih]
      exact (ratio_eq_of_norm_zero S n a hsymm hn hadd hneg h0 hbc).symm
  rw [← hr]
  field_simp [(hn y).ne']

end BensonRepresentations.EuclideanForm

#print axioms BensonRepresentations.EuclideanForm.additive_of_subadditive
#print axioms BensonRepresentations.EuclideanForm.norm_identity
#print axioms BensonRepresentations.EuclideanForm.norm_nonneg
#print axioms BensonRepresentations.EuclideanForm.ratio_eq_of_norm_zero
#print axioms BensonRepresentations.EuclideanForm.eq_smul_of_norm_zero
