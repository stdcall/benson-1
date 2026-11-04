import Mathlib.LinearAlgebra.Span.Basic

/-!
# Proposition 2.2.7: the centre of `Λ` from the module category

Benson, *Representations and Cohomology I*, Section 2.2, proof of
Proposition 2.2.7 (`prop:morita-centres`): multiplication by `λ ∈ Z(Λ)` is a
natural transformation from the identity functor of `Λ-Mod` to itself, and
conversely every such natural transformation `φ` is multiplication by
`λ = φ_Λ(1)`, which then lies in `Z(Λ)`.

Formalised: `NatEndo Λ` is a family of `Λ`-linear endomorphisms `φ_M` of all
left `Λ`-modules `M` (in the universe of `Λ`) natural in `M`;
`app_eq_smul` (`φ_M(m) = φ_Λ(1) • m`, by naturality for `f : Λ → M`,
`f(μ) = μ m`), `central` (`φ_Λ(1)` is central), `ofCentral` (the natural
transformation given by a central element) and `ofCentral_app_one`: the two
constructions are inverse, so natural endomorphisms of the identity functor
correspond to `Z(Λ)`.

Not covered: that the correspondence is a ring isomorphism (composition of
natural transformations), and the conclusion `Z(Λ) ≅ Z(Γ)` for equivalent
module categories (transport of natural transformations along an
equivalence).
-/

namespace BensonRepresentations.CentreNaturalEndo

universe u

/-- A natural endomorphism of the identity functor of `Λ-Mod`. -/
structure NatEndo (Λ : Type u) [Ring Λ] where
  app : ∀ (M : Type u) [AddCommGroup M] [Module Λ M], M →ₗ[Λ] M
  natural : ∀ (M N : Type u) [AddCommGroup M] [Module Λ M] [AddCommGroup N] [Module Λ N]
    (f : M →ₗ[Λ] N) (m : M), f (app M m) = app N (f m)

variable {Λ : Type u} [Ring Λ]

/-- `φ_M(m) = λ m` with `λ = φ_Λ(1)` (naturality for `f : Λ → M`, `f(μ) = μ m`). -/
theorem app_eq_smul (φ : NatEndo Λ) (M : Type u) [AddCommGroup M] [Module Λ M] (m : M) :
    φ.app M m = φ.app Λ 1 • m := by
  have h := φ.natural Λ M (LinearMap.toSpanSingleton Λ M m) 1
  rw [LinearMap.toSpanSingleton_apply, LinearMap.toSpanSingleton_apply_one] at h
  exact h.symm

/-- `λ = φ_Λ(1)` is central: `φ_Λ(μ) = λ μ` by naturality and `= μ λ` by
`Λ`-linearity of `φ_Λ`. -/
theorem central (φ : NatEndo Λ) (μ : Λ) : φ.app Λ 1 * μ = μ * φ.app Λ 1 := by
  have h1 : φ.app Λ μ = φ.app Λ 1 * μ := by rw [app_eq_smul φ Λ μ, smul_eq_mul]
  have h2 : φ.app Λ μ = μ * φ.app Λ 1 := by
    have h := (φ.app Λ).map_smul μ 1
    rw [smul_eq_mul, mul_one, smul_eq_mul] at h
    exact h
  rw [← h1, h2]

/-- Multiplication by a central element is a natural endomorphism. -/
def ofCentral (c : Λ) (hc : ∀ μ : Λ, c * μ = μ * c) : NatEndo Λ where
  app M _ _ :=
    { toFun := fun m => c • m
      map_add' := smul_add c
      map_smul' := fun μ m => by
        simp only [RingHom.id_apply, smul_smul, hc μ] }
  natural M N _ _ _ _ f m := by
    simp only [LinearMap.coe_mk, AddHom.coe_mk, map_smul]

/-- The central element of `ofCentral c` is `c`. -/
theorem ofCentral_app_one (c : Λ) (hc : ∀ μ : Λ, c * μ = μ * c) :
    (ofCentral c hc).app Λ 1 = c := by
  simp [ofCentral]

/-- Every natural endomorphism is `ofCentral` of its central element. -/
theorem eq_ofCentral (φ : NatEndo Λ) (M : Type u) [AddCommGroup M] [Module Λ M] (m : M) :
    φ.app M m = (ofCentral (φ.app Λ 1) (central φ)).app M m := by
  rw [app_eq_smul]
  rfl

end BensonRepresentations.CentreNaturalEndo

#print axioms BensonRepresentations.CentreNaturalEndo.app_eq_smul
#print axioms BensonRepresentations.CentreNaturalEndo.central
#print axioms BensonRepresentations.CentreNaturalEndo.ofCentral_app_one
#print axioms BensonRepresentations.CentreNaturalEndo.eq_ofCentral
