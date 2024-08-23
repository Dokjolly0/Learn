print("Benvenuto nel calcolatore shell! ")
    
def is_number(number):
    try:
        int(number)
        return number
    except ValueError:
        float(number)
        return number
    except:
        return false
def check_operator(operator):
        if operator == '+':
            return operator
        elif operator == '-':
            return operator
        elif operator == '*':
            return operator
        elif operator == '/':
            return operator
        else:
            return False

def calc(n1, operator, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        print("Numeri non validi! ")
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '*':
        return n1 * n2
    elif operator == '/':
        if float(n2) == 0:
            print("Impossibile dividere un numero per 0")
            return False
        #print(f"N1: {n1}, N2: {n2}")
        return n1 / n2

def print_result(result):
    print(f"Il risultato del calcolo è: {str(result)}")

def ask_number():
    number1 = input("Inserisci un numero: ")
    try:
        condition = number1.isdigit()
    except ValueError:
        condition = False
    except:
        condition = False
    
    while condition == False:
        number1 = input(f"Numero non valido, inserisci un numero valido: ")
        condition = is_number(number1)
    return number1

def ask_operator(condition = False):
    operator = input("Inserisci l'operatore: ")
    if len(operator) == 1:
        condition = check_operator(operator)
    while condition == False:
        operator = input("Inserisci un operatore valido: ")
        condition = check_operator(operator)
    return operator

def main():
        actual_result = 0
        numero1 = is_number(ask_number())
        #print(numero1)
        operatore = ask_operator()
        #print(operatore)
        numero2 = is_number(ask_number())
        #print(numero2)
        
        if calc(numero1, operatore, numero2) == False:
            return
        result = calc(numero1, operatore, numero2)
        #print(f"Result: {str(result)}")
        actual_result += result
        print_result(actual_result)
        
        continua = input("Scegli una delle seguenti opzioni: (continua calcolo -> c), (nuovo calcolo -> n), (esci -> qualsiasi altro tasto): ").lower()
        while True:
            if continua == 'c':
                #print(f"Numero1: {str(actual_result)}")
                operatore = ask_operator()
                #print(f"Operatore: {str(operatore)}")
                numero2 = is_number(ask_number())
                #print(f"Numero2: {str(numero2)}")
                if calc(actual_result, operatore, numero2) == False:
                    return
                actual_result = calc(actual_result, operatore, numero2)
                #print(f"Result: {str(result)}")
                print_result(actual_result)
                continua = input("Scegli una delle seguenti opzioni: (continua calcolo -> c), (nuovo calcolo -> n), (esci -> qualsiasi altro tasto): ").lower()
                if continua == 'c':
                    continue
                elif continua == 'n':
                    main()
                else:
                    exit()
            elif continua == 'n':
                main()
            else:
                exit()

try:
    if __name__ == '__main__':
        main()
except KeyboardInterrupt:
    print("\nUscita dal calcolatore! ")








































































def title_case(title = ""):
    i = 0
    new_title = ''
    for char in title:
        if i == 0:
            char = char.upper()
        else: 
            char = char.lower()
        new_title += char
        i += 1
    return new_title

#print(title_case("AlEx ViOlattO"))

# print("Benvenuto nel calcolatore shell! ")
# total = 0
# def print_result(total):
#     print("Il risultato è: " + str(total))

# def calc(total = 0, number = 2):
#     n1 = 0
#     operator = ''
#     n2 = 0
#     result = 0

#     if number == 2:
#         n1 = float(input("Inserisci un numero: "))
#         operator = str(input("inserisci l'operatore: "))
#         while operator != '+' and operator != '-' and operator != '*' and operator != '/':
#             operator = input("inserisci un operatore valido: ")
#         n2 = float(input("Inserisci il secondo numero: "))
#     elif number == 1:
#         operator = str(input("inserisci l'operatore: "))
#         while operator != '+' and operator != '-' and operator != '*' and operator != '/':
#             operator = input("inserisci un operatore valido: ")
#         n1 = float(input("Inserisci un numero: "))

#     if operator == '+':
#         if number == 1:
#             result = total + n1
#             total = result
#             print_result(total)
#         else:
#             result = n1 + n2
#             total += result
#             print_result(total)
#     elif operator == '-':
#         if number == 1:
#             result = total - n1
#             total = result
#             print_result(total)
#         else:
#             result = n1 - n2
#             total += result
#             print_result(total)
#     elif operator == '*':
#         if number == 1:
#             result = total * n1
#             total = result
#             print_result(total)
#         else:
#             result = n1 * n2
#             total += result
#             print_result(total)
#     elif operator == '/':
#         if n2 == 0:
#             print("Impossibile dividere un numero per 0")
#             return 0
#         if number == 1:
#             result = total / n1
#             total = result
#             print_result(total)
#         else:
#             result = n1 / n2
#             total += result
#             print_result(total)
#     else:
#         print("Operatore non valido")
    
#     recalc = input("Vuoi continuare il calcolo (c), vuoi fare un nuovo calcolo (n) o uscire (qualsiasi altro tasto)").lower()
#     if recalc == 'c':
#         calc(total, 1)
#     elif recalc == 'n':
#         calc()
#     else:
#         return 0





# try:
#     calc()
# except KeyboardInterrupt:
#     print("\nUscita dal calcolatore. ")