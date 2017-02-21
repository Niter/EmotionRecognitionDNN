# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import numpy as np
import tensorflow as tf
import scipy.io as sio

# Constant Value
NUM_INTERVIEW = 32
NUM_FRAME = 63
NUM_SCALE = 32
NUM_CHANNEL = 32
NUM_VIDEO = 40

NUM_TRAIN = 28
NUM_TEST = 4
NUM_OUTPUT_CLASS = 2
SIZE_TRAIN = NUM_TRAIN * NUM_VIDEO
SIZE_TEST = NUM_TEST * NUM_VIDEO

DATA_PATH = '../Datasets/EEGMatlab/'

# Grab the prepocessed data from data folder
print('Start Loading Data')
wholeX = sio.loadmat(DATA_PATH + 'CWTX.mat')['WholeX']
dataY = sio.loadmat(DATA_PATH + 'CWTY.mat')['WholeY'][0]
wholeY = np.zeros((NUM_VIDEO * NUM_INTERVIEW, 2))
wholeY[dataY >= 5, 1] = 1
wholeY[dataY < 5, 0] = 1
trainX, trainY = wholeX[:SIZE_TRAIN , :, :], wholeY[:SIZE_TRAIN, :]
testX, testY = wholeX[SIZE_TRAIN:, :, :], wholeY[SIZE_TRAIN:, :]
print('Finish Loading Data')

print(testY)
