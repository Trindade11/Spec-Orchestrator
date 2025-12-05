# Spec Orchestrator - Document Catalog

> Complete catalog of all documentation in the project with descriptions and purposes

**Generated**: 2024-12-05 | **Documents**: 49 | **Total Size**: ~87k tokens (347k characters)

---

## 📁 Project Structure

```
Spec Orchestrator/
├── .windsurf/               # IDE-specific configurations and workflows
│   ├── rules/              # Project rules for AI agents
│   └── workflows/          # Automated workflow definitions
├── .specify/               # Spec Kit methodology toolkit
│   ├── docs/              # Methodology documentation
│   ├── memory/            # Project constitution
│   ├── scripts/           # Automation scripts
│   ├── templates/         # Document templates
│   └── triage/            # Triage backlog system
├── project-context/        # Project-specific technical context (created by /speckit-context)
└── specs/                  # Feature specifications (created by /speckit-specify)
```

---

## 🏛️ Core Files (Start Here)

### `.windsurf/rules/specrules.md` (6.3k chars)
**Purpose**: **MANDATORY** reading for all AI agents - defines behavioral rules and workflow integration  
**Contains**:
- Spec Kit integration (11 commands with purposes)
- Visual modeling requirements (Mermaid mandatory in specs/plans, gap notation standards)
- Project lifecycle flow (progressive Macro → Micro with decision points)
- Communication style (user-centric, clear language, complete commands)
- Stack consistency (respect plan.md choices)
- **Golden Rule**: Iterative Completeness - "🔄 Need another round?" is MANDATORY
- Source of truth hierarchy (constitution → context → docs → templates)

**Critical for**: AI agents starting ANY interaction with this project  
**When to read**: ALWAYS FIRST - before any work

### `.specify/memory/constitution.md` (7.3k chars)
**Purpose**: The project's **governing document** - principles that apply to ALL features  
**Contains**:
- 12 core principles including:
  - Visual Modeling First (diagrams are mandatory, not optional)
  - User-Centric Communication (explain for non-developers)
  - Established Components (use mainstream, documented libraries)
  - Test-First Development (tests before implementation)
  - Traceability (every code line → requirement link)
  - Iterative Completeness (the "Need another round?" rule)
- 3 quality gates with explicit checklists:
  - Gate 1: Specification Ready (process flow, prioritized stories, ≤3 clarifications)
  - Gate 2: Plan Ready (architecture diagram, tech stack, constitution check)
  - Gate 3: Implementation Ready (tasks broken down, criteria defined, dependencies mapped)
- Governance (versioning with semantic vX.Y.Z, amendment process)

**Critical for**: Understanding non-negotiable project constraints  
**When to read**: Before /speckit-specify, /speckit-plan, /speckit-implement

