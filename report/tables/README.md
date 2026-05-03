# Table Inventory

LaTeX tables for the report.

## Table List

| File | Caption | Section | Status |
|------|---------|---------|--------|
| `critical_point_stats.tex` | Critical point statistics from analysis | 5 | DONE |
| `baseline_comparison.tex` | Baseline methods comparison | 5 | TODO |
| `ablation_study.tex` | Ablation study results | 5 | TODO |

## Usage

Include tables in LaTeX sections:
```latex
\input{tables/critical_point_stats}
```

## Table Guidelines

- Use `booktabs` package (toprule, midrule, bottomrule)
- Align numbers by decimal point when appropriate
- Include units in column headers
- Caption should be self-contained
