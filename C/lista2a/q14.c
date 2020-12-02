#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n1, n2, n3, n4, n5;
    float media;

    printf("Números: \n");
    scanf("%d%d%d%d%d", &n1,&n2,&n3,&n4,&n5);

    media = (n1 + n2 + n3 + n4 + n5) / 5;

    printf("MEDIA: %0.2f", media);

    // Números maiores que a media
    printf("\nNúmeros maiores que a média:\n");
    if ( n1 > media) {
        printf("\n%d", n1);
    }
    if ( n2 > media) {
        printf("\n%d", n2);
    }
    if ( n3 > media) {
        printf("\n%d", n3);
    }
    if ( n4 > media) {
        printf("\n%d", n4);
    }
    if ( n5 > media) {
        printf("\n%d", n5);
    }
    
    system("pause");
    return 0;

}