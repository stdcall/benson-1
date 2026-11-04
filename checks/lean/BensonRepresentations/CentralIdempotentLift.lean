import Mathlib.RingTheory.Nakayama
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.RingTheory.TwoSidedIdeal.Basic
import Mathlib.Tactic.NoncommRing

/-!
# Central idempotents: Theorem 1.9.4 (iii) and Proposition 1.8.4

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), printed p. 18: the proof of Theorem 1.9.4 (iii) in the author's
corrected form ("Comments and corrections", 8 September 2010): "Lift each
`eᵢ` to an idempotent `fᵢ` in `Λ`.  Then `fᵢΛ(1 - fᵢ)` is contained in
`J(𝒪) fᵢΛ(1 - fᵢ)`.  Thus Nakayama's Lemma implies that `fᵢΛ(1 - fᵢ) = 0`.
By symmetry, we also have `(1 - fᵢ)Λfᵢ = 0`.  This implies that `fᵢ` is
central in `Λ`."  Also printed p. 16, the uniqueness half of the proof of
Proposition 1.8.4.

Notation.  `R` is the coefficient ring `𝒪`, `A` the `𝒪`-algebra `Λ`, finitely
generated as an `R`-module (`Module.Finite R A`; the book has `Λ` free of
finite rank).  `I` is an ideal of `R` contained in the Jacobson radical
(`I = J(𝒪) = (π)` in the book), and `N = I • ⊤ = πΛ` is the kernel of the
reduction `Λ → Λ̄`.  "`fᵢ` lifts the central idempotent `eᵢ` of `Λ̄`" enters
only through its consequences `fᵢ x (1 - fᵢ) ∈ N` and `(1 - fᵢ) x fᵢ ∈ N`
for all `x` (`eᵢ` is central), `fᵢ fⱼ ∈ N` for `i ≠ j` and
`1 - ∑ fᵢ ∈ N`; no quotient ring is constructed, and completeness of `𝒪`
(needed to lift the `eᵢ` at all, part (i)) is not used.

* `eq_zero_of_range_le`: an idempotent `R`-linear endomorphism `L` of `A` with
  image in `I • ⊤` is zero (Nakayama's lemma, mathlib's
  `Submodule.eq_bot_of_le_smul_of_le_jacobson_bot`, applied to its image).
* `peirce_eq_zero`: the author's step, `fΛ(1 - f) ⊆ πΛ` implies
  `fΛ(1 - f) = 0`; `central_of_lift`: `f` is central.
* `idempotent_mem_eq_zero`: `πΛ` contains no non-zero idempotent.
* `lift_orthogonal`, `lift_sum_eq_one`: the steps the proof leaves to the
  reader: the central lifts `fᵢ` are pairwise orthogonal and sum to `1`.
  (Primitivity of `fᵢ`: a decomposition `fᵢ = g + h` into orthogonal central
  idempotents reduces to one of `eᵢ`, and `ḡ, h̄ ≠ 0` by
  `idempotent_mem_eq_zero`; the reduction map is not formalized.)
* `central_lift_unique`: two central idempotents congruent modulo `πΛ` are
  equal (uniqueness of the lifts).
* `central_unique_of_nil`: the uniqueness argument of Proposition 1.8.4,
  "`f - ff'` is nilpotent and idempotent, hence zero", for central
  idempotents congruent modulo a two-sided nil ideal.

Not covered: the existence part of Proposition 1.8.4 (the induction
`fΛ(1 - f) = fJⁿ(1 - f)`), and the lifting of idempotents in part (i).
-/

namespace BensonRepresentations.CentralIdempotentLift

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A] [Module.Finite R A]
  (I : Ideal R) (hI : I ≤ Ideal.jacobson ⊥)

