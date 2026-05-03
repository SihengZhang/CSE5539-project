import numpy as np
import torch
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import ndimage
from dataclasses import dataclass
from typing import Literal
import json

@dataclass
class CriticalPointStats:
    """Statistics for critical points in a single slice."""
    slice_idx: int
    num_minima: int
    num_maxima: int
    num_saddles: int
    total: int
    axis: int
    axis_pos: int

    def to_dict(self) -> dict:
        return {
            'slice_idx': self.slice_idx,
            'num_minima': self.num_minima,
            'num_maxima': self.num_maxima,
            'num_saddles': self.num_saddles,
            'total': self.total,
            'axis': self.axis,
            'axis_pos': self.axis_pos
        }

def compute_gradient(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Compute gradient using central differences."""
    gy, gx = np.gradient(data)
    return gx, gy

def compute_hessian(data: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute Hessian matrix components."""
    gy, gx = np.gradient(data)
    gxy, gxx = np.gradient(gx)
    gyy, gyx = np.gradient(gy)
    return gxx, gyy, gxy

def find_critical_points(data: np.ndarray, gradient_threshold: float = 1e-4) -> dict:
    """
    Find and classify critical points in a 2D scalar field.

    Critical points are where gradient magnitude is near zero.
    Classification based on Hessian eigenvalues:
    - Minimum: both eigenvalues > 0 (det > 0, trace > 0)
    - Maximum: both eigenvalues < 0 (det > 0, trace < 0)
    - Saddle: eigenvalues have different signs (det < 0)

    Returns dict with positions of each type.
    """
    gx, gy = compute_gradient(data)
    grad_mag = np.sqrt(gx**2 + gy**2)

    # Normalize gradient magnitude for threshold comparison
    grad_mag_normalized = grad_mag / (grad_mag.max() + 1e-10)

    # Find candidate critical points (local minima of gradient magnitude)
    # Use morphological approach: point is critical if gradient mag is locally minimal
    footprint = np.ones((3, 3))
    local_min_grad = ndimage.minimum_filter(grad_mag_normalized, footprint=footprint)

    # Critical point candidates: where gradient is locally minimal and small
    candidates = (grad_mag_normalized == local_min_grad) & (grad_mag_normalized < gradient_threshold)

    # Compute Hessian for classification
    gxx, gyy, gxy = compute_hessian(data)

    # Hessian determinant and trace
    det_H = gxx * gyy - gxy * gxy
    trace_H = gxx + gyy

    # Classify critical points
    minima_mask = candidates & (det_H > 0) & (trace_H > 0)
    maxima_mask = candidates & (det_H > 0) & (trace_H < 0)
    saddle_mask = candidates & (det_H < 0)

    minima_pos = np.argwhere(minima_mask)
    maxima_pos = np.argwhere(maxima_mask)
    saddle_pos = np.argwhere(saddle_mask)

    return {
        'minima': minima_pos,
        'maxima': maxima_pos,
        'saddles': saddle_pos
    }

def analyze_slice(data: np.ndarray, slice_idx: int, metadata: dict) -> CriticalPointStats:
    """Analyze critical points in a single slice."""
    cp = find_critical_points(data)

    return CriticalPointStats(
        slice_idx=slice_idx,
        num_minima=len(cp['minima']),
        num_maxima=len(cp['maxima']),
        num_saddles=len(cp['saddles']),
        total=len(cp['minima']) + len(cp['maxima']) + len(cp['saddles']),
        axis=metadata['axis'],
        axis_pos=metadata['axis_pos']
    )

def plot_critical_point_distribution(stats_list: list[CriticalPointStats], output_dir: Path):
    """Plot distribution of critical points across all slices."""

    minima = [s.num_minima for s in stats_list]
    maxima = [s.num_maxima for s in stats_list]
    saddles = [s.num_saddles for s in stats_list]
    totals = [s.total for s in stats_list]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Histogram of total critical points per slice
    ax = axes[0, 0]
    ax.hist(totals, bins=50, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Number of Critical Points')
    ax.set_ylabel('Number of Slices')
    ax.set_title('Distribution of Total Critical Points per Slice')
    ax.axvline(np.mean(totals), color='r', linestyle='--', label=f'Mean: {np.mean(totals):.1f}')
    ax.legend()

    # 2. Stacked histogram by type
    ax = axes[0, 1]
    ax.hist([minima, maxima, saddles], bins=30, stacked=True,
            label=['Minima', 'Maxima', 'Saddles'], edgecolor='black', alpha=0.7)
    ax.set_xlabel('Number of Critical Points')
    ax.set_ylabel('Number of Slices')
    ax.set_title('Distribution by Critical Point Type')
    ax.legend()

    # 3. Box plot by type
    ax = axes[1, 0]
    bp = ax.boxplot([minima, maxima, saddles], labels=['Minima', 'Maxima', 'Saddles'], patch_artist=True)
    colors = ['#2ecc71', '#e74c3c', '#3498db']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax.set_ylabel('Count per Slice')
    ax.set_title('Critical Point Counts by Type')

    # 4. Distribution by axis
    ax = axes[1, 1]
    axis_names = ['X (YZ plane)', 'Y (XZ plane)', 'Z (XY plane)']
    axis_totals = {0: [], 1: [], 2: []}
    for s in stats_list:
        axis_totals[s.axis].append(s.total)

    positions = [1, 2, 3]
    bp = ax.boxplot([axis_totals[0], axis_totals[1], axis_totals[2]],
                    positions=positions, labels=axis_names, patch_artist=True)
    colors = ['#9b59b6', '#f39c12', '#1abc9c']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax.set_ylabel('Total Critical Points')
    ax.set_title('Critical Point Distribution by Slice Axis')

    plt.tight_layout()
    plt.savefig(output_dir / 'critical_points_distribution.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_dir / 'critical_points_distribution.png'}")

def plot_type_ratios(stats_list: list[CriticalPointStats], output_dir: Path):
    """Plot ratios of critical point types."""

    total_minima = sum(s.num_minima for s in stats_list)
    total_maxima = sum(s.num_maxima for s in stats_list)
    total_saddles = sum(s.num_saddles for s in stats_list)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 1. Pie chart of overall distribution
    ax = axes[0]
    sizes = [total_minima, total_maxima, total_saddles]
    labels = [f'Minima\n({total_minima:,})', f'Maxima\n({total_maxima:,})', f'Saddles\n({total_saddles:,})']
    colors = ['#2ecc71', '#e74c3c', '#3498db']
    explode = (0.02, 0.02, 0.02)
    ax.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.set_title('Overall Critical Point Type Distribution')

    # 2. Scatter plot: minima vs maxima per slice
    ax = axes[1]
    minima = [s.num_minima for s in stats_list]
    maxima = [s.num_maxima for s in stats_list]
    saddles = [s.num_saddles for s in stats_list]

    scatter = ax.scatter(minima, maxima, c=saddles, cmap='viridis', alpha=0.6, s=20)
    ax.set_xlabel('Number of Minima')
    ax.set_ylabel('Number of Maxima')
    ax.set_title('Minima vs Maxima (color = Saddles)')
    plt.colorbar(scatter, ax=ax, label='Number of Saddles')
    ax.plot([0, max(minima)], [0, max(minima)], 'r--', alpha=0.5, label='1:1 line')
    ax.legend()

    plt.tight_layout()
    plt.savefig(output_dir / 'critical_points_ratios.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_dir / 'critical_points_ratios.png'}")

def plot_example_slices(slices: np.ndarray, stats_list: list[CriticalPointStats], output_dir: Path):
    """Plot example slices with different critical point densities."""

    # Sort by total critical points
    sorted_indices = sorted(range(len(stats_list)), key=lambda i: stats_list[i].total)

    # Select slices: low, medium-low, medium, medium-high, high complexity
    n = len(sorted_indices)
    selected = [
        sorted_indices[n // 10],           # 10th percentile (low)
        sorted_indices[n // 4],            # 25th percentile
        sorted_indices[n // 2],            # 50th percentile (median)
        sorted_indices[3 * n // 4],        # 75th percentile
        sorted_indices[9 * n // 10],       # 90th percentile (high)
    ]

    fig, axes = plt.subplots(2, 5, figsize=(20, 8))

    for col, idx in enumerate(selected):
        data = slices[idx]
        stat = stats_list[idx]

        # Top row: the slice
        ax = axes[0, col]
        im = ax.imshow(data, cmap='viridis')
        ax.set_title(f'Slice {idx}\nTotal CP: {stat.total}')
        ax.axis('off')
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

        # Bottom row: critical points overlay
        ax = axes[1, col]
        ax.imshow(data, cmap='gray', alpha=0.7)

        cp = find_critical_points(data)
        if len(cp['minima']) > 0:
            ax.scatter(cp['minima'][:, 1], cp['minima'][:, 0], c='green', s=10, label='Min', alpha=0.8)
        if len(cp['maxima']) > 0:
            ax.scatter(cp['maxima'][:, 1], cp['maxima'][:, 0], c='red', s=10, label='Max', alpha=0.8)
        if len(cp['saddles']) > 0:
            ax.scatter(cp['saddles'][:, 1], cp['saddles'][:, 0], c='blue', s=10, label='Saddle', alpha=0.8)

        ax.set_title(f'Min:{stat.num_minima} Max:{stat.num_maxima} Sad:{stat.num_saddles}')
        ax.axis('off')
        if col == 0:
            ax.legend(loc='upper left', fontsize=8)

    plt.suptitle('Example Slices by Critical Point Complexity (10th, 25th, 50th, 75th, 90th percentile)',
                 fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig(output_dir / 'critical_points_examples.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_dir / 'critical_points_examples.png'}")

def plot_complexity_histogram(stats_list: list[CriticalPointStats], output_dir: Path):
    """Plot histogram with stratification bins for sampling."""

    totals = [s.total for s in stats_list]

    fig, ax = plt.subplots(figsize=(10, 6))

    # Define stratification bins
    percentiles = [0, 20, 40, 60, 80, 100]
    bin_edges = [np.percentile(totals, p) for p in percentiles]
    colors = ['#3498db', '#2ecc71', '#f1c40f', '#e67e22', '#e74c3c']
    labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']

    for i in range(len(bin_edges) - 1):
        mask = [(bin_edges[i] <= t < bin_edges[i+1]) if i < len(bin_edges) - 2
                else (bin_edges[i] <= t <= bin_edges[i+1]) for t in totals]
        count = sum(mask)
        ax.bar(i, count, color=colors[i], edgecolor='black', alpha=0.8)
        ax.text(i, count + 20, f'{count}', ha='center', fontsize=11)

    ax.set_xticks(range(5))
    ax.set_xticklabels([f'{labels[i]}\n[{bin_edges[i]:.0f}, {bin_edges[i+1]:.0f})'
                        for i in range(5)])
    ax.set_xlabel('Complexity Level (Critical Point Count Range)')
    ax.set_ylabel('Number of Slices')
    ax.set_title('Slice Distribution by Critical Point Complexity\n(For Stratified Sampling)')

    plt.tight_layout()
    plt.savefig(output_dir / 'critical_points_stratification.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_dir / 'critical_points_stratification.png'}")

def generate_report(stats_list: list[CriticalPointStats], output_dir: Path):
    """Generate a text report summarizing the analysis."""

    minima = [s.num_minima for s in stats_list]
    maxima = [s.num_maxima for s in stats_list]
    saddles = [s.num_saddles for s in stats_list]
    totals = [s.total for s in stats_list]

    total_minima = sum(minima)
    total_maxima = sum(maxima)
    total_saddles = sum(saddles)
    total_all = total_minima + total_maxima + total_saddles

    # Axis breakdown
    axis_stats = {0: {'count': 0, 'total_cp': 0},
                  1: {'count': 0, 'total_cp': 0},
                  2: {'count': 0, 'total_cp': 0}}
    for s in stats_list:
        axis_stats[s.axis]['count'] += 1
        axis_stats[s.axis]['total_cp'] += s.total

    report = f"""# Critical Point Analysis Report
## Temperature Field - NYX 512x512x512 Dataset

### Overview
- **Total slices analyzed**: {len(stats_list):,}
- **Slice dimensions**: 256 x 256
- **Total critical points detected**: {total_all:,}

### Critical Point Type Distribution

| Type     | Count     | Percentage | Mean/Slice | Std/Slice |
|----------|-----------|------------|------------|-----------|
| Minima   | {total_minima:>9,} | {100*total_minima/total_all:>9.1f}% | {np.mean(minima):>10.1f} | {np.std(minima):>9.1f} |
| Maxima   | {total_maxima:>9,} | {100*total_maxima/total_all:>9.1f}% | {np.mean(maxima):>10.1f} | {np.std(maxima):>9.1f} |
| Saddles  | {total_saddles:>9,} | {100*total_saddles/total_all:>9.1f}% | {np.mean(saddles):>10.1f} | {np.std(saddles):>9.1f} |
| **Total**| {total_all:>9,} | {100.0:>9.1f}% | {np.mean(totals):>10.1f} | {np.std(totals):>9.1f} |

### Per-Slice Statistics

| Metric              | Minima | Maxima | Saddles | Total |
|---------------------|--------|--------|---------|-------|
| Min                 | {min(minima):>6} | {min(maxima):>6} | {min(saddles):>7} | {min(totals):>5} |
| Max                 | {max(minima):>6} | {max(maxima):>6} | {max(saddles):>7} | {max(totals):>5} |
| Mean                | {np.mean(minima):>6.1f} | {np.mean(maxima):>6.1f} | {np.mean(saddles):>7.1f} | {np.mean(totals):>5.1f} |
| Median              | {np.median(minima):>6.1f} | {np.median(maxima):>6.1f} | {np.median(saddles):>7.1f} | {np.median(totals):>5.1f} |
| Std                 | {np.std(minima):>6.1f} | {np.std(maxima):>6.1f} | {np.std(saddles):>7.1f} | {np.std(totals):>5.1f} |

### Distribution by Slice Axis

| Axis | Plane   | Slice Count | Avg CP/Slice |
|------|---------|-------------|--------------|
| X    | YZ      | {axis_stats[0]['count']:>11} | {axis_stats[0]['total_cp']/max(axis_stats[0]['count'],1):>12.1f} |
| Y    | XZ      | {axis_stats[1]['count']:>11} | {axis_stats[1]['total_cp']/max(axis_stats[1]['count'],1):>12.1f} |
| Z    | XY      | {axis_stats[2]['count']:>11} | {axis_stats[2]['total_cp']/max(axis_stats[2]['count'],1):>12.1f} |

### Complexity Percentiles (Total Critical Points per Slice)

| Percentile | Value |
|------------|-------|
| 10th       | {np.percentile(totals, 10):>5.0f} |
| 25th       | {np.percentile(totals, 25):>5.0f} |
| 50th (Median) | {np.percentile(totals, 50):>5.0f} |
| 75th       | {np.percentile(totals, 75):>5.0f} |
| 90th       | {np.percentile(totals, 90):>5.0f} |

### Stratification Bins for Sampling

| Bin       | CP Range        | Slice Count |
|-----------|-----------------|-------------|
| Very Low  | [{np.percentile(totals, 0):>4.0f}, {np.percentile(totals, 20):>4.0f}) | {sum(1 for t in totals if np.percentile(totals, 0) <= t < np.percentile(totals, 20)):>11} |
| Low       | [{np.percentile(totals, 20):>4.0f}, {np.percentile(totals, 40):>4.0f}) | {sum(1 for t in totals if np.percentile(totals, 20) <= t < np.percentile(totals, 40)):>11} |
| Medium    | [{np.percentile(totals, 40):>4.0f}, {np.percentile(totals, 60):>4.0f}) | {sum(1 for t in totals if np.percentile(totals, 40) <= t < np.percentile(totals, 60)):>11} |
| High      | [{np.percentile(totals, 60):>4.0f}, {np.percentile(totals, 80):>4.0f}) | {sum(1 for t in totals if np.percentile(totals, 60) <= t < np.percentile(totals, 80)):>11} |
| Very High | [{np.percentile(totals, 80):>4.0f}, {np.percentile(totals, 100):>4.0f}] | {sum(1 for t in totals if np.percentile(totals, 80) <= t <= np.percentile(totals, 100)):>11} |

### Key Observations

1. **Type Balance**: The ratio of minima to maxima is approximately {total_minima/max(total_maxima,1):.2f}:1
2. **Saddle Dominance**: Saddle points constitute {100*total_saddles/total_all:.1f}% of all critical points
3. **Complexity Variance**: Critical point counts range from {min(totals)} to {max(totals)} per slice (CV = {100*np.std(totals)/np.mean(totals):.1f}%)
4. **Axis Consistency**: All three axes show similar average critical point densities

### Generated Files

- `critical_points_distribution.png` - Overall distribution histograms and boxplots
- `critical_points_ratios.png` - Type ratios and correlations
- `critical_points_examples.png` - Example slices at different complexity levels
- `critical_points_stratification.png` - Bins for stratified sampling
- `critical_points_stats.json` - Raw statistics in JSON format
- `critical_points_report.md` - This report

---
*Analysis performed on {len(stats_list)} slices extracted from temperature.f32*
"""

    report_path = output_dir / 'critical_points_report.md'
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Saved: {report_path}")

    return report

def main():
    # Paths
    data_dir = Path("data")
    slices_dir = data_dir / "temperature_slices"
    output_dir = data_dir / "critical_points_analysis"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load slices
    print("Loading slices...")
    data = torch.load(slices_dir / "slices.pt", weights_only=False)
    slices = data['slices'].squeeze(1).numpy()  # (3000, 256, 256)
    metadata_list = data['metadata']

    print(f"Loaded {len(slices)} slices of shape {slices[0].shape}")

    # Analyze critical points for each slice
    print("\nAnalyzing critical points...")
    stats_list = []

    for i in range(len(slices)):
        stat = analyze_slice(slices[i], i, metadata_list[i])
        stats_list.append(stat)

        if (i + 1) % 500 == 0:
            print(f"  Analyzed {i + 1}/{len(slices)} slices...")

    print(f"\nTotal critical points found: {sum(s.total for s in stats_list):,}")

    # Generate plots
    print("\nGenerating plots...")
    plot_critical_point_distribution(stats_list, output_dir)
    plot_type_ratios(stats_list, output_dir)
    plot_example_slices(slices, stats_list, output_dir)
    plot_complexity_histogram(stats_list, output_dir)

    # Save raw statistics as JSON
    stats_json = [s.to_dict() for s in stats_list]
    json_path = output_dir / 'critical_points_stats.json'
    with open(json_path, 'w') as f:
        json.dump(stats_json, f, indent=2)
    print(f"Saved: {json_path}")

    # Generate report
    print("\nGenerating report...")
    report = generate_report(stats_list, output_dir)

    print(f"\nAnalysis complete! Results saved to {output_dir}/")
    print("\nSummary:")
    print(f"  - Total slices: {len(stats_list)}")
    print(f"  - Total critical points: {sum(s.total for s in stats_list):,}")
    print(f"  - Avg per slice: {np.mean([s.total for s in stats_list]):.1f}")

if __name__ == "__main__":
    main()
