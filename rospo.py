parola, ripetizioni = "rospo", "14323"           # 'roooosssppooo'
parola, ripetizioni = "artificio", "144232312"  # 'arrrrttttiifffiicccioo'

# scrivi qui


def wow(p, r):
    risultato = ""
    for i, let in enumerate(p):
        if i < len(r):
            num_ripetizioni = int(r[i])
            risultato += let * num_ripetizioni
    return risultato

ris = wow(parola, ripetizioni)
print(ris)