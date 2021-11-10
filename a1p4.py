"""
ECE606, F'21, Assignment 1, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code as you like.
"""

def encode(d, i):
    """
    You need to implement this method. See the handout for its specs.
    """
    return i % (10**d) #representation in form of non negative integer

def decode(d, i):
    """
    You need to implement this method. See the handout for its specs.
    """
    if i >= (10**d/2):  #eg: if i = 50 return 50-100 = -50
        return i - (10 ** d)
    else:   # here i <10**d/2  so it can be represented by i
        return i

def add(d, i, j):
    """
    You need to implement this method. See the handout for its specs.
    """
    s = i+j
    if len(str(s)) > d: #if digits of sum exceed d
        return int(str(s)[-d:]) #take last d digits from the sum
    else:
        return s

def multiply(d, i, j):
    """
    You need to implement this method. See the handout for its specs.
    """
    m = i*j
    sum = 0
    if len(str(m)) > d: #if digits of the multiplication exceed d
        if (i ==0) or (j == 0): #if either of i or j is 0 return 0
            return 0
        elif j%2==0:  #if j is even
            sum = add(d, sum, multiply(d, add(d, i, i), j//2))
        else:
            sum = add(d,sum,add(d, i, multiply(d,add(d,i,i),j//2))) # condition when j is odd (otherwise)
        return sum
    else:
        return m

