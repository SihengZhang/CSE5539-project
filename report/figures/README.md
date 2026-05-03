# Figure Inventory

All figures for the report, organized by section.

## Organization

```
figures/
├── problem/        # Section 1: Problem Statement
├── method/         # Section 3: Proposed Solution
├── experiments/    # Section 5: Experimental Results
└── analysis/       # Critical point analysis (from data/)
```

## Figure List

### Section 1: Problem Statement

| File | Caption | Status |
|------|---------|--------|
| `problem/data_growth.png` | Scientific data growth projections | TODO |
| `problem/topology_importance.png` | Critical points in cosmology data | TODO |
| `problem/compression_damage.png` | Topology damage from uniform compression | TODO |

### Section 3: Proposed Solution

| File | Caption | Status |
|------|---------|--------|
| `method/architecture.png` | Overall system architecture | TODO |
| `method/rl_agent.png` | RL agent state-action space | TODO |
| `method/diffusion_model.png` | Diffusion model with conditioning | TODO |
| `method/reward_function.png` | Topology-aware reward components | TODO |

### Section 5: Experimental Results

| File | Caption | Status |
|------|---------|--------|
| `experiments/baseline_comparison.png` | Compression vs topology preservation | TODO |
| `experiments/training_curves.png` | RL and diffusion training convergence | TODO |
| `experiments/policy_visualization.png` | Learned compression policy | TODO |
| `experiments/reconstruction_examples.png` | Before/after reconstruction | TODO |

### Analysis Figures (from critical point analysis)

| Source File | Caption | Status |
|-------------|---------|--------|
| `analysis/critical_points_distribution.png` | CP distribution across slices | DONE |
| `analysis/critical_points_examples.png` | Example slices at different complexity | DONE |
| `analysis/critical_points_ratios.png` | CP type ratios and correlations | DONE |
| `analysis/critical_points_stratification.png` | Stratification bins for sampling | DONE |

## Copying Analysis Figures

Run from the report directory:
```bash
make copy-figures
```

Or manually:
```bash
cp ../data/critical_points_analysis/*.png figures/analysis/
```

## Figure Guidelines

- Resolution: 300 DPI minimum
- Format: PNG for raster, PDF for vector
- Width: Single column (~3.5 in) or double column (~7 in)
- Font size: Readable at print size (minimum 8pt)
- Color: Use colorblind-friendly palettes
