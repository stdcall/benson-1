import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Order.ModularLattice

/-!
# Lemma 4.11.4: an inequality of dimensions for a square-zero endomorphism

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), printed p. 139, Lemma 4.11.4: "Suppose `d : V → V` is an endomorphism
with `d² = 0`.  If `U₁ ≤ U₂` are subspaces of `V` then
`dim U₂/U₁ ≥ dim dU₂/dU₁ + dim d⁻¹U₂/d⁻¹U₁`", and its proof: `d` defines
isomorphisms `d⁻¹U₂/d⁻¹U₁ ≅ ((U₂ ∩ Im(d)) + U₁)/U₁` and
`U₂/(U₂ ∩ (Ker(d) + U₁)) ≅ dU₂/dU₁`, and
`U₁ ≤ (U₂ ∩ Im(d)) + U₁ ≤ U₂ ∩ (Ker(d) + U₁) ≤ U₂`.  The lemma is the key
step of the proof of Proposition 4.11.5 (the functorial filtration for
`k⟨X, Y⟩/(X², Y²)`).

Notation.  `V` is a finite dimensional vector space over a division ring `K`
(the book: a field `k`; `V` finite dimensional as the modules there are);
`dU` is `U.map d`, `d⁻¹U` is `U.comap d`.  Dimensions of quotients are
written as differences: the lemma is stated as
`dim dU₂ + dim d⁻¹U₂ + dim U₁ ≤ dim U₂ + dim dU₁ + dim d⁻¹U₁`.

* `finrank_map_add`, `finrank_comap`: rank-nullity for `d` on `U` and on
  `d⁻¹U`.
* `chain`: the inclusions of the proof (here `d² = 0` gives `Im(d) ≤ Ker(d)`).
* `finrank_comap_quotient`, `finrank_map_quotient`: the two isomorphisms of
  the proof, as equalities of dimensions of the quotients.
* `square_zero_dim`: the lemma.

Not covered: the use of the lemma in Proposition 4.11.5 (its consequence
`dim CᵏM/Cᵏ0 ≥ dim dCᵏM/dCᵏ0 + dim d⁻¹CᵏM/d⁻¹Cᵏ0` for words `C`); the
filtration itself is checked on modules in `checks/sage/chapter-4b.py`.
-/

namespace BensonRepresentations.SquareZeroDimension

variable {K V : Type*} [DivisionRing K] [AddCommGroup V] [Module K V]
  [FiniteDimensional K V]

open Module Submodule LinearMap

/-- Rank-nullity for `d` restricted to `U`. -/
theorem finrank_map_add (d : V →ₗ[K] V) (U : Submodule K V) :
    finrank K (U.map d) + finrank K ↥(U ⊓ ker d) = finrank K U := by
  have h := LinearMap.finrank_range_add_finrank_ker (d.domRestrict U)
  rw [LinearMap.range_domRestrict, LinearMap.ker_domRestrict] at h
  have e : (ker d).comap U.subtype = (U ⊓ ker d).comap U.subtype := by
    ext x
    simp
  rw [e, LinearEquiv.finrank_eq (Submodule.comapSubtypeEquivOfLe inf_le_left)] at h
  exact h

/-- `dim d⁻¹U = dim Ker(d) + dim (U ∩ Im(d))`. -/
theorem finrank_comap (d : V →ₗ[K] V) (U : Submodule K V) :
    finrank K (U.comap d) = finrank K (ker d) + finrank K ↥(U ⊓ range d) := by
  have h := finrank_map_add d (U.comap d)
  rw [Submodule.map_comap_eq] at h
  have hk : U.comap d ⊓ ker d = ker d := by
    apply inf_eq_right.mpr
    intro x hx
    rw [LinearMap.mem_ker] at hx
    simp [hx]
  rw [hk, inf_comm] at h
  omega

omit [FiniteDimensional K V] in
/-- `d² = 0` gives `Im(d) ≤ Ker(d)`. -/
theorem range_le_ker (d : V →ₗ[K] V) (hd : d ∘ₗ d = 0) : range d ≤ ker d := by
  rintro _ ⟨x, rfl⟩
  rw [LinearMap.mem_ker, ← LinearMap.comp_apply, hd, LinearMap.zero_apply]

