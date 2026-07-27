# Benford's law in the Review panel — theory and implementation

  

---
 
## 1. What Benford's law says


In many naturally occurring collections of numbers, the **leading digit is not uniformly distributed**. You might expect each of 1–9 to lead about 11% of the time. In practice 1 leads about 30% of the time and 9 about 4.6%.

  The law states:
 

$$P(\text{first digit} = d) = \log_{10}\left(1 + \frac{1}{d}\right)$$
 

| Digit | Probability | Exact   |
| ----: | ----------: | ------- |
|     1 |      30.10% | 0.30103 |
|     2 |      17.61% | 0.17609 |
|     3 |      12.49% | 0.12494 |
|     4 |       9.69% | 0.09691 |
|     5 |       7.92% | 0.07918 |
|     6 |       6.69% | 0.06695 |
|     7 |       5.80% | 0.05799 |
|     8 |       5.12% | 0.05115 |
|     9 |       4.58% | 0.04576 |

  

These sum to exactly 1 (the sum telescopes: $\sum_{d=1}^{9} [\log_{10}(d+1) - \log_{10}(d)] = \log_{10} 10 - \log_{10} 1 = 1$).

### Why it happens  

The cleanest intuition is the **mantissa argument**. Write any positive number as $x = m \times 10^k$ where $1 \le m < 10$. The leading digit is $\lfloor m \rfloor$. If a quantity is produced by a process spanning several orders of magnitude — multiplicative growth, or amounts aggregated from many different scales — then $\log_{10} x \bmod 1$ tends towards **uniform** on $[0, 1)$.

  

If that log-mantissa is uniform, then:

  

$$P(\text{first digit} = d) = P(\log_{10} d \le \log_{10}m < \log_{10}(d+1)) = \log_{10}(d+1) - \log_{10}(d) = \log_{10}\left(1+\tfrac{1}{d}\right)$$

  

The span from 1 to 2 occupies 30% of a logarithmic decade; the span from 9 to 10 occupies 4.6%. That is the whole law.

  

### Scale invariance

  

Benford is the **unique** distribution invariant under a change of units. If a set of figures follows Benford in pounds, it follows Benford in euros, in thousands, or in cents. This matters here: it means the test does not care what currency or presentation scale a filing uses. It is also the deep reason the law shows up so often — any "natural" law of leading digits that does not depend on arbitrary human units must be this one.

  

### Where it does *not* apply

  

Benford needs figures free to range across magnitudes. It fails, legitimately, for:

  

- **Bounded or assigned numbers** — VAT rates, page numbers, employee counts, years, phone numbers, invoice sequences.

- **Tightly clustered values** — anything with a narrow range, e.g. adult heights in cm.

- **Percentages and ratios** — bounded by construction, own distribution. *(Excluded — see §3.)*

- **Small samples** — not a failure of the law, a failure of evidence. *(§6, §9, §10.)*

  

This is why population selection matters as much as the arithmetic.

  

---

  

## 2. What the checks are actually for

  

Benford is a **screening** tool, not evidence. Fabricated or manually adjusted figures often deviate because people inventing numbers unconsciously spread leading digits too evenly, or cluster them below psychological thresholds. A deviation says *"the shape here is unusual, go look"*. It never says *"this is fraud"* — and in a filing, the far more common causes of deviation are entirely innocent: rounding, subtotals, small samples.

  

The UI states this explicitly above the result.

  

---

  

## 3. Choosing the population

  

**`collectReviewDocumentStats()` — `index.js`**

  

The single most consequential decision, and the one most likely to make the statistics meaningless if got wrong. The panel walks every numeric fact in the open filing and applies these rules:

  

| Rule | Decision | Reasoning |

|---|---|---|

| **All periods** | Included | Comparatives are real figures from the same preparation process, printed in the same document. Restricting to the current year roughly halved the sample for no analytical gain. |

| **Untagged figures** | Included | Synthetic untagged facts are real monetary amounts recovered from the filing's own tables (detailed trading statements). Excluding them discarded exactly the sample the test needs. |

