import numpy as np
import maxlogmap2turbo as mp
import turbocode as tc
import turbodecode as td

def prior (e1, e2, ni):
    X, Y = [], []
    Lpriori = np.zeros (1784)
    iter = 0
    
    for k in range (((ni-1)//2)+1):
       
        Lsachant = mp.maxlogmap (e1, Lpriori)
        Lextrin = Lsachant - Lpriori - np.array ([h[0] for h in e1])
        iter += 1

        if iter == ni:
            x = np.stack([np.array([h[0] for h in e1]), np.array([h[1] for h in e1]), Lpriori], axis= - 1)
            y = Lsachant.copy()
            X.append (x)
            Y.append (y)
        
        Lpriori = tc.interleaver (Lextrin)

        Lsachant = mp.maxlogmap (e2, Lpriori)
        Lextrin = Lsachant - Lpriori - np.array ([h[0] for h in e2])
        iter += 1

        if iter == ni:
            x = np.stack([np.array([h[0] for h in e2]), np.array([h[1] for h in e2]), Lpriori], axis = -1)
            y = Lsachant.copy()
            X.append (x)
            Y.append (y)

        Lpriori = td.deinterleaver (Lextrin)
    
    return np.array (X), np.array (Y)


print ("new m")