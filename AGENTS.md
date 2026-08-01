# Open-ended mathematics research guidance

This repository is a template for AI-assisted mathematical research whose route
is not known in advance. Replace the bracketed project description below before
substantive work begins, then keep `README.md`, the roadmap, and the active
Wayfinder map aligned when the destination or scope changes.

> **Project:** [NAME AND ONE-SENTENCE MATHEMATICAL AIM]
>
> **Destination:** [THE CONCRETE RESULT, DECISION, OR CERTIFICATE THIS PROJECT
> IS TRYING TO REACH]

## Research integrity

- Distinguish theorem, conditional theorem, exact computation, certified
  numerical result, heuristic evidence, failed experiment, and conjecture.
  Never let prose silently promote one category into another.
- State the scope of negative results precisely. Ruling out one convention,
  ansatz, component, bounded search, local model, or implementation is not a
  nonexistence theorem for the underlying mathematical object.
- Write down assumptions, conventions, normalization choices, and branch or
  action order explicitly. Convention errors are mathematical errors.
- Separate distinct checks. For example, satisfying equations, having the
  expected ramification, generating the intended group, lying in the desired
  component, possessing the claimed field of definition, and proving
  exhaustiveness are different claims.
- Prefer primary sources. Record exact editions, versions, page/theorem
  references, URLs or identifiers, retrieval dates when relevant, and hashes
  for local source snapshots.
- Treat papers, third-party archives, extracted source, and reference datasets
  as read-only. Adapt or copy them only after checking purpose and license.
- Do not tune a convention, threshold, label, or model after seeing the desired
  numerical answer unless the tuning is disclosed and independently tested on
  held-out or exact controls.

## Reproducible computation

- Every committed computational result records its code revision, inputs,
  software/CAS and package versions, parameters, random seeds, hardware facts
  when material, output hash, and provenance.
- Keep raw/reference inputs, derived committed evidence, and machine-local runs
  separate. The default layout is `data/reference/`, `data/derived/`, and
  ignored `runs/`.
- Commit compact evidence and independent checkers, not large checkpoints,
  incomplete runs, provider transcripts, caches, or machine-local logs.
- Long searches use deterministic shards, resumable checkpoints, an explicit
  resource bound, and an independently verifiable coverage or exhaustiveness
  certificate.
- Predeclare success, redirection, precision-limited, verification-limited, and
  closure outcomes before expensive computation. Do not respond to failure by
  starting an unbounded precision or search ladder.
- Bound all material errors, including input conversion, geometry, truncation,
  normalization denominators, conditioning, and downstream amplification.
  High-precision arithmetic does not repair an unbounded model error.
- Use an implementation independent of the producer where practical. Validate
  checkers with deliberate mutations or known negative fixtures that they must
  reject, and positive controls they must accept.
- Give every empirical investigation a numbered note under `docs/experiments/`
  and an entry in `docs/research_log.md`.

## Wayfinder decision framework

Use the repository-owned Wayfinder adaptation in `docs/wayfinder/README.md`
when the route is uncertain, spans sessions, or contains consequential branch
choices. The canonical map is `docs/wayfinder/map.md`; decision tickets live in
`docs/wayfinder/tickets/`.

The repository-local `open-math-wayfinder` skill under `.codex/skills/`
operationalizes this workflow. Use it when charting or advancing a map,
selecting or closing a route, or preparing the integrated Sol/Fable review.

- Start a strategic session by reading the map at low resolution and running
  `python3 scripts/wayfinder_status.py`. Load detailed tickets only as needed.
- A ticket is one sharp decision or investigation, not an ordinary
  implementation slice. Keep questions that cannot yet be stated sharply in
  the map's `Not yet specified` section.
- Refer to tickets by linked title in user-facing prose, never by a bare number
  or filename.
- Claim a frontier ticket before substantive work. Resolve no more than one
  strategic ticket per session, except explicitly parallel research tickets.
- Execution may occur inside a ticket only when its decision criteria specify
  the uncertainty, deterministic inputs, stopping bound, advancement branch,
  redirection branch, closure branch, and independent certificate.
- Put detailed reasoning in the ticket resolution. The map gets only a linked
  one-line gist; experiment notes and derived artifacts remain the evidence
  layer.
- When a resolution exposes a sharp next question, create and wire a ticket.
  Keep indistinct in-scope work in the fog. Close work beyond the destination
  into `Out of scope`, not `Decisions so far`.

## Sol/Fable review integrated with Wayfinder

The read-only dual-review harness in `scripts/adversarial_review.py` is the
standard adversarial second look for consequential Wayfinder decisions.

- Run a bounded Sol/Fable review before selecting or changing the strategic
  route, closing a significant route, promoting a new frontier, or publishing
  a claim whose assumptions or evidence boundary are easy to overstate.
- Give both reviewers the same sharp question, declared decision criteria,
  compact committed evidence, and proposed consequence. Do not send secrets,
  credentials, private correspondence, or material not permitted to leave the
  machine.
- Inspect the two blind reviews before their reciprocal critiques. Record
  material objections, the independent checks used to address them, and the
  evidence-packet hash in the ticket.
- Reviewer agreement is advisory planning evidence only. It is not a proof,
  source citation, reproduced computation, exhaustiveness certificate, or
  authorization for an external action.
- A review must improve the ticket: add a missing control, narrow an overclaim,
  choose a cheaper discriminator, sharpen a stopping rule, or explain why an
  objection does not apply. Do not use model consensus as a ceremonial stamp.
- Keep full review runs under ignored `runs/reviews/`. Commit only a compact
  summary or hashes when the review materially affects a durable decision.

## Working with the user

- Lead with outcomes and concrete evidence. Explain assumptions and tradeoffs
  at the user's mathematical altitude.
- Give concise progress updates during long work and state what is running,
  what has been learned, and what decision the work will resolve.
- Make safe, in-scope assumptions to maintain progress. Stop for user input
  when a choice changes the mathematical destination, expands external
  authority, spends substantial resources, or triggers an irreversible action.
- A request to continue authorizes the next safe, already-scoped step; it does
  not silently broaden the research program.

## Repository and Git discipline

- Preserve unfamiliar work and unrelated user changes. Never delete or rewrite
  them merely to tidy the tree. Prefer recoverable moves for obsolete
  project-owned material.
- Commit at small logical breakpoints and run `make test` before every commit.
- Stage only intended paths. Do not commit incomplete runs or secrets.
- Push each completed, tested breakpoint when a remote is configured so machine
  failure or chat loss does not erase the research state.
- Keep durable context in committed files, not only in conversations. A fresh
  agent should be able to recover the destination, frontier, evidence, and next
  command from the repository alone.

## Project-specific choices to fill in

Replace this section with the project's preferred systems and domain rules:

- primary proof assistant or CAS, if any;
- numerical certification standard;
- source and data licenses;
- expected theorem and artifact formats;
- resource budgets for long computations;
- domain-specific checks that must remain independent;
- neighboring repositories or services that are read-only references.
