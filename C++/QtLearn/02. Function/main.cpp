#include <QCoreApplication>
#include <QDebug>
#include <iostream>
#include "QObject.h"

//Le funzioni hanno 2 metodi di passare i valori:
void byVal(int a){ //Per valore --> Crei una copia di quel valore
    a = a * 10;
    std::cout << a << std::endl;
}
void byRef(int &b){ //Per referenza --> Usi il valore attuale dell'oggetto
    b = b * 10;
    std::cout << b  << std::endl;
}

QObject *get_qt_obj(QString name){
    QObject *obj = new QObject();
    obj->setObjectName(name);
    return obj; //Sara eliminato //main.cpp:18:12: error: call to deleted constructor of 'QObject'
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    int aa = 10; //In pratica in byVal si crea una copia identica di aa, quindi se poi vai a riguardare quel valore rimane sempre uguale
    int bb = 10; //In pratica in byRef si usa il valore esatto di bb in quel momento, quindi se poi riguardi il valore cambia in base ai calcoli in cui lo hai usato
    byVal(aa); //100
    byVal(aa); //100
    byRef(bb); //100
    byRef(bb); //1000
    std::cout << "Valore di a: " << aa /*10*/ << std::endl << "Valore di b: " << bb /*1000*/  << std::endl;

    struct aereo{
        double peso;
        double pesoInLibre(){return peso * 2.20462;}
    };
    aereo boeing747;
    boeing747.peso = 1270;
    qInfo() << "Peso in kiloogrammi: " << boeing747.peso;
    qInfo() << "Peso in libre: " << boeing747.pesoInLibre();

    int aaa = 20;
    int *value_ptr = &aaa; // Al puntatore bisogna assegnare l'indirizzo della variabile a cui dovrà puntare. | & -> indirizzo
    int val_ptr = *&aaa; // *&aaa è equivalente a aaa, poiché &aaa restituisce l'indirizzo di aaa e * dereferenzia quell'indirizzo per ottenere il valore.
    std::cout << "Valore di aaa: " << val_ptr << std::endl << "Indirizzo di memoria: " << value_ptr << std::endl;

    QObject *obj1 = get_qt_obj("Oggetto 1");
    qInfo() << "QObject name: " << obj1 -> objectName();
    delete obj1;

    return a.exec();
}







