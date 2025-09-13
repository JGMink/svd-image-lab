import numpy as np
import matplotlib.pyplot as plt

def plot_singular_values(singular_values):
    plt.figure(figsize=(10, 5))
    plt.plot(singular_values, marker='o')
    plt.title('Singular Values')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid()
    plt.show()

def show_side_by_side(original, reconstructed):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(reconstructed, cmap='gray')
    plt.title('Reconstructed Image')
    plt.axis('off')
    
    plt.show()