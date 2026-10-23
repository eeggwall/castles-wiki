# PE502 house style

Part I applies to every paper in this series and to the OEIS proof notes. Part II adds the rules
for the PE502 castle reports. Read the guide before drafting or revising, and run the checklist
at the end before handing in a draft. When a review produces a new rule, add it here.

Symbols and names are not listed here. They are defined in the published reports, and each
report reuses what earlier reports defined (section 11).


# Part I. Writing a paper

## 1. Readers

- The readers are applied mathematicians, engineers and physicists. They know generating
  functions, linear algebra, continued fractions, series and calculus. They are not specialists
  in enumerative combinatorics or topology.
- Write above the elementary level and below the level of a combinatorics preprint. A term from
  outside the readers' background gets one sentence of explanation where it first appears:
  shift of finite type, entropy, adjugate, Cayley-Hamilton theorem, period of a continued
  fraction. For a cited theorem, say what it states and how the paper uses it.
- A paper stands alone: a reader with the PDF and its reference list can follow every step. It
  never mentions internal notes, plans or tools.


## 2. Voice

- Write as a normal mathematics paper: plain declarative prose in the first person plural ("we
  subtract the strips that stay below the ceiling").
- The Introduction says what question the paper answers and why it is worth answering. Results
  and proofs carry no commentary.
- No analogies, anecdotes, opinions or ornamental lines.
- Do not speculate about motives or perception.
- State a fact directly: "Exchanging the heights 1 and 2 turns a ridge castle into a Fibonacci
  castle."
- Never ask a question and answer it in the next sentence ("Could ...? They cannot: ...").
  State the answer.
- A paragraph follows one direction. When the argument turns, start a new paragraph.


## 3. Structure

- Open with a simple, concrete question, and let the paper's topics grow out of it: PE502-3
  opens with an exercise on the Pell numbers, and strips, Pell strips and Pell castles follow
  from its solution.
- The Introduction states the main results as Theorems, in words and in symbols, and says where
  each is proved.
- Each section follows one line of argument, from the question it opens with to its answer.
- Keep the number of moving parts small. Every Definition, symbol and Lemma is used on the main
  line of the paper; cut side results, extra notation and objects that only appear once.
- Introduce a Definition or Lemma close to the step that uses it. Avoid stacking several new
  constructions before using any of them; group them up front only when they belong together.
- State a problem in full where it is used. Don't refer to "the exercise" as if the reader
  already knows it.
- Each section opens with a sentence or a picture before its first formula. A paragraph never
  opens with a bare formula standing in for a heading; use `\paragraph{...}`.
- A technical report ends with a section titled Conclusion: a concise summary of the results in
  order, one `\paragraph{...}` per topic, each result with a pointer to the Theorem, equation,
  table or figure that states it. It adds no new results. A short note may end on its last
  proof.
- No section on future work. The references follow the Conclusion, or the last section.


## 4. Results and proofs

- The numbered environments are Theorem, Proposition, Lemma, Corollary, Definition, Remark and
  Example, with their standard meanings:
  - Theorem: a main result of the paper.
  - Proposition: a result of independent interest that is not a main result.
  - Lemma: a step used in the proof of something else.
  - Corollary: a direct consequence of a Theorem or Proposition.
  - Definition: a new object or name.
  - Remark: a comment that needs no proof.
  - Example: a worked case.
- A Theorem or Proposition states one result, or a short list of parallel results.
- Every Theorem, Proposition, Lemma and Corollary is proved in the paper or cited to a source
  that proves it.
- A proof is as long as its steps require. A routine verification takes one sentence
  ("expanding the product gives ..."). A proof with several genuine steps is split into labeled
  steps (`\emph{Strips.}`, `\emph{Difference.}`).
- Cut any claim that is off the thread or unproved, and every hedge and caveat. Don't add a
  proof or a hedge to save it.
- Cut sentences that say nothing new or restate a definition.
- A result found only by computation (for example by Berlekamp-Massey) is proved, or reported
  as computed values in a table. It is never stated as a Theorem, Proposition, Lemma or
  Corollary.
- Every number in the text and tables is checked by brute force or exact computation. Tables say
  "Every entry agrees with brute-force enumeration."
- Never say that a sequence is not found in the OEIS.


## 5. Explanation

- Every new object gets a concrete example where it is introduced: a figure, a small table, or
  its smallest case written out.
- Don't jump from words to dense notation. Write out the smallest case (the matrices `R_2` and
  `R_3` and their characteristic polynomials) before the general argument, and describe a named
  quantity in words before giving its formula.
