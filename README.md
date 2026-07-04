# Connective Product Cyber Incidents Dataset (CPCID)

An open, machine-readable dataset of documented cyber incidents affecting **connective products**, with a source-quality grading rubric. Every incident and every figure traces to a cited primary or authoritative source.

Maintained by **The Tesseract Academy** (Kampakis and Co Ltd), a UK research and data-science practice. Full write-up: [Cyber Incidents Affecting Connective Products](https://gov.tesseract.academy/research/connective-product-cyber-incidents), part of the [Tesseract Foundational Research](https://gov.tesseract.academy/research) programme.

Licence: dataset released under **CC-BY-4.0** (see `LICENSE`).

---

## The gap this fills

There is no open, structured, longitudinal dataset of cyber incidents affecting connective products. The evidence exists, but it is scattered across national-agency advisories (NCSC, CISA, ENISA, CERT-FR), vendor threat reports (Mandiant, Volexity, Dragos, Cloudflare, Akamai) and news reporting, in prose, with inconsistent definitions, no shared identifiers, and no consistent grading of source reliability. Analysts who need to reason about *which product classes are targeted, by what vector, with what impact* must reconstruct that picture by hand each time.

CPCID assembles a curated core of well-documented incidents into a single machine-readable record with:

- one row per incident, with a stable identifier;
- a controlled technology-group and vulnerability-type taxonomy (SKOS);
- an explicit confidence flag on every incident;
- honesty caveats preserved inline (contested attributions, uncorroborated figures, incidents with genuinely no CVE);
- a documented rubric for grading source quality against the Government Data Quality Framework.

It is deliberately small and curated rather than large and noisy. The value is provenance and honesty, not volume.

---

## Scope

**In scope.** Incidents 2021 to 2025 across five connective-product technology groups:

| Tech group (code) | Definition |
|-------------------|------------|
| `IoT` | Internet-connectable consumer and enterprise devices (SOHO routers, IP/CCTV cameras, DVRs, NAS, VoIP, smart products) |
| `OT` | Operational technology / industrial control systems (PLCs, HMIs, DCS, UPS, building automation, heating controllers) |
| `computing_devices` | General computing hardware and low-level layers (hypervisors, UEFI/BIOS firmware) |
| `networking_equipment` | Internet-facing network and edge appliances (routers, switches, firewalls, VPN/SSL-VPN gateways, NAC) |
| `software_firmware` | Software and firmware components embedded in or serving connective products, including open-source dependencies, commercial software and AI/ML components |

**Out of scope (deliberately excluded).** Medical devices; apps and app stores. See `BUILD_REPORT.md`.

---

## Files

```
data/incidents.csv        One row per incident (16 incidents). Human- and machine-readable.
data/incidents.jsonld     The same records as JSON-LD, with an inline @context.
taxonomy/cpcid.ttl        SKOS concept scheme: 5 technology groups + vulnerability-type vocabulary.
RUBRIC.md                 Source-quality grading rubric (Government Data Quality Framework).
BUILD_REPORT.md           Honest account of what is and is not in the dataset, and the data gaps.
scripts/validate.py       Validates the CSV, JSON-LD and Turtle. Prints PASS/FAIL.
LICENSE                   CC-BY-4.0.
CITATION.cff              Citation metadata.
```

### CSV columns

`id, name, year, tech_group, vendor_or_product, cve, vector, impact_summary, impact_quantified, uk_relevance, source_url, confidence`

- `cve` is semicolon-separated, or `none` where no CVE applies (for example default-credential or living-off-the-land incidents).
- `impact_quantified` gives a corroborated figure, or `not_corroborated` where no reliable quantified impact exists.
- `confidence` is one of `high`, `medium`, `low`, derived via the rubric.

Incident identifiers are also minted as URIs under `https://data.tesseract.academy/cpcid/incident/<id>` in the JSON-LD.

---

## Related resources

The `references/` folder provides secondary context that situates the incident dataset within the wider public evidence base. These are supporting material, not the primary artifact (which remains the incidents dataset, taxonomy and rubric).

- [`references/RELATED_DATASETS.md`](references/RELATED_DATASETS.md) : the real, public datasets relevant to connective-product cyber security, grouped by the same five technology groups, with an honest note that these are lab/testbed captures and exposure indices, not real-incident registers (the gap this dataset addresses).
- [`references/BIBLIOGRAPHY.md`](references/BIBLIOGRAPHY.md) : the academic literature base, grouped by strand, within which the incident taxonomy sits, with verification flags carried through.
- [`references/POLICY_LANDSCAPE.md`](references/POLICY_LANDSCAPE.md) : a dated timeline of UK cross-government activity on connective-product security, plus the cross-department evidence gap and brief international context.

---

## Methodology

1. **Selection.** Incidents were selected on two criteria: the most commonly targeted product classes (edge VPN/firewall appliances, consumer IoT, hypervisors, ubiquitous open-source components), and the most serious consequences (confirmed critical-national-infrastructure impact, record-scale effect, or systemic supply-chain significance), with UK relevance prioritised.
2. **Sourcing.** Every incident is anchored to a primary or authoritative source (CISA, NCSC, CERT-FR, vendor PSIRT, Mandiant, Volexity, Dragos, Cloudflare, Akamai, Binarly, ESET, or an NVD/CVE record). No incident, CVE, figure or citation was invented.
3. **Grading.** Sources and figures are graded against the six dimensions of the Government Data Quality Framework using the tiered evidence hierarchy in `RUBRIC.md`, producing the per-incident `confidence` flag.
4. **Honesty controls.** Contested attributions are stated as contested (for example the MidnightEclipse actor is UTA0218, not confirmed Volt Typhoon). Extrapolated or uncorroborated figures are flagged (for example the MOVEit monetary total). Incidents that genuinely have no CVE record `none` rather than a manufactured identifier.

---

## Validate it yourself

```
pip install rdflib
python scripts/validate.py
```

This checks the CSV columns and controlled values, parses the JSON-LD as JSON, and parses the Turtle taxonomy with rdflib, then prints a PASS/FAIL summary.

---

## How to cite

> The Tesseract Academy (Kampakis and Co Ltd) (2026). *Connective Product Cyber Incidents Dataset (CPCID)*. Zenodo. DOI: 10.5281/zenodo.XXXXXXX (placeholder, to be minted on first Zenodo release).

Machine-readable citation metadata is in `CITATION.cff`.

---

## Contributing

Contributions are welcome and low-friction. You can help by:

- **proposing a new incident** that fits the scope, with a cited primary or authoritative source and a rubric grading for each claim;
- **flagging an error** in a figure, attribution or source URL (open an issue with the corrected source);
- **extending the taxonomy** with a technology-group or vulnerability-type concept, with a `skos:definition` and, where sensible, a CWE/CVE/CPE or ENISA cross-reference.

Please follow the grading discipline in `RUBRIC.md`: no claim without a reproducible source at the cited URL, and no source without a grade. Open an issue or a pull request.

Questions, corrections, or collaboration: **fabio@thetesseractacademy.com**.
