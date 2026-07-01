#!/usr/bin/env python3
"""Validate the CPCID dataset artifacts.

Checks, in order:
  1. data/incidents.csv    required columns present and non-empty; tech_group in the allowed set.
  2. data/incidents.jsonld valid JSON; @graph present and non-empty.
  3. taxonomy/cpcid.ttl     parses with rdflib as a SKOS concept scheme.

Prints a PASS/FAIL summary and exits non-zero on any failure.
Dependencies: Python standard library plus rdflib.
"""

import csv
import json
import sys
from pathlib import Path

try:
    import rdflib
except ImportError:
    print("FAIL: rdflib is not installed. Run: pip install rdflib")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "incidents.csv"
JSONLD_PATH = ROOT / "data" / "incidents.jsonld"
TTL_PATH = ROOT / "taxonomy" / "cpcid.ttl"

REQUIRED_COLUMNS = [
    "id", "name", "year", "tech_group", "vendor_or_product", "cve",
    "vector", "impact_summary", "impact_quantified", "uk_relevance",
    "source_url", "confidence",
]
ALLOWED_TECH_GROUPS = {
    "IoT", "OT", "computing_devices", "networking_equipment", "software_firmware",
}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}

results = []


def record(name, ok, detail=""):
    results.append((name, ok, detail))
    flag = "PASS" if ok else "FAIL"
    line = f"[{flag}] {name}"
    if detail:
        line += f": {detail}"
    print(line)


def check_csv():
    if not CSV_PATH.exists():
        record("CSV exists", False, str(CSV_PATH))
        return
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    record("CSV parses", True, f"{len(rows)} rows")

    header_ok = rows and all(col in rows[0] for col in REQUIRED_COLUMNS)
    record("CSV has required columns", bool(header_ok),
           "" if header_ok else "missing one or more required columns")
    if not header_ok:
        return

    empty = []
    bad_group = []
    bad_conf = []
    for r in rows:
        for col in REQUIRED_COLUMNS:
            if r.get(col) is None or str(r.get(col)).strip() == "":
                empty.append(f"{r.get('id', '?')}:{col}")
        if r["tech_group"] not in ALLOWED_TECH_GROUPS:
            bad_group.append(f"{r['id']}={r['tech_group']}")
        if r["confidence"] not in ALLOWED_CONFIDENCE:
            bad_conf.append(f"{r['id']}={r['confidence']}")

    record("CSV all required cells non-empty", not empty,
           "" if not empty else ", ".join(empty[:5]))
    record("CSV tech_group in allowed set", not bad_group,
           "" if not bad_group else ", ".join(bad_group))
    record("CSV confidence in allowed set", not bad_conf,
           "" if not bad_conf else ", ".join(bad_conf))


def check_jsonld():
    if not JSONLD_PATH.exists():
        record("JSON-LD exists", False, str(JSONLD_PATH))
        return
    try:
        with JSONLD_PATH.open(encoding="utf-8") as f:
            doc = json.load(f)
    except json.JSONDecodeError as e:
        record("JSON-LD is valid JSON", False, str(e))
        return
    record("JSON-LD is valid JSON", True)

    has_context = "@context" in doc
    record("JSON-LD has @context", has_context)

    graph = doc.get("@graph", [])
    record("JSON-LD @graph non-empty", bool(graph), f"{len(graph)} incidents")


def check_ttl():
    if not TTL_PATH.exists():
        record("Turtle exists", False, str(TTL_PATH))
        return
    g = rdflib.Graph()
    try:
        g.parse(TTL_PATH.as_posix(), format="turtle")
    except Exception as e:  # noqa: BLE001
        record("Turtle parses with rdflib", False, str(e))
        return
    record("Turtle parses with rdflib", True, f"{len(g)} triples")

    skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
    concepts = set(g.subjects(rdflib.RDF.type, skos.Concept))
    schemes = set(g.subjects(rdflib.RDF.type, skos.ConceptScheme))
    record("Turtle has a skos:ConceptScheme", bool(schemes), f"{len(schemes)} scheme(s)")
    record("Turtle has skos:Concept nodes", bool(concepts), f"{len(concepts)} concept(s)")


def main():
    print("CPCID dataset validation")
    print("=" * 40)
    check_csv()
    check_jsonld()
    check_ttl()
    print("=" * 40)
    passed = sum(1 for _, ok, _ in results if ok)
    total = len(results)
    all_ok = passed == total
    print(f"SUMMARY: {passed}/{total} checks passed -> {'PASS' if all_ok else 'FAIL'}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
