import numpy as np
import maxstar as ms
 
 
 
def maxlogmap (v, Lpriori = None):
    if Lpriori is None : 
        Lpriori = np.zeros (len (v))
    n = len (v)
    A = np.zeros ((n+1, 4))
    B = np.zeros ((n+1, 4))
    Gamma = [np.zeros ((4, 4)) for k in range (n)]
 
    for k in range (n):
   
        Gamma[k] [0] [0] = ms.scalaire (v[k][0], v[k][1], 1, 1) + (Lpriori[k] * (1))/2
        Gamma[k] [0] [2] = ms.scalaire (v[k][0], v[k][1], -1, -1) + (Lpriori[k] * (-1))/2
 
        Gamma[k] [1] [0] = ms.scalaire (v[k][0], v[k][1], -1, -1) + (Lpriori[k] * (-1))/2
        Gamma[k] [1] [2] = ms.scalaire (v[k][0], v[k][1], 1, 1) + (Lpriori[k] * (1))/2
 
        Gamma[k] [2] [1] = ms.scalaire (v[k][0], v[k][1], -1, 1) + (Lpriori[k] * (-1))/2
        Gamma[k] [2] [3] = ms.scalaire (v[k][0], v[k][1], 1, -1) + (Lpriori[k] * (1))/2
 
        Gamma[k] [3] [1] = ms.scalaire (v[k][0], v[k][1], 1, -1) + (Lpriori[k] * (1))/2
        Gamma[k] [3] [3] = ms.scalaire (v[k][0], v[k][1], -1, 1) + (Lpriori[k] * (-1))/2
 
       
    A[0][1] = -float ("inf")
    A[0][2] = -float ("inf")
    A[0][3] = -float ("inf")

    #A[1][0] = Gamma[0][0][0]
    #A[1][1] = -float ("inf")
    #A[1][2] = Gamma[0][0][2]
    #A[1][3] = -float ("inf")
 
   
    for k in range (0, n):
 
        A[k+1][0] = max (A[k][0] + Gamma[k][0][0], A[k][1] + Gamma[k][1][0])
        A[k+1][1] = max (A[k][2] + Gamma[k][2][1], A[k][3] + Gamma[k][3][1])
        A[k+1][2] = max (A[k][0] + Gamma[k][0][2], A[k][1] + Gamma[k][1][2])
        A[k+1][3] = max (A[k][2] + Gamma[k][2][3], A[k][3] + Gamma[k][3][3])

        A[k] = A[k] - max (A[k])

    
    #B[n][1] = -float ("inf")
    #B[n][2] = -float ("inf")
    #B[n][3] = -float ("inf")

    #B[n-1][0] = Gamma[n-1][0][0]
    #B[n-1][1] = Gamma[n-1][1][0]
    #B[n-1][2] = -float ("inf")
    #B[n-1][3] = -float ("inf")
 


    
    for k in reversed (range (0, n)):
 
        B[k][0] = max (B[k+1][0] + Gamma[k][0][0], B[k+1][2] + Gamma[k][0][2])
        B[k][1] = max (B[k+1][0] + Gamma[k][1][0], B[k+1][2] + Gamma[k][1][2])
        B[k][2] = max (B[k+1][1] + Gamma[k][2][1], B[k+1][3] + Gamma[k][2][3])
        B[k][3] = max (B[k+1][1] + Gamma[k][3][1], B[k+1][3] + Gamma[k][3][3])

        #B[k] = B[k] - max (B[k])

 
    LLR = []
    R0 = []
    R1 = []
 
    for k in range (n):
       
        R0.append ( max (
            A[k][0] + Gamma[k][0][0] + B[k+1][0],
            A[k][1] + Gamma[k][1][2] + B[k+1][2],
            A[k][2] + Gamma[k][2][3] + B[k+1][3],
            A[k][3] + Gamma[k][3][1] + B[k+1][1]))
 
        R1.append ( max (
            A[k][0] + Gamma[k][0][2] + B[k+1][2],
            A[k][1] + Gamma[k][1][0] + B[k+1][0],
            A[k][2] + Gamma[k][2][1] + B[k+1][1],
            A[k][3] + Gamma[k][3][3] + B[k+1][3]))
 
 
    for k in range (len (R1)):
        LLR.append (R0[k] - R1[k])
 
    M = []
   
    for h in LLR:
        if h > 0:
            M.append (0)
        if h < 0 :
            M.append (1)
           
    return np.array (LLR)
 
 
 
