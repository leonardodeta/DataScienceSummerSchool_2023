panini, burgers = 3, 5   # Servito bla bla... alla fine stampa 'Avanzano 2 burger.'
#panini, burgers = 9,3   # Servito bla bla... alla fine stampa 'Avanzano 6 panini.'
#panini, burgers = 4,4   # Servito bla bla... alla fine stampa 'credenza vuota!'

# scrivi qui
while panini > 0:
    if burgers <= 0:
        break
    panini = panini - 1
    burgers = burgers - 1
    print("servito un panino:", panini, "panini rimanenti,", burgers, "burgers rimanenti")

if panini == 0 and burgers == 0:
    print("Credenza vuota!")
else:
    if burgers > panini: 
        print("Avanzano", burgers, "burgers")
    else:
        print("Avanzano", panini, "panini")

####################### 
print("")
print("#"*100, "\n")

panini, burgers = 3, 5   # Servito bla bla... alla fine stampa 'Avanzano 2 burger.'
#panini, burgers = 9,3   # Servito bla bla... alla fine stampa 'Avanzano 6 panini.'
#panini, burgers = 4,4   # Servito bla bla... alla fine stampa 'credenza vuota!'


while panini > 0 and burgers > 0:
    panini = panini - 1
    burgers = burgers - 1
    print("servito un panino:", panini, "panini rimanenti,", burgers, "burgers rimanenti")

if panini == 0 and burgers == 0:
    print("Credenza vuota!")
else:
    if burgers > panini: 
        print("Avanzano", burgers, "burgers")
    else:
        print("Avanzano", panini, "panini")