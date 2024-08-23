#include <QCoreApplication>
#include <QDebug>
#include <array>
#include <iostream>
using namespace std;

void data_type(){
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
}
