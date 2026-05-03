# Section 2: Existing Approaches - Working Notes

## Methods to Cover

### Traditional Compressors
1. **SZ** (Di & Cappello, 2016)
   - Error-bounded lossy compression
   - Uniform error bounds
   - Limitation: No topology awareness

2. **ZFP** (Lindstrom, 2014)
   - Fixed-rate floating-point compression
   - Block-based transform
   - Limitation: No semantic awareness

### Neural Compression
1. **Autoencoders/VAE**
   - Learn latent representations
   - Optimize for reconstruction loss (MSE)
   - Limitation: MSE != topology preservation

2. **Neural implicit representations**
   - Encode data as network weights
   - Interesting but not our focus

### Topology-Aware Methods
1. **Persistence diagrams**
   - Multi-scale topology summary
   - Can measure topology difference

2. **Morse-Smale complexes**
   - Capture gradient flow structure
   - Used in simplification

## Gap Analysis
No prior work combines:
- RL for adaptive compression decisions
- Diffusion models for reconstruction
- Topology-aware rewards

## Table to Create
| Method | Adaptive | Topology-Aware | Learning-Based |
|--------|----------|----------------|----------------|
| SZ | No | No | No |
| ZFP | No | No | No |
| VAE | Yes | No | Yes |
| Ours | Yes | Yes | Yes |

## Key Citations to Add
- [ ] Find more recent neural compression papers
- [ ] Topology-preserving visualization papers
- [ ] RL for optimization papers
