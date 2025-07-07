import XSectModule as xsm
import os
import matplotlib.pyplot as plt
# Iron (for various phases: Example BCC) and  Aluminum, and Titanium, and Tungsten
# 0.1 to 15 Angstroms

# Constants
# ------------------------------------------------------------------------------
N_A = 6.022E23



# BCC Iron
# ------------------------------------------------------------------------------

# Material Properties
FeDensityBCC = 7.87 # [g/cc]
FeA = 55.845 # [Da]
FeNumberDensity = xsm.numberDensity(FeDensityBCC, FeA) # [cm^-3]

# Photons
FeMu = xsm.parseXCOM(f'CrossSectionData{os.path.sep}Fe_XCOM.txt', FeDensityBCC)
plt.plot(FeMu[:,0]/1000000,FeMu[:,1])
plt.xlim(0.050,15)
plt.ylim(1E-1,1E2)
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Linear Attenuation Coefficient [/cm]')
plt.xlabel('Photon Energy [MeV]')
plt.tight_layout()
plt.show()

# Neutrons
FeSigma = xsm.parseEXFOR(f'CrossSectionData{os.path.sep}Fe0_EXFOR.csv', FeNumberDensity)
plt.plot(xsm.neutronWavelength(FeSigma[:,0]),FeSigma[:,1])
# plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1,10)
plt.ylim(4E-1,2E0)
plt.ylabel('Linear Attenuation Coefficient [/cm]')
plt.xlabel('Neutron Wavelength [Angstrom]')
plt.tight_layout()
plt.show()