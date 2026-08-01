# Open Mathematics Research Template

A repository template for long-horizon, AI-assisted mathematics research when
the destination is meaningful but the route is not yet known.

It combines four practices that work especially well together:

1. a durable, tracked Wayfinder decision map;
2. falsifiable and bounded computational experiments;
3. independent verification and explicit evidence levels; and
4. a read-only Sol/Fable adversarial-review harness integrated into strategic
   route selection and closure.

The template is intentionally domain-neutral. It supports pure mathematics,
computational algebra, number theory, geometry, combinatorics, formalization,
and certified numerical work without prescribing a CAS or proof assistant.

## The research loop

```text
destination -> frontier ticket -> predeclared branches -> bounded work
            -> independent checks -> Sol/Fable review -> durable decision
            -> newly visible frontier
```

Wayfinder prevents an open problem from becoming an unstructured backlog. The
review harness prevents the map from becoming self-confirming. Reproducible
evidence prevents either planning layer from being mistaken for mathematics.

## Start a project

1. Use this repository as a GitHub template or clone it into a new repository.
2. Replace the bracketed project and destination text in `AGENTS.md`,
   `README.md`, and `docs/wayfinder/map.md`.
3. Record project-specific tools, mathematical conventions, source policies,
   and computation budgets in `AGENTS.md`.
4. Create the first decision ticket from `templates/decision-ticket.md`.
5. Run:

   ```console
   make test
   python3 scripts/wayfinder_status.py
   ```

6. Commit and push the initialized research state before beginning a long
   investigation.

## Repository layout

```text
AGENTS.md                    durable instructions for AI collaborators
.codex/skills/open-math-wayfinder/ repository-local integrated workflow skill
docs/wayfinder/map.md        low-resolution destination and decision index
docs/wayfinder/tickets/      one sharp strategic question per tracked file
docs/experiments/            numbered experiment notes
docs/research_log.md         index of empirical evidence
data/reference/              authenticated, read-only research inputs
data/derived/                compact committed results and certificates
runs/                        ignored checkpoints, logs, and review transcripts
scripts/wayfinder_status.py  frontier and blocker validation
scripts/adversarial_review.py read-only Claude/Codex evidence review
templates/                   ticket, experiment, and review-question templates
```

## Sol/Fable review

The harness gives Claude Fable and Codex Sol the same explicit evidence packet,
first independently and then with one reciprocal critique round. Inputs receive
stable displayed line numbers and SHA-256 provenance. Both clients run without
repository write access or general research tools.

```console
python3 scripts/adversarial_review.py doctor

python3 scripts/adversarial_review.py run \
  --question-file runs/reviews/question.txt \
  --evidence docs/wayfinder/tickets/0001-example.md \
  --evidence docs/experiments/0001-example.md \
  --codex-model gpt-5.6-sol \
  --output runs/reviews/0001-route-review
```

This contacts the configured model providers and transmits the selected packet.
Never include secrets or material that cannot leave the machine. Review output
is advisory and must not be represented as proof or independent computation.
See `docs/adversarial-review.md`.

## Requirements

- Python 3.11 or newer for the repository utilities;
- Git;
- optional `claude` and `codex` CLIs for dual review;
- whatever proof assistants or CAS packages the mathematical project chooses.

The core validation utilities use only Python's standard library.

## Attribution

The decision-map framework adapts Matt Pocock's MIT-licensed
[Wayfinder skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md).
See `NOTICE` for the upstream copyright notice and a summary of this template's
tracked-local and computational-research adaptations.

## License

MIT. See `LICENSE` and `NOTICE`.
