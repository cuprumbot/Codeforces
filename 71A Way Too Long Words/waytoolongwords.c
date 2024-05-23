#include <stdio.h>
#include <string.h>

int main () {
  int cant;
  char str[101];

  scanf("%d", &cant);
  getchar();            // consumir el \n después del número

  int i;
  for (i = 0; i < cant; i++) {
    scanf("%s", str);

    int len = strlen(str);
    if (len > 10) {
      printf("%c%d%c\n", str[0], len-2, str[len-1]);
    } else {
      printf("%s\n", str);
    }
  }

  return 0;
}