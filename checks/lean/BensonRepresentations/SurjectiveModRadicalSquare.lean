import Mathlib.Algebra.Algebra.Operations
import Mathlib.Algebra.Algebra.Subalgebra.Pointwise
import Mathlib.Algebra.Algebra.Subalgebra.Lattice
import Mathlib.Order.ModularLattice

/-!
# Proposition 1.2.8: a subring that fills `Λ` modulo `J²` is `Λ`

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), printed p. 5, Proposition 1.2.8 and its proof: "We show that
`Λ' + Jⁿ(Λ) = Λ' + Jⁿ⁺¹(Λ)` for `n ≥ 2`, so that by induction and part (i)
of the previous theorem we deduce that `Λ' = Λ`."

Notation.  `A` is the ring `Λ`, viewed as an algebra over a commutative ring
`R` (for `R = ℤ`, subalgebras are exactly the subrings, which is the book's
case); `S` is the subring `Λ'`, `T` its underlying `R`-submodule, and `J` the
radical `J(Λ)` as an `R`-submodule of `A`, with powers taken in the semiring
of submodules (`Jⁿ` is spanned by products of `n` elements of `J`).

Hypotheses.  The book's `Λ` is Artinian and `J = J(Λ)`; the proof uses only
that `J` is a right ideal (`J * ⊤ ≤ J`; `J(Λ)` is two-sided) and that `J` is
nilpotent (Theorem 1.2.7 (i)), and these are the hypotheses here.

* `fill_step`: the inductive step `Λ' + Jⁿ = Λ ⇒ Λ' + Jⁿ⁺¹ = Λ` for `n ≥ 2`,
  by the book's argument: `x ∈ Jⁿ⁻¹`, `y ∈ J` are written
  `x = x' + (x - x')`, `y = y' + (y - y')` with `x' ∈ Jⁿ⁻¹ ∩ Λ'`,
  `x - x' ∈ Jⁿ`, `y' ∈ J ∩ Λ'`, `y - y' ∈ J²` (here the modular law
  `Jⁿ⁻¹ = (Jⁿ⁻¹ ∩ Λ') + Jⁿ`), and the four products land in `Λ' + Jⁿ⁺¹`.
* `eq_top_of_sup_sq`: Proposition 1.2.8.

Not covered: that `J(Λ)` is nilpotent for Artinian `Λ` (Theorem 1.2.7 (i)) is a
hypothesis.  The necessity of the square (with `J` in place of `J²` the
statement fails, e.g. for `𝔽₃S₃`) is checked in `checks/sage/chapter-1.py`.
-/

namespace BensonRepresentations.SurjectiveModRadicalSquare

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

open Submodule

/-- `Jᵏ⁺¹ * ⊤ ≤ Jᵏ⁺¹` for a right ideal `J`. -/
theorem pow_succ_mul_top_le (J : Submodule R A) (hJ : J * ⊤ ≤ J) (k : ℕ) :
    J ^ (k + 1) * ⊤ ≤ J ^ (k + 1) := by
  rw [pow_succ, mul_assoc]
  exact mul_le_mul_right hJ _

/-- The powers decrease from the first one on: `Jᵏ⁺² ≤ Jᵏ⁺¹`. -/
theorem pow_succ_succ_le (J : Submodule R A) (hJ : J * ⊤ ≤ J) (k : ℕ) :
    J ^ (k + 2) ≤ J ^ (k + 1) := by
  calc J ^ (k + 2) = J ^ (k + 1) * J := pow_succ J (k + 1)
    _ ≤ J ^ (k + 1) * ⊤ := mul_le_mul_right le_top _
    _ ≤ J ^ (k + 1) := pow_succ_mul_top_le J hJ k

