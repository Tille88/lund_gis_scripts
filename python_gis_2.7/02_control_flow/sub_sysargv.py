import sys
import math
from random import randint, seed

def main():
    for a in sys.argv:
        print a
        
    #task 1
    poly = [(0, 0), (-1, 5), (2, 3), (1, 5), (3, 6), (4, 5), (5, 3), 
            (8, -2), (4, -4), (2, -5)]
    temp = 0
    for i in range(0, len(poly)):
        if i < len(poly)-1:
            temp += poly[i][0]*poly[i+1][1] - poly[i][1]*poly[i+1][0]
            print "i= " + str(i)        
            print ("("+str(poly[i][0])+")" + "*" + \
                  "("+str(poly[i+1][1])+")" + "-" + \
                  "("+str(poly[i][1]))+")" + "*" + \
                  "("+str(poly[i+1][0]) + ")"
            print "temp= " + str(temp)
        else:
            temp += poly[i][0]*poly[0][1] - poly[i][1]*poly[0][0]
            print "i= " + str(i)        
            print ("("+str(poly[i][0])+")" + "*" + \
                  "("+str(poly[0][1])+")" + "-" + \
                  "("+str(poly[i][1]))+")" + "*" + \
                  "("+str(poly[0][0]) + ")"
            print "temp= " + str(temp)                  
    print "signed area =" + str(float(temp)/float(2))


       
    def area(coord):
        temp=0
        for i in range(0, len(coord)):
            if i < len(coord)-1:            
                temp += coord[i][0]*coord[i+1][1] - coord[i][1]*coord[i+1][0]
            else:
                temp += poly[i][0]*poly[0][1] - poly[i][1]*poly[0][0]
        return float(temp)/float(2)
    
    #test, must be passed a list of list as above...
    #test = area(poly)
    #print test
    #coord must be in tuple form inside a list, e.g. [(x1,y1),(x2,y2),...,(xn,yn)]
    
    def centroid(coord):
        tempx=0
        tempy=0        
        for i in range(0, len(coord)-1):
            print i
            tempx += (coord[i][0]+coord[i+1][0]) * \
                    (coord[i][0]*coord[i+1][1]-coord[i+1][0]*coord[i][1])
            tempy += (coord[i][1]+coord[i+1][1]) * \
                    (coord[i][0]*coord[i+1][1]-coord[i+1][0]*coord[i][1])
            print tempx, tempy
            print tempx, tempy
            #area_temp = area(coord)
        cx = tempx / (6*area(coord))
        cy = tempy / (6*area(coord))
        return cx, cy
        
    print centroid(poly)    
    #Gives (7,3), which clearly isn't correct....
    
    ######################    
    #Ex. 2.4
    def print_ln(r):
        r = float(r)
        if r>0:            
            print "ln(" + str(r) +") = " + str(math.log(r))
        else:
            print "ln(" + str(r) +") is illegal"
    
    #first   
    print "2.4. first FOR"
    for r in sys.argv[1:]:
        print_ln(r) 

    #second
    print "2.4. second FOR"
    for r in range(1,len(sys.argv)):
        print "i =" + str(r)        
        print_ln(sys.argv[r]) 
    
    
    print "second ii; does not work:"
    #ValueError: could not convert string to float: C:/Tempdata/JonasTillmanWorkspace/Ex3/sysargvEXResub.py
    print sys.argv[0]
    # OUTPUT: C:/Tempdata/JonasTillmanWorkspace/Ex3/sysargvEXResub.py
    #print "2.4. second FOR"
    #for r in range(len(sys.argv)):
    #    print "i =" + str(r)        
    #    print_ln(sys.argv[r]) 

    #third
    print "2.4. first WHILE"
    r=1
    while r < len(sys.argv):
        print "i =" + str(r)        
        print_ln(sys.argv[r])
        r += 1
    
    
    print "2.4. second WHILE"
    i=1    
    while 1:
        print "i =" + str(i)
        try:
            print_ln(sys.argv[i])
        except:
            break
        i +=1
        
        
    ######################    
    #Ex. 2.9
    seed(123)
    def dice(n):
        p = 0         
        for i in range(1,n+1):
            dice_a = randint(1,6)
            dice_b = randint(1,6)
            if (dice_a == 6 or dice_b ==6):
                p += 1
        print p/float(n)
        print "actual probability = 11/36, appr. 0.306"
            
    dice(200000)
 
    ######################    
    #Ex. 2.10
    def new_game(n):
        counter = 0   
        for i in range(1,n+1):
            counter -= 1
            dice_a = randint(1,6)
            dice_b = randint(1,6)
            dice_c = randint(1,6)
            dice_d = randint(1,6)
            total = dice_a + dice_b + dice_c + dice_d            
            if total<9:
                counter += 10
        return counter

    new_game(500)
    new_game(10000)
    
 
    
if __name__ == '__main__':
    main()