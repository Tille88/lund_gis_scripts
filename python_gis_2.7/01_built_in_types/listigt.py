from random import randint, seed

def main():
    # List all even numbers in 'data'
    data = range(10) # Numbers 0 - 9 in a list
    even = data[0:9:2] # Modify here
    #alternatively    
    even = [x for x in data if x%2==0] # Modify here
    print even
    
    # List all even numbers in 'data' that also aren't divisible by 8.
    data = range(100) # Numbers 0 - 99 in a list
    div28 = [x for x in data if x%2==0 and x%8!=0] # Modify here
    print div28
    
    # Uniqely list all numbers occuring ONLY 3 times in 'random_nbrs'
    seed(10)
    random_nbrs = [randint(0, 25) for x in range(100)]
    triples = [x for x in data if random_nbrs.count(x)==3] # Modify here
    print triples
    
    # Test whether the following strings are palindromes.
    str1 = 'sator arepo tenet opera rotas'
    str2 = 'palindrome'
    str3 = 'ni talar bra latin'
    str1 == str1[::-1]    
    str2 == str2[::-1]    
    str3.replace(" ","") == str3.replace(" ","")[::-1]    
    
    # Also extract all unique vowels in each of the strings defined above.
    # Note: The vowels don't have to be listed in alphabetic order.
    vow1 = set([x for x in str1 if x in ['a','e','i','o','u']])
    #Alternatively
       vow1 = set([x for x in str1 if x in 'aeiou'])
    vow2 = set([x for x in str2 if x in ['a','e','i','o','u']])
    vow3 = set([x for x in str3 if x in ['a','e','i','o','u']]) # Modify here
    print vow1 # ['a', 'e', 'o']
    print vow2 # ['a', 'i', 'e', 'o']
    print vow3 # ['i', 'a']      
   
   
    # Following this comment are three numbers. The first is a pandigital happy
    # number, the two other form a prime twin (with 100 355 digits each!).
    # Develop some code to check whether any of these numbers are palindromic.
    nbr1 = 1034567892987654301
    p1 = 65516468355 * 2**333333 + 1
    p2 = 65516468355 * 2**333333 - 1
    [int(i) for i in str(nbr1)] == [int(i) for i in str(nbr1)][::-1]
    [int(i) for i in str(p1)] == [int(i) for i in str(p1)][::-1]
    [int(i) for i in str(p2)] == [int(i) for i in str(p2)][::-1]    
    
if __name__ == '__main__':
    main()