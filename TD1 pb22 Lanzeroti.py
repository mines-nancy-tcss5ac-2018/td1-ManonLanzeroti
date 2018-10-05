def trier():
    f= open('p022_names.txt','r')
    fichier=f.read()
    files = fichier.split(",")
    tri= sorted(files)
    return tri

def ordonne(caractere):
    L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    i=0
    while caractere != L[i] and i<len(L):
        i+=1
    return i+1

def valeur(P):
    val=0
    for caractere in P: #on �value la valeur de chaque lettre du pr�nom
        if caractere== '"' : val+=0
        else: val += ordonne(caractere) 
    return val #val est la valeur du pr�nom P

def solve():
    S=0
    tri=trier()
    val=0
    values=[] #liste qui contient la valeur de chaque pr�nom
    for P in tri: 
        val=valeur(P)
        values.append(val)  #values contient les valeurs de chaque pr�nom
    n=len(values)
    for i in range(n):
        S+= (i+1)*values[i]
    return S

print(solve())
