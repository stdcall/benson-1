import Mathlib.Algebra.GroupWithZero.Action.Defs
import Mathlib.Algebra.Group.Action.Basic
import Mathlib.Tactic.Abel

/-!
# Group extensions and low degree cocycles

Section 3.7, Propositions 3.7.2 and 3.7.3 (pp. 75–76). A group `G` acts on an
abelian group `M` (written additively, `g • m` = the module action). For a
function `α : G → G → M` the set of pairs `(m, g)` carries the multiplication
of the proof of Proposition 3.7.3,

`(m₁, g₁)(m₂, g₂) = (m₁ + g₁ m₂ + α[g₁|g₂], g₁ g₂)`;

`α = 0` gives the split extension, whose elements Benson writes as matrices
`(1 0; m g)`.

* `assoc_iff_cocycle`: the multiplication is associative iff `α` is a
  2-cocycle for the bar resolution,
  `α[g₁|g₂] + α[g₁g₂|g₃] = g₁ α[g₂|g₃] + α[g₁|g₂g₃]` (Proposition 3.7.3).
* `shift_mul_iff`: the bijection `(m, g) ↦ (m + β[g], g)` (new coset
  representatives `β[g] ĝ`) is multiplicative from the `α'`-product to the
  `α`-product iff `α' = α + δβ`, i.e.
  `α'[g₁|g₂] = α[g₁|g₂] + β[g₁] + g₁ β[g₂] - β[g₁g₂]` (proof of 3.7.3).
* `section_mul_iff`: in the split extension `g ↦ (β[g], g)` is a homomorphism
  iff `β` is a 1-cocycle, `β[g₁] + g₁ β[g₂] = β[g₁g₂]` (Proposition 3.7.2).
* `mul_inv_split`, `conj_complement`: in the split extension
  `(-g'⁻¹ m, g'⁻¹)` is a right inverse of `(m, g')`, and conjugating the
  complement of a 1-cocycle `β` by `(m, g')` (product with this element) gives
  the complement of `β'` with `β'[g] - β[g] = (1 - g)(m - β[g'])` (proof of
  Proposition 3.7.2).

Not covered: that every extension is isomorphic to one of these models (the
choice of coset representatives), that an isomorphism of extensions has the
form `(m, g) ↦ (m + β[g], g)`, the identity element and inverses for a general
cocycle, and the identification of the classes with `Ext^n_RG(R, M)`.
Exhaustive finite checks of the counts are in `checks/sage/chapter-3a.py`.
-/

namespace BensonRepresentations.GroupExtensionCocycle

variable {G M : Type*} [Group G] [AddCommGroup M] [DistribMulAction G M]

/-- The multiplication of the proof of Proposition 3.7.3 on pairs `(m, g)`. -/
def mul (α : G → G → M) (x y : M × G) : M × G :=
  (x.1 + x.2 • y.1 + α x.2 y.2, x.2 * y.2)

/-- The 2-cocycle condition `δα = 0` for the bar resolution. -/
def IsCocycle₂ (α : G → G → M) : Prop :=
  ∀ g₁ g₂ g₃ : G, α g₁ g₂ + α (g₁ * g₂) g₃ = g₁ • α g₂ g₃ + α g₁ (g₂ * g₃)

/-- The 1-cocycle condition. -/
def IsCocycle₁ (β : G → M) : Prop :=
  ∀ g₁ g₂ : G, β g₁ + g₁ • β g₂ = β (g₁ * g₂)

theorem assoc_iff_cocycle (α : G → G → M) :
    (∀ x y z : M × G, mul α (mul α x y) z = mul α x (mul α y z)) ↔
      IsCocycle₂ α := by
  constructor
  · intro h g₁ g₂ g₃
    have e := congrArg Prod.fst (h (0, g₁) (0, g₂) (0, g₃))
    simp only [mul, smul_zero, zero_add, add_zero] at e
    simpa [add_comm, add_left_comm, add_assoc] using e
  · intro h x y z
    obtain ⟨m₁, g₁⟩ := x
    obtain ⟨m₂, g₂⟩ := y
    obtain ⟨m₃, g₃⟩ := z
    simp only [mul, Prod.mk.injEq, mul_assoc, and_true]
    rw [smul_add, smul_add, mul_smul]
    have := h g₁ g₂ g₃
    rw [← sub_eq_zero]
    rw [← sub_eq_zero] at this
    rw [← this]
    abel

