import matplotlib as mpl
import seaborn as sns
from numpy import *
import matplotlib.pyplot as plt

###############################################
########## Set up axis and figure #############
###############################################


#fig.subplots_adjust(hspace=0.7, wspace=0.5)

################################################
#########   Make the energy plot   #############
################################################

fig, axarr = plt.subplots(1, 1, facecolor='white')
x,y = loadtxt('energy.dat', unpack=1, usecols=[0,1])
my = min(y)
My = max(y)
buffer = My - my

axarr.plot(x,y, c='black')#, label='Energy (Unitless)')
axarr.set_title("Energy in the mesh", fontsize=12, fontweight='bold')    
axarr.set_xlabel('Time', fontsize=10)
axarr.set_ylabel('Energy', fontsize=10)
axarr.set_axis_bgcolor('gainsboro')
axarr.set_ylim([my-0.1*buffer, My])
axarr.set_axis_bgcolor('white')

plt.savefig('Images/energy.png')

################################################
#########     Make the bargraph    #############
################################################

fig, axarr = plt.subplots(1, 1, facecolor='white')
sides0, num_cells0 = loadtxt('hist_data0.txt', unpack=1, usecols=[0,1])
sides1, num_cells1 = loadtxt('hist_data1.txt', unpack=1, usecols=[0,1])

N = len(sides0)
ind = arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars

rects1 = axarr.bar(ind, num_cells0, width, color='orange')
rects2 = axarr.bar(ind + width, num_cells1, width, color = 'b' )

axarr.set_ylabel('Number of Cells', fontsize=10)
axarr.set_xlabel('Sides', fontsize=10)
axarr.set_title('Distribution of Cell Shapes',fontsize=12, fontweight='bold')
axarr.set_xticks(ind+width)
sides0 = sides0.astype(int)
axarr.set_xticklabels(sides0)
axarr.legend( (rects1[0], rects2[0]), ('Before', 'After') )
axarr.set_xlim(0, N-width)
axarr.set_axis_bgcolor('white')

plt.savefig('Images/bargraph.png')

################################################
#####     Make the area/perim graphs    ########
################################################

fig, axarr = plt.subplots(1, 1, facecolor='white')
fin = open("parameters.hpp", 'r')
for i in range(3):
    junk = fin.readline()
beta = fin.readline().split()[4]
lam = fin.readline().split()[4]
junk = fin.readline()
area = fin.readline().split()[4]
gamma = fin.readline().split()[4]
fin.close()

# Make area plot
a = open('area.txt').read().splitlines()
data = map(float, a)
axarr.hist(data, 10)
Title = 'Equilibrium Area'#: beta = ' + beta + '\nlambda = ' + lam + ' gamma = ' + gamma
axarr.set_title(Title, fontsize=12, fontweight='bold')
axarr.set_xlabel('Area', fontsize=10)
axarr.set_ylabel('Number of Cells', fontsize = 10)
axarr.set_axis_bgcolor('white')
plt.savefig('Images/area.png')

fig, axarr = plt.subplots(1, 1, facecolor='white')
p = open('perim.txt').read().splitlines()
data = map(float, p)
axarr.hist(data, 10)
Title = 'Equilibrium Perimeter' #: beta = ' + beta + '\nlambda = ' + lam + ' gamma = ' + gamma
axarr.set_title(Title, fontsize=12, fontweight='bold')
axarr.set_xlabel('Perimeter', fontsize=10)
axarr.set_ylabel('Number of Cells', fontsize = 10)
axarr.set_axis_bgcolor('white')
plt.savefig('Images/perim.png')
