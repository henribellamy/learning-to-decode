from numpy import *

 
 
def convolutif (bit, l, v):
    etat = l[-1]
    if etat == "a":
        if bit == 0:
            l.append ("a")
            v.append ((0, 0))
        else :
            l.append ("c")
            v.append ((1, 1))
    if etat == "b" :
        if bit == 0:
            l.append ("a")
            v.append ((1, 1))
        else :
            l.append ("c")
            v.append ((0, 0))
    if etat == "c":
        if bit == 0:
            l.append ("b")
            v.append ((1, 0))
        else :
            l.append ("d")
            v.append ((0, 1))
    if etat == "d":
        if bit == 0:
            l.append ("b")
            v.append ((0, 1))
        else :
            l.append ("d")
            v.append ((1, 0))
   

 
 
 
def convolutifSystematique (bit, l, v):
    etat = l[-1]
    if etat == "a":
        if bit == 0:
            l.append ("a")
            v.append ((0, 0))
        else :
            l.append ("c")
            v.append ((1, 1))
    if etat == "b" :
        if bit == 0:
            l.append ("c")
            v.append ((0, 0))
        else :
            l.append ("a")
            v.append ((1, 1))
    if etat == "c":
        if bit == 0:
            l.append ("d")
            v.append ((0, 1))
        else :
            l.append ("b")
            v.append ((1, 0))
    if etat == "d":
        if bit == 0:
            l.append ("b")
            v.append ((0, 1))
        else :
            l.append ("d")
            v.append ((1, 0))
 
 
def cc1 (u, want = False):
    l = ["a"]
    v = []
    u = list (u)
    while len (u) != 0:
        m = u.pop(0)
        convolutif (m, l, v)
    if want == True :
        return v, l
    return array (v)



def cc2 (u, want = False):
    l = ["a"]
    v = []
    u = list (u)
    while len (u) != 0:
        m = u.pop(0)
        convolutifSystematique (m, l, v)
    if want == True :
        return v, l
    return array (v)


def cc3 (u, want = False):
    d = random.randint (0, 4)
    if d == 0:
        l = ["a"]
    if d == 1:
        l = ["b"]
    if d == 2:
        l = ["c"]
    if d == 3:
        l = ["d"]
    v = []
    u = list (u)
    while len (u) != 0:
        m = u.pop(0)
        convolutifSystematique (m, l, v)
    if want == True :
        return v, l
    return array (v)