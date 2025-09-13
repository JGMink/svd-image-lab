def calculate_mse(original, compressed):
    return ((original - compressed) ** 2).mean()

def calculate_psnr(original, compressed):
    mse = calculate_mse(original, compressed)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    return 20 * np.log10(max_pixel / np.sqrt(mse))

def calculate_ssim(original, compressed):
    from skimage.metrics import structural_similarity as ssim
    return ssim(original, compressed, multichannel=True)