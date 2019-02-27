# Mach Number Approximation

### Purpose
The purpose of this program is to easily calculate the Mach number by interpolating the possible pressure ratios within a given set of Mach numbers for the [NASA Space Grant Midwest High-Power Rocketry Competition](http://iss.ae.illinois.edu/nasa-space-grant-midwest-high-power-rocketry-competition/). Since the goal of this competition is to break the sound barrier, it is important find the accurate airspeed in respect to the current speed of sound.

### Methodology
An MIT lecture [note](http://web.mit.edu/16.unified/www/SPRING/fluids/Spring2008/LectureNotes/f16.pdf) contains equations on the relationship between Mach number and pressure ratios in:
  * Incompressible subsonic fluids
  * Compressible supersonic fluids

Although for subsonic speeds, the Mach number can be easily solved, the equation of supersonic speeds is far more difficult to solve for. Instead, the result of pressure ratios is iterated through a list of possible Mach numbers and then plotted them on a graph. 
