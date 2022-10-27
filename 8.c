#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main() {
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    for (int i = a; i <= b; i++) {
        bool primo = true;
        if (i < 2) {
            primo = false;
        } else {
            for (int j = 2; j < i && primo; j++) {
                if (i%j == 0 && i != j) {
                    primo = false;
                }
            }
            if (primo == true) {
                if (i > 9) {
                    int numDigits = 0;
                    while (i / (int) pow(10, numDigits) >= 1) {
                        numDigits++;
                    }
                    int sum = 0;
                    for (int k = 0; k <= numDigits; k++) {
                        int paso = i / (int) pow(10, k);
                        int resta = 0;
                        if (paso > 9) {
                            resta = i / (int) pow(10, k + 1);
                        }
                        int result = paso - resta * 10;
                        sum += result;
                    }
                    if (sum < 2) {
                        primo = false;
                    } else {
                        for (int l = 2; l < sum; l++) {
                            if (sum%l == 0 && sum != l) {
                                primo = false;
                            }
                        }
                    }
                    if (primo == true) {
                        printf("%d\n", i);
                    }
                } else {
                    printf("%d\n", i);
                }
            }
        }
    }
    return 0;
}