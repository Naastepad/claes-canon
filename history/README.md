# Historical layer

This directory is the non-fiction historical substrate for the Claes project.

## Purpose

The historical layer separates **what is historically supported** from **what the novel makes Claes do with it**. Story Claims and Narrative Instances may point to historical events; historical events never acquire fictional Claes participation merely because they are relevant to the story.

Canonical dependency direction:

**source → HIST.EVENT → possible world consequences → Story Claim / Narrative Instance**

Never invert this chain to manufacture history from fiction.

## Files

- `LOW_COUNTRIES_TRANSFORMATION_1540_1605.yaml` — machine-readable event spine for the Low Countries, deliberately broader than a military 'Eighty Years' War' chronology.
- `LOW_COUNTRIES_TRANSFORMATION_1540_1605.md` — human-readable chronological synthesis and usage rules.
- `ZEELAND_REVOLT_TIMELINE.yaml` — regional layer for Zeeland, Goes, Reimerswaal, Middelburg, Vlissingen, Veere and the Delta waterways.

## Evidence statuses

- `VERIFIED` — source has been consulted and directly supports the event as represented.
- `SUPPORTED` — supported by a scholarly synthesis, but exact local detail may remain open.
- `NEEDS_LOCATOR` — historically important and provisionally listed for orientation, but an exact locator must be added before detailed scene use.
- `OPEN` — research question, not an event claim.

## Event design

Each event may carry:
- date/interval and precision;
- geography and scale;
- event type;
- actors/institutions;
- source IDs and evidence status;
- immediate and structural consequences;
- sensory/material consequences where historically supportable;
- `claes_relevance` without fictionalising the event;
- `memory_afterlife` to distinguish event from later narration or commemoration;
- `do_not_infer` guardrails.

## Core historiographic guardrail

For the Revolt and religious transition always distinguish:

**what happened → what a person could perceive → what was subsequently told → what a community later remembered or suppressed.**

This distinction is informed by Judith Pollmann's work on early modern memory and must be preserved when later sources describe violence, iconoclasm, sieges or confessional change.
