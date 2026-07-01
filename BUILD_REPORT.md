# Build Report (CPCID)

A scrupulously honest account of how the Connective Product Cyber Incidents Dataset was built: what was included, what was deliberately excluded, which figures are low-confidence or uncorroborated, and what is not yet in the dataset. This document exists so a human reviewer can check the dataset before publishing it to GitHub and Zenodo.

Built 2026-07-01 from four internal research briefings (threat-landscape trends; incidents/vectors/impacts; case studies; steering notes). Every incident and figure in the dataset traces to a source URL that already appeared in that source material. Nothing was added from the open web during the build.

---

## 1. What was included

16 incidents, one per row in `data/incidents.csv`, spanning 2021 to 2025 and all five technology groups:

- **networking_equipment (4):** Ivanti Connect Secure (CPCID-001), Fortinet FortiOS SSL-VPN (CPCID-002), Cisco ArcaneDoor + IOS XE (CPCID-003), Palo Alto PAN-OS GlobalProtect (CPCID-004).
- **software_firmware (4):** MOVEit Transfer / Cl0p (CPCID-005), XZ Utils backdoor (CPCID-006), CUPS printing vulnerabilities (CPCID-007), Log4Shell (CPCID-016).
- **IoT (3):** Aisuru botnet (CPCID-008), KV-botnet / Volt Typhoon router takedown (CPCID-009), Hikvision cameras (CPCID-010).
- **OT (3):** Unitronics PLC water-utility attacks (CPCID-011), Volt Typhoon CNI pre-positioning (CPCID-012), FrostyGoop district-heating attack (CPCID-013).
- **computing_devices (2):** ESXiArgs ransomware (CPCID-014), LogoFAIL + BlackLotus UEFI compromise (CPCID-015).

Each incident carries a primary or authoritative source URL and a rubric-derived confidence flag. All 16 come from the case-study evidence base; no incident was drawn from outside it.

**A note on CPCID-016 (Log4Shell).** The source material treats Log4Shell as a supplementary case: it was disclosed in December 2021 (just outside a strict 2022 start) but mass-exploited through 2022, with NCSC-UK co-authoring the response. It is included here because the dataset scope runs from 2021 and Log4Shell is the archetypal ubiquitous-component incident. If a reviewer requires a strict 2022-or-later disclosure window, CPCID-016 is the row to drop; the other 15 stand independently.

---

## 2. What was deliberately excluded

- **Medical devices.** Out of scope per the source brief, despite being connective products with documented incidents. Not in the dataset.
- **Apps and app stores.** Out of scope per the source brief. Not in the dataset.
- **National prevalence and cost statistics.** The DSIT Cyber Security Breaches Survey figures, NCSC incident counts, Verizon/Mandiant/ENISA vector shares, and IBM cost benchmarks are all real and cited in the source material, but they are all-cause aggregates, not per-incident records. They belong in a narrative report, not in an incident dataset keyed one-row-per-incident, so they are excluded from `incidents.csv` by design. A reviewer wanting a companion aggregates table can request one; it is not built here to avoid mixing incidence records with survey/telemetry aggregates (which the source material warns are non-additive).

---

## 3. Figures flagged low-confidence or not corroborated

The following are recorded honestly in the dataset and must be checked by the reviewer before any onward use:

