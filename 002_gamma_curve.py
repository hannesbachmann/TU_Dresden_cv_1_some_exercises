"""

Opencv tutorial on gamma correction: https://pyimagesearch.com/2015/10/05/opencv-gamma-correction/
"""

import cv2
import numpy as np


def read_image(img_path):
    """Read a grayscale image from resource folder.

    :param img_path: name of the image (with ending)
    :type img_path: str
    :return: grayscale image
    :rtype: ndarray
    """
    resource_path = 'C:\\Users\\Hannes\\PycharmProjects\\CV_exercices\\resources\\' + img_path
    return cv2.imread(resource_path)


def gamma_correction(img, gamma):
    """gamma correction of an image

    :param gamma: correction parameter
    :type gamma: float
    :param img: some image
    :type img: cv2 mat img
    :return: new gamma corrected image
    """
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma  # inverted gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(img, table)


def show(img, gamma_corrected, current_gamma):
    cv2.imshow("original grayscale", img)
    cv2.imshow(f"gamma={current_gamma} grayscale", gamma_corrected)
    cv2.waitKey()


def start():
    # load grayscale image from file
    img = read_image('flowers_gray.png')
    # gamma correction on img
    gamma = 0.5
    if gamma != 0:
        corrected_img = gamma_correction(img, gamma)
        show(img, corrected_img, gamma)


if __name__ == '__main__':
    start()

