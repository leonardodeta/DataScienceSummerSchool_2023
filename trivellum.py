
carrello = []
pozzo = ['███','▓▓▓','▒▒▒', '░░░']  # <-- cima del pozzo
#pozzo = ['┼┼','┤├','┐┌', '╗╔', '║║']  #  ['║', '║', '╗', '╔', '┐', '┌', '┤', '├', '┼', '┼']

# scrivi qui

x = len(pozzo)
while x != 0:
    x -= 1
    blocchi = list(pozzo[x]) # trasformo la stringa in una lista con i tre elementi
    print('il pozzo è', pozzo) # stampo il pozzo
    print("trivello lo strato", pozzo[x], "e lo divido nei blocchi", blocchi) # stampo il blocco che mi interessa e la nuova lista creata
    pozzo.remove(pozzo[x]) # tolgo il blocco dal pozzo
    carrello += blocchi # aggiungo al carrello i miei blocchi
    

print('il pozzo finale è:', pozzo)
print('il carrello finale è:', carrello)

