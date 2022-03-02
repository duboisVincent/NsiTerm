def rechercheMAX(lst):
    maxi = lst[0]
    indi = 0
    for i in range(1,len(lst)):
        if lst[i] > maxi:
            maxi = lst[i]
            indi = i
    return (maxi,indi)

def rechercheGENE(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j = j + 1
        if j == g:
            trouve = True
        i = i + 1
    return trouve
rechercheGENE("ATCG","wxcATCGwxc")