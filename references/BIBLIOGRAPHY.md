# Bibliography

The academic and recognised-technical literature base within which the Connective Product Cyber Incidents Dataset (CPCID) taxonomy sits. Scope: peer-reviewed and recognised technical literature on cyber incidents affecting connective products (IoT, OT/ICS, networking and edge equipment, computing devices, and software/firmware including open-source and AI components). Primary window 2022 to 2026, with foundational older works cited where they remain the canonical reference (for example, EPSS and the standard IDS datasets).

Compiled 2026-07-01 by targeted search across arXiv (cs.CR, cs.NI, cs.SE), USENIX, ACM Digital Library, IEEE Xplore, NDSS, MDPI, Crossref DOI records, and recognised industry threat-intelligence primary sources. Every citation was checked against a primary or authoritative source. Where a field could not be confirmed against the primary page, it is flagged with a verification note or "UNVERIFIED". Any citation carried as unverified must never be presented as settled fact.

Entries are grouped by literature strand. Format: title; authors; venue; year; URL.

---

## Strand 1: Empirical measurement of IoT/OT attacks and botnets

Honeypots, network telescopes/darknets, Shodan-based exposure studies, and Mirai retrospectives.

1. **The End of the Canonical IoT Botnet: A Measurement Study of Mirai's Descendants.** Leon Böck, Valentin Sundermann, Isabella Fusari, Shankar Karuppayah, Max Mühlhäuser, Dave Levin. arXiv preprint (cs.CR), 2023. arXiv:2309.01130. <https://arxiv.org/abs/2309.01130>
2. **HoneyIoT: Adaptive High-Interaction Honeypot for IoT Devices Through Reinforcement Learning.** Chongqi Guan, Heting Liu, Guohong Cao, Sencun Zhu, Thomas La Porta. ACM WiSec, 2023. arXiv:2305.06430. <https://arxiv.org/abs/2305.06430>
3. **Analyzing Unsolicited Internet Traffic: Measuring IoT Security Threats via Network Telescopes.** Shereen Ismail, Taelyn Dyer, Raul Martinez, Garrett Gastman, Yozelyn Chavez, Asma Jodeiri Akbarfam. IEEE 7th World AI IoT Congress (AIIoT), 2026. arXiv:2605.02795. <https://arxiv.org/abs/2605.02795>
4. **Merit Network Telescope: Processing and Initial Insights from Nearly 20 Years of Darknet Traffic for Cybersecurity Research.** Shereen Ismail, Eman Hammad, William Hatcher, Salah Dandan, Ammar Alomari, Michael Spratt. arXiv preprint (cs.SI), 2025. arXiv:2510.25050. <https://arxiv.org/abs/2510.25050>
5. **A Scan-Based Analysis of Internet-Exposed IoT Devices Using Shodan Data.** Richelle Williams, Fernando Koch. arXiv preprint (cs.CR, cs.NI), 2026. arXiv:2602.15263. <https://arxiv.org/abs/2602.15263>
6. **Evolving IoT Botnet Threats and Practical Honeypot Observation: A Summary Review and Experimental Study.** Author list UNVERIFIED (article not opened). Journal of Cybersecurity and Privacy (MDPI), vol. 6, art. 82, 2026. DOI: 10.3390/jcp6030082. <https://doi.org/10.3390/jcp6030082>

Verification note (Strand 1): items 1 to 5 fully verified by fetching the arXiv abstract page (title, authors, arXiv ID matched). Item 6: title, MDPI journal and DOI confirmed from search metadata; the full author list was not enumerated, so authorship is UNVERIFIED until the DOI landing page is opened.

---

## Strand 2: Edge-device, VPN, and network-appliance exploitation (n-day and zero-day trends)

The most numerically grounded work on in-the-wild edge and enterprise exploitation currently comes from vendor threat-intelligence teams (Google Threat Intelligence Group, formerly Mandiant plus Project Zero), which are primary-source but not peer-reviewed. Peer-review status is flagged for each.

