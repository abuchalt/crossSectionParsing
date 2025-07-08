import XSectModule as xsm
import os
import matplotlib.pyplot as plt
import numpy as np

# Universal Constants
# ------------------------------------------------------------------------------
N_A = 6.022E23



# Visualization Parameters
# ------------------------------------------------------------------------------
margin = 3
Erange = (0.05, 15) # [MeV]
λrange = (0.1, 10)



# Elements of Interest
# ------------------------------------------------------------------------------
myList = [
    {'symbol': 'W', 'density': 19.3,'mass': 183.84}, # Tungsten
    {'symbol': 'Fe', 'density': 7.87,'mass': 55.845}, # BCC Iron
    {'symbol': 'Ti', 'density': 4.51,'mass': 47.867}, # Titanium
    {'symbol': 'Al', 'density': 2.71,'mass': 26.981539} # Aluminum
] # Atomic Symbol, Density [g/cc], Molar Mass [Da]



# Photons
# ------------------------------------------------------------------------------
visible_y = np.array([])
for element in myList:

    # Extract Dict
    symbol = element['symbol']
    ρ = element['density']
    M = element['mass']
    XCOMdir = f'CrossSectionData{os.path.sep}'+symbol+f'_XCOM.txt'

    # Debug
    # print(symbol)

    # Plot
    MuData = xsm.parseXCOM(XCOMdir, ρ)
    xdata = MuData[:,0]/1000000 # [eV] -> [MeV]
    ydata = MuData[:,1] # [/cm]
    plt.plot(xdata, ydata, label=symbol)

    # Formatting
    plt.xlim(Erange)
    visible_y = np.append(visible_y, ydata[(xdata >= Erange[0]) & (xdata <= Erange[1])])

# Formatting   
if len(visible_y) > 0: # Set y-limits based on visible data
    plt.ylim(np.min(visible_y)/margin, np.max(visible_y)*margin)
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Linear Attenuation Coefficient [/cm]')
plt.xlabel('Photon Energy [MeV]')
plt.legend()
plt.tight_layout()
plt.show()



# Neutrons
# ------------------------------------------------------------------------------
visible_y = np.array([])
for element in myList:

    # Extract Dict
    symbol = element['symbol']
    ρ = element['density']
    M = element['mass']
    EXFORdir = f'CrossSectionData{os.path.sep}'+symbol+f'0_EXFOR.csv'

    # Calculated Properties
    N = xsm.numberDensity(ρ, M) # [cm^-3]

    # Debug
    # print(symbol)

    # Plot
    SigmaData = xsm.parseEXFOR(EXFORdir, N)
    xdata = xsm.neutronWavelength(SigmaData[:,0]) # [eV] -> [A]
    ydata = SigmaData[:,1] # [/cm]
    plt.plot(xdata, ydata, label=symbol)

    # Formatting
    plt.xlim(λrange)
    visible_y = np.append(visible_y, ydata[(xdata >= λrange[0]) & (xdata <= λrange[1])])

# Formatting   
if len(visible_y) > 0: # Set y-limits based on visible data
    plt.ylim(np.min(visible_y)/margin, np.max(visible_y)*margin)
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Linear Attenuation Coefficient [/cm]')
plt.xlabel('Neutron Wavelength [Angstrom]')
plt.title('Neutron Absorption')
plt.legend()
plt.tight_layout()
plt.show()