| **Sign** | Magnitudes (`Math.abs`) | Benford works on magnitudes, and sign in a filing is largely presentational — brackets denote costs. A loss of `(2,514)` is a valid observation of leading digit 2. |

| **Percentages / ratios** | Excluded | Bounded by construction; they follow their own distribution and would distort the digits. Detected by `isRatioLikeFact()` — `index.js`. |

| **Dimensional breakdowns** | Excluded | A tagged fact carrying dimensions restates a total that is already counted; including both double-weights one underlying amount. |

| **Zero / unparsable** | Excluded | No leading digit. |

| **Duplicates** | Excluded per period | Keyed on `period + magnitude`. The same amount repeated *within* a period restates one figure (a P&L total also appearing in a note); the same amount in *two* periods is two genuine observations. |

  

The panel reports every exclusion under the result (`reviewSampleReductionNote()` — `index.js`), because a document with 365 figures yielding a sample of 118 otherwise reads as a bug.

  

---

  

## 4. Counting the digits

  

**`firstSignificantDigit()` — `benford.js`**

  

Normalises any magnitude into $[1, 10)$ by repeated division/multiplication, then takes the floor:

  

```js

let n = Math.abs(value);

while(n >= 10) n /= 10;

while(n < 1) n *= 10;

return Math.floor(n);

```

  

This is deliberately not `String(value)[0]` — that breaks on `0.045` (leading digit 4, not 0), on exponential notation, and on negatives.

  

`benfordDigitCounts()` (`benford.js`) tallies these into a 9-element array.

  

---

  

## 5. MAD — the descriptive statistic

  

**`benfordMad()` — `benford.js`**

  

Mean absolute deviation between observed and expected proportions:

  

$$\text{MAD} = \frac{1}{9}\sum_{d=1}^{9} \left| \hat{p}_d - p_d \right|$$

  

where $\hat{p}_d$ is the observed proportion and $p_d$ the Benford proportion. It is a plain average distance — easy to read, and it has **no built-in sense of sample size**. That last point is the crux of everything below.

  

### The Nigrini bands, and why they are not the verdict

  

**`MAD_CONFORMITY` — `benford.js`**

  

Forensic accounting's standard reference (Nigrini) gives fixed cutoffs:

  

| MAD | Band |

|---|---|

| ≤ 0.006 | Close conformity |

| ≤ 0.012 | Acceptable |

| ≤ 0.015 | Marginal |

| > 0.015 | Non-conforming |

  

**These are calibrated on large transaction datasets — thousands to millions of records — and take no account of $N$.** Applied to a filing they are actively misleading, for the reason set out next. They are retained in the code as `mad_band` because they are the familiar reference, but they never drive the verdict, and both the AI prompt and payload instruction tell the model explicitly to ignore them.

  

---

  

## 6. The noise floor — the number that makes MAD readable

  

**`expectedMadUnderNull()` — `benford.js`**

  

A small sample deviates from Benford *even when it fits perfectly*, purely from random sampling. So the question is never "is MAD large?" but **"is MAD larger than chance alone would produce at this sample size?"**

  

### Derivation

  

For digit $d$, the observed count is $\text{Binomial}(N, p_d)$, so the observed proportion has standard error:

  

$$\sigma_d = \sqrt{\frac{p_d(1-p_d)}{N}}$$

  

Approximating each binomial as normal, $\hat{p}_d - p_d \sim N(0, \sigma_d^2)$. The mean absolute value of a zero-centred normal is $\sigma\sqrt{2/\pi}$. Therefore:

  

$$\mathbb{E}[\text{MAD}] \approx \frac{1}{9}\sum_{d=1}^{9} \sqrt{\frac{2}{\pi}} \cdot \sqrt{\frac{p_d(1-p_d)}{N}}$$

  

**A subtlety worth recording:** the nine digit counts are multinomial, so they are *negatively correlated* (they must sum to $N$). That correlation is irrelevant here — by **linearity of expectation**, the mean of a sum is the sum of the means regardless of dependence. The only approximation is the normal-for-binomial step. If we ever needed the *variance* of the MAD, correlation would matter and this shortcut would not hold.

  

Note the $1/\sqrt{N}$ scaling: **quadrupling the sample halves the noise floor.**

  

