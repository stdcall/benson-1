#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// The Brauer map and the transfer maps (Lemma 6.2.5).
#let brauer-transfer-square = grid-diagram(
  (
    ($(k G)^D$, $k C_G (D)$),
    ($(k G)_D^G$, $k C_G (D)_D^(N_G (D))$),
  ),
  across: (label: $Br_D$),
  down: (((label: $Tr_(D, G)$), (label: $Tr_(D, N_G (D))$)),),
  gap: 10mm,
  row: 10mm,
)
