# -*- coding: utf-8 -*-


from __future__ import division

import time

#############################################################
#############################################################
####EX 8.34
#############################################################
#############################################################

#Creating generator
def odds(start=1):
    if start % 2 == 0:
        start += 1
    else:
        start = start
    while True:
        yield start
        start += 2

#Test output
for i in odds(start=7):
    if i < 1000:
        print i
    else:
        break

#############################################################
#############################################################
####EX 8.35
#############################################################
#############################################################

#import itertools

class SparseVector(object):
    def __init__(self, n):
        self.vect = {}
        self.length = n      
        
    def __setitem__(self, key, item): 
        self.vect[key] = item
        
    def __getitem__(self, key):
        try:
            return self.vect[key]       
        except:
            return 0
    
    def __add__(self, other):
        max_length = max(self.length,other.length)
        temp_obj = SparseVector(max_length)
        for i in range(0,max_length):
            #print i
            first = 0
            second = 0
            try:
                first = self.vect[i]
            except:
                pass#print "first is 0"
            try:
                second = other.vect[i]
            except:
                pass#print "second is 0"
            if first != 0 or second != 0:
                temp_obj.vect[i] = first + second
                #print first+second
        return temp_obj
                    
    def __str__(self):
        for_print = ""
        for i in range(0,self.length):
            try:
                value =  self.vect[i]
                for_print += "[{}]={} ".format(i,value)
            except:
                for_print += "[{}]=0 ".format(i)
        return for_print                    

    def nonzeros(self):
        return self.vect
        
    def __iter__(self):
        return iter([(self[i], i) for i in range(0,self.length)])
        
        
#TEST
a = SparseVector(4)
a[2] = 9.2
a[0] = -1
a[1]
#a[2]
print a
print a.nonzeros()


b = SparseVector(5)
b[1] = 1
print b
print b.nonzeros()

c = a+b
print c
print c.nonzeros()

for ai, i in a:
    print 'a[%d]:=%g ' % (i, ai)





#############################################################
#############################################################
####EX 1
#############################################################
#############################################################


import collections
import functools
import math
import time


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned 
    (not reevaluated).
    '''
    def __init__(self, func):
         self.func = func
         self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

#############################
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1):    
        if n % i == 0:
            return False
    return True

#FROM https://gist.github.com/jeremiahmarks/ce13f5921fc131770a91
def is_perf_square(x):
    s = int(math.sqrt(x))
    return s*s == x 
def is_fib(n): 
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return is_perf_square(5*n*n + 4) or is_perf_square(5*n*n - 4)

@memoized
def is_fib_and_prime(n):
    '''Determine whether an integer n is both a Fibonacci number and a prime'''
    if is_prime(n):
        return True
    elif is_fib(n):
        return True
    else:
        return False

def main():
    n = 100
    start = time.time()
    for x in xrange(n):
        is_fib_and_prime(28657) # 1597, 28657
    end = time.time()
    print (end - start) / n

    # Reference values (in seconds) to show effect of memoize decorator
    #
    #       | Without memoized | With memoized
    # ------+------------------+--------------
    #  1597 |          0.00405 |       0.00016
    # 28657               0.56 |        0.0056
    
if __name__ == '__main__':
    main()