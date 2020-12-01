#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int atualDias, atualMes, atualAno, nascDia, nascMes, nascAno, idade;

    printf("---Data atual---\n");
    printf("Dia | Mes | Ano\n");
    scanf("%d%d%d", &atualDias,&atualMes,&atualAno);

    printf("-Data Nascimento-\n");
    scanf("%d%d%d", &nascDia, &nascMes, &nascAno);

    idade = atualAno - nascAno;

    if ((atualMes < nascMes)) {
        idade -= 1;
        printf("Idade: %d", idade);
    } else if ((atualMes == nascMes) && (atualDias < nascDia)) {
        idade -= 1;
        printf("Idade: %d", idade);
    } else {
        printf("Idade: %d", idade);
    }

    
    system("pause");
    return 0;

}