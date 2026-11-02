# Johnson Controls Smart Building Ontology point naming

Canonical structure:

`(<aggregation_descriptor>_)?(<aggregation>_)?(<descriptor>_)*(<component>_)?(<measurement_descriptor>_)?(<measurement>_)?<point_type>(_<number>)*`

## Rules

1. `point_type` is required.
2. `aggregation_descriptor` is required whenever `aggregation` is used.
3. Optional sections are omitted rather than left blank.
4. Sections are joined with underscores.
5. Values should first be checked against `DBO_Subfields_Register.csv`.
6. Where a human-readable or constrained equipment tag needs abbreviations, use `Subfield_Abbreviations_Register.csv`.
7. Equipment entities must use `Entity_Abbreviations_Register.csv`.
8. Do not invent an abbreviation. Submit a pull request with `status=proposed` when no approved mapping exists.

## Source precedence

1. Explicit project-specific values.
2. JCI entity and subfield registers in this repository.
3. BDNS.
4. Google Digital Buildings Ontology.
5. Supporting resource list.
