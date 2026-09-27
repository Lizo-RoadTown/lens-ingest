# lens-ingest — build-out plan (self-directed)

This is lens-ingest's own plan for working itself out. Work top-down; check items off
and append what you learned. Precedent to consult (not to copy as identity): the decomposition method +
PROVES run log in the lens-core repo (github.com/Lizo-RoadTown/lens-core —
`docs/decomposition/proves/process-log.md` and `skills/decomposition/SKILL.md`),
the PROVES source itself (read-only), and the PROVES spine
`staging_extractions → validation_decisions → core_entities`.

## What lens-ingest must become

- [ ] **1. A source reader.** Fetch source material — web / file / github. A small,
  swappable reader interface so a lab injects which sources it draws from as config,
  not code.
- [ ] **2. A candidate builder.** Map a source → `candidates` rows with the evidence
  that backs each one, and the `sources` rows that record where it came from.
- [ ] **3. Write to the standard.** Write `candidates` + `sources` via the injected
  `LENS_DB_URL` — against the schema defined in **lens-core**, never a hardcoded shape.
- [ ] **4. The `ingest` CLI.** Runs reader → builder → write end-to-end. Add a
  `--dry-run` that prints the candidate rows it *would* write without connecting
  (testable with no DB).
- [ ] **5. Tests.** Reader (mocked fetch), builder (source → rows mapping),
  `--dry-run` output. Mirror the stdlib + pytest style of `tapestry-cli`.

### Migrate-from (precedent, generalize — do not copy as identity)
- PROVES `extraction-api/app.py` — queueing.
- PROVES `extraction-api/worker.py` + `processors/` — fetch + dispatch.
- PROVES `production/Version 3/extractor_v3.py` — fetch tools; and `task_builder.py`
  — prompt construction (the cleanest standalone piece).

### AVOID these PROVES anti-patterns
- Parsing LLM prose as control flow (`base.py` / `agent_v3.py`) — use **structured
  returns** instead.
- Hardcoded `sys.path`.
- Inline DB-URL — the connection is injected via `LENS_DB_URL`.

## What you own vs. don't
Own: `sources` + `candidates` writes. Do NOT implement review/promotion, serve, or
observe here — those are the sibling repos. lens-ingest only captures and stages.

## Record as you go
Append here: what you built, what you needed, what's missing, what you had to decide.
Also write it to loom-memory scoped to `lens-ingest`. This log is capture-before-loss.
