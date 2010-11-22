#include <stdio.h>

int main() {
  int i = 1;
  for (i=1;i<101;i++) {
    if (i%3 < 1 && i%5 < 1) {
      printf("fizzbuzz\n");
    } else if (i%3 < 1) {
      printf("fizz\n");
    } else if (i%5 < 1) {
      printf("buzz\n");
    } else {
      printf("i\n");
    }
  }
}
