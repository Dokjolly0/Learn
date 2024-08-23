#ifndef FUNCTION_H
#define FUNCTION_H
#include <iostream>

void print(){
    std::cout << "Hai usato la funzione print! \n";
}
void area_rettangolo(float base, float altezza){
    std::cout << "L'area del rettangolo è di " << base * altezza << "metri quadrati\n";
}

#endif // FUNCTION_H
