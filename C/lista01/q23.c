#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n1, n2, n3;
    float media;

    printf("Digite 3 números: ");
    scanf("%d%d%d", &n1,&n2,&n3);

    media = (n1 + n2 + n3) / 3;

    printf("Medoa = %0.2f", media);
    
    system("pause");
    return 0;

}