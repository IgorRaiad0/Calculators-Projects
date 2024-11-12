package App;

import objetos.Equacao2Grau;

public class main {
    public static void main(String[] args) {

        Equacao2Grau eq = new Equacao2Grau(4,0,-16); // CRIANDO UM OBJETO E USANDO O CONSTRUTOR

        System.out.println("O delta é" + eq.Showcalcdelta());
        System.out.println("As raizes são xi, xii: " + eq.Showcalcbaskara());




    }
}
