#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void)
{

    setlocale(LC_ALL, "");

    float nota1, nota2, media, exame, mediaFinal;

    printf("Nota 1: ");
    scanf("%f", &nota1);

    printf("Nota 2: ");
    scanf("%f", &nota2);

    media = (nota1 + nota2) / 2;

    // Verificação
    if (media >= 7) {
        printf("MEDIA: %0.2f\n", media);
        printf("Aprovado");
    } else {
        if (media < 7) {
            printf("Recuperação: ");
            scanf("%f", &exame);
            mediaFinal = (media + exame) / 2;
            if (mediaFinal >= 5) {
                printf("%0.2f\n", mediaFinal);
                printf("Aprovado");
            } else {
                printf("%0.2f\n", mediaFinal);
                printf("Reprovado");
            }
        }
    }
    

    system("pause");
    return 0;
}