/-- The inductive step of the proof: `Λ' + Jⁿ = Λ` implies
`Λ' + Jⁿ⁺¹ = Λ` for `n ≥ 2` (here `n = k + 2`). -/
theorem fill_step (S : Subalgebra R A) (J : Submodule R A) (hJ : J * ⊤ ≤ J)
    (h2 : Subalgebra.toSubmodule S ⊔ J ^ 2 = ⊤) (k : ℕ)
    (hn : Subalgebra.toSubmodule S ⊔ J ^ (k + 2) = ⊤) :
    Subalgebra.toSubmodule S ⊔ J ^ (k + 3) = ⊤ := by
  set T := Subalgebra.toSubmodule S
  have hTT : T * T ≤ T := by
    have := Subalgebra.mul_toSubmodule_le S S
    rwa [sup_idem] at this
  -- the modular law: `Jᵏ⁺¹ = (Jᵏ⁺¹ ⊓ T) ⊔ Jᵏ⁺²` and `J = (J ⊓ T) ⊔ J²`
  have hx : J ^ (k + 1) = J ^ (k + 1) ⊓ T ⊔ J ^ (k + 2) := by
    rw [inf_sup_assoc_of_le T (pow_succ_succ_le J hJ k), hn, inf_top_eq]
  have hy : J = J ⊓ T ⊔ J ^ 2 := by
    have hle : J ^ 2 ≤ J := by simpa using pow_succ_succ_le J hJ 0
    rw [inf_sup_assoc_of_le T hle, h2, inf_top_eq]
  have key : J ^ (k + 2) ≤ T ⊔ J ^ (k + 3) := by
    calc J ^ (k + 2) = J ^ (k + 1) * J := pow_succ J (k + 1)
      _ = (J ^ (k + 1) ⊓ T ⊔ J ^ (k + 2)) * (J ⊓ T ⊔ J ^ 2) := by
          rw [← hx, ← hy]
      _ = (J ^ (k + 1) ⊓ T) * (J ⊓ T) ⊔ (J ^ (k + 1) ⊓ T) * J ^ 2 ⊔
            (J ^ (k + 2) * (J ⊓ T) ⊔ J ^ (k + 2) * J ^ 2) := by
          rw [Submodule.sup_mul, Submodule.mul_sup, Submodule.mul_sup]
      _ ≤ T ⊔ J ^ (k + 3) := by
          refine sup_le (sup_le ?_ ?_) (sup_le ?_ ?_)
          · exact le_sup_of_le_left
              ((mul_le_mul' inf_le_right inf_le_right).trans hTT)
          · refine le_sup_of_le_right ?_
            calc (J ^ (k + 1) ⊓ T) * J ^ 2 ≤ J ^ (k + 1) * J ^ 2 :=
                  mul_le_mul_left inf_le_left _
              _ = J ^ (k + 3) := (pow_add J (k + 1) 2).symm
          · refine le_sup_of_le_right ?_
            calc J ^ (k + 2) * (J ⊓ T) ≤ J ^ (k + 2) * J :=
                  mul_le_mul_right inf_le_left _
              _ = J ^ (k + 3) := (pow_succ J (k + 2)).symm
          · refine le_sup_of_le_right ?_
            calc J ^ (k + 2) * J ^ 2 = J ^ (k + 4) := (pow_add J (k + 2) 2).symm
              _ ≤ J ^ (k + 3) := pow_succ_succ_le J hJ (k + 2)
  apply top_le_iff.mp
  calc ⊤ = T ⊔ J ^ (k + 2) := hn.symm
    _ ≤ T ⊔ (T ⊔ J ^ (k + 3)) := sup_le_sup_left key T
    _ = T ⊔ J ^ (k + 3) := by rw [← sup_assoc, sup_idem]

/-- Proposition 1.2.8: if `J` is a nilpotent right ideal (e.g. `J(Λ)` for
Artinian `Λ`) and the subring `Λ'` satisfies `Λ' + J² = Λ`, then `Λ' = Λ`. -/
theorem eq_top_of_sup_sq (S : Subalgebra R A) (J : Submodule R A)
    (hJ : J * ⊤ ≤ J) (m : ℕ) (hnil : J ^ m = ⊥)
    (h2 : Subalgebra.toSubmodule S ⊔ J ^ 2 = ⊤) : S = ⊤ := by
  have all : ∀ k, Subalgebra.toSubmodule S ⊔ J ^ (k + 2) = ⊤ := by
    intro k
    induction k with
    | zero => simpa using h2
    | succ k ih => exact fill_step S J hJ h2 k ih
  have hz : J ^ (m + 2) = ⊥ := by rw [pow_add, hnil, bot_mul]
  have := all m
  rw [hz, sup_bot_eq] at this
  exact Algebra.toSubmodule_eq_top.mp this

end BensonRepresentations.SurjectiveModRadicalSquare

#print axioms BensonRepresentations.SurjectiveModRadicalSquare.pow_succ_mul_top_le
#print axioms BensonRepresentations.SurjectiveModRadicalSquare.pow_succ_succ_le
#print axioms BensonRepresentations.SurjectiveModRadicalSquare.fill_step
#print axioms BensonRepresentations.SurjectiveModRadicalSquare.eq_top_of_sup_sq
