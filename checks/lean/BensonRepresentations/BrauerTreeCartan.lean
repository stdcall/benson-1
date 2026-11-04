import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# Cartan determinants of Brauer trees: proof of Theorem 6.5.5

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), printed pp. 217–218, proof of Theorem 6.5.5: the Cartan matrix of a
Brauer tree algebra with `e` edges and exceptional multiplicity `m` has
determinant `e m + 1`.

Notation.  Matrices are indexed by a finite type `ι` with `Fintype.card ι = e`
(the edges); `J` is the matrix with all entries one.

* `det_star_centre`: the star whose centre is exceptional,
  `det (I + m J) = e m + 1` (also the Cartan matrix of the Brauer
  correspondent `b`, with `m = (p^n - 1)/e`, giving `det = p^n`).
* `det_star_leaf`: the star whose exceptional vertex is a leaf, the matrix
  with diagonal `(m + 1, 2, …, 2)` and all other entries `1`, i.e.
  `diag(m, 1, …, 1) + J`, has determinant `e m + 1` (over a field, `m ≠ 0`;
  for `m = 0` the matrix has two equal rows when `e ≥ 2`).
* `step_z_two`, `step_z_exceptional`: the two displays of p. 218,
  `(lm + 1)r + ((l - 1)m + 1)(r + 1) - 2((l - 1)m + 1)r = em + 1` and the
  corrected `(lm + 1)r + ((l - 1)m + 1)(rm + 1) - (m + 1)((l - 1)m + 1)r =
  em + 1`, with `e = l + r - 1`; `step_printed` shows that the printed
  factor `(l + 1)m + 1` changes the left side by `-2m(m + 1)r`.

Not covered: the expansion `det C = det X det Y₀ + det X₀ det Y - z det X₀
det Y₀` for matrices overlapping in one entry and the identification of the
four determinants with those of the subtrees (checked on all trees with at
most 7 edges in `checks/sage/chapter-6.py`); the induction itself.
-/

namespace BensonRepresentations.BrauerTreeCartan

open Matrix

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- `det (I + m J) = e m + 1` over any commutative ring. -/
theorem det_star_centre {R : Type*} [CommRing R] (m : R) :
    (1 + Matrix.of (fun _ _ : ι => m)).det = Fintype.card ι * m + 1 := by
  have h : Matrix.of (fun _ _ : ι => m) =
      replicateCol Unit (fun _ : ι => m) * replicateRow Unit (fun _ : ι => (1 : R)) := by
    ext i j
    simp [Matrix.mul_apply]
  rw [h, det_one_add_replicateCol_mul_replicateRow]
  simp [dotProduct, Finset.sum_const, Finset.card_univ]
  ring

/-- The star with an exceptional leaf `i₀`: `det (diag d + J) = e m + 1`
where `d i₀ = m` and `d i = 1` otherwise. -/
theorem det_star_leaf {K : Type*} [Field K] (i₀ : ι) {m : K} (hm : m ≠ 0) :
    (Matrix.diagonal (fun i => if i = i₀ then m else 1) +
        Matrix.of (fun _ _ : ι => (1 : K))).det = Fintype.card ι * m + 1 := by
  set d : ι → K := fun i => if i = i₀ then m else 1 with hd
  have hd0 : ∀ i, d i ≠ 0 := by
    intro i
    by_cases h : i = i₀ <;> simp [hd, h, hm]
  have hdet : (Matrix.diagonal d).det = m := by
    rw [det_diagonal, Finset.prod_eq_single i₀]
    · simp [hd]
    · intro b _ hb
      simp [hd, hb]
    · simp
  have hunit : IsUnit (Matrix.diagonal d).det := by
    rw [hdet]
    exact hm.isUnit
  have hJ : Matrix.of (fun _ _ : ι => (1 : K)) =
      replicateCol Unit (fun _ : ι => (1 : K)) *
        replicateRow Unit (fun _ : ι => (1 : K)) := by
    ext i j
    simp [Matrix.mul_apply]
  have hinv : (Matrix.diagonal d)⁻¹ = Matrix.diagonal (fun i => (d i)⁻¹) := by
    apply Matrix.inv_eq_left_inv
    rw [diagonal_mul_diagonal]
    ext i j
    by_cases h : i = j
    · subst h
      simp [inv_mul_cancel₀ (hd0 i)]
    · simp [h]
  have hsum : ∑ i, (d i)⁻¹ = m⁻¹ + ((Fintype.card ι : K) - 1) := by
    have : ∀ i, (d i)⁻¹ = 1 + (if i = i₀ then m⁻¹ - 1 else 0) := by
      intro i
      by_cases h : i = i₀ <;> simp [hd, h]
    simp only [this, Finset.sum_add_distrib, Finset.sum_ite_eq', Finset.mem_univ,
      ite_true, Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
    ring
  rw [hJ, det_add_replicateCol_mul_replicateRow hunit, hdet, hinv, det_unique]
  simp [Matrix.add_apply, Matrix.mul_apply, diagonal_apply]
  rw [hsum]
  field_simp
  ring

/-- The display for `z = 2` (p. 218). -/
theorem step_z_two {R : Type*} [CommRing R] (l r m : R) :
    (l * m + 1) * r + ((l - 1) * m + 1) * (r + 1) - 2 * ((l - 1) * m + 1) * r =
      (l + r - 1) * m + 1 := by
  ring

/-- The display for `z = m + 1` (p. 218), with the corrected factor
`(l - 1) m + 1 = det X₀`. -/
theorem step_z_exceptional {R : Type*} [CommRing R] (l r m : R) :
    (l * m + 1) * r + ((l - 1) * m + 1) * (r * m + 1) -
        (m + 1) * ((l - 1) * m + 1) * r = (l + r - 1) * m + 1 := by
  ring

/-- With the printed factor `(l + 1) m + 1` the left side is off by
`-2 m (m + 1) r`. -/
theorem step_printed {R : Type*} [CommRing R] (l r m : R) :
    (l * m + 1) * r + ((l - 1) * m + 1) * (r * m + 1) -
        (m + 1) * ((l + 1) * m + 1) * r =
      (l + r - 1) * m + 1 - 2 * m * (m + 1) * r := by
  ring

end BensonRepresentations.BrauerTreeCartan

#print axioms BensonRepresentations.BrauerTreeCartan.det_star_centre
#print axioms BensonRepresentations.BrauerTreeCartan.det_star_leaf
#print axioms BensonRepresentations.BrauerTreeCartan.step_z_two
#print axioms BensonRepresentations.BrauerTreeCartan.step_z_exceptional
#print axioms BensonRepresentations.BrauerTreeCartan.step_printed
