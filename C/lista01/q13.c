#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <math.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float raio, pi=3.14, volume;

    printf("Raio = ");
    scanf("%f", &raio);

    volume = (4 * pi * (pow(raio,3)));

    printf("Volume = %0.2f", volume);
    
    system("pause");
    return 0;

}