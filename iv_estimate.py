import sys
import numpy as np
import scipy as scipy
import math
import scipy.integrate as integrate
import scipy.constants as consts
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.optimize import curve_fit

# Constants
m = consts.m_e				# electron mass
e = consts.e 				# electron charge
hbar = consts.hbar			# reduced Planck constant
h = consts.h 				# Planck constant
pi = consts.pi 				# pi

# Data preprocessing from .csv file
filename = sys.argv[1] 
data = np.genfromtxt(filename, delimiter=',', skip_header=1, names=['V','I']) 

#extracts data points from .csv file
voltage = data['V']		# experimental voltage
current = data['I'] 	# experimental current

# Simmons model current density prediction for singular voltage
def J_simmons(V, phi, d):
	return (e/(2*pi*hbar*d**2)) * ((phi - e*V/2)*scipy.exp(-(4*pi*d/hbar) * np.sqrt(2*m) * np.sqrt(phi - e*V/2)) - (phi + e*V/2)*scipy.exp(-(4*pi*d/hbar) * np.sqrt(2*m) * np.sqrt(phi + e*V/2)))

# Simmons model current density prediction for array of voltages
def J_simmons_array(V_arr, phi, d):
	return np.array([J_simmons(v, phi*e, d*1e-9) for v in V_arr])

# Nanogap parameter estimation
# popt array is parameter estimates, pcov is covariance matrix
popt, pcov = curve_fit(J_simmons_array, voltage, current, p0=[0.5,0.5]) 
perr = np.sqrt(np.diag(pcov))

# determination of device resistance at 100 mV
R = 0.1/J_simmons(.1, popt[0]*e, popt[1]*1e-9) 

# print to console
print "\nNanogap parameter estimation for %s" % filename
print "-"*len("Nanogap parameter estimation for %s" % filename)
print "Effective barrier height: (%f +/- %f) eV" % (popt[0], perr[0])
print "Gap width [nm]: (%f +/- %f) nm" % (popt[1], perr[1])
print "Device resistance (V = 100 mV): %f kOhm\n" % (1e-3*R)


plt.rc('text', usetex=True)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.rc('font', **font)
plot = 1
if plot: 
	plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	plt.plot(voltage, current, 'bo', label=filename[:-4], markerfacecolor='None', markeredgecolor='b')
	plt.plot(voltage, J_simmons_array(voltage, *popt), 'r', label='$\overline{\phi} = %5.3f$ eV, $d = %5.3f$ nm, $R = %5.3f$ k$\Omega$' % (popt[0], popt[1], R*1e-3))
	plt.xlabel('V (V)')
	plt.ylabel('I(V) (A)')
	plt.legend()
	plt.show() 