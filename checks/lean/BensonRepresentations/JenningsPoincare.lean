import Mathlib.Algebra.Polynomial.Reverse
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.BigOperators.Intervals

/-!
# The Poincaré series of the radical layers of `kP`

Section 3.14, Theorem 3.14.6 and Corollary 3.14.7, p. 95: the Poincaré series
of the radical layers of `kP` is
`∑ t^i dim(J^i kP / J^(i+1) kP) = ∏_r (1 + t^r + ⋯ + t^((p-1) r))^(n_r)`,
where `|Γ_r(P) / Γ_(r+1)(P)| = p^(n_r)`; hence the radical length is
`1 + ∑_r (p - 1) r n_r`, and the series is symmetric (the step of the proof of
Corollary 3.14.7 before self-duality is used).

Notation: the indices `r` range over a finite set `s` with values `r i`, the
exponents are `n i`; `layer p r = 1 + X^r + ⋯ + X^((p-1) r) ∈ ℕ[X]` and
`poincare = ∏_(i ∈ s) layer p (r i) ^ n i`, `L = ∑_(i ∈ s) n i ((p - 1) r i)`.

* `reflect_layer`: `X^((p-1) r) layer(1/X) = layer`.
* `reflect_poincare`: `X^L poincare(1/X) = poincare`.
* `coeff_symm`: the coefficients of `t^i` and `t^(L-i)` agree (`i ≤ L`).
* `natDegree_poincare`: for `p ≥ 1` the degree is `L`, so the radical length
  (the number of non-zero layers, top layer in degree `L`) is `1 + L`.
* `eval_one_poincare`: the value at `t = 1` (the dimension of `kP`) is
  `p^(∑ n i)`, i.e. `|P| = p^n` with `n = ∑ n_r`.

Not covered: the product formula itself (Jennings' theorem, the PBW basis and
`F_r = Γ_r`; checked in `checks/sage/chapter-3b.py` for all groups of order
`p^k ≤ 32`, 81, 125, 49 and 13 of the 267 groups of order 64), and the
self-duality argument `Soc^i kP = J^(l-i) kP` (checked there as well).
-/

namespace BensonRepresentations.JenningsPoincare

open Polynomial Finset

/-- `1 + X^r + ⋯ + X^((p-1) r)`. -/
noncomputable def layer (p r : ℕ) : ℕ[X] := ∑ j ∈ range p, X ^ (j * r)

lemma natDegree_layer_le (p r : ℕ) : (layer p r).natDegree ≤ (p - 1) * r := by
  unfold layer
  refine natDegree_sum_le_of_forall_le _ _ (fun j hj => ?_)
  rw [natDegree_X_pow]
  have : j ≤ p - 1 := by have := mem_range.mp hj; omega
  exact Nat.mul_le_mul_right r this

lemma reflect_sum {ι : Type*} (t : Finset ι) (f : ι → ℕ[X]) (N : ℕ) :
    reflect N (∑ i ∈ t, f i) = ∑ i ∈ t, reflect N (f i) := by
  classical
  induction t using Finset.induction_on with
  | empty => simp
  | insert a t ha ih => rw [sum_insert ha, sum_insert ha, reflect_add, ih]

theorem reflect_layer (p r : ℕ) : reflect ((p - 1) * r) (layer p r) = layer p r := by
  unfold layer
  rw [reflect_sum]
  have h : ∀ j ∈ range p, reflect ((p - 1) * r) ((X : ℕ[X]) ^ (j * r)) =
      X ^ ((p - 1 - j) * r) := by
    intro j hj
    have hj' : j ≤ p - 1 := by have := mem_range.mp hj; omega
    rw [reflect_monomial, revAt_le (Nat.mul_le_mul_right r hj'),
      ← Nat.sub_mul]
  rw [sum_congr rfl h]
  exact sum_range_reflect (fun j => (X : ℕ[X]) ^ (j * r)) p

lemma reflect_pow (f : ℕ[X]) {N : ℕ} (hf : f.natDegree ≤ N) (n : ℕ) :
    reflect (n * N) (f ^ n) = reflect N f ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, pow_succ, show (n + 1) * N = n * N + N by ring,
      reflect_mul _ _ ((natDegree_pow_le).trans (Nat.mul_le_mul_left n hf)) hf, ih]

/-- The product over the Jennings layers. -/
noncomputable def poincare {ι : Type*} (s : Finset ι) (p : ℕ) (r n : ι → ℕ) : ℕ[X] :=
  ∏ i ∈ s, layer p (r i) ^ n i

/-- `L = ∑ n_r (p - 1) r`. -/
def L {ι : Type*} (s : Finset ι) (p : ℕ) (r n : ι → ℕ) : ℕ :=
  ∑ i ∈ s, n i * ((p - 1) * r i)

lemma natDegree_layer_pow_le (p r n : ℕ) :
    (layer p r ^ n).natDegree ≤ n * ((p - 1) * r) :=
  natDegree_pow_le.trans (Nat.mul_le_mul_left n (natDegree_layer_le p r))

