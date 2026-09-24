import convolutif as cv
import numpy as np
import numpy.random as rd
 
def P (s, k1 = 8, k2 = 223):
    premiers = [0, 31, 37, 43, 47, 53, 59, 61, 67]
    m = (s-1)%2
    i = np.floor ((s-1)/(2*k2))
    j = np.floor ((s-1)/2) - i*k2
    t = (19*i +1) % (k1/2)
    q = t%8 +1
    c = (premiers[int (q)]*j + 21*m)%k2
    pi = 2*(t+c*(k1/2) + 1) -m
    return int (pi)
 
 
 
def interleaver (trame, k = 1784):
    new = [trame[P(v)-1] for v in range (1, k+1)]
    return np.array (new)
 
 
 
def turbo (u):
    n = len (u)
    u1, u2 = u.copy (), u.copy ()
    c1 = cv.conv2 (u1)
    inter = interleaver (u2)
    c2 = cv.conv2 (inter)
    v = []
    for k in range (n):
        a = (u[k], c1[2*k+1], c2[2*k+1])
        v.append (a)
    return np.array (v)
 
 
u = [1, 1, 0, 1, 0, 0]
u = rd.randint (0, 2, 1784)
