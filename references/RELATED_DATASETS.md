# Related Public Datasets

Secondary context for the Connective Product Cyber Incidents Dataset (CPCID). This document catalogues the real, public datasets that are relevant to the cyber security of connective products, grouped by the same five technology groups the incident dataset uses (`IoT`, `OT`, `computing_devices`, `networking_equipment`, `software_firmware`).

## Honest framing (read this first)

These datasets are almost all lab or testbed packet-and-flow captures, host telemetry, or vulnerability and exposure indices. They are **not** real-world incident records. They measure the *detectability of known attack patterns* on controlled testbeds, or catalogue *known and exploited vulnerabilities*, not the frequency, cost or root cause of real incidents in deployed products. Coverage of OT and firmware is thin: only a small number of datasets give genuine OT process data, and true firmware-binary datasets are scarce. Crucially, **no real-incident register indexed by connective-product class exists on Kaggle** (the closest proxies are exposure and known-exploited-vulnerability lists such as CISA KEV and Project Zero, which are aggregate/curated rather than primary-source per-incident records). That absence is exactly the gap this repository's incident dataset addresses: a curated, product-class-indexed corpus of documented incidents with provenance and confidence flags.

Method and verification notes:

- Every entry below was verified live via the Kaggle MCP (`search_datasets`, `search_competitions`, `search_notebooks`) on 2026-07-01. Owner/slug, URL and byte size are taken directly from the Kaggle API responses.
- Sizes are shown as reported by Kaggle in bytes, converted to MB/GB for readability (1 GB = 1,000,000,000 bytes, matching Kaggle's display convention).
- Where a licence or row count was not returned by the API it is marked "not stated" rather than invented. Kaggle's dataset API returns file sizes but not authoritative row counts, so row counts are given only where the owner explicitly reported them.
- Most of these are academic benchmark datasets published by research groups (Canadian Institute for Cybersecurity at UNB, UNSW Canberra / ACCS, Stratosphere Lab CTU, iTrust SUTD, and others); Kaggle hosts community-uploaded mirrors. Provenance should always be cited back to the originating research paper as well as the Kaggle mirror. Several mirrors carry "Unknown" or "Other" licences that may not match the original terms (SWaT and MQTT-IoT-IDS2020 in particular are normally gated by request forms at their origin labs), so usage rights must be verified before any onward use.

## Technology group mapping key

- **IoT**: consumer and general Internet of Things devices (cameras, doorbells, smart plugs, sensors).
- **OT**: operational technology, ICS/SCADA, industrial control (water treatment, power, manufacturing).
- **computing_devices**: hosts, endpoints, servers, memory dumps, host process telemetry, malware on machines.
- **networking_equipment**: routers, switches, flow-level network traffic, NIDS flow features.
- **software_firmware**: software vulnerabilities, CVE/CWE records, firmware/app malware, exploit catalogues.

Many datasets straddle two groups (for example an IoT botnet capture is both IoT and networking_equipment). Both the primary and secondary group are listed.

---

## Group 1: IoT (consumer / general Internet of Things)

| Dataset | Kaggle slug or canonical source | Size | Licence | Description | Tech-group mapping |
|---|---|---|---|---|---|
| CIC-IoT-2023 (UNB CIC IoT 2023) | `madhavmalhotra/unb-cic-iot-dataset` (source: UNB CIC) | ~2.98 GB | Other (specified in description); original CIC dataset is academic-use, cite UNB | Network traffic from 105 real IoT devices under 33 attacks in 7 categories (DDoS, DoS, recon, web-based, brute force, spoofing, Mirai). One of the largest, most-cited modern IoT attack datasets. | IoT (primary), networking_equipment (secondary) |
| CIC-IoT-2023 (clean Parquet mirror) | `stevemekam/cic-iot-attack-dataset-2023-clean-parquet-version` | ~926 MB | MIT | ML-ready Parquet copy of CIC-IoT-2023, highest usability (0.94). Recommended clean mirror. | IoT (primary), networking_equipment (secondary) |
| TON_IoT (network subset) | `arnobbhowmik/ton-iot-network-dataset` (source: UNSW Canberra, Nour Moustafa) | ~1.79 MB | CC BY 4.0 | IoT/IIoT network telemetry plus normal and attack traffic (scanning, DoS, DDoS, ransomware, backdoor, injection, XSS, password, MITM). Multi-modal variants exist (network, Linux/Windows host telemetry). | IoT (primary), networking_equipment and computing_devices (secondary) |
| Bot-IoT (UNSW BoT-IoT) | `vigneshvenkateswaran/bot-iot` (source: UNSW Canberra, Koroniotis et al.) | ~1.26 GB | not stated (Unknown on Kaggle; original academic-use) | Botnet traffic (DDoS, DoS, OS/service scan, keylogging, data exfiltration) generated on a realistic IoT testbed. Large flow volume. A 5% subset (`vigneshvenkateswaran/bot-iot-5-data`, ~57 MB) and a CICFlowMeter variant (`dhoogla/cicbotiot`, ~1.1 GB, CC BY-NC-SA 4.0) exist. | IoT (primary), networking_equipment (secondary) |
| N-BaIoT | `mkashifn/nbaiot-dataset` (source: UCI, Meidan et al. 2018) | ~1.88 GB | not stated (Unknown on Kaggle; original UCI/academic) | Statistical traffic features from 9 commercial IoT devices infected by Mirai and BASHLITE (Gafgyt), plus benign traffic. Classic device-level botnet-detection benchmark. | IoT (primary), networking_equipment (secondary) |
| IoT-23 (Stratosphere Lab, CTU) | `surajsooraj26/iot-23` (source: Stratosphere Lab, Avast-funded) | ~9.16 GB | CC0: Public Domain (mirror; original CC0) | Labelled malicious and benign IoT network traffic (Zeek conn.log flows and PCAPs) from 20 malware captures plus 3 benign captures. Real malware on real devices, a rare "closer to real incident" IoT dataset. | IoT (primary), networking_equipment and software_firmware (secondary) |
| RT-IoT2022 (Real-Time IoT) | `joebeachcapital/real-time-internet-of-things-rt-iot2022` (source: UCI) | ~7.64 MB | CC BY 4.0 | Cyber attacks captured from a real-time IoT infrastructure (Nmap patterns, DoS/DDoS via Hydra/SlowLoris) plus normal patterns from Amazon Alexa, ThingSpeak, MQTT devices. Clean and small. | IoT (primary), networking_equipment (secondary) |
| Multi-Protocol IoT Attack Dataset (real honeypot) | `mohamedbouzira/multi-protocol-iot-attack-dataset-realhoneypot` | ~40.9 MB | CC BY-NC 4.0 | Real-world multi-protocol IoT honeypot data (reported 2.6M events / 35K attacks). One of the few genuinely adversarial (not testbed-synthetic) IoT captures on Kaggle. | IoT (primary), networking_equipment (secondary) |
| DDoS Botnet Attack on IoT Devices | `siddharthm1698/ddos-botnet-attack-on-iot-devices` | size not stated reliably (Kaggle reports 0 bytes for current version; verify on download) | Data files (c) Original Authors | Labelled malicious/benign packets for DDoS botnet prediction on IoT devices (derived from BoT-IoT). Popular teaching dataset. | IoT (primary), networking_equipment (secondary) |
| Gotham 2025 (large-scale IoT NIDS) | `alyhaider/gotham-2025-master-csv` | ~453 MB | CC BY-SA 4.0 | Large-scale IoT network-traffic dataset for intrusion detection (from the Gotham IoT testbed). Recent (uploaded 2026), useful as a current benchmark. | IoT (primary), networking_equipment (secondary) |
| MQTT-IoT-IDS2020 (protocol-specific) | `ogunyemioluwapelumi/mqtt-iot-ids2020-private` (canonical: IEEE DataPort / Ulster University, Hindy et al.) | ~15.5 MB | not stated (Unknown on Kaggle) | MQTT-broker IoT traffic (normal plus aggressive scan, UDP scan, Sparta SSH brute force, MQTT brute force). Thinly documented mirror (usability 0.12); verify against the canonical source before citing. | IoT (primary), networking_equipment (secondary) |

---

## Group 2: OT (ICS / SCADA / industrial control)

OT is the thinnest group on Kaggle. Beyond HAI and a repackaged SWaT mirror, most ICS/SCADA benchmarks (WADI, Morris Power System, HIL/gas-pipeline SCADA) live on their originating lab portals rather than Kaggle. For OT-heavy claims, cite the primary sources.

| Dataset | Kaggle slug or canonical source | Size | Licence | Description | Tech-group mapping |
|---|---|---|---|---|---|
| HAI Security Dataset (HIL-based Augmented ICS) | `icsdataset/hai-security-dataset` (source: National Security Research Institute, Korea) | ~837 MB | CC BY-SA 4.0 | Time-series telemetry from a Hardware-In-the-Loop testbed combining a steam-turbine and a pumped-storage hydropower process, with labelled normal and attack (process-manipulation) periods. The strongest genuinely-OT dataset on Kaggle. | OT (primary) |
| SWaT (Secure Water Treatment) | `vishala28/swat-dataset-secure-water-treatment-system` (canonical: iTrust SUTD, request form) | ~106 MB | CC0: Public Domain (mirror; canonical SWaT is request-gated, treat mirror provenance with care and cite iTrust) | Sensor and actuator readings from a 6-stage water treatment testbed under normal operation and 36 attack scenarios. The most-cited ICS anomaly-detection benchmark. | OT (primary) |
| WADI (Water Distribution) | canonical only: iTrust SUTD request form (NO verified Kaggle dataset as of 2026-07-01) | not applicable | request-gated | Companion to SWaT from the same iTrust lab. No standalone verified Kaggle mirror was found; obtain directly from iTrust SUTD and do not cite a Kaggle WADI slug. | OT (primary) |
| Integrated IDPS Security 3Datasets (IIS3D) | `rogernickanaedevha/integrated-idps-security-3datasets` | ~911 MB | CC0 | Merge of CSE-CIC-IDS2018, UNB-CIC-IoT2023 and UNSW-NB15 for cross-domain intrusion detection. Not pure OT, but a multi-domain baseline that includes industrial IoT. | OT / IoT / networking_equipment (mixed) |

---

## Group 3: computing_devices (hosts / endpoints / memory / host telemetry)

| Dataset | Kaggle slug or canonical source | Size | Licence | Description | Tech-group mapping |
|---|---|---|---|---|---|
| CIC-MalMem-2022 (obfuscated malware memory) | `luccagodoy/obfuscated-malware-memory-2022-cic` (source: CIC, UNB) | ~4.03 MB | Data files (c) Original Authors | Feature breakdown of benign vs malign memory dumps, balanced across spyware, ransomware and trojan-horse families. Endpoint/host memory forensics. | computing_devices (primary), software_firmware (secondary) |
| BETH Dataset (real host kernel/process telemetry) | `katehighnam/beth-dataset` | ~41.7 MB | CC0: Public Domain | Real kernel-level process and system-call logs from honeypot hosts (over 8 million events), labelled benign vs malicious. Genuinely real host telemetry, not synthetic. Published at a NeurIPS workshop. | computing_devices (primary) |
| Microsoft Malware Prediction (competition) | `competitions/microsoft-malware-prediction` | (competition data, ~half a terabyte class fleet) | competition terms | Telemetry from ~16.8M Windows machines (Defender/endpoint properties); target is whether a machine will soon be hit by malware. Large real-endpoint-fleet dataset. Closed 2019, data still downloadable. | computing_devices (primary), software_firmware (secondary) |
| Microsoft Malware Classification Challenge (BIG 2015) | `competitions/malware-classification` | ~half a terabyte | competition terms | Byte and disassembly (.asm) files for malware across 9 families; classify malware into families. The canonical PE-malware-family dataset. Closed 2015, data still available. | computing_devices (primary), software_firmware (secondary) |

---

## Group 4: networking_equipment (flow-level NIDS / router/switch traffic)

| Dataset | Kaggle slug or canonical source | Size | Licence | Description | Tech-group mapping |
|---|---|---|---|---|---|
| UNSW-NB15 | `mrwellsdavid/unsw-nb15` (source: ACCS / UNSW Canberra, Moustafa & Slay 2015) | ~156 MB | not stated (Unknown on Kaggle; original academic) | Network-flow features (IXIA PerfectStorm) across 9 attack families (fuzzers, analysis, backdoors, DoS, exploits, generic, recon, shellcode, worms) plus normal. General NIDS benchmark; one of the most-used security datasets on Kaggle (181,670 downloads). | networking_equipment (primary) |
| NSL-KDD | `hassan06/nslkdd` (source: UNB, Tavallaee et al. 2009) | ~14.5 MB | not stated (Unknown on Kaggle; original public) | Cleaned/de-duplicated refinement of KDD Cup 99 for intrusion detection (DoS, probe, R2L, U2R). Legacy but ubiquitous baseline; note it is old and not representative of current traffic. Best-documented mirror `dhoogla/nslkdd` (~2 MB, CC BY-NC-SA 4.0). | networking_equipment (primary) |
| CIC-IDS2017 | `dhoogla/cicids2017` (source: CIC, UNB; curated by Laurens D'hooge) | ~238 MB | CC BY-NC-SA 4.0 | Flow-based intrusion detection (CICFlowMeter features) covering benign plus brute force, Heartbleed, botnet, DoS, DDoS, web attacks, infiltration. High-quality curation. | networking_equipment (primary) |
| CSE-CIC-IDS2018 | `dhoogla/csecicids2018` (source: CSE / CIC; curated by D'hooge) | ~634 MB | CC BY-NC-SA 4.0 | Follow-up to CIC-IDS2017 generated on AWS (50 attacker machines, 420 victim hosts); brute force, DoS, DDoS, web, infiltration, botnet. A larger official variant (`bcccdatasets/large-scale-ids-dataset-bccc-cse-cic-ids2018`, ~17.8 GB, MIT) exists. | networking_equipment (primary), computing_devices (secondary) |
| DDoS Dataset (balanced and unbalanced) | `devendra416/ddos-datasets` | ~2.88 GB | Other (specified in description) | Large balanced and unbalanced DDoS flow datasets (CIC-DDoS2019-style captures). Good for volumetric-attack modelling against network infrastructure. | networking_equipment (primary) |
| NetFlow V2 / V3 Datasets (NF-UQ family) | `athena21/netflow-datasets-v2` and `athena21/netflow-v3-datasets` (cite Sarhan/Layeghy/Portmann, UQ, NF-UQ-NIDS) | ~1.46 GB (v2), ~1.49 GB (v3) | CC BY-NC-SA 4.0 | Standardised NetFlow-feature versions of multiple NIDS benchmarks (BoT-IoT, ToN-IoT, UNSW-NB15, CSE-CIC-IDS2018) sharing a common feature schema. Excellent for cross-dataset generalisation studies. | networking_equipment (primary), IoT (secondary) |

---

## Group 5: software_firmware (CVE / vulnerability / firmware and app malware / exploit catalogues)

| Dataset | Kaggle slug or canonical source | Size | Licence | Description | Tech-group mapping |
|---|---|---|---|---|---|
| CVE and CWE Mapping Dataset | `krooz0/cve-and-cwe-mapping-dataset` | ~32.6 MB | CC BY-NC-SA 4.0 | CVEs from 2002 to 2021 mapped to CWE weakness categories (all three CWE views). Core for weakness-classification and vulnerability-taxonomy work. | software_firmware (primary) |
| CVEfixes (vulnerable and fixed code) | `girish17019/cvefixes-vulnerable-and-fixed-code` (cite Bhandari et al. CVEfixes) | ~392 MB | Other (specified in description) | Vulnerabilities paired with their fixing commits across open-source projects, at method/file level with CWE and CVSS metadata. Underpins vulnerability-detection and auto-repair research (relevant to firmware/software supply chain). | software_firmware (primary) |
| NVD CVE 2020-2025 (with CVSS) | `ibrahimqasimi/cve-cybersecurity-vulnerabilities-2020-2025` | ~351 KB | Apache 2.0 | Recent NVD CVE records with severity and CVSS (reported 4,800 published vulnerabilities). Compact and current. | software_firmware (primary) |
| Vulnerability Management Datasets (CVE + CISA KEV + EPSS) | `francescomanzoni/vulnerability-management-datasets` | ~49 MB | Apache 2.0 | Combines CVE, CISA Known-Exploited-Vulnerabilities and EPSS exploit-probability scores; updated daily. Strong for exploitation-likelihood analysis. | software_firmware (primary) |
| CISA Known Exploited Vulnerabilities | `ibrahimqasimi/cisa-known-exploited-vulnerabilities` (source: US CISA KEV) | ~147 KB | MIT | The CISA KEV catalogue (vulnerabilities confirmed exploited in the wild, reported 1,587 entries), with vendor/product and due-date fields. The closest thing to a curated "real incident driver" list, directly relevant to connective-product exposure. | software_firmware (primary) |
| CVE 2024 Database: Exploits, CVSS, OS | `manavkhambhayata/cve-2024-database-exploits-cvss-os` | ~118 KB | Other (specified in description) | Live-extracted NVD 2024 vulnerabilities with affected OS, CVSS and attack vectors. Useful for OS/product-level exposure mapping. | software_firmware (primary), computing_devices (secondary) |
| Google Project Zero: 0-days in the Wild | `jlcole/google-zero-days-in-the-wild` (source: Google Project Zero tracker) | ~22.6 KB | CC BY-NC-SA 4.0 | Google Project Zero's tracker of zero-day vulnerabilities detected exploited in the wild (vendor, product, CVE, detection date). Real-world exploitation record, small but authoritative. | software_firmware (primary) |
| CIC-AndMal-2020 (Android app malware) | `albertozorzetto/cic-andmal-2020-dynamic-static-analysis` (source: CIC, UNB) | ~59 MB | CC0: Public Domain | ~400K Android apps across 14 malware categories and 191 families, static and dynamic features. Firmware/app-layer malware on mobile connective devices. | software_firmware (primary), computing_devices (secondary) |
| UGRansome (ransomware / zero-day anomaly) | `nkongolo/ugransome-dataset` | ~3.15 MB | CC BY-SA 4.0 | Feature set for anomaly detection in zero-day attacks and ransomware (network plus ransomware-family signals). Peer-reviewed, actively maintained. | software_firmware (primary), networking_equipment (secondary) |
| Ransomware detection dataset (PE features) | `amdj3dax/ransomware-detection-data-set` | ~2.24 MB | Apache 2.0 | PE-header/attribute features for ransomware vs benign binary classification on Windows executables. | software_firmware (primary), computing_devices (secondary) |

---

## Cross-cutting IoMT and IIoT datasets (map to IoT + software_firmware / computing_devices)

| Dataset | Kaggle slug or canonical source | Size | Licence | Description | Tech-group mapping |
|---|---|---|---|---|---|
| Edge-IIoTset (IoT + IIoT cyber security) | `mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot` (uploaded by original author, Ferrag et al.) | ~1.75 GB | CC BY-NC-SA 4.0 | Large IoT/IIoT security dataset from a 7-layer testbed with more than 10 IoT device types and 14 attacks across 5 threat categories (DoS/DDoS, information gathering, MITM, injection, malware). Spans IoT, industrial IoT and networking. | IoT + OT (IIoT) + networking_equipment |
| CIC IoMT 2024 (Internet of Medical Things) | `amineipad/cic-iomt-dataset-2024` (cite CIC UNB) | ~176 MB | MIT (mirror) | Cybersecurity network-traffic benchmark for Internet-of-Medical-Things devices (Wi-Fi, MQTT, Bluetooth), 18+ attacks. Connective medical devices. (Note: medical devices are out of scope for CPCID itself; listed here for completeness.) | IoT (primary, medical), networking_equipment (secondary) |

---

## Relevant competitions and notebooks (context for reproducibility)

- **Advanced AI for Cybersecurity: Intrusion Detection with UNSW-NB15** (`competitions/advanced-ai-for-cybersecurity-intrusion-detection-with-unsw-nb-15`): community competition, live, deadline 2026-09-05. Shows an active modelling task on connective-network traffic.
- **Microsoft Malware Prediction** and **Microsoft Malware Classification Challenge (BIG 2015)**: closed but data still usable; the two largest real-endpoint malware datasets on the platform (see Group 3).
- **Active notebook ecosystem.** Verified example notebooks include `daniilnahliuk1/ids-multi-dataset-preprocessing-pipeline` (multi-dataset IDS preprocessing) and `mryoussefmahdi/eplainable-model-for-iot-attacks-classification` (explainable IoT attack classification), plus dozens to hundreds of public kernels on the headline datasets (CIC-IoT-2023, UNSW-NB15, NSL-KDD, Edge-IIoTset). Each headline dataset ships with reusable, forkable analysis code, lowering the cost of a reproducible study.

---

## What this corpus enables, and what it does not

The public Kaggle corpus is strong enough to support a reproducible, open-data study of attack *detectability* across all five technology groups, and to quantify vulnerability and exploitation *exposure* by product/OS/vendor category weighted by exploit probability (EPSS) rather than raw count. Real (not synthetic) anchors exist: BETH (real honeypot host telemetry), IoT-23 (real malware on real IoT devices), the Multi-Protocol IoT honeypot dataset, the Microsoft endpoint-fleet data, CISA KEV and Project Zero.

Limitations that must be stated plainly:

- **Most traffic datasets are synthetic/testbed captures, not incident records.** They measure detectability of known attack patterns, not the frequency, cost or root cause of real incidents in deployed products.
- **Mirror provenance and licence drift.** Many entries are community re-uploads of research datasets; licences on Kaggle mirrors ("Unknown", "Other") often do not match the original terms. Cite the original source and verify usage rights before publishing.
- **OT and firmware coverage is thin.** Only HAI (and a repackaged SWaT mirror) give real OT process data on Kaggle; WADI and most SCADA/ICS benchmarks are not on Kaggle at all. True firmware-binary datasets are scarce; the software_firmware group leans on CVE metadata and PE/Android malware rather than device firmware images.
- **Class imbalance and dataset age.** NSL-KDD and KDD-derived sets are old and not representative of current traffic; several IoT sets are heavily attack-weighted. Any incident-rate or base-rate claim from these datasets is unreliable and should be avoided.
- **No unified "incident" ground truth.** There is no single Kaggle dataset that records real-world cyber incidents against connective products with dates, products, impact and cost. The closest proxies (CISA KEV, Project Zero, small breach-summary tables) are aggregate/curated, not primary-source per-incident records, and should be treated as indicative only. This is precisely the gap CPCID's curated incident dataset addresses.

*Verification note: all slugs, URLs and byte sizes above were returned by the Kaggle MCP on 2026-07-01. Row counts are given only where explicitly reported by the dataset owner. WADI has no verified Kaggle dataset.*
