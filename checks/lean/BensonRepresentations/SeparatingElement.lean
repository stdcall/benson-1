import Mathlib.RingTheory.RootsOfUnity.PrimitiveRoots
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Group.Conj
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic.LinearCombination

/-!
# The separating element of Lemma 5.3.1

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), Section 5.3, Lemma 5.3.1 and its proof, p. 175 of the printed book.
The author's list of corrections ("Comments and corrections", 8 September
2010) says that the printed proof uses the Mackey decomposition theorem
incorrectly, without giving a fix: the claim that `M_j↑^G↓_⟨g'⟩` is free when
`g'` is not conjugate into `⟨g⟩` fails (for `G` cyclic of order 4, `g = a²`,
`g' = a` the module has dimension 2; see `checks/sage/chapter-5.py`).  This
file proves the step that replaces it: the induced character formula gives
the values of `x = ∑_j e^(-2πij/n) [M_j↑^G]` directly.

Notation.  `G` is a finite group, `g ∈ G` has order `n = orderOf g`, `K` is a
field of characteristic zero (the book's `ℂ`) and `ζ ∈ K` a primitive `n`th
root of unity (the book's `e^(2πi/n)`, which corresponds to `ε`).  The
Brauer character of `M_j` (`g ↦ ε^j`) is `λ_j(g^m) = ζ^(jm)`.  The induced
class function `λ_j↑^G(y) = |⟨g⟩|⁻¹ ∑_(z ∈ G, z⁻¹yz ∈ ⟨g⟩) λ_j(z⁻¹yz)` is
written with exponents, `indLambda g ζ j y = n⁻¹ ∑_z ∑_(m < n) [z⁻¹yz = g^m]
ζ^(jm)` (the elements `g^m`, `m < n`, are the elements of `⟨g⟩`, each once).
The book's `e^(-2πij/n)` is `ζ⁻¹ ^ j`, with `j` running over `0, …, n - 1`
instead of `1, …, n` (the term `j = n` equals the term `j = 0`).

* `geom_mul`, `sum_root`: `∑_(j<n) ζ^(-j) ζ^(jm) = n` if `m ≡ 1 (mod n)`
  and `0` otherwise (`m < n`).
* `sum_indLambda`: `∑_(j<n) ζ^(-j) λ_j↑^G(y) = |{z ∈ G : z⁻¹ y z = g}|`.
* `sum_indLambda_ne_zero_iff`: this value is non-zero iff `y` is conjugate
  to `g`; so `t_y(x) ≠ 0` exactly for `y` conjugate to `g`, which is the
  statement of Lemma 5.3.1 (with `y` running over the `p'`-elements).

Not covered: that the Brauer character of an induced module is the induced
class function (Curtis–Reiner, *Methods of Representation Theory* I,
Lemma (21.28)); that `x ∈ A(G, 1)` (`M_j` is projective since `⟨g⟩` is a
`p'`-group); the choice of the isomorphism between roots of unity in `k̂`
and in `ℂ` (Section 5.3).  The formula is checked against the Brauer
characters of the induced modules over finite fields in
`checks/sage/chapter-5.py`.
-/

namespace BensonRepresentations.SeparatingElement

open Finset

variable {G : Type*} [Group G] [Fintype G] [DecidableEq G]
variable {K : Type*} [Field K]

/-- The induced class function of `λ_j` (`λ_j(g^m) = ζ^(jm)`) at `y`. -/
noncomputable def indLambda (g : G) (ζ : K) (j : ℕ) (y : G) : K :=
  ((orderOf g : ℕ) : K)⁻¹ *
    ∑ z : G, ∑ m ∈ range (orderOf g),
      if z⁻¹ * y * z = g ^ m then ζ ^ (j * m) else 0

lemma geom_mul (w : K) (n : ℕ) :
    (∑ j ∈ range n, w ^ j) * (w - 1) = w ^ n - 1 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [sum_range_succ, add_mul, ih, pow_succ]
    ring

/-- Orthogonality for the characters of a cyclic group. -/
lemma sum_root {n : ℕ} {ζ : K} (hζ : IsPrimitiveRoot ζ n) (hn : 0 < n)
    {m : ℕ} (hm : m < n) :
    ∑ j ∈ range n, ζ⁻¹ ^ j * ζ ^ (j * m) =
      if m = 1 % n then (n : K) else 0 := by
  have hz : ζ ≠ 0 := hζ.ne_zero hn.ne'
  have hterm : ∀ j, ζ⁻¹ ^ j * ζ ^ (j * m) = (ζ ^ m * ζ⁻¹) ^ j := by
    intro j
    rw [mul_pow, ← pow_mul, mul_comm m j, mul_comm]
  simp_rw [hterm]
  have h1 : ζ ^ (1 % n) = ζ := by
    rw [hζ.eq_orderOf, pow_mod_orderOf, pow_one]
  split_ifs with h
  · subst h
    rw [h1, mul_inv_cancel₀ hz]
    simp
  · have hw : ζ ^ m * ζ⁻¹ ≠ 1 := by
      intro hw
      have : ζ ^ m = ζ ^ (1 % n) := by
        rw [h1]
        field_simp at hw
        exact hw
      exact h (hζ.pow_inj hm (Nat.mod_lt _ hn) this)
    have hwn : (ζ ^ m * ζ⁻¹) ^ n = 1 := by
      rw [mul_pow, ← pow_mul, mul_comm m n, pow_mul, hζ.pow_eq_one, one_pow,
        inv_pow, hζ.pow_eq_one, inv_one, one_mul]
    have := geom_mul (ζ ^ m * ζ⁻¹) n
    rw [hwn, sub_self] at this
    exact (mul_eq_zero.mp this).resolve_right (sub_ne_zero.mpr hw)

theorem sum_indLambda [CharZero K] (g y : G) (ζ : K)
    (hζ : IsPrimitiveRoot ζ (orderOf g)) :
    ∑ j ∈ range (orderOf g), ζ⁻¹ ^ j * indLambda g ζ j y =
      ((univ.filter fun z : G => z⁻¹ * y * z = g).card : K) := by
  set n := orderOf g with hn_def
  have hn : 0 < n := orderOf_pos g
  have hnK : (n : K) ≠ 0 := Nat.cast_ne_zero.mpr hn.ne'
  have hg : g ^ (1 % n) = g := by rw [hn_def, pow_mod_orderOf, pow_one]
  unfold indLambda
  -- move the sum over j inside
  have step1 : ∑ j ∈ range n, ζ⁻¹ ^ j * ((n : K)⁻¹ * ∑ z : G,
      ∑ m ∈ range n, if z⁻¹ * y * z = g ^ m then ζ ^ (j * m) else 0) =
      (n : K)⁻¹ * ∑ z : G, ∑ m ∈ range n,
        if z⁻¹ * y * z = g ^ m then
          ∑ j ∈ range n, ζ⁻¹ ^ j * ζ ^ (j * m) else 0 := by
    simp only [mul_sum]
    rw [sum_comm]
    refine sum_congr rfl fun z _ => ?_
    rw [sum_comm]
    refine sum_congr rfl fun m _ => ?_
    split_ifs
    · rw [mul_sum]
      exact sum_congr rfl fun j _ => by ring
    · simp
  rw [step1]
  have step2 : ∀ z : G, (∑ m ∈ range n,
      if z⁻¹ * y * z = g ^ m then ∑ j ∈ range n, ζ⁻¹ ^ j * ζ ^ (j * m)
        else 0) = if z⁻¹ * y * z = g then (n : K) else 0 := by
    intro z
    have hsub : ∀ m ∈ range n, (if z⁻¹ * y * z = g ^ m then
        ∑ j ∈ range n, ζ⁻¹ ^ j * ζ ^ (j * m) else 0) =
        if m = 1 % n then (if z⁻¹ * y * z = g then (n : K) else 0)
          else 0 := by
      intro m hm
      rw [sum_root hζ hn (mem_range.mp hm)]
      by_cases h : m = 1 % n
      · subst h
        simp [hg]
      · simp [h]
    rw [sum_congr rfl hsub, sum_ite_eq' (range n) (1 % n)]
    simp [Nat.mod_lt _ hn]
  simp_rw [step2]
  rw [← sum_filter, sum_const, nsmul_eq_mul]
  field_simp

theorem sum_indLambda_ne_zero_iff [CharZero K] (g y : G) (ζ : K)
    (hζ : IsPrimitiveRoot ζ (orderOf g)) :
    ∑ j ∈ range (orderOf g), ζ⁻¹ ^ j * indLambda g ζ j y ≠ 0 ↔
      IsConj y g := by
  rw [sum_indLambda g y ζ hζ, Nat.cast_ne_zero, ← Nat.pos_iff_ne_zero,
    card_pos, isConj_iff]
  constructor
  · rintro ⟨z, hz⟩
    exact ⟨z⁻¹, by simpa using (mem_filter.mp hz).2⟩
  · rintro ⟨c, hc⟩
    exact ⟨c⁻¹, mem_filter.mpr ⟨mem_univ _, by simpa using hc⟩⟩

end BensonRepresentations.SeparatingElement

#print axioms BensonRepresentations.SeparatingElement.sum_root
#print axioms BensonRepresentations.SeparatingElement.sum_indLambda
#print axioms BensonRepresentations.SeparatingElement.sum_indLambda_ne_zero_iff