omit [FiniteDimensional K V] in
/-- The inclusions `U₁ ≤ (U₂ ∩ Im(d)) + U₁ ≤ U₂ ∩ (Ker(d) + U₁) ≤ U₂`. -/
theorem chain (d : V →ₗ[K] V) (hd : d ∘ₗ d = 0) {U₁ U₂ : Submodule K V}
    (h : U₁ ≤ U₂) :
    U₁ ≤ (U₂ ⊓ range d) ⊔ U₁ ∧ (U₂ ⊓ range d) ⊔ U₁ ≤ U₂ ⊓ (ker d ⊔ U₁) ∧
      U₂ ⊓ (ker d ⊔ U₁) ≤ U₂ :=
  ⟨le_sup_right,
    sup_le (le_inf inf_le_left (le_sup_of_le_left (inf_le_right.trans (range_le_ker d hd))))
      (le_inf h le_sup_right),
    inf_le_left⟩

/-- `d⁻¹U₂/d⁻¹U₁ ≅ ((U₂ ∩ Im(d)) + U₁)/U₁`, as dimensions. -/
theorem finrank_comap_quotient (d : V →ₗ[K] V) {U₁ U₂ : Submodule K V}
    (h : U₁ ≤ U₂) :
    finrank K (U₂.comap d) + finrank K U₁ =
      finrank K ↥((U₂ ⊓ range d) ⊔ U₁) + finrank K (U₁.comap d) := by
  have c1 := finrank_comap d U₁
  have c2 := finrank_comap d U₂
  have key := Submodule.finrank_sup_add_finrank_inf_eq (U₂ ⊓ range d) U₁
  have hinf : (U₂ ⊓ range d) ⊓ U₁ = U₁ ⊓ range d := by
    apply le_antisymm
    · exact le_inf inf_le_right (inf_le_left.trans inf_le_right)
    · exact le_inf (le_inf (inf_le_left.trans h) inf_le_right) inf_le_left
  rw [hinf] at key
  omega

/-- `U₂/(U₂ ∩ (Ker(d) + U₁)) ≅ dU₂/dU₁`, as dimensions. -/
theorem finrank_map_quotient (d : V →ₗ[K] V) {U₁ U₂ : Submodule K V}
    (h : U₁ ≤ U₂) :
    finrank K U₂ + finrank K (U₁.map d) =
      finrank K ↥(U₂ ⊓ (ker d ⊔ U₁)) + finrank K (U₂.map d) := by
  have m1 := finrank_map_add d U₁
  have m2 := finrank_map_add d U₂
  have hmod : U₂ ⊓ (ker d ⊔ U₁) = U₁ ⊔ (U₂ ⊓ ker d) := by
    rw [sup_comm, inf_comm, sup_inf_assoc_of_le _ h, inf_comm]
  have key := Submodule.finrank_sup_add_finrank_inf_eq U₁ (U₂ ⊓ ker d)
  have hinf : U₁ ⊓ (U₂ ⊓ ker d) = U₁ ⊓ ker d := by
    rw [← inf_assoc, inf_eq_left.mpr h]
  rw [hinf] at key
  rw [hmod]
  omega

/-- Lemma 4.11.4: `dim U₂/U₁ ≥ dim dU₂/dU₁ + dim d⁻¹U₂/d⁻¹U₁`. -/
theorem square_zero_dim (d : V →ₗ[K] V) (hd : d ∘ₗ d = 0) {U₁ U₂ : Submodule K V}
    (h : U₁ ≤ U₂) :
    finrank K (U₂.map d) + finrank K (U₂.comap d) + finrank K U₁ ≤
      finrank K U₂ + finrank K (U₁.map d) + finrank K (U₁.comap d) := by
  have q1 := finrank_comap_quotient d h
  have q2 := finrank_map_quotient d h
  have hc := chain d hd h
  have mono := Submodule.finrank_mono hc.2.1
  omega

end BensonRepresentations.SquareZeroDimension

#print axioms BensonRepresentations.SquareZeroDimension.finrank_map_add
#print axioms BensonRepresentations.SquareZeroDimension.finrank_comap
#print axioms BensonRepresentations.SquareZeroDimension.chain
#print axioms BensonRepresentations.SquareZeroDimension.finrank_comap_quotient
#print axioms BensonRepresentations.SquareZeroDimension.finrank_map_quotient
#print axioms BensonRepresentations.SquareZeroDimension.square_zero_dim