1. **Hello 0-Days, My Old Friend: A 2024 Zero-Day Exploitation Analysis.** Casey Charrier, James Sadowski, Clement Lecigne, Vlad Stolyarov. Google Threat Intelligence Group (GTIG), 2025. Not peer-reviewed (industry primary-source analysis). <https://cloud.google.com/blog/topics/threat-intelligence/2024-zero-day-trends>
2. **Look What You Made Us Patch: 2025 Zero-Days in Review.** Casey Charrier, James Sadowski, Zander Work, Clement Lecigne, Benoit Sevens, Fred Plan. Google Threat Intelligence Group (GTIG), 2026. Not peer-reviewed. <https://cloud.google.com/blog/topics/threat-intelligence/2025-zero-day-review>
3. **How Low Can You Go? An Analysis of 2023 Time-to-Exploit Trends.** Casey Charrier, Robert Weiner. Google Cloud / Mandiant, 2024. Not peer-reviewed. <https://cloud.google.com/blog/topics/threat-intelligence/time-to-exploit-trends-2023>
4. **A Longitudinal Measurement Study of Log4Shell Exploitation from a Reactive Network Telescope.** Aakash Singh, Kuldeep Singh Yadav, V. Anil Kumar, Samiran Ghosh, Pranita Baro, Basavala Bhanu Prasanth. arXiv preprint, 2026. arXiv:2601.04281. Not yet peer-reviewed. <https://arxiv.org/abs/2601.04281>
5. **A review of zero-day in-the-wild exploits in 2023.** Google Threat Analysis Group / Project Zero (corporate byline; individual author bylines UNVERIFIED). blog.google, 2024. Not peer-reviewed. <https://blog.google/innovation-and-ai/technology/safety-security/a-review-of-zero-day-in-the-wild-exploits-in-2023/>

Verification note (Strand 2): the GTIG/Mandiant reports (items 1 to 3) are recognised industry primary sources widely cited in academic work, but are not peer-reviewed. Item 5: title, publisher and year confirmed from multiple sources; named authorship UNVERIFIED. See also Strand 5 item 5 (Parla, EPSS-vs-KEV) on the n-day patching gap from the prediction side.

---

## Strand 3: Software and firmware supply-chain security

SBOM, dependency confusion, XZ Utils, malicious-package studies, and AI-component supply chain.

1. **SoK: Taxonomy of Attacks on Open-Source Software Supply Chains.** Piergiorgio Ladisa, Henrik Plate, Matias Martinez, Olivier Barais. IEEE Symposium on Security and Privacy (S&P), 2023, pp. 1509 to 1526. DOI: 10.1109/SP46215.2023.10179304. <https://ieeexplore.ieee.org/document/10179304/> (author copy: <https://oaklandsok.github.io/papers/ladisa2023.pdf>)
2. **Beyond Typosquatting: An In-depth Look at Package Confusion.** Shradha Neupane, Grant Holmes, Elizabeth Wyss, Drew Davidson, Lorenzo De Carli. 32nd USENIX Security Symposium, 2023. <https://www.usenix.org/conference/usenixsecurity23/presentation/neupane> (PDF: <https://www.usenix.org/system/files/usenixsecurity23-neupane.pdf>)
3. **Wolves in the Repository: A Software Engineering Analysis of the XZ Utils Supply Chain Attack.** Piotr Przymus, Thomas Durieux. arXiv preprint (cs.SE, cs.CR), 2025. arXiv:2504.17473. Not yet peer-reviewed. <https://arxiv.org/abs/2504.17473>
4. **An Empirical Study on Software Bill of Materials: Where We Stand and the Road Ahead.** Boming Xia, Tingting Bi, Zhenchang Xing, Qinghua Lu, Liming Zhu. 45th IEEE/ACM International Conference on Software Engineering (ICSE), 2023. arXiv:2301.05362. <https://arxiv.org/abs/2301.05362>
5. **A Large-Scale Exploit Instrumentation Study of AI/ML Supply Chain Attacks in Hugging Face Models.** Beatrice Casey, Joanna C. S. Santos, Mehdi Mirakhorli. arXiv preprint (cs.CR, cs.LG, cs.SE), 2024. arXiv:2410.04490. <https://arxiv.org/abs/2410.04490>
6. **Killing Two Birds with One Stone: Malicious Package Detection in NPM and PyPI using a Single Model of Malicious Behavior Sequence.** Junan Zhang, Kaifeng Huang, Yiheng Huang, Bihuan Chen, Ruisi Wang, Chong Wang, Xin Peng. arXiv preprint (cs.CR, cs.SE), 2023. arXiv:2309.02637. <https://arxiv.org/abs/2309.02637>

