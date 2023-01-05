"""
histogram equalization to improve the contrast of an image

THEORY
------
Consider an image whose pixel values are confined to some specific range of values only.
For example, brighter image will have all pixels confined to high values.
But a good image will have pixels from all regions of the image.
So you need to stretch this histogram to either ends.

Opencv documentation with code: https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
Wikipedia article:              https://en.wikipedia.org/wiki/Histogram_equalization
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


def read_image(img_path):
    """Read a grayscale image from resource folder.

    :param img_path: name of the image (with ending)
    :type img_path: str
    :return: grayscale image
    :rtype: ndarray
    """
    resource_path = 'C:\\Users\\Hannes\\PycharmProjects\\CV_exercices\\resources\\' + img_path
    return cv2.imread(resource_path)


def plot_histogram(img):
    """plot histogram and normalized cdf

    :param img: some image
    :type img: cv2 mat image
    """
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()


def histogram_equalization(img):
    """histogram equalization to improve the contrast of an image

    :param img: some image
    :type img: cv2 mat image
    """
    plot_histogram(img)

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    equalized_img = cdf[img]
    plot_histogram(equalized_img)

    # show both, the original and the equalized image
    cv2.imshow("original", img)
    cv2.imshow("histogram_equalized", equalized_img)
    cv2.waitKey()
    pass


def start():
    # load grayscale image from file
    img = read_image('flowers_gray.png')
    histogram_equalization(img)


if __name__ == '__main__':
    start()
