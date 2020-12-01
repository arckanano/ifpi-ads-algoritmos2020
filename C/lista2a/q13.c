#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n, maior=0, menor=0, i=0;

		do {
				printf("Numero: ");
				scanf("%d", &n);
				if (i == 0){
				maior = n;
				menor = n;
				}else if (n > maior) {
					maior = n;
				} else if (n < menor) {
					menor = n;
				}
				i++;
		}
			while(i<5);
			printf("Maior = %d\nMenor = %d", maior, menor);
    
    return 0;

}