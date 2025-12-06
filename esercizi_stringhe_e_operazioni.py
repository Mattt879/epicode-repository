# CHIEDE UNA FRASE E INVERTE L'ORDINE DELLE PAROLE
frase = input("Inserisci una frase: ")

# Inversione dell'ordine delle parole
parole = frase.split()
parole_invertite = parole[::-1]
frase_invertita = " ".join(parole_invertite)
print("La frase con l'ordine delle parole invertito è:", frase_invertita)

# CONTROLLO PALINDROMO (IGNORA SPAZI E MAIUSCOLE)

# 1. Normalizzazione della frase: minuscolo e senza spazi
frase_minuscola = frase.lower()
frase_normalizzata = frase_minuscola.replace(" ", "")

# 2. Inversione dei caratteri della frase normalizzata
frase_invertita_caratteri = frase_normalizzata[::-1]

# 3. Confronto e risultato

if frase_normalizzata == frase_invertita_caratteri:
    print(f"La frase '{frase}' è un palindromo")
else:
    print(f"La frase '{frase}' non è un palindromo.")