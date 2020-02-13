#include "pch.h"
#include <iostream>
#include <string>
using namespace std;
int reg = 0;
string ciudad;
void menu();

void Partido() {

}

void Voto() {

}



void Recuento() {
}



struct Registro
{
	string city[20];
	string partido[20];
	int votos[20];

}registro;

void Ciudad() {
	reg++;
	cout << "Dame la ciudad de los votos" << endl;
	getline(cin, ciudad);
	for (int i = 0; i < reg; i++)
	{
		if (ciudad == registro.city[i]) {
			cout << "La ciudad ya existe no se agregara" << endl;
		}
		else if (ciudad != registro.city[i])
		{
			registro.city[i] = ciudad;
		}
	}

}

void Alta() {
	int opcion = 0;
	do
	{
		cout << "1. Registrar ciudad" << endl;
		cout << "2. Registrar partido" << endl;
		cout << "3. Registrar voto" << endl;
		cout << "4. Regresar al menu principal" << endl;
		cin >> opcion;
		switch (opcion)
		{
		case 1:
			Ciudad();
			Alta();
			break;
		case 2:
			Partido();
			Alta();
			break;
		case 3:
			Voto();
			Alta();
			break;
		case 4:
			menu();
			break;
		default:
			cout << "Opcion incorrecta" << endl;
			break;
		}
	} while (true);
}

void menu() {
	int opcion = 0;
	do
	{
		cout << "1. Dar de alta votos " << endl;
		cout << "2. Realizar recuento de votos " << endl;
		cout << "3. Salir " << endl;
		cin >> opcion;
		switch (opcion)
		{
		case 1:
			Alta();
			menu();
			break;
		case 2:
			Recuento();
			menu();
			break;
		case 3:
			cout << "Adios " << endl;
			break;
		default:
			cout << "Opcion incorrecta" << endl;
			Alta();
			menu();
			break;
		}

	} while (opcion != 3);
}

int main()
{
	menu();
}