def logmap (v, Lpriori = None):
    if Lpriori is None : 
        Lpriori = np.zeros (len (v))
    n = len (v)
    A = np.zeros ((n+1, 4))
    B = np.zeros ((n+1, 4))
    Gamma = [np.zeros ((4, 4)) for k in range (n)]
 
    for k in range (n):
   
        Gamma[k] [0] [0] = ms.scalaire (v[k][0], v[k][1], 1, 1) + (Lpriori[k] * (1))/2
        Gamma[k] [0] [2] = ms.scalaire (v[k][0], v[k][1], -1, -1) + (Lpriori[k] * (-1))/2
 
        Gamma[k] [1] [0] = ms.scalaire (v[k][0], v[k][1], -1, -1) + (Lpriori[k] * (-1))/2
        Gamma[k] [1] [2] = ms.scalaire (v[k][0], v[k][1], 1, 1) + (Lpriori[k] * (1))/2
 
        Gamma[k] [2] [1] = ms.scalaire (v[k][0], v[k][1], -1, 1) + (Lpriori[k] * (-1))/2
        Gamma[k] [2] [3] = ms.scalaire (v[k][0], v[k][1], 1, -1) + (Lpriori[k] * (1))/2
 
        Gamma[k] [3] [1] = ms.scalaire (v[k][0], v[k][1], 1, -1) + (Lpriori[k] * (1))/2
        Gamma[k] [3] [3] = ms.scalaire (v[k][0], v[k][1], -1, 1) + (Lpriori[k] * (-1))/2
 
       
    A[0][1] = -float ("inf")
    A[0][2] = -float ("inf")
    A[0][3] = -float ("inf")

    A[1][0] = Gamma[0][0][0]
    A[1][1] = -float ("inf")
    A[1][2] = Gamma[0][0][2]
    A[1][3] = -float ("inf")
 
   
    for k in range (1, n):
 
        A[k+1][0] = ms.maxstar2 (A[k][0] + Gamma[k][0][0], A[k][1] + Gamma[k][1][0])
        A[k+1][1] = ms.maxstar2 (A[k][2] + Gamma[k][2][1], A[k][3] + Gamma[k][3][1])
        A[k+1][2] = ms.maxstar2 (A[k][0] + Gamma[k][0][2], A[k][1] + Gamma[k][1][2])
        A[k+1][3] = ms.maxstar2 (A[k][2] + Gamma[k][2][3], A[k][3] + Gamma[k][3][3])

        A[k] = A[k] - max (A[k])

    
    B[n][1] = -float ("inf")
    B[n][2] = -float ("inf")
    B[n][3] = -float ("inf")

    B[n-1][0] = Gamma[n-1][0][0]
    B[n-1][1] = Gamma[n-1][1][0]
    B[n-1][2] = -float ("inf")
    B[n-1][3] = -float ("inf")
 
 
    for k in reversed (range (0, n-1)):
 
        B[k][0] = ms.maxstar2 (B[k+1][0] + Gamma[k][0][0], B[k+1][2] + Gamma[k][0][2])
        B[k][1] = ms.maxstar2 (B[k+1][0] + Gamma[k][1][0], B[k+1][2] + Gamma[k][1][2])
        B[k][2] = ms.maxstar2 (B[k+1][1] + Gamma[k][2][1], B[k+1][3] + Gamma[k][2][3])
        B[k][3] = ms.maxstar2 (B[k+1][1] + Gamma[k][3][1], B[k+1][3] + Gamma[k][3][3])

        B[k] = B[k] - max (B[k])

 
    LLR = []
    R0 = []
    R1 = []
 
    for k in range (n):
       
        R0.append ( ms.maxstar4 (
            A[k][0] + Gamma[k][0][0] + B[k+1][0],
            A[k][1] + Gamma[k][1][2] + B[k+1][2],
            A[k][2] + Gamma[k][2][3] + B[k+1][3],
            A[k][3] + Gamma[k][3][1] + B[k+1][1]))
 
        R1.append ( ms.maxstar4 (
            A[k][0] + Gamma[k][0][2] + B[k+1][2],
            A[k][1] + Gamma[k][1][0] + B[k+1][0],
            A[k][2] + Gamma[k][2][1] + B[k+1][1],
            A[k][3] + Gamma[k][3][3] + B[k+1][3]))
 
 
    for k in range (len (R1)):
        LLR.append (R0[k] - R1[k])
 
    M = []
   
    for h in LLR:
        if h > 0:
            M.append (0)
        if h < 0 :
            M.append (1)
           
    return np.array (LLR)





