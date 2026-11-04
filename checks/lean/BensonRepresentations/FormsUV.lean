import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# The elements `u`, `v` and the two forms: Lemma 5.10.3, Proposition 5.10.4

Book: D. J. Benson, *Representations and Cohomology I*, second edition
(1998), Section 5.10, Lemma 5.10.3 and Proposition 5.10.4 with their
proofs, pp. 197–198 of the printed book.

Notation.  `A` is the representation ring `a(G)` (a commutative ring),
`dual : A →+* A` the ring homomorphism `[M] ↦ [M*]`, `u = [P_k] - [Ω⁻¹(k)]`,
`v = [P_k] - [Ω(k)]` (Definition 5.10.1).  `B x y` is the form `(x, y)`
(`([M], [N]) = dim_k Hom_kG(M, N)`) and `S x y` the form `⟨x, y⟩`, both
with values in a type `R` (`ℤ` or `ℂ`).

* `u_mul_v` (Lemma 5.10.3): from the two isomorphisms of the proof,
  `P_k ⊕ Ω(k) ⊗ Ω⁻¹(k) ≅ k ⊕ P_k ⊗ Ω⁻¹(k)` (Schanuel) and
  `P_k ⊗ P_k ≅ P_k ⊗ Ω(k) ⊕ P_k`, written as equations in `A`, it follows
  that `(P - Ω)(P - Ω') = 1`.
* `forms_i`, `forms_ii`, `forms_iii` (Proposition 5.10.4): from
  `⟨x, y⟩ = (u x, y)` (Lemma 5.10.2 (iii), extended bilinearly), the
  symmetry of `⟨ , ⟩` (Lemma 5.10.2), `u v = 1`, `dual u = v` and the
  adjunction `(x z, y) = (x, z* y)` (`Hom_kG(M ⊗ Z, N) ≅ Hom_kG(M, Z* ⊗ N)`),
  the identities (i) `(x, y) = ⟨v x, y⟩ = ⟨x, u y⟩`, (ii) `⟨x, y⟩ = (u x, y)
  = (x, v y)` and (iii) `(x, y) = (y, v² x) = (u² y, x)` hold for all `x, y`.
  This is the book's proof ("the rest follows from the identity `uv = 1` and
  the fact that `u` is obtained from `v` by dualising").

Not covered: the module isomorphisms themselves (Schanuel's lemma, the
adjunction, `P_k` self-dual, `Ω⁻¹(k) ≅ Ω(k)*`) and Lemma 5.10.2, which are
the hypotheses here; they are checked on modules of `C_q`, `S₃`, `A₄`,
`C₃ ⋊ C₄`, `D₁₀`, `V₄` in `checks/sage/chapter-5.py`.  Bilinearity of the
forms is not needed for these identities.
-/

namespace BensonRepresentations.FormsUV

variable {A R : Type*} [CommRing A]

/-- Lemma 5.10.3: `u v = 1` from the two isomorphisms of its proof. -/
theorem u_mul_v (P Om Om' : A) (hSchanuel : P + Om * Om' = 1 + P * Om')
    (hproj : P * P = P * Om + P) : (P - Om) * (P - Om') = 1 := by
  linear_combination hproj + hSchanuel

variable (B S : A → A → R) (dual : A →+* A) (u v : A)

theorem forms_i (huv : u * v = 1) (hdual : dual u = v)
    (hadj : ∀ x y z, B (x * z) y = B x (dual z * y))
    (hS : ∀ x y, S x y = B (u * x) y) (x y : A) :
    B x y = S (v * x) y ∧ B x y = S x (u * y) := by
  constructor
  · rw [hS, ← mul_assoc, huv, one_mul]
  · rw [hS, mul_comm u x, hadj, hdual, ← mul_assoc, mul_comm v u, huv,
      one_mul]

theorem forms_ii (hdual : dual u = v)
    (hadj : ∀ x y z, B (x * z) y = B x (dual z * y))
    (hS : ∀ x y, S x y = B (u * x) y) (x y : A) :
    S x y = B (u * x) y ∧ S x y = B x (v * y) := by
  refine ⟨hS x y, ?_⟩
  rw [hS, mul_comm u x, hadj, hdual]

theorem forms_iii (huv : u * v = 1) (hdual : dual u = v)
    (hadj : ∀ x y z, B (x * z) y = B x (dual z * y))
    (hS : ∀ x y, S x y = B (u * x) y) (hsymm : ∀ x y, S x y = S y x)
    (x y : A) :
    B x y = B y (v * v * x) ∧ B x y = B (u * u * y) x := by
  have h1 : B x y = S (v * x) y :=
    (forms_i B S dual u v huv hdual hadj hS x y).1
  have h2 : B x y = B y (v * v * x) := by
    rw [h1, hsymm, hS, mul_comm u y, hadj, hdual, mul_assoc]
  refine ⟨h2, ?_⟩
  rw [h2, show u * u * y = y * u * u by ring, hadj, hdual, hadj, hdual,
    mul_assoc]

end BensonRepresentations.FormsUV

#print axioms BensonRepresentations.FormsUV.u_mul_v
#print axioms BensonRepresentations.FormsUV.forms_i
#print axioms BensonRepresentations.FormsUV.forms_ii
#print axioms BensonRepresentations.FormsUV.forms_iii
