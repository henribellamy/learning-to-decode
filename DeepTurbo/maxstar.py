import numpy as np
import numpy.random as rd
import convolutif as cv




def scalaire (x, y, a, b):
    return a*x + b*y
 


def maxstar2 (a,b):
    if a == -float ("inf") or b == -float ("inf"):
       return max (a,b)
    return max (a, b) + np.log (1+ np.exp (-abs (a-b)))



def maxstar4 (a,b,c,d):
    return maxstar2 (maxstar2 (a,b), maxstar2 (c,d))


'''
def maxstar4(a, b, c, d):
    values = np.array([a, b, c, d])
    if np.all(values == -np.inf):
        return -np.inf
    maxval = np.max(values)
    # On ignore les -inf en filtrant
    exp_terms = np.exp(values - maxval) * (values > -np.inf)
    correction = np.log(np.sum(exp_terms))
    return maxval + correction
'''


def maxstar (a, b, c = None, d = None):
    if c == None and d == None:
        return max (a, b) + np.log (1+ np.exp (-abs (a-b)))
    e = max (a, b) + log (1+ np.exp (-abs (a-b)))
    f = max (c, d) + log (1+ np.exp (-abs (c-d)))
    return max (e, f) + log (1+ np.exp (-abs (e-f)))



def formea (n):
    c = []
    m, l = cv.conv2 (n, want = True)
 
    if l[-1] == "a":
        m.append (0)
        m.append (0)
        m.append (0)
        m.append (0)
       
    if l[-1] == "b":
        m.append (1)
        m.append (1)
        m.append (0)
        m.append (0)
       
    if l[-1] == "c":
        m.append (1)
        m.append (0)
        m.append (1)
        m.append (1
                  )
    if l[-1] == "d":
        m.append (0)
        m.append (1)
        m.append (1)
        m.append (1)
 
    for k in range ((len (m)//2)):
        c.append ((1-2*(m[2*k]), 1-2*(m[2*k+1])))
    return c



def forme (n):
    c = np.array ([])
    m, l = cv.conv2 (n, want = True)
    m = np.array (m)
    
    if l[-1] == "a":
        m = np.concatenate ((m, [0, 0, 0, 0]))
        
    if l[-1] == "b":
        m = np.concatenate ((m, [1, 1, 0, 0]))
        
    if l[-1] == "c":
        m = np.concatenate ((m, [1, 0, 1, 1]))
        
    if l[-1] == "d":
        m = np.concatenate ((m, [0, 1, 1, 1]))
        
    c = np.stack([1 - 2*m[::2], 1 - 2*m[1::2]], axis=1)
    return c



def generate (u, mu, sigma):
    v = forme (u)
    c = []
    for h in v:
        c.append ( array (h) + rd.randn (2) * sigma + mu)
    return np.array (c)


