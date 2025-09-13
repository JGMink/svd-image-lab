import numpy as np
from skimage.metrics import structural_similarity as ssim # type: ignore

def calculate_mse(original: np.ndarray, compressed: np.ndarray) -> float:
    """
    Compute the Mean Squared Error (MSE) between two images.
    """
    return float(((original - compressed) ** 2).mean())

def calculate_psnr(original: np.ndarray, compressed: np.ndarray, max_pixel: float = 255.0) -> float:
    """
    Compute the Peak Signal-to-Noise Ratio (PSNR) between two images.
    """
    mse = calculate_mse(original, compressed)
    if mse == 0:
        return float("inf")
    return 20 * np.log10(max_pixel / np.sqrt(mse))

def calculate_ssim(original: np.ndarray, compressed: np.ndarray) -> float:
    """
    Compute the Structural Similarity Index (SSIM) between two images.
    """
    return float(ssim(original, compressed, channel_axis=-1))