### The floor by sample size

  

| N | Noise floor | vs Nigrini's 0.015 |

|---:|---:|---|

| 25 | 0.0470 | 3.1× above |

| 50 | 0.0332 | 2.2× above |

| 110 | 0.0224 | 1.5× above |

| **118** | **0.0216** | **1.4× above** |

| 250 | 0.0149 | just below |

| 500 | 0.0105 | below |

| 1,000 | 0.0074 | below |

| 5,000 | 0.0033 | below |

| 10,000 | 0.0023 | below |

  

**This is the bug the current implementation exists to fix.** Below ~246 figures, perfectly Benford data scores worse than 0.015 on average, so a fixed-cutoff verdict labels it non-conforming *no matter how well it fits*. The minimum sample for each band to be reachable at all:

  

| Band | Cutoff | Minimum N for the band to be attainable |

|---|---|---|

| Marginal | 0.015 | 246 |

| Acceptable | 0.012 | 384 |

| Close | 0.006 | 1,533 |

  

A UK small-company filing yields tens to low hundreds of figures. It can essentially never reach "close conformity", and will usually be branded non-conforming on arithmetic alone.

  

### `mad_ratio`

  

The panel reports `mad / expected_mad`. **A ratio near 1 means the deviation is entirely explained by sampling noise.** This is the single most interpretable number in the output, and it works at any sample size — including those too small for a formal test.

  

---

  

## 7. Chi-square — the actual test

  

**`benfordChiSquare()` — `benford.js`**

  

Pearson's goodness-of-fit statistic:

  

$$\chi^2 = \sum_{d=1}^{9} \frac{(O_d - E_d)^2}{E_d}, \qquad E_d = N \cdot p_d$$

  

Each term measures squared error scaled by how much error that cell should show — so a shortfall of 3 in a cell expecting 5 counts far more than the same shortfall in a cell expecting 500. **This is what makes chi-square sample-size aware where MAD is not.**

  

### Degrees of freedom = 8

  

**`BENFORD_DF` — `benford.js`**

  

There are 9 categories. The counts must sum to $N$, which is one linear constraint, so only 8 can vary freely: $\text{df} = 9 - 1 = 8$.

  

No further reduction applies. Degrees of freedom are also reduced by each parameter *estimated from the data*, but the Benford proportions are fixed a priori by theory — nothing is fitted. So it stays at 8.

  

### Validity: expected count ≥ 5

  

**`MIN_EXPECTED_PER_CELL` and `MIN_BENFORD_SAMPLE` — `benford.js`**

  

The chi-square distribution is an *approximation* to the true discrete sampling distribution, and it degrades when expected cell counts are small. The standard (Cochran) rule is every expected count ≥ 5.

  

The binding constraint is the rarest digit, 9, at $p_9 = 0.04576$:

  

$$N \ge \frac{5}{0.04576} = 109.27 \quad\Rightarrow\quad N \ge 110$$

  

This is **derived in code, not hardcoded**, so the rule and the number cannot drift apart:

  

```js

export const MIN_BENFORD_SAMPLE = Math.ceil(

MIN_EXPECTED_PER_CELL / Math.min(...FIRST_DIGIT_PROBS)

);

```

  

The same derivation applied to the second-digit test gives 59, because its rarest cell is far commoner (8.50%).

  

Below 110 the panel does **not** give up — it switches to a Monte Carlo p-value (§9), which makes no asymptotic assumption. Only below 10 figures is no verdict offered at all.

  

This replaced an arbitrary threshold of 50, which had no derivation behind it.

  

---

  

## 8. The p-value

  

**`chiSquarePValue()` — `benford.js`**

  

The p-value is the upper-tail probability: **given that the data really do follow Benford, how likely is a $\chi^2$ this large or larger?** Small p means the observed pattern would be surprising under Benford.

  

### How it is computed

  

$$P(X > x) = Q\!\left(\frac{\text{df}}{2}, \frac{x}{2}\right)$$

  

where $Q(s, x)$ is the **regularised upper incomplete gamma function**. The implementation uses the standard approach: a series expansion where $x < s+1$ (converging quickly there) and a continued fraction elsewhere, evaluated by the modified Lentz method, with a Lanczos approximation for $\log \Gamma$. No third-party statistics library.

  

