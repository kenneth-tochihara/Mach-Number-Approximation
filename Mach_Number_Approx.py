#Import some stuff
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
import csv

#Constants and arrays
machNums = np.arange(0.0, 1.601, 0.001)
pRatio = []
gam = 1.4

#Calculates the pressure ratios
for m1 in machNums:
    if m1 < 1:
        #Find p01/p1
        pRatio.append(((1 + ((gam - 1)/2)*(m1 ** 2))**(gam/(gam - 1))))
    else:
        #Find p02/p1
        pRatio.append((((gam + 1)**2 * m1**2)/((4 * gam * m1**2) - 2 * (gam - 1)))**(gam /(gam - 1)) * ((1 - gam + (2 * gam * (m1**2)))/(gam + 1)))

#Extreme interpolation
#f = interpolate.interp1d(pRatio, machNums)

#Line fitting
deg = 4
p = np.polyfit(machNums, pRatio, deg)
fitted = []
for val in machNums:
    eq = 0
    for i in range(deg + 1):
        eq += p[i] * (val ** (deg - i))
    fitted.append(eq)


#Extreme plotting
plt.axhline(y=1, label = 'Mach 1', linewidth=1, color='#A9A9A9')
plt.plot(machNums, pRatio, 'm-', label = 'Calculated', linewidth = 0.5)
plt.plot(machNums, fitted, 'b-', label = 'Fitted', linewidth = 0.5)
plt.legend()
plt.xlabel('Pressure Ratio')
plt.ylabel('Mach Number')
plt.title('Approximating the Mach Number')
plt.show()
