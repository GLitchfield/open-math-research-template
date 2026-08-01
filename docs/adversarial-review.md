# Sol/Fable adversarial review

`scripts/adversarial_review.py` asks Claude Fable and Codex Sol to review the
same explicit evidence packet independently, then optionally gives each one
opportunity to criticize the other's answer. The output is advisory. It is not
a mathematical proof, reproduced computation, literature source, or
exhaustiveness certificate.

## Trust boundary

The harness does not give either reviewer a writable repository. It combines
only explicitly requested UTF-8 files into a packet with stable displayed line
numbers and SHA-256 provenance. Claude runs in safe mode without tools, MCP
servers, or session persistence. Codex runs ephemerally in a temporary
directory with a read-only sandbox and no web search. Both are told to use only
the packet, and citations outside the packet are rejected.

The vendor clients still contact their providers, and the packet is
transmitted to those providers. Never include secrets, credentials, private
correspondence, unpublished restricted material, or anything not permitted to
leave the machine.

Check installed clients and Claude subscription authentication without
displaying account identifiers:

```console
python3 scripts/adversarial_review.py doctor
```

## Protocol

1. Commit the code and evidence under review. Dirty repositories are rejected
   unless `--allow-dirty` is explicit and the dirty fingerprint is intentional.
2. Put one bounded, decision-relevant question in a text file, usually under
   ignored `runs/reviews/`.
3. Name every evidence file explicitly. Directories, binary files, external
   paths, and oversized packets are rejected.
4. Pin both model identifiers. Claude defaults to `claude-fable-5`; Codex has
   no moving default.
5. Inspect both blind answers before their reciprocal critiques.
6. Independently check material objections. Record their disposition and the
   packet hash in the Wayfinder ticket.

```console
python3 scripts/adversarial_review.py run \
  --question-file runs/reviews/question.txt \
  --evidence docs/wayfinder/tickets/0001-question.md \
  --evidence docs/experiments/0001-result.md \
  --codex-model gpt-5.6-sol \
  --output runs/reviews/0001
```

The default reciprocal round requires four provider calls. Use `--rounds 0`
for a cheaper blind comparison.

## Outputs and restart behavior

Each run records a manifest, exact evidence packet, structured blind and
critique answers, raw client output, and a compact `REPORT.md`. Completed stages
are written atomically and can resume only when question, evidence, Git state,
models, timeout, and round count still match.

Keep full runs ignored. When a review materially informs a decision, commit a
compact summary or the packet/report hashes with an unmistakable advisory
label. Do not publish raw provider output automatically.

## Good review questions

- Does the evidence establish the exact sentence proposed for publication?
- Which conclusion depends on an unstated mathematical or computational
  assumption?
- What counterexample or independent calculation would most efficiently
  falsify the interpretation?
- Does the verifier check the same property the producer claims?
- Are the stopping and redirection rules capable of distinguishing structural
  failure from precision or verification limits?

Avoid asking whether the project is simply “correct.” Broad approval invites
false confidence and weakens the evidence boundary.