> **Why not the even-df closed form?** An earlier version exploited the fact that a chi-square with *even* df $2m$ is an Erlang distribution, whose survival function is elementary:

> $$Q(x; 2m) = e^{-x/2} \sum_{i=0}^{m-1} \frac{(x/2)^i}{i!}$$

> That is exact and neat, but it only works for even df. The second-digit test needs **df = 9**, and the power calculation needs **fractional** df, so the general function replaced it. The closed form is now just a special case of what `regularizedGammaQ` computes.

  

### Verified against published critical values

  

Both df the panel uses, checked against published tables:

  

| $\chi^2$ | df | Published p | Implementation |

|---:|---:|---:|---:|

| 13.362 | 8 | 0.100 | 0.09999 |

| 15.507 | 8 | 0.050 | 0.05001 |

| 20.090 | 8 | 0.010 | 0.01000 |

| 26.125 | 8 | 0.001 | 0.00100 |

| 14.684 | 9 | 0.100 | 0.09999 |

| 16.919 | 9 | 0.050 | 0.05000 |

| 21.666 | 9 | 0.010 | 0.01000 |

| 27.877 | 9 | 0.001 | 0.00100 |

  

Asserted in `test/benford.test.js`.

  

### Verdict bands

  

**`benfordVerdict()` — `benford.js`**

  

| p-value | Verdict | Label | Colour |

|---|---|---|---|

| ≥ 0.05 | `conforms` | Consistent with Benford | green |

| 0.01 – 0.05 | `marginal` | Unclear | orange |

| < 0.01 | `nonconforming` | Inconsistent with Benford | red |

  

Anything the test cannot answer — sample below 110, or no figures — also shows **orange**. Silence on a check like this must not look like a pass.

  

### Two things a p-value is not

  

1. **It is not the probability that the filing is fine.** It is $P(\text{data} \mid \text{Benford true})$, not $P(\text{Benford true} \mid \text{data})$. Inverting those is the standard misreading.

2. **"Consistent" is failure to reject, not proof.** A small sample fails to reject almost anything. That is why the noise floor and ratio are shown alongside — they say *how much power the test actually had*.

  

There is also a known failure mode in the opposite direction: at very large $N$, chi-square detects deviations far too trivial to care about, which is precisely why Nigrini favoured MAD for big datasets. Filings never approach those sizes, so chi-square is the right tool *here* — but the choice is scale-dependent, not universal.

  

---

  

## 9. Monte Carlo — a verdict below the asymptotic threshold

  

**`monteCarloPValue()` — `benford.js`**

  

Declining to answer below 110 figures was safe but unhelpful: plenty of small-company filings sit under it. The chi-square *approximation* fails there, but the underlying question is still answerable — by simulating the exact null distribution rather than approximating it.

  

### The method

  

1. Take the observed statistic $\chi^2_{obs}$.

2. Draw 20,000 samples of the **same size $N$** from the expected digit distribution.

3. Compute $\chi^2$ for each simulated sample.

4. The p-value is the fraction of simulations at least as extreme as the observation.

  

This is a **permutation-style exact test**. It makes no distributional assumption at all — it *is* the sampling distribution, constructed by brute force. It is therefore valid at any $N$, though it cannot manufacture power that a small sample does not have.

  

### Two implementation details that matter

  

**Determinism.** Findings are cached and shown as deterministic, so a filing must not produce a different p-value on each render. The generator is a seeded `mulberry32`, with the seed derived by FNV-style hashing of the observed counts and total. Same filing → same seed → same p-value, every time.

  

**The add-one correction.** The p-value is computed as:

  

$$p = \frac{(\text{simulations at least as extreme}) + 1}{(\text{iterations}) + 1}$$

  

Without the $+1$, a run where no simulation exceeds the observation reports $p = 0$ — which no finite simulation can ever justify. The correction bounds the smallest reportable value at $1/20001$.

  

### Cross-validation

  

Where both methods are valid they should agree, and on the WEXAS filing they do:

  

| Method | p-value |

|---|---|

