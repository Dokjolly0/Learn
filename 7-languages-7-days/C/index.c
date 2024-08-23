#include <stdio.h>
#define PI = 3.141975

//Commento singola linea
/*Commento multi linea */

int main(){
    //Hello world
    printf("Hello world! \n");

    //Tipi di dato
    int n1 = 0;
    float n2 = 0;
    double n3 = 0;
    char c1 = 'a';
    char string1[] = "Questa è la mia stringa";

    //Strutture dati
    int array1[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; /*Dichiarazione e assegnazione*/
    int array2[10];
    array2[0] = 1; array2[1] = 2; array2[2] = 3; array2[3] = 4; array2[4] = 5; array2[5] = 6; array2[6] = 7; array2[7] = 8; array2[8] = 9; array2[9] = 10;

    if(sizeof(array1) >= 0) printf(sizeof(array1));

    return 0;
}
