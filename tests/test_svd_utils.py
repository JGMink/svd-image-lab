import unittest
import numpy as np
from svd_image_lab.svd_utils import decompose_image, reconstruct_image

class TestSVDUtils(unittest.TestCase):

    def setUp(self):
        # Create a simple 2D array for testing
        self.image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.U, self.S, self.Vt = decompose_image(self.image)

    def test_decompose_image(self):
        # Test if the decomposition returns the correct shapes
        self.assertEqual(self.U.shape, (3, 3))
        self.assertEqual(self.S.shape, (3,))
        self.assertEqual(self.Vt.shape, (3, 3))

    def test_reconstruct_image(self):
        # Test if the reconstruction returns the original image
        reconstructed = reconstruct_image(self.U, self.S, self.Vt)
        np.testing.assert_array_almost_equal(reconstructed, self.image)

    def test_reconstruction_with_k(self):
        # Test reconstruction with a reduced rank
        k = 2
        reconstructed_k = reconstruct_image(self.U[:, :k], self.S[:k], self.Vt[:k, :])
        self.assertEqual(reconstructed_k.shape, (3, 3))

if __name__ == '__main__':
    unittest.main()