Verification note (Strand 3): items 3, 4, 5, 6 fully verified via arXiv abstract fetch. Item 1 verified via IEEE Xplore document ID plus DOI plus corroborating search snippets. Item 2 verified via the USENIX proceedings snippet and official PDF path (the live USENIX page returned an access block to the fetcher, but the URL is the standard proceedings path).

---

## Strand 4: OT/ICS incident and threat analysis

Living-off-the-land against critical infrastructure, PLC attacks, ICS malware, and critical-infrastructure threat modelling.

1. **A Tale of Two Industroyers: It was the Season of Darkness.** Luis Salazar, Sebastian R. Castro, Juan Lozano, Keerthi Koneru, Emmanuele Zambon, Bing Huang, Ross Baldick, Marina Krotofil, Alonso Rojas, Alvaro A. Cardenas. IEEE Symposium on Security and Privacy (S&P), 2024. <https://escholarship.org/uc/item/0dr9b00s> (IEEE CSDL: <https://www.computer.org/csdl/proceedings-article/sp/2024/313000a162/1Ub24B7070k>)
2. **SoK: Security of Programmable Logic Controllers.** Efrén López-Morales, Ulysse Planta, Carlos Rubio-Medrano, Ali Abbasi, Alvaro A. Cardenas. 33rd USENIX Security Symposium, 2024 (arXiv version). arXiv:2403.00280. <https://arxiv.org/abs/2403.00280>
3. **Compromising Industrial Processes using Web-Based Programmable Logic Controller Malware.** Ryan Pickren, Tohid Shekari, Saman Zonouz, Raheem Beyah. Network and Distributed System Security Symposium (NDSS), 2024. <https://www.ndss-symposium.org/ndss-paper/compromising-industrial-processes-using-web-based-programmable-logic-controller-malware/> (PDF: <https://www.ndss-symposium.org/wp-content/uploads/2024-49-paper.pdf>)
4. **Cyber security of OT networks: A tutorial and overview.** Sarthak Kapoor, Sumit Kumar, Harsh Vardhan. arXiv preprint, 2025. arXiv:2502.14017. Not peer-reviewed. <https://arxiv.org/abs/2502.14017>
5. **Impact of FrostyGoop ICS Malware on Connected OT Systems.** Dragos, Inc. (threat-intelligence team; corporate byline). Dragos Intelligence Brief, 2024. Recognised industry technical report, not peer-reviewed. <https://hub.dragos.com/report/frostygoop-ics-malware-impacting-operational-technology>
6. **PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038a).** CISA, NSA, FBI (joint advisory). 2024. Recognised government technical report, not peer-reviewed. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a>

Verification note (Strand 4): items 1, 2, 3, 5 fully verified. A related survey, "Vulnerabilities and Attacks Against Industrial Control Systems and Critical Infrastructures" (Makrakis, Kolias, Kambourakis, Rieger, Benjamin; arXiv:2109.03945), catalogues Stuxnet/Industroyer/TRITON but is dated 2021 (out of window) and its full author list was not re-fetched, so it is flagged UNVERIFIED-on-authorship, out-of-window, and omitted from the numbered set. Item 6 (AA24-038a) is the canonical primary source on Volt Typhoon living-off-the-land TTPs; no single peer-reviewed academic paper of comparable authority was found for Volt Typhoon specifically.

---

## Strand 5: Vulnerability-exploitation prediction and prevalence (EPSS / KEV)

EPSS, CISA KEV analyses, exploitation-in-the-wild studies, CVSS-vs-EPSS. Note: two distinct EPSS papers are frequently conflated. The Jacobs, Romanosky, Adjerid, Baker quartet is the 2020 Journal of Cybersecurity precursor (item 1). The DTRAP EPSS system paper (item 2) has a different author list (adds Edwards and Roytman, drops Baker). Both are listed and kept distinct.

