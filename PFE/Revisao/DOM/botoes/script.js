const text = document.getElementById("text")
const btn = document.getElementById("btn")

btn.addEventListener("click", ()=>{
    text.textContent = "Titulo alterado com JS"

})

////////////////////////////////////////////////////////////
const text_style = document.querySelector("#text-style")
const btn_style = document.querySelector("#btn-style")

btn_style.addEventListener("click", ()=>{
    text_style.style.color = "blue";
    text_style.style.fontSize = "32px"
})