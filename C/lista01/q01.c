#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char const *argv[])
{
    float velMS, velKM;

    printf("Velocidade me m/s: ");
    scanf("%f", &velMS);

    velKM = velMS * 3.6;

    printf("%0.2f m/s em km/h: %0.2f", velMS, velKM);
    
    system("PAUSE");
    return 0;
}