1. **Improving vulnerability remediation through better exploit prediction.** Jay Jacobs, Sasha Romanosky, Idris Adjerid, Wade Baker. Journal of Cybersecurity, 6(1), art. tyaa015, Oxford University Press, 2020. DOI: 10.1093/cybsec/tyaa015. <https://academic.oup.com/cybersecurity/article/6/1/tyaa015/5905457>
2. **Exploit Prediction Scoring System (EPSS).** Jay Jacobs, Sasha Romanosky, Benjamin Edwards, Michael Roytman, Idris Adjerid. Digital Threats: Research and Practice (DTRAP), 2(3), art. 20, ACM, 2021 (arXiv:1908.04856, 2019). DOI: 10.1145/3436242. <https://dl.acm.org/doi/10.1145/3436242> (arXiv: <https://arxiv.org/abs/1908.04856>)
3. **Enhancing Vulnerability Prioritization: Data-Driven Exploit Predictions with Community-Driven Insights.** Jay Jacobs, Sasha Romanosky, Octavian Suciu, Benjamin Edwards, Armin Sarabi. IEEE European Symposium on Security and Privacy Workshops (EuroS&PW), 2023, pp. 194 to 206. arXiv:2302.14172. <https://arxiv.org/abs/2302.14172>
4. **Expected Exploitability: Predicting the Development of Functional Vulnerability Exploits.** Octavian Suciu, Connor Nelson, Zhuoer Lyu, Tiffany Bao, Tudor Dumitras. 31st USENIX Security Symposium, 2022. <https://www.usenix.org/conference/usenixsecurity22/presentation/suciu> (PDF: <https://www.usenix.org/system/files/sec22-suciu.pdf>)
5. **Efficacy of EPSS in High Severity CVEs found in CISA KEV.** Rianna Parla. arXiv preprint (cs.CR), 2024. arXiv:2411.02618. Non-peer-reviewed. <https://arxiv.org/abs/2411.02618>
6. **Conflicting Scores, Confusing Signals: An Empirical Study of Vulnerability Scoring Systems.** Viktoria Koscinski, Mark Nelson, Ahmet Okutan, Robert Falso, Mehdi Mirakhorli. arXiv preprint (cs.CR), 2025. arXiv:2508.13644. Non-peer-reviewed at time of check. <https://arxiv.org/abs/2508.13644>

Verification note (Strand 5): items 1, 2, 3, 4 fully verified. Item 2 with an ACM caveat: ACM DL pages returned an access block, so metadata was cross-verified via FIRST.org, SSRN and arXiv; Wade Baker is NOT an author of item 2 (unlike item 1), and the arXiv record mis-renders "Adjerid" as "Adjeril". Items 5 and 6 are genuine arXiv preprints, metadata-verified but non-peer-reviewed. Additional lead for extension: NIST CSWP 41 "Likely Exploited Vulnerabilities" (Peter Mell et al., NIST white paper, 2025) proposes the newer LEV metric.

---

## Strand 6: Surveys and systematic literature reviews (SLRs)

SLR/PRISMA status noted per item.

