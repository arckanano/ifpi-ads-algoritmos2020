#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n1, n2, n3;

    printf("N1 | N2 | N3\n");
    scanf("%d%d%d", &n1,&n2,&n3);

    if ( (n1 > n2) && ( n1 > n3)) {
        // n1 e maior
        printf("%d é Hipotenusa e os outros são cetetos.", n1);
    } else if ( (n2 > n1) && (n2 > n3)) {
        // n2 é maior
        printf("%d é Hipotenusa e os outros são cetetos.", n2);
    } else {
        //n3 é maior
        printf("%d é Hipotenusa e os outros são cetetos.", n3);
    }
    
    system("pause");
    return 0;

}