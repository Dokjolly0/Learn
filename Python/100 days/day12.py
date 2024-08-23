import day12_function as function
import day12_game_function as game
            
def main():
    scelta = 0
    while scelta <= 0:
        try:
            print("1. Indovina il numero")
            print("2. Pari o dispari")
            scelta = int(input("\nScegli il gioco: "))
        except ValueError:
            print("Devi inserire un numero! ")
            
    if scelta == 1:
        game.guess_my_number()
    elif scelta == 2:
        game.pari_o_dispari()
    else:
        print("Gioco non ancora implementato! ")
        exit()
    
if __name__ == "__main__":
    try:
        #main()
        print()
    except KeyboardInterrupt:
        print("\nUscita dal gioco. ")
        
#Tiro 10 -> Se fai strike al primo dei 2 tiri hai diritto a 2 tiri in piu
#Tiro 10 -> Se fai spare entro i 2 tiri hai diritto a 1 tiri in piu
#Spare -> Lo spare vale 10 + il risultato del turo dopo
#Strike -> Lo strike vale 10 + i 2 tiri successivi
        