| Asymptotic chi-square | 0.1626 |

| Monte Carlo (20,000 runs) | 0.1580 |

  

Asserted as a test — agreement within 0.02 — which validates both implementations against each other.

  

### Thresholds

  

| Sample size | Method | Field `p_value_method` |

|---|---|---|

| ≥ 110 | Asymptotic chi-square | `chi-square` |

| 10 – 109 | Monte Carlo | `monte-carlo` |

| < 10 | No verdict | `null` |

  

The UI names the method whenever it is Monte Carlo, because "p = 0.16 by simulation on 40 figures" is a materially weaker claim than the same number from a well-powered test.

  

---

  

## 10. Statistical power — what the test could actually catch

  

**`powerAtEffect()`, `minimumDetectableEffect()` — `benford.js`**

  

This closes the most serious gap in the old output. A verdict of "Consistent with Benford" was easily read as *"the figures are fine"*, when it often meant *"this sample is too small to tell"*. Those are entirely different statements and the panel could not distinguish them.

  

**Power** is the probability of correctly rejecting the null when the data really are distorted. It depends on sample size, significance level, and how large the distortion is.

  

### Effect size

  

Distortion is measured by **Cohen's** $w$:

  

$$w = \sqrt{\sum_d \frac{(q_d - p_d)^2}{p_d}}$$

  

where $q$ is the true (distorted) distribution and $p$ is Benford. The chi-square statistic under that alternative follows a **noncentral** chi-square with noncentrality:

  

$$\lambda = N w^2$$

  

### Computing power

  

The noncentral chi-square CDF has no elementary form, so the implementation uses **Patnaik's approximation**: match the mean and variance of the noncentral distribution with a *scaled central* one.

  

$$\nu = \frac{(\text{df}+\lambda)^2}{\text{df}+2\lambda}, \qquad c = \frac{\text{df}+2\lambda}{\text{df}+\lambda}$$

  

$$P(\chi^2_{nc} > x) \approx Q\!\left(\frac{\nu}{2}, \frac{x}{2c}\right)$$

  

Note $\nu$ is generally **fractional** — which is exactly why the general incomplete-gamma function was needed and the even-df closed form had to go.

  

Power is then $P(\chi^2_{nc} > \chi^2_{crit})$, and `minimumDetectableEffect()` bisects on $w$ to find the smallest effect reaching 80% power at $\alpha = 0.05$.

  

### Making it readable

  

Cohen's $w$ means nothing to an accountant, so it is translated into a concrete distortion. For an alternative that inflates one digit's share by $\delta$ and shrinks the rest proportionally, the algebra collapses neatly:

  

$$w^2 = \frac{\delta^2}{p} + \frac{\delta^2}{1-p} = \frac{\delta^2}{p(1-p)} \quad\Rightarrow\quad \delta = w\sqrt{p(1-p)}$$

  

giving a percentage-point excess on a single digit.

  

### What this means in practice

  

| N | Min detectable $w$ | As excess on digit 1 |

|---:|---:|---:|

| 118 | 0.356 | **16.3 pp** |

| 500 | 0.173 | 7.9 pp |

| 2,000 | 0.087 | 4.0 pp |

  

Detectable effect scales as $1/\sqrt{N}$: quadrupling the sample halves it (asserted as a test).

  

**At 118 figures, digit 1's share would have to be inflated by about 16 percentage points — from 30% to 46% — before this test would reliably notice.** That is a very large distortion. It is the honest counterweight to a green verdict, and the panel now states it:

  

> *At this sample size the test would catch a distortion of roughly 16 percentage points on a single digit 80% of the time. Smaller distortions than that could pass unnoticed, so a clean result is not proof the figures are sound.*

  

---

  

## 11. The second-digit test

  

**`secondDigitExpected()`, `secondSignificantDigit()` — `benford.js`**

  

An independent test on the same figures, standard in forensic practice. Benford's law extends beyond the leading digit:

  

$$P(D_2 = d) = \sum_{k=1}^{9} \log_{10}\left(1 + \frac{1}{10k + d}\right)$$

  

summing over the decade each first digit contributes.

  

| Second digit | Probability |

|---:|---:|

