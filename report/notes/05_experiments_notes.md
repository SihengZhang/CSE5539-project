# Section 5: Experiments - Working Notes

## Dataset Statistics (COMPLETED)

### NYX Temperature Field
- Original: 512 × 512 × 512 float32
- Extracted: 3,000 random 256 × 256 slices
- Axis distribution: X=1004, Y=1012, Z=984
- Value range: [2.28e3, 4.78e6] → normalized [0, 1]

### Critical Point Analysis (COMPLETED)
From `data/critical_points_analysis/critical_points_report.md`:

| Type | Count | Percentage | Mean/Slice |
|------|-------|------------|------------|
| Minima | 103,434 | 28.2% | 34.5 |
| Maxima | 59,635 | 16.3% | 19.9 |
| Saddles | 203,670 | 55.5% | 67.9 |
| **Total** | **366,739** | **100%** | **122.2** |

Key observations:
- Saddles dominate (55.5%)
- High variance: 0 to 1,854 per slice
- CV = 229.8%

### Stratification Bins
| Bin | CP Range | Count |
|-----|----------|-------|
| Very Low | [0, 4) | 524 |
| Low | [4, 11) | 660 |
| Medium | [11, 25) | 592 |
| High | [25, 108) | 623 |
| Very High | [108, 1854] | 601 |

## Baseline Experiments (TODO)

### SZ Compression
- [ ] Install pysz
- [ ] Test error bounds: 1e-2, 1e-3, 1e-4, 1e-5
- [ ] Measure: compression ratio, PSNR, CP preservation

### ZFP Compression
- [ ] Install zfpy
- [ ] Test rates: 4, 8, 16, 32 bits/value
- [ ] Measure: compression ratio, PSNR, CP preservation

### VAE Baseline
- [ ] Implement simple VAE
- [ ] Latent dimensions: 64, 128, 256
- [ ] Measure: compression ratio, PSNR, CP preservation

## Diffusion Model (TODO)

### Architecture
- [ ] U-Net design
- [ ] Conditioning mechanism
- [ ] Training hyperparameters

### Training
- [ ] Train unconditional DDPM
- [ ] Add CP conditioning
- [ ] Evaluate reconstruction

## RL Agent (TODO)

### Environment
- [ ] State representation
- [ ] Action space design
- [ ] Reward function implementation

### Training
- [ ] PPO setup
- [ ] Training curves
- [ ] Policy visualization

## Results to Generate

### Tables
- [ ] Baseline comparison table
- [ ] Ablation study table
- [ ] Per-axis results table

### Figures
- [x] CP distribution (from analysis)
- [x] Example slices (from analysis)
- [ ] Baseline comparison plot
- [ ] Training curves
- [ ] Policy visualization
- [ ] Reconstruction examples
