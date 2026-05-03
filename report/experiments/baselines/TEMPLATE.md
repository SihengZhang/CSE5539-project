# Baseline Experiment: [METHOD NAME]

## Metadata
- **Date:** YYYY-MM-DD
- **Method:** [SZ / ZFP / VAE / etc.]
- **Script:** `baselines/run_[method].py`

## Parameters

| Parameter | Value |
|-----------|-------|
| Error bound / Rate | ... |
| Other param | ... |

## Command

```bash
conda activate cse5539
python baselines/run_[method].py --param1 value --param2 value
```

## Results

### Compression Metrics

| Metric | Value |
|--------|-------|
| Compression Ratio | X:1 |
| Compressed Size | X MB |
| Compression Time | X s |
| Decompression Time | X s |

### Quality Metrics

| Metric | Value |
|--------|-------|
| PSNR | X dB |
| SSIM | X |
| MSE | X |

### Topology Preservation

| Metric | Value |
|--------|-------|
| CP Detection Rate | X% |
| Minima Preserved | X% |
| Maxima Preserved | X% |
| Saddles Preserved | X% |
| Position Error (mean) | X pixels |
| Position Error (std) | X pixels |

## Figures

- `figures/experiments/[method]_reconstruction.png`
- `figures/experiments/[method]_error_map.png`
- `figures/experiments/[method]_cp_comparison.png`

## Observations

[Key findings and observations]

## Comparison Notes

[How this compares to other baselines]
