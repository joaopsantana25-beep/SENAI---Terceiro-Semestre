package biblioteca;

public class Usuario {
    private String nome;
    private String prontuario;

    //Construtores
    public Usuario(String nome, String prontuario){
        this.nome = nome;
        this.prontuario = prontuario;
    }

    //Metodos
    public void exibirDados(){
        System.out.println("Nome: " + nome);
        System.out.println("Prontuario: " + prontuario);
    }

    //Setters
    public void setNome(String nome){
        this.nome = nome;
    }

    public void setProntuario(String nome){
        this.prontuario = prontuario;
    }

    //Getters
    public String getNome(){
        return nome;
    }

    public String getProntuario(){
        return prontuario;
    }
}
