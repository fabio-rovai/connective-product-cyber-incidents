# Source-Quality Grading Rubric (CPCID)

This rubric operationalises the six dimensions of the UK **Government Data Quality Framework** into a tiered evidence hierarchy and a scoring procedure for grading every source cited in the Connective Product Cyber Incidents Dataset (CPCID). It exists so that any claim in the dataset can be traced to a source, and every source can be graded for reliability on a consistent, auditable basis.

Reference: The Government Data Quality Framework, GOV.UK, https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework

The Framework adopts the DAMA-UK six data-quality dimensions. It also states that perfect data quality is not always achievable and that the dimensions most aligned with the user need should be prioritised, with trade-offs declared transparently. This rubric follows that instruction: for an incident dataset built from public reporting, the load-bearing dimensions are **accuracy**, **validity** and **timeliness**, and this rubric weights them accordingly.

---

## 1. The evidence hierarchy (tiers)

Each source is assigned exactly one tier. Where a claim is supported by sources at more than one tier, grade the claim at the highest (most reliable) tier that fully supports it, and record the corroborating lower-tier sources.

| Tier | Label | Examples | Base reliability |
|------|-------|----------|------------------|
| T1 | Peer-reviewed / statutory-standard | Peer-reviewed papers; formal standards (ETSI EN 303 645); statutory instruments | Highest |
| T2 | Official government / national agency | NCSC, DSIT, CISA, ENISA, CERT-FR, NSA, FBI/DOJ advisories and annual reviews; NVD/CVE records; CISA KEV | High |
| T3 | Vendor threat report / vendor PSIRT | Mandiant, Volexity, Dragos, Cloudflare, Akamai, Talos, Binarly, ESET; vendor security advisories | Moderate |
| T4 | Grey literature | Industry surveys, consultancy reports, think-tank notes, conference talks, technical gists | Low to moderate |
| T5 | News / secondary reporting | Trade and mainstream press, encyclopaedic aggregations (used only where they consolidate primary sources) | Low |

Note on tier assignment: a vendor PSIRT advisory that discloses the vendor's own product vulnerability is T3, but a **CVE/NVD record or a CISA KEV listing** for that same vulnerability is T2, because it is a national-agency artefact of confirmed exploitation. Prefer the T2 artefact when grading the vulnerability claim.

---

## 2. The six dimensions, operationalised

Each source and each claim is scored 0 to 2 on each dimension (0 = fails, 1 = partial, 2 = met). Definitions below are the CPCID interpretation of the Government Data Quality Framework dimensions.

### Completeness
Does the source fully document the incident on the fields the dataset records (what happened, vector, product, impact, attribution)? A source that names the CVE but not the vector scores 1.

### Uniqueness
Is the source a distinct, non-duplicated origin of the claim, or is it re-reporting another source without adding evidence? Score 2 for a primary source; 1 for a secondary source that adds analysis; 0 for a pure re-post that would double-count if treated as independent corroboration.

### Validity
Is the claim expressed in a form that conforms to the dataset's code frame (a real CVE identifier of correct format, a tech_group in the controlled set, a dated event)? A fabricated or malformed CVE, or a tech_group outside the taxonomy, fails validity. Where no CVE exists (for example default-credential or living-off-the-land incidents), the correct valid value is `none`, not an invented identifier.

### Accuracy
Do the specific figures and attributions match what the cited source actually says at the cited URL? Accuracy is the dimension most often lost through drift: a headline figure quoted from memory, a contested attribution stated as settled, or an extrapolation presented as a measurement. Any figure that cannot be reproduced from the source scores 0 and must be flagged `not_corroborated` in the dataset.

### Consistency
Is the claim consistent with the rest of the corpus and with itself across fields? For example, the `year` field, the `impact_summary` and the source should not disagree on when an incident occurred; attribution language should be consistent between `impact_summary` and `confidence`.

### Timeliness
Is the source dated, and is it the most current authoritative account? Threat intelligence ages quickly (victim counts, patch status, attribution all revise). Every source carries a publication date; where a later authoritative source supersedes an earlier figure, grade against the later one and note the revision.

---

## 3. Scoring procedure

1. Assign the tier (Section 1).
2. Score the six dimensions 0 to 2 (Section 2). Maximum raw score 12.
3. Compute a weighted quality score. For this dataset, accuracy, validity and timeliness carry double weight (they are the user-need-critical dimensions for incident data), giving a weighted maximum of 18:

   `weighted = completeness + uniqueness + (2 x validity) + (2 x accuracy) + consistency + (2 x timeliness)`

4. Map to a confidence flag used in `data/incidents.csv` (`confidence` column):

   | Weighted score | Tier floor | Dataset confidence |
   |----------------|-----------|--------------------|
   | 15 to 18 | T1 or T2 | `high` |
   | 10 to 14 | T2 or T3 | `medium` |
   | below 10, or any single-source T4/T5 headline figure | any | `low` |

5. Apply the override rules:
   - Any figure that is an **extrapolation or back-of-envelope estimate** (for example a records-times-cost multiplier) is capped at `low` regardless of score, and the underlying computation is stated.
   - Any **contested attribution** (actor label disputed across sources) is capped at `medium` for the attribution claim, and the dataset states the disputed and the confirmed label explicitly.
   - A claim carried only by a **single T3, T4 or T5 source** with no independent corroboration cannot exceed `medium`.

---

## 4. Worked examples from this dataset

- **Ivanti mass exploitation (CPCID-001).** Primary source CISA AA24-060B (T2), corroborated by Mandiant (T3) and NCSC (T2). Figures (1,700+ compromised appliances) reproduce from the source. High on accuracy, validity, timeliness. Dataset confidence: `high`.
- **MOVEit financial impact (CPCID-005).** The 93 to 95 million individuals figure is well sourced (T2 plus consolidated reporting), but the monetary total is an extrapolation using a per-record multiplier. Per the override rule, the monetary figure is capped and the dataset states the defensible range (approximately 6.5 to 10 billion USD) and records that the 12 billion USD figure is not corroborated. Incident confidence `high`; the specific cost figure is flagged in text.
- **MidnightEclipse attribution (CPCID-004).** Confirmed actor label is UTA0218 (Volexity, T3). A Volt Typhoon link was raised only as a low-confidence hypothesis. Per the contested-attribution override, the dataset records `not_corroborated` for the state-actor link and states UTA0218 is the confirmed label. Incident confidence `high`; the Volt Typhoon claim is explicitly not corroborated.
- **Aisuru 29.7 Tbps (CPCID-008).** Single-vendor telemetry (Cloudflare, T3) with no published margin of error. Directionally sound but not a national statistic. Dataset confidence: `medium`.

---

## 5. How to use this rubric when contributing

When proposing a new incident or figure (see `README.md`), state for each claim: the source URL, its tier, the six-dimension scores, the resulting weighted score, and the confidence flag. Contributions that assert a figure without a reproducible source at the cited URL will not be merged. This mirrors the discipline the dataset itself follows: no claim without a source, no source without a grade.
