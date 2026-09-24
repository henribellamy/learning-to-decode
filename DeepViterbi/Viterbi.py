from math import sqrt
from numpy import *
 
 
 
def f (x, y, m, n):
    return  - (x*m + y*n)
 
 
def viterbi (s, v):
    s["a"][0] = f(v[0], v[1], 1, 1) + f(v[2], v[3], 1, 1)
    s["a"][1] = ["a", "a", "a"]
 
    s["b"][0] = f(v[0], v[1], -1, -1) + f(v[2], v[3], -1, 1)
    s["b"][1] = ["a", "c", "b"]
 
    s["c"][0] = f(v[0], v[1], 1, 1) + f(v[2], v[3], -1, -1)
    s["c"][1] = ["a", "a", "c"]
 
    s["d"][0] = f(v[0], v[1], -1, -1) + f(v[2], v[3], 1, -1)
    s["d"][1] = ["a", "c", "d"]
 
    v = v[4:]
   
    for k in range (int (len (v)/2)):
        x,y = v[2*k], v[2*k +1]
        la, lb, lc, ld = s["a"][1], s["b"][1], s["c"][1], s["d"][1]
        va, vb, vc, vd = s["a"][0],s["b"][0],s["c"][0],s["d"][0]
 
        if f (x,y,1,1) + va > f(x,y,-1,-1) + vb:
            s["a"][0] = vb + f(x,y,-1,-1)
            s["a"][1] = lb + ["a"]
        else :
            s["a"][0] = va + f(x,y,1,1)
            s["a"][1] = la + ["a"]
 
 
        if f (x,y,-1,1) + vc > f(x,y,1,-1) + vd:
            s["b"][0] = vd + f(x,y,1,-1)
            s["b"][1] = ld + ["b"]
        else :
            s["b"][0] = vc + f(x,y,-1,1)
            s["b"][1] = lc + ["b"]
 
 
        if f (x,y,1,1) + vb > f(x,y,-1,-1) + va:
            s["c"][0] = va + f(x,y,-1,-1)
            s["c"][1] = la + ["c"]
        else :
            s["c"][0] = vb + f(x,y,1,1)
            s["c"][1] = lb + ["c"]
 
 
        if f (x,y,1,-1) + vc > f(x,y,-1,1) + vd:
            s["d"][0] = vd + f(x,y,-1,1)
            s["d"][1] = ld + ["d"]
        else :
            s["d"][0] = vc + f(x,y,1,-1)
            s["d"][1] = lc + ["d"]
 
 
 
 
 
def chemin (s):
    etat = 0
    x = min (s["a"][0], s["b"][0], s["c"][0], s["d"][0])
 
    if x == s["a"][0]:
        etat = "a"
    if x == s["b"][0]:
        etat = "b"
    if x == s["c"][0]:
        etat = "c"
    if x == s["d"][0]:
        etat = "d"
 
    return s[etat][1]
 
###########################Viterbi1 non systématique############################
 
 
def valeur1(i,j):
    if i == "a":
        if j == "a" :
            return 0
        return 1
    if i == "b" :
        if j == "a":
            return 0
        return 1
    if i == "c":
        if j == "b" :
            return 0
        return 1
    if i == "d":
        if j == "b":
            return 0
        return 1
 
 
def lecture1 (c):
    l = []
    for k in range (len (c)-1):
        l.append (valeur1 (c[k], c[k+1]))
    return l
 
 
 
def decoder1 (v):
    s = {"a" : [0, []], "b" : [0, []], "c" : [0, []], "d" : [0, []]}
    viterbi (s,v)
    return lecture1 (chemin (s))
 
 
 
###########################Viterbi2 systématique################################
 
def valeur2(i,j):
    if i == "a":
        if j == "a" :
            return 0
        return 1
    if i == "b" :
        if j == "c":         #Pour non syst : mettre "a"
            return 0
        return 1
    if i == "c":
        if j == "d" :        #Pour non syst : mettre "b"
            return 0
        return 1
    if i == "d":
        if j == "b":
            return 0
        return 1
 
 
def lecture2 (c):
    l = []
    for k in range (len (c)-1):
        l.append (valeur2 (c[k], c[k+1]))
    return l
 
 
 
def decoder2 (v):
    s = {"a" : [0, []], "b" : [0, []], "c" : [0, []], "d" : [0, []]}
    viterbi (s,v)
    return lecture2 (chemin (s))
