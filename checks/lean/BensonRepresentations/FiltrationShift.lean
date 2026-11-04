import Mathlib.Algebra.Module.Submodule.Ker
import Mathlib.Algebra.Module.Submodule.Range
import Mathlib.Algebra.Module.Submodule.Map
import Mathlib.LinearAlgebra.Quotient.Basic

/-!
# Section 4.10, Example: the functors `F_ij` for `k[T]/(Tⁿ)`

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), printed pp. 134–135, the Example after Proposition 4.10.6 (the
functorial filtration method for the group algebra `Λ = k[T]/(Tⁿ)` of a
cyclic `p`-group).  For a `Λ`-module `M` the book sets
`F_ij(M) = Ker(Tⁱ) ∩ (Im(Tʲ) + Ker(Tⁱ⁻¹))` and states:

* "Since `Ker(Tⁱ) ⊇ Im(Tʲ)` if `i ≥ n - j`, we have
  `F_(i+1, n-i)(M) = Ker(Tⁱ) = F_(i,0)(M)`";
* "if `n - j ≥ i > 0`, the action of `T` induces an isomorphism from
  `F_(i,j-1)/F_(i,j)` to `F_(i-1,j)/F_(i-1,j+1)`".

The second statement needs `i > 1`: for `i = 1` the target
`F_(0,j)/F_(0,j+1)` is zero (`Ker(T⁰) = 0`), while `F_(1,j-1)/F_(1,j)` is not
zero on the uniserial module of dimension `j`, `1 ≤ j < n` (checked in
`checks/sage/chapter-4b.py`).  Here the corrected statement is proved for
`i ≥ 2`, `j ≥ 1`, without the bound `n - j ≥ i` and for any module.

Notation.  `V` is the module `M` over a ring `R` (the book: a vector space over
`k`), `T : V → V` the action of `T` (any `R`-linear endomorphism), and
`F T i j` the submodule `F_ij(M)`.  The book's `i ≥ 2` and `j ≥ 1` are written
`i + 2` and `j + 1`, so that `F T (i + 2) j / F T (i + 2) (j + 1)` is the
source and `F T (i + 1) (j + 1) / F T (i + 1) (j + 2)` the target.

* `F_zero`: `F_(i,0) = Ker(Tⁱ)`.
* `range_le_ker`, `F_top`: if `Tⁿ = 0` and `i + j ≥ n` then
  `Im(Tʲ) ≤ Ker(Tⁱ)`, and `F_(i+1, n-i) = Ker(Tⁱ)` for `i ≤ n`.
* `map_le`: `T` maps `F_(i,j-1)` into `F_(i-1,j)` (for every `j`, so also
  `F_(i,j)` into `F_(i-1,j+1)`).
* `le_map_sup`: `T(F_(i,j-1)) + F_(i-1,j+1) = F_(i-1,j)`, so the induced map
  is surjective.
* `inf_comap_le`: `F_(i,j-1) ∩ T⁻¹(F_(i-1,j+1)) = F_(i,j)`, so it is
  injective.
* `shiftEquiv`: the induced isomorphism of the quotients.

Not covered: that these subquotients are the functors `Sᵢ` of the book and
that the `Mᵢ` form a complete list of indecomposables (checked for
`n ≤ 6` over `𝔽₂`, `𝔽₃` in `checks/sage/chapter-4b.py`).
-/

namespace BensonRepresentations.FiltrationShift

variable {R V : Type*} [Ring R] [AddCommGroup V] [Module R V]

open Submodule

/-- `F_ij = Ker(Tⁱ) ∩ (Im(Tʲ) + Ker(Tⁱ⁻¹))`. -/
def F (T : Module.End R V) (i j : ℕ) : Submodule R V :=
  LinearMap.ker (T ^ i) ⊓ (LinearMap.range (T ^ j) ⊔ LinearMap.ker (T ^ (i - 1)))

lemma pow_succ_apply (T : Module.End R V) (n : ℕ) (x : V) :
    (T ^ (n + 1)) x = (T ^ n) (T x) := by
  rw [pow_succ, Module.End.mul_apply]

