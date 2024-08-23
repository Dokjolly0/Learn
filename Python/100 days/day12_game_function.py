import random
import day12_function as function

def guess_my_number():
    print("Benvenuto nel guess my number game! ")
    secret = random.randint(1, 101)
    attemps = 0
    
    while attemps <= 0:
        try:
            attemps = int(input("Inserisci il numero di tentativi per indovinare il numero: "))
        except ValueError: 
            print("Devi inserire un numero! ")
    
    try:
        choise = int(input("Indovina il un numero da 1 a 100: "))
        function.suggerimento(secret, choise)
        attemps -= 1
    except ValueError:
        choise = 0
        print("Devi inserire un numero! ")
        
    while secret != choise:
        choise = function.richiedi(secret, choise, attemps)
        attemps -= 1
        
def pari_o_dispari():
    condition = False
    player = input("Scegli se vuoi essere pari o dispari: ").lower()
    while player != 'pari' and player != 'dispari':
        player = input("Inserisci o pari o dispari: ").lower()
        
    while condition == False:
        try:
            numero_player = int(input("Inserisci un numero: "))
            condition = True
        except ValueError:
            print("Inserisci un numero valido\n")
            condition = False

    numero_cpu = random.randint(1, 201)
    totale = numero_cpu + numero_player
    
    if totale %2 == 0:
        print(f"Pari ({totale})")
        if player == 'pari':
            print("Hai vinto! ")
        else:
            print("Ha vinto il pc! ")
    else:
        print(f"Dispari ({totale})")
        if player == 'dispari':
            print("Hai vinto! ")
        else:
            print("Ha vinto il pc! ")
            
            
            
"""
_______________________
|      |      |      |
|      |      |      |
|______|______|______|
|      |      |      |
|      |      |      |
|______|______|______|
|      |      |      |
|      |      |      |
|______|______|______|
"""
            