import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def h1(x):
	y = 1./(1+np.exp(-(x*400+24)))
	return y

def h2(x):
	y = 1./(1+np.exp(-(x*400-24)))
	return y

def h11(x, y):
	z = 1./(1+np.exp(-(x+100*y+200)))
	return z

def h12(x, y):
	z = 1./(1+np.exp(-(x+100*y-200)))
	return z


def h13(x, y):
	z = 1./(1+np.exp(-(100*x+y+200)))
	return z

def h14(x, y):
	z = 1./(1+np.exp(-(100*x+y-200)))
	return z

def h21(x, y):
	return h11(x, y) - h12(x, y)

def h22(x, y):
	return h13(x, y) - h14(x, y)

def h31(x, y):
	return h21(x, y) + h22(x, y)

def f(x, y):
	z = 1./ (1+np.exp(-(50*h31(x, y)-100)))
	return z

if __name__ == '__main__':
	# x = np.linspace(-1, 1, 100)
	# y = h1(x) - h2(x)
	# plt.plot(x, y)
	# plt.show()
	x = np.linspace(-5, 5, 300)
	y = x
	X, Y = np.meshgrid(x, y)
	Z = f(X, Y)
	ax = plt.axes(projection='3d')
	ax.plot_surface(X, Y, Z)
	ax.set_xlabel('x1')
	ax.set_ylabel('x2')
	plt.show()