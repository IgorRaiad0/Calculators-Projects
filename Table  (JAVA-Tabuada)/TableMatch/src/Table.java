public class Table {
    //Attribute
    int number = 0;
    int operation = 0;

    //CONSTRUTOR
    public Table() {
        this.number = number;
        this.operation = operation;
    }

    // Métodos mostrar calculadora

    public int showTableMultplicate(int number, int operation) {

        System.out.println("Será mostrado até a tabuada do: " + number + " do 1 até o: " + operation);

        int mul = 0;

        for (int i = 1; i <= number ; i++) {

            for (int j = 1; j <= operation; j++) {
                mul = i * j;

                System.out.println(i + "x" + j + "=" + mul);

            }
            System.out.println("======================");
        }
        return mul;
    }

    public int showTableAdition(int number, int operation) {

        System.out.println("Será mostrado até a tabuada do: " + number + " do 1 até o: " + operation);

        int ad = 0;

        for (int i = 1; i <= number ; i++) {

            for (int j = 1; j <= operation; j++) {
                ad = i + j;

                System.out.println(i + "+" + j + "=" + ad);
            }
            System.out.println("======================");
        }
        return ad;
    }

    public int showTableSubtration(int number, int operation) {

        System.out.println("Será mostrado até a tabuada do: " + number + " do 1 até o: " + operation);

        int sub = 0;

        for (int i = 1; i <= number ; i++) {

            for (int j = 1; j <= operation; j++) {
                sub = i - j;

                System.out.println(i + "-" + j + "=" + sub);
            }
            System.out.println("======================");
        }
        return sub;
    }

    public int showTableDivision(int number, int operation) {

        System.out.println("Será mostrado até a tabuada do: " + number + " com operações de 1 até: " + operation);

        int div = 0;

        for (int i = 1; i <= number ; i++) {

            for (int j = 1; j <= operation; j++) {
                div = i / j;


                System.out.println(i + "/" + j + "=" + div);
            }
            System.out.println("======================");
        }
        return div;
    }
}
