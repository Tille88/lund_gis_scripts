# -*- coding: utf-8 -*-


from random import randint
import re

def gen_mp_s_nh():
    '''Generate a single multipolygon with no hole.'''
    mpoly = '(('
    n = randint(5, 15)
    for i in xrange(n - 1):
        mpoly += str(randint(-20, 20)) + ' ' + str(randint(-20, 20)) + ', '
    mpoly += str(randint(-20, 20)) + ' ' + str(randint(-20, 20)) + '))'
    return mpoly

def gen_mp_s_h():
    '''Generate a single multipolygon with a hole.'''
    mpoly = '(('
    n = randint(3, 7)
    for i in xrange(n - 1):
        mpoly += str(randint(-20, 20)) + ' ' + str(randint(-20, 20)) + ', '
    mpoly += str(randint(-20, 20)) + ' ' + str(randint(-20, 20)) + '),('
    n = randint(3, 7)
    for i in xrange(n - 1):
        mpoly += str(randint(-20, 20)) + ' ' + str(randint(-20, 20)) + ', '
    mpoly += str(randint(-20, 20)) + ' ' + str(randint(-20, 20)) + '))'
    return mpoly

def gen_mp_m_nh():
    '''Generate several multipolygons with no hole.'''
    mpoly = ''
    n = randint(2, 5)
    for x in xrange(n - 1):
        mpoly += gen_mp_s_nh() + ','
    mpoly += gen_mp_s_nh()
    return mpoly

def gen_mp_m_h():
    mpoly = ''
    n = randint(3, 7)
    h = False
    for x in xrange(n - 1):
        if randint(0, 1) == 0:
            mpoly += gen_mp_s_h() + ','
        else:
            mpoly += gen_mp_s_nh() + ','
            h = True
    if h:
        mpoly += gen_mp_s_h()
    else:
        mpoly += gen_mp_s_nh()
    return mpoly

def gen_wkt_multipoly_single_no_hole():
    '''Generate a WKT representation of a single multipolygon with no hole.'''
    return 'MULTIPOLYGON({0})'.format(gen_mp_s_nh())

def gen_wkt_multipoly_single_hole():
    '''Generate a WKT representation of a single multipolygon with a hole.'''
    return 'MULTIPOLYGON({0})'.format(gen_mp_s_h())

def gen_wkt_multipoly_multi_no_hole():
    '''Generate a WKT representation of several multipolygons with no holes.'''
    return 'MULTIPOLYGON({0})'.format(gen_mp_m_nh())

def gen_wkt_multipoly_multi_hole():
    '''Generate a WKT representation of several multipolygons where at least
    one has a hole.'''
    return 'MULTIPOLYGON({0})'.format(gen_mp_m_h())

def main():
    print 'MULTIPOLYGON 1 (single, no hole)'
    print '--------------------------------'
    poly_single_no_hole = gen_wkt_multipoly_single_no_hole()
    # Assure using regular expressions that the polygon is of the described type. 
    pattern = "MULTIPOLYGON\(\(\(((-)?\d+\s(-)?\d+(,\s)?)+\)\)\)"
    match = re.match(pattern,poly_single_no_hole)
    #print(match.group())
    assert match.group() == poly_single_no_hole
    print("passed")
    
    print 'MULTIPOLYGON 2 (single, hole)'
    print '----------------------------'    
    poly_single_hole = gen_wkt_multipoly_single_hole()
    # Assure using regular expressions that the polygon is of the described type.
    pattern = "MULTIPOLYGON\(\((\(((-)?\d+\s(-)?\d+(,\s)?)+\)(,)?)+\)\)"
    match = re.match(pattern,poly_single_hole)
    #print(match.group())
    assert match.group() == poly_single_hole
    print("passed")
    
    print 'MULTIPOLYGON 3 (multi, no hole)'
    print '-------------------------------'
    poly_multi_no_hole = gen_wkt_multipoly_multi_no_hole()
    # Assure using regular expressions that the polygon is of the described type.
    #search_res = re.search("(\(\(((-)?\d+\s(-)?\d+(,\s)?)+\)\)(,)?)+",poly_multi_no_hole)
    #search_res.group()
    pattern = "MULTIPOLYGON\((\(\(((-)?\d+\s(-)?\d+(,\s)?)+\)\)(,)?)+\)"
    match = re.match(pattern,poly_multi_no_hole)
    #print(match.group())
    assert match.group() == poly_multi_no_hole
    print("passed")

    print 'MULTIPOLYGON 4 (multi, hole)'
    print '----------------------------'    
    poly_multi_hole = gen_wkt_multipoly_multi_hole()
    # Assure using regular expressions that the polygon is of the described type.
    #search_res = re.search("\((\((\(((-)?\d+\s(-)?\d+(,\s)?)+\)(,)?)+\)(,)?)+\)",poly_multi_hole)
    #search_res.group()
    pattern = "MULTIPOLYGON\((\((\(((-)?\d+\s(-)?\d+(,\s)?)+\)(,)?)+\)(,)?)+\)"
    match = re.match(pattern,poly_multi_hole)
    #print(match.group())
    assert match.group() == poly_multi_hole
    print("passed")

    
    
if __name__ == '__main__':
    main()
