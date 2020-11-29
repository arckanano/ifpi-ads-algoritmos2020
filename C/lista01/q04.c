#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n1, n2;
    float quociente, resto;

    printf("n1 | n2\n");
    scanf("%d%d",&n1, &n2);

    resto = n1 % n2;
    quociente = n1 / n2;

    printf("Resto: %0.2f\nQuociente: %0.2f", resto, quociente);
    
    system("pause");
    return 0;

}