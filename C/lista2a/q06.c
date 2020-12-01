#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int a,b,c, soma_dos_angulos;
    printf("N1, N2, N3\n");
    scanf("%d%d%d", &a,&b,&c);

    soma_dos_angulos = a + b + c;

    if (soma_dos_angulos == 180) {
        // acutangulo: 3 angulos < 90
        if ( (a < 90) && (b < 90) && (c < 90)) {
            printf("Acutangulo");
        }
        if ( (a == 90) || (b == 90) || (c == 90)) {
            printf("Retangulo.");
        }
        if ( (a > 90) || (b > 90) || (c > 90)) {
            printf("Obtusangulo");
        }
    } else {
        printf("Não é triangulo");
    }
    
    system("pause");
    return 0;

}