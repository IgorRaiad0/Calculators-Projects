package objetos;

public class Equacao2Grau {
    // Atributos
    int a;
    int b;
    int c;

    // Criando um construtor
    public Equacao2Grau(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    // Método para calcular o delta
    public double Showcalcdelta() {
        var d = (b * b) - (4 * a * c);
        return d;
    }

    // Método para mostrar as raízes usando Bhaskara
    public String Showcalcbaskara() {
        double delta = Showcalcdelta();
        if (delta > 0) {
            double xi = (-b + Math.sqrt(delta)) / (2 * a);// match.sqrt() usado para definir raiz quadrada de um úneros entre parenteses
            double xii = (-b - Math.sqrt(delta)) / (2 * a);
            return "Raiz 1: " + xi + ", Raiz 2: " + xii;
        } else if (delta == 0) {
            double xi = -b / (2 * a);
            double xii = xi;
            return "Raiz 1: " + xi + "Raiz 2" + xii;
        } else {
            return "Não existem raízes reais. Delta menor que zero";
        }
    }
}
