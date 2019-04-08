def trirap(M):
    if M==[]:
        return []
    else:
        p=M[0]
        t1=[]
        t2=[]
        for x in M[1:]:
            if x<p:
                t1.append(x)
            else:
                t2.append(x)
        return trirap(t1)+[p]+trirap(t2)