- A worked example has a figure and every intermediate step.
- A sentence that says something "shows why" or "explains" is followed by the steps that do so.
- Display every multi-term expression and any formula long enough to wrap across a line. Never
  chain rational functions inline in a paragraph.
- Name a sequence by its common name and A-number: "the Pell-Lucas numbers `\oeis{A001333}`",
  not "the companion sequence".
- When "both sides", "it" or "this" could mean more than one thing, name the thing.


## 6. Notation

- Define every symbol in the sentence where it first appears or the next one. This includes
  standard notation: `\operatorname{Re} z`, `i`, `I`, `J`, the all-ones vector `\mathbf 1`,
  `e_a`, `\chi_M`, `\operatorname{adj}`. Define a variable before using it: "the coefficient
  `a_n` of `x^n`", then `a_n`.
- A letter has one meaning in a paper. When a standard symbol collides with one already in use,
  decorate the other object and say so where it first appears.
- An object has one symbol for the whole paper. Don't switch symbols inside a proof.
- Keep every parameter a quantity depends on, even in a section where it is fixed:
  `\delta_{h-1}`, not `\delta`.
- When two parameters are related, write the relation: tower height `k = h - 1`.
- A plain count gets a plain variable: "`m`, the number of height-2 columns", not `r(c)`, which
  reads as a function `r` applied to `c`.
- When a cited source uses other symbols, translate them into ours.
- If the literature has a term for a family or property, use it. Before explaining where a name
  comes from, or citing precedent for it, check the literature.
- If the paper reuses symbols from earlier papers or resolves a collision, the Introduction
  ends with a Notation paragraph that lists them.


## 7. Numbering and cross-references

- Number equations within sections: (3.1), (3.2), ... in Section 3, with
  `\numberwithin{equation}{section}`.
- Number the main results, every equation in a Theorem or Proposition, and every identity that
  a later step uses. Not every display needs a number.
- Refer back by type and number, spelled out: `Equation~\eqref`, `Theorem~\ref`,
  `Lemma~\ref`, `Section~\ref`, `Table~\ref`, `Figure~\ref`. Never point back by position or
  order ("the generating function from above", "the second generating function"), except to
  the display just before the sentence.
- A step that uses an earlier result cites it by number in the same sentence. A proof says by
  number which equation of its statement each step proves.
- When a step uses a result from more than three pages back, restate it in a clause along with
  its number: "by Lemma 4, which bounds the expansion between `c_1 - 1` and `c_1`".


## 8. Figures and tables

- Never cut a figure, table or worked example to save space.
- One point per figure. A figure that shows two things becomes two figures. Each panel gets its
  own sentence in the caption.
- When the objects of a small size are few, draw all of them, as PE502-3 draws all four Pell
  castles of width 4.
- Every figure and table is referenced in the text, with the right type (`Figure~\ref`,
  `Table~\ref`).
- A caption defines the symbols it uses and states no fact that holds by definition.
- A table whose rows wrap onto several lines gets thin rules between its rows
  (`\cmidrule{1-N}`), and each text entry starts with a capital.


## 9. Citations

- Cite OEIS sequences with `\oeis{A000000}`. Never cite them by author and year, and never
  print "OEIS Foundation Inc.". In the reference list, each OEIS entry lists the pages that cite
  it, each page linked back to the text.
- Cite primary sources only.
- Read a source before citing it, and give the locator (Theorem I.1, p. 27; Example 2.1).
- A name attached to a result has a reference, and the text says what the result is. "Euler and
  Lagrange" with no reference does not qualify.
- A known result stated as a Theorem carries its source in its header, as the restated castle
  Definition carries `\pepub[Sec.~2]{PE502-1}`: `\begin{theorem}[{\cite[Sec.~2, p.~66]{key}}]`.
  Use `\cite` there, not `\parencite`, which would print a second pair of parentheses. The
  report may still prove the result, and the text says what the source states.
- Refer to an author by name or as "they", never "he" or "she".


## 10. Language and source

- American spelling: neighbor, color, labeled, center, behavior.
- One sentence per line in the `.tex` source.
- `\title` and an explicit `\date` each sit on one line. The author line is
  `Charles (Chaz) Reid`.
- No one-line widows or orphans in the PDF.


# Part II. PE502 castle reports

## 11. Series notation

- A symbol defined in a published report keeps that meaning in every later report. Before
  introducing a symbol, check the notation used in every report that you cite, and re-use
  what is already there.
