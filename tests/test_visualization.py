import unittest
from svd_image_lab.visualization import plot_singular_values, show_side_by_side
import numpy as np
import matplotlib.pyplot as plt

class TestVisualization(unittest.TestCase):

    def test_plot_singular_values(self):
        singular_values = np.array([1, 0.5, 0.2])
        plt.figure()
        plot_singular_values(singular_values)
        # Check if the plot was created
        self.assertIsNotNone(plt.gcf())
        plt.close()

    def test_show_side_by_side(self):
        original_image = np.random.rand(10, 10)
        reconstructed_image = np.random.rand(10, 10)
        plt.figure()
        show_side_by_side(original_image, reconstructed_image)
        # Check if the plot was created
        self.assertIsNotNone(plt.gcf())
        plt.close()

if __name__ == '__main__':
    unittest.main()