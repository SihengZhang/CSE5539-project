# Reproducibility Guide

Complete instructions for reproducing all results in the paper.

## Requirements

### Software
- Python 3.11
- Conda (recommended) or pip
- CUDA-capable GPU (for training)

### Hardware
- GPU: NVIDIA V100/A100 or equivalent (16+ GB VRAM)
- RAM: 32 GB minimum
- Storage: 100 GB for data and checkpoints

## Environment Setup

### Option 1: Conda (Recommended)

```bash
# Clone repository
git clone [repo-url]
cd CSE5539-project

# Create conda environment
conda create -n cse5539 python=3.11 -y
conda activate cse5539

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Virtual Environment

```bash
# Clone repository
git clone [repo-url]
cd CSE5539-project

# Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Data Setup

### NYX Dataset

1. Download from SDRBench:
   ```bash
   # Data should be placed in:
   # data/SDRBENCH-EXASKY-NYX-512x512x512/temperature.f32
   ```

2. Or copy from local archive (if available):
   ```bash
   mkdir -p data
   cp -r /archives/disk1/SDRBench/SDRBENCH-EXASKY-NYX-512x512x512 data/
   ```

## Single-Line Reproduction

Run all experiments with:

```bash
./report/reproducibility/run_all.sh
```

This will execute:
1. Data preparation (slice extraction)
2. Critical point analysis
3. Baseline experiments (SZ, ZFP, VAE)
4. Diffusion model training
5. RL agent training
6. Final evaluation

## Step-by-Step Reproduction

### Step 1: Data Preparation (DONE)

```bash
conda activate cse5539
python extract_slices.py
```

**Output:**
- `data/temperature_slices/slices.pt` (3000 slices, 751 MB)
- `data/temperature_slices/metadata.pt`

### Step 2: Critical Point Analysis (DONE)

```bash
python analyze_critical_points.py
```

**Output:**
- `data/critical_points_analysis/critical_points_report.md`
- `data/critical_points_analysis/critical_points_stats.json`
- `data/critical_points_analysis/*.png` (4 figures)

### Step 3: Baseline Experiments (TODO)

```bash
# SZ compression
python baselines/run_sz.py --error-bounds 1e-2 1e-3 1e-4 1e-5

# ZFP compression
python baselines/run_zfp.py --rates 4 8 16 32

# VAE baseline
python baselines/run_vae.py --latent-dims 64 128 256
```

### Step 4: Diffusion Model Training (TODO)

```bash
python train_diffusion.py --config configs/diffusion.yaml
```

### Step 5: RL Agent Training (TODO)

```bash
python train_rl.py --config configs/rl.yaml
```

### Step 6: Evaluation (TODO)

```bash
python evaluate.py --all --output results/
```

## Expected Results

After running all experiments, you should have:

```
results/
├── baselines/
│   ├── sz_results.json
│   ├── zfp_results.json
│   └── vae_results.json
├── diffusion/
│   ├── checkpoints/
│   └── training_log.json
├── rl/
│   ├── checkpoints/
│   └── training_log.json
└── eval/
    ├── comparison.json
    └── figures/
```

## Verification

Run the environment check script:

```bash
python report/reproducibility/environment_check.py
```

This verifies:
- Python version
- Required packages installed
- GPU availability
- Data files present

## Troubleshooting

### CUDA Out of Memory
Reduce batch size in config files:
```yaml
batch_size: 16  # Try 8 or 4
```

### Missing Data Files
Ensure NYX data is downloaded and placed correctly:
```bash
ls data/SDRBENCH-EXASKY-NYX-512x512x512/temperature.f32
```

### Package Version Conflicts
Use exact versions from requirements.txt:
```bash
pip install -r requirements.txt --force-reinstall
```

## Contact

For questions about reproduction, contact:
- Siheng Zhang <zhang.13642@osu.edu>
