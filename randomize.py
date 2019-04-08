import random as r
def randomize(L):
    M1=[]
    M2=[]
    M1=L.copy()
    while len(M1)>0:
        r
        p=M1.pop(r.randint(0,len(M1)-1))
        M2.append(p)
    return M2
