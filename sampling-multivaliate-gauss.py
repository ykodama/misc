# coding: utf-8
import numpy as np
from scipy import special
import matplotlib.pyplot as plt


D_list = [2, 3, 5, 10, 30, 100]
subplot_list = [1, 3, 5, 2, 4, 6]
fig = plt.figure()

for i_subplot, D in enumerate(D_list):
	mean = np.zeros(D) # 平均は原点
	cov = np.identity(D) # 共分散は単位行列
    X = np.random.multivariate_normal(mean, cov, 100000)
    r_list = []
    # 各点の中心からの距離を計算
    for i in xrange(X.shape[0]):
        sum = 0 
        for j in xrange(D):
            sum += X[i, j] ** 2

        r = np.sqrt(sum)
        r_list.append(r)

    x_df = np.arange(0, 14, 0.1)
    S_D = D * (np.math.pi**(D/2.)) / special.gamma((D/2.) + 1) #単位超球の表面積
    y_df = S_D * (x_df ** (D-1)) / ((2*np.math.pi) ** (D/2.)) * np.exp( - (x_df**2) / 2.)

    plt.subplot(3, 2, subplot_list[i_subplot])
    plt.ylim(0, 0.6)
    plt.yticks([0, 0.2, 0.4, 0.6])
    plt.hist(r_list, normed=True, bins=10, alpha=0.2) # サンプル点のヒストグラム描画
    plt.plot(x_df, y_df, color='purple') # p(r)の理論曲線描画
    plt.xlabel('r')
    plt.ylabel('p (r)')
    plt.title("D=%d" % D)
    plt.tight_layout()


# ↓は図1. 図2はsubplot無しで重ね書きした. (ソースコードの大部分が同じなので省略)
plt.savefig("sampling-mv-gauss.eps", dpi=480)