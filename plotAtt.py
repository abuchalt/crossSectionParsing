import XSectModule as xsm
import os
# Iron (for various phases: Example BCC) and  Aluminum, and Titanium, and Tungsten
# 0.1 to 15 Angstroms
N_A = 6.022E23

# CuDensity = 8.96 # [g/cc]
# CuMuData = xsm.parseXCOM(f'CrossSectionData{os.path.sep}Cu_XCOM.txt')
FeDensityBCC = 7.87 # [g/cc]
FeA = 55.845 # [Da]
FeNumberDensity = FeDensityBCC*N_A/FeA
FeSigma = xsm.parseEXFOR(f'CrossSectionData{os.path.sep}Fe0_EXFOR.csv', FeNumberDensity)

print(FeSigma)

print(xsm.photonWavelength(1000000))