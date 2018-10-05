def rev(chaine): #inverse la chaine de caractère
    rev_chaine = ""
    for lettre in chaine:
        rev_chaine = lettre + rev_chaine
    return rev_chaine

def nombreinverse(nombre): #renvoie le nombre dont les chiffres sont inversés
    chaine = str(nombre)
    rev_chaine = ""
    for lettre in chaine:
        rev_chaine = lettre + rev_chaine
    return int(rev_chaine)


def palindrome(n): #vérifie si un nombre est un palindrome
    ch1, ch2 = "", ""
    ch_n = str(n)
    revch_n = rev(ch_n)
    s = n + int(revch_n) #on fait la somme de n et son inversé
    ch_s = str(s)
    revch_s = rev(ch_s)
    l=len(ch_s)
    for i in range(l//2):
        ch1 += ch_s[i]
        ch2 += revch_s[i]
    if ch1 == ch2: return True
    else: return False

def Lychrel(nombre): #renvoie True si le nombre considéré est un nombre de Lychrel et renvoie False sinon
    j=0
    nb = nombre
    p = palindrome(nb)
    while p == False and j < 50:
        nbinverse = nombreinverse(nb)
        nb = nb + nbinverse
        p = palindrome(nb)
        j += 1
    if j==50: return True
    else: return False
     

#détermine le nombre de nombres de Lychrel plus petits que n   
def solve(n):
    i=0
    for nombre in range(n +1):
        if Lychrel(nombre) == True:
            i+=1
    return i
        
    
print(solve(10000))
        