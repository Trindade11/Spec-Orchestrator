# Spec Orchestrator

> A complete Spec-Driven Development (SDD) methodology toolkit for AI-assisted software development

**Version**: 1.0.0 | **License**: MIT | **Status**: Production Ready

---

## 🎯 What is Spec Orchestrator?

Spec Orchestrator is a comprehensive methodology and toolkit that enables **specification-driven development** where living specifications are the primary artifacts, and code is generated/assisted by AI agents that consume these specifications.

### Core Philosophy

```
Specifications are truth. Code is generated.
Plans evolve. Quality is built-in.
Gaps are visible. Learning is continuous.
```

**Traditional Development**:
```
Requirements → Code → Documentation (often outdated)
```

**Spec-Driven Development**:
```
Living Specification ↔ AI-Assisted Code ← Always in sync
```

---

## ✨ Key Features

### 🔄 SDP-PDCA Methodology
Continuous improvement cycle adapted for AI-assisted development:
- **PLAN**: Triage → Constitution → Specify → Clarify → Design
- **DO**: Tasks → Implementation (test-first, traceable)
- **CHECK**: 6-level validation (artifacts, quality, tests, acceptance, constitution, user)
- **ACT**: Learn, refine, iterate with versioned artifacts

### 🧠 Memory System
Continuous project state management:
- **Orchestration**: `project-workplan.md` (which agent to call next)
- **Dashboard**: `project-overview.md` (macro view with gaps)
- **Principles**: `constitution.md` (evolving rules)
- **Knowledge**: Captured in artifact versions and constitution evolution

### 📊 Visual-First
All specifications and plans MUST include Mermaid diagrams:
- Process flows (business view)
- System interactions (technical view)
- Component architecture
- Gap notation (`[?]` and `:::gap` for uncertainties)

### 🤖 AI-Native
Designed for AI agents from the ground up:
- Clear, parseable specifications
- Explicit traceability (every code line → requirement)
- Structured commands (`/speckit-*`)
- Iterative refinement ("🔄 Need another round?")

---

## 🚀 Quick Start

### Prerequisites

- Git
- Text editor or IDE (Windsurf, VS Code, Cursor, etc.)
- Markdown preview with Mermaid support

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/spec-orchestrator.git
cd spec-orchestrator

# Initialize your project
# (Windows PowerShell)
.\.specify\scripts\powershell\check-prerequisites.ps1

# (Optional) Copy methodology to your existing project
cp -r .specify /path/to/your/project/
cp -r .windsurf /path/to/your/project/
```

### First Steps

1. **Read the documentation**:
   ```
   Start with: SYSTEM-PROMPT-CONTEXT.md (for AI agents)
            or: CATALOG.md (for humans)
   ```

2. **Initialize project context**:
   ```
   Run: /speckit-context
   This creates project-workplan.md and project-overview.md
   ```

3. **Define your scope**:
   ```
   Run: /speckit-triage (multiple rounds)
   Separate principles from features
   ```

4. **Build your constitution**:
   ```
   Run: /speckit-constitution
   Consolidate project principles
   ```

5. **Create your first spec**:
   ```
   Run: /speckit-specify "Your feature description"
   ```

---

## 📚 Documentation Structure

### For First-Time Users

| Document | Purpose | Read When |
|----------|---------|-----------|
| **README.md** | Project overview | You are here! |
| **SYSTEM-PROMPT-CONTEXT.md** | Condensed context for AI | Using AI agents |
| **CATALOG.md** | Complete document inventory | Need to find something |
| `.specify/docs/README.md` | Documentation hub | Learning the methodology |

### For AI Agents

**Essential Reading Order**:
1. `.windsurf/rules/specrules.md` - Project behavior rules
2. `project-context/project-workplan.md` - Current phase & next action
3. `project-context/project-overview.md` - Macro state & gaps
4. `.specify/memory/constitution.md` - Project principles
5. `SYSTEM-PROMPT-CONTEXT.md` - Quick reference

### Core Methodology

| Document | Topic | Location |
|----------|-------|----------|
| **SDP-PDCA** | Spec-Driven Plan-Do-Check-Act | `.specify/docs/sdp-pdca.md` |
| **Memory System** | Continuous state management | `.specify/docs/memory-system.md` |
| **Project Lifecycle** | Macro → Micro evolution | `.specify/docs/flows/project-lifecycle.md` |
| **Best Practices** | Guidelines & anti-patterns | `.specify/docs/best-practices.md` |

### Visual Guides

All in `.specify/docs/flows/`:
- `overview.md` - SDD methodology overview
- `command-flow.md` - Each command detailed
- `triage-system.md` - Backlog architecture
- `gap-notation.md` - Uncertainty visualization
- `decision-tree.md` - Decision frameworks

---

## 🔀 Workflow Commands

### Available Commands (`/speckit-*`)

| Command | Purpose | Input | Output |
|---------|---------|-------|--------|
| `/speckit-context` | Initialize project context | Project info | `project-context/` folder |
| `/speckit-triage` | Separate principles from features | Mixed input | Backlogs + workplan + overview |
| `/speckit-constitution` | Create/update principles | Backlog or input | `constitution.md` |
| `/speckit-specify` | Create feature spec (WHAT/WHY) | Feature description | `spec.md` |
| `/speckit-clarify` | Resolve ambiguities | Spec with gaps | Updated `spec.md` |
| `/speckit-plan` | Create technical plan (HOW) | Spec | `plan.md` |
| `/speckit-tasks` | Break into tasks | Plan | `tasks.md` |
| `/speckit-implement` | Execute implementation | Tasks | Code + tests |
| `/speckit-analyze` | Cross-artifact analysis | Spec + plan + tasks | Analysis report |
| `/speckit-checklist` | Generate quality checklist | Spec/plan | Checklist file |
| `/speckit-taskstoissues` | Convert tasks to GitHub issues | Tasks | GitHub issues |

### Command Sequence (New Project)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryTextColor': '#000'}}}%%
flowchart LR
    CTX[/speckit-context] --> TRI[/speckit-triage]
    TRI --> CON[/speckit-constitution]
    CON --> SPE[/speckit-specify]
    SPE --> CLA[/speckit-clarify]
    CLA --> PLN[/speckit-plan]
    PLN --> TSK[/speckit-tasks]
    TSK --> IMP[/speckit-implement]
    
    style CTX fill:#d1c4e9,stroke:#512da8
    style TRI fill:#ffecb3,stroke:#ff8f00
    style CON fill:#e3f2fd,stroke:#1976d2
    style SPE fill:#f3e5f5,stroke:#7b1fa2
    style PLN fill:#fff8e1,stroke:#f57f17
    style IMP fill:#e8f5e9,stroke:#4caf50
```

