# PE 502: the Pell castle strip

## The generating function

$$D(x) \;=\; \frac{1}{1 - 2x - x^2} \;=\; \sum_{i=0}^{\infty} a_i x^i$$

## Where the recurrence comes from (and why $a_{-1}$ isn't a problem)

Matching coefficients on $(1 - 2x - x^2) D(x) = 1$:

- $[x^0]$: $a_0 = 1$
- $[x^1]$: $a_1 - 2a_0 = 0$, so $a_1 = 2$
- $[x^{n+2}]$ for $n \ge 0$: $a_{n+2} - 2a_{n+1} - a_n = 0$

The $a_n$ term doesn't "disappear" at the boundary - it multiplies $a_{-1}$, which is $0$ by convention (a power series has no negative powers). Uniformly:

$$a_n - 2a_{n-1} - a_{n-2} \;=\; [n = 0]$$

with $a_{-1} = a_{-2} = 0$. The base cases $a_0 = 1$, $a_1 = 2$ are the same recurrence evaluated at $n = 0, 1$ with those zeros substituted. Nothing special about them.

## The castle reading

$D(x) = 1/(1 - 2x - x^2)$ is a **two-atom composition scheme**. Read it as counting tilings of a $1 \times n$ strip using:

- a width-1 atom with weight $2$
- a width-2 atom with weight $1$

Then $a_n$ is the total weight of such tilings, and $a_n = 2 a_{n-1} + a_{n-2}$ is just "peel off the last atom."

Two facts from PE 502 lock this in:

1. **Unsigned tower count.** $T(k, L) = (k+1)^L$. For height-$2$ towers ($k = 1$), that's $2^L$: each column independently picks one of two states. **This is the width-1, weight-2 atom.**

2. **Rule 3, mandatory gap.** Adjacent blocks on the same row need a gap of width $\ge 1$. Bundle "block-end + start-of-mandatory-gap" as one atomic unit and its minimum width is $2$. **This is the width-2, weight-1 atom.**

So the denominator splits exactly along PE 502's structural rules:

$$\underbrace{1}_{\text{empty}} \;-\; \underbrace{2x}_{\text{per-column binary state (height-2 tower)}} \;-\; \underbrace{x^2}_{\text{mandatory-gap block+gap unit (rule 3)}}$$

Without rule 3 you'd only have the $2x$ atom, denominator $1 - 2x$, and $a_n = 2^n$ - the naive $2^L$ per-column count. **The $x^2$ term is what rule 3 costs you.** Or rather, what it buys you: the correction that turns a raw column-product into a proper castle count.

## Match with the wiki's rational recurrence

The wiki gives, for the signed castle generating function:

$$\operatorname{den}_k \;=\; \operatorname{den}_{k-1}(1 - 2x) + x \cdot \operatorname{num}_{k-1}$$

Same shape: a $(1 - 2x)$ factor (per-column binary atom) plus a smaller $x$-weighted correction (the mandatory-gap tax). $D(x)$ is the baby case of that family - the height-2, one-signed-strip castle.

## The Pell fingerprint

$$a_0, a_1, a_2, \ldots \;=\; 1, 2, 5, 12, 29, 70, 169, \ldots$$

Half-companion Pell numbers, growth rate $1 + \sqrt{2}$. That growth rate is the **cost of adding one column of a rule-3-obeying height-2 castle strip.**

## One-line takeaway

The $a_n$ term is the **castle mandatory-gap tax**. Without rule 3 the recurrence would be one-step ($a_n = 2 a_{n-1}$); rule 3 introduces a memory of length 2, which is exactly what the $+ a_n$ delivers.
