#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int prof1hora, prof2hora, prof1valorHora, prof2valorHora, prof1salario, prof2salario;

    printf("Horas-aula dadas pelo professor 1: ");
    scanf("%d", &prof1hora);
    printf("Valor da hora professor 1: ");
    scanf("%d", &prof1valorHora);

    printf("Horas-aula dadas pelo professor 2: ");
    scanf("%d", &prof2hora);
    printf("Valor da hora professor 2: ");
    scanf("%d", &prof2valorHora);

    prof1salario = prof1hora * prof1valorHora;
    prof2salario = prof2hora * prof2valorHora;

    // Verificar quem tem maior salário
    if ( prof1salario == prof2salario) {
        printf("Recebem o mesmo salário\nProfessor 1: %d\nProfessor 2: %d", prof1salario, prof2salario);
    } else if (prof1salario > prof2salario) {
        printf("O professor 1 recebe mais: R$%d,00", prof1salario);
    } else {
        printf("O professor 2 recebe mais: R$%d,00", prof2salario);
    }
    
    system("pause");
    return 0;

}