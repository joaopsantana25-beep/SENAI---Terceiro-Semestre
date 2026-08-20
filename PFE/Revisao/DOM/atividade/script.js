const botao = document.getElementById("cadastrarProduto")
const vitrine = document.getElementById("vitrine")

botao.addEventListener("click", ()=>{
    const nomeProduto = document.getElementById("nomeProduto")
    const precoProduto = document.getElementById("precoProduto")
    const p = document.createElement("p")


    if(!nomeProduto.value || !precoProduto.value){
        nomeProduto.value = ""
        precoProduto.value = ""  
        alert("Preencha todos os campos")  
        return
    }

    p.innerText=`Produto: ${nomeProduto.value} - R$ ${(Number(precoProduto.value)).toFixed(2)}`
    p.classList.add("card")

    vitrine.appendChild(p)

    nomeProduto.value = ""
    precoProduto.value = ""   
   
})