| 0 | 11.968% |

| 1 | 11.389% |

| 2 | 10.882% |

| 3 | 10.433% |

| 4 | 10.031% |

| 5 | 9.668% |

| 6 | 9.337% |

| 7 | 9.035% |

| 8 | 8.757% |

| 9 | 8.500% |

  

### Why it is worth running

  

- **Much flatter.** The commonest cell is only 1.4× the rarest, against 6.6× for the first digit. That flatness means the ≥5 rule binds far sooner: **59 figures instead of 110**, so it often produces a verdict where the first-digit test cannot.

- **Sensitive to different distortions.** Rounding shows up as an excess of **0s and 5s** in the second digit while barely touching the first. A filing rounded to the nearest thousand distorts here first.

- **Genuinely independent evidence.** Different statistic, different degrees of freedom, same underlying figures.

  

### Details

  

- **df = 9** (ten categories minus one constraint). This is what forced the general incomplete-gamma implementation.

- **`secondSignificantDigit`** works on the mantissa, not the written string: `0.045` → 5, `1234` → 2, `46641579` → 6.

- **A value with one significant digit reads as 0** — `7` is `7.0`, so its second digit is 0. This inflates digit 0 for heavily rounded figures. That is *informative rather than a defect*: it is exactly the rounding signal the test is meant to surface. Worth remembering when reading an excess of 0s.

  

On the WEXAS filing: $\chi^2 = 9.3$ on 9 df, **p = 0.41** — consistent, and independently corroborating the first-digit result.

  

---

  

## 12. Worked example — WEXAS LIMITED, period ending 2019-12-31

  

Sample: **118** figures, drawn from 365 in the document (155 dimensional breakdowns, 86 within-period duplicates, 8 percentages and 6 zero/unreadable excluded).

  

| Digit | Observed | Expected | Contribution to $\chi^2$ |

|---:|---:|---:|---:|

| 1 | 34 | 35.5 | 0.065 |

| 2 | 21 | 20.8 | 0.002 |

| 3 | 13 | 14.7 | 0.206 |

| 4 | 15 | 11.4 | 1.111 |

| 5 | 6 | 9.3 | 1.196 |

| 6 | 15 | 7.9 | **6.382** |

| 7 | 5 | 6.8 | 0.496 |

| 8 | 7 | 6.0 | 0.154 |

| 9 | 2 | 5.4 | 2.140 |

| | | **total** | **11.753** |

  

| Statistic | Value | Reading |

|---|---|---|

| MAD | 0.0223 | meaningless alone |

| Noise floor at N=118 | 0.0216 | what a perfect fit would score |

| **Ratio** | **1.03** | deviation is 3% above pure chance |

| $\chi^2$ (8 df) | 11.753 | — |

| **p-value** | **0.163** | not remotely significant |

| **Verdict** | **Consistent with Benford** | green |

  

Under the old fixed bands this filing was reported **"Non-conforming"** — on a MAD of 0.0223 against a noise floor of 0.0216. It was being flagged for deviating by 3% more than random chance produces.

  

Note that digit 6 alone contributes over half the statistic (15 observed against 7.9 expected). Even so, the total does not approach significance — which is exactly what the test is for. Eyeballing one conspicuous bar in the chart will mislead you; that is why the chart is presented next to a test rather than on its own.

  

---

  

## 13. Output reference

  

`analyzeBenford()` returns:

  

| Field | Meaning |

|---|---|

| `sample_size` | Figures used, after all exclusions |

| `sufficient` | Whether **any** verdict was produced (asymptotic or Monte Carlo) |

| `asymptotic_valid` | Whether `sample_size >= min_sample`, i.e. chi-square is trustworthy |

| `min_sample` | Derived threshold for the asymptotic test (110) |

| `df` | Degrees of freedom (8) |

| `mad` | Mean absolute deviation |

| `expected_mad` | Noise floor at this sample size |

| `mad_ratio` | `mad / expected_mad`; ~1 = indistinguishable from a perfect fit |

| `mad_band` | Nigrini band — **reference only, never the verdict** |

| `chi_square` | Test statistic |

| `p_value` | Upper-tail probability; `null` when untestable |

