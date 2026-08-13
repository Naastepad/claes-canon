# Narrative Instances

This directory contains the concrete story instances that connect the Claes canon to a project-neutral Narrative Knowledge Base such as the McKee/NOS Knowledge Objects.

These records are **not** universal narrative theory and are **not** Lemma rules. They say where and how story truth is dramatized.

## Namespaces

- `NI.BOOK.*`
- `NI.ACT.*`
- `NI.SEQUENCE.*`
- `NI.CHAPTER.*`
- `NI.SCENE.*`
- `NI.BEAT.*`
- `ARC.*`
- `MOTIF.*`

A Narrative Instance may reference:

- entities (`ENT.*`);
- active or introduced story claims (`STC.*`);
- arcs (`ARC.*`);
- motifs (`MOTIF.*`);
- source/canon decisions when needed;
- future Narrative Knowledge Objects (`KO.*`) only as analysis targets, never as copied theory.

Example reasoning path:

`KO.SCENE + NI.SCENE.DEE_FIRST_ENCOUNTER.1563.001 -> diagnostic`

The concrete scene remains here; McKee's definition of Scene remains in the external Narrative Knowledge Base.