---

## 📁 Project Structure

```
spec-orchestrator/
├── .windsurf/                  # IDE configurations
│   ├── rules/
│   │   └── specrules.md       # AI agent behavior rules
│   └── workflows/
│       └── speckit-*.md       # Command definitions
│
├── .specify/                   # Methodology toolkit
│   ├── docs/                   # Documentation
│   │   ├── sdp-pdca.md        # Methodology
│   │   ├── memory-system.md   # State management
│   │   └── flows/             # Visual guides
│   ├── memory/
│   │   └── constitution.md    # Project principles
│   ├── templates/             # Artifact templates
│   ├── scripts/               # Automation
│   └── triage/                # Backlog system
│
├── project-context/            # Project-specific (created by /speckit-context)
│   ├── project-workplan.md    # 🎯 Orchestration
│   ├── project-overview.md    # 📊 Dashboard
│   ├── env-vars.md
│   ├── database-schema.md
│   ├── tools-registry.md
│   ├── agent-framework.md
│   └── folder-structure.md
│
├── specs/                      # Features (created by /speckit-specify)
│   └── ###-feature-name/
│       ├── spec.md            # Specification
│       ├── plan.md            # Implementation plan
│       ├── tasks.md           # Task breakdown
│       └── checklists/        # Quality gates
│
├── CATALOG.md                  # Document inventory
├── SYSTEM-PROMPT-CONTEXT.md   # AI agent quick reference
└── README.md                   # This file
```

---

## 🎨 Example: Creating a Feature

### Step 1: Specify (WHAT and WHY)

```bash
/speckit-specify "User authentication with OAuth2 (Google + GitHub)"
```

**Output**: `specs/001-user-authentication/spec.md` with:
- Process flow diagram (Mermaid)
- User stories (P1/P2/P3)
- Functional requirements (FR-001, FR-002...)
- Success criteria (measurable)

### Step 2: Clarify (if needed)

```bash
/speckit-clarify
```

**Agent asks**:
- Q1: Session storage? → Redis
- Q2: Logout behavior? → Invalidate everywhere

### Step 3: Plan (HOW)

```bash
/speckit-plan
```

**Output**: `plan.md` with:
- System interaction diagram (sequenceDiagram)
- Component architecture
- Tech stack (Passport.js, Redis)
- API contracts

### Step 4: Break into Tasks

```bash
/speckit-tasks
```

**Output**: `tasks.md` with phases:
- Setup: Passport.js + Redis
- Tests: OAuth strategies
- Core: Authentication logic
- Integration: Session management

### Step 5: Implement

```bash
/speckit-implement
```

**Executes tasks**, generates code, runs tests, updates tracking.

---

## 🏆 Key Principles

### 1. Visual Modeling First
**Every spec and plan MUST have Mermaid diagrams**. Diagrams are requirements, not decoration.

### 2. Iterative Completeness
**ALWAYS ask "🔄 Need another round?"** before closing any phase. Never assume completeness.

### 3. Gap Visibility
**Use `[?]` and `:::gap`** to show uncertainties explicitly. Never hide what you don't know.

