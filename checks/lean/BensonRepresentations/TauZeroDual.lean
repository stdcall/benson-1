import Mathlib.Analysis.Complex.Basic
import Mathlib.Algebra.Module.LinearMap.Star
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# The last sentence of Theorem 5.11.1

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), Section 5.11, Theorem 5.11.1, p. 199 of the printed book.  The book
ends the theorem with "for any `x = ∑ a_i [M_i] ∈ A(G)` we have
`(x, τ₀(x)) = ∑ |a_i|² ≥ 0` with equality if and only if `x = 0`"; from the
displayed duality `([N'], τ₀[N]) = d(N) δ` and the antilinearity of `τ₀`
the value is `∑ |a_i|² d(M_i)`, which is `∑ |a_i|²` only when every
`d(M_i) = 1` (for instance when `k` is algebraically closed).

Notation.  `V` is a complex vector space (`A(G)`), `B : V →ₗ V →ₗ ℂ` the
bilinear form `( , )`, `τ : V →ₗ⋆ V` the antilinear map `τ₀`, `e i` the
classes `[M_i]` of distinct indecomposable modules and `d i ≥ 1` the numbers
`d(M_i) = dim End(M_i)/J End(M_i)`.  The hypothesis `hdual` is the first
statement of Theorem 5.11.1 for the `M_i`.

* `form_tau`: `(x, τ₀ x) = ∑ |a_i|² d(M_i)` for `x = ∑ a_i e_i`.
* `form_tau_eq_zero_iff`: the value is `0` iff all `a_i = 0`.

Not covered: the duality itself (almost split sequences); the linear
independence of the `[M_i]` (so that `x = 0` iff all `a_i = 0`).  The
printed value `∑ |a_i|²` is refuted for `x = [S]`, `S` the 2-dimensional
simple `GF(2)C₃`-module (`d(S) = 2`), and for a module of `GF(2)V₄` with
`d = 2`, in `checks/sage/chapter-5.py`.
-/

namespace BensonRepresentations.TauZeroDual

open Finset

variable {ι : Type*} [Fintype ι]
variable {V : Type*} [AddCommGroup V] [Module ℂ V]

theorem form_tau [DecidableEq ι] (B : V →ₗ[ℂ] V →ₗ[ℂ] ℂ) (τ : V →ₗ⋆[ℂ] V) (e : ι → V)
    (d : ι → ℕ) (hdual : ∀ i j, B (e i) (τ (e j)) = if i = j then (d j : ℂ)
      else 0) (a : ι → ℂ) :
    B (∑ i, a i • e i) (τ (∑ i, a i • e i)) =
      ((∑ i, Complex.normSq (a i) * d i : ℝ) : ℂ) := by
  simp only [map_sum, map_smulₛₗ, LinearMap.sum_apply, LinearMap.smul_apply,
    smul_eq_mul, hdual]
  push_cast
  refine sum_congr rfl fun i _ => ?_
  simp only [mul_ite, mul_zero, sum_ite_eq', mem_univ, ite_true]
  rw [← Complex.mul_conj]
  simp only [starRingEnd_apply, id]
  ring

theorem form_tau_eq_zero_iff (d : ι → ℕ) (hd : ∀ i, 1 ≤ d i) (a : ι → ℂ) :
    (∑ i, Complex.normSq (a i) * d i : ℝ) = 0 ↔ ∀ i, a i = 0 := by
  have hnn : ∀ i ∈ univ, 0 ≤ Complex.normSq (a i) * d i :=
    fun i _ => mul_nonneg (Complex.normSq_nonneg _) (Nat.cast_nonneg _)
  rw [sum_eq_zero_iff_of_nonneg hnn]
  refine ⟨fun h i => ?_, fun h i _ => by simp [h i]⟩
  have h1 := h i (mem_univ i)
  have hdi : (d i : ℝ) ≠ 0 := by
    have := hd i
    exact Nat.cast_ne_zero.mpr (by omega)
  exact Complex.normSq_eq_zero.mp ((mul_eq_zero.mp h1).resolve_right hdi)

end BensonRepresentations.TauZeroDual

#print axioms BensonRepresentations.TauZeroDual.form_tau
#print axioms BensonRepresentations.TauZeroDual.form_tau_eq_zero_iff