1. **Systematic Literature Review of IoT Botnet DDoS Attacks and Evaluation of Detection Techniques.** Metehan Gelgi, Yueting Guan, Sanjay Arunachala, Maddi Samba Siva Rao, Nicola Dragoni. Sensors (MDPI), 24(11), art. 3571, 2024. DOI: 10.3390/s24113571. <https://doi.org/10.3390/s24113571> (Formal SLR, Petersen/Wohlin guidelines; does not explicitly claim PRISMA compliance.)
2. **Towards Securing Smart Homes: A Systematic Literature Review of Malware Detection Techniques and Recommended Prevention Approach.** Omar Alshamsi, Khaled Shalan, Usman Butt. Information (MDPI), 15(10), art. 631, 2024. DOI: 10.3390/info15100631. <https://doi.org/10.3390/info15100631> (SLR; confirm the exact PRISMA statement in the full text before labelling it PRISMA specifically.)
3. **Industrial Internet of Things Ecosystems Security and Digital Forensics: Achievements, Open Challenges, and Future Directions.** Victor R. Kebande, Ali Ismail Awad. ACM Computing Surveys, 2024. DOI: 10.1145/3635030. <https://doi.org/10.1145/3635030> (Narrative survey at a top-tier venue, not a PRISMA SLR.)
4. **Cybersecurity Solutions for Industrial Internet of Things and Edge Computing Integration: Challenges, Threats, and Future Directions.** Tamara Zhukabayeva, Lazzat Zholshiyeva, Nurdaulet Karabayev, Shafiullah Khan, Noha Alnazzawi. Sensors (MDPI), 25(1), art. 213, 2025. DOI: 10.3390/s25010213. <https://doi.org/10.3390/s25010213> (Systematic review of 185 peer-reviewed articles 2020 to 2024; SLR-style, PRISMA not explicitly asserted.)
5. **Cyber security of OT networks: A tutorial and overview.** Sarthak Kapoor, Sumit Kumar, Harsh Vardhan. arXiv preprint, 2025. arXiv:2502.14017. <https://arxiv.org/abs/2502.14017> (Tutorial/overview, not an SLR; non-peer-reviewed. Also appears in Strand 4.)
6. **A Survey on Security and Privacy Issues in Edge-Computing-Assisted Internet of Things.** Abdulmalik Alwarafy, Khaled A. Al-Thelaya, Mohamed Abdallah, Jens Schneider, Mounir Hamdi. IEEE Internet of Things Journal, 8(6), pp. 4004 to 4022, 2020. DOI: 10.1109/JIOT.2020.3015432. <https://doi.org/10.1109/JIOT.2020.3015432> (Narrative survey, not a PRISMA SLR. OUT OF WINDOW (2020); metadata from search, IEEE Xplore not fetched. Include only as an older high-citation edge anchor; prefer item 4 for an in-window edge survey.)

Verification note (Strand 6): items 1 to 4 verified via Crossref DOI records (and PMC full text for items 1 and 4). Item 5 verified via arXiv. Item 6 partially verified (search metadata, pre-2022). Gap: no 2022 to 2026 IoT-security SLR in IEEE Communications Surveys and Tutorials specifically was surfaced.

---

## Strand 7: Datasets and benchmarks papers

The origin papers behind the standard IoT/IIoT intrusion-detection datasets. These anchor any empirical or ML-based methodology, and connect this bibliography to the datasets catalogued in `RELATED_DATASETS.md`.

1. **CICIoT2023: A Real-Time Dataset and Benchmark for Large-Scale Attacks in IoT Environment.** Euclides Carlos Pinto Neto, Sajjad Dadkhah, Raphael Ferreira, Alireza Zohourian, Rongxing Lu, Ali A. Ghorbani. Sensors (MDPI), 23(13), art. 5941, 2023. DOI: 10.3390/s23135941. <https://www.mdpi.com/1424-8220/23/13/5941> (dataset: <https://www.unb.ca/cic/datasets/iotdataset-2023.html>)
2. **Towards the Development of Realistic Botnet Dataset in the Internet of Things for Network Forensic Analytics: Bot-IoT Dataset.** Nickolaos Koroniotis, Nour Moustafa, Elena Sitnikova, Benjamin Turnbull. Future Generation Computer Systems, 100, pp. 779 to 796, 2019. DOI: 10.1016/j.future.2019.05.041. <https://arxiv.org/abs/1811.00701> (dataset: <https://research.unsw.edu.au/projects/bot-iot-dataset>)
3. **TON_IoT Telemetry Dataset: A New Generation Dataset of IoT and IIoT for Data-Driven Intrusion Detection Systems.** Abdullah Alsaedi, Nour Moustafa, Zahir Tari, Abdun Mahmood, Adnan Anwar. IEEE Access, 8, pp. 165130 to 165150, 2020. DOI: 10.1109/ACCESS.2020.3022862. <https://doi.org/10.1109/ACCESS.2020.3022862> (dataset: <https://research.unsw.edu.au/projects/toniot-datasets>)
4. **Edge-IIoTset: A New Comprehensive Realistic Cyber Security Dataset of IoT and IIoT Applications for Centralized and Federated Learning.** Mohamed Amine Ferrag, Othmane Friha, Djallel Hamouda, Leandros Maglaras, Helge Janicke. IEEE Access, 10, pp. 40281 to 40306, 2022. DOI: 10.1109/ACCESS.2022.3165809. <https://doi.org/10.1109/ACCESS.2022.3165809> (repository record: <https://ro.ecu.edu.au/ecuworks2022-2026/552/>)
5. **N-BaIoT: Network-Based Detection of IoT Botnet Attacks Using Deep Autoencoders.** Yair Meidan, Michael Bohadana, Yael Mathov, Yisroel Mirsky, Dominik Breitenbacher, Asaf Shabtai, Yuval Elovici. IEEE Pervasive Computing, 17(3), pp. 12 to 22, July to September 2018. DOI: 10.1109/MPRV.2018.03367731. <https://arxiv.org/abs/1805.03409> (dataset: UCI ML Repository, "detection_of_IoT_botnet_attacks_N_BaIoT")

