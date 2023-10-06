import math
import numpy as np
import matplotlib.pyplot as plot
import random

x = np.pi / 12  


# Exercise 1
a = math.exp(x) * math.cos(x)

# print (a)


# Exercise 2
xH = np.pi/6

xL = -(np.pi/6)

time = np.arange(xL,xH,0.00002)

amplitude = np.cos(time)

plot.plot(time,amplitude)

plot.title('Cosine wave from -2pi to 2pi')

plot.xlabel('Time')

plot.ylabel('Amplitude = cosine(time)')

plot.grid(True, which='both')

plot.axhline(y=0,color='b')

plot.savefig('cosineWave.png')

plot.ioff()
plot.show()


# Exercise 3
np.random.seed(0)
mu,sigma = 5.0,2.0
y = np.random.normal(mu,sigma, size=100000)

random.seed(0)
yRandom = np.random.uniform(0,10,100000)

meanFirst = np.mean(y)
meanSecond = np.mean(yRandom)


standardDeviationFirst = np.std(y)
print(meanFirst )
print(standardDeviationFirst)


standardDeviationSecond = np.std(yRandom)
print(meanSecond )
print(standardDeviationSecond)


# fig, yx = plot.subplots(figsize =(10, 7))
# plot.show(yx.hist(y, bins = [0, 25, 50, 75, 100]))
# plot.savefig('Hist1.png')

plot.figure()
_, bins, _ = plot.hist(yRandom, 100, density=True)
plot.plot(bins, np.ones_like(bins)*0.1, linewidth=2, color='r')


# fig, yRandomx = plot.subplots(figsize =(10, 7))
# plot.show(yRandomx.hist(yRandom, bins = [0, 25, 50, 75, 100]))
# plot.savefig('Hist2.png')

plot.figure()
_, bins, _ = plot.hist(y, 100, density=True)
plot.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

plot.show()