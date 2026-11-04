import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Algebra.Group.Action.Defs

/-!
# The wreath product embedding behind induction and tensor induction

Section 3.15, p. 97: for `H ≤ G` with left coset representatives
`g_1, …, g_n`, write `g g_j = g_(π(j)) h_j` and `i(g) = (π; h_1, …, h_n)`.
With the printed multiplication of `Σ_n ≀ H`
`(π'; h'_1, …, h'_n)(π; h_1, …, h_n) = (π' π; h'_(π(1)) h_1, …, h'_(π(n)) h_n)`
the map `i` is a homomorphism, and the printed formula
`(π; h_1, …, h_n)(m_1, …, m_n) = (h_(π⁻¹(1)) m_(π⁻¹(1)), …, h_(π⁻¹(n)) m_(π⁻¹(n)))`
is an action (on `M^n`; the same formula on the tensor factors defines the
action on `M^(⊗n)`).

Notation: `Fin n` indexes the cosets, `rep : Fin n → G` are the
representatives, `pi g : Equiv.Perm (Fin n)` and `hh g : Fin n → H` are the
data of the decomposition `g * rep j = rep (pi g j) * hh g j`, assumed to
exist (hypothesis `hdec`) and to be unique because the cosets `rep j H` are
disjoint (hypothesis `huniq`). `M` is any type with an action of `H`
(for the book, an `RH`-module).

* `wmul`: the printed product; `wmul_assoc`: it is associative.
* `i_mul`: `i(x y) = i(x) i(y)` for the printed product.
* `act`: the printed action on `Fin n → M`; `act_wmul`, `act_one`: it is an
  action; in particular `x ↦ act (i x)` is an action of `G` (`act_i_mul`).

Not covered: the action on `M^(⊗n)` (the same index bookkeeping on pure
tensors, not formalized), that `i^*(M^n)` is `M↑^G` (the book's
identification `M↑^G = ⊕ g_j ⊗ M`), the independence of the choice of
representatives up to conjugation; these and
Proposition 3.15.2 are checked in `checks/sage/chapter-3b.py` on small groups.
-/

namespace BensonRepresentations.WreathEmbedding

variable {G : Type*} [Group G] {H : Subgroup G} {n : ℕ}

/-- The printed product in `Σ_n ≀ H`. -/
def wmul (a b : Equiv.Perm (Fin n) × (Fin n → H)) :
    Equiv.Perm (Fin n) × (Fin n → H) :=
  (a.1 * b.1, fun j => a.2 (b.1 j) * b.2 j)

theorem wmul_assoc (a b c : Equiv.Perm (Fin n) × (Fin n → H)) :
    wmul (wmul a b) c = wmul a (wmul b c) := by
  simp only [wmul, Equiv.Perm.mul_apply, mul_assoc]

section embedding

variable (rep : Fin n → G) (pi : G → Equiv.Perm (Fin n)) (hh : G → Fin n → H)
  (hdec : ∀ (g : G) (j : Fin n), g * rep j = rep (pi g j) * (hh g j : G))
  (huniq : ∀ (j j' : Fin n) (h h' : H), rep j * (h : G) = rep j' * (h' : G) →
    j = j' ∧ h = h')

include hdec huniq in
/-- `i(x y) = i(x) i(y)` with the printed multiplication. -/
theorem i_mul (x y : G) :
    (pi (x * y), hh (x * y)) = wmul (pi x, hh x) (pi y, hh y) := by
  have key : ∀ j, rep (pi (x * y) j) * (hh (x * y) j : G) =
      rep (pi x (pi y j)) * ((hh x (pi y j) * hh y j : H) : G) := by
    intro j
    rw [← hdec, mul_assoc, hdec y j, ← mul_assoc, hdec x, Subgroup.coe_mul,
      mul_assoc]
  have h := fun j => huniq _ _ _ _ (key j)
  simp only [wmul, Prod.mk.injEq]
  constructor
  · ext j
    simp [(h j).1]
  · funext j
    exact (h j).2

end embedding

section action

variable {M : Type*} [MulAction H M]

/-- The printed action `(π; h)(m)_i = h_(π⁻¹ i) m_(π⁻¹ i)`. -/
def act (a : Equiv.Perm (Fin n) × (Fin n → H)) (m : Fin n → M) : Fin n → M :=
  fun i => a.2 (a.1⁻¹ i) • m (a.1⁻¹ i)

theorem act_one (m : Fin n → M) : act ((1 : Equiv.Perm (Fin n)), fun _ => (1 : H)) m = m := by
  funext i
  simp [act]

theorem act_wmul (a b : Equiv.Perm (Fin n) × (Fin n → H)) (m : Fin n → M) :
    act (wmul a b) m = act a (act b m) := by
  funext i
  simp only [act, wmul, mul_inv_rev, Equiv.Perm.mul_apply, mul_smul]
  rw [show b.1 (b.1⁻¹ (a.1⁻¹ i)) = a.1⁻¹ i by simp [Equiv.Perm.coe_inv]]

variable (rep : Fin n → G) (pi : G → Equiv.Perm (Fin n)) (hh : G → Fin n → H)
  (hdec : ∀ (g : G) (j : Fin n), g * rep j = rep (pi g j) * (hh g j : G))
  (huniq : ∀ (j j' : Fin n) (h h' : H), rep j * (h : G) = rep j' * (h' : G) →
    j = j' ∧ h = h')

include hdec huniq in
/-- `x ↦ act (i x)` is an action of `G`: `i^*(M^n)` (and `i^*(M^(⊗n))`) is a
`G`-module. -/
theorem act_i_mul (x y : G) (m : Fin n → M) :
    act (pi (x * y), hh (x * y)) m = act (pi x, hh x) (act (pi y, hh y) m) := by
  rw [i_mul rep pi hh hdec huniq x y, act_wmul]

end action

end BensonRepresentations.WreathEmbedding

#print axioms BensonRepresentations.WreathEmbedding.wmul_assoc
#print axioms BensonRepresentations.WreathEmbedding.i_mul
#print axioms BensonRepresentations.WreathEmbedding.act_one
#print axioms BensonRepresentations.WreathEmbedding.act_wmul
#print axioms BensonRepresentations.WreathEmbedding.act_i_mul
