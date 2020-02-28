#include <stdio.h>
int main()
{
	char x;
	int y;
	double z;
	printf("Bir karakter giriniz : ");
	scanf("%c",&x);

	printf("\nBir tamsayısı giriniz : ");
	scanf("%d",&y);

	printf("\nBir ondalıklı sayı giriniz : ");
	scanf("%lf",&z);

	printf("girilen x karakteri %c y tamsayısı %d z ondalıklı sayısı %lf",x,y,z);
	return 0; 
}
