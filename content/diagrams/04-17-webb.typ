#import "common.typ": cd, edge, node
#import "../main-defs.typ": *

// The components of stable quivers in the Examples of Section 4.17, drawn as
// meshes, as in the book. The module in column h and row r (rows counted
// downwards) has arrows to the modules in column h + 1 and rows r ± 1, so
// that the translation Ω² moves a module two columns to the left. A picture
// gives its modules by these places and the arrows follow.

#let key(place) = str(place.first()) + "," + str(place.last())

// The label of a valued arrow, "(2,1)", in small roman type, as printed.
#let value(pair) = text(size: 0.7em)[(#pair.first(),#pair.last())]

// A mesh. `modules` are pairs (place, label). The mesh arrows join two
// places of which at least one holds a module and the other a module, an
// object of `continued` (dots for the component going on beyond the
// picture) or one of the `ends` (an empty place: the arrows trail off
// there). `across` lists further arrows (from, to), such as those through a
// projective module; `valuation` gives the label of an arrow from one row to
// another, or `none`; `marks` are labels joined to nothing; `dotted` lists
// lines through given places along an edge of the picture to be identified
// with another.
#let mesh(
  modules,
  continued: (),
  ends: (),
  across: (),
  valuation: (from, to) => none,
  marks: (),
  dotted: (),
  gap: 6mm,
  row: 4mm,
) = {
  let kind = (:)
  for (place, _) in modules { kind.insert(key(place), "module") }
  for place in continued { kind.insert(key(place), "continued") }
  for place in ends { kind.insert(key(place), "end") }
  let places = modules.map(((place, _)) => place) + continued + ends
  let arrow(from, to) = {
    let pair = valuation(from.last(), to.last())
    if pair == none { edge(from, to, "->") } else {
      edge(from, to, value(pair), "->", label-side: left)
    }
  }
  let arrows = ()
  for place in places {
    let (h, r) = place
    for next in ((h + 1, r - 1), (h + 1, r + 1)) {
      if (
        key(next) in kind
          and "module" in (kind.at(key(place)), kind.at(key(next)))
      ) { arrows.push(arrow(place, next)) }
    }
  }
  cd(
    spacing: (gap, row),
    ..modules.map(((place, label)) => node(place, label)),
    ..continued.map(place => node(place, $dots.c$)),
    ..ends.map(place => node(place, [], width: 1.5em, height: 1em)),
    ..arrows,
    ..across.map(((from, to)) => edge(from, to, "->")),
    ..marks.map(((place, label)) => node(place, label)),
    ..dotted
      .map(line => range(line.len() - 1).map(i => edge(
        line.at(i),
        line.at(i + 1),
        "..",
      )))
      .flatten(),
  )
}

