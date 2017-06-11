# -*- coding: utf-8 -*-

#################################
#################################
# EX. 4.3
#################################
#################################


#ORIGINAL
from numpy import linspace
x = linspace(0,1,3)
# y = 2*x + 1:
y = x; y *=2; y +=1
# z = 4*x - 4:
z = x; z *=4; z -=4

#WHY DO X, Y AND Z HAVE THE SAME VALUES?
#When trying to assign x values to y throu y = x
#and z = x, you don't create any new objects,
#but additional pointers to the array that x also points to. 

#HOW TO CHANGE THE SCRIPT TO GET THE INTENDED VALUES?
from numpy import linspace, copy
x = linspace(0,1,3)
# y = 2*x + 1:
y = copy(x); y *=2; y +=1
# z = 4*x - 4:
z = copy(x); z *=4; z -=4

print x, y, z

#################################
#################################
# EX. 4.16
#################################
#################################
import os
#os.getcwd()
os.chdir('C:\Tempdata\JonasTillmanWorkspace\Ex10')
import numpy as np
import matplotlib.pyplot as plt

#Open file locally
file = open('temperatures.dat', 'r')
for i in range(0,17):
    file.readline()  # swallow the initial comment lines
#Read in header separately
header = [_.strip() for _ in file.readline().rstrip().split("   ")]    
file.close()

#Read in as numpy array
data = np.loadtxt('temperatures.dat',comments='*',skiprows=18)
#data.shape 
#Set years array separately
years = data[:,0]

#Transform to dictionary for index lookups
header_dict = dict()
for i, month in enumerate(header):
    header_dict[month] = i

#Allowing for command line input
#Note: Plot displays when all input is finished (e.g. can plot multiple 
#months in the same plot)
control_val = True
while control_val:
    month = raw_input("Please enter the month you want to plot (e.g. JAN or FEB): ")
    plt.plot(years,data[:,header_dict[month]])
    plt.show()
    control_inp = raw_input("Do you want to plot another month? [y/n]")
    if control_inp == 'n':
        control_val = False

#NOTE: IF RUNNING WHOLE SCRIPT AT ONCE, THEN THE EX. 4.16 AND 4.17 
#OUTPUT WILL OVERPLOT, SEE ATTACHED SCREENSHOTS...

#################################
#################################
# EX. 4.17
#################################
#################################

#####################################
#Start with 1961 to 1989 (inclusive)
start_index = data[:,0].tolist().index(1961)
end_index = data[:,0].tolist().index(1989)
early_per = data[start_index:end_index+1,1:12+1]
#need to reshape
y_early = np.reshape(early_per, early_per.shape[0]*early_per.shape[1])
x_early = np.array(sorted(12*[x for x in range(1961,1990)]))
#y_early.shape == x_early.shape
n = x_early.shape[0]
A_early = np.array([x_early, np.zeros(n)+1])
A_early = A_early.transpose()
result = np.linalg.lstsq(A_early, y_early)
# result is a 4-tuple, the solution (a,b) is the 1st entry:
a, b = result[0]
early_years = np.array([x for x in range(1961,1990)])
#Plot scatter and fitted line
plt.plot(x_early,y_early, 'bo')
plt.plot(early_years,a*early_years + b, 'r-')

#####################################
#Repeat with 1990 to 2000 (inclusive)
start_index = data[:,0].tolist().index(1990)
end_index = data[:,0].tolist().index(2000)
lat_per = data[start_index:end_index+1,1:12+1]
#need to reshape
y_lat = np.reshape(lat_per, lat_per.shape[0]*lat_per.shape[1])
x_lat = np.array(sorted(12*[x for x in range(1990,2001)]))
#y_lat.shape == x_lat.shape
n = x_lat.shape[0]
A_lat = np.array([x_lat, np.zeros(n)+1])
A_lat = A_lat.transpose()
result = np.linalg.lstsq(A_lat, y_lat)
# result is a 4-tuple, the solution (a,b) is the 1st entry:
a, b = result[0]
lat_years = np.array([x for x in range(1990,2001)])
#Plot scatter and fitted line
plt.plot(x_lat,y_lat, 'go')
plt.plot(lat_years,a*lat_years + b, 'r-')

#Seeing a clear structural break in the fitted lines...



  
#if __name__ == '__main__':
#    main()