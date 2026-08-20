const produtos = ["Mouse", "Teclado", "Processador", "Monitor"];
const botao = document.getElementById("btnCarregar");
const lista = document.getElementById("produtos");
const carregar = document.getElementById("carregamento");


botao.addEventListener("click",()=>{
    lista.innerHTML = ""
    carregar.innerHTML="Carregando...";
    document.body.style.cursor = "wait";
    botao.style.cursor = document.body.style.cursor

    botao.disabled = true ;

    setTimeout(()=>{
        carregar.innerHTML = ""
        document.body.style.cursor = "default";
        botao.style.cursor = "pointer"
        lista.style.cursor = document.body.style.cursor
        botao.disabled = false;

        produtos.forEach(produto => {
        const li = document.createElement("li");
        li.innerText = produto;
        lista.appendChild(li);
    })},
    3000);
       
})
