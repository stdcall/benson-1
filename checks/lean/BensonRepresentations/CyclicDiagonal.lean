import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Int.Defs
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# The Cartan–Eilenberg diagonal approximation for a cyclic group

Section 3.5, p. 67 (after Proposition 3.5.5): for `Z/n = ⟨x⟩` and the periodic
free resolution `P` of `R` with generators `e_m` and `d e_m = D_m e_(m-1)`,
`D_m = x - 1` for odd `m` (the resolution of Cartan and Eilenberg) and
`D_m = N = 1 + x + ⋯ + x^(n-1)` for even `m ≥ 2`, the diagonal approximation is
`Δ(e_m) = ∑_(r+s=m) Δ_rs(1) (e_r ⊗ e_s)` with

* `Δ_rs(1) = 1 ⊗ 1` for `r` even,
* `Δ_rs(1) = 1 ⊗ x` for `r` odd, `s` even,
* `Δ_rs(1) = ∑_(0 ≤ i < j ≤ n-1) x^i ⊗ x^j` for `r`, `s` odd (corrected from the
  printed `i ≤ j`).

Notation: `R(Z/n) ⊗_R R(Z/n) = R(Z/n × Z/n)` is a commutative ring `A` in which
`x ⊗ 1` is `x` and `1 ⊗ x` is `y`; `Z/n` acts on `P ⊗ P` diagonally, by `x y`.
Since `Δ` is a map of `R(Z/n)`-modules, it is a chain map iff for all `r, s`
the coefficient of `e_r ⊗ e_s` in `Δ(d e_(r+s+1)) = (d ⊗ 1 + (-1)^r 1 ⊗ d) Δ(e_(r+s+1))`
agrees:

`D_(r+s+1)(x y) Δ_rs = Δ_(r+1,s) D_(r+1)(x) + (-1)^r Δ_(r,s+1) D_(s+1)(y)`.

* `mul_S_sub_one_left`, `mul_S_sub_one_right`: the two telescoping identities
  for `S = ∑_(i<j) x^i y^j` (no relation needed).
* `chain_map`: the coefficient identity above for every `n`, `r`, `s` in any
  commutative ring with `y^n = 1` (so in particular in `R(Z/n × Z/n)`).
* `printed_not_chain_map`: with the printed `i ≤ j` the identity fails
  (`n = 2`, `r = 0`, `s = 1`, evaluated at the character `x = y = -1` of
  `Z/2 × Z/2` with values in `ℤ`).

Not covered: the passage from the coefficient identities to the chain map on
`P ⊗ P` (bookkeeping of the free bases, checked in `checks/sage/chapter-3a.py`
for `n ≤ 8` and total degree `≤ 6`), the augmentation in degree 0, and the cup
product computation of Proposition 3.5.5. With `T = 1 - x` of
Proposition 3.5.1 the odd–odd component changes sign (Sage only).
-/

namespace BensonRepresentations.CyclicDiagonal

open Finset

variable {A : Type*} [CommRing A]

/-- `N(z) = 1 + z + ⋯ + z^(n-1)`. -/
def norm (n : ℕ) (z : A) : A := ∑ i ∈ range n, z ^ i

/-- `S = ∑_(0 ≤ i < j ≤ n-1) x^i y^j`, grouped as `∑_j y^j ∑_(i<j) x^i`. -/
def S (n : ℕ) (x y : A) : A := ∑ j ∈ range n, y ^ j * ∑ i ∈ range j, x ^ i

/-- The printed `∑_(0 ≤ i ≤ j ≤ n-1) x^i y^j`: the terms `i = j` add `N(x y)`. -/
def S' (n : ℕ) (x y : A) : A := S n x y + norm n (x * y)

lemma norm_succ (n : ℕ) (z : A) : norm (n + 1) z = norm n z + z ^ n := by
  simp [norm, sum_range_succ]

lemma S_succ (n : ℕ) (x y : A) : S (n + 1) x y = S n x y + y ^ n * norm n x := by
  simp [S, norm, sum_range_succ]

lemma mul_norm (n : ℕ) (z : A) : (z - 1) * norm n z = z ^ n - 1 := by
  induction n with
  | zero => simp [norm]
  | succ n ih =>
    rw [norm_succ]
    linear_combination ih

/-- `(x - 1) S = N(x y) - N(y)`. -/
theorem mul_S_sub_one_left (n : ℕ) (x y : A) :
    (x - 1) * S n x y = norm n (x * y) - norm n y := by
  induction n with
  | zero => simp [S, norm]
  | succ n ih =>
    rw [S_succ, norm_succ, norm_succ]
    linear_combination ih + y ^ n * mul_norm n x

/-- `(y - 1) S = y^n N(x) - y N(x y)`. -/
theorem mul_S_sub_one_right (n : ℕ) (x y : A) :
    (y - 1) * S n x y = y ^ n * norm n x - y * norm n (x * y) := by
  induction n with
  | zero => simp [S, norm]
  | succ n ih =>
    rw [S_succ, norm_succ, norm_succ]
    linear_combination ih

