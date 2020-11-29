#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float n1, n2, n3, mediaPonderada;
    int p1, p2, p3;

    printf("Notas:");
    scanf("%f %f %f", &n1, &n2, &n3);

    printf("Peso de cada nota: ");
    scanf("%d %d %d", &p1,&p2,&p3);

    mediaPonderada = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3);
    
    printf("Media Ponderada = %0.2f", mediaPonderada);

    system("pause");
    return 0;

}