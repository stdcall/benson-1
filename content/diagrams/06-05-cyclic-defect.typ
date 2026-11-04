#import "../main-defs.typ": *

// The Cartan matrix C of a Brauer tree in the proof of Theorem 6.5.5: the
// Cartan matrices X and Y of the subtrees L and R stand along the diagonal
// and overlap in the single entry z of the edge E, all other entries being
// zero. The matrix is drawn as a grid of three rows and three columns; a
// block occupies the rows and columns from its first to its last, its
// label stands in its row away from the overlap, and its edges inside the
// matrix are drawn, so that the overlap is boxed.
#let block-matrix(blocks, overlap, zero, size: 3) = {
  let inside(block, i) = block.first <= i and i <= block.last
  let cells = ()
  for row in range(size) {
    for column in range(size) {
      let covering = blocks.filter(b => inside(b, row) and inside(b, column))
      if covering.len() == 0 {
        cells.push(grid.cell(x: column, y: row, zero))
      } else if covering.len() == blocks.len() {
        cells.push(grid.cell(x: column, y: row, overlap))
      }
    }
  }
  let lines = ()
  for block in blocks {
    let span = block.last - block.first + 1
    let row = if block.first == 0 { block.first } else { block.last }
    cells.push(grid.cell(
      x: block.first,
      y: row,
      colspan: span,
      block.label,
    ))
    // The edges of the block that lie inside the matrix, in thin rules.
    let (start, end) = (block.first, block.last + 1)
    for edge in (start, end).filter(e => 0 < e and e < size) {
      lines.push(grid.vline(x: edge, start: start, end: end, stroke: 0.45pt))
      lines.push(grid.hline(y: edge, start: start, end: end, stroke: 0.45pt))
    }
  }
  math.mat(grid(
    columns: (1.6em,) * size,
    rows: (1.5em,) * size,
    align: center + horizon,
    stroke: none,
    ..cells,
    ..lines,
  ))
}

#let cartan-overlap = block-matrix(
  (
    (label: $X$, first: 0, last: 1),
    (label: $Y$, first: 1, last: 2),
  ),
  $z$,
  $0$,
)
