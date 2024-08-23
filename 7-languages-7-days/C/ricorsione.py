import os

def clear_console():
    if os.name == 'nt':  # Per Windows
        os.system('cls')
    else:  # Per Unix-like (Linux, macOS)
        os.system('clear')

def fattoriale(n):
    # Caso base: se n è 0, il fattoriale di 0 è 1
    if n == 0:
        print("Il numero è 0")
        return 1
    # Caso ricorsivo: n! = n * (n-1)!
    else:
        # Chiamata ricorsiva per calcolare (n-1)!
        risultato_parziale = fattoriale(n - 1)
        # Calcolo del fattoriale corrente moltiplicando n per il risultato parziale
        risultato = n * risultato_parziale
        # Stampa del valore corrente e del risultato
        print(n, risultato)
        return risultato

def main():
    clear_console()
    numero = 5
    risultato = fattoriale(numero)
    print(f"Il fattoriale di {numero} è {risultato}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Uscita dal programma! ")
