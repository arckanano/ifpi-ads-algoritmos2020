#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int valorKm, valorM;

    printf("Valor em KM = ");
    scanf("%d", &valorKm);

    valorM = valorKm * 1000;

    printf("%d KM = %d M", valorKm, valorM);
    
    system("pasue");
    return 0;

}