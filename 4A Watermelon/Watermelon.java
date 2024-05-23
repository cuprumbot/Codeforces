import java.util.Scanner;

public class Watermelon {
  public static void main (String[] args) {
    Scanner scanner = new Scanner(System.in);
    int num = scanner.nextInt();

    if (num == 2 || num % 2 != 0) {
      System.out.println("NO");
    } else {
      System.out.println("YES");
    }
  }
}