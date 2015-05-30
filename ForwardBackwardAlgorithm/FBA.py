# -*- coding: utf-8 -*-
# Forward-Backward Algorithmによるイカサマサイコロ使用の事後確率計算

import numpy as np

#遷移確率、出力確率の設定
transProb = np.array([[0.9, 0.1], [0.1, 0.9]])
emitProb = np.array([[1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6],
					 [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]])

# サイコロの目とサイコロ状態系列の生成関数
def dice(n_iter):
	numlist = [1, 2, 3, 4, 5, 6]
	statelist = [0, 1]  # 0:通常サイコロ, 1:イカサマサイコロ
	X = []
	Y = []
	state = 0
	for i in range(n_iter):
		state = np.random.choice(statelist, p=transProb[state, :])
		num_dice = np.random.choice(numlist, p=emitProb[state, :])
		X.append(state)
		Y.append(num_dice)

	return X, Y

def FBA(X):
	alpha[t] = emitProb[x, y] * 


X, Y = dice(200)
print X
print Y