### `project-context/project-workplan.md` (template: 3.0k chars)
**Purpose**: 🎯 **ORCHESTRATION ENGINE** - The AI's navigation system  
**Contains**:
- **Current phase** (exactly which step of PLAN/DO/CHECK/ACT you're in)
- **Next recommended action** (which `/speckit-*` command to run)
- **Agent execution plan** with status (TODO → IN_PROGRESS → DONE)
- **Decision points tracking**:
  - DP1: Project Structure (folder organization)
  - DP2: Tech Stack (technologies and frameworks)
- **Triage rounds log** (progressive refinement history)
- **Backlog summary** (pending constitution vs specification entries)
- **Project initialization checklist** (setup progress tracking)

**Critical for**: Knowing **exactly** what to do next  
**When to read**: **FIRST** - before any command execution  
**Updated by**: Every `/speckit-*` command must update this

### `project-context/project-overview.md` (template: 4.2k chars)
**Purpose**: 📊 **MACRO DASHBOARD** - Single-page project health view  
**Contains**:
- **High-level description** (elevator pitch of the project)
- **Main functional blocks diagram** (Mermaid flowchart with gap notation `[?]`)
- **Global project mindmap** (Business, Users, Capabilities, Technical, Risks)
- **Completion status tables**:
  - By artifact (constitution, specs, plans, tasks, code)
  - By functional block (% complete, status 🟢🟡🔴)
- **Identified gaps** categorized:
  - Critical gaps (blockers)
  - Gaps of attention (important but not blocking)
- **Next steps** (clear action items)
- **Version history** (V1, V2, V3... with timestamps)
- **Quick links** (to key project artifacts)

**Critical for**: Understanding **where the project is** and **what's missing**  
**When to read**: After workplan - for context on current state  
**Updated by**: Every significant command (versions increment on major changes)

---

## 🔀 Workflows (.windsurf/workflows/)

### `/speckit-triage` (12.2k chars)
**Purpose**: **Content router** - Separates "rules for all features" from "specific feature requests"  
**Philosophy**: Not everything is a feature; some are principles  
**Input**: Mixed/broad user input (vision, ideas, constraints, features)  
**Output**: 
- `triage_constitution.md` - Backlog of principles ("Always...", "Never...", "Use X for...")
- `triage_specification.md` - Backlog of features ("Build a...", "User can...", specific workflows)
- `project-workplan.md` - Updated with round log and phase status
- `project-overview.md` - Refined with macro blocks and identified gaps

**Key feature**: **Multi-round design** (not one-shot)  
- Round 1: Initial vision, project type, high-level goals
- Round 2..N: Progressive refinement of personas, use cases, constraints
- Exit when: Macro view stable + at least one feature ready to specify

**Use when**: Starting a project or major scope change

### `/speckit-context` (7.8k chars)
**Purpose**: Initialize or update project-context/ folder  
**Creates**:
- `project-workplan.md` - orchestration plan
- `project-overview.md` - macro dashboard
- `env-vars.md` - environment variables
- `database-schema.md` - database structure
- `tools-registry.md` - MCPs and tools
- `agent-framework.md` - agent architecture
- `folder-structure.md` - project organization

**When to run**: Step 0 of new projects

### `/speckit-constitution` (6.9k chars)
**Purpose**: Create/update constitution from triage backlog  
**Input**: Pending entries from `triage_constitution.md`  
**Output**: Updated `.specify/memory/constitution.md`  
**Key feature**: Semantic versioning of constitution (MAJOR.MINOR.PATCH)

### `/speckit-specify` (12.1k chars)
**Purpose**: Create feature specifications (WHAT and WHY)  
**Input**: Feature description or triage backlog  
**Output**: `specs/###-feature-name/spec.md` with:
- Process flow diagram (Mermaid - business language)
- User stories (prioritized P1/P2/P3)
- Functional requirements (FR-001, FR-002...)
- Success criteria (measurable, technology-agnostic)
- Acceptance scenarios (Given/When/Then)

**Quality limit**: Maximum 3 `[NEEDS CLARIFICATION]` markers allowed

### `/speckit-clarify` (11.5k chars)
**Purpose**: Resolve ambiguities in specifications through structured questions  
**Input**: Current spec with gaps  
**Output**: Updated spec with clarifications integrated  
**Key feature**: 
- Maximum 5 questions per session
- Provides recommended answers based on best practices
- Updates spec atomically after each answer

### `/speckit-plan` (5.3k chars)
**Purpose**: Create technical implementation plans (HOW)  
**Input**: Feature specification  
**Output**: `plan.md` with:
- System interaction diagram (sequenceDiagram - technical)
- Component architecture (flowchart)
- Tech stack decisions
- API contracts
- Data model
- Research findings

**Phases**: Research (Phase 0) → Design & Contracts (Phase 1)

### `/speckit-tasks` (missing - referenced in /speckit-implement)
**Purpose**: Break plan into actionable tasks  
**Output**: `tasks.md` with task breakdown, dependencies, acceptance criteria

### `/speckit-implement` (9.7k chars)
**Purpose**: Execute implementation following tasks.md  
**Prerequisites**: Checklists must pass (or user override)  
**Process**:
1. Verify checklists
2. Load context (plan.md, tasks.md, project-context/)
3. Create/verify ignore files
4. Execute tasks phase-by-phase
5. Update project-overview.md and project-workplan.md

**Execution order**: Setup → Tests → Core → Integration → Polish

### `/speckit-analyze` (7.3k chars)
**Purpose**: Cross-artifact consistency analysis  
**Input**: spec.md, plan.md, tasks.md  
**Output**: Read-only analysis report with:
- Duplication detection
- Ambiguity detection
- Constitution alignment check
- Coverage gaps
- Inconsistencies

**Severity levels**: CRITICAL, HIGH, MEDIUM, LOW

### `/speckit-checklist` (12.1k chars)
**Purpose**: Generate quality checklists (UNIT TESTS FOR REQUIREMENTS)  
**Philosophy**: Checklists validate requirements quality, NOT implementation  
**Output**: Domain-specific checklist files (e.g., `ux.md`, `security.md`, `api.md`)  
**Quality dimensions**:
- Completeness
- Clarity
- Consistency
- Measurability
- Coverage
- Edge cases

**Key rule**: Items must test REQUIREMENTS, not code behavior

### `/speckit-taskstoissues` (1.2k chars)
**Purpose**: Convert tasks to GitHub issues  
**Prerequisites**: 
- GitHub remote configured
- tasks.md exists
- GitHub MCP server available

---

## 📚 Documentation (.specify/docs/)

### Core Documentation

#### `README.md` (1.9k chars)
Navigation hub for all documentation with quick links

#### `glossary.md` (6.6k chars)
Complete terminology reference:
- Core concepts (SDD, Constitution, Specification, Plan, Tasks)
- Triage system terms
- Command definitions
- Diagram types and notation
- Requirements taxonomy
- User story format
- Abbreviations

#### `best-practices.md` (9.3k chars)
Guidelines and anti-patterns:
- Golden Rules (0-6)
- "Need Another Round?" practice (mandatory)
- Do's and Don'ts with visual comparisons
- Common anti-patterns and fixes
- Quality checklists per phase
- Naming conventions
- Iteration guidelines
- Communication templates

#### `agent-context.md` (12.9k chars)
**Critical for AI agents** - How to interpret and use artifacts:
- Reading priority (project-context → constitution → spec → plan → tasks)
- Artifact interpretation guide
- Decision making when conflicts arise
- Output guidelines
- Code generation rules
- Context synchronization
- Triage backlog consumption
- Error handling

#### `examples.md` (16.8k chars)
Complete feature walkthrough showing all artifacts in practice

#### `migration-guide.md` (12.3k chars)
How to adopt Spec Kit in existing projects

### Visual Flows (.specify/docs/flows/)

#### `FLOWS.md` (2.5k chars)
Index of all visual flow diagrams

#### `overview.md` (7.1k chars)
SDD methodology overview with complete workflow visualization

#### `project-lifecycle.md` (10.9k chars)
Progressive project evolution (Macro → Micro):
- V1: After triage (macro blocks with gaps)
- V2: After specs (detailed connections)
- V3+: After plans and implementation (technical view)
- Multi-round triage process
- Decision points
- Refinement flow

#### `command-flow.md` (16.4k chars)
Detailed flow for each command with decision trees

#### `triage-system.md` (8.2k chars)
Backlog system architecture:
- Classification criteria
- File structure (constitution/specification backlogs + log)
- Consumer behavior
- Scope change detection

#### `gap-notation.md` (6.8k chars)
Standards for visualizing gaps in diagrams:
- `[?]` suffix for unclear steps
- `:::gap` class for incomplete areas
- Red/orange styling
- Dashed lines for uncertain connections

#### `artifact-relationships.md` (9.3k chars)
How artifacts relate and depend on each other

#### `entry-lifecycle.md` (9.3k chars)
Lifecycle of triage entries from creation to absorption

#### `decision-tree.md` (9.9k chars)
Decision trees for choosing commands and actions

---

## 🎨 Templates (.specify/templates/)

### Core Templates

#### `spec-template.md` (5.4k chars)
Feature specification structure:
- Process flow diagram (mandatory)
- Agent collaboration (if multi-agent)
- User stories with priorities (P1/P2/P3)
- Functional requirements
- Success criteria
- Key entities
- Acceptance scenarios

#### `plan-template.md` (5.8k chars)
Implementation plan structure:
- System interaction diagram (sequenceDiagram)
- Component architecture (flowchart)
- Technical context
- Constitution check
- Research phase
- Design & contracts phase
- Data model
- API contracts

#### `tasks-template.md` (9.1k chars)
Task breakdown structure with phases and dependencies

#### `checklist-template.md` (1.3k chars)
Quality gate checklist structure

#### `agent-file-template.md` (464 chars)
Template for agent-specific context files

### Project Context Templates (.specify/templates/project-context/)

#### `README.md` (4.0k chars)
Guide to project-context/ folder

#### `project-workplan-template.md` (3.0k chars)
Orchestration plan template

#### `project-overview-template.md` (4.2k chars)
Macro dashboard template with mindmap

#### `env-vars-template.md` (3.0k chars)
Environment variables documentation

#### `database-schema-template.md` (6.5k chars)
Database schema with semantic meanings

#### `tools-registry-template.md` (5.7k chars)
MCPs and tools inventory

#### `agent-framework-template.md` (7.1k chars)
Agent architecture documentation

#### `folder-structure-template.md` (6.0k chars)
Project organization guide

### Methodology Documents (.specify/docs/)

#### `sdp-pdca.md` (18.5k chars)
**Purpose**: Complete integration of PDCA methodology with Spec-Driven Development  
**Contains**:
- Philosophy and comparison (Traditional PDCA vs SDP-PDCA)
- Complete SDP-PDCA cycle with visual flow
- Detailed breakdown of all 4 phases:
  - **PLAN**: Context → Triage → Constitution → Specify → Clarify → Design
  - **DO**: Tasks → Implementation (5 phases: Setup, Tests, Core, Integration, Polish)
  - **CHECK**: 6-level validation (artifacts, quality, tests, acceptance, constitution, user)
  - **ACT**: Categorized refinement + learning capture
- Integration with project artifacts (workplan, overview, constitution, specs, plans, tasks)
- Metrics and KPIs for each phase
- Complete example (User Authentication feature walkthrough)
- Key differentiators from traditional PDCA
- Benefits mindmap
- Quick reference card

**Critical for**: Understanding the complete methodology cycle  
**When to read**: When learning the methodology or planning iterations

#### `memory-system.md` (15.8k chars)
**Purpose**: Continuous project state management and update protocols  
**Contains**:
- Multi-layered memory architecture (4 types: Persistent, Versioned, Transient, Contextual)
- Automatic update mechanisms (workflow-triggered per command)
- 3-step sync protocol after every significant change
- 4 memory consistency rules (source of truth hierarchy, version sync, timestamps, gap propagation)
- Memory query patterns for AI agents starting work
- Query optimization decision tree
- Daily integrity check checklist
- Memory maintenance tasks and garbage collection
- Memory evolution timeline (Week 1 → Month 6)
- AI agent memory guidelines with pseudocode
- Memory-driven development loop (READ → WORK → WRITE → VERIFY)
- Best practices (DO's and DON'Ts)
- Future enhancements planned

**Critical for**: Ensuring project always knows its current state  
**When to read**: When setting up workflows or debugging inconsistencies

---

## 🔧 Scripts (.specify/scripts/powershell/)

### `check-prerequisites.ps1` (4.8k chars)
**Purpose**: Validate prerequisites for any command  
**Modes**:
- `-Json`: Return paths as JSON
- `-PathsOnly`: Return only paths (minimal)
- `-RequireTasks`: Ensure tasks.md exists
- `-IncludeTasks`: Include tasks content

### `create-new-feature.ps1` (10.8k chars)
**Purpose**: Initialize new feature branch and folder structure  
**Creates**:
- Feature branch `###-feature-name`
- `specs/###-feature-name/` folder
- Copies templates (spec.md, plan.md, tasks.md)

### `setup-plan.ps1` (1.9k chars)
**Purpose**: Setup planning phase prerequisites

### `update-agent-context.ps1` (19.9k chars)
**Purpose**: Update agent-specific context files  
**Supports**: Cursor, Claude, Windsurf, and other AI agents  
**Features**:
- Auto-detects AI agent type
- Preserves manual additions
- Updates technology context
- Manages markers for safe updates

### `common.ps1` (3.8k chars)
**Purpose**: Shared PowerShell utilities

---

## 🗂️ Triage System (.specify/triage/)

### `triage_constitution.md` (441 chars)
Backlog for Constitution principles and rules

### `triage_specification.md` (468 chars)
Backlog for Specification features

### `triage_log.json` (124 chars)
Metadata and history of triage sessions

---

## 📊 Statistics by Category

| Category | Files | Total Chars | Purpose |
|----------|-------|-------------|---------|
| **Workflows** | 11 | 92,434 | Command execution logic |
| **Docs** | 15 | 140,228 | Methodology guides |
| **Templates** | 14 | 65,594 | Artifact structures |
| **Scripts** | 5 | 41,182 | Automation utilities |
| **Memory** | 1 | 7,280 | Project constitution |
| **Triage** | 3 | 1,033 | Backlog system |
| **TOTAL** | **49** | **347,751** | Complete system |

---

## 🎯 Reading Sequences

### For New Users
1. `CATALOG.md` (this file)
2. `.specify/docs/README.md`
3. `.specify/docs/overview.md`
4. `.specify/docs/glossary.md`
5. `.specify/docs/best-practices.md`

### For AI Agents
1. `.windsurf/rules/specrules.md` ⭐ ALWAYS READ FIRST
2. `project-context/project-workplan.md` (if exists)
3. `project-context/project-overview.md` (if exists)
4. `.specify/memory/constitution.md`
5. `.specify/docs/agent-context.md`
6. Relevant feature specs/plans/tasks

### For Contributors
1. `.specify/docs/migration-guide.md`
2. `.specify/docs/best-practices.md`
3. `.specify/templates/` (understand structure)
4. `.specify/docs/flows/` (understand methodology)

---

## 🔍 Quick Reference

### Find Documentation About...

| Topic | File |
|-------|------|
| **Commands** | `.windsurf/workflows/*.md`, `glossary.md` |
| **Diagrams** | `flows/gap-notation.md`, `best-practices.md` |
| **AI Agent Rules** | `.windsurf/rules/specrules.md`, `agent-context.md` |
| **Constitution** | `.specify/memory/constitution.md` |
| **Project Lifecycle** | `flows/project-lifecycle.md` |
| **Triage System** | `flows/triage-system.md` |
| **Templates** | `.specify/templates/*-template.md` |
| **Examples** | `examples.md` |
| **Glossary** | `glossary.md` |
| **Best Practices** | `best-practices.md` |

---

## 🔄 Maintenance

This catalog is generated from the actual project structure. To update:

```powershell
python analyze_docs.py
# Then manually update CATALOG.md based on docs_analysis.json
```

---

> **Note**: This catalog provides a map of the Spec Orchestrator documentation.  
> Each file is designed to be read independently, with cross-references for deeper understanding.
