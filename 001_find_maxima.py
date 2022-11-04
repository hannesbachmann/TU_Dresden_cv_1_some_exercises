"""
Mark local maxima or plateaus in a 4-or 8-neighborhood in an image.
This can be used to detect edges.
"""

import cv2
import os
import numpy as np


def read_image(img_path):
    resource_path = 'C:\\Users\\Hannes\\PycharmProjects\\CV_exercices\\resources\\' + img_path
    return cv2.imread(resource_path, cv2.IMREAD_GRAYSCALE)


def mark_maxima_in_image(img, neighborhood=8, plateau=True):
    """Mark local maxima or plateaus in a 4-or 8-neighborhood in an image.

    :param img: old greyscale image
    :type img: ndarray
    :param neighborhood: 4 or 8, defines the radius (as number of pixels) around a pixel the pixel will be compared with
    :type neighborhood: int
    :param plateau: when True equal neighboring pixels to a maxima will also be marked
    :type plateau: bool
    :return: new image with marked local maxima/plateaus
    :rtype: ndarray
    """
    new_img = img.copy()
    for r_i, row in enumerate(img):
        for c_i, col_point in enumerate(row):
            if r_i == 0 or c_i == 0 or r_i == len(img)-1 or c_i == len(row)-1:
                # edge cases
                new_img[r_i][c_i] = img[r_i][c_i]
            else:
                if plateau:
                    if neighborhood == 4:
                        # get 4-neighborhood
                        top_neighbor = img[r_i - 1][c_i]
                        bottom_neighbor = img[r_i + 1][c_i]
                        right_neighbor = img[r_i][c_i + 1]
                        left_neighbor = img[r_i][c_i - 1]
                        # mark local maxima with 0
                        if img[r_i][c_i] >= top_neighbor \
                                and img[r_i][c_i] >= bottom_neighbor \
                                and img[r_i][c_i] >= right_neighbor \
                                and img[r_i][c_i] >= left_neighbor:
                            new_img[r_i][c_i] = 0
                        else:
                            new_img[r_i][c_i] = 255
                    elif neighborhood == 8:
                        # get 8-neighborhood
                        top_neighbor = img[r_i - 1][c_i]
                        bottom_neighbor = img[r_i + 1][c_i]
                        right_neighbor = img[r_i][c_i + 1]
                        left_neighbor = img[r_i][c_i - 1]
                        # with diagonal neighborhood
                        top_right_neighbor = img[r_i - 1][c_i + 1]
                        bottom_right_neighbor = img[r_i + 1][c_i + 1]
                        top_left_neighbor = img[r_i - 1][c_i - 1]
                        bottom_left_neighbor = img[r_i + 1][c_i - 1]
                        # mark local maxima with 0
                        if img[r_i][c_i] >= top_neighbor \
                                and img[r_i][c_i] >= bottom_neighbor \
                                and img[r_i][c_i] >= right_neighbor \
                                and img[r_i][c_i] >= left_neighbor \
                                and img[r_i][c_i] >= top_right_neighbor \
                                and img[r_i][c_i] >= top_left_neighbor \
                                and img[r_i][c_i] >= bottom_right_neighbor \
                                and img[r_i][c_i] >= bottom_left_neighbor:
                            new_img[r_i][c_i] = 0
                        else:
                            new_img[r_i][c_i] = 255
                else:
                    if neighborhood == 4:
                        # get 4-neighborhood
                        top_neighbor = img[r_i - 1][c_i]
                        bottom_neighbor = img[r_i + 1][c_i]
                        right_neighbor = img[r_i][c_i + 1]
                        left_neighbor = img[r_i][c_i - 1]
                        # mark local maxima with 0
                        if img[r_i][c_i] > top_neighbor \
                                and img[r_i][c_i] > bottom_neighbor \
                                and img[r_i][c_i] > right_neighbor \
                                and img[r_i][c_i] > left_neighbor:
                            new_img[r_i][c_i] = 0
                        else:
                            new_img[r_i][c_i] = 255
                    elif neighborhood == 8:
                        # get 8-neighborhood
                        top_neighbor = img[r_i - 1][c_i]
                        bottom_neighbor = img[r_i + 1][c_i]
                        right_neighbor = img[r_i][c_i + 1]
                        left_neighbor = img[r_i][c_i - 1]
                        # with diagonal neighborhood
                        top_right_neighbor = img[r_i - 1][c_i + 1]
                        bottom_right_neighbor = img[r_i + 1][c_i + 1]
                        top_left_neighbor = img[r_i - 1][c_i - 1]
                        bottom_left_neighbor = img[r_i + 1][c_i - 1]
                        # mark local maxima with 0
                        if img[r_i][c_i] > top_neighbor \
                                and img[r_i][c_i] > bottom_neighbor \
                                and img[r_i][c_i] > right_neighbor \
                                and img[r_i][c_i] > left_neighbor \
                                and img[r_i][c_i] > top_right_neighbor \
                                and img[r_i][c_i] > top_left_neighbor \
                                and img[r_i][c_i] > bottom_right_neighbor \
                                and img[r_i][c_i] > bottom_left_neighbor:
                            new_img[r_i][c_i] = 0
                        else:
                            new_img[r_i][c_i] = 255

    return new_img


if __name__ == '__main__':
    # get grayscale image
    image = read_image('flowers_gray.png')
    # calc image with marked maxima/plateaus
    max_image = mark_maxima_in_image(image)
    # display image
    cv2.imshow('original grayscale', image)
    cv2.imshow('local maxima', max_image)
    cv2.waitKey()

    pass
