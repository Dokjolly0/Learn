#include "../namespace.h"
#include "../function.h"
#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath> // Per la funzione sqrt
#include <iomanip> // Per std::fixed e std::setprecision

using cmd::print;
using cmd::input;
using std::string;

int main() {
    std::string prompt;
    std::vector<double> numeri;
    double result = 0;
    std::string operazione;

    while (true) {
        std::cout << "Inserisci l'operazione da effettuare: ";
        std::getline(std::cin, prompt); // Ottiene l'input con anche gli spazi vuoti

        if (prompt.empty()) {
            if (!numeri.empty()) {
                result = numeri.back();
            }
            std::cout << "Risultato finale: " << std::fixed << std::setprecision(0) << result << std::endl;
            exit(0);
        }

        try {
            double number = std::stod(prompt);
            numeri.push_back(number);

            if (!operazione.empty() && numeri.size() >= 2) {
                double b = numeri.back(); numeri.pop_back();
                double a = numeri.back(); numeri.pop_back();

                if (operazione == "+") {
                    result = a + b;
                } else if (operazione == "-") {
                    result = a - b;
                } else if (operazione == "*") {
                    result = a * b;
                } else if (operazione == "/") {
                    if (b == 0) {
                        std::cerr << "Errore: divisione per zero.\n";
                        numeri.push_back(a);
                        numeri.push_back(b);
                        continue;
                    }
                    result = a / b;
                } else if (operazione == "**") {
                    b = static_cast<int>(b); // Converte b in intero
                    result = potenza(a, b);
                } else if (operazione == "//") {
                    if (a < 0) {
                        std::cerr << "Errore: radice quadrata di un numero negativo.\n";
                        numeri.push_back(a);
                        continue;
                    }
                    result = static_cast<int>(std::sqrt(a)); // Radice quadrata intera
                } else if (operazione == "sqrt") {
                    if (b < 0) {
                        std::cerr << "Errore: radice quadrata di un numero negativo.\n";
                        numeri.push_back(b);
                        continue;
                    }
                    result = std::sqrt(b);
                } else if (operazione == "log"){
                    result = std::log10(a);
                } else if (operazione == "log_base"){
                    result = log_base(a, b);
                }

                numeri.push_back(result);
                std::cout << std::fixed << std::setprecision(0) << result << std::endl;
                operazione.clear();
            }
        } catch (const std::invalid_argument& err) {
            if (prompt == "+" || prompt == "-" || prompt == "*" || prompt == "/" || prompt == "**" || prompt == "//" || prompt == "sqrt" || prompt == "log" || prompt == "log_base") {
                operazione = prompt;

                // Stampa immediatamente il risultato se l'operazione è "//"
                if (operazione == "//" && numeri.size() >= 1) {
                    double a = numeri.back(); numeri.pop_back();
                    if (a < 0) {
                        std::cerr << "Errore: radice quadrata di un numero negativo.\n";
                        numeri.push_back(a);
                        continue;
                    }
                    result = static_cast<int>(std::sqrt(a)); // Calcola la radice quadrata intera
                    numeri.push_back(result);
                    std::cout << std::fixed << std::setprecision(0) << result << std::endl;
                    operazione.clear();
                }
            } else {
                std::cerr << "Operazione non riconosciuta.\n";
            }
        }
    }

    return 0;
}