theorem reflect_poincare {ι : Type*} (s : Finset ι) (p : ℕ) (r n : ι → ℕ) :
    reflect (L s p r n) (poincare s p r n) = poincare s p r n := by
  classical
  unfold poincare L
  induction s using Finset.induction_on with
  | empty => simp
  | insert a t ha ih =>
    rw [prod_insert ha, sum_insert ha]
    have h1 := natDegree_layer_pow_le p (r a) (n a)
    have h2 : (∏ i ∈ t, layer p (r i) ^ n i).natDegree ≤
        ∑ i ∈ t, n i * ((p - 1) * r i) := by
      refine (natDegree_prod_le _ _).trans (sum_le_sum fun i _ => ?_)
      exact natDegree_layer_pow_le p (r i) (n i)
    rw [reflect_mul _ _ h1 h2, ih, reflect_pow _ (natDegree_layer_le p (r a)),
      reflect_layer]

theorem coeff_symm {ι : Type*} (s : Finset ι) (p : ℕ) (r n : ι → ℕ) {i : ℕ}
    (hi : i ≤ L s p r n) :
    (poincare s p r n).coeff i = (poincare s p r n).coeff (L s p r n - i) := by
  conv_lhs => rw [← reflect_poincare s p r n]
  rw [coeff_reflect, revAt_le hi]

lemma degree_lower_lt (q r : ℕ) (hr : 1 ≤ r) :
    (∑ j ∈ range q, (X : ℕ[X]) ^ (j * r)).degree < ((X : ℕ[X]) ^ (q * r)).degree := by
  rw [degree_X_pow]
  refine (degree_sum_le _ _).trans_lt ?_
  refine (Finset.sup_lt_iff (WithBot.bot_lt_coe _)).mpr fun j hj => ?_
  rw [degree_X_pow]
  exact WithBot.coe_lt_coe.mpr (Nat.mul_lt_mul_of_pos_right (mem_range.mp hj) hr)

lemma layer_succ (q r : ℕ) :
    layer (q + 1) r = (∑ j ∈ range q, (X : ℕ[X]) ^ (j * r)) + X ^ (q * r) := by
  unfold layer
  rw [sum_range_succ]

lemma layer_monic {p r : ℕ} (hp : 1 ≤ p) (hr : 1 ≤ r) : (layer p r).Monic := by
  obtain ⟨q, rfl⟩ : ∃ q, p = q + 1 := ⟨p - 1, by omega⟩
  rw [layer_succ]
  exact Monic.add_of_right (monic_X_pow _) (degree_lower_lt q r hr)

lemma natDegree_layer {p r : ℕ} (hp : 1 ≤ p) (hr : 1 ≤ r) :
    (layer p r).natDegree = (p - 1) * r := by
  obtain ⟨q, rfl⟩ : ∃ q, p = q + 1 := ⟨p - 1, by omega⟩
  rw [layer_succ, natDegree_add_eq_right_of_degree_lt (degree_lower_lt q r hr),
    natDegree_X_pow]
  simp

/-- The degree of the Poincaré polynomial is `L`: the radical length is
`1 + ∑ (p - 1) r n_r`. -/
theorem natDegree_poincare {ι : Type*} (s : Finset ι) {p : ℕ} (hp : 1 ≤ p)
    (r n : ι → ℕ) (hr : ∀ i ∈ s, 1 ≤ r i) :
    (poincare s p r n).natDegree = L s p r n := by
  unfold poincare L
  rw [natDegree_prod_of_monic _ _ (fun i hi => (layer_monic hp (hr i hi)).pow _)]
  refine sum_congr rfl fun i hi => ?_
  rw [(layer_monic hp (hr i hi)).natDegree_pow, natDegree_layer hp (hr i hi)]

lemma eval_one_layer (p r : ℕ) : (layer p r).eval 1 = p := by
  unfold layer
  simp [eval_finsetSum]

/-- The total dimension: `∑ dim J^i/J^(i+1) = p^(∑ n_r)`. -/
theorem eval_one_poincare {ι : Type*} (s : Finset ι) (p : ℕ) (r n : ι → ℕ) :
    (poincare s p r n).eval 1 = p ^ (∑ i ∈ s, n i) := by
  unfold poincare
  rw [eval_prod]
  simp only [eval_pow, eval_one_layer]
  exact prod_pow_eq_pow_sum s n p

end BensonRepresentations.JenningsPoincare

#print axioms BensonRepresentations.JenningsPoincare.reflect_layer
#print axioms BensonRepresentations.JenningsPoincare.reflect_poincare
#print axioms BensonRepresentations.JenningsPoincare.coeff_symm
#print axioms BensonRepresentations.JenningsPoincare.natDegree_poincare
#print axioms BensonRepresentations.JenningsPoincare.eval_one_poincare
