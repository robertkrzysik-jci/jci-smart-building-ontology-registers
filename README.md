# Johnson Controls Smart Building Ontology Registers

Central GitHub repository for controlled naming data used by Johnson Controls Smart Building Ontology workflows.

## Controlled registers

- `data/Subfield_Abbreviations_Register.csv`: 303 abbreviation mappings.
- `data/Entity_Abbreviations_Register.csv`: 1127 JCI entity mappings.
- `data/DBO_Subfields_Register.csv`: 376 DBO subfields with categories and definitions.
- `data/Ontology_Point_Name_Structure.csv`: the seven point-name sections shown in the supplied DBO structure.
- `data/Ontology_Point_Name_Examples.csv`: reviewable examples.

See `docs/POINT_NAMING.md` for syntax and precedence.

## Propose a change

1. Create a branch from `main`.
2. Edit only the relevant CSV.
3. Use `proposed` for new mappings until approved.
4. Run `python scripts/validate_registers.py`.
5. Open a pull request and complete the supplied template.
6. Merge only after validation and register-owner approval.

## External reference alignment

BDNS provides an asset abbreviation register and mappings including DBO/IFC columns. Google Digital Buildings provides the ontology model, YAML source and validation tooling. These external sources are fallbacks and must not override explicit project or JCI values.

## Publishing checklist

- Replace the placeholder team in `.github/CODEOWNERS`.
- Choose repository visibility according to JCI policy.
- Add an organisation-approved licence before any public release.
