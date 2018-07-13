# -*- coding=utf-8 -*-
# Kalman filter example demo in Python

# 参考：
# 1、卡尔曼滤波,最最容易理解的讲解.找遍网上就这篇看懂了.
# https://blog.csdn.net/phker/article/details/48468591
# 2、通俗理解卡尔曼滤波及其算法实现（实例解析）
# https://blog.csdn.net/tiandijun/article/details/72469471
# 3、python起步之卡尔曼滤波
# https://www.cnblogs.com/catmelo/p/4175826.html

# 以下部分根据参考文献[3]复制的代码，取值参考文献[1-2]

# A Python implementation of the example given in pages 11-15 of "An
# Introduction to the Kalman Filter" by Greg Welch and Gary Bishop,
# University of North Carolina at Chapel Hill, Department of Computer
# Science, TR 95-041,
# http://www.cs.unc.edu/~welch/kalman/kalmanIntro.html

# by Andrew D. Straw
# coding:utf-8
import numpy
import pylab

# 这里是假设A=1，H=1的情况

# intial parameters
n_iter = 200
sz = (n_iter,)  # size of array
x = 25  # truth value (typo in example at top of p. 13 calls this z)
z = numpy.random.normal(x, 2, size=sz)  # observations (normal about x, sigma=0.1)
A = 1
B = 0
u = []  # 控制量
for i in range(n_iter):
    u.append(0)

Q = 1e-5  # process variance

# allocate space for arrays
xhat = numpy.zeros(sz)  # a posteriori estimate of x 后验
P = numpy.zeros(sz)  # a posteriori error estimate
xhatminus = numpy.zeros(sz)  # a priori estimate of x 先验
Pminus = numpy.zeros(sz)  # a priori error estimate
K = numpy.zeros(sz)  # gain or blending factor

R = 1e-2  # estimate of measurement variance, change to see effect 测量噪声

# initial guesses
# X(0|0)和P(0|0)。他们的值不用太在意，随便给一个就可以了，因为随着卡尔曼的工作，X会逐渐的收敛
# P，一般不要取0，因为这样可能会令卡尔曼完全相信你给定的X(0|0)是系统最优的，从而使算法不能收敛
xhat[0] = 0.0
P[0] = 10.0

for k in range(1, n_iter):
    # time update
    xhatminus[k] = A*xhat[k - 1] + B*u[k-1]  # X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0
    Pminus[k] = A*P[k - 1]*(1.0/A) + Q  # P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1

    # measurement update
    K[k] = Pminus[k] / (Pminus[k] + R)  # Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
    xhat[k] = xhatminus[k] + K[k] * (z[k] - xhatminus[k])  # X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
    P[k] = (1 - K[k]) * Pminus[k]  # P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1

pylab.figure()
pylab.plot(z, 'k+', label='noisy measurements')  # 测量值
pylab.plot(xhat, 'b-', label='a posteri estimate')  # 过滤后的值
pylab.axhline(x, color='g', label='truth value')  # 系统值
pylab.legend()
pylab.xlabel('Iteration')
pylab.ylabel('Voltage')

pylab.figure()
valid_iter = range(1, n_iter)  # Pminus not valid at step 0
pylab.plot(valid_iter, Pminus[valid_iter], label='a priori error estimate')
pylab.xlabel('Iteration')
pylab.ylabel('$(Voltage)^2$')
pylab.setp(pylab.gca(), 'ylim', [0, .01])
pylab.show()
