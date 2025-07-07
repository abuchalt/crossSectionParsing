import os
import numpy as np
# import matplotlib.pyplot as plt

def parseEXFOR(filepath, N):
    data = np.genfromtxt(filepath, delimiter=',', skip_header=1)
    Energies = data[:,10] # [eV]
    Coeffs = data[:,4]*1E-24*N # [barns] -> [cm^2] -> [cm^-1]
    SigmaData = np.array(list(zip(Energies,Coeffs)))
    return SigmaData

def parseXCOM(filepath, ρ):
    data = np.genfromtxt(filepath, delimiter=" ", skip_header=2)
    Energies = data[:,0]/1000000 # [MeV] -> [eV]
    Coeffs = data[:,1]*ρ # [cm^2/g] -> [cm^-1]
    # coeffsNoCoh = data[:,2]*ρ # [cm^2/g] -> [cm^-1]
    muData = np.array(list(zip(Energies,Coeffs)))
    return muData

def neutronWavelength(E):
    # Accepts E in eV
    h = 4.1357E-15 # [eV.s]
    c = 2.998E18 # [A/s]
    m_n = 939.57*1E6 # [MeV/c^2] -> [eV/c^2]
    p = np.sqrt(2*m_n*E) # [eV/c]
    return h*c/p # [Angstrom]

def photonWavelength(E):
    # Accepts E in eV
    h = 4.1357E-15 # [eV.s]
    c = 2.998E17 # [nm/s]
    return h*c/E # [nm]