def moyenne(liste):
    numé = 0
    deno = 0
    for valeurs in liste:
        note = valeurs[0]
        coeff = valeurs[1]
        numé = numé + note * coeff
        deno = deno + coeff
    return numé/deno
    
def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
