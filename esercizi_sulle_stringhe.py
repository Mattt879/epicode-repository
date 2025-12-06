"""estrai primo ed ultimo carattere [0] è sempre il primo [-1] con riferimento negativo conta dal fondo"""
testo = "Python"
print("primo carattere: " , testo[0])
print("ultimo carattere: " , testo[-1])

"""convertire in maiuscolo e minuscolo"""
prova = "CoMpUtEr"
print(prova.upper())
print(prova.lower())

"""quante volte compare una lettera"""
ciao = "programmazione"
lettera = "a"
conteggio = ciao.count(lettera)
print(f"la lettera '{lettera}' compare {conteggio} volte.")

"""verificare se inizia e finisce con lettera specifica"""
saluto = "fantastico"
print(saluto.startswith("f"))
print(saluto.endswith("o"))

"""invertire una stringa questo è slicing [::-1]"""
matteo = "corso"
print(matteo[::-1])

"""estrarre caratteri in posizioni varie [::-2] negativo quindi parte dalla fine e prende un carattere ogni 2"""
ecco = "abcdefg"
print (ecco[::-2])

"""rimuovere gli spazi all'inizio e alla fine"""
pasto = "         ciao mondo        "
print (pasto.strip())
print(pasto)

"""prende e ripetere le prime 3 lettere varie volte"""
parola = "programmazione"
print (parola[:3]*3)
"""print (parola[:3]*3)  non mettendo nulla come primo input nella quadra prende il primo carattere,come secondo input l'ultimo carattere in quella posizione [:3] quindi pro"""
print (parola[2:6]*3)
"""inserendo un numero nella quadra come primo input esclude quei caratteri partendo da successivo e come secondo input l'ultima lettera [2:6] quindi ogra"""