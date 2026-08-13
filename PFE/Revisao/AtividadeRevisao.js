let precos = [10,20,30,40]


let precosComDesconto10 = precos.map(n=> n*.90)
let precosAcimaDe25 = precosComDesconto10.filter(n=> n>25)
let totalPrecosAcima25 = precosAcimaDe25.reduce((soma,total)=>soma+total,0)

console.log(precos)
console.log(precosComDesconto10)
console.log(precosAcimaDe25)
console.log(totalPrecosAcima25)