/-- The coefficient `D_m(z)` of the differential `d e_m = D_m e_(m-1)`. -/
def D (n m : ℕ) (z : A) : A := if m % 2 = 1 then z - 1 else norm n z

/-- `Δ_rs(1)` of p. 67 for a given choice of the odd–odd component `S₀`. -/
def Δ (S₀ : A) (r s : ℕ) (y : A) : A :=
  if r % 2 = 0 then 1 else if s % 2 = 0 then y else S₀

/-- The coefficient identity of the chain map condition, for the corrected
`Δ_rs` (`i < j`), every `n`, `r`, `s`, in any commutative ring with `y^n = 1`. -/
theorem chain_map (n : ℕ) (x y : A) (hy : y ^ n = 1) (r s : ℕ) :
    D n (r + s + 1) (x * y) * Δ (S n x y) r s y =
      Δ (S n x y) (r + 1) s y * D n (r + 1) x +
        (-1) ^ r * Δ (S n x y) r (s + 1) y * D n (s + 1) y := by
  have h1 := mul_S_sub_one_left n x y
  have h2 := mul_S_sub_one_right n x y
  rcases Nat.mod_two_eq_zero_or_one r with hr | hr <;>
    rcases Nat.mod_two_eq_zero_or_one s with hs | hs
  · -- r even, s even: x y - 1 = y (x - 1) + (y - 1)
    have hm : (r + s + 1) % 2 = 1 := by omega
    have hr1 : (r + 1) % 2 = 1 := by omega
    have hs1 : (s + 1) % 2 = 1 := by omega
    have he : (-1 : A) ^ r = 1 := by
      rw [← Nat.div_add_mod r 2, hr, pow_add, pow_mul]; simp
    simp only [D, Δ, hm, hr, hs, hr1, hs1, he]
    norm_num
    ring
  · -- r even, s odd: N(x y) = S (x - 1) + N(y)
    have hm : (r + s + 1) % 2 = 0 := by omega
    have hr1 : (r + 1) % 2 = 1 := by omega
    have hs1 : (s + 1) % 2 = 0 := by omega
    have he : (-1 : A) ^ r = 1 := by
      rw [← Nat.div_add_mod r 2, hr, pow_add, pow_mul]; simp
    simp only [D, Δ, hm, hr, hs, hr1, hs1, he]
    norm_num
    linear_combination -h1
  · -- r odd, s even: y N(x y) = N(x) - S (y - 1)
    have hm : (r + s + 1) % 2 = 0 := by omega
    have hr1 : (r + 1) % 2 = 0 := by omega
    have hs1 : (s + 1) % 2 = 1 := by omega
    have he : (-1 : A) ^ r = -1 := by
      rw [← Nat.div_add_mod r 2, hr, pow_add, pow_mul]; simp
    simp only [D, Δ, hm, hr, hs, hr1, hs1, he]
    norm_num
    rw [hy] at h2
    linear_combination h2
  · -- r odd, s odd: (x y - 1) S = N(x) - y N(y)
    have hm : (r + s + 1) % 2 = 1 := by omega
    have hr1 : (r + 1) % 2 = 0 := by omega
    have hs1 : (s + 1) % 2 = 0 := by omega
    have he : (-1 : A) ^ r = -1 := by
      rw [← Nat.div_add_mod r 2, hr, pow_add, pow_mul]; simp
    simp only [D, Δ, hm, hr, hs, hr1, hs1, he]
    norm_num
    rw [hy] at h2
    linear_combination y * h1 + h2

/-- With the printed `i ≤ j` the identity fails: `n = 2`, `r = 0`, `s = 1`, at the
character `x = y = -1` of `Z/2 × Z/2` in `ℤ` (where `y^2 = 1`). -/
theorem printed_not_chain_map :
    ¬ (D 2 (0 + 1 + 1) ((-1 : ℤ) * (-1)) * Δ (S' 2 (-1 : ℤ) (-1)) 0 1 (-1) =
      Δ (S' 2 (-1 : ℤ) (-1)) (0 + 1) 1 (-1) * D 2 (0 + 1) (-1) +
        (-1) ^ 0 * Δ (S' 2 (-1 : ℤ) (-1)) 0 (1 + 1) (-1) * D 2 (1 + 1) (-1)) := by
  decide

end BensonRepresentations.CyclicDiagonal

#print axioms BensonRepresentations.CyclicDiagonal.mul_S_sub_one_left
#print axioms BensonRepresentations.CyclicDiagonal.mul_S_sub_one_right
#print axioms BensonRepresentations.CyclicDiagonal.chain_map
#print axioms BensonRepresentations.CyclicDiagonal.printed_not_chain_map
