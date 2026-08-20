const produto = document.getElementById("nomeProduto")
const preco = document.getElementById("precoProduto")
const botaoAdicionar = document.getElementById("Adicionar")
const catalogo = document.getElementById("catalogo")

botaoAdicionar.addEventListener("click",()=>{
    const nomeProduto = produto.value
    const precoProduto = preco.value

    if (nomeProduto && precoProduto){
        catalogo.appendChild(nomeProduto);     
    }
})