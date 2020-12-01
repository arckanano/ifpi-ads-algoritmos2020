#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n1, n2;

    printf("N1 | N2\n");
    scanf("%d%d",&n1,&n2);

    if (n1 > n2) {
        printf("%d maior que %d", n1, n2);
    } else {
        printf("%d maior que %d", n2, n1);
    }
    
    system("pause");
    return 0;

}