### 4. Constitution Compliance
**All work follows constitution principles**. Violations must be explicitly justified.

### 5. Traceability
**Every code line links to a requirement** (FR-XXX). No orphan code.

### 6. Multi-Level Validation
**CHECK at 6 levels**: Artifacts, Quality, Tests, Acceptance, Constitution, User.

### 7. Continuous Learning
**Capture knowledge** in artifact version history and constitution evolution. Mistakes are lessons, not failures.

### 8. Memory-Driven
**Update workplan + overview** after every significant change. Memory is truth.

---

## 📊 Project Statistics

- **Total Documentation**: 49 files
- **Total Content**: ~347,000 characters (~87k tokens)
- **Workflows**: 11 automated commands
- **Templates**: 14 artifact templates
- **Documentation Guides**: 15 methodology docs
- **Scripts**: 5 automation utilities
- **Languages**: Markdown, PowerShell, Mermaid

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Read the methodology**: Start with `.specify/docs/README.md`
2. **Follow the workflow**: Use `/speckit-triage` to separate ideas
3. **Create specs first**: Run `/speckit-specify` for new features
4. **Maintain quality**: All PRs must pass `/speckit-analyze`
5. **Update memory**: Always update `project-overview.md`

### Contribution Guidelines

- **Specs before code**: No PR without a corresponding spec
- **Tests required**: Test coverage ≥80%
- **Constitution compliance**: Follow all principles
- **Documentation**: Update docs with features
- **Changelog**: Add to `CHANGELOG.md`

---

## 📖 Learning Resources

### Getting Started
1. Read `SYSTEM-PROMPT-CONTEXT.md` (10 min)
2. Watch the visual flows in `.specify/docs/flows/` (20 min)
3. Read `best-practices.md` (15 min)
4. Try `/speckit-context` in a test project (10 min)

### Deep Dive
1. Study `sdp-pdca.md` for methodology (30 min)
2. Learn `memory-system.md` for state management (25 min)
3. Explore `examples.md` for complete walkthrough (30 min)

### Master Level
1. Read all `.specify/docs/flows/*.md` (2h)
2. Study all workflow definitions in `.windsurf/workflows/` (3h)
3. Understand template system in `.specify/templates/` (1h)
4. Review all scripts in `.specify/scripts/` (1h)

---

## 🌟 Why Spec Orchestrator?

### Problems It Solves

❌ **Without Spec Orchestrator**:
- Specifications outdated or missing
- Code doesn't match requirements
- AI agents generate inconsistent code
- No clear project state
- Rework due to misalignment
- Knowledge lost over time

✅ **With Spec Orchestrator**:
- Living specifications always current
- Code traces to requirements
- AI agents follow consistent methodology
- Clear project state (workplan + overview)
- Quality built-in (6-level validation)
- Knowledge captured and reused

### Benefits

| Benefit | Impact |
|---------|--------|
| **Clarity** | Visual models make requirements explicit |
| **AI-Ready** | Specs serve as perfect AI context |
| **Traceability** | Every line of code links to a requirement |
| **Quality** | Multi-level validation catches issues early |
| **Learning** | Continuous improvement through captured learnings |
| **Collaboration** | Non-devs can read and validate specs |
| **Scalability** | AI agents adapt to any project speed |
| **Memory** | Project always knows its state |

---

## 🔮 Roadmap

### Version 1.x (Current)
- ✅ Core methodology (SDP-PDCA)
- ✅ 11 workflow commands
- ✅ Complete documentation
- ✅ Memory system
- ✅ Visual flows

### Version 2.0 (Planned)
- [ ] Web dashboard for project-overview.md
- [ ] Automated integrity checks (Git hooks)
- [ ] Semantic search across memory
- [ ] Memory snapshots and diffing
- [ ] AI memory summarization
- [ ] CLI tool for workflow commands
- [ ] VS Code extension
- [ ] Templates for additional frameworks

### Future
- [ ] Multi-repo orchestration
- [ ] Team collaboration features
- [ ] Analytics and insights
- [ ] Integration with project management tools
- [ ] Mobile app for reviews

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **W. Edwards Deming** - For PDCA methodology
- **Mermaid.js** - For beautiful diagrams
- **Spec-Driven Development community** - For inspiration
- **AI Agent developers** - For pushing the boundaries

---

## 📞 Support

- **Documentation**: Browse `.specify/docs/`
- **Examples**: See `.specify/docs/examples.md`
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Email**: support@specorchestrator.dev

---

## 🎵 Project Motto

> "Specifications are truth. Plans evolve. Code is generated.  
> Gaps are visible. Quality is built-in. Learning is continuous.  
> Always ask: 🔄 Need another round?"

---

**Ready to orchestrate your specifications?**

Start with: `/speckit-context` → `/speckit-triage` → Build something amazing! 🚀

---

**Last Updated**: 2024-12-05  
**Version**: 1.0.0  
**Maintained by**: Spec Orchestrator Core Team