- Never invent a new letter for a quantity that already has one. Drafts have written `S(w)`,
  `C(w)`, `N_h(w)` and `u_w` for the number of castles, and each was rejected: that number is
  `A`. (`S` is taken, for the signed castle count below.)
- Keep every parameter of a castle count: `A_{\mathrm{ridge}}(w,h)`, not `N_h(w)`. The
  metallic order of the ridge castles is `a = h - 1`.
- Collisions with series notation are decorated: the Pell numbers are `P^\star_n`, because `P`
  is the signed tower count. The Notation paragraph says so, and the text reminds the reader
  where the symbol returns.

### Castle counts

- `A` counts castles. `A(w,h)` is the number of castles of width `w` and height `h`.
- The count of a family X is `A_X(w,h)`, with an upright subscript (`A_{\mathrm{ridge}}(w,h)`).
  If the family's definition fixes the height, write `A_X(w)` and say once which height is
  implied.
- The even-block and odd-block parts are `A^e` and `A^o`, or `A^e_X` and `A^o_X` for a family.
- A signed count adds up `(-1)^blocks`, so each even-block object counts `+1` and each odd-block
  object `-1`. There are two signed counts, and the letter says which objects are added up:
  - `P` adds up over **towers** (a castle with its bottom row removed): `P(k, L)` over the
    towers of height at most `k` on a base of length `L`, as in PE502-1, and `P_X` over the
    towers of family X, as PE502-2's `P_F`.
  - `S` adds up over **castles**: `S(w, h)` over the castles of width `w` and height `h`,
    and `S_X` over the castles of family X. So `S = A^e - A^o`, `A^e = (A + S)/2` and
    `A^o = (A - S)/2`, and the same with the subscript X.
  - Never use `P` for a sum over castles. A castle has one block more than its tower, so the
    two signs are opposite: even-block castles are odd-block towers, and the castle split
    `(A + S)/2` corresponds to PE502-1's tower split `(T - P)/2`. A report that cites one for
    the other says so. The two are related by `S(w, h) = P(h-2, w) - P(h-1, w)`.
- A signed transfer matrix is the transfer matrix with a tilde: `\tilde M`, its principal
  submatrix `\tilde M'`, and `\tilde R_h` for the ridge matrix `R_h`. `S` is never a matrix.
- Introduce the phrase "signed count" once; after that, use the symbol.
- New reports do not use `F(w,h)`. The Project Euler count is `A^e(w,h)`, and the report says
  once, at first use, that it is the `F(w,h)` of `\pepub{PE502-1}`.


## 12. Castles and families

- The Introduction restates the castle definition of `\pepub{PE502-1}` as a cited Definition,
  and recaps in words, before symbols, the earlier results the report needs. Don't re-derive
  the basics in passing prose.
- A castle of height `h` has a column of height `h`; that is what "height `h`" means. Write
  "castles of height `h`", never "exact height" or "height exactly". Don't restate the fact in
  the text or in captions.
- When a cited source writes "exact height", translate it to "height", as with any other
  notation (section 6).
- A skyline that does not reach `h` is not a castle of height `h`: the flat row `(1, ..., 1)` is
  a castle of height 1. Towers may have height 0; castles may not.
- Strips, and any other skylines that need not reach their top height, need not be castles of
  height `h`. Say so where they are defined. Never write that strips "are not castles": a strip
  below the ceiling is still a castle of a lower height.
- The ceiling is the top height `h` of a strip rule. Castle strips need not reach it; castles of
  height `h` do. Write "the castle strips that reach the ceiling", never "require the ceiling"
  or "requiring the ceiling", which suggests a castle of height `h` might not reach `h`. When the
  report's question involves strips, introduce castle strips and the ceiling in the opening of
  the Introduction.
- The metallic means are the golden, silver and bronze *means*, de Spinadel's names, never
  "ratio". The title and the Introduction call them the metallic rungs of a ladder.
- Removing the bottom row of a castle leaves towers, plural. Each block of a tower carries
  towers of its own, as in the tower grammar of PE502-1.
- At height 2, write "castles of height 2" or "`h=2` castles", never "height at most 2", "height
  up to 2" or "height `\le 2`". For `h >= 3`, a sweep over "height at most `h`" is fine.
- Towers are not castles. A tower count such as `P(1, L)` is never restated as a count of
  castles of height at most 2.
- A result proved at one height names that height in every sentence and caption that states it.
  A fixed-height argument is never "the general case".
- Prefer a concrete statement at a named height to an abstract one: "the ridge castles of
  height 5 number `F_{3w+2} - 4 \cdot 3^{w-1}`".
