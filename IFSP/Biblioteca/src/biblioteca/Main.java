import biblioteca.Emprestimo;
import biblioteca.Livro;
import biblioteca.Usuario;


public static void main(String[] args) {
    Livro livro1 = new Livro("Pequeno Princípe", "Antoine de Saint-Exupéry");
    Usuario usuario1 = new Usuario("João Paulo", "SP3299999");
    Emprestimo emprestimo = new Emprestimo();


    emprestimo.realizarEmprestimo(usuario1,livro1);
}
