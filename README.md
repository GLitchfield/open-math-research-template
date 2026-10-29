# Open Mathematics Research Template

A starting point for a math research project run with AI agents, where the goal is clear but the route to it isn't. My [Erdős–Szekeres project](https://github.com/GLitchfield/erdos-szekeres-convex-poly) started from it.

It sets up four things:

1. **A decision map** (`docs/wayfinder/`). The map records the goal, the open strategic questions, and the decisions made so far. Each open question gets its own ticket, so a long investigation stays organized across sessions.
2. **Bounded experiments** (`docs/experiments/`). Each experiment states its question and its possible outcomes before it runs, and records its inputs, code version and results.
3. **Independent checks and evidence levels.** Results are labeled by how they were established, from a proof to a heuristic, and important results get a check from code separate from the code that produced them.
4. **A two-model review** (`scripts/adversarial_review.py`). Claude and OpenAI's Codex each review the same evidence for a decision, first separately and then by critiquing each other's answer once.

The template doesn't assume a particular field, proof assistant or computer algebra system.

## How a project moves

```text
goal -> open question (ticket) -> possible outcomes declared -> bounded work
     -> independent checks -> two-model review -> decision recorded
     -> next open question
```

## Start a project

1. Use this repository as a GitHub template, or clone it into a new repository.
2. Replace the bracketed project and goal text in `AGENTS.md`, `README.md` and `docs/wayfinder/map.md`.
3. Record the project's tools, mathematical conventions, source policies and computation budgets in `AGENTS.md`.
4. Create the first ticket from `templates/decision-ticket.md`.
5. Run:

   ```console
   make test
   python3 scripts/wayfinder_status.py
   ```

6. Commit and push this starting state before beginning a long investigation.

## Repository layout

```text
AGENTS.md                    instructions for AI agents working in the repository
.codex/skills/open-math-wayfinder/ the decision-map workflow as a Codex skill
docs/wayfinder/map.md        the goal and an index of decisions
docs/wayfinder/tickets/      one strategic question per file
docs/experiments/            numbered experiment notes
docs/research_log.md         index of experiments and their results
data/reference/              read-only research inputs
data/derived/                small committed results and certificates
runs/                        checkpoints, logs and review transcripts (not committed)
scripts/wayfinder_status.py  checks which tickets are open or blocked
scripts/adversarial_review.py the two-model review
templates/                   ticket, experiment and review-question templates
```

## Two-model review

The review script sends Claude and Codex the same evidence files, with line numbers and SHA-256 hashes so the review can be traced to exact inputs. Each model answers on its own, then critiques the other's answer once. Neither model can write to the repository or use other research tools during the review.

```console
python3 scripts/adversarial_review.py doctor

python3 scripts/adversarial_review.py run \
  --question-file runs/reviews/question.txt \
  --evidence docs/wayfinder/tickets/0001-example.md \
  --evidence docs/experiments/0001-example.md \
  --claude-model CLAUDE_MODEL_ID \
  --codex-model CODEX_MODEL_ID \
  --output runs/reviews/0001-route-review
```

Replace `CLAUDE_MODEL_ID` and `CODEX_MODEL_ID` with whichever Claude and Codex models you want to use. The script has no default for either, and it records both in the run's provenance. In my projects I called the two reviewers Fable and Sol.

The review sends the evidence files to both model providers, so never include secrets or anything that can't leave your machine. A review is advice for making a decision. It is not a proof or an independent computation. See `docs/adversarial-review.md`.

## Requirements

- Python 3.11 or newer (the core scripts use only the standard library)
- Git
- the `claude` and `codex` command-line tools, for the review
- whatever proof assistant or computer algebra system the project uses

## Attribution

The decision map adapts Matt Pocock's MIT-licensed [Wayfinder skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md). See `NOTICE` for the upstream copyright notice and a summary of the changes.

## License

MIT. See `LICENSE` and `NOTICE`.
