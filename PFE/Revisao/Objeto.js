let aluno = {
    nome:"Carlos",
    idade: 25 ,
    prontuario: "1234",
    notas:{
        pfe: 80,
        ppdm: 90,
        psof: 100
    },

    perguntar: function(mensagem){
        console.log(mensagem)
    }

}


//destructor de objetos
//const {nome, idade, prontuario} = aluno;


console.log(aluno.notas.ppdm)
aluno.perguntar("Que dia é hoje?");
