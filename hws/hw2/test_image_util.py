import numpy as np
import pytest

from image_util import horizontal_flip, region_avg, region_median, \
        denoise, thresholding, center_crop


sample_image1 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

expected_image1 = np.array([
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ])

sample_image2 = np.array([i for i in range(0, 16)]).reshape(4,4)

expected_blurred = np.array([
        [2, 2, 3],
        [4, 5, 5],
        [5, 6, 6]
    ])

sample_image3 = np.array([
        [50, 120, 200],
        [90, 150, 180],
        [30, 170, 220]
    ])

expected_th = np.array([
        [0, 0, 255],
        [0, 0, 255],
        [0, 255, 255]
    ]) 

sample_image4 = np.array([
        [10, 20, 30, 40, 50],
        [20, 30, 50, 50, 60],
        [20, 30, 40, 50, 60],
        [20, 30, 40, 60, 70],
        [30, 40, 50, 60, 70]])

expected4 = np.array([[20, 25, 35, 50, 50],
       [20, 30, 40, 50, 50],
       [25, 30, 40, 50, 60],
       [30, 30, 40, 60, 60],
       [30, 35, 45, 60, 65]])


sample_image5 =  np.array([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ])

expected5 = np.array([
        [7, 8, 9],
        [12, 13, 14],
        [17, 18, 19]
    ])

def test_horizontal_flip():
    flipped_image = horizontal_flip(sample_image1)
    assert np.array_equal(flipped_image, expected_image1)

def test_horizontal_flip_identity():
    # Test flipping an image twice returns the original image
    flipped_twice = horizontal_flip(horizontal_flip(sample_image2))
    assert np.array_equal(flipped_twice, sample_image2)


def test_region_avg():
    # Test region average for center pixel
    assert region_avg(sample_image1, 1, 1) == pytest.approx(5.0)

    # Test region average for top-left corner
    assert region_avg(sample_image1, 0, 0) == pytest.approx((1 + 2 + 4 + 5) / 4)

    # Test region average for bottom-right corner
    assert region_avg(sample_image1, 2, 2) == pytest.approx((5 + 6 + 8 + 9) / 4)

    # Test region average for region partially outside image boundary
    assert region_avg(sample_image1, 0, 1) == pytest.approx((1 + 2 + 3 + 4 + 5 + 6) / 6)


def test_region_median():
    # Test region median for center pixel with odd-sized region
    assert region_median(sample_image1, 1, 1, k=3) == 5.0

    # Test region median for center pixel with even-sized region
    assert region_median(sample_image1, 1, 1, k=3) == 5.0

    # Test region median for corner pixel
    assert region_median(sample_image1, 0, 0, k=3) == 3.0

def test_denoise():
    # Test denoising with default kernel size
    denoised_image = denoise(sample_image4)
    assert np.array_equal(denoised_image, expected4)

def test_thresholding():
    threshold = 150
    binary_image = thresholding(sample_image3, threshold)
    assert np.array_equal(binary_image, expected_th)

def test_center_crop_valid():
    # Test center crop with valid crop sizes
    cropped_image = center_crop(sample_image5, 3, 3)
    assert np.array_equal(cropped_image, expected5)

def test_center_crop_invalid():
    # Test center crop with invalid crop sizes
    with pytest.raises(ValueError):
        center_crop(sample_image5, 6, 6) 

    with pytest.raises(ValueError):
        center_crop(sample_image5, 3, 6) 

    with pytest.raises(ValueError):
        center_crop(sample_image5, 6, 3)

