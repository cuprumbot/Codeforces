#include <stdio.h>

int main () {
  int num;
  scanf("%d", &num);
  
  if (num == 2 || num % 2) {
    printf("NO\n");
  } else {
    printf("YES\n");
  }

  return 0;
}