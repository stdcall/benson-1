import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.Algebra.Algebra.Basic

/-!
# Lemma 2.6.2: an extension whose middle term is `M₁ ⊕ M₃` splits

Benson, *Representations and Cohomology I*, Section 2.6, Lemma 2.6.2
(`lem:isomorphic-middle-splits`): if `Λ` is an algebra over a field `k` and
`0 → M₁ → M₂ → M₃ → 0` is a short exact sequence of `Λ`-modules of finite
`k`-dimension with `M₂ ≅ M₁ ⊕ M₃`, the sequence splits.

The book's proof: in the exact sequence
`0 → Hom(M₃, M₁) → Hom(M₃, M₂) → Hom(M₃, M₃) → Ext¹(M₃, M₁)` the last map is
zero "by dimension counting", so `Hom(M₃, M₂) → Hom(M₃, M₃)` is onto and a
preimage of the identity splits the sequence.

Formalised here:

* `surjective_of_finrank_eq`: the dimension count, for an exact sequence
  `0 → A → B → C` of finite-dimensional `k`-spaces with
  `dim B = dim A + dim C`;
* `postcomp`: composition with a `Λ`-linear map, as a `k`-linear map of
  `Hom_Λ` spaces; `ker_postcomp`: left exactness of `Hom_Λ(M₃, -)`;
* `finrank_hom_of_equiv`: `dim Hom_Λ(M₃, M₂) = dim Hom_Λ(M₃, M₁) +
  dim Hom_Λ(M₃, M₃)` when `M₂ ≃ M₁ × M₃`;
* `exists_section_of_equiv_prod`: Lemma 2.6.2.

Notation: `i : M₁ → M₂`, `p : M₂ → M₃` the maps of the sequence; `M₁ ⊕ M₃` is
`M₁ × M₃`.  The hypothesis that `p` is onto is not needed (it follows).  Not
covered: the identification of the cokernel with `Ext¹` (the long exact
sequence) and the remark that the sequence then represents `0 ∈ Ext¹`.
-/

namespace BensonRepresentations.SplitOfIsoMiddle

open Module

/-- The dimension count: in an exact sequence `0 → A → B → C` of
finite-dimensional vector spaces with `dim B = dim A + dim C`, the last map is
onto. -/
theorem surjective_of_finrank_eq {k A B C : Type*} [Field k]
    [AddCommGroup A] [Module k A] [AddCommGroup B] [Module k B]
    [AddCommGroup C] [Module k C]
    [FiniteDimensional k A] [FiniteDimensional k B] [FiniteDimensional k C]
    (i : A →ₗ[k] B) (p : B →ₗ[k] C) (hi : Function.Injective i)
    (hexact : LinearMap.ker p = LinearMap.range i)
    (hdim : finrank k B = finrank k A + finrank k C) :
    Function.Surjective p := by
  have h1 := LinearMap.finrank_range_add_finrank_ker p
  rw [hexact, LinearMap.finrank_range_of_inj hi] at h1
  have h2 : finrank k (LinearMap.range p) = finrank k C := by omega
  rw [← LinearMap.range_eq_top]
  exact Submodule.eq_top_of_finrank_eq h2

variable {k Λ : Type*} [Field k] [Ring Λ] [Algebra k Λ]
variable {M M₁ M₂ M₃ : Type*} [AddCommGroup M] [Module Λ M]
  [AddCommGroup M₁] [Module Λ M₁] [Module k M₁] [IsScalarTower k Λ M₁]
  [AddCommGroup M₂] [Module Λ M₂] [Module k M₂] [IsScalarTower k Λ M₂]
  [AddCommGroup M₃] [Module Λ M₃] [Module k M₃] [IsScalarTower k Λ M₃]

/-- `Hom_Λ(M, N)` is finite dimensional over `k` when `M` and `N` are. -/
theorem finiteDimensional_hom [Module k M] [IsScalarTower k Λ M] [FiniteDimensional k M]
    [FiniteDimensional k M₁] : FiniteDimensional k (M →ₗ[Λ] M₁) :=
  FiniteDimensional.of_injective
    (LinearMap.restrictScalarsₗ (R := k) (S := Λ) (M := M) (N := M₁) (R₁ := k))
    (LinearMap.restrictScalars_injective k)

variable (k) in
/-- Composition with `g`, as a `k`-linear map `Hom_Λ(M, N) → Hom_Λ(M, N')`. -/
def postcomp (g : M₁ →ₗ[Λ] M₂) : (M →ₗ[Λ] M₁) →ₗ[k] (M →ₗ[Λ] M₂) where
  toFun f := g ∘ₗ f
  map_add' f f' := by ext x; simp
  map_smul' c f := by ext x; simp

@[simp]
theorem postcomp_apply (g : M₁ →ₗ[Λ] M₂) (f : M →ₗ[Λ] M₁) :
    postcomp k g f = g ∘ₗ f := rfl

theorem postcomp_injective (i : M₁ →ₗ[Λ] M₂) (hi : Function.Injective i) :
    Function.Injective (postcomp k (M := M) i) := by
  intro f f' h
  ext x
  exact hi (LinearMap.congr_fun h x)

