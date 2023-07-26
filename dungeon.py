cerco,caverna='il tesoro', ['un masso','una trappola','delle spade','il tesoro','una ragnatela','un boleto delle tombe']

cerco,caverna = 'il talismano del potere', ['una trappola','un boleto delle tombe','una ragnatela']
cerco, caverna = 'la corona di rubini', []                         # funziona anche in questi casi particolari?
#cerco, caverna = 'la corona di rubini', ['la corona di rubini']    #
#cerco, caverna = 'la corona di rubini', ['il martello di granito'] #

# scrivi qui

print("Entro")
x = 0
while x < len(caverna):
    if caverna[x] != cerco:
        print("Vedo", caverna[x])
    else:
        print("Che fortuna, ho trovato",cerco)
        break
    x += 1

# Non trovo quello che cerco?
if caverna == []:
    print("Purtroppo", cerco, "non c'è, la caverna è vuota ")
else:
    if caverna[x-1] != cerco:
        print("Purtroppo", cerco, "non c'è")

# è ora di tornare
print("Torno indietro")


x -= 1 # tolgo uno così non stampa quello che cerco di nuovo
while x != -1:
    print("vedo", caverna[x])
    x -= 1
print("Esco")
