let pessoas = [
    {nome:"Joao",idade:25},
    {nome:"Carlos",idade:23}
]

let carrinhos = [0,1,2,3]

for (let carro of carrinhos){
    console.log(carro);
}
    
for (let pessoa of pessoas){
    console.log(pessoa.nome);
}

console.log(pessoas.find(p => p.idade<25));
