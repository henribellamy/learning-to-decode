import numpy as np
import maxlogmap2turbo as mp
import turbocode as tc
 
 
def deinterleaver (m, k = 1784):
    sortie = []
    indice = [tc.P(v) for v in range (1, k+1)]
    for i in range (1784):
        sortie.append (m[indice.index (i+1)])
    return np.array (sortie)
 
 
 
def extrait (trame3):
    c0, c1, c2 = [], [], []
    e1, e2 = [], []
   
    for h in trame3:
        c0.append (h[0])
        c1.append (h[1])
        c2.append (h[2])
 
    c0i = tc.interleaver (c0)
   
    for k in range (len (trame3)):
        e1.append (c0[k])
        e1.append (c1[k])
        e2.append (c0i[k])
        e2.append (c2[k])
       
    return np.array (e1), np.array (e2)
 
 
 
def treat (m):
    c = []
    for k in range ((len (m)//2)):
        c.append ((m[2*k], m[2*k+1]))
    return np.array (c)
 
 
def decoder (v, ni):
    e1, e2 = extrait (v)         #extrait les trames codés par c1 et c2
    e1, e2 = treat (e1), treat (e2)  #regroupe les bits par couples
    Lpriori = np.zeros (1784)        #information a priori initialement nulle
   
    for k in range (ni):
       
        Lsachant = mp.maxlogmap (e1, Lpriori)
        Lextrin = Lsachant - Lpriori - np.array ([h[0] for h in e1])
       
        Lpriori = tc.interleaver (Lextrin)
        Lsachant = mp.maxlogmap (e2, Lpriori)
        Lextrin = Lsachant - Lpriori - np.array ([h[0] for h in e2])
 
        Lpriori = deinterleaver (Lextrin)
    
    return deinterleaver (Lsachant)
 

def up (trame):
    e1, e2 = extrait (trame)
    e1, e2 = treat (e1), treat (e2)
    return e1, e2
'''
a = turbo (u)
a = -2*a +1
b = decoder (a, 4)
c = int32 (sign (b))
for k in range (len (c)):
    if c[k] == -1:
        c[k] = 0
print (sum (c!=u))
'''
 
#Lextrin = deinterleaver (Lsachant)*(-1) - deinterleaver (Lpriori) - array ([h[0] for h in e2])
"""
Lpriori = np.zeros (1784)
e1, e2 = extrait (turbo (u))
e1, e2 = treat (e1), treat (e2)
e1 = -2*e1 + 1
e2 = -2*e2 + 1
 
print (u)
#print (logmap (e1))
#print (maxlogmap (e1, Lpriori))
"""