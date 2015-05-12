# -*- coding: utf-8 -*-
# Forward-Backward Algorithm

import numpy as np

transProb = np.array([[0.9, 0.1], [0.1, 0.9]])
emitProb = np.array([[1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6],
					 [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]])

def dice(n_iter):
	numlist = [1, 2, 3, 4, 5, 6]
	statelist = [0, 1]
	X = []
	Y = []
	state = 0 # 0:通常サイコロ, 1:イカサマサイコロ
	for i in range(n_iter):
		state = np.random.choice(statelist, p=transProb[state, :])
		num_dice = np.random.choice(numlist, p=emitProb[state, :])
		Y.append(num_dice)
		X.append(state)

	return X, Y

class HMM(object):
	def __init__(self):
		pass

X, Y = dice(200)
print X
print Y