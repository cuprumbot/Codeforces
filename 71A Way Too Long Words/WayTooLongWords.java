import java.util.Scanner;

public class WayTooLongWords {
  public static void main (String[] args) {
    Scanner scanner = new Scanner(System.in);

    int cant = scanner.nextInt();

    for (int i = 0; i < cant; i++) {
      String str = scanner.next();

      int len = str.length();
      if (len > 10) {
        System.out.println( "" + str.charAt(0) + (str.length()-2) + str.charAt(len-1) );
      } else {
        System.out.println( str );
      }
    }
  }
}