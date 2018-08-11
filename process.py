#!/usr/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

class process():
    @staticmethod
    def read():
        """
        adasfk;aj
        :return:
        """
        img = cv2.imread("C:/Users/josep/Desktop/bot/img/2.jpg", flags=1)
        img = cv2.resize(img, None, fx=0.15, fy=0.15, interpolation=cv2.INTER_CUBIC)
        return img

    @staticmethod
    def addNoise(img):
        """
        asdfadsf
        :param img:
        :return:
        """
        pass

