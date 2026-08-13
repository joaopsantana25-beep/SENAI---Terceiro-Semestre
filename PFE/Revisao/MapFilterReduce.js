/*
Map - Transformar dados
Filter - Filtrar dados
Reduce - resumir/calcular dados
*/

let numeros = [1,2,3,4]

let dobrados = numeros.map(n => n*2)
let maioresQue2 = numeros.filter(n => n>2)
let total = numeros.reduce((soma,valor) =>soma + valor,0)


console.log(numeros)
console.log(dobrados)
console.log(maioresQue2)
console.log(total)