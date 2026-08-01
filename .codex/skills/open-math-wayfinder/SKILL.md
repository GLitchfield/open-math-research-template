---
name: open-math-wayfinder
description: Advance open-ended mathematics research through the repository's tracked Wayfinder decision map, bounded computation criteria, reproducible evidence, and read-only Sol/Fable adversarial review. Use when charting a new mathematical research destination, choosing or resolving a strategic ticket, redirecting or closing a research route, promoting a new frontier, planning a consequential computation, or reviewing whether evidence supports a proposed mathematical claim.
---

# Open Math Wayfinder

Use the tracked decision map to find the next question, and use Sol/Fable to
challenge consequential route decisions without confusing model review with
mathematical evidence.

## Load the project contract

1. Read `AGENTS.md` completely.
2. Read `docs/wayfinder/map.md` at low resolution.
3. Read `docs/wayfinder/README.md` and
   `docs/agents/issue-tracker.md` before changing the map or tickets.
4. Run `python3 scripts/wayfinder_status.py`.
5. Read only the selected ticket and directly relevant closed tickets or
   evidence. Do not load the entire ticket history by default.

## Chart a new map

1. Name a concrete destination with the user. The destination fixes scope.
2. Map the first sharp decisions breadth-first. Put indistinct in-scope areas
   in `Not yet specified`; do not pre-slice fog into speculative tickets.
3. Create the map from `docs/wayfinder/map.md` and tickets from
   `templates/decision-ticket.md`.
4. Create tickets first, then wire `blocked_by` filenames.
5. For computational tickets, predeclare inputs, conventions, resource bound,
   advancement, redirection, precision/verification limits, closure, negative
   result scope, and independent certificate.
6. Validate, commit, and push the charted state. Do not hand-resolve a ticket
   during the map-charting session.

If the whole route is already clear and fits one session, do not create a
Wayfinder map merely for ceremony.

## Advance an existing map

1. Use the user-named ticket or claim the first unclaimed frontier ticket.
2. Resolve one strategic ticket per session, except explicitly parallel
   research tickets.
3. Keep routine implementation inside the selected decision's scope; do not
   create implementation tickets that add no new decision.
4. Record empirical work in a numbered experiment note and add it to
   `docs/research_log.md`.
5. Before strategic selection, redirection, closure, or frontier promotion,
   run the Sol/Fable protocol below.
6. Write the detailed resolution in the ticket, set `status: closed`, and add
   one linked gist to `Decisions so far`.
7. Create newly sharp tickets, update the fog, and close newly exposed
   beyond-destination work into `Out of scope`.
8. Run `make test`, commit the decision with its evidence, and push.

## Run the Sol/Fable protocol

Read `docs/adversarial-review.md` before the first run in a project.

1. Commit the evidence under review.
2. Write one sharp question under ignored `runs/reviews/`. Include the proposed
   consequence and the ticket's terminal branches.
3. Select only compact UTF-8 evidence files. Never send secrets, credentials,
   restricted sources, or large raw runs.
4. Check providers with:

   ```console
   python3 scripts/adversarial_review.py doctor
   ```

5. Run both blind reviews and one reciprocal critique round:

   ```console
   python3 scripts/adversarial_review.py run \
     --question-file runs/reviews/question.txt \
     --evidence docs/wayfinder/tickets/NNNN-question.md \
     --evidence docs/experiments/NNNN-result.md \
     --codex-model MODEL_ID \
     --output runs/reviews/NNNN-review
   ```

6. Inspect both initial reviews before critique answers.
7. Check material objections independently. Use them to add missing controls,
   narrow claims, select cheaper discriminators, or sharpen stopping rules.
8. Record the evidence-packet hash, material objections, and their disposition
   in the ticket. Keep full provider output ignored.

Never cite reviewer agreement as proof, certification, exhaustiveness,
literature authority, or permission for an external action.

## Preserve mathematical claim levels

- Label theorem, exact computation, certified numerics, observation,
  heuristic, conditional claim, and failed experiment distinctly.
- Scope every negative result to the exact component, convention, model,
  implementation, or bounded search that was tested.
- Separate producer and checker implementations where practical and include
  mutation controls.
- Reject unbounded search or precision escalation without a newly reviewed,
  predeclared decision ticket.
