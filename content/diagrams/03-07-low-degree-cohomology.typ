#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// A lifting problem: G above the fourth object of the first row of an
// extension, mapping down to it; the dotted map to be found goes from G to
// the third object. Further rows follow below, joined to the first by the
// vertical maps `down`.
#let lifting-problem(rows, down: ()) = grid-diagram(
  ((none, none, none, $G$, none), ..rows),
  across: (none, ..rows.map(_ => "->")),
  down: ((none, none, none, "->", none), ..down),
  extra: (edge((3, 0), (2, 1), "..>"),),
  row: 7mm,
)

// Green's lifting theorem (Theorem 3.7.7): a lift of G -> GL_n(O/p^i) to
// GL_n(O/p^(i+1)), whose kernel is End_k(M).
#let green-lifting = lifting-problem((
  (
    $1$,
    $End_k (M)$,
    $GL_n (cal(O) slash frak(p)^(i+1))$,
    $GL_n (cal(O) slash frak(p)^i)$,
    $1$,
  ),
))

// Maranda's theorem (Theorem 3.7.8): two extensions with the same kernel,
// the first mapping to the second by reduction, and multiplication by p^r
// on the kernels.
#let maranda-lifting = {
  let kernel = $End_cal(O) (tilde(M) slash p^(r+1) tilde(M))$
  lifting-problem(
    (
      (
        $1$,
        kernel,
        $GL_n (cal(O) slash p^(a+r+1))$,
        $GL_n (cal(O) slash p^a)$,
        $1$,
      ),
      (
        $1$,
        kernel,
        $GL_n (cal(O) slash p^(a+1))$,
        $GL_n (cal(O) slash p^(a-r))$,
        $1$,
      ),
    ),
    down: ((none, (label: $p^r$), "->", "->", none),),
  )
}
