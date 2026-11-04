import Mathlib.Algebra.CharP.Lemmas
import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.Tactic.NoncommRing

/-!
# Dimension subgroups

Section 3.14, p. 93 (Jennings' theorem): for a `p`-group `P` and the powers
`J^r(kP)` of the radical of `kP`, the dimension subgroups
`F_r(P) = {g ∈ P | g - 1 ∈ J^r(kP)}` are normal subgroups, the `p`-th power of
an element of `F_r(P)` lies in `F_(pr)(P)`, and `[F_r(P), F_s(P)] ⊆ F_(r+s)(P)`,
by the identities

* `gh - 1 = (g - 1) + (h - 1) + (g - 1)(h - 1)`,
* `g⁻¹ - 1 = -g⁻¹(g - 1)`, `hgh⁻¹ - 1 = h(g - 1)h⁻¹`,
* `g^p - 1 = (g - 1)^p` (characteristic `p`),
* `[g, h] - 1 = ((g - 1)(h - 1) - (h - 1)(g - 1)) g⁻¹ h⁻¹`, `[g, h] = g h g⁻¹ h⁻¹`.

Notation: `A` is any ring (for the book, `A = kP`), `J r` an additive subgroup
of `A` for every `r : ℕ` with `J r * J s ⊆ J (r + s)` and `A * J r ⊆ J r`,
`J r * A ⊆ J r` (the powers of a two-sided ideal satisfy these); the group is
the unit group `Aˣ` (for the book, `P ⊆ (kP)ˣ`; `F_r(P)` is the intersection of
`P` with the subgroup below, so it inherits all the properties).

* `F`: `{g : Aˣ | g - 1 ∈ J r}` is a subgroup.
* `F_normal`: it is normal.
* `commutator_mem`: `g ∈ F r`, `h ∈ F s` give `g h g⁻¹ h⁻¹ ∈ F (r + s)`.
* `pow_char_mem`: in characteristic `p` (prime), `g ∈ F r` gives `g^p ∈ F (p r)`.

Not covered: `F_1(P) = P`, `F_2(P) = Φ(P)`, the equality `F_r(P) = Γ_r(P)` and
the dimension count of Theorem 3.14.6 (checked in `checks/sage/chapter-3b.py`
for all groups of order `p^k ≤ 32`, 81, 125, 49 and 13 of order 64).
-/

namespace BensonRepresentations.DimensionSubgroups

variable {A : Type*} [Ring A]

/-- A multiplicative family of two-sided ideals, such as the powers of the
radical: `J r * J s ⊆ J (r + s)`. -/
structure Filtration (A : Type*) [Ring A] where
  J : ℕ → AddSubgroup A
  mul_mem : ∀ {r s : ℕ} {a b : A}, a ∈ J r → b ∈ J s → a * b ∈ J (r + s)
  mul_left : ∀ {r : ℕ} (x : A) {a : A}, a ∈ J r → x * a ∈ J r
  mul_right : ∀ {r : ℕ} {a : A} (x : A), a ∈ J r → a * x ∈ J r

variable (Φ : Filtration A)

/-- The dimension subgroup `F r = {g | g - 1 ∈ J r}` of the unit group. -/
def F (r : ℕ) : Subgroup Aˣ where
  carrier := {g | (g : A) - 1 ∈ Φ.J r}
  one_mem' := by simp
  mul_mem' := by
    intro g h hg hh
    simp only [Set.mem_ofPred_eq, Units.val_mul] at *
    have e : (g : A) * h - 1 = ((g : A) - 1) + ((h : A) - 1) +
        ((g : A) - 1) * ((h : A) - 1) := by noncomm_ring
    rw [e]
    exact add_mem (add_mem hg hh) (Φ.mul_right _ hg)
  inv_mem' := by
    intro g hg
    simp only [Set.mem_ofPred_eq] at *
    have e : ((g⁻¹ : Aˣ) : A) - 1 = -(((g⁻¹ : Aˣ) : A) * ((g : A) - 1)) := by
      rw [mul_sub, Units.inv_mul, mul_one]; abel
    rw [e]
    exact neg_mem (Φ.mul_left _ hg)

lemma mem_F {r : ℕ} {g : Aˣ} : g ∈ F Φ r ↔ (g : A) - 1 ∈ Φ.J r := Iff.rfl

/-- `h g h⁻¹ - 1 = h (g - 1) h⁻¹`: `F r` is normal. -/
theorem F_normal (r : ℕ) : (F Φ r).Normal := by
  refine ⟨fun g hg h => ?_⟩
  rw [mem_F] at *
  have e : ((h * g * h⁻¹ : Aˣ) : A) - 1 =
      (h : A) * ((g : A) - 1) * ((h⁻¹ : Aˣ) : A) := by
    simp only [Units.val_mul]
    rw [mul_sub, sub_mul, mul_one, Units.mul_inv]
  rw [e]
  exact Φ.mul_right _ (Φ.mul_left _ hg)

/-- `[g, h] - 1 = ((g - 1)(h - 1) - (h - 1)(g - 1)) g⁻¹ h⁻¹`. -/
lemma commutator_sub_one (g h : Aˣ) :
    ((g * h * g⁻¹ * h⁻¹ : Aˣ) : A) - 1 =
      (((g : A) - 1) * ((h : A) - 1) - ((h : A) - 1) * ((g : A) - 1)) *
        (((g⁻¹ : Aˣ) : A) * ((h⁻¹ : Aˣ) : A)) := by
  have hg : (g : A) * ((g⁻¹ : Aˣ) : A) = 1 := Units.mul_inv g
  have hh : (h : A) * ((h⁻¹ : Aˣ) : A) = 1 := Units.mul_inv h
  have key : ((g : A) - 1) * ((h : A) - 1) - ((h : A) - 1) * ((g : A) - 1) =
      (g : A) * h - (h : A) * g := by noncomm_ring
  rw [key, sub_mul]
  simp only [Units.val_mul]
  have e1 : (g : A) * h * (((g⁻¹ : Aˣ) : A) * ((h⁻¹ : Aˣ) : A)) =
      (g : A) * h * ((g⁻¹ : Aˣ) : A) * ((h⁻¹ : Aˣ) : A) := by noncomm_ring
  have e2 : (h : A) * g * (((g⁻¹ : Aˣ) : A) * ((h⁻¹ : Aˣ) : A)) = 1 := by
    calc (h : A) * g * (((g⁻¹ : Aˣ) : A) * ((h⁻¹ : Aˣ) : A))
        = (h : A) * ((g : A) * ((g⁻¹ : Aˣ) : A)) * ((h⁻¹ : Aˣ) : A) := by
          noncomm_ring
      _ = 1 := by rw [hg, mul_one, hh]
  rw [e1, e2]

/-- `[F_r, F_s] ⊆ F_(r+s)`. -/
theorem commutator_mem {r s : ℕ} {g h : Aˣ} (hg : g ∈ F Φ r) (hh : h ∈ F Φ s) :
    g * h * g⁻¹ * h⁻¹ ∈ F Φ (r + s) := by
  rw [mem_F] at *
  rw [commutator_sub_one]
  refine Φ.mul_right _ (sub_mem (Φ.mul_mem hg hh) ?_)
  rw [add_comm]
  exact Φ.mul_mem hh hg

/-- `(g - 1)^k ∈ J (k r)` for `k ≥ 1`. -/
lemma pow_sub_one_mem {r : ℕ} {g : Aˣ} (hg : g ∈ F Φ r) :
    ∀ k : ℕ, ((g : A) - 1) ^ (k + 1) ∈ Φ.J ((k + 1) * r) := by
  intro k
  induction k with
  | zero => simpa [mem_F] using hg
  | succ k ih =>
    rw [pow_succ, show (k + 1 + 1) * r = (k + 1) * r + r by ring]
    exact Φ.mul_mem ih hg

/-- In characteristic `p`, `g^p - 1 = (g - 1)^p`, so `F_r^p ⊆ F_(pr)`. -/
theorem pow_char_mem (p : ℕ) [Fact p.Prime] [CharP A p] {r : ℕ} {g : Aˣ}
    (hg : g ∈ F Φ r) : g ^ p ∈ F Φ (p * r) := by
  rw [mem_F, Units.val_pow_eq_pow_val]
  have e : (g : A) ^ p - 1 = ((g : A) - 1) ^ p := by
    rw [sub_pow_char_of_commute (p := p) (Commute.one_right _), one_pow]
  rw [e]
  obtain ⟨k, hk⟩ : ∃ k, p = k + 1 := ⟨p - 1, (Nat.succ_pred_eq_of_pos
    (Fact.out : p.Prime).pos).symm⟩
  subst hk
  exact pow_sub_one_mem Φ hg k

end BensonRepresentations.DimensionSubgroups

#print axioms BensonRepresentations.DimensionSubgroups.F
#print axioms BensonRepresentations.DimensionSubgroups.F_normal
#print axioms BensonRepresentations.DimensionSubgroups.commutator_sub_one
#print axioms BensonRepresentations.DimensionSubgroups.commutator_mem
#print axioms BensonRepresentations.DimensionSubgroups.pow_char_mem
