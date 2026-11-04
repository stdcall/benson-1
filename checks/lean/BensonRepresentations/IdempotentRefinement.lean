import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.RingTheory.Nilpotent.Basic
import Mathlib.RingTheory.TwoSidedIdeal.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Idempotent refinement: Proposition 1.7.2, Theorem 1.7.3, Corollary 1.7.4

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), Section 1.7, pp. 13–14 of the printed book, with the author's
correction of the last sentence of the proof of Theorem 1.7.3 ("Comments and
corrections", 8 September 2010).

Notation.  `A` is the ring `Λ`; a two-sided ideal `N` of `Λ` is a
`TwoSidedIdeal A`; "`e` is an idempotent of `Λ/N` lifted by `a`" is the
hypothesis `a * a - a ∈ N`, and "`f` lifts `e`" is `f - a ∈ N`, so no quotient
ring is constructed.  The book's `N` is nilpotent; we only use that every
element of `N` is nilpotent (`∀ x ∈ N, IsNilpotent x`), which follows.

* `refinement_identity`: the displayed identity of the proof of Theorem 1.7.3,
  `e² - e = (3a² - 2a³)(3a² - 2a³ - 1) = -(3 - 2a)(1 + 2a)(a² - a)²` for
  `e = 3a² - 2a³`, in an arbitrary ring, and `e - a = (a² - a)(1 - 2a)`
  (`e` has the same image as `a`).
* `exists_idempotent_lift`: the first assertion of Theorem 1.7.3.  The book
  lifts from `Λ/N^(i-1)` to `Λ/N^i`; here the same step `a ↦ 3a² - 2a³` is
  iterated `k` times, and the iterate `P k` (a polynomial in `a`, so all
  factors commute) satisfies `P k² - P k ∈ (a² - a)^(2^k) ℤ[a]`
  (`iter_sq_sub`), which is zero once `2^k` exceeds the nilpotency index of
  `a² - a`.
* `nu_mul_f₁`, `mu_sub_nu`, `one_sub_inv_mul_nu`, `nu_isUnit`,
  `nu_inverse`: the second assertion of Theorem 1.7.3 in the author's
  corrected form: for idempotents `f₁, f₂` and a unit `μ` with
  `f₂μ - μf₁ ∈ N` (`μ̄ e₁ = e₂ μ̄`), `ν = f₂μf₁ + (1 - f₂)μ(1 - f₁)` has
  `νf₁ = f₂ν`, `1 - μ⁻¹ν = μ⁻¹(f₂μ + μf₁ - 2f₂μf₁) = μ⁻¹(f₂μ - μf₁)(1 - 2f₁)`,
  and `(1 + (1 - μ⁻¹ν) + (1 - μ⁻¹ν)² + ⋯) μ⁻¹` (a finite sum, since
  `1 - μ⁻¹ν ∈ N` is nilpotent) is a two-sided inverse of `ν`.  The printed
  reading `1 - ν = f₂μ + μf₁ - 2f₂μf₁` is false in general (it holds iff
  `μ = 1`); `mu_sub_nu` is the true identity.  `nu_isUnit_of_one_sub` only
  needs `1 - μ⁻¹ν` to be invertible, which is how "proved exactly as in
  1.7.3" applies in Theorem 1.9.4 (i) with `N = πΛ ⊆ J(Λ)`.
* `conjugate_of_components`: the converse half of the proof of
  Proposition 1.7.2: from `μ₁ ∈ eΛe'`, `μ₂ ∈ e'Λe`, `μ₃ ∈ (1-e)Λ(1-e')`,
  `μ₄ ∈ (1-e')Λ(1-e)` with `μ₁μ₂ = e`, `μ₂μ₁ = e'`, `μ₃μ₄ = 1 - e`,
  `μ₄μ₃ = 1 - e'`, the elements `μ = μ₁ + μ₃`, `μ' = μ₂ + μ₄` satisfy
  `μμ' = μ'μ = 1` and `eμ = μ₁ = μe'`.  The identification of homomorphisms
  `Λe → Λe'` with `eΛe'` (Lemma 1.3.3) is not formalized.
* `orthogonal_of_chain`, `sum_of_chain`: the proof of Corollary 1.7.4: if
  `g 0 = 1`, `g n = 0` and each `g (i+1)` is an idempotent of
  `g i Λ g i`, then `fᵢ = g i - g (i+1)` (`i < n`) are pairwise orthogonal
  idempotents with sum `1`.  The lifting of `e_i + ⋯ + e_n` inside
  `f'_(i-1) Λ f'_(i-1)` is the first assertion applied to that corner ring;
  primitivity of the `fᵢ` is not formalized.

Not covered: the quotient rings `Λ/N^i`, the lifting of conjugacy classes
of idempotents as a statement about `Λ/N`, and the `N`-adic limit of
Theorem 1.9.4 (i).
-/

namespace BensonRepresentations.IdempotentRefinement

open Polynomial

/-- The identity displayed in the proof of Theorem 1.7.3. -/
theorem refinement_identity {A : Type*} [Ring A] (a : A) :
    let e := 3 * a ^ 2 - 2 * a ^ 3
    e ^ 2 - e = e * (e - 1) ∧
      e * (e - 1) = -((3 - 2 * a) * (1 + 2 * a) * (a ^ 2 - a) ^ 2) := by
  intro e
  refine ⟨?_, ?_⟩ <;> simp only [e] <;> noncomm_ring

/-- `e = 3a² - 2a³` has the same image as `a` modulo any ideal containing
`a² - a`. -/
theorem refinement_sub {A : Type*} [Ring A] (a : A) :
    (3 * a ^ 2 - 2 * a ^ 3) - a = (a ^ 2 - a) * (1 - 2 * a) := by
  noncomm_ring

/-- The iterates `a, 3a² - 2a³, …` as polynomials in `X = a`. -/
noncomputable def P : ℕ → ℤ[X]
  | 0 => X
  | k + 1 => 3 * P k ^ 2 - 2 * P k ^ 3

/-- `P k² - P k` is divisible by `(X² - X)^(2^k)`. -/
theorem iter_sq_sub (k : ℕ) :
    ∃ U : ℤ[X], P k ^ 2 - P k = (X ^ 2 - X) ^ (2 ^ k) * U := by
  induction k with
  | zero => exact ⟨1, by simp [P]⟩
  | succ k ih =>
    obtain ⟨U, hU⟩ := ih
    refine ⟨-((3 - 2 * P k) * (1 + 2 * P k)) * U ^ 2, ?_⟩
    have h : P (k + 1) ^ 2 - P (k + 1)
        = -((3 - 2 * P k) * (1 + 2 * P k)) * (P k ^ 2 - P k) ^ 2 := by
      simp only [P]; ring
    rw [h, hU, pow_succ 2 k, pow_mul]
    ring

/-- `P k - X` is divisible by `X² - X`. -/
theorem iter_sub (k : ℕ) : ∃ C : ℤ[X], P k - X = (X ^ 2 - X) * C := by
  induction k with
  | zero => exact ⟨0, by simp [P]⟩
  | succ k ih =>
    obtain ⟨C, hC⟩ := ih
    obtain ⟨U, hU⟩ := iter_sq_sub k
    obtain ⟨m, hm⟩ : ∃ m, 2 ^ k = m + 1 := ⟨2 ^ k - 1, by
      have := Nat.one_le_two_pow (n := k); omega⟩
    refine ⟨(X ^ 2 - X) ^ m * U * (1 - 2 * P k) + C, ?_⟩
    have h : P (k + 1) - X = (P k ^ 2 - P k) * (1 - 2 * P k) + (P k - X) := by
      simp only [P]; ring
    rw [h, hU, hC, hm, pow_succ]
    ring

/-- Theorem 1.7.3, first assertion: modulo a two-sided ideal all of whose
elements are nilpotent (e.g. a nilpotent ideal), every idempotent lifts.  The
lift is a polynomial in the given representative `a`. -/
theorem exists_idempotent_lift {A : Type*} [Ring A] (N : TwoSidedIdeal A)
    (hN : ∀ x ∈ N, IsNilpotent x) (a : A) (ha : a * a - a ∈ N) :
    ∃ f : A, f * f = f ∧ f - a ∈ N := by
  obtain ⟨m, hm⟩ := hN _ ha
  obtain ⟨U, hU⟩ := iter_sq_sub m
  obtain ⟨C, hC⟩ := iter_sub m
  refine ⟨aeval a (P m), ?_, ?_⟩
  · have h := congrArg (aeval a) hU
    simp only [map_sub, map_pow, map_mul, aeval_X] at h
    have hz : (a ^ 2 - a) ^ (2 ^ m) = 0 := by
      have hle : m ≤ 2 ^ m := (Nat.lt_two_pow_self).le
      rw [sq, ← Nat.add_sub_cancel' hle, pow_add, hm, zero_mul]
    rw [hz, zero_mul, sub_eq_zero, sq] at h
    exact h
  · have h := congrArg (aeval a) hC
    simp only [map_sub, map_pow, map_mul, aeval_X] at h
    rw [h, sq]
    exact N.mul_mem_right _ _ ha

section Conjugacy

variable {A : Type*} [Ring A]

/-- The element `ν = f₂μf₁ + (1 - f₂)μ(1 - f₁)` of the proof. -/
def nu (f₁ f₂ μ : A) : A := f₂ * μ * f₁ + (1 - f₂) * μ * (1 - f₁)

theorem nu_mul_f₁ {f₁ f₂ : A} (h₁ : f₁ * f₁ = f₁) (h₂ : f₂ * f₂ = f₂) (μ : A) :
    nu f₁ f₂ μ * f₁ = f₂ * nu f₁ f₂ μ := by
  simp only [nu]
  calc (f₂ * μ * f₁ + (1 - f₂) * μ * (1 - f₁)) * f₁
      = f₂ * μ * (f₁ * f₁) + (1 - f₂) * μ * (f₁ - f₁ * f₁) := by noncomm_ring
    _ = (f₂ * f₂) * μ * f₁ + (f₂ - f₂ * f₂) * μ * (1 - f₁) := by
        rw [h₁, h₂, sub_self, sub_self]; noncomm_ring
    _ = f₂ * (f₂ * μ * f₁ + (1 - f₂) * μ * (1 - f₁)) := by noncomm_ring

/-- The corrected identity `μ - ν = f₂μ + μf₁ - 2f₂μf₁ = (f₂μ - μf₁)(1 - 2f₁)`
(the printed text had `1 - ν` on the left). -/
theorem mu_sub_nu {f₁ : A} (h₁ : f₁ * f₁ = f₁) (f₂ μ : A) :
    μ - nu f₁ f₂ μ = f₂ * μ + μ * f₁ - 2 * f₂ * μ * f₁ ∧
      f₂ * μ + μ * f₁ - 2 * f₂ * μ * f₁ = (f₂ * μ - μ * f₁) * (1 - 2 * f₁) := by
  refine ⟨by simp only [nu]; noncomm_ring, ?_⟩
  calc f₂ * μ + μ * f₁ - 2 * f₂ * μ * f₁
      = f₂ * μ - μ * f₁ - 2 * f₂ * μ * f₁ + 2 * (μ * (f₁ * f₁)) := by
        rw [h₁]; noncomm_ring
    _ = (f₂ * μ - μ * f₁) * (1 - 2 * f₁) := by noncomm_ring

/-- `1 - μ⁻¹ν = μ⁻¹(f₂μ - μf₁)(1 - 2f₁)`, as in the author's correction. -/
theorem one_sub_inv_mul_nu {f₁ : A} (h₁ : f₁ * f₁ = f₁) (f₂ : A) (μ : Aˣ) :
    1 - (↑μ⁻¹ : A) * nu f₁ f₂ μ
      = (↑μ⁻¹ : A) * ((f₂ * μ - μ * f₁) * (1 - 2 * f₁)) := by
  rw [← (mu_sub_nu h₁ f₂ (μ : A)).2, ← (mu_sub_nu h₁ f₂ (μ : A)).1, mul_sub,
    Units.inv_mul]

/-- The printed reading `1 - ν = f₂μ + μf₁ - 2f₂μf₁` holds only for `μ = 1`. -/
theorem printed_reading_iff {f₁ : A} (h₁ : f₁ * f₁ = f₁) (f₂ μ : A) :
    1 - nu f₁ f₂ μ = f₂ * μ + μ * f₁ - 2 * f₂ * μ * f₁ ↔ μ = 1 := by
  rw [← (mu_sub_nu h₁ f₂ μ).1]
  constructor
  · intro h; exact (sub_left_inj.mp h).symm
  · intro h; rw [h]

/-- If `1 - μ⁻¹ν` is invertible (e.g. it lies in `J(Λ)`), `ν` is a unit. -/
theorem nu_isUnit_of_one_sub {f₁ f₂ : A} (μ : Aˣ)
    (h : IsUnit (1 - (1 - (↑μ⁻¹ : A) * nu f₁ f₂ μ))) : IsUnit (nu f₁ f₂ μ) := by
  rw [sub_sub_cancel] at h
  have : nu f₁ f₂ μ = (μ : A) * ((↑μ⁻¹ : A) * nu f₁ f₂ μ) := by
    rw [← mul_assoc, Units.mul_inv, one_mul]
  rw [this]
  exact μ.isUnit.mul h

/-- Theorem 1.7.3, second assertion: if `f₂μ - μf₁` lies in a two-sided nil
ideal, `ν` is a unit and `ν f₁ ν⁻¹ = f₂`. -/
theorem nu_isUnit {f₁ f₂ : A} (h₁ : f₁ * f₁ = f₁) (h₂ : f₂ * f₂ = f₂)
    (N : TwoSidedIdeal A) (hN : ∀ x ∈ N, IsNilpotent x) (μ : Aˣ)
    (hμ : f₂ * μ - μ * f₁ ∈ N) :
    ∃ u : Aˣ, (u : A) = nu f₁ f₂ μ ∧ (u : A) * f₁ * (↑u⁻¹ : A) = f₂ := by
  have hmem : 1 - (↑μ⁻¹ : A) * nu f₁ f₂ μ ∈ N := by
    rw [one_sub_inv_mul_nu h₁ f₂ μ]
    exact N.mul_mem_left _ _ (N.mul_mem_right _ _ hμ)
  obtain ⟨u, hu⟩ := nu_isUnit_of_one_sub μ (hN _ hmem).isUnit_one_sub
  refine ⟨u, hu, ?_⟩
  rw [hu, nu_mul_f₁ h₁ h₂, ← hu, mul_assoc, Units.mul_inv, mul_one]

/-- The explicit inverse of the author's correction: if `n = 1 - μ⁻¹ν`
satisfies `n^r = 0`, then `(1 + n + ⋯ + n^(r-1)) μ⁻¹` is a two-sided inverse
of `ν`. -/
theorem nu_inverse {f₁ f₂ : A} (μ : Aˣ) (r : ℕ)
    (hr : (1 - (↑μ⁻¹ : A) * nu f₁ f₂ μ) ^ r = 0) :
    let n := 1 - (↑μ⁻¹ : A) * nu f₁ f₂ μ
    let s := (∑ j ∈ Finset.range r, n ^ j) * (↑μ⁻¹ : A)
    s * nu f₁ f₂ μ = 1 ∧ nu f₁ f₂ μ * s = 1 := by
  intro n s
  have hν : nu f₁ f₂ μ = (μ : A) * (1 - n) := by
    simp only [n]; rw [sub_sub_cancel, ← mul_assoc, Units.mul_inv, one_mul]
  have geom : ∀ t : ℕ, (∑ j ∈ Finset.range t, n ^ j) * (1 - n) = 1 - n ^ t ∧
      (1 - n) * (∑ j ∈ Finset.range t, n ^ j) = 1 - n ^ t := by
    intro t
    induction t with
    | zero => simp
    | succ t ih =>
      constructor
      · rw [Finset.sum_range_succ, add_mul, ih.1, pow_succ]; noncomm_ring
      · rw [Finset.sum_range_succ, mul_add, ih.2, pow_succ']; noncomm_ring
  have hr' : n ^ r = 0 := hr
  constructor
  · simp only [s]
    rw [hν, mul_assoc, ← mul_assoc (↑μ⁻¹ : A), Units.inv_mul, one_mul, (geom r).1,
      hr', sub_zero]
  · simp only [s]
    rw [hν, mul_assoc, ← mul_assoc (1 - n), (geom r).2, hr', sub_zero, one_mul,
      Units.mul_inv]

end Conjugacy

section Components

variable {A : Type*} [Ring A]

/-- Proposition 1.7.2, converse direction of the proof. -/
theorem conjugate_of_components {e e' μ₁ μ₂ μ₃ μ₄ : A}
    (he : e * e = e) (he' : e' * e' = e')
    (h₁ : μ₁ = e * μ₁ * e') (h₂ : μ₂ = e' * μ₂ * e)
    (h₃ : μ₃ = (1 - e) * μ₃ * (1 - e')) (h₄ : μ₄ = (1 - e') * μ₄ * (1 - e))
    (h₁₂ : μ₁ * μ₂ = e) (h₂₁ : μ₂ * μ₁ = e')
    (h₃₄ : μ₃ * μ₄ = 1 - e) (h₄₃ : μ₄ * μ₃ = 1 - e') :
    (μ₁ + μ₃) * (μ₂ + μ₄) = 1 ∧ (μ₂ + μ₄) * (μ₁ + μ₃) = 1 ∧
      e * (μ₁ + μ₃) = μ₁ ∧ (μ₁ + μ₃) * e' = μ₁ := by
  have e'c : e' * (1 - e') = 0 := by rw [mul_sub, mul_one, he', sub_self]
  have c'e' : (1 - e') * e' = 0 := by rw [sub_mul, one_mul, he', sub_self]
  have ec : e * (1 - e) = 0 := by rw [mul_sub, mul_one, he, sub_self]
  have ce : (1 - e) * e = 0 := by rw [sub_mul, one_mul, he, sub_self]
  have z14 : μ₁ * μ₄ = 0 := by
    rw [h₁, h₄]
    calc e * μ₁ * e' * ((1 - e') * μ₄ * (1 - e))
        = e * μ₁ * (e' * (1 - e')) * μ₄ * (1 - e) := by noncomm_ring
      _ = 0 := by rw [e'c]; noncomm_ring
  have z32 : μ₃ * μ₂ = 0 := by
    rw [h₃, h₂]
    calc (1 - e) * μ₃ * (1 - e') * (e' * μ₂ * e)
        = (1 - e) * μ₃ * ((1 - e') * e') * μ₂ * e := by noncomm_ring
      _ = 0 := by rw [c'e']; noncomm_ring
  have z23 : μ₂ * μ₃ = 0 := by
    rw [h₂, h₃]
    calc e' * μ₂ * e * ((1 - e) * μ₃ * (1 - e'))
        = e' * μ₂ * (e * (1 - e)) * μ₃ * (1 - e') := by noncomm_ring
      _ = 0 := by rw [ec]; noncomm_ring
  have z41 : μ₄ * μ₁ = 0 := by
    rw [h₄, h₁]
    calc (1 - e') * μ₄ * (1 - e) * (e * μ₁ * e')
        = (1 - e') * μ₄ * ((1 - e) * e) * μ₁ * e' := by noncomm_ring
      _ = 0 := by rw [ce]; noncomm_ring
  have eμ₃ : e * μ₃ = 0 := by
    rw [h₃]
    calc e * ((1 - e) * μ₃ * (1 - e')) = (e * (1 - e)) * μ₃ * (1 - e') := by
          noncomm_ring
      _ = 0 := by rw [ec]; noncomm_ring
  have μ₃e' : μ₃ * e' = 0 := by
    rw [h₃]
    calc (1 - e) * μ₃ * (1 - e') * e' = (1 - e) * μ₃ * ((1 - e') * e') := by
          noncomm_ring
      _ = 0 := by rw [c'e']; noncomm_ring
  have eμ₁ : e * μ₁ = μ₁ := by
    conv_rhs => rw [h₁]
    conv_lhs => rw [h₁]
    rw [← mul_assoc, ← mul_assoc, he]
  have μ₁e' : μ₁ * e' = μ₁ := by
    conv_rhs => rw [h₁]
    conv_lhs => rw [h₁]
    rw [mul_assoc, he']
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [add_mul, mul_add, mul_add, h₁₂, z14, z32, h₃₄]; noncomm_ring
  · rw [add_mul, mul_add, mul_add, h₂₁, z23, z41, h₄₃]; noncomm_ring
  · rw [mul_add, eμ₁, eμ₃, add_zero]
  · rw [add_mul, μ₁e', μ₃e', add_zero]

end Components

section Chain

variable {A : Type*} [Ring A]

variable {g : ℕ → A} (hid : ∀ i, g i * g i = g i)
  (hg : ∀ i, g i * g (i + 1) = g (i + 1) ∧ g (i + 1) * g i = g (i + 1))
include hid hg

/-- In a chain of idempotents with `g (i+1) ∈ g i Λ g i`, every later term
lies in every earlier corner. -/
theorem chain_le {i j : ℕ} (hij : i ≤ j) : g i * g j = g j ∧ g j * g i = g j := by
  induction j, hij using Nat.le_induction with
  | base => exact ⟨hid i, hid i⟩
  | succ j _ ih =>
    constructor
    · rw [← (hg j).1, ← mul_assoc, ih.1]
    · rw [← (hg j).2, mul_assoc, ih.2]

/-- `fᵢ = g i - g (i+1)` is idempotent. -/
theorem idempotent_of_chain (i : ℕ) :
    (g i - g (i + 1)) * (g i - g (i + 1)) = g i - g (i + 1) := by
  have h1 := (hg i).1
  have h2 := (hg i).2
  have h3 := hid i
  have h4 := hid (i + 1)
  calc (g i - g (i + 1)) * (g i - g (i + 1))
      = g i * g i - g i * g (i + 1) - g (i + 1) * g i + g (i + 1) * g (i + 1) := by
        noncomm_ring
    _ = g i - g (i + 1) := by rw [h1, h2, h3, h4]; abel

/-- The proof of Corollary 1.7.4: `fᵢ fⱼ = fⱼ fᵢ = 0` for `i < j`. -/
theorem orthogonal_of_chain {i j : ℕ} (hij : i < j) :
    (g i - g (i + 1)) * (g j - g (j + 1)) = 0 ∧
      (g j - g (j + 1)) * (g i - g (i + 1)) = 0 := by
  have a := chain_le hid hg (Nat.succ_le_of_lt hij)
  have b := chain_le hid hg (Nat.succ_le_of_lt hij |>.trans (Nat.le_succ j))
  have hl : g (i + 1) * (g j - g (j + 1)) = g j - g (j + 1) := by
    rw [mul_sub, a.1, b.1]
  have hr : (g j - g (j + 1)) * g (i + 1) = g j - g (j + 1) := by
    rw [sub_mul, a.2, b.2]
  have zl : (g i - g (i + 1)) * g (i + 1) = 0 := by
    rw [sub_mul, (hg i).1, hid, sub_self]
  have zr : g (i + 1) * (g i - g (i + 1)) = 0 := by
    rw [mul_sub, (hg i).2, hid, sub_self]
  constructor
  · rw [← hl, ← mul_assoc, zl, zero_mul]
  · rw [← hr, mul_assoc, zr, mul_zero]

omit hid hg in
/-- The sum telescopes: with `g 0 = 1` and `g n = 0`, `∑_(i<n) fᵢ = 1`. -/
theorem sum_of_chain (g : ℕ → A) (n : ℕ) (h0 : g 0 = 1) (hn : g n = 0) :
    ∑ i ∈ Finset.range n, (g i - g (i + 1)) = 1 := by
  rw [Finset.sum_range_sub', h0, hn, sub_zero]

end Chain

end BensonRepresentations.IdempotentRefinement

#print axioms BensonRepresentations.IdempotentRefinement.refinement_identity
#print axioms BensonRepresentations.IdempotentRefinement.refinement_sub
#print axioms BensonRepresentations.IdempotentRefinement.iter_sq_sub
#print axioms BensonRepresentations.IdempotentRefinement.iter_sub
#print axioms BensonRepresentations.IdempotentRefinement.exists_idempotent_lift
#print axioms BensonRepresentations.IdempotentRefinement.nu_mul_f₁
#print axioms BensonRepresentations.IdempotentRefinement.mu_sub_nu
#print axioms BensonRepresentations.IdempotentRefinement.one_sub_inv_mul_nu
#print axioms BensonRepresentations.IdempotentRefinement.printed_reading_iff
#print axioms BensonRepresentations.IdempotentRefinement.nu_isUnit_of_one_sub
#print axioms BensonRepresentations.IdempotentRefinement.nu_isUnit
#print axioms BensonRepresentations.IdempotentRefinement.nu_inverse
#print axioms BensonRepresentations.IdempotentRefinement.conjugate_of_components
#print axioms BensonRepresentations.IdempotentRefinement.chain_le
#print axioms BensonRepresentations.IdempotentRefinement.idempotent_of_chain
#print axioms BensonRepresentations.IdempotentRefinement.orthogonal_of_chain
#print axioms BensonRepresentations.IdempotentRefinement.sum_of_chain
