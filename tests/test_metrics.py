import unittest
from src.svd_image_lab.metrics import calculate_mse, calculate_psnr, calculate_ssim

class TestMetrics(unittest.TestCase):

    def test_calculate_mse(self):
        img1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        img2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(calculate_mse(img1, img2), 0)

        img1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        img2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(calculate_mse(img1, img2), 1)

    def test_calculate_psnr(self):
        img1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        img2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(calculate_psnr(img1, img2), float('inf'))

        img1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        img2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertAlmostEqual(calculate_psnr(img1, img2), 48.13080360836857, places=5)

    def test_calculate_ssim(self):
        img1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        img2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(calculate_ssim(img1, img2), 1)

        img1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        img2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertLess(calculate_ssim(img1, img2), 1)

if __name__ == '__main__':
    unittest.main()