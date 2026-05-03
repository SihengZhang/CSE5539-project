# Experiment Log

Chronological record of all experiments for the RL-Driven Diffusion Compression project.

---

## 2026-05-03 - Data Preparation

**Objective:** Extract 2D slices from 3D NYX temperature field for training

**Parameters:**
- Source: `data/SDRBENCH-EXASKY-NYX-512x512x512/temperature.f32`
- Volume shape: 512 × 512 × 512 (float32)
- Slice size: 256 × 256
- Number of slices: 3,000
- Random seed: 42

**Command:**
```bash
conda activate cse5539
python extract_slices.py
```

**Results:**
- Output: `data/temperature_slices/slices.pt` (751 MB)
- Tensor shape: (3000, 1, 256, 256)
- Axis distribution: X=1004, Y=1012, Z=984
- Original range: [2.28e3, 4.78e6]
- Normalized to: [0, 1]

**Observations:**
- Balanced sampling across all three axes
- Data is ready for PyTorch training

**Status:** COMPLETE

---

## 2026-05-03 - Critical Point Analysis

**Objective:** Analyze topological features (critical points) in extracted slices

**Parameters:**
- Input: All 3,000 slices
- Gradient threshold: 1e-4 (normalized)
- Classification: Hessian eigenvalue analysis

**Command:**
```bash
conda activate cse5539
python analyze_critical_points.py
```

**Results:**

| Type | Count | Percentage | Mean/Slice | Std/Slice |
|------|-------|------------|------------|-----------|
| Minima | 103,434 | 28.2% | 34.5 | 77.8 |
| Maxima | 59,635 | 16.3% | 19.9 | 48.2 |
| Saddles | 203,670 | 55.5% | 67.9 | 155.4 |
| **Total** | **366,739** | **100%** | **122.2** | **280.9** |

Per-slice statistics:
- Min CPs per slice: 0
- Max CPs per slice: 1,854
- Median: 17
- Coefficient of variation: 229.8%

**Observations:**
- Saddle points dominate (55.5% of all CPs)
- High variance in CP density across slices
- Stratification bins identified for sampling:
  - Very Low [0, 4): 524 slices
  - Low [4, 11): 660 slices
  - Medium [11, 25): 592 slices
  - High [25, 108): 623 slices
  - Very High [108, 1854]: 601 slices

**Output files:**
- `data/critical_points_analysis/critical_points_report.md`
- `data/critical_points_analysis/critical_points_stats.json`
- `data/critical_points_analysis/critical_points_distribution.png`
- `data/critical_points_analysis/critical_points_examples.png`
- `data/critical_points_analysis/critical_points_ratios.png`
- `data/critical_points_analysis/critical_points_stratification.png`

**Status:** COMPLETE

---

## TODO: Baseline Experiments

### SZ Compression
**Objective:** Establish baseline compression performance with SZ
**Parameters to test:**
- Error bounds: 1e-2, 1e-3, 1e-4, 1e-5
**Metrics:** Compression ratio, PSNR, SSIM, CP detection rate, CP position error

### ZFP Compression
**Objective:** Establish baseline compression performance with ZFP
**Parameters to test:**
- Rates: 4, 8, 16, 32 bits/value
**Metrics:** Compression ratio, PSNR, SSIM, CP detection rate, CP position error

### VAE Baseline
**Objective:** Establish neural compression baseline
**Parameters to test:**
- Latent dimensions: 64, 128, 256
**Metrics:** Compression ratio, PSNR, SSIM, CP detection rate, CP position error

---

## TODO: Diffusion Model Training

**Objective:** Train DDPM for scientific data reconstruction
**Architecture:** U-Net with conditioning
**Training:** Standard DDPM objective

---

## TODO: RL Agent Training

**Objective:** Learn adaptive compression policy
**Algorithm:** PPO
**Reward:** Topology-aware (CP preservation + compression)

---

*Template for new entries:*

```markdown
## YYYY-MM-DD - Experiment Name

**Objective:** What we're testing

**Parameters:**
- param1: value
- param2: value

**Command:**
\`\`\`bash
python script.py --args
\`\`\`

**Results:**
- Metric 1: value
- Metric 2: value

**Observations:**
Key findings

**Next steps:**
What to try next

**Status:** IN PROGRESS / COMPLETE / FAILED
```
