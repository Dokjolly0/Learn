'use strict';
const fs = require('fs');

console.log("Variabili");
var var1 = 0; // Var // Non block scope // Vareble
let numero = 0// Let // Block scope // variable
const PI = 3.14197; // Const //Block scope // Immutable

function reverse (string){
    if(typeof string === "string"){
        let newString = "";
        const len = string.length - 1;
        for(let i = len; i >= 0; i--){            
            newString += string[i];
        }
        return newString;
    } else{
        console.log("La funzione funziona solo con le stringhe! ");
    }
}

reverse(10);
console.log(reverse("0123456789"));
console.clear();

function arr_count (arr){
    if(typeof arr === "object"){
        let sum = 0;
        for(let i = 0; i < arr.length; i++){
            if(typeof arr[i] === "number") sum += arr[i];
        }
        return sum;
    } else {
        console.log("La funzione funziona solo con gli array! ");
    }
}

let arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let arrFake = "Fake";
arr_count(arrFake);
console.log(arr_count(arr1));

let libro = {
    autore: "Alex",
    pagine: 69,
    titolo: "Il mio libro",
    copertina: "source",
    print_info(){
        for(let prop in libro){
            if (prop === "print_info") continue;
            console.log(prop);
        }   
    }
}

libro.print_info();
console.clear();

//Scrittura su json
//Crea un oggetto
const oggetto_da_convertire = {
    autore: "Alex",
    pagine: 69,
    titolo: "Il mio libro",
    copertina: "source",
    casa_editrice: "Alex corporation! ",
}
//Convertilo in json
let json_file = JSON.stringify(oggetto_da_convertire, null, 2);
//Scegli la path
let path = "/home/Dokjolly/Desktop/Alex/Learn/Js/libro.josn";
//Salva il file
fs.writeFile(path, json_file, err => {
    if(err) console.log("Errore: " + err);
    else console.log("Json creato in " + path + "!");
})