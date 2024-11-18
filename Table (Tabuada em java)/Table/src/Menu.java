import java.util.Scanner;

public class Menu {
    Table table = new Table();
    Scanner input = new Scanner(System.in);


    public Menu() {

    }


    public void showMenu() {
        int op = -1;
        while (op != 0) {
            System.out.println("Escolha uma opção de tabuada:");
            System.out.println("[1] Adição, [2] Subtração, [3] Divisão, [4] Multiplicação");
            op = Integer.parseInt(input.nextLine());// conversão de string para inteiro.

            switch (op) {

                case 1:
                    System.out.println("Escolha o numero até qual tabuada será mostrado, e até qual operador:");
                    int x = Integer.parseInt(input.nextLine());
                    int y = Integer.parseInt(input.nextLine());
                    table.showTableAdition(x, y);
                    break;
                case 2:
                    System.out.println("Escolha o numero até qual tabuada será mostrado, e até qual operador:");
                    int s = Integer.parseInt(input.nextLine());
                    int a = Integer.parseInt(input.nextLine());
                    table.showTableSubtration(s, a);
                    break;
                case 3:
                    System.out.println("Escolha o numero até qual tabuada será mostrado, e até qual operador:");
                    int c = Integer.parseInt(input.nextLine());
                    int z = Integer.parseInt(input.nextLine());
                    table.showTableDivision(c, z);
                    break;
                case 4:
                    System.out.println("Escolha o numero até qual tabuada será mostrado, e até qual operador:");
                    int n = Integer.parseInt(input.nextLine());
                    int m = Integer.parseInt(input.nextLine());
                    table.showTableMultplicate(n, m);
                    break;
            }


        }


    }

}