# Report Folder

This folder contains all materials for the final CSE 5539 project report: **RL-Driven Diffusion for Topology-Preserving Scientific Data Compression**.

## Structure

```
report/
├── PROGRESS.md          # Master progress tracker (START HERE)
├── main.tex             # Main LaTeX document
├── preamble.tex         # Shared packages and macros
├── bibliography.bib     # References
├── Makefile             # Build automation
│
├── sections/            # LaTeX sections (one per required question)
├── notes/               # Working notes (markdown)
├── figures/             # Figures organized by section
├── tables/              # LaTeX tables
├── experiments/         # Experiment logs and records
└── reproducibility/     # Reproduction instructions
```

## Report Requirements

The final report must answer these 6 questions:

1. **Problem Statement**: What is the problem? Why does it matter?
2. **Existing Approaches**: What are current solutions and their limitations?
3. **Proposed Solution**: How do you propose to solve this?
4. **Why It Works**: Why should your solution work?
5. **Experimental Results**: What happened when you tried it?
6. **Lessons Learned**: What did we learn? Future work?

## Grading Rubric

- Completeness and clarity: 55%
- Claims and correctness: 30%
- Reproducibility: 10%
- Excitement: 5%

## Building the Report

```bash
cd report
make pdf        # Compile LaTeX to PDF
make clean      # Remove build artifacts
make watch      # Auto-recompile on changes (requires latexmk)
```

## Quick Links

- [Progress Tracker](PROGRESS.md) - Track what's done and what's left
- [Experiment Log](experiments/experiment_log.md) - All experiments chronologically
- [Reproducibility Guide](reproducibility/REPRODUCIBILITY.md) - How to reproduce results