Verification note (Strand 7): all five are the canonical origin papers for their datasets. CICIoT2023 (item 1) and TON_IoT (item 3) DOIs are high-confidence but verified via secondary sources rather than a direct publisher-page fetch (both publisher pages returned access blocks). Bot-IoT, Edge-IIoTset and N-BaIoT are fully verified against primary sources (arXiv or institutional repository). Correct author order for N-BaIoT places Breitenbacher before Shabtai.

---

## Where this work is published (target and citation venues)

- Top security venues: USENIX Security, IEEE Symposium on Security and Privacy (S&P/Oakland), NDSS, ACM CCS.
- Measurement venues: ACM Internet Measurement Conference (IMC), Passive and Active Measurement (PAM), ACM SIGCOMM, The Web Conference (WWW).
- Applied/systems security: ACSAC, EuroS&P, ACM WiSec (wireless/IoT), ACM AsiaCCS.
- Survey venues: ACM Computing Surveys, IEEE Communications Surveys and Tutorials, IEEE Internet of Things Journal.
- Datasets and metrics: Digital Threats: Research and Practice (DTRAP), Sensors and IEEE Access (dataset papers), Journal of Cybersecurity.
- Preprints and threat-intel primary sources: arXiv cs.CR / cs.NI / cs.SE; Google Threat Intelligence Group and Mandiant reports; Dragos intelligence briefs; CISA/NSA/FBI advisories and the CISA KEV catalog; FIRST.org (EPSS).

---

## Consolidated list of unverified or caveated citations

For transparency, the following were NOT fully locked down against a primary source and must not be presented as settled fact:

- Strand 1, item 6 (JCP 6:82, 2026): authorship UNVERIFIED (article not opened).
- Strand 2, item 5 (Google 2023 zero-day review): individual author bylines UNVERIFIED (title/publisher/year confirmed).
- Strand 5, item 2 (DTRAP EPSS): venue/DOI cross-verified via FIRST.org/SSRN/arXiv, not the ACM DL page (blocked); arXiv mis-renders "Adjerid" as "Adjeril".
- Strand 5, items 5 and 6 (Parla; Koscinski et al.): genuine arXiv preprints, non-peer-reviewed.
- Strand 6, item 6 (Alwarafy et al., 2020): out-of-window (2020); metadata from search, IEEE Xplore not fetched.
- Strand 7, items 1 and 3 (CICIoT2023, TON_IoT): DOIs high-confidence but verified via secondary sources, publisher pages blocked.
- Strand 4 (mentioned only): Makrakis et al. arXiv:2109.03945 omitted from the numbered set (2021, out-of-window; authorship not re-fetched).

All other citations were verified by fetching the arXiv abstract page, the DOI/Crossref record, the institutional repository, or the official proceedings/dataset page.

---

## How this literature relates to CPCID

The intrusion-detection datasets in Strand 7 are packet/flow captures from lab testbeds, not curated real-world incident records, and none is indexed by connective-product class. IoT-botnet measurement (Strand 1), edge/appliance exploitation (Strand 2), supply-chain (Strand 3), and OT/ICS (Strand 4) are studied largely in isolation, with different venues, metrics and datasets, and no single work unifies them into a cross-product-class threat model. Exploitation-prediction ground truth (Strand 5) is incomplete and contested (scoring systems disagree; EPSS under-warns on CVEs that later hit KEV). CPCID sits inside this literature as a small, curated, product-class-indexed corpus of documented incidents with explicit source-quality grading, addressing the recurring "no unified open incident dataset mapped to product class" gap the literature identifies.
