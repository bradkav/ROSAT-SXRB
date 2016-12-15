import numpy as np
import matplotlib.pyplot as pl
import matplotlib as mpl
from scipy.interpolate import interp2d,Rbf,griddata
from mpl_toolkits.axes_grid1 import make_axes_locatable
import sys

font = {'family' : 'sans-serif',
        'size'   : 15}

mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.major.width'] = 1
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['xtick.minor.width'] = 1
mpl.rcParams['ytick.major.size'] = 5
mpl.rcParams['ytick.major.width'] = 1
mpl.rcParams['ytick.minor.size'] = 3
mpl.rcParams['ytick.minor.width'] = 1
mpl.rc('font', **font)

###-----------------------------------------

#Use: python PlotROSATmaps_unc.py bandID
#where bandID = 1,2,4,5,6,7 is the energy band to plot


bandID = int(sys.argv[1])

if (bandID == 1):
    colmap = "Blues"
if (bandID == 2):
    colmap = "GnBu"
if (bandID == 4):
    colmap = "Greens"
if (bandID == 5):
    colmap = "Oranges"
if (bandID == 6):
    colmap = "Reds"
if (bandID == 7):
    colmap = "Purples"


#Load Xray map
XrayMap = np.loadtxt("../maps/ROSAT_R"+str(bandID)+"_unc.txt")


#Set data ranges for the plot
minval = 1
maxval = 1e5
cticks = [0.0,1,2,3,4,5]
clabs = [r'$1$',r'$10$',r'$10^{2}$',r'$10^{3}$',r'$10^{4}$',r'$10^{5}$']

#Do some plotting
fig = pl.figure(figsize=(12,7))
ax1 = fig.add_subplot(111)

im1 = ax1.imshow(np.log10(np.abs(np.clip(XrayMap, minval,maxval)))
        , extent=[-180, 180, -90, 90],cmap=colmap, origin="lower")

divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.1)

cb1 = pl.colorbar(im1, label=r"$10^{-6}$ counts per second per arcmin$^{2}$",\
            ticks=cticks, extend="both", cax=cax)
cb1.ax.set_yticklabels(clabs)

ax1.set_aspect(1.0)

ax1.set_xlim(-180,180)
ax1.set_ylim(-90, 90)

ax1.set_xticks([-180, -120, -60, 0, 60, 120, 180])
ax1.set_yticks([-90, -45, 0, 45, 90])


bandtext = "..."

if (bandID == 1):
    bandtext = "(Band R1: 0.11 - 0.284 keV)"
if (bandID == 2):
    bandtext = "(Band R2: 0.14 - 0.284 keV)"
if (bandID == 4):
    bandtext = "(Band R4: 0.44 - 1.01 keV)"
if (bandID == 5):
    bandtext = "(Band R5: 0.56 - 1.21 keV)"
if (bandID == 6):
    bandtext = "(Band R6: 0.73 - 1.56 keV)"
if (bandID == 7):
    bandtext = "(Band R7: 1.05 - 2.04 keV)"


ax1.set_title('ROSAT Soft X-ray Background - uncertainty '+bandtext, fontsize=12)

#Put a box around region 12...
#ax1.plot([-80, -80, 80, 80, -80], [+5, +15, +15, +5, +5], 'k:')

ax1.set_xlabel(r'$l$ [degrees]', labelpad=5)
ax1.set_ylabel(r'$b$ [degrees]', labelpad=5)

pl.savefig('../plots/ROSAT_R' + str(bandID) +'_fullsky_unc.pdf', bbox_inches="tight")