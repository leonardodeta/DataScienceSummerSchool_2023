# scrivi la funzione
def mangia(scatola : list):
    for x in range(len(scatola)):
        if scatola[x] % 2 != 0:
            scatola[x] = scatola[x] - 1
    



# NON TOCCARE, queste linee devono funzionare
scatola1 = [3, 3, 3, 3, 3]
scatola2 = [1, 3, 5, 7, 9]
scatola3 = [19, 3, 14, 1, 10, 9, 2, 16, 8, 7, 13, 11, 18, 17, 6, 5, 4, 12, 20, 15]

mangia(scatola1)  # deve MODIFICARE scatola1
mangia(scatola2)
mangia(scatola3)

print(scatola1) # Deve stampare la lista [2, 2, 2, 2, 2]
print(scatola2) # Deve stampare la lista [0, 2, 4, 6, 8]
print(scatola3) # Deve stampare la lista [18, 2, 14, 0, 10, 8, 2, 16, 8, 6, 12, 10, 18, 16, 6, 4, 4, 12, 20, 14]


print(mangia([2,4,5,7])) # DEVE stampare None. Perchè ?
# perché non c'è il return