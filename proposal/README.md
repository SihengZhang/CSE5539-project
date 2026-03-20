# Project Proposal: RL-Driven Diffusion for Scientific Data Compression

## Overview

This proposal presents a novel approach to scientific data compression that combines:
- **Reinforcement Learning**: Learns adaptive compression strategies
- **Diffusion Models**: Enables high-quality reconstruction
- **Topological Preservation**: Focuses on critical points in scientific fields

## Key Innovation

Unlike generic compression methods, this approach uses RL to learn what information matters most for scientific analysis, prioritizing preservation of topological critical points (density peaks in cosmology, vortex cores in turbulence) over uniform reconstruction quality.

## Documents

### 📄 Full Proposal (project_proposal.tex)
Comprehensive 30-page proposal with:
- Detailed literature review and references
- Complete experimental methodology
- Technical architecture descriptions
- Extensive follow-up discussion

### 📄 Simple Proposal (project_proposal_simple.tex) ⭐ **2 PAGES**
Concise version covering all core questions:
- Research question and motivation
- Related work and gap
- Experimental plan with expected outcomes
- Resources and timeline
- Follow-up directions

**Perfect for quick reviews or presentations!**

## Datasets

- **Nyx**: Cosmological simulations (dark matter, baryon density)
- **Miranda**: Turbulence simulations (velocity, vorticity)

## Compiling the LaTeX Documents

### Prerequisites
- LaTeX distribution (e.g., TeX Live, MiKTeX)
- Required packages: amsmath, booktabs, geometry, enumitem, titlesec

### Quick Start

```bash
# Compile both versions
make

# Compile only the 2-page simple version
make simple

# View the full proposal
make view

# View the simple 2-page version
make view-simple

# Clean auxiliary files
make clean

# Remove all generated files
make cleanall
```

### Manual Compilation

```bash
# Full version
pdflatex project_proposal.tex
pdflatex project_proposal.tex  # Run twice for references

# Simple version
pdflatex project_proposal_simple.tex
pdflatex project_proposal_simple.tex
```

### Alternative: Online Compilation
Upload either `.tex` file to [Overleaf](https://www.overleaf.com/) for online editing and compilation.

## Document Structure

### Full Proposal
1. **Research Question**: Can RL learn better compression strategies for scientific data?
2. **Related Work**: Reviews existing compression methods and their limitations
3. **Experimental Plan**: Detailed experiments with baselines, diffusion models, RL training
4. **Resources**: GPU requirements, datasets, timeline
5. **Follow-up Work**: Extensive discussion of next steps based on different outcomes
6. **References**: Complete bibliography

### Simple Proposal (2 pages)
1. **Research Question and Motivation**: Core problem statement
2. **Related Work and Gap**: What's missing in current approaches
3. **Experimental Plan**: 4 experiments with expected outcomes
4. **Resources and Timeline**: Computational needs and 12-week schedule
5. **Expected Results and Follow-up**: What we'll learn in different scenarios
6. **Conclusion**: Key insights

## Key Metrics

- **Compression ratio**: Storage savings
- **Critical point detection rate**: Topology preservation
- **Position error**: Spatial accuracy of preserved features
- **Reconstruction quality**: MSE, PSNR, power spectrum

## Expected Impact

Success would enable:
- Larger scientific simulations with limited storage
- Faster data transmission for distributed collaborations
- Archival of long-term simulation campaigns
- Real-time analysis of streaming simulation data

## Research Questions Answered

1. **Primary Question**: Can RL learn task-specific compression strategies that preserve topology better than domain-agnostic methods?

2. **Why Existing Work Falls Short**: Current methods use uniform strategies and don't prioritize scientifically important features

3. **What We'll Learn**: Whether RL can discover non-obvious compression strategies, how diffusion models handle scientific data, and fundamental trade-offs between compression and topology preservation

4. **Resources**: 4-8 GPUs for 1-2 weeks, ~500-800 GPU-hours total

5. **Follow-up Paths**: Clear directions for success, moderate success, and challenging scenarios

## Getting Started

```bash
# Clone and navigate to proposal directory
cd proposal

# Compile the simple 2-page version (recommended for quick review)
make simple
make view-simple

# Or compile the full detailed version
make
make view
```

## Files in This Directory

- `project_proposal.tex` - Full detailed proposal (~30 pages)
- `project_proposal_simple.tex` - Concise 2-page version ⭐
- `Makefile` - Build automation
- `README.md` - This file
- `SUMMARY.md` - One-page quick reference

Choose the version that fits your needs!
