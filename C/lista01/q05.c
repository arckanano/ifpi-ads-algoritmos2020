#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");

    int n, centena, dezena, unidade;
    
    printf("Número: ");
    scanf("%i", &n);

    // Centenas
    centena = n / 100;
    // Dezena
    dezena = (n % 100) / 10;
    //Unidade
    unidade = (n % 100) % 10;;

    // Saída
    printf("%i%i%i", unidade, dezena, centena);
    
    system("pause");
    return 0;

}