#stampa numeri da 1 a 10
for i in range (1, 11):
    print(i)
#metti 11 perchè l'ultimo lo salta

#stampa numeri pari da 1 a 20

for q in range ( 2, 21, 2):
    print (q)
#la funzione 2 salta di 2 in 2 

#stampa le lettere della parola
parola = "python"
for c in parola:
    print (c)

#somma numeri da 1 a 100
somma = 0
for w in range (1, 101):
    somma += w
print (somma)

#somma con contatore basta lasciarlo sotto for vedi ultima riga
somma = 0
for w in range (1, 101):
    somma += w
    #print(somma)


#stampa tabellina
for e in range (1, 11):
    print (f" 5 x {e} = {5*e}")

#calcolo fattorale di un  numero
print ("fattoriale")
p = 5
fattoriale = 1
for i in range (1, p+1):
    fattoriale *= i
print ("fattoriale: ", fattoriale)

#contare quante vocali ci sono in una parola
prova = "programmazione"
vocali = "aeiou"
conta = 0
for z in prova:
    if z in vocali:
        conta +=1
print ("le vocali totali sono:", conta)

#stampa una matrice 3x3
for u in range (1, 4):
    for s in range (1, 4):
        print (u, s, end = "  ")
    print ()

#operatore contniue da 1 a 10 salta 5

for r in range (1, 11):
    if r == 5:
        continue
    print (r)

#break con fermo a 7

for p in range (1, 11):
    if p == 8:
        break
    print (p)