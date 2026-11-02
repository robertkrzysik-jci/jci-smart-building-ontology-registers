#!/usr/bin/env python3
import csv, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
errors=[]
specs={
"Entity_Abbreviations_Register.csv":["discipline","entity_name","entity_abbreviation","status","source","notes"],
"Subfield_Abbreviations_Register.csv":["name","abbreviation","status","source","notes"],
"DBO_Subfields_Register.csv":["category","subfield","definition","status","source"],
"Ontology_Point_Name_Structure.csv":["position","section","requirement","examples"],
"Ontology_Point_Name_Examples.csv":["point_name","entity_abbreviation","status","notes"],
}
for fn,header in specs.items():
 p=root/"data"/fn
 with p.open(newline="",encoding="utf-8") as f:
  rd=csv.DictReader(f); rows=list(rd)
 if rd.fieldnames!=header: errors.append(f"{fn}: header must be {header}")
 if not rows: errors.append(f"{fn}: register is empty")
 for i,r in enumerate(rows,2):
  if "status" in r and r["status"] not in {"approved","proposed","deprecated","example"}: errors.append(f"{fn}:{i}: invalid status")
# Subfield names must be unique; entity source may contain discipline-specific alternatives.
fn,key="Subfield_Abbreviations_Register.csv","name"
with (root/"data"/fn).open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
seen={}
for i,r in enumerate(rows,2):
 k=r[key].strip().casefold()
 if k in seen: errors.append(f"{fn}:{i}: duplicate {key}; first at row {seen[k]}")
 else: seen[k]=i
if errors:
 print("Validation failed:"); [print("-",e) for e in errors]; sys.exit(1)
print("OK: all five registers validated")
