import os
import json

# #### Problema 3: Sistema di prenotazione
# Crea un programma che simula un semplice sistema di prenotazione per un ristorante. Il programma deve consentire di:
# - Aggiungere una prenotazione con il nome del cliente e il numero di persone.
# - Cancellare una prenotazione specificando il nome del cliente.
# - Visualizzare tutte le prenotazioni.

def scrivi_su_json(path, new_data):
    if os.path.exists(path):
        #print("Esiste")
        with open(path, 'r') as file:
            existing_data = json.load(file)
        
        # Controlla se existing_data è una lista
        if isinstance(existing_data, list):
            existing_data.append(new_data)
        else:
            # Se non è una lista, crea una lista con l'elemento esistente e il nuovo dato
            existing_data = [existing_data, new_data]
    else:
        print("Non esiste")
        existing_data = [new_data]
    
    with open(path, 'w') as file:
        json.dump(existing_data, file, indent=4)
        

def cerca_per_nome(path, value):
    #Se non esiste la path ritorna none
    if not os.path.exists(path):
        return None
    
    #Leggi e salva il json attuale su un file
    with open(path, 'r') as file:
        data = json.load(file)
        
        #Se è una lista
        if isinstance(data, list):
            #Tra tutte le chiavi cerca il valore
            for item in data:
                #Se lo trovi lo ritorni
                if item.get("Nome") == value:
                    return item
    #Altrimenti ritorni none
    return None

def search_all(path):
    #Se non esiste la path ritorna none
    if not os.path.exists(path):
        return None
    
    #Leggi e salva il json attuale su un file
    with open(path, 'r') as file:
        data = json.load(file)
        data_list = []
        #Se è una lista
        if isinstance(data, list):
            return data
    #Altrimenti ritorni none
    return None

def cancella_oggetto(lista, nome):
    return [oggetto for oggetto in lista if oggetto["Nome"] != nome]
        

print("Benvenuto al servizio di prenotazione del ristorante! \n")
#user = input("Se sei admin logga, altrimenti prosegui per prenotare. login/any: ").lower()
user = "login"

if user == 'login':
    select = -1
    print("Benvenuto nel gestionale, scegli una voce del seguente menu. \n")
    print("0. Esci. \n")
    print("1. Visualizza prenotazioni. \n")
    print("2. Cancella una prenotazione. \n")
    print("3. Inserisci manualmente una prenotazione. \n")
    print("4. Cerca una specifica prenotazione: \n")
    
    while select < 0 or select > 4:
        try:
            select = int(input("Scelta: "))
            if select < 0 or select > 4:
                print("Inserisci un numero tra quelli elencati nel menu. \n")
        except ValueError:
            print("Inserisci un numero valido: \n")
            select = -1

    if select == 0:
        
        exit()
        
    elif select == 1:
        
        arr_persone = []
        arr_nomi = []
        i = 0
        data = search_all("prenotazioni.json")
        print(data)
        print("\n\n")
        for prenotazione in data:
            try:
                nome = data[i]["Nome"]
                persone = data[i]["Persone"]
                arr_persone.append(persone)
                arr_nomi.append(nome)
                i += 1
                print(f"La prenotazione numero {i} è stata fatta da {nome} ed ha richiesto un tavolo da {persone} persone.")
                
            except TypeError:
                print("Non ci sono prenotazioni ")
        
    elif select == 2:
        
        found = False
        i = 0
        # Leggi il file JSON
        try:
            with open('prenotazioni.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except:
            print("Nessuna prenotazione attualmente registrata. ")
            exit()
            
        while found == False:
            nome_da_cancellare = input("Inserisci il nome da cancellare: ").lower()
            for prenotazione in data:
                try:
                    #print("Try")
                    nome = data[i]["Nome"]
                    #print(nome)
                    i += 1
                    if nome == nome_da_cancellare:
                        break
                except:
                    print("Errore ")
                    
            if nome == nome_da_cancellare:
                print("Trovato ")
                found = True
                break
            else: 
                response = input("Nome non trovato, vuoi trovarne un altro? y/n: ").lower()
                if response == 'y':
                    i = 0
                    continue
                else:
                    found = True        
        new_data = cancella_oggetto(data, nome)

        # Scrivi il file JSON aggiornato
        with open('prenotazioni.json', 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)
        
    elif select == 3:
        
        nome = input("Inserisci il nome della prenotazione: ").lower()
        persone = input("Inserisci il numero di persone: ").lower()
        convert = False
        while convert == False:
            try:
                persone = int(persone)
                convert = True
            except ValueError:
                persone = input("Non è un numero di persone valido, inserisci un numero valido: ")
                convert = False # Lo metto ma non necessario
        
        #path = os.path.dirname(os.path.abspath(__file__)) + "prenotazioni.json"
        new_data = {
            "Nome": nome,
            "Persone": persone,
        }
        scrivi_su_json("prenotazioni.json", new_data)
        
    elif select == 4: 
        
        query = input("Inserisci il nome della prenotazione da cercare: ").lower()
        data = cerca_per_nome("prenotazioni.json", query)
        try:
            nome = data["Nome"]
            persone = data["Persone"]
            print(f"La prenotazione è stata effettuata a nome di {nome} ed è per {persone} persone")
        except TypeError:
            print("La prenotazione non esiste. ")
        
    else: 
        print("Numero non valido! ") ## Controllato anche dal while
        