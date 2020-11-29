#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int lado, area;

    printf("Lado: \n");
    scanf("%d", &lado);

    area = lado * lado;

    printf("%d", area);
    
    system("pause");
    return 0;

}