import numpy as np

def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert an RGB image to grayscale. If already grayscale, returns unchanged.
    """
    if len(image.shape) == 3 and image.shape[2] == 3:
        return np.mean(image, axis=2)
    return image

def decompose_image(image: np.ndarray):
    """
    Perform Singular Value Decomposition (SVD) on the input image.
    Returns U, S, Vt.
    """
    gray = to_grayscale(image)
    U, S, Vt = np.linalg.svd(gray, full_matrices=False)
    return U, S, Vt

def reconstruct_image(U: np.ndarray, S: np.ndarray, Vt: np.ndarray, k: int) -> np.ndarray:
    """
    Reconstruct the image using the first k singular values.
    """
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    Vt_k = Vt[:k, :]
    return np.dot(U_k, np.dot(S_k, Vt_k))

def svd_image_compression(image: np.ndarray, k: int) -> np.ndarray:
    """
    Compress the image using SVD by retaining only k singular values.
    """
    U, S, Vt = decompose_image(image)
    return reconstruct_image(U, S, Vt, k)