lemma pow_succ_apply' (T : Module.End R V) (n : ℕ) (x : V) :
    (T ^ (n + 1)) x = T ((T ^ n) x) := by
  rw [pow_succ', Module.End.mul_apply]

/-- `F_(i,0) = Ker(Tⁱ)`. -/
theorem F_zero (T : Module.End R V) (i : ℕ) : F T i 0 = LinearMap.ker (T ^ i) := by
  apply le_antisymm inf_le_left
  intro x hx
  exact mem_inf.mpr ⟨hx, mem_sup_left ⟨x, by simp⟩⟩

/-- If `Tⁿ = 0` and `i + j ≥ n` then `Im(Tʲ) ≤ Ker(Tⁱ)`. -/
theorem range_le_ker (T : Module.End R V) {n i j : ℕ} (hT : T ^ n = 0)
    (hij : n ≤ i + j) : LinearMap.range (T ^ j) ≤ LinearMap.ker (T ^ i) := by
  rintro _ ⟨m, rfl⟩
  rw [LinearMap.mem_ker, ← Module.End.mul_apply, ← pow_add]
  obtain ⟨c, hc⟩ := Nat.exists_eq_add_of_le hij
  rw [hc, pow_add, hT, zero_mul, LinearMap.zero_apply]

/-- The first statement of the Example: `F_(i+1, n-i) = Ker(Tⁱ)` when
`Tⁿ = 0` and `i ≤ n`. -/
theorem F_top (T : Module.End R V) {n i : ℕ} (hT : T ^ n = 0) (hi : i ≤ n) :
    F T (i + 1) (n - i) = LinearMap.ker (T ^ i) := by
  have h1 : LinearMap.range (T ^ (n - i)) ⊔ LinearMap.ker (T ^ i) =
      LinearMap.ker (T ^ i) :=
    sup_eq_right.mpr (range_le_ker T hT (by omega))
  have h2 : LinearMap.ker (T ^ i) ≤ LinearMap.ker (T ^ (i + 1)) := by
    intro x hx
    rw [LinearMap.mem_ker] at hx ⊢
    rw [pow_succ_apply', hx, map_zero]
  simp only [F, Nat.add_sub_cancel, h1]
  exact inf_eq_right.mpr h2

/-- `T` maps `F_(i,j-1)` into `F_(i-1,j)` (book indices; here `i + 2` and
`j`). -/
theorem map_le (T : Module.End R V) (i j : ℕ) :
    (F T (i + 2) j).map T ≤ F T (i + 1) (j + 1) := by
  rintro _ ⟨x, hx, rfl⟩
  obtain ⟨hx1, hx2⟩ := mem_inf.mp hx
  rw [show i + 2 - 1 = i + 1 by omega] at hx2
  rw [LinearMap.mem_ker] at hx1
  rw [F, Nat.add_sub_cancel, mem_inf]
  obtain ⟨y, ⟨m, rfl⟩, z, hz, rfl⟩ := mem_sup.mp hx2
  rw [LinearMap.mem_ker] at hz
  refine ⟨?_, ?_⟩
  · rw [LinearMap.mem_ker, ← pow_succ_apply]
    exact hx1
  · refine mem_sup.mpr ⟨(T ^ (j + 1)) m, ⟨m, rfl⟩, T z, ?_, ?_⟩
    · rw [LinearMap.mem_ker, ← pow_succ_apply]
      exact hz
    · rw [map_add, pow_succ_apply']

/-- Surjectivity of the induced map: `F_(i-1,j) ≤ T(F_(i,j-1)) + F_(i-1,j+1)`
(with the reverse inclusion from `map_le`). -/
theorem le_map_sup (T : Module.End R V) (i j : ℕ) :
    F T (i + 1) (j + 1) ≤ (F T (i + 2) j).map T ⊔ F T (i + 1) (j + 2) := by
  intro y hy
  obtain ⟨hy1, hy2⟩ := mem_inf.mp hy
  simp only [Nat.add_sub_cancel] at hy2
  rw [LinearMap.mem_ker] at hy1
  obtain ⟨_, ⟨m, rfl⟩, k, hk, rfl⟩ := mem_sup.mp hy2
  rw [LinearMap.mem_ker] at hk
  -- x = Tʲ m lies in F_(i,j-1), and y - T x = k lies in F_(i-1,j+1)
  have hTk : (T ^ (i + 1)) k = 0 := by rw [pow_succ_apply', hk, map_zero]
  have hm : (T ^ (i + 2)) ((T ^ j) m) = 0 := by
    have : (T ^ (i + 1)) ((T ^ (j + 1)) m) = 0 := by
      rw [map_add, hTk, add_zero] at hy1; exact hy1
    rw [pow_succ_apply, ← pow_succ_apply']; exact this
  refine mem_sup.mpr ⟨T ((T ^ j) m), ⟨(T ^ j) m, mem_inf.mpr ⟨?_, ?_⟩, rfl⟩, k,
    mem_inf.mpr ⟨?_, ?_⟩, ?_⟩
  · rw [LinearMap.mem_ker]; exact hm
  · exact mem_sup_left ⟨m, rfl⟩
  · rw [LinearMap.mem_ker]; exact hTk
  · simp only [Nat.add_sub_cancel]
    exact mem_sup_right (by rw [LinearMap.mem_ker]; exact hk)
  · rw [← pow_succ_apply']

/-- Injectivity of the induced map: an element of `F_(i,j-1)` whose image
lies in `F_(i-1,j+1)` lies in `F_(i,j)`. -/
theorem inf_comap_le (T : Module.End R V) (i j : ℕ) :
    F T (i + 2) j ⊓ (F T (i + 1) (j + 2)).comap T ≤ F T (i + 2) (j + 1) := by
  intro x hx
  obtain ⟨hx12, hx3⟩ := mem_inf.mp hx
  obtain ⟨hx1, -⟩ := mem_inf.mp hx12
  rw [mem_comap] at hx3
  obtain ⟨-, hx3⟩ := mem_inf.mp hx3
  simp only [Nat.add_sub_cancel] at hx3
  refine mem_inf.mpr ⟨hx1, ?_⟩
  rw [show i + 2 - 1 = i + 1 by omega]
  obtain ⟨_, ⟨m, rfl⟩, k, hk, hsum⟩ := mem_sup.mp hx3
  rw [LinearMap.mem_ker] at hk
  -- T (x - Tʲ⁺¹ m) = k, so x - Tʲ⁺¹ m ∈ Ker(Tⁱ⁺¹)
  have hd : (T ^ (i + 1)) (x - (T ^ (j + 1)) m) = 0 := by
    rw [pow_succ_apply, map_sub, ← pow_succ_apply', ← hsum, add_sub_cancel_left, hk]
  refine mem_sup.mpr ⟨(T ^ (j + 1)) m, ⟨m, rfl⟩, x - (T ^ (j + 1)) m, ?_, ?_⟩
  · rw [LinearMap.mem_ker]; exact hd
  · rw [add_comm, sub_add_cancel]

/-- The submodule `P'` of `P`, as a submodule of `P`. -/
abbrev rel (P P' : Submodule R V) : Submodule R P := P'.comap P.subtype

/-- `T` restricted to `F_(i,j-1) → F_(i-1,j)`. -/
def restrictT (T : Module.End R V) (i j : ℕ) :
    F T (i + 2) j →ₗ[R] F T (i + 1) (j + 1) :=
  (T.domRestrict (F T (i + 2) j)).codRestrict (F T (i + 1) (j + 1))
    (fun x => map_le T i j ⟨x.1, x.2, rfl⟩)

lemma le_F_succ (T : Module.End R V) (i j : ℕ) : F T (i + 1) (j + 1) ≤ F T (i + 1) j := by
  intro x hx
  obtain ⟨hx1, hx2⟩ := mem_inf.mp hx
  refine mem_inf.mpr ⟨hx1, ?_⟩
  obtain ⟨_, ⟨m, rfl⟩, k, hk, rfl⟩ := mem_sup.mp hx2
  refine mem_sup.mpr ⟨(T ^ j) (T m), ⟨T m, rfl⟩, k, hk, ?_⟩
  rw [← pow_succ_apply]

/-- The induced map `F_(i,j-1)/F_(i,j) → F_(i-1,j)/F_(i-1,j+1)`. -/
def shiftMap (T : Module.End R V) (i j : ℕ) :
    (F T (i + 2) j ⧸ rel (F T (i + 2) j) (F T (i + 2) (j + 1))) →ₗ[R]
      (F T (i + 1) (j + 1) ⧸ rel (F T (i + 1) (j + 1)) (F T (i + 1) (j + 2))) :=
  Submodule.mapQ _ _ (restrictT T i j) (by
    rintro ⟨x, hx⟩ hx'
    simp only [mem_comap, Submodule.coe_subtype] at hx' ⊢
    exact map_le T i (j + 1) ⟨x, hx', rfl⟩)

theorem shiftMap_bijective (T : Module.End R V) (i j : ℕ) :
    Function.Bijective (shiftMap T i j) := by
  constructor
  · rw [← LinearMap.ker_eq_bot, Submodule.eq_bot_iff]
    intro q hq
    induction q using Submodule.Quotient.induction_on with
    | H x =>
      rw [LinearMap.mem_ker, shiftMap, Submodule.mapQ_apply,
        Submodule.Quotient.mk_eq_zero] at hq
      rw [Submodule.Quotient.mk_eq_zero]
      simp only [mem_comap, Submodule.coe_subtype, restrictT,
        LinearMap.codRestrict_apply, LinearMap.domRestrict_apply] at hq ⊢
      exact inf_comap_le T i j ⟨x.2, hq⟩
  · intro q
    induction q using Submodule.Quotient.induction_on with
    | H y =>
      obtain ⟨_, ⟨x, hx, rfl⟩, k, hk, hsum⟩ := mem_sup.mp (le_map_sup T i j y.2)
      refine ⟨Submodule.Quotient.mk ⟨x, hx⟩, ?_⟩
      rw [shiftMap, Submodule.mapQ_apply, Submodule.Quotient.eq]
      simp only [mem_comap, Submodule.coe_subtype, AddSubgroupClass.coe_sub,
        restrictT, LinearMap.codRestrict_apply, LinearMap.domRestrict_apply]
      have : T x - y.1 = -k := by rw [← hsum, sub_add_cancel_left]
      rw [this]
      exact neg_mem hk

/-- The isomorphism `F_(i,j-1)/F_(i,j) ≅ F_(i-1,j)/F_(i-1,j+1)` induced by `T`
(book: `i ≥ 2`, `j ≥ 1`). -/
noncomputable def shiftEquiv (T : Module.End R V) (i j : ℕ) :
    (F T (i + 2) j ⧸ rel (F T (i + 2) j) (F T (i + 2) (j + 1))) ≃ₗ[R]
      (F T (i + 1) (j + 1) ⧸ rel (F T (i + 1) (j + 1)) (F T (i + 1) (j + 2))) :=
  LinearEquiv.ofBijective (shiftMap T i j) (shiftMap_bijective T i j)

end BensonRepresentations.FiltrationShift

#print axioms BensonRepresentations.FiltrationShift.F_zero
#print axioms BensonRepresentations.FiltrationShift.range_le_ker
#print axioms BensonRepresentations.FiltrationShift.F_top
#print axioms BensonRepresentations.FiltrationShift.map_le
#print axioms BensonRepresentations.FiltrationShift.le_map_sup
#print axioms BensonRepresentations.FiltrationShift.inf_comap_le
#print axioms BensonRepresentations.FiltrationShift.shiftMap_bijective
#print axioms BensonRepresentations.FiltrationShift.shiftEquiv
