import Mathlib.Algebra.Group.Hom.Defs
import Mathlib.Algebra.Group.Basic

/-!
# Proposition 2.3.7: the connecting homomorphism is well defined

Benson, *Representations and Cohomology I*, Section 2.3, proof of
Proposition 2.3.7 (`prop:long-exact-homology`): for a short exact sequence
`0 → C' → C → C'' → 0` of chain complexes (Definition 2.3.6,
`def:short-exact-complexes`) and a cycle `x ∈ C''_n`, choose `y ∈ C_n` with
`ψ_n(y) = x`; then `∂_n(y) = φ_(n-1)(z)` for some `z ∈ C'_(n-1)`, `z` is a
cycle, and its class does not depend on the choice of `y`.

Notation: the three degrees `n`, `n - 1`, `n - 2` of the book are the suffixes
`n`, `m`, `l` (`Cn = C_n`, `C'm = C'_(n-1)`, `Cl = C_(n-2)`, ...);
`d'n = ∂'_n`, `dn = ∂_n`, `d''n = ∂''_n`, `d'm = ∂'_(n-1)`, `dm = ∂_(n-1)`,
`φn = φ_n`, ..., `ψm = ψ_(n-1)`.  Only the parts of the hypotheses used are
assumed: exactness `Ker ψ = Im φ` in degrees `n` and `n - 1`, injectivity of
`φ_(n-1)` and `φ_(n-2)`, the commuting squares and `∂ ∘ ∂ = 0` in `C`.  The
objects are abelian groups (modules over any ring are a special case).

Not covered: that `[z]` depends only on the class `[x]` (this needs degree
`n + 1`), additivity of the connecting map and the exactness of the long
exact sequence ("not hard to check" in the book), and the snake lemma 2.3.9.
-/

namespace BensonRepresentations.ConnectingHomomorphism

variable {C'n Cn C''n C'm Cm C''m C'l Cl : Type*}
  [AddCommGroup C'n] [AddCommGroup Cn] [AddCommGroup C''n]
  [AddCommGroup C'm] [AddCommGroup Cm] [AddCommGroup C''m]
  [AddCommGroup C'l] [AddCommGroup Cl]

/-- The lift `z` exists: `ψ_(n-1)(∂_n y) = ∂''_n(ψ_n y) = ∂''_n x = 0`, and
`Ker ψ_(n-1) = Im φ_(n-1)`. -/
theorem exists_lift (dn : Cn →+ Cm) (d''n : C''n →+ C''m) (φm : C'm →+ Cm)
    (ψn : Cn →+ C''n) (ψm : Cm →+ C''m)
    (hexm : ∀ y, ψm y = 0 → ∃ z, φm z = y)
    (hsq : ∀ y, ψm (dn y) = d''n (ψn y))
    {x : C''n} (hx : d''n x = 0) {y : Cn} (hy : ψn y = x) :
    ∃ z, φm z = dn y :=
  hexm _ (by rw [hsq, hy, hx])

/-- `z` is a cycle: `φ_(n-2)(∂'_(n-1) z) = ∂_(n-1)(φ_(n-1) z) = ∂_(n-1) ∂_n y = 0`. -/
theorem lift_is_cycle (dn : Cn →+ Cm) (d'm : C'm →+ C'l) (dm : Cm →+ Cl)
    (φm : C'm →+ Cm) (φl : C'l →+ Cl)
    (hφl : Function.Injective φl)
    (hsq : ∀ z, dm (φm z) = φl (d'm z))
    (hdd : ∀ y, dm (dn y) = 0)
    {y : Cn} {z : C'm} (hz : φm z = dn y) :
    d'm z = 0 := by
  apply hφl
  rw [← hsq, hz, hdd, map_zero]

/-- Independence of the choices: if `y, y'` both lift `x` and
`φ_(n-1) z = ∂_n y`, `φ_(n-1) z' = ∂_n y'`, then `z - z' = ∂'_n u` with
`y - y' = φ_n u`. -/
theorem lift_well_defined (d'n : C'n →+ C'm) (dn : Cn →+ Cm)
    (φn : C'n →+ Cn) (φm : C'm →+ Cm) (ψn : Cn →+ C''n)
    (hexn : ∀ y, ψn y = 0 → ∃ u, φn u = y)
    (hφm : Function.Injective φm)
    (hsq : ∀ u, dn (φn u) = φm (d'n u))
    {y y' : Cn} (hyy : ψn y = ψn y') {z z' : C'm}
    (hz : φm z = dn y) (hz' : φm z' = dn y') :
    ∃ u, d'n u = z - z' := by
  obtain ⟨u, hu⟩ := hexn (y - y') (by rw [map_sub, hyy, sub_self])
  refine ⟨u, hφm ?_⟩
  rw [← hsq, hu, map_sub, map_sub, hz, hz']

end BensonRepresentations.ConnectingHomomorphism

#print axioms BensonRepresentations.ConnectingHomomorphism.exists_lift
#print axioms BensonRepresentations.ConnectingHomomorphism.lift_is_cycle
#print axioms BensonRepresentations.ConnectingHomomorphism.lift_well_defined
