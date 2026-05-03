#!/bin/bash
# Run all experiments for RL-Driven Diffusion Compression
# Usage: ./report/reproducibility/run_all.sh

set -e  # Exit on error

echo "=========================================="
echo "RL-Driven Diffusion Compression"
echo "Full Reproduction Script"
echo "=========================================="

# Activate conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate cse5539

# Check environment
echo ""
echo "[1/6] Checking environment..."
python -c "import torch; import numpy; import scipy; print('Environment OK')"

# Step 1: Data preparation
echo ""
echo "[2/6] Data Preparation..."
if [ -f "data/temperature_slices/slices.pt" ]; then
    echo "Slices already extracted, skipping."
else
    python extract_slices.py
fi

# Step 2: Critical point analysis
echo ""
echo "[3/6] Critical Point Analysis..."
if [ -f "data/critical_points_analysis/critical_points_stats.json" ]; then
    echo "Analysis already done, skipping."
else
    python analyze_critical_points.py
fi

# Step 3: Baseline experiments
echo ""
echo "[4/6] Baseline Experiments..."
# TODO: Uncomment when baseline scripts are ready
# python baselines/run_sz.py --error-bounds 1e-2 1e-3 1e-4 1e-5
# python baselines/run_zfp.py --rates 4 8 16 32
# python baselines/run_vae.py --latent-dims 64 128 256
echo "TODO: Baseline scripts not yet implemented"

# Step 4: Diffusion model training
echo ""
echo "[5/6] Diffusion Model Training..."
# TODO: Uncomment when training script is ready
# python train_diffusion.py --config configs/diffusion.yaml
echo "TODO: Diffusion training script not yet implemented"

# Step 5: RL agent training
echo ""
echo "[6/6] RL Agent Training..."
# TODO: Uncomment when training script is ready
# python train_rl.py --config configs/rl.yaml
echo "TODO: RL training script not yet implemented"

# Final evaluation
echo ""
echo "=========================================="
echo "Reproduction complete!"
echo "=========================================="
echo ""
echo "Completed steps:"
echo "  [x] Data preparation"
echo "  [x] Critical point analysis"
echo "  [ ] Baseline experiments (TODO)"
echo "  [ ] Diffusion model training (TODO)"
echo "  [ ] RL agent training (TODO)"
echo ""
echo "Results are in:"
echo "  - data/temperature_slices/"
echo "  - data/critical_points_analysis/"