- Every family of castles gets a Definition that states its construction rule, a figure, and a
  row in the roster table. With two or more families, the roster table (family, rule, counted
  by, count, section) comes before the families are discussed, placed at the top of a page.
- If every family is built the same way, say so in the Introduction, name the steps, and refer
  back to them by name.
- Start with the concrete family. A property such as "golden by width" comes after the family
  that motivates it.
- A family name may be coined. It is short and fits what its castles are. A modifier adds
  conditions to the noun and never removes one: castles that drop the condition `c_1 = 1` of
  Pell castles are not "smooth Pell castles". Avoid ambiguous names: "golden castle", with no
  qualifier, could mean a dozen things.
- A Definition fixes a parameter only when the parameter is part of the concept. Pell castles
  have height 3 by definition, so "Pell castle" carries the height. Smoothness is about height
  differences, so a smooth castle is defined at every height, and the height is named wherever
  it is fixed: "smooth castles of height 4".
- Once a name is tied to a parameter value (Pell to height 3), don't use it at other values
  without saying so.
- Every rule that defines a family has a name. A family is never left as "the ceiling rule".
- Growth words are adjectives on an axis, never family names: "golden by width", "silver by
  width". Not "golden castles", and not "the family is golden". Define the property before its
  first use.
- The title names the main subject of the report.


## 13. Castle figures

- Draw figures as PE502-3 does: each new family with example castles or strips, each strip rule
  with its transfer graph (states at their heights), and all members of a small size.
- Draw castles as PE502-1 does: unit cells with blocks outlined row by row, reusing the `cell`,
  `brick` and `wall` TikZ styles. Use another drawing convention only when the drawing itself is
  the point.
- Name a skyline as one: "the skyline `(3)`", never a bare `(3)`, which reads as an equation
  number.


## 14. Series citations and source

- Cite PE502 publications with `\pepub{PE502-N}`. Never cite one by author and year, and never
  write a bare "PE502-1" in the text.
- Cite a numbered result of an earlier PE502 report by its number:
  `\pepub[Eq.~(4.2)]{PE502-3}`, `\pepub[Thm.~4]{PE502-3}`.
- In a `.bib` file, the author of a PE502 report is `Reid, Charles`, whatever name the report's
  author line prints.
- Cite the problem statement as `\parencite{PE502}` (projecteuler.net/problem=502).
- No wiki pages, from the castles wiki or from charlesreid1.com: read what the wiki page cites
  and cite that. A report never mentions the wiki, divisions or its sidecar app.
- Record sequences that are not in the OEIS in the private notes file `PE502-N/oeis.md`.
- `\series` and `\reportnumber` each sit on one line.


# Checklist before handing in a draft

Run these from the repository root and fix every hit (`R` is the report folder). A hit on
"above" is fine only when it points at the display just before the sentence.

```sh
R=PE502-N
grep -nE 'neighbour|colour|labell|centre|behaviour' $R/$R.tex
grep -nE 'cite\{OEIS|OEIS Foundation|not (found )?in the OEIS' $R/$R.tex
grep -nwE 'he|she|his|her' $R/$R.tex
grep -nE '(from|formula|function|equation|result) above|as before|earlier|previously|the (first|second|third) (equation|formula|generating function)' $R/$R.tex
```

For a PE502 report, also run these. A hit on `F(w,h)` is fine only in the one sentence that
relates `A^e(w,h)` to PE502-1. Every hit on the last three is wrong (section 12).

```sh
grep -nE 'cite\{PE502-' $R/$R.tex
grep -nE '(^|[^{])PE502-[0-9]' $R/$R.tex
grep -nE 'F\(w, ?h\)' $R/$R.tex
grep -niE 'exact(ly)?[- ~]+height|height[- ~]+(of[ ~]+)?exactly' $R/$R.tex
grep -nE 'height (at most|up to) \$?2|height \$\\le ?2' $R/$R.tex
grep -nE '(golden|silver|bronze) ratio|requir(e|ed|ing) the ceiling|are not castles' $R/$R.tex
```

Then:

- `make build R=PE502-N` finishes with no undefined references or citations and no overfull
  boxes, and every figure looks right in the PDF.
- Every symbol is defined where it first appears, and every count in the text matches a
  computation.
- Equations are numbered within sections, every equation a later step uses has a number, every
  back-reference is spelled out with its type, and the OEIS entries in the reference list link
  back to the text.
- The main results are stated in the Introduction, and a technical report ends with a
  Conclusion whose results each carry a pointer.
- No revision removes a figure, table or worked example.
- Read each section once: it follows one line of argument, and every object it introduces is
  used on the main line.
