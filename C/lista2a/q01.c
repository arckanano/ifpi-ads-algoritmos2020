#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n1, n2, n3;

		printf("n1:");
		scanf("%d", &n1);

		printf("n2:");
		scanf("%d", &n2);

		printf("n3:");
		scanf("%d", &n3);

		if ((n1==n2)&&(n1==n3)) {
			printf("São 3 iguais");
		} else if ((n1==n2)||(n1==n3)||(n2==n3)) {
			printf("São 2 iguais");
		} else {
			printf("Nenhum igual");
		}

    return 0;

}