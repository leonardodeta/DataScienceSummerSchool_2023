# scrivi la funzione

def nobulli(bullo : str):
    nuovo = ''
    for x in range(len(bullo)):
        if bullo[x] == 'w' or bullo[x] == 'a' or bullo[x] == 'k' or bullo[x] == 'a' or bullo[x] == ' ':
            nuovo = nuovo + bullo[x]
    return nuovo

def nobulli2(bullo, m):
    nuovo = ''
    for x in range(len(bullo)):
        for y in range(len(m)):
            if bullo[x] == m[y]: 
                nuovo = nuovo + bullo[x]
    return nuovo


# NON TOCCARE, queste linee devono funzionare
bullo1 = "waekai waekai waekai waekai"
bullo2 = "bwaka rwaka swaka twaka zwaka mmmwatka"
bullo3 = "eweaekea zwxarkma qwoagkpa"
res1 = nobulli(bullo1)   # Deve RITORNARE il verso pulito "waka waka waka waka"
print(res1)
res2 = nobulli(bullo2)   # Deve RITORNARE il verso pulito "waka waka waka waka waka waka"
print(res2)
res3 = nobulli(bullo3)   # Deve RITORNARE il verso pulito "waka waka waka"
print(res3)


print('-------')


mantieni = ['w', 'a', 'k', ' ']
res4 = nobulli2(bullo1, mantieni)   # Deve RITORNARE il verso pulito "waka waka waka waka"
print(res4)
res5 = nobulli2(bullo2, mantieni)   # Deve RITORNARE il verso pulito "waka waka waka waka waka waka"
print(res5)
res6 = nobulli2(bullo3, mantieni)   # Deve RITORNARE il verso pulito "waka waka waka"
print(res6)