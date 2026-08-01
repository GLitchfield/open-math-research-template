# Issue tracker: committed local Markdown

Wayfinder strategic decisions live under `docs/wayfinder/` and are committed
and pushed with the evidence they govern. This tracker is intentionally
narrower than a general implementation backlog.

The upstream Wayfinder skill supports tracker-specific storage and falls back
to local Markdown. This template makes tracked Markdown the default so
strategic state survives machine loss, branch changes, context compaction, and
provider changes. Do not create a parallel scratch or GitHub-issue map unless a
recorded decision migrates the canonical tracker.

## Conventions

- The canonical map is `docs/wayfinder/map.md`.
- Decision tickets are files under `docs/wayfinder/tickets/`.
- Numeric filename prefixes provide stable ordering only; prose uses linked
  ticket titles.
- Front matter records type, mode, status, claim, and blockers.
- Detailed resolutions live in tickets. The map receives a one-line linked
  gist.
- Numbered experiment notes and derived artifacts remain the evidence layer.

## Wayfinding operations

- **Map:** `docs/wayfinder/map.md`.
- **Child ticket:** copy `templates/decision-ticket.md` into
  `docs/wayfinder/tickets/NNNN-short-title.md`.
- **Blocking:** list ticket filenames in `blocked_by`. A ticket is unblocked
  when every blocker is closed.
- **Frontier:** run `python3 scripts/wayfinder_status.py`.
- **Claim:** replace `claim: unclaimed` before substantive work.
- **Resolve:** write the answer under `## Resolution`, link evidence, set
  `status: closed`, and append one linked gist to the map.
- **New visibility:** create newly sharp tickets; keep indistinct in-scope work
  in `Not yet specified`; move beyond-destination work to `Out of scope`.
- **Durability:** validate, commit, and push the decision state together with
  the evidence it governs.

If the project deliberately migrates to GitHub Issues or another tracker,
document the mapping, migrate all open decisions and blockers once, update
`AGENTS.md`, and retire this tracker rather than operating two canonical maps.
