# RL-Driven Diffusion Models for Topology-Preserving Scientific Data Compression

CSE 5539 Course Project - The Ohio State University

## Overview

This project explores using reinforcement learning to guide diffusion-based compression of scientific data, learning adaptive strategies that preserve topologically critical features (density peaks, vortex cores) better than uniform compression methods.

## Quick Start

```bash
# Clone and setup
git clone [repo-url]
cd CSE5539-project

# Create conda environment
conda create -n cse5539 python=3.11 -y
conda activate cse5539

# Install dependencies
pip install -r requirements.txt

# Run all experiments (single line)
./report/reproducibility/run_all.sh
```

## Project Structure

```
CSE5539-project/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── CLAUDE.md                    # Development guidance
│
├── extract_slices.py            # Data preparation script
├── analyze_critical_points.py   # Critical point analysis
│
├── data/                        # Data directory (gitignored)
│   ├── SDRBENCH-EXASKY-NYX-512x512x512/  # Raw NYX data
│   ├── temperature_slices/      # Extracted 2D slices
│   └── critical_points_analysis/  # Analysis results
│
├── proposal/                    # Project proposal
│   └── project_proposal.tex
│
└── report/                      # Final report materials
    ├── PROGRESS.md              # Progress tracker
    ├── main.tex                 # LaTeX report
    ├── sections/                # Report sections
    ├── notes/                   # Working notes
    ├── figures/                 # Report figures
    ├── tables/                  # LaTeX tables
    ├── experiments/             # Experiment logs
    └── reproducibility/         # Reproduction instructions
```

## Current Progress

| Phase | Status |
|-------|--------|
| Data Preparation | DONE |
| Critical Point Analysis | DONE |
| Baseline Experiments | TODO |
| Diffusion Model | TODO |
| RL Agent | TODO |
| Final Report | IN PROGRESS |

## Dataset

We use the NYX cosmology simulation temperature field:
- Volume: 512 x 512 x 512 float32
- Extracted: 3,000 random 256 x 256 2D slices
- Critical points analyzed: 366,739 total

## Key Results (Preliminary)

From critical point analysis:
- Saddle points dominate (55.5%)
- High variance in complexity (0-1854 CPs per slice)
- Balanced sampling across all three axes

## Requirements

- Python 3.11
- PyTorch
- See `requirements.txt` for full list

## Reproduction

See [report/reproducibility/REPRODUCIBILITY.md](report/reproducibility/REPRODUCIBILITY.md) for detailed instructions.

## Report

The final report is in `report/`. Build with:
```bash
cd report
make pdf
```

## Author

Siheng Zhang - zhang.13642@osu.edu

## License

Academic use only (course project).
