package biblioteca;
import biblioteca.Usuario;
import biblioteca.Livro;

public class Emprestimo {

    //Metodos
    public void realizarEmprestimo(Usuario usuario, Livro livro){
        if (livro.emprestar()){
            System.out.println("Empréstimo realizado com sucesso");
            System.out.println("Usuário: "+ usuario.getNome());
            System.out.println("Livro: "+ livro.getTitulo());
        }
        else{
            System.out.println("Livro indisponível");
        }
    }

}
