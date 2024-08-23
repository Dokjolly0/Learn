import random

print(r"""
      
______ _            _    _            _    
| ___ \ |          | |  (_)          | |   
| |_/ / | __ _  ___| | ___  __ _  ___| | __
| ___ \ |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_/ / | (_| | (__|   <| | (_| | (__|   < 
\____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/  

      """)

carte_giocatore = []
carte_banco = []
carte_desponibili = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'j', 'j', 'j', 'j', 'Q', 'Q', 'Q', 'Q', 'k', 'k', 'k', 'k']
max_index = len(carte_desponibili) -1

def ripesca(scelta):
    if scelta == 'y':
        pesca_carta('player')
        print(f"Carte giocatore: {carte_giocatore}")
        scelta = input("Vuoi pescare una nuova carta? y/n: ").lower()
        return scelta
    else: 
        exit()

def pesca_carta(player):
    global max_index
    player = player.lower()
    if player == 'player':
        index_player = random.randint(0, max_index)
        max_index -= 1
        carte_giocatore.append(carte_desponibili[index_player])
        carte_desponibili.pop(index_player)
        #print(f"Index player: {max_index_player}")
    elif player == 'banco':
        index_banco = random.randint(0, max_index)
        max_index -= 1
        carte_banco.append(carte_desponibili[index_banco])
        carte_desponibili.pop(index_banco)
        #print(f"Index banco: {max_index_banco}")
    else:
        print("Player non valido, perfavore inserisci o 'player', o 'banco'")
        return
    
def calcola_valore(player):
    valore_totale = 0
    if player == 'player':
        for card in carte_giocatore:
            if card == 1:
                scelta = input("Vuoi tenere il valore dell'asso 1 o 11? ").lower()
                while scelta != '1' or scelta != '11' and card:
                    if scelta == '1':
                        valore_totale += 1
                        break
                    elif scelta == '11':
                        valore_totale += 11
                        break
                    else:
                        scelta = input("Inserisci il valore che preferisci, o 1 o 11: ").lower()
                    #print(scelta)
            elif card in range(2, 11):
                valore_totale += card
            elif card == 'j' or card == 'Q' or card == 'k':
                valore_totale += 10
        #print(f"Valore totale player: {valore_totale}")
        return valore_totale
    elif player == 'banco':
        assi_banco = []
        for card in carte_banco:
            if card == 1:
                assi_banco.append(card)
            elif card in range(2, 11):
                valore_totale += card
            elif card == 'j' or card == 'Q' or card == 'k':
                valore_totale += 10
            #print(valore_totale)
            
            if len(assi_banco) == 1 and valore_totale > 10:
                valore_totale += 1
            elif len(assi_banco) == 1 and valore_totale < 10:
                valore_totale += 11
            elif len(assi_banco) >= 2:
                valore_totale += 12
        #print(f"Valore totale banco: {valore_totale}")
        return valore_totale
    else:
        print("Player non valido, perfavore inserisci o 'player', o 'banco'")
        return
    
def play():
    ##Pesca carte
    pesca_carta('player')
    pesca_carta('player')
    pesca_carta('banco')
    pesca_carta('banco')
    
    
    ##Stampa carte
    print(f"Carte giocatore: {carte_giocatore}")
    print(f"Carte banco: [{carte_banco[0]}]")
    ##Scelta player
    scelta = input("Vuoi pescare una nuova carta? y/n: ").lower()
    while scelta == 'y':
        scelta = ripesca(scelta)
        
        
        
    ##Mostra carte banco
    print(f"Carte banco: {carte_banco}")
    ##Calcola valore
    totale_player = calcola_valore('player')
    totale_banco = calcola_valore('banco')
    while totale_banco < 17:
        print("\nIl banco non totalizza 17, pesca un'altra carta: ")
        pesca_carta('banco')
        totale_banco = calcola_valore('banco')
        print(f"Carte banco: {carte_banco}")
        print("\n")
        
        
        
    ##Stabilisci vincitore
    if totale_banco > 21 and totale_player > 21:
        print("Entrambi i giocatori hanno perso! ")
        print(f"Totale player: {totale_player} {carte_giocatore} \nTotale banco: {totale_banco} {carte_banco}")
    elif totale_banco <= 21 and totale_player > 21:
        print(f"\nIl banco ha vinto con un punteggio di {totale_banco}! ")
        print(f"Totale player: {totale_player} {carte_giocatore} \nTotale banco: {totale_banco} {carte_banco}")
    elif totale_banco > 21 and totale_player <= 21:
        print(f"\nIl player ha vinto con un punteggio di {totale_player}! ")
        print(f"Totale player: {totale_player} {carte_giocatore} \nTotale banco: {totale_banco} {carte_banco}")
    else:
        vicinanza_punti_player = 21 - totale_player
        vicinanza_punti_banco = 21 - totale_banco
        if vicinanza_punti_banco < vicinanza_punti_player:
            print(f"\nIl banco ha vinto con un punteggio di {totale_banco}! ")
            print(f"Totale player: {totale_player} {carte_giocatore} \nTotale banco: {totale_banco} {carte_banco}")
        else:
            print(f"\nIl player ha vinto con un punteggio di {totale_player}! ")
            print(f"Totale player: {totale_player} {carte_giocatore} \nTotale banco: {totale_banco} {carte_banco}")
    

def reset():
    carte_giocatore = []
    carte_banco = []
    carte_desponibili = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'j', 'j', 'j', 'j', 'Q', 'Q', 'Q', 'Q', 'k', 'k', 'k', 'k']
    print("\n")

def main():
    play()
        
        
if __name__ == "__main__":
    try:
        main()
        rematch = input("Vuoi rigiocare? y/n: ").lower()
        while rematch == 'y':
            reset()
            main()
    
            if rematch != 'y':
                exit()
    except KeyboardInterrupt:
        print("Uscita dal gioco. ")
