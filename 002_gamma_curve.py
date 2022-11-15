import math

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def read_image(img_path):
    """Read a grayscale image from resource folder.

    :param img_path: name of the image (with ending)
    :type img_path: str
    :return: grayscale image
    :rtype: ndarray
    """
    resource_path = 'C:\\Users\\Hannes\\PycharmProjects\\CV_exercices\\resources\\' + img_path
    return cv2.imread(resource_path, cv2.IMREAD_GRAYSCALE)


def gamma_operator(img, gamma):
    scaled_img = img.copy() / 255
    for r_i, row in enumerate(scaled_img):
        for c_i, col_point in enumerate(row):
            scaled_img[r_i][c_i] = col_point ** gamma # round(col_point ** gamma, 1)
    return scaled_img


def histogram(img_f, param_c):
    hist_results = 0
    for r_i in range(img_f.shape[0]):
        for c_i in range(img_f.shape[1]):
            if img_f[r_i][c_i] == param_c:
                hist_results += 1
    return hist_results


def histogram_curve(img):
    x_c_axis = [i for i in range(100)]
    y_histogram_axis = [histogram(img_f=img, param_c=x / 100) for x in range(100)]
    plt.plot(x_c_axis, y_histogram_axis)
    plt.show()
    pass


def cumulative_distribution_of_colors(img, param_c):
    c_selector = lambda c2: histogram(img, param_c) if c2 <= param_c else 0

    summed_histogram = sum([sum([c_selector(img[i_row][i_col]) for i_col in range(img.shape[1])]) for i_row in range(img.shape[0])])
    print(f"c: {param_c}, sum: {summed_histogram}")
    return summed_histogram / (img.shape[0] * img.shape[1])


def cumulative_distribution_of_colors_curve(img):
    x_c_axis = [i for i in range(10)]
    y_histogram_axis = [cumulative_distribution_of_colors(img, i / 10) for i in range(10)]
    plt.plot(x_c_axis, y_histogram_axis)
    plt.show()
    pass


if __name__ == '__main__':
    # get grayscale image from file
    img = read_image('flowers_gray.png')
    # convert image to hsv (in case of using RGB and not GRAY)
    # img = cv2.cvtColor(img, "RGB2HSV")
    current_gamma = 0.5
    gamma_img = gamma_operator(img, current_gamma)
    # histogram(gamma_img, 0.5)
    # histogram_curve(gamma_img)
    scale_percent = 20  # percent of original size
    width = int(gamma_img.shape[1] * scale_percent / 100)
    height = int(gamma_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(gamma_img, dim, interpolation=cv2.INTER_AREA)
    new_resized = resized.copy()
    for i_row in range(resized.shape[0]):
        for i_col in range(resized.shape[1]):
            new_resized[i_row][i_col] = round(resized[i_row][i_col], 1)

    cumulative_distribution_of_colors_curve(new_resized)

    cv2.imshow("original grayscale", img)
    cv2.imshow(f"gamma={current_gamma} grayscale", gamma_img)
    cv2.waitKey()
