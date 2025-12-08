# Documentation Review Progress (Temporary)

> Tracking which docs have been reviewed and how they were aligned with the new methodology.

## Legend

- **Status**
  - `DONE` – Reviewed and aligned with: `/speckit-context → /speckit-constitution → /speckit-specify` (triage optional), English-only, and Project Rules as primary AI rules where applicable.
  - `PARTIAL` – Touched, but still has items to revisit.
  - `PENDING` – Not yet reviewed in this refactor.

---

## Core Methodology & Entry Docs

| File | Status | Main Changes / Checks |
|------|--------|------------------------|
| `Project Rules` | DONE | Made it the primary AI rules doc; clarified that specs are iterative/multi-round; set default flow to `/speckit-context → /speckit-constitution (minimal rails) → /speckit-specify`; made `/speckit-triage` optional and multi-round; ensured English-only. |
| `README.md` | DONE | Updated intro to be more user-oriented and benefit-focused; added an explicit line for users who are currently coding by vibe with AI and want to move to a visual, spec-driven, PDCA-aligned workflow; made the "Why Spec Orchestrator" section speak explicitly to vibe coding pain points and PDCA distortion; updated Quick Start and workflows to use the new default flow; simplified the Mermaid command-sequence diagram (removed init directive and changed node syntax to quoted labels) to avoid renderer lexical errors; removed `.windsurf` references; aligned project structure with `commands/`; clarified triage as optional helper for large/mixed input; recommended configuring `Project Rules` as project/IDE rules/system prompt; added attribution to GitHub Spec Kit and the adaptation by Rodrigo Trindade; ensured Quick Start text is fully English-only. |
| `CATALOG.md` | DONE | Set Project Rules as first AI reading source; adjusted documentation structure; clarified multi-round `/speckit-specify`; marked triage as optional; ensured English-only descriptions; noted `.specify/` as the Spec Orchestrator toolkit adapted from GitHub Spec Kit; aligned `project-lifecycle.md` description with context + constitution baseline and triage as optional helper. |

---

## Command Docs (`commands/`)

| Command Doc | Status | Main Changes / Checks |
|-------------|--------|------------------------|
| `speckit-context.md` | DONE | Clarified creation/update of `project-workplan.md` and `project-overview.md`; aligned "Next steps" to recommend `/speckit-constitution` as default and `/speckit-triage` as optional for large/mixed input; removed remaining Portuguese. |
| `speckit-constitution.md` | DONE | Documented early use for minimal rails at project start and later consolidation of backlog/learning; clarified behavior when triage backlog is empty; translated all guidance to English. |
| `speckit-specify.md` | DONE (no major structural change) | Confirmed multi-round, iterative nature; verified that it works both with triage backlog and direct conversational input; ensures updates to `project-overview.md` and `project-workplan.md`. |
| `speckit-triage.md` | DONE | Reframed as optional command for large/mixed input (voice, docs, brain dumps); added/translated "When to use" section; clarified that it feeds constitution/specify and can update overview/workplan. |
| `speckit-plan.md` | DONE | Updated initialization to point to `/speckit-context` (not triage) when `project-context/` is missing; removed Portuguese fragments; kept plan as main updater of overview/workplan. |
| `speckit-tasks.md` | DONE | Removed remaining Portuguese terms; kept rules for generating `tasks.md` and updating overview/workplan. |
| `speckit-implement.md` | DONE (validated) | Confirmed it only depends on existing `tasks.md`/context; no hard dependency on triage; language already in English. |
| `speckit-analyze.md` | DONE (validated) | Read-only consistency checker respecting constitution as non-negotiable; no required changes for new flow; English-only. |
| `speckit-checklist.md` | DONE (validated) | Checklists as "unit tests for requirements"; no triage assumptions; English-only. |
| `speckit-taskstoissues.md` | DONE (validated) | Simple bridge from `tasks.md` to GitHub issues; no methodological conflicts; English-only. |

---

## Flow Docs (`.specify/docs/flows/`)

| Flow Doc | Status | Main Changes / Checks |
|----------|--------|------------------------|
| `project-lifecycle.md` | DONE | Default path set to `/speckit-context → /speckit-constitution (minimal rails) → /speckit-specify`; triage shown as optional branch; artifacts update table clarifies triage is optional; diagrams updated accordingly. |
| `overview.md` | DONE | "Complete Workflow" diagram now branches on input type/size; `/speckit-context` is default; triage is optional helper feeding constitution/specify; Command Purpose Matrix uses a generic router instead of forcing triage-first. |
| `decision-tree.md` | DONE | Artifact State Decision now recommends `/speckit-context` then `/speckit-constitution` when starting fresh; Example 1 (Complete New Feature) shows default conversational path with triage as optional; Anti-Patterns "Right" side emphasizes context-first and triage only for large/mixed input. |
| `triage-system.md` | DONE (validated) | Describes internals of triage, backlogs, and consumers (`speckit-constitution`, `speckit-specify`); no claim that triage is mandatory; consistent with triage as an optional system. |
| `entry-lifecycle.md` | DONE (validated) | Focused on triage entry states and artifact absorption; independent of whether triage is mandatory; consistent with backlog semantics. |
| `triage-system.md` | DONE (validated) | Architecture of triage backlogs and consumers; no need for flow order changes; English-only. |

---

## Methodology & Agent Docs (`.specify/docs/`)

| Doc | Status | Main Changes / Checks |
|-----|--------|------------------------|
| `sdp-pdca.md` | DONE | PLAN phase now encodes default flow (`context → constitution → specify → clarify → plan`) with triage explicitly marked as optional for large/mixed input; detailed PLAN diagram, metrics, full-iteration example, and quick reference all updated to respect this; English-only maintained. |
| `agent-context.md` | DONE | Reading priority set to: `Project Rules` → `project-context/` (if exists) → `constitution.md` → `spec.md` → `plan.md` → `tasks.md`; removed suggestion to "proceed with defaults" when constitution is missing, recommending `/speckit-constitution` to create minimal rails instead. |
| `project-rhythm.md` | DONE | Feature and macro rhythms no longer assume triage as mandatory; project setup uses context + constitution (triage if needed); feature PLAN section uses specify with triage marked as optional. |
| `best-practices.md` | DONE (one template line pending manual tweak) | "Correct Flow" now shows `/speckit-context → /speckit-constitution → /speckit-specify → /speckit-plan → /speckit-tasks → /speckit-implement` as default, with `/speckit-triage` as optional helper for large/mixed input. |
| `glossary.md` | DONE (validated) | Definitions of triage, commands, and artifacts are consistent with triage as an optional system and the current file locations; no changes required. |
| `memory-system.md` | DONE (validated) | Memory architecture now treats Project Rules as the primary AI rules doc; query checklist and contextual memory no longer reference `specrules.md` or `.windsurf` system prompts. |
| `migration-guide.md` | DONE (validated) | Migration steps and checklists mention triage only as part of setting up a workflow; they do not contradict the new default flow or force triage as mandatory. |
| `examples.md` | DONE | Authentication example still showcases the triage-based path, but Phase 0 now positions `/speckit-context` as the recommended first step and explains that `/speckit-triage` is used here because the input is large/mixed; workplan text clarifies that context/specify/plan/tasks/implement primarily maintain the orchestration. |
| `.specify/docs/README.md` | DONE (validated) | Documentation index and navigation only; no embedded methodology flow beyond the iterative completeness principle. |

---

## Notes

- This file is **temporary** and meant only to track the documentation refactor.
- Once the refactor is complete and validated (including `docs_analysis.json`), this file can be removed or converted into a permanent changelog section.
