# Project Summary: RL-Driven Diffusion for Topology-Preserving Scientific Data Compression

## One-Sentence Pitch
Use reinforcement learning to guide diffusion-based compression of scientific data, learning adaptive strategies that preserve topologically critical features (density peaks, vortex cores) better than uniform compression methods.

## The Problem
- Scientific simulations generate petabytes of data
- Current compression treats all data equally (uniform error bounds)
- Critical topological features (where ∇f = 0) are essential for scientific analysis
- Generic compressors don't understand scientific importance

## Our Approach

### Three Components:
1. **RL Compression Agent**: Learns where to allocate bits
   - State: Local field statistics (gradients, Hessian, density)
   - Action: Compression level per region
   - Reward: Balance compression ratio + topology preservation

2. **Diffusion Reconstruction Model**: Reconstructs full field from compressed data
   - Conditioned on preserved critical point locations
   - Learns physical priors from training data

3. **Topology-Aware Rewards**: Measures critical point preservation
   - Detection rate (how many found?)
   - Position error (how accurate?)
   - Persistence diagram distance (full topology)

## Key Innovation
**Task-aware compression**: Learn what to preserve based on scientific utility, not uniform fidelity.

## Datasets
- **Nyx** (cosmology): Dark matter density, identify halos and filaments
- **Miranda** (turbulence): Velocity fields, identify vortex cores

## Experiments

### Exp 1: Baselines
Compare against: gzip, SZ, ZFP, VAE
- Expected: 10-50× compression, 60-80% critical point preservation

### Exp 2: Diffusion Model Training
Train 3D U-Net diffusion model
- Test: conditioning on critical points improves topology

### Exp 3: RL Policy Training (CORE)
Train PPO agent to learn compression policy
- **Success**: 50-200× compression with 85-95% critical point detection
- **Moderate**: Matches best baselines with less tuning
- **Failure**: Reveals fundamental limits or need for better rewards

### Exp 4: Generalization
Test transfer across datasets, resolutions, physics regimes

## Success Criteria
✓ 30% better critical point preservation at same compression, OR
✓ 2× higher compression at same critical point preservation, OR
✓ Interpretable policies that align with scientific intuition

## Resources
- **GPUs**: 4-8 GPUs (V100/A100) for 1-2 weeks
- **Total**: ~500-800 GPU-hours
- **Data**: 50-100 GB of Nyx/Miranda samples
- **Software**: PyTorch, Stable-Baselines3, SZ/ZFP

## Timeline: 12 Weeks
- Weeks 1-2: Data prep, baselines
- Weeks 3-4: Diffusion model training
- Weeks 5-6: RL environment setup
- Weeks 7-9: RL policy training
- Weeks 10-11: Evaluation
- Week 12: Write-up

## Follow-up Directions

### If Successful:
- Multi-field joint compression
- Time-series compression
- Real-time in-situ compression
- Transfer to other domains (climate, medical imaging)

### If Moderate:
- Better reward shaping
- Hierarchical RL
- Hybrid RL + traditional methods

### If Challenging:
- Simplify to 2D first
- Try supervised learning baseline
- Alternative generative models (VAE-GAN)
- Theoretical analysis of limits

## Why This Matters
- Enable larger simulations with limited storage
- Faster data sharing in scientific collaborations
- Archival of long-term campaigns
- Demonstrates ML can learn scientific priors from rewards (not just supervised data)

## Research Questions Answered

### 1. Primary Question
Can RL learn task-specific compression strategies that preserve topology better than domain-agnostic methods?

### 2. Why Existing Work Falls Short
- SZ/ZFP: Uniform error bounds, no topology awareness
- Neural compressors: Optimize MSE/LPIPS, not topology
- No prior work combines RL + diffusion + topology metrics

### 3. What We'll Learn
- Can RL discover non-obvious compression strategies?
- Do diffusion models handle scientific data well?
- What are the fundamental trade-offs?
- When does transfer learning work across scientific domains?

### 4. Practical Impact
If successful, this could become a standard tool in computational science, similar to how HDF5 or SZ are used today but with much better task-specific performance.
