package biblioteca;

public class Livro{
    private String titulo;
    private String autor;
    private boolean disponivel;

    //Construtores
    public Livro(String titulo, String autor){
        this.titulo = titulo;
        this.autor = autor;
        this.disponivel = true;
    }

    //Metodos
    public boolean emprestar(){
        if (this.disponivel){
            this.disponivel = false;
            return true;
        }
        return false;
    }

    public void devolver(){
        this.disponivel = true;
    }

    //Setters
    public void setTitulo(String titulo){
        this.titulo = titulo;
    }

    public void setAutor(String autor){
        this.autor = autor;
    }

    //Getters
    public String getTitulo(){
        return titulo;
    }

    public String getAutor(){
        return autor;
    }
}
