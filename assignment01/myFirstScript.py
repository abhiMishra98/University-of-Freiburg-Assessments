import math
import numpy as np
import matplotlib.pyplot as plot
x = np.pi / 12  

a = math.exp(x) * math.cos(x)

print (a)

xH = np.pi/6
print(xH)
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

plot.show()

