import numpy as np
import torch
from pathlib import Path
import random

def load_volume(filepath: str, shape: tuple = (512, 512, 512)) -> np.ndarray:
    """Load raw float32 binary file as 3D volume."""
    data = np.fromfile(filepath, dtype=np.float32)
    return data.reshape(shape)

def extract_random_slice(volume: np.ndarray, slice_size: int = 256) -> tuple[np.ndarray, dict]:
    """
    Extract a random 256x256 slice from a random axis.

    Returns:
        slice_data: 2D numpy array of shape (256, 256)
        metadata: dict with axis, position, and patch offsets
    """
    vol_shape = volume.shape
    axis = random.randint(0, 2)  # 0=x, 1=y, 2=z

    # Pick random position along the chosen axis
    axis_pos = random.randint(0, vol_shape[axis] - 1)

    # Get the 2D plane
    if axis == 0:  # YZ plane
        plane = volume[axis_pos, :, :]
    elif axis == 1:  # XZ plane
        plane = volume[:, axis_pos, :]
    else:  # XY plane
        plane = volume[:, :, axis_pos]

    # Extract random 256x256 patch from the plane
    max_row = plane.shape[0] - slice_size
    max_col = plane.shape[1] - slice_size

    row_start = random.randint(0, max_row)
    col_start = random.randint(0, max_col)

    patch = plane[row_start:row_start + slice_size, col_start:col_start + slice_size]

    metadata = {
        'axis': axis,
        'axis_pos': axis_pos,
        'row_start': row_start,
        'col_start': col_start
    }

    return patch.copy(), metadata

def normalize_slices(slices: np.ndarray) -> tuple[np.ndarray, float, float]:
    """Normalize slices to [0, 1] range."""
    vmin, vmax = slices.min(), slices.max()
    normalized = (slices - vmin) / (vmax - vmin + 1e-8)
    return normalized, vmin, vmax

def main():
    random.seed(42)
    np.random.seed(42)

    # Paths
    data_dir = Path("data")
    volume_path = data_dir / "SDRBENCH-EXASKY-NYX-512x512x512" / "temperature.f32"
    output_dir = data_dir / "temperature_slices"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Parameters
    num_slices = 3000
    slice_size = 256

    print(f"Loading volume from {volume_path}...")
    volume = load_volume(str(volume_path))
    print(f"Volume shape: {volume.shape}, dtype: {volume.dtype}")
    print(f"Volume range: [{volume.min():.4e}, {volume.max():.4e}]")

    # Extract slices
    print(f"\nExtracting {num_slices} random {slice_size}x{slice_size} slices...")
    slices = np.zeros((num_slices, slice_size, slice_size), dtype=np.float32)
    metadata_list = []

    axis_counts = {0: 0, 1: 0, 2: 0}

    for i in range(num_slices):
        patch, meta = extract_random_slice(volume, slice_size)
        slices[i] = patch
        metadata_list.append(meta)
        axis_counts[meta['axis']] += 1

        if (i + 1) % 500 == 0:
            print(f"  Extracted {i + 1}/{num_slices} slices...")

    print(f"\nSlices per axis: X={axis_counts[0]}, Y={axis_counts[1]}, Z={axis_counts[2]}")

    # Normalize to [0, 1]
    print("\nNormalizing slices to [0, 1]...")
    slices_normalized, vmin, vmax = normalize_slices(slices)
    print(f"Original range: [{vmin:.4e}, {vmax:.4e}]")

    # Convert to PyTorch tensor with channel dimension: (N, 1, H, W)
    slices_tensor = torch.from_numpy(slices_normalized).unsqueeze(1)
    print(f"Tensor shape: {slices_tensor.shape}, dtype: {slices_tensor.dtype}")

    # Save as PyTorch file
    output_file = output_dir / "slices.pt"
    torch.save({
        'slices': slices_tensor,  # (3000, 1, 256, 256)
        'metadata': metadata_list,
        'normalization': {'vmin': vmin, 'vmax': vmax},
        'source': 'temperature.f32',
        'shape': (num_slices, 1, slice_size, slice_size)
    }, output_file)
    print(f"\nSaved to {output_file}")

    # Also save raw numpy version for flexibility
    np_output = output_dir / "slices.npy"
    np.save(np_output, slices_normalized)
    print(f"Saved numpy version to {np_output}")

    # Save metadata separately as well
    meta_output = output_dir / "metadata.pt"
    torch.save({
        'metadata': metadata_list,
        'normalization': {'vmin': vmin, 'vmax': vmax},
        'axis_counts': axis_counts
    }, meta_output)
    print(f"Saved metadata to {meta_output}")

    print("\nDone! Files ready for PyTorch training.")
    print(f"  - Load with: data = torch.load('{output_file}')")
    print(f"  - Access slices: data['slices']  # shape: (3000, 1, 256, 256)")

if __name__ == "__main__":
    main()
