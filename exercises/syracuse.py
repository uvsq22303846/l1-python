import random

n = random.randint(1, 100) 
n_max = random.randint(1, 1000)

def syracuse(n):
    
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        liste.append(n)
    return liste

def TestConjecture(n_max):
    for i in range(1, n_max +1):
        last = syracuse(i)[-1]
        if last == 1:
            return True
        else:
            return False

def tempsVol(n):
    return len(syracuse(n))

def tempsVolListe(n_max):
    vol_liste = []
    for i in range(1, n_max+1):
        vol = len(syracuse(i))
        vol_liste.append(vol)
    return vol_liste

print(syracuse(n))
print(TestConjecture(n_max))
print(tempsVol(n))
print(tempsVolListe(n_max))