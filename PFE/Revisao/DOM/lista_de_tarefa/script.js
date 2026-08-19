const input = document.getElementById("Tarefa")
const botao = document.getElementById("btnAdicionar")
const lista = document.getElementById("lista")
const items  = document.querySelectorAll("#lista li")

items.forEach((items) => {
    item.addEventListener("click",()=>{
        item.remove();
    });
});

botao.addEventListener("click", ()=>{
    const texto = input.value;

    const li = document.createElement("li");

    li.innerText = texto;
    lista.appendChild(li)

    li.addEventListener("click", () => {
        li.remove();
    })

    input.value=""
})

