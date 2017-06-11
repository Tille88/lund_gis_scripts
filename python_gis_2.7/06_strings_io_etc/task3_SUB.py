#Having input (cmd line options) as:
#tmp.out 1.1 3 2.6 8.3 7 -0.1675

#!/usr/bin/env python
import sys, math

#print sys.argv
#creating a list of the inputs
input_pairs = sys.argv[2:len(sys.argv)]

#catching the output file name
try:
    outfilename = sys.argv[1]
except:
    print "Usage:",sys.argv[0], "infile outfile"
    sys.exit(1)
    
ofile = open(outfilename, 'w')  # open file for writing

def myfunc(y):
    if y >= 0.0:
        return y**5*math.exp(-y)
    else:
        return 0.0

# read values 2 at the time and write out transformed values:
for i in range(0,len(input_pairs),2):
    x, y = (float(input_pairs[i]), float(input_pairs[i+1]))
    fy = myfunc(y)  # transform y value
    ofile.write('%g  %12.5e\n' % (x,fy)) #write formatted output to file
ofile.close() #close file
