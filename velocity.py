'''

velocity.py by Kenneth Tochihara
Use for ground computer to convert the pressure ratio to an actual velocity.

'''

## Import essential classes
from scipy import interpolate
import numpy as np

## Establish machNums values and other constants
machNums = np.arange(0.0, 1.601, 0.001)
pRatio = []
gam = 1.4

# Calculates the pressure ratios
for m1 in machNums:
    if m1 < 1:
        # Find p01/p1
        pRatio.append(((1 + ((gam - 1)/2)*(m1 ** 2))**(gam/(gam - 1))))
    else:
        # Find p02/p1
        pRatio.append((((gam + 1)**2 * m1**2)/((4 * gam * m1**2) - 2 * (gam - 1)))**(gam /(gam - 1)) * ((1 - gam + (2 * gam * (m1**2)))/(gam + 1)))

## Interpolation with x as pRatio and y as machNums
f = interpolate.interp1d(pRatio, machNums)

## An easy to use function to find a machNum
def get_machNum(pRatio):
    return f(pRatio)

## Convert machNum to a velocity m/s
def get_velocity(machNum, temp):
    return machNum * temp