omit [Module.Finite R A] in
/-- `I • ⊤` (that is, `πΛ`) is closed under multiplication on either side. -/
theorem smul_top_mul_mem {x : A} (hx : x ∈ I • (⊤ : Submodule R A)) (a b : A) :
    a * x * b ∈ I • (⊤ : Submodule R A) := by
  let L : A →ₗ[R] A :=
    { toFun := fun y => a * y * b
      map_add' := fun y z => by noncomm_ring
      map_smul' := fun r y => by rw [RingHom.id_apply, mul_smul_comm, smul_mul_assoc] }
  have h : (I • (⊤ : Submodule R A)).map L ≤ I • (⊤ : Submodule R A) := by
    rw [Submodule.map_smul'']
    exact Submodule.smul_mono le_rfl le_top
  exact h ⟨x, hx, rfl⟩

include hI in
/-- Nakayama's lemma in the form used: an idempotent linear endomorphism of `Λ`
with image in `πΛ` vanishes. -/
theorem eq_zero_of_range_le (L : A →ₗ[R] A) (hL : ∀ x, L (L x) = L x)
    (hle : ∀ x, L x ∈ I • (⊤ : Submodule R A)) (x : A) : L x = 0 := by
  have hfg : (LinearMap.range L).FG := by
    rw [LinearMap.range_eq_map]
    exact (Module.Finite.fg_top).map L
  have hsub : LinearMap.range L ≤ I • LinearMap.range L := by
    rintro _ ⟨y, rfl⟩
    have h1 : L (L y) ∈ (I • (⊤ : Submodule R A)).map L := ⟨L y, hle y, rfl⟩
    rw [Submodule.map_smul'', ← LinearMap.range_eq_map, hL] at h1
    exact h1
  have hbot := Submodule.eq_bot_of_le_smul_of_le_jacobson_bot I _ hfg hsub hI
  have : L x ∈ LinearMap.range L := ⟨x, rfl⟩
  rw [hbot] at this
  exact (Submodule.mem_bot R).1 this

/-- The map `x ↦ a x b` as an `R`-linear map. -/
def sandwich (a b : A) : A →ₗ[R] A where
  toFun x := a * x * b
  map_add' x y := by noncomm_ring
  map_smul' r x := by rw [RingHom.id_apply, mul_smul_comm, smul_mul_assoc]

include hI in
/-- The author's step: if `f` is idempotent and `fΛ(1 - f) ⊆ πΛ`, then
`fΛ(1 - f) = 0`. -/
theorem peirce_eq_zero {f : A} (hf : f * f = f)
    (h : ∀ x, f * x * (1 - f) ∈ I • (⊤ : Submodule R A)) (x : A) :
    f * x * (1 - f) = 0 := by
  have hc : (1 - f) * (1 - f) = 1 - f := by
    calc (1 - f) * (1 - f) = 1 - f - f + f * f := by noncomm_ring
      _ = 1 - f := by rw [hf]; abel
  have hL : ∀ y, sandwich (R := R) f (1 - f) (sandwich (R := R) f (1 - f) y)
      = sandwich (R := R) f (1 - f) y := by
    intro y
    simp only [sandwich, LinearMap.coe_mk, AddHom.coe_mk]
    calc f * (f * y * (1 - f)) * (1 - f) = (f * f) * y * ((1 - f) * (1 - f)) := by
          noncomm_ring
      _ = f * y * (1 - f) := by rw [hf, hc]
  exact eq_zero_of_range_le I hI (sandwich f (1 - f)) hL (fun y => h y) x

/-- If `fΛ(1 - f) = 0` and `(1 - f)Λf = 0`, then `f` is central. -/
theorem central_of_peirce {f : A} (h₁ : ∀ x, f * x * (1 - f) = 0)
    (h₂ : ∀ x, (1 - f) * x * f = 0) (x : A) : f * x = x * f := by
  have a : f * x = f * x * f := by
    have := h₁ x
    calc f * x = f * x * f + f * x * (1 - f) := by noncomm_ring
      _ = f * x * f := by rw [this, add_zero]
  have b : x * f = f * x * f := by
    have := h₂ x
    calc x * f = f * x * f + (1 - f) * x * f := by noncomm_ring
      _ = f * x * f := by rw [this, add_zero]
  rw [a, b]

include hI in
/-- Theorem 1.9.4 (iii), the author's argument: an idempotent lift of a
central idempotent of `Λ̄ = Λ/πΛ` is central in `Λ`. -/
theorem central_of_lift {f : A} (hf : f * f = f)
    (h₁ : ∀ x, f * x * (1 - f) ∈ I • (⊤ : Submodule R A))
    (h₂ : ∀ x, (1 - f) * x * f ∈ I • (⊤ : Submodule R A)) (x : A) :
    f * x = x * f := by
  have hc : (1 - f) * (1 - f) = 1 - f := by
    calc (1 - f) * (1 - f) = 1 - f - f + f * f := by noncomm_ring
      _ = 1 - f := by rw [hf]; abel
  have h₂' : ∀ x, (1 - f) * x * (1 - (1 - f)) ∈ I • (⊤ : Submodule R A) := by
    intro x; rw [sub_sub_cancel]; exact h₂ x
  refine central_of_peirce (peirce_eq_zero I hI hf h₁) (fun y => ?_) x
  have := peirce_eq_zero I hI hc h₂' y
  rwa [sub_sub_cancel] at this

include hI in
/-- `πΛ` contains no non-zero idempotent. -/
theorem idempotent_mem_eq_zero {g : A} (hg : g * g = g)
    (hmem : g ∈ I • (⊤ : Submodule R A)) : g = 0 := by
  have hL : ∀ y, sandwich (R := R) g 1 (sandwich (R := R) g 1 y)
      = sandwich (R := R) g 1 y := by
    intro y
    simp only [sandwich, LinearMap.coe_mk, AddHom.coe_mk, mul_one]
    rw [← mul_assoc, hg]
  have h := eq_zero_of_range_le I hI (sandwich g 1) hL
    (fun y => by
      simp only [sandwich, LinearMap.coe_mk, AddHom.coe_mk]
      have := smul_top_mul_mem I hmem 1 y
      simpa using this) 1
  simpa [sandwich] using h

include hI in
/-- Two central idempotents congruent modulo `πΛ` are equal. -/
theorem central_lift_unique {f f' : A} (hf : f * f = f) (hf' : f' * f' = f')
    (hcf : ∀ x, f * x = x * f) (hcf' : ∀ x, f' * x = x * f')
    (hmem : f - f' ∈ I • (⊤ : Submodule R A)) : f = f' := by
  -- `f(1 - f') = f(f - f')` and `f'(1 - f) = -f'(f - f')` are idempotents in `πΛ`.
  have e1 : f * (1 - f') = f * (f - f') := by
    rw [mul_sub, mul_sub, hf, mul_one]
  have e2 : f' * (1 - f) = f' * (f - f') * (-1) := by
    rw [mul_sub, mul_sub, hf', mul_one]; noncomm_ring
  have i1 : f * (1 - f') * (f * (1 - f')) = f * (1 - f') := by
    calc f * (1 - f') * (f * (1 - f')) = f * ((1 - f') * f) * (1 - f') := by
          noncomm_ring
      _ = f * (f * (1 - f')) * (1 - f') := by rw [← hcf (1 - f')]
      _ = (f * f) * ((1 - f') * (1 - f')) := by noncomm_ring
      _ = f * (1 - f') := by
          rw [hf, show (1 - f') * (1 - f') = 1 - f' by
            calc (1 - f') * (1 - f') = 1 - f' - f' + f' * f' := by noncomm_ring
              _ = 1 - f' := by rw [hf']; abel]
  have i2 : f' * (1 - f) * (f' * (1 - f)) = f' * (1 - f) := by
    calc f' * (1 - f) * (f' * (1 - f)) = f' * ((1 - f) * f') * (1 - f) := by
          noncomm_ring
      _ = f' * (f' * (1 - f)) * (1 - f) := by rw [← hcf' (1 - f)]
      _ = (f' * f') * ((1 - f) * (1 - f)) := by noncomm_ring
      _ = f' * (1 - f) := by
          rw [hf', show (1 - f) * (1 - f) = 1 - f by
            calc (1 - f) * (1 - f) = 1 - f - f + f * f := by noncomm_ring
              _ = 1 - f := by rw [hf]; abel]
  have m1 : f * (1 - f') ∈ I • (⊤ : Submodule R A) := by
    rw [e1]; simpa using smul_top_mul_mem I hmem f 1
  have m2 : f' * (1 - f) ∈ I • (⊤ : Submodule R A) := by
    rw [e2]; exact smul_top_mul_mem I hmem f' (-1)
  have z1 := idempotent_mem_eq_zero I hI i1 m1
  have z2 := idempotent_mem_eq_zero I hI i2 m2
  have a : f = f * f' := by
    rw [mul_sub, mul_one, sub_eq_zero] at z1; exact z1
  have b : f' = f' * f := by
    rw [mul_sub, mul_one, sub_eq_zero] at z2; exact z2
  rw [a, hcf f', ← b]

include hI in
/-- The central lifts are pairwise orthogonal. -/
theorem lift_orthogonal {f f' : A} (hf : f * f = f) (hf' : f' * f' = f')
    (hcf : ∀ x, f * x = x * f) (hmem : f * f' ∈ I • (⊤ : Submodule R A)) :
    f * f' = 0 := by
  have hi : f * f' * (f * f') = f * f' := by
    calc f * f' * (f * f') = f * (f' * f) * f' := by noncomm_ring
      _ = f * (f * f') * f' := by rw [← hcf f']
      _ = (f * f) * (f' * f') := by noncomm_ring
      _ = f * f' := by rw [hf, hf']
  exact idempotent_mem_eq_zero I hI hi hmem

include hI in
/-- The central lifts sum to `1`: if `1 - ∑ fᵢ ∈ πΛ` and the `fᵢ` are
pairwise orthogonal idempotents, then `∑ fᵢ = 1`. -/
theorem lift_sum_eq_one {ι : Type*} (s : Finset ι) (f : ι → A)
    (hf : ∀ i ∈ s, f i * f i = f i)
    (horth : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → f i * f j = 0)
    (hmem : 1 - ∑ i ∈ s, f i ∈ I • (⊤ : Submodule R A)) :
    ∑ i ∈ s, f i = 1 := by
  set t := ∑ i ∈ s, f i with ht
  have tt : t * t = t := by
    rw [ht, Finset.sum_mul_sum]
    refine Finset.sum_congr rfl fun i hi => ?_
    rw [Finset.sum_eq_single i (fun j hj hji => horth i hi j hj (Ne.symm hji))
      (fun h => absurd hi h), hf i hi]
  have hc : (1 - t) * (1 - t) = 1 - t := by
    calc (1 - t) * (1 - t) = 1 - t - t + t * t := by noncomm_ring
      _ = 1 - t := by rw [tt]; abel
  have := idempotent_mem_eq_zero I hI hc hmem
  exact (sub_eq_zero.mp this).symm

omit [Module.Finite R A] in
/-- Proposition 1.8.4, uniqueness: two idempotents, one of them central (the
book has both central), congruent modulo a two-sided nil ideal (e.g. `I ⊆ J²(Λ)` for Artinian `Λ`) are equal. -/
theorem central_unique_of_nil (N : TwoSidedIdeal A) (hN : ∀ x ∈ N, IsNilpotent x)
    {f f' : A} (hf : f * f = f) (hf' : f' * f' = f')
    (hcf : ∀ x, f * x = x * f) (hmem : f - f' ∈ N) : f = f' := by
  have idem_nil : ∀ g : A, g * g = g → g ∈ N → g = 0 := by
    intro g hg hgN
    obtain ⟨m, hm⟩ := hN g hgN
    have : ∀ k, g ^ (k + 1) = g := by
      intro k; induction k with
      | zero => simp
      | succ k ih => rw [pow_succ, ih, hg]
    cases m with
    | zero =>
      rw [pow_zero] at hm
      calc g = 1 * g := (one_mul g).symm
        _ = 0 := by rw [hm, zero_mul]
    | succ m => rw [← this m, hm]
  have k1 : f - f * f' = f * (f - f') := by rw [mul_sub, hf]
  have k2 : f' - f' * f = f' * (f' - f) := by rw [mul_sub, hf']
  have c : f' * f = f * f' := (hcf f').symm
  have g1 : (f - f * f') * (f - f * f') = f - f * f' := by
    calc (f - f * f') * (f - f * f') = f * f - f * (f * f') - f * f' * f +
          f * f' * (f * f') := by noncomm_ring
      _ = f - f * f' := by
          rw [← mul_assoc f f f', hf, mul_assoc f f' f, c, ← mul_assoc, hf,
            mul_assoc, ← mul_assoc f' f f', c, mul_assoc, hf', ← mul_assoc, hf]
          abel
  have g2 : (f' - f' * f) * (f' - f' * f) = f' - f' * f := by
    have c' : f * f' = f' * f := c.symm
    calc (f' - f' * f) * (f' - f' * f) = f' * f' - f' * (f' * f) - f' * f * f' +
          f' * f * (f' * f) := by noncomm_ring
      _ = f' - f' * f := by
          rw [← mul_assoc f' f' f, hf', mul_assoc f' f f', c', ← mul_assoc, hf',
            mul_assoc, ← mul_assoc f f' f, c', mul_assoc, hf, ← mul_assoc, hf']
          abel
  have z1 := idem_nil _ g1 (by rw [k1]; exact N.mul_mem_left _ _ hmem)
  have z2 := idem_nil _ g2 (by
    rw [k2, show f' - f = -(f - f') by abel, mul_neg]
    exact N.neg_mem (N.mul_mem_left _ _ hmem))
  rw [sub_eq_zero] at z1 z2
  calc f = f * f' := z1
    _ = f' * f := c.symm
    _ = f' := z2.symm

end BensonRepresentations.CentralIdempotentLift

#print axioms BensonRepresentations.CentralIdempotentLift.smul_top_mul_mem
#print axioms BensonRepresentations.CentralIdempotentLift.eq_zero_of_range_le
#print axioms BensonRepresentations.CentralIdempotentLift.peirce_eq_zero
#print axioms BensonRepresentations.CentralIdempotentLift.central_of_peirce
#print axioms BensonRepresentations.CentralIdempotentLift.central_of_lift
#print axioms BensonRepresentations.CentralIdempotentLift.idempotent_mem_eq_zero
#print axioms BensonRepresentations.CentralIdempotentLift.central_lift_unique
#print axioms BensonRepresentations.CentralIdempotentLift.lift_orthogonal
#print axioms BensonRepresentations.CentralIdempotentLift.lift_sum_eq_one
#print axioms BensonRepresentations.CentralIdempotentLift.central_unique_of_nil
