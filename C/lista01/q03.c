#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    float velKM, velMS;

    printf("Velocidade em Km/h: ");
    scanf("%f", &velKM);

    velMS = velKM / 3.6;

    printf("Resultado: %0.2f ms/s\n", velMS);

    system("pause");
    return 0;

}