#import "statements.typ": editorial-bib-item
#import "bibliography-style.typ": bib-description

// The works cited only in the editorial notes, after the Bibliography of the
// book; descriptions are generated from editorial.bib.
#metadata((kind: "bibliography-boundary", enter: true))
#heading(level: 1, numbering: none)[Editorial references]

#editorial-bib-item[
  #bib-description("Simson2007", editorial: true)
] <bib:Simson2007>

#metadata((kind: "bibliography-boundary", enter: false))
