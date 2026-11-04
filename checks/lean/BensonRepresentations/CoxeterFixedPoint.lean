import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# A Coxeter transformation has no non-zero fixed point

Book: D. J. Benson, *Representations and Cohomology I*, second edition (1998),
Section 4.6, Lemma 4.6.9 and its proof, p. 124 of the printed book.

Notation.  The vertices `x_1, …, x_n` of `T` form a type `ι`; vectors of
`ℝ^T` are functions `ι → K` (`v = ∑ r_i v_i` is `fun i => r i`), `K` a
linearly ordered field.  A *reflection-type map* at `i` is
`refl φ i u = u - φ i u • v_i`: it changes only the coordinate `i`, by
`φ i u` (`Function.update`).  `prodRefl φ [i₁, …, i_k] = w_{i₁} ∘ ⋯ ∘ w_{i_k}`.

* `prodRefl_apply_of_not_mem`: the product of the `w_j`, `j ∈ l`, does not
  change the coordinates outside `l`.
* `fixed_of_prod_fixed`: the argument of the proof of (i).  If the indices of
  `l` are distinct and `w_{i₁} ⋯ w_{i_k} (v) = v`, then every `w_{i_j}` fixes
  `v` ("the multiple of `v_1` in `w_1(v)` is still `r_1`, and hence
  `w_1(v) = v`", and so on).  Only the shape of the maps is used: `φ` is
  arbitrary.
* `coxeter_no_fixed_point`: Lemma 4.6.9 (i).  For the reflections
  `w_i(u) = u - 2(u, v_i)/(v_i, v_i) v_i` of a positive definite form
  `(u, w) = ∑_{x,y} u_x S_xy w_y` (the symmetrised Cartan matrix of a finite
  Dynkin diagram, Proposition 4.6.3 (i)) and a list containing every vertex
  once, the Coxeter transformation fixes only `0`.
* `sum_iterate_fixed`, `exists_not_positive`: Lemma 4.6.9 (ii).  If
  `c^h(v) = v` (`h ≥ 1`; in the book `h` is the order of `c`) then
  `∑_{i<h} c^i(v)` is fixed by `c`; so if `c` is additive with no non-zero
  fixed point, some `c^m(v)`, `m < h`, is not positive (positive: all
  coordinates `≥ 0` and not zero, Definition 4.6.7).
* `coxeter_exists_not_positive`: the two combined for the Coxeter
  transformation of a positive definite form.

Not covered: that the symmetrised Cartan matrix of a finite Dynkin diagram is
positive definite and that `c` has finite order (Propositions 4.6.3, 4.6.4;
checked in `checks/sage/chapter-4a.py` for every finite Dynkin diagram with
at most 8 vertices, where also `det(c - 1) ≠ 0` and `∑ c^i = 0` are
computed for the Coxeter transformations).
-/

namespace BensonRepresentations.CoxeterFixedPoint

open Finset

variable {ι K : Type*} [DecidableEq ι]

/-- `w_i(u) = u - φ_i(u) v_i`: only the coordinate `i` changes. -/
def refl [Ring K] (φ : ι → (ι → K) → K) (i : ι) (u : ι → K) : ι → K :=
  Function.update u i (u i - φ i u)

/-- `w_{i₁} ∘ ⋯ ∘ w_{i_k}`, the last one applied first. -/
def prodRefl [Ring K] (φ : ι → (ι → K) → K) : List ι → (ι → K) → (ι → K)
  | [] => id
  | i :: l => fun u => refl φ i (prodRefl φ l u)

theorem prodRefl_apply_of_not_mem [Ring K] (φ : ι → (ι → K) → K) (l : List ι)
    (u : ι → K) {j : ι} (hj : j ∉ l) : prodRefl φ l u j = u j := by
  induction l with
  | nil => rfl
  | cons i l ih =>
    have hji : j ≠ i := fun h => hj (h ▸ List.mem_cons_self)
    simp only [prodRefl, refl, Function.update_of_ne hji]
    exact ih fun h => hj (List.mem_cons_of_mem _ h)

theorem refl_eq_self_iff [Ring K] (φ : ι → (ι → K) → K) (i : ι) (u : ι → K) :
    refl φ i u = u ↔ φ i u = 0 := by
  constructor
  · intro h
    have := congr_fun h i
    simp only [refl, Function.update_self] at this
    exact sub_eq_self.mp this
  · intro h
    simp [refl, h]

/-- The proof of Lemma 4.6.9 (i): a product of reflection-type maps at
distinct indices fixes `v` only if each factor does. -/
theorem fixed_of_prod_fixed [Ring K] (φ : ι → (ι → K) → K) (l : List ι)
    (hl : l.Nodup) (v : ι → K) (hv : prodRefl φ l v = v) :
    ∀ i ∈ l, refl φ i v = v := by
  induction l with
  | nil => simp
  | cons i l ih =>
    rw [List.nodup_cons] at hl
    set u := prodRefl φ l v with hu
    have hui : u i = v i := prodRefl_apply_of_not_mem φ l v hl.1
    have hv' : refl φ i u = v := hv
    have hφ : φ i u = 0 := by
      have := congr_fun hv' i
      simp only [refl, Function.update_self] at this
      rw [hui] at this
      exact sub_eq_self.mp this
    have huv : u = v := by
      rw [← hv', (refl_eq_self_iff φ i u).2 hφ]
    have hrest := ih hl.2 huv
    intro j hj
    rcases List.mem_cons.1 hj with rfl | hj
    · rw [← huv]
      exact (refl_eq_self_iff φ j u).2 hφ
    · exact hrest j hj

variable [Fintype ι] [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The bilinear form `(u, w) = ∑_{x,y} u_x S_xy w_y`. -/
def form (S : ι → ι → K) (u w : ι → K) : K := ∑ x, ∑ y, u x * S x y * w y

/-- `φ_i(u) = 2 (u, v_i) / (v_i, v_i)`, so `refl` is the reflection `w_i` of
Definition 4.6.1. -/
def φS (S : ι → ι → K) (i : ι) (u : ι → K) : K :=
  2 * (∑ x, u x * S x i) / S i i

theorem form_single (S : ι → ι → K) (u : ι → K) (i : ι) :
    form S u (Pi.single i 1) = ∑ x, u x * S x i := by
  unfold form
  refine sum_congr rfl fun x _ => ?_
  rw [sum_eq_single i]
  · simp
  · intro y _ hy; simp [hy]
  · simp

theorem diag_pos (S : ι → ι → K)
    (hpos : ∀ u : ι → K, u ≠ 0 → 0 < form S u u) (i : ι) : 0 < S i i := by
  have h := hpos (Pi.single i 1) (by
    intro h0
    have := congr_fun h0 i
    simp at this)
  rw [form_single, sum_eq_single i (fun y _ hy => by simp [hy])
    (by simp)] at h
  simpa using h

/-- Lemma 4.6.9 (i). -/
theorem coxeter_no_fixed_point (S : ι → ι → K)
    (hpos : ∀ u : ι → K, u ≠ 0 → 0 < form S u u) (l : List ι)
    (hl : l.Nodup) (hall : ∀ i, i ∈ l) (v : ι → K)
    (hv : prodRefl (φS S) l v = v) : v = 0 := by
  have hfix := fixed_of_prod_fixed (φS S) l hl v hv
  have hperp : ∀ i, ∑ x, v x * S x i = 0 := by
    intro i
    have h := (refl_eq_self_iff (φS S) i v).1 (hfix i (hall i))
    have hd := (diag_pos S hpos i).ne'
    unfold φS at h
    field_simp at h
    linarith
  by_contra hne
  have h := hpos v hne
  have : form S v v = 0 := by
    unfold form
    rw [sum_comm]
    refine sum_eq_zero fun y _ => ?_
    rw [← sum_mul, hperp y, zero_mul]
  linarith

omit [DecidableEq ι] [Fintype ι] in
/-- If `c^h(v) = v`, then `∑_{i<h} c^i(v)` is fixed by the additive map `c`. -/
theorem sum_iterate_fixed (c : (ι → K) → (ι → K))
    (hadd : ∀ u w, c (u + w) = c u + c w) (h : ℕ) (v : ι → K)
    (hv : c^[h] v = v) :
    c (∑ i ∈ range h, c^[i] v) = ∑ i ∈ range h, c^[i] v := by
  have hzero : c 0 = 0 := by
    have := hadd 0 0
    simp at this
    exact this
  have hsum : ∀ (s : Finset ℕ) (f : ℕ → ι → K),
      c (∑ i ∈ s, f i) = ∑ i ∈ s, c (f i) := by
    intro s f
    induction s using Finset.induction_on with
    | empty => simpa using hzero
    | insert a s ha ih => rw [sum_insert ha, sum_insert ha, hadd, ih]
  rw [hsum]
  have hshift : ∀ i, c (c^[i] v) = c^[i + 1] v := fun i =>
    (Function.iterate_succ_apply' c i v).symm
  simp_rw [hshift]
  rcases Nat.eq_zero_or_pos h with rfl | hh
  · simp
  · obtain ⟨k, rfl⟩ : ∃ k, h = k + 1 := ⟨h - 1, by omega⟩
    rw [sum_range_succ, sum_range_succ' (fun i => c^[i] v), hv]
    simp

/-- Positive vectors (Definition 4.6.7): non-zero with non-negative
coordinates. -/
def Positive (w : ι → K) : Prop := (∀ x, 0 ≤ w x) ∧ w ≠ 0

omit [DecidableEq ι] in
/-- Lemma 4.6.9 (ii) for an additive `c` without non-zero fixed points. -/
theorem exists_not_positive (c : (ι → K) → (ι → K))
    (hadd : ∀ u w, c (u + w) = c u + c w)
    (hfix : ∀ u, c u = u → u = 0) (h : ℕ) (hh : 0 < h) (v : ι → K)
    (hv : c^[h] v = v) : ∃ m < h, ¬ Positive (c^[m] v) := by
  by_contra hcon
  have hpos : ∀ m < h, Positive (c^[m] v) := fun m hm =>
    by_contra fun hm' => hcon ⟨m, hm, hm'⟩
  set s := ∑ i ∈ range h, c^[i] v
  have hs : s = 0 := hfix s (sum_iterate_fixed c hadd h v hv)
  obtain ⟨hnn, hne⟩ := hpos 0 hh
  simp only [Function.iterate_zero, id] at hnn hne
  obtain ⟨x, hx⟩ : ∃ x, v x ≠ 0 := by
    by_contra hall
    exact hne (funext fun y => by_contra fun hy => hall ⟨y, hy⟩)
  have hvx : 0 < v x := lt_of_le_of_ne (hnn x) (Ne.symm hx)
  have hsx : s x = ∑ i ∈ range h, (c^[i] v) x := by
    simp [s, Finset.sum_apply]
  have hge : v x ≤ s x := by
    rw [hsx]
    have h0 : (0 : ℕ) ∈ range h := mem_range.2 hh
    have := single_le_sum (f := fun i => (c^[i] v) x)
      (fun i hi => (hpos i (mem_range.1 hi)).1 x) h0
    simpa using this
  have : s x = 0 := by rw [hs]; rfl
  linarith

theorem refl_add (S : ι → ι → K) (i : ι) (u w : ι → K) :
    refl (φS S) i (u + w) = refl (φS S) i u + refl (φS S) i w := by
  funext j
  by_cases hj : j = i
  · subst hj
    simp only [refl, Function.update_self, Pi.add_apply, φS, add_mul,
      sum_add_distrib]
    ring
  · simp [refl, Function.update_of_ne hj]

theorem prodRefl_add (S : ι → ι → K) (l : List ι) (u w : ι → K) :
    prodRefl (φS S) l (u + w) = prodRefl (φS S) l u + prodRefl (φS S) l w := by
  induction l with
  | nil => rfl
  | cons i l ih => simp only [prodRefl]; rw [ih, refl_add]

/-- Lemma 4.6.9 (ii) for the Coxeter transformation of a positive definite
form: if `c^h(v) = v` with `h ≥ 1`, some `c^m(v)`, `m < h`, is not
positive. -/
theorem coxeter_exists_not_positive (S : ι → ι → K)
    (hpos : ∀ u : ι → K, u ≠ 0 → 0 < form S u u) (l : List ι)
    (hl : l.Nodup) (hall : ∀ i, i ∈ l) (h : ℕ) (hh : 0 < h) (v : ι → K)
    (hv : (prodRefl (φS S) l)^[h] v = v) :
    ∃ m < h, ¬ Positive ((prodRefl (φS S) l)^[m] v) :=
  exists_not_positive (prodRefl (φS S) l) (prodRefl_add S l)
    (fun u hu => coxeter_no_fixed_point S hpos l hl hall u hu) h hh v hv

end BensonRepresentations.CoxeterFixedPoint

#print axioms BensonRepresentations.CoxeterFixedPoint.prodRefl_apply_of_not_mem
#print axioms BensonRepresentations.CoxeterFixedPoint.refl_eq_self_iff
#print axioms BensonRepresentations.CoxeterFixedPoint.fixed_of_prod_fixed
#print axioms BensonRepresentations.CoxeterFixedPoint.coxeter_no_fixed_point
#print axioms BensonRepresentations.CoxeterFixedPoint.sum_iterate_fixed
#print axioms BensonRepresentations.CoxeterFixedPoint.exists_not_positive
#print axioms BensonRepresentations.CoxeterFixedPoint.coxeter_exists_not_positive
