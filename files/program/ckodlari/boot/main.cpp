#include <iostream>
#include <stdio.h>
using namespace std;


void ekrani_temizle() {

	__asm
	{

		mov al, 02h;
		mov ah, 00h;
		int 10h;
	}

}


int main() {
	cout << "Hello World";
}
