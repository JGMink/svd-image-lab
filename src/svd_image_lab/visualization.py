import matplotlib.pyplot as plt #type: ignore
import numpy as np

def plot_singular_values(singular_values: np.ndarray) -> None:
    """
    Plot singular values as a curve to show their relative importance.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(singular_values, marker="o")
    plt.title("Singular Values")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid()
    plt.show()

def show_side_by_side(original: np.ndarray, reconstructed: np.ndarray, titles=("Original", "Reconstructed")) -> None:
    """
    Display two images side by side for visual comparison.
    """
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap="gray")
    plt.title(titles[0])
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(reconstructed, cmap="gray")
    plt.title(titles[1])
    plt.axis("off")
    
    plt.show()
