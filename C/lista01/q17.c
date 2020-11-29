#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int valorKg, valorG;

    printf("Valor em KM = ");
    scanf("%d", &valorKg);

    valorG = valorKg * 1000;

    printf("%d Kilos = %d gramas", valorKg, valorG);
    
    system("pasue");
    return 0;

}