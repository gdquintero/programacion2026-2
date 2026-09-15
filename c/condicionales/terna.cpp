#include <iostream>

using namespace std;

int main() {
    int a, b, c;
	bool cond1, cond2, cond3;

	cout << "Escriba a: ";
	cin >> a;

	cout << "Escriba b: ";
	cin >> b;

	cout << "Escriba c: ";
	cin >> c;

	cond1 = pow(a, 2) + pow(b, 2) == pow(c, 2);
	cond2 = pow(a, 2) + pow(c, 2) == pow(b, 2);
	cond3 = pow(b, 2) + pow(c, 2) == pow(a, 2);

	if (cond1 || cond2 || cond3) {
		cout << "Los numeros forman una terna pitagorica" << endl;
	}
	else {
		cout << "Los numeros NO forman una terna pitagorica" << endl;
	}
    return 0;
}