- **MOVEit monetary total (CPCID-005).** The individuals-affected figure (approximately 93 to 95 million) and organisation count (2,700+) are well sourced. The monetary total is an extrapolation using IBM's per-record cost; the dataset states a defensible range (approximately 6.5 to 10 billion USD) and records that the widely-quoted 12 billion USD figure is **not corroborated** by an authoritative source. The source material separately notes a 15.8 billion USD back-of-envelope figure elsewhere; that too is an extrapolation, not a measurement, and is not asserted here.
- **MidnightEclipse actor attribution (CPCID-004).** The confirmed actor is **UTA0218** (Volexity). A Volt Typhoon / Chinese-APT link was raised only as a low-confidence hypothesis. The dataset's `impact_quantified` is `not_corroborated` and the text states UTA0218 is the confirmed label and the Volt Typhoon link is **not confirmed**.
- **Aisuru botnet figures (CPCID-008).** The 29.7 Tbps DDoS record and the 1-to-4-million infected-host estimate are single-vendor telemetry (Cloudflare) with no published margin of error. Confidence set to `medium`; treat the exact figures as indicative, not official statistics. The firmware-update-server propagation claim is researcher-reported (moderate confidence).
- **Hikvision APT41/APT10 interest (CPCID-010).** Reported, not established (moderate confidence). The incident confidence is `high` on the vulnerability and UK-policy facts, but the specific APT attribution is stated as reported.
- **FrostyGoop attribution (CPCID-013).** Dragos did not formally attribute to a nation-state; Moscow-based IPs were noted. Recorded as unattributed but Russia-linked. The router initial-access flaw has **no assigned CVE** and none was invented.
- **ESXiArgs CVE mapping (CPCID-014).** Not every victim clearly matched CVE-2021-21974; the safest characterisation is OpenSLP-exposed, unpatched or end-of-life ESXi. Both CVE-2021-21974 and the related CVE-2020-3992 are listed, with this caveat in `vector`.
- **Incidents with genuinely no CVE.** CPCID-008 (Aisuru), CPCID-009 (KV-botnet), CPCID-011 (Unitronics), CPCID-012 (Volt Typhoon) and CPCID-013 (FrostyGoop) record `cve = none`. This is correct: default-credential exploitation, end-of-life-hardware exploitation and living-off-the-land are not single-CVE events, and no identifier was manufactured.

---

## 4. What is NOT yet in the dataset

- **No per-device-type UK-only attack counts.** No public source provides a clean UK-only, per-device-type attack count or cost. The dataset does not contain one, and none should be inferred from it.
- **No margins of error on vendor telemetry.** The vendor figures referenced in some incidents (Cloudflare, Akamai, and the telemetry sources in the wider source material: Nokia, Zscaler, Forescout, Dragos, Mandiant) do not publish confidence intervals. Their figures are point estimates from proprietary sensor estates; the true error is unknown and potentially large.
- **No aggregate prevalence/cost table** (see Section 2). Deliberately omitted from an incident-keyed dataset.
- **No structured victim-organisation list.** Named downstream victims (for example Zellis, BBC, British Airways, Boots for MOVEit) appear in prose in `impact_summary` but are not modelled as separate structured entities. A future version could add a victims table.
- **No temporal event modelling.** Each incident is a single row with a `year`; multi-year campaigns (Fortinet 2022 to 2025, Ivanti follow-on flaws) are collapsed to a primary year with detail in prose.

---

## 5. The biggest data gaps (verbatim from the source material)

These are the structural limitations of the underlying evidence, quoted from the incidents/vectors/impacts briefing (source file 02), so a reviewer sees them unfiltered:

- **"No denominator. Nobody knows the true population of attacks or compromised connective products."** All figures are single-vendor telemetry, survey self-report, or incident-response caseloads, each with its own bias.
- **"Definitional drift. 'Breach', 'attack', 'incident', 'intrusion' and 'compromise' are defined differently in every report ... These are not addable."**
- **"Attribution to device class is inconsistent ... Direct comparison across product types is usually invalid."**
- **"Cost figures are dominated by outliers and self-report ... Ransom-versus-recovery-versus-lost-revenue are frequently conflated."**
- **"Survivorship and reporting bias. Under-reporting is severe ... Every prevalence number here is therefore a lower bound."**
- **"No published margins of error on the telemetry sources. Nokia, Zscaler, Forescout, Dragos and Mandiant do not publish confidence intervals ... Treat as directional."**
- **"The USD 15.8bn MOVEit and ~1-in-5-SMB-bankruptcy figures are extrapolations/secondary claims, not measured, and are flagged Low confidence throughout."**
- **"Botnet device counts (Raptor Train 200k+, Flax Typhoon 260k+) may overlap and are estimates from disruption operations, not full censuses."**

These gaps are the reason the dataset is deliberately curated and per-incident rather than an aggregate count, and the reason every row carries an explicit confidence flag.

---

## 6. Reviewer checklist before publishing

1. Spot-check three to five `source_url` values resolve and support the stated `impact_quantified`.
2. Confirm the MOVEit and MidnightEclipse honesty caveats read as intended.
3. Confirm no CVE identifier is malformed or invented (cross-check against NVD).
4. Decide whether to keep or drop CPCID-016 (Log4Shell) given the 2022 disclosure-window question.
5. Mint the Zenodo DOI and replace the placeholder in `README.md` and `CITATION.cff`.
6. Confirm the repository contains no em dash characters (a house rule; the build used commas, colons and parentheses throughout).
