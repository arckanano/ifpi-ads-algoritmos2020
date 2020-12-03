#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int senha, senhaValida=1234;

    printf("SENHA: ");
    scanf("%d", &senha);

    if (senha == senhaValida) {
        printf("Acesso permitido");
    } else {
        printf("Acesso Negado.");
    }
    
    system("pause");
    return 0;

}