| `p_value_method` | `chi-square` / `monte-carlo` / `null` |

| `verdict` | `conforms` / `marginal` / `nonconforming` / `null` |

| `verdict_label` | Display string |

| `digits[]` | Per-digit count, observed and expected proportion |

| `power.min_detectable_w` | Cohen's $w$ detectable at 80% power |

| `power.min_detectable_digit_shift` | The same, as a single-digit excess |

| `power.alpha` / `power.target` | 0.05 / 0.8 |

| `second_digit` | Independent second-digit test — same shape, `df` 9, own `min_sample` (59), own verdict and power |

| `note` | Explanation when Monte Carlo was used, or no test was possible |

  

Consumed by the UI in `reviewDataQualitySection()` (`index.js`) and passed to the AI as `supplied_review_findings.benford`. The AI payload instruction and the anomaly-detection prompt both tell the model to name the p-value method, to quote the power figure whenever the verdict is `conforms`, to report `second_digit` separately, and to ignore `mad_band`.

  

---

  

## 14. Limitations

  

- **A pass is weak evidence, and the panel now quantifies how weak.** At 118 figures only a ~16 percentage-point distortion would be reliably caught. It is a screen, not an audit.

- **Filings are not transaction data.** Statements are full of subtotals, roll-ups and derived sums, which are not independent draws from one generating process. Benford's assumptions are only approximately met, which argues for treating *any* filing-level result cautiously in both directions.

- **Units are mixed.** The sample can contain a per-share figure of `0.19` alongside `46,641,579`. Mixing populations weakens the test — still open.

- **Monte Carlo cannot create power.** Below 110 figures it gives a *valid* verdict, not a *strong* one. Read it alongside the power figure.

- **Rounding.** Figures presented to the nearest £1,000 distort leading digits. The round-number check reports this, and an excess of second-digit 0s corroborates it.

- **Patnaik is an approximation.** The power figures use a mean/variance match to the noncentral chi-square. Good to a few percent in this range — fine for "roughly 16 points", not for a precise power curve.

  

---

  

## 15. Open items

  

- [ ] **Filter to monetary facts.** The population mixes per-share figures and share counts with monetary amounts. Filtering on unit (e.g. GBP) would give one homogeneous population, at the cost of some sample. Worth measuring both ways before committing.

- [ ] **First-two-digits test.** The natural next step after the second digit: 90 cells, much finer resolution, but it needs roughly 900+ figures for the ≥5 rule, so it would rarely fire on a single filing. More useful across a portfolio.

- [ ] **Use the second-digit test when the first-digit sample is too small.** Its threshold is 59 against 110, so between those sizes it can give an asymptotic verdict where the first-digit test falls back to simulation. Currently both are reported independently and the panel does not say the second is the stronger evidence there.

- [ ] **Consider a Monte Carlo power estimate.** Would replace the Patnaik approximation with a simulated one, at some cost in page-load time.

  

### Done

  

- [x] **Derive `MIN_BENFORD_SAMPLE` from `MIN_EXPECTED_PER_CELL`** — now computed as `Math.ceil(MIN_EXPECTED_PER_CELL / Math.min(...FIRST_DIGIT_PROBS))`, with the same derivation giving the second-digit threshold of 59.

- [x] **Remove the dead `LOG10` constant.**

- [x] **Add a second-digit test** — §11.

- [x] **Monte Carlo test for small samples** — §9. Cross-validated against the asymptotic test where both are valid.

- [x] **Report statistical power** — §10.

  

---

  

## References

  

- Benford, F. (1938). *The Law of Anomalous Numbers*. Proceedings of the American Philosophical Society.

- Newcomb, S. (1881). *Note on the Frequency of Use of the Different Digits in Natural Numbers*. American Journal of Mathematics. (The earlier discovery.)

- Hill, T. P. (1995). *A Statistical Derivation of the Significant-Digit Law*. Statistical Science. (The scale-invariance result.)

- Nigrini, M. (2012). *Benford's Law: Applications for Forensic Accounting, Auditing, and Fraud Detection*. Wiley. (Source of the MAD bands, and of the caution about their sample-size dependence.)