#Import some stuff
from scipy import interpolate
import numpy as np

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

#Interpolation
f = interpolate.interp1d(pRatio, machNums)

#Tell user input range
print('Min: %d\nMax: %d' % (min(pRatio), max(pRatio)))

#User Input/Output
ans = ""
while ans is "":
    try:
        p = float(raw_input("Pressure Ratio: "))
        print("Mach Number: %d" % f(p))
    except:
        print("Invalid input.") #Takes into account the fact that input could be invalid.
        pass
    ans = raw_input("Again? (Enter to continue)")
