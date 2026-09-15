#include <iostream>

using namespace std;

int main() {
    	int x, y;

	cout << "Escriba un numero (x): ";
	cin >> x;

	cout << "Escriba otro numero (y): ";
	cin >> y;

	if (x < y) {
		cout << "x es menor que y" << endl;
	}
	else if (x > y) {
		cout << "x es mayor que y" << endl;
	}
	else {
		cout << "Los numeros son iguales" << endl;
	}
    return 0;
}