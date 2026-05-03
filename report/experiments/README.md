# Experiment Tracking

This folder contains logs and records for all experiments.

## Structure

```
experiments/
├── experiment_log.md    # Chronological master log
├── baselines/           # Baseline experiment records
├── diffusion/           # Diffusion model experiments
└── rl/                  # RL training experiments
```

## Experiment Log Format

Each experiment entry should include:
- **Date**: When the experiment was run
- **Objective**: What we're testing
- **Parameters**: Key hyperparameters
- **Command**: Exact command to reproduce
- **Results**: Quantitative outcomes
- **Observations**: Key findings
- **Next steps**: What to try next

## Naming Convention

Experiment records: `YYYY-MM-DD_experiment_name.md`

Example: `2026-05-03_sz_baseline.md`

## Quick Links

- [Master Log](experiment_log.md)
- [Baseline Template](baselines/TEMPLATE.md)
