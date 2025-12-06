#chiedi a utente di inserire numero positivo continua a chiedere finchè non inserice >0 
#stampa quando positivo hai inserito numero positivo: X

numero1 = int(input("inserisci un numero positivo: "))
while numero1 <= 0:
    print (f"riprova")
    numero1 = int(input("inserisci un numero: "))
    
print(f"Hai inserito il numero positivo: {numero1}")
