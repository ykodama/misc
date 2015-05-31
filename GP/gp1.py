# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


n = 100
theta0 = 1.0
theta1 = 16.0
theta2 = 0.0
theta3 = 0.0


def covariance_func(xi, xj):
	return theta0 * np.exp(-0.5 * theta1 * (xi - xj) * (xi - xj)) \
			+ theta2 + theta3 * xi * xj


def main():
	# sample n random variables
	xs = np.array([(x * 1.0 / n) * 2.0 - 1.0 for x in range(n)])

	#compute covariance matrix
	color = ['r', 'g', 'b']
	for c in color:
		cov = np.zeros((n, n))
		for i in range(n):
			for j in range(n):
				cov[i][j] = covariance_func(xs[i], xs[j])

		# draw y from multivariate gaussian
		z = np.zeros((n))
		ys = np.random.multivariate_normal(z, cov)

		plt.plot(xs, ys, color=c)

	plt.xlim([-1.0, 1.0])
	plt.show()


if __name__ == '__main__':
	main()