// Ω^e(S), written Ω(S) for e = 1 and S for e = 0.
#let omega-power(e, simple) = if e == 0 { simple } else if e == 1 {
  $Omega(#simple)$
} else { $Omega^(#e) (#simple)$ }

// Example (i): the component ℤÃ₁₂ of the modules Ω^n(k) for the Klein four
// group, each arrow valued (2,2), with the projective cover P_k of k
// attached below between Ω(k) and Ω⁻¹(k).
#let klein-four-component = {
  let exponents = (2, 1, 0, -1, -2)
  let row = (
    $dots.c$,
    ..exponents.map(e => omega-power(e, $k$)),
    $dots.c$,
  )
  let middle = exponents.position(e => e == 0) + 1
  let projective = (middle, 1)
  cd(
    spacing: (6mm, 5mm),
    ..row.enumerate().map(((x, label)) => node((x, 0), label)),
    node(projective, $P_k$),
    ..range(row.len() - 1).map(x => edge(
      (x, 0),
      (x + 1, 0),
      value((2, 2)),
      "->",
      label-side: left,
    )),
    edge((middle - 1, 0), projective, "->"),
    edge(projective, (middle + 1, 0), "->"),
  )
}

// Example (ii): the 3-tube of the modules W_{i,α}(c), c running through 1,
// ᾱ, α. The modules W_{4,α}, …, W_{1,α} stand in the rows 1 to 4, W_{1,α}(1)
// in the first column, with arrows trailing off upwards from W_{4,α} and
// dots above; going up a row moves c one step back through the cycle, and
// τ⁻¹, two columns to the right, one step on. The left and right edges,
// dotted, are identified.
#let three-tube = {
  let cycle = ($1$, $macron(alpha)$, $alpha$)
  let columns = range(7)
  let modules = ()
  for r in range(1, 5) {
    let i = 5 - r
    for h in columns.filter(h => calc.even(h + r)) {
      let c = cycle.at(calc.rem-euclid(int((h - 3 * (i - 1)) / 2), 3))
      modules.push(((h, r), $W_(#i, alpha) (#c)$))
    }
  }
  let top = columns.filter(calc.even)
  mesh(
    modules,
    ends: top.map(h => (h, 0)),
    marks: top.map(h => ((h, -0.7), $dots.v$)),
    dotted: (columns.first(), columns.last()).map(h => (
      (h, 0.5),
      (h, 2),
      (h, 4),
    )),
    gap: 1.5mm,
    row: 4mm,
  )
}

// The component of the modules Ω^n(S) of the simple modules S, given by the
// simple module of each row: Ω^(3−h)(S) in column h at every place with
// h + r odd; in the middle column, at the other rows, the projective cover
// P_S of the simple S of the row, between Ω(S) and Ω⁻¹(S); dots at both
// ends.
#let simples-component(simples, valuation: (from, to) => none, dotted: ()) = {
  let modules = ()
  for (r, simple) in simples.enumerate() {
    for h in range(1, 6).filter(h => calc.odd(h + r)) {
      modules.push(((h, r), omega-power(3 - h, simple)))
    }
    if calc.odd(r) {
      modules.push(((3, r), $P_#simple$))
    }
  }
  let odd-rows = range(simples.len()).filter(calc.odd)
  mesh(
    modules,
    continued: odd-rows.map(r => (0, r)) + odd-rows.map(r => (6, r)),
    across: odd-rows.map(r => (((2, r), (3, r)), ((3, r), (4, r)))).join(),
    valuation: valuation,
    dotted: dotted,
    gap: 7mm,
    row: 7mm,
  )
}

// ℤÃ₅: the simples k, ω, ω̄ in turn down the rows; the top and bottom edges,
// dotted, are identified.
#let simples-component-a5 = {
  let cycle = ($k$, $omega$, $macron(omega)$)
  let rows = 7
  simples-component(
    range(rows).map(r => cycle.at(calc.rem(r, cycle.len()))),
    dotted: (0, rows - 1).map(r => (
      (0.5, r),
      (1, r),
      (3, r),
      (5, r),
      (5.5, r),
    )),
  )
}

// ℤB̃₃: the simples k and the two dimensional S; the arrows from the row of
// k to the row of S below it are valued (1,2), those from S to k below it
// (2,1), and those back up the opposite way round.
#let simples-component-b3 = {
  let values = ("0,1": (1, 2), "2,3": (2, 1))
  simples-component(
    ($k$, $S$, $S$, $k$),
    valuation: (from, to) => {
      if from < to {
        values.at(str(from) + "," + str(to), default: none)
      } else {
        let pair = values.at(str(to) + "," + str(from), default: none)
        if pair != none { pair.rev() }
      }
    },
  )
}

// Example (iii): a component ℤA_∞^∞ of modules of the first kind M(C) for a
// dihedral group. Going up and to the left applies R_q, going down and to
// the left L_q, from M(C) in the middle; arrows trail off above and below,
// with dots.
#let string-component = {
  let centre = (3, 2)
  let factor(name, n) = if n == 0 { none } else {
    math.attach(
      name,
      b: $q$,
      t: if n == 1 { none } else if n < 0 { $-#(-n)$ } else { $#n$ },
    )
  }
  let modules = ()
  for h in range(1, 6) {
    for r in range(5).filter(r => calc.odd(h + r)) {
      let (dh, dr) = (h - centre.first(), r - centre.last())
      let (left, right) = (int((dr - dh) / 2), int(-(dh + dr) / 2))
      modules.push((
        (h, r),
        $M(#factor($L$, left) #factor($R$, right) C)$,
      ))
    }
  }
  let even = range(0, 7, step: 2)
  mesh(
    modules,
    continued: ((0, 1), (0, 3), (6, 1), (6, 3)),
    ends: even.map(h => (h, -1)) + even.map(h => (h, 5)),
    marks: (2, 4)
      .map(h => (((h, -1.6), $dots.v$), ((h, 5.6), $dots.v$)))
      .join(),
    gap: 1mm,
    row: 2.5mm,
  )
}

// The component with the projective P attached between M(A⁻¹B) and
// M(AB⁻¹).
#let projective-string-component = mesh(
  (
    ((1, 2), $M(A^(-1) B)$),
    ((2, 1), $M(R_q A B^(-1))$),
    ((2, 2), $P$),
    ((2, 3), $M(L_q A B^(-1))$),
    ((3, 2), $M(A B^(-1))$),
  ),
  continued: ((0, 1), (0, 3), (4, 1), (4, 3)),
  ends: ((1, 0), (3, 0), (1, 4), (3, 4)),
  across: (((1, 2), (2, 2)), ((2, 2), (3, 2))),
  gap: 12mm,
  row: 7mm,
)