/-- Left exactness of `Hom_Λ(M, -)`: if `Ker p = Im i` with `i` injective, the
maps `f` with `p ∘ f = 0` are exactly the `i ∘ g`. -/
theorem ker_postcomp (i : M₁ →ₗ[Λ] M₂) (p : M₂ →ₗ[Λ] M₃) (hi : Function.Injective i)
    (hexact : LinearMap.ker p = LinearMap.range i) :
    LinearMap.ker (postcomp k (M := M) p) = LinearMap.range (postcomp k (M := M) i) := by
  ext f
  simp only [LinearMap.mem_ker, LinearMap.mem_range, postcomp_apply]
  constructor
  · intro hf
    have hmem : ∀ x, f x ∈ LinearMap.range i := by
      intro x
      rw [← hexact, LinearMap.mem_ker]
      exact LinearMap.congr_fun hf x
    refine ⟨(LinearEquiv.ofInjective i hi).symm ∘ₗ
      f.codRestrict (LinearMap.range i) hmem, ?_⟩
    ext x
    simp
  · rintro ⟨g, rfl⟩
    ext x
    have : i (g x) ∈ LinearMap.ker p := by rw [hexact]; exact ⟨g x, rfl⟩
    simpa using this

theorem map_smul_scalar (e : M₂ ≃ₗ[Λ] M₁ × M₃) (c : k) (y : M₂) : e (c • y) = c • e y := by
  rw [← algebraMap_smul Λ c y, e.map_smul, algebraMap_smul]

/-- `Hom_Λ(M, M₂) ≃ Hom_Λ(M, M₁) × Hom_Λ(M, M₃)` over `k` when `M₂ ≃ M₁ × M₃`. -/
def homEquivProd (e : M₂ ≃ₗ[Λ] M₁ × M₃) :
    (M →ₗ[Λ] M₂) ≃ₗ[k] (M →ₗ[Λ] M₁) × (M →ₗ[Λ] M₃) where
  toFun f := (LinearMap.fst Λ M₁ M₃ ∘ₗ e.toLinearMap ∘ₗ f,
    LinearMap.snd Λ M₁ M₃ ∘ₗ e.toLinearMap ∘ₗ f)
  invFun gh := e.symm.toLinearMap ∘ₗ gh.1.prod gh.2
  map_add' f f' := by ext x <;> simp
  map_smul' c f := by ext x <;> simp [map_smul_scalar]
  left_inv f := by ext x; simp
  right_inv gh := by ext x <;> simp

theorem finrank_hom_of_equiv [Module k M] [IsScalarTower k Λ M] [FiniteDimensional k M]
    [FiniteDimensional k M₁]
    [FiniteDimensional k M₂] [FiniteDimensional k M₃] (e : M₂ ≃ₗ[Λ] M₁ × M₃) :
    finrank k (M →ₗ[Λ] M₂) = finrank k (M →ₗ[Λ] M₁) + finrank k (M →ₗ[Λ] M₃) := by
  have := finiteDimensional_hom (k := k) (Λ := Λ) (M := M) (M₁ := M₁)
  have := finiteDimensional_hom (k := k) (Λ := Λ) (M := M) (M₁ := M₃)
  rw [(homEquivProd (k := k) (M := M) e).finrank_eq, Module.finrank_prod]

/-- **Lemma 2.6.2.** If `0 → M₁ → M₂ → M₃` is exact (`i` injective,
`Ker p = Im i`), the modules are finite dimensional over `k` and
`M₂ ≅ M₁ ⊕ M₃`, then `p` has a section: the sequence splits. -/
theorem exists_section_of_equiv_prod [FiniteDimensional k M₁] [FiniteDimensional k M₂]
    [FiniteDimensional k M₃] (i : M₁ →ₗ[Λ] M₂) (p : M₂ →ₗ[Λ] M₃)
    (hi : Function.Injective i) (hexact : LinearMap.ker p = LinearMap.range i)
    (e : M₂ ≃ₗ[Λ] M₁ × M₃) :
    ∃ s : M₃ →ₗ[Λ] M₂, p ∘ₗ s = LinearMap.id := by
  have := finiteDimensional_hom (k := k) (Λ := Λ) (M := M₃) (M₁ := M₁)
  have := finiteDimensional_hom (k := k) (Λ := Λ) (M := M₃) (M₁ := M₂)
  have := finiteDimensional_hom (k := k) (Λ := Λ) (M := M₃) (M₁ := M₃)
  have hsurj := surjective_of_finrank_eq (k := k) (postcomp k (M := M₃) i)
    (postcomp k (M := M₃) p) (postcomp_injective i hi) (ker_postcomp i p hi hexact)
    (finrank_hom_of_equiv e)
  obtain ⟨s, hs⟩ := hsurj LinearMap.id
  exact ⟨s, hs⟩

end BensonRepresentations.SplitOfIsoMiddle

#print axioms BensonRepresentations.SplitOfIsoMiddle.surjective_of_finrank_eq
#print axioms BensonRepresentations.SplitOfIsoMiddle.ker_postcomp
#print axioms BensonRepresentations.SplitOfIsoMiddle.finrank_hom_of_equiv
#print axioms BensonRepresentations.SplitOfIsoMiddle.exists_section_of_equiv_prod
