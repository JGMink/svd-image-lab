def decompose_image(image):
    """Perform Singular Value Decomposition on the input image."""
    import numpy as np
    
    # Convert image to grayscale if it's not already
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)
    
    # Perform SVD
    U, S, Vt = np.linalg.svd(image, full_matrices=False)
    return U, S, Vt

def reconstruct_image(U, S, Vt, k):
    """Reconstruct the image using the first k singular values."""
    # Keep only the first k components
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    Vt_k = Vt[:k, :]
    
    # Reconstruct the image
    reconstructed_image = np.dot(U_k, np.dot(S_k, Vt_k))
    return reconstructed_image

def svd_image_compression(image, k):
    """Compress the image using SVD by retaining only k singular values."""
    U, S, Vt = decompose_image(image)
    compressed_image = reconstruct_image(U, S, Vt, k)
    return compressed_image