/-- New coset representatives: `(m, g) ↦ (m + β[g], g)`. -/
def shift (β : G → M) (x : M × G) : M × G := (x.1 + β x.2, x.2)

omit [Group G] [DistribMulAction G M] in
theorem shift_bijective (β : G → M) : Function.Bijective (shift β) := by
  refine ⟨fun x y h => ?_, fun y => ⟨(y.1 - β y.2, y.2), ?_⟩⟩
  · obtain ⟨m₁, g₁⟩ := x
    obtain ⟨m₂, g₂⟩ := y
    simp only [shift, Prod.mk.injEq] at h
    obtain ⟨h1, rfl⟩ := h
    simpa using h1
  · simp [shift]

theorem shift_mul_iff (α α' : G → G → M) (β : G → M) :
    (∀ x y : M × G, shift β (mul α' x y) = mul α (shift β x) (shift β y)) ↔
      ∀ g₁ g₂ : G, α' g₁ g₂ = α g₁ g₂ + β g₁ + g₁ • β g₂ - β (g₁ * g₂) := by
  constructor
  · intro h g₁ g₂
    have e := congrArg Prod.fst (h (0, g₁) (0, g₂))
    simp only [shift, mul, smul_zero, zero_add, add_zero] at e
    rw [eq_sub_iff_add_eq, e]
    abel
  · intro h x y
    obtain ⟨m₁, g₁⟩ := x
    obtain ⟨m₂, g₂⟩ := y
    simp only [shift, mul, Prod.mk.injEq, and_true, smul_add]
    rw [h g₁ g₂]
    abel

theorem section_mul_iff (β : G → M) :
    (∀ g₁ g₂ : G, mul (fun _ _ => (0 : M)) (β g₁, g₁) (β g₂, g₂) =
        (β (g₁ * g₂), g₁ * g₂)) ↔ IsCocycle₁ β := by
  simp [mul, IsCocycle₁]

/-- In the split extension `(-g'⁻¹ m, g'⁻¹)` is a right inverse of `(m, g')`. -/
theorem mul_inv_split (m : M) (g' : G) :
    mul (fun _ _ => (0 : M)) (m, g') (-(g'⁻¹ • m), g'⁻¹) = (0, 1) := by
  simp [mul, smul_neg, smul_inv_smul]

/-- Conjugating the complement `{(β[g], g)}` by `(m, g')` sends `(β[g], g)`
to `(β'[h], h)` with `h = g' g g'⁻¹` and `β'[h] - β[h] = (1 - h)(m - β[g'])`. -/
theorem conj_complement (β : G → M) (hβ : IsCocycle₁ β) (m : M) (g' g : G) :
    mul (fun _ _ => (0 : M)) (mul (fun _ _ => (0 : M)) (m, g') (β g, g))
        (-(g'⁻¹ • m), g'⁻¹) =
      (β (g' * g * g'⁻¹) + ((m - β g') - (g' * g * g'⁻¹) • (m - β g')),
        g' * g * g'⁻¹) := by
  have hhg : g' * g * g'⁻¹ * g' = g' * g := by
    rw [mul_assoc (g' * g) g'⁻¹ g', inv_mul_cancel, mul_one]
  have c1 := hβ (g' * g * g'⁻¹) g'
  have c2 := hβ g' g
  rw [hhg, ← c2] at c1
  simp only [mul, add_zero, Prod.mk.injEq, and_true]
  have e : (g' * g) • -(g'⁻¹ • m) = -((g' * g * g'⁻¹) • m) := by
    rw [smul_neg, ← mul_smul]
  rw [e, smul_sub]
  have hb : β (g' * g * g'⁻¹) = β g' + g' • β g - (g' * g * g'⁻¹) • β g' := by
    rw [← c1]
    abel
  rw [hb]
  abel

end BensonRepresentations.GroupExtensionCocycle

#print axioms BensonRepresentations.GroupExtensionCocycle.assoc_iff_cocycle
#print axioms BensonRepresentations.GroupExtensionCocycle.shift_bijective
#print axioms BensonRepresentations.GroupExtensionCocycle.shift_mul_iff
#print axioms BensonRepresentations.GroupExtensionCocycle.section_mul_iff
#print axioms BensonRepresentations.GroupExtensionCocycle.mul_inv_split
#print axioms BensonRepresentations.GroupExtensionCocycle.conj_complement
