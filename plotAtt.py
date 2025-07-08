import XSectModule as xsm
import os
import matplotlib.pyplot as plt
import numpy as np
# Iron (for various phases: Example BCC) and  Aluminum, and Titanium, and Tungsten
# 0.1 to 15 Angstroms

# Universal Constants
# ------------------------------------------------------------------------------
N_A = 6.022E23



# Visualization Parameters
# ------------------------------------------------------------------------------
margin = 3
Erange = (0.05, 15) # [MeV]
λrange = (0.1, 10)



# BCC Iron
# ------------------------------------------------------------------------------

# Material Properties
FeDensityBCC = 7.87 # [g/cc]
FeA = 55.845 # [Da]
FeNumberDensity = xsm.numberDensity(FeDensityBCC, FeA) # [cm^-3]

# Photons
FeMu = xsm.parseXCOM(f'CrossSectionData{os.path.sep}Fe_XCOM.txt', FeDensityBCC)
# Plot
xdata = FeMu[:,0]/1000000 # [eV] -> [MeV]
ydata = FeMu[:,1] # [/cm]
plt.plot(xdata, ydata)
# Formatting
plt.xlim(Erange)
visible_y = ydata[(xdata >= Erange[0]) & (xdata <= Erange[1])]
if len(visible_y) > 0: # Set y-limits based on visible data
    plt.ylim(np.min(visible_y)/margin, np.max(visible_y)*margin)
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Linear Attenuation Coefficient [/cm]')
plt.xlabel('Photon Energy [MeV]')
plt.tight_layout()
plt.show()

# Neutrons
FeSigma = xsm.parseEXFOR(f'CrossSectionData{os.path.sep}Fe0_EXFOR.csv', FeNumberDensity)
# Plot
xdata = xsm.neutronWavelength(FeSigma[:,0]) # [eV] -> [A]
ydata = FeSigma[:,1] # [/cm]
plt.plot(xdata, ydata)
# Formatting
xmin = 0.1
xmax = 10
plt.xlim(λrange)
visible_y = ydata[(xdata >= λrange[0]) & (xdata <= λrange[1])]
if len(visible_y) > 0: # Set y-limits based on visible data
    plt.ylim(np.min(visible_y)/margin, np.max(visible_y)*margin)
# plt.xscale('log')
plt.yscale('log')
plt.ylabel('Linear Attenuation Coefficient [/cm]')
plt.xlabel('Neutron Wavelength [Angstrom]')
plt.tight_layout()
plt.show()