def maxlogmapOptimisé(v, Lpriori=None):
    n = len(v)
    if Lpriori is None:
        Lpriori = np.zeros(n)

    A = -np.inf * np.ones((n + 1, 4))
    B = -np.inf * np.ones((n + 1, 4))
    Gamma = np.full((n, 4, 4), -np.inf)

    # === 1. Calcul des métriques Gamma ===
    for k in range(n):
        sys0 = ms.scalaire(v[k][0], v[k][1], 1, 1)
        sys1 = ms.scalaire(v[k][0], v[k][1], -1, -1)
        sys2 = ms.scalaire(v[k][0], v[k][1], -1, 1)
        sys3 = ms.scalaire(v[k][0], v[k][1], 1, -1)

        L = Lpriori[k]
        L2p = L / 2
        L2n = -L / 2

        # transitions valides du codeur
        Gamma[k][0][0] = sys0 + L2p
        Gamma[k][0][2] = sys1 + L2n
        Gamma[k][1][0] = sys1 + L2n
        Gamma[k][1][2] = sys0 + L2p
        Gamma[k][2][1] = sys2 + L2n
        Gamma[k][2][3] = sys3 + L2p
        Gamma[k][3][1] = sys3 + L2p
        Gamma[k][3][3] = sys2 + L2n

    # === 2. Initialisation Alpha ===
    A[0][0] = 0  # état initial
    A[1][0] = Gamma[0][0][0]
    A[1][2] = Gamma[0][0][2]

    # === 3. Propagation avant (Alpha) ===
    for k in range(1, n):
        Ak = A[k]
        Akp1 = A[k + 1]
        Gk = Gamma[k]

        Akp1[0] = max(Ak[0] + Gk[0][0], Ak[1] + Gk[1][0])
        Akp1[1] = max(Ak[2] + Gk[2][1], Ak[3] + Gk[3][1])
        Akp1[2] = max(Ak[0] + Gk[0][2], Ak[1] + Gk[1][2])
        Akp1[3] = max(Ak[2] + Gk[2][3], Ak[3] + Gk[3][3])

        A[k] -= np.max(A[k])  # normalisation pour éviter les overflow

    # === 4. Initialisation Beta ===
    B[n][0] = 0  # état final
    B[n - 1][0] = Gamma[n - 1][0][0]
    B[n - 1][1] = Gamma[n - 1][1][0]

    # === 5. Propagation arrière (Beta) ===
    for k in reversed(range(n - 1)):
        Bk = B[k]
        Bkp1 = B[k + 1]
        Gk = Gamma[k]

        Bk[0] = max(Bkp1[0] + Gk[0][0], Bkp1[2] + Gk[0][2])
        Bk[1] = max(Bkp1[0] + Gk[1][0], Bkp1[2] + Gk[1][2])
        Bk[2] = max(Bkp1[1] + Gk[2][1], Bkp1[3] + Gk[2][3])
        Bk[3] = max(Bkp1[1] + Gk[3][1], Bkp1[3] + Gk[3][3])

        B[k] -= np.max(B[k])  # normalisation

    # === 6. Calcul des LLR ===
    LLR = np.zeros(n)
    for k in range(n):
        Gk = Gamma[k]
        Ak = A[k]
        Bkp1 = B[k + 1]

        # transitions pour bit = 0
        R0 = max(
            Ak[0] + Gk[0][0] + Bkp1[0],
            Ak[1] + Gk[1][2] + Bkp1[2],
            Ak[2] + Gk[2][3] + Bkp1[3],
            Ak[3] + Gk[3][1] + Bkp1[1],
        )

        # transitions pour bit = 1
        R1 = max(
            Ak[0] + Gk[0][2] + Bkp1[2],
            Ak[1] + Gk[1][0] + Bkp1[0],
            Ak[2] + Gk[2][1] + Bkp1[1],
            Ak[3] + Gk[3][3] + Bkp1[3],
        )

        LLR[k] = R0 - R1

    return LLR


print ("neww maxlogmap")