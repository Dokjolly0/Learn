#include <QCoreApplication>
#include <QDebug>
#include <array>
#include <iostream>
#include "function.h"

using namespace std;

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    qInfo() << "Questa è una stampa!";

    qInfo() << "Enum";
    enum Color {red, green = 10, blue}; //Index 0 based //Se lo assegni ha quel valore
    Color colore = Color::red; //0
    //Color colore = Color::green; //10
    //Color colore = Color::blue; //2
    qInfo() << colore;

    qInfo() << "Struct";
    struct Fruits {
        int apples = 0;
        int bananas = 0;
        int mangos = 0;
    };
    Fruits fruits; //Dichiari un nuovo oggetto Fruits che avra le proprieta di Fruits
    qInfo() << fruits.apples;

    qInfo() << "Array";
    //int numbers[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; //1 metodo
    array<int, 10> numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; //2 metodo
    //for(int number:numbers){qInfo() << number;}
    for(int number:numbers){cout << number << " ";}
    cout << "\nHello" << endl;

    int value1 = {0};
    cout << "Inserisci un numero intero: ";
    //cin >> value1;
    qInfo() << value1;

    //int age = {0};
    //if (age == 0){qFatal("Non è un eta valida!");}

    //Ternary
    int numero = 5;
    bool check = (numero == 5? true: false);
    qInfo() << check;

    //Switch
    //std::cout << "Trova il mio numero fortunato: ";
    //std::cin >> numero;
    switch(numero){ // No stringhe in c++
        case 0: qInfo() << "Non hai scelto il mio numero, il numero è piu alto"; break;
        case 1: qInfo() << "Non hai scelto il mio numero, il numero è piu alto"; break;
        case 2: qInfo() << "Hai indovinato il mio numero!"; break;
        case 3: qInfo() << "Non hai scelto il mio numero, il numero è piu basso"; break;
        case 4: qInfo() << "Non hai scelto il mio numero, il numero è piu basso"; break;
        case 5: qInfo() << "Non hai scelto il mio numero, il numero è piu basso"; break;
        default: qInfo() << "Il mio numero è compreso tra 0 e 5"; break;
    }

    int eta = {1};
    qInfo() << "Verifica eta.";
    //std::cout << "Inserisci l'eta: ";
    //std::cin >> eta;
    eta > 0 && eta <= 120 ? qInfo() << "Hai un eta valida! ": qInfo() << "Non hai un eta valida";

    print();
    area_rettangolo(100, 12);

    return a.exec();
}


















