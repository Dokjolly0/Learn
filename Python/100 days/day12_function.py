def suggerimento(secret, choise):
    if secret != choise:
        if choise > 0 and choise < 101:
            if choise > secret:
                print("Il numero è piu basso! ")
            elif choise < secret:
                print("Devi inserire un numero piu alto! ")
        else:
            print("Devi inserire un numero compreso tra 1 e 100\n")
    else:
        print("Complimenti, hai indovinato il numero! ")
        exit()

def richiedi(secret, choise, attemps):
    print(f"Tentativi rimanenti: {attemps}")
    if attemps > 0:
        try:
            choise = int(input("Indovina il un numero da 1 a 100: "))
            suggerimento(secret, choise)
            return choise
        except ValueError:
            print("Devi inserire un numero! ")
    else:
        print("Hai esaurito i tentativi! ")
        exit()