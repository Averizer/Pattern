#include <bitset>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cmath>
#include <unistd.h>
#include <algorithm>

using namespace std;

int cma = 0;

//Clase para coordenadas
class Patron{
    private:
        vector<int> caracteristicas;
        vector<int> c;
        string nom;
    public:
        Patron(vector<int>,vector<int>,string);
        vector<int> obtenercaracteristicas();
        vector<int> obtenerclase();
        string obtenernombre();
        void cambiarValores(vector<int>);
};

Patron::Patron(vector<int>car,vector<int>cla,string n){
    caracteristicas = car;
    c = cla;
    nom = n;
}

vector<int> Patron::obtenercaracteristicas(){
    return caracteristicas;
}

vector<int> Patron::obtenerclase(){
    return c;
}

string Patron::obtenernombre()
{
    return nom;
}

void Patron::cambiarValores(vector<int>car){
    caracteristicas = car;
}

//Funciones
vector<Patron> LectorVectores();
vector<Patron> LectorPalabras();
void imprime(vector< vector<Patron> > a);
void CalculoMaximo(vector< vector<Patron> > a);
void imprimeMaxMin();
void recuperaMaxMin(vector< vector<Patron> > a);
void recuperaPalabra(vector< vector<Patron> > a);
void recuperaMaxRuido(vector< vector<Patron> > a);
//
//Variables
vector <int> maximo;
vector <int> minimo;
vector <int> sum_max;
vector <int> z;
int cont = 0;
int elem = 0;
int clas = 0;
int flag = 0;
double alfa;
double error;
//
//Funcion principal 
int main()
{
    system("clear");
    cout << "\t\tMemoria Asociativa Alpha Beta\n\n";

    int t = 0;
    while(t != 3)
    {
        // cout << "\t\t1- Clasificador de palabras.(Ejemplo complejo)\n";
        cout << "\t\t1.- Clasificador de bits. (Ejemplo sencillo)\n";
        cout << "\t\t2.- Salir.\n";
        cout << "Elija una opcion: ";
        cin >> t;
        
        if(t == 5)
        {
            flag = 0;
            cout << "Cuantas palabras desea:";
            cin >> clas;
            
            vector< vector <Patron> > v;
                
            for(int q = 0; q < clas; q++)
            {  
                vector<Patron> aux = LectorPalabras();
                v.push_back(aux);

                cont++;
            }
            for(int i = 0; i < clas*elem; i++)
                maximo.push_back(0);
            for(int i = 0; i < clas*elem;i++)
                minimo.push_back(100);
            system("clear");

            int opc=10;

            CalculoMaximo(v);

            while(opc!=0)
            {
                cout << "1- Volver a ingresar datos\n";
                cout << "2- Imprimir matriz maxima\n";
                cout << "3- Recuperar datos de matriz maxima\n";
                cout << "0- Salir\n";
                cout << "Elija una opcion: ";
                cin >> opc;
                if(opc == 1)
                {
                    system("clear");
                    cout << "\t\tMemoria Asociativa Alpha Beta\n\n";
                    cout << "\t\tCon codificacion OneHot\n\n";
                    cout << "Cuantas palabras desea:";
                    cin >> clas;
                    cont = 0;
                    for(int q = 0; q < clas; q++)
                    {  
                        vector<Patron> aux = LectorPalabras();
                        v[q] = aux;
                        cont++;
                    }
                }
                else if(opc == 2)
                    imprimeMaxMin();
                else if(opc == 3)
                    recuperaPalabra(v);
                else if(opc == 0)
                    return 0;
                else
                    cout << "Opcion no valida.\n\n";
            }
        }
        else
        {
            flag = 1; 
            cout << "Cuantas clases desea:";
            cin >> clas;
            cout << "Cuantos elementos tendra cada patron: ";
            cin >> elem;
            
            vector< vector <Patron> > v;
                
            for(int i = 0; i < clas*elem; i++)
                maximo.push_back(0);
            for(int i = 0; i < clas*elem;i++)
                minimo.push_back(100);

            for(int q = 0; q < clas; q++)//REALIZA LA LECTURA DE LOS PATRONES
            {  
                vector<Patron> aux = LectorVectores();
                v.push_back(aux);
                cont++;
            }
            system("cls");

            int opc=10;

            CalculoMaximo(v);

            while(opc!=0)
            {
                cout << "1- Volver a ingresar datos\n";
                cout << "2- Imprimir matriz maxima\n";
                cout << "3- Recuperar datos de matriz maxima\n";
                cout << "4- Recuperar patron con rudio.\n";
                cout << "0- Salir\n";
                cout << "Elija una opcion: ";
                cin >> opc;
                if(opc == 1)
                {
                    system("clear");
                    sum_max.clear();

                    cout << "\t\tMemoria Asociativa Alpha Beta\n\n";
                    cout << "\t\tCon codificacion OneHot\n\n";
                    cout << "Cuantas clases desea:";
                    cin >> clas;
                    cout << "Cuantos elementos tendra cada patron: ";
                    cin >> elem;
                    cont = 0;
                    for(int q = 0; q < clas; q++)
                    {  
                        vector<Patron> aux = LectorVectores();
                        v[q] = aux;
                        cont++;
                    }
                }
                else if(opc == 2)
                    imprimeMaxMin();
                else if(opc == 3)
                    recuperaMaxMin(v);
                else if(opc == 4)
                    recuperaMaxRuido(v);
                else if(opc == 0)
                    return 0;
                else
                    cout << "Opcion no valida.\n\n";
            }
        }
    }
}

void imprimeMaxMin()
{
    cout << "\t\tMatriz Maxima\n\n";
    for(int k = 0; k < clas; k++)
    {
        for(int m = 0; m < elem; m++)
            cout << maximo[(k*(elem))+m] << ' ';
        cout << "\n\n";
    }
    /*for(int i = 0; i < sum_max.size(); i++)
        cout << sum_max[i] << ' ';*/
    cout << "\n\n";
}

void recuperaPalabra(vector< vector<Patron> > a)
{
    vector<int>va;
    cout << "\t\tRecuperacion de Matriz Maxima (Palabra)\n\n";
    string x="a";   

    cout << "Ingrese el patron a recuperar: ";
    cin >> x;
    
    int s_acum = 0;
    z.clear();  
    va.clear();

    for(int i = 0; i < x.length(); i++)
    {  
        int aux = (int)x[i];
        bitset<8> letra(aux);
        for(int j = 7; j >= 0; j--)
        {
            if(aux == 1)
                s_acum++;
            va.push_back(letra[j]);
        }
    } 

    for(int k = 0; k < clas; k++)
    {
        int t_max = 100;
        for(int m = 0; m < elem; m++)
        {
            int m_temp;
            if(maximo[(k*(elem))+m] == 2)
            {
                m_temp = 1;
            }
            else if(maximo[(k*(elem))+m] == 1)
            {   if(va[m] == 1)
                    m_temp = 1;
                else
                    m_temp = 0;
            }
            else if(maximo[(k*(elem))+m] == 0)
            {
                m_temp = 0;
            }   
            t_max = min(t_max,m_temp);
        }
        z.push_back(t_max);
    }
    vector<int> r_t;
    r_t.clear();
    int t_max = -1;

    for(int i = 0; i < clas; i++)
    {   
        r_t.push_back(sum_max[i]*z[i]);
        t_max = max(t_max,sum_max[i]*z[i]);
    }   
    for(int i = 0; i < clas; i++)
    {   
        if(r_t[i] != t_max)
            r_t[i] = 0;
        else
            r_t[i] = 1;
    }  
    string r_a;
    r_a.clear();
    for(int y = 0; y < clas; y++)
    {   
        r_a += r_t[y]+'0';
    }

    for(int i = 0; i < a.size(); i++)
    {
        vector<Patron> aux = a[i];
        for(int j = 0; j < aux.size(); j++)
        {
            string s_aux2;
            int temp_cont=0;
            vector<int> aly = aux[j].obtenerclase();
            string nombre = aux[j].obtenernombre();
            for(int y = 0; y < clas; y++)
            {   
                s_aux2 += aly[y]+'0';
            }
            if(!r_a.compare(s_aux2))
            {
                cout << "El patron pertence a la clase " << nombre << ".\n\n"; 
                return;
            }
        }
    }
    cout << "El patron no pertence a ninguna clase\n\n";
}

void recuperaMaxRuido(vector< vector<Patron> > a)
{
    vector<int>va;
    cout << "\t\tRecuperacion de Matriz Maxima\n\n";
    string x="a"; 
    z.clear();  
    va.clear();
    int c_op=0,tp_r=0;
    double p_r = 0;
    vector<string> cads;
    for(int i = 0; i < a.size(); i++)
    {
        vector<Patron> aux = a[i];
        for(int j = 0; j < aux.size(); j++)
        {
            string s_aux2,s_aux;
            int temp_cont=0;
            vector<int> aly = aux[j].obtenerclase();
            vector<int> alx = aux[j].obtenercaracteristicas();
            string nombre = aux[j].obtenernombre();
            for(int y = 0; y < clas; y++)
            {   
                s_aux2 += aly[y]+'0';
            }
            for(int x = 0; x < elem; x++)
                s_aux += alx[x]+'0';
            cads.push_back(s_aux);
            cout << i + 1 << "- " << s_aux2 << ' ' << nombre << endl;
        }
    }

    cout << "Seleccione la clase a la que desea agregarle ruido:";
    cin >> c_op;

    x = cads[c_op];

    int c_u=0,c_c=0;
    if(flag == 1)
    {
        for(int i = 0; i < x.length(); i++)
        {  
            int aux = x[i] - '0';
            if(aux == 0)
                c_c++;
            else
                c_u++;
            va.push_back(aux);
        } 
    }

    cout << "1-Ruido aditivo.\n";
    cout << "2-Ruido sustractivo.\n";
    cout << "3-Ruido mixto.\n";
    cout << "Seleccione el tipo de ruido deseado: ";
    cin >> tp_r;

    if(tp_r == 1)
    {
        cout << "Ingrese el porcentaje de ruido: ";
        cin >> p_r;
        int un_c = (c_c*p_r)/100;
        while(un_c != 0)
        {
            int con_ca=0;
            for(int i = 0; i < va.size(); i++)
            {
                if(va[i] == 0)
                    con_ca++;
            }

            int r_pos = rand() % va.size();
            if(va[r_pos] == 0)
            {
                va[r_pos] = 1;
                un_c--;
            }

            if(con_ca == va.size())
                un_c = 0;
        }
    }
    else if(tp_r == 2)
    {
        cout << "Ingrese el porcentaje de ruido: ";
        cin >> p_r;
        int un_c = (c_u*p_r)/100;
        while(un_c != 0)
        {
            int con_ca=0;
            for(int i = 0; i < va.size(); i++)
            {
                if(va[i] == 1)
                    con_ca++;
            }

            int r_pos = rand() % va.size();
            if(va[r_pos] == 1)
            {
                va[r_pos] = 0;
                un_c--;
            }

            if(con_ca == va.size())
                un_c = 0;
        }
    }
    else if(tp_r == 3)
    {
        cout << "Ingrese el porcentaje de ruido: ";
        cin >> p_r;
        int un_c = (c_u*(p_r/2))/100;
        int un_u = (c_c*(p_r/2))/100;
        while(un_c != 0 && un_u != 0)
        {

            int r_t_a = rand() % 2;
            if(r_t_a == 0)
            {
                int r_pos = rand() % va.size();
                if(va[r_pos] == 0)
                {
                    va[r_pos] = 1;
                    un_c--;
                }
            }
            else if(r_t_a == 1)
            {
                int r_pos = rand() % va.size();
                if(va[r_pos] == 1)
                {
                    va[r_pos] = 0;
                    un_u--;
                } 
            }
            
        }
    }
    /*for(int i = 0; i < va.size(); i++)
    {
        cout << va[i];
    }
    cout << endl;*/

    vector<Patron> aux = a[0];
    vector<int> alx = aux[0].obtenercaracteristicas();
    vector<int> aly = aux[0].obtenerclase();

    for(int k = 0; k < aly.size(); k++)
    {
        int t_max = 100;
        for(int m = 0; m < alx.size(); m++)
        {
            int m_temp;
            if(maximo[(k*(alx.size()))+m] == 2)
            {
                m_temp = 1;
            }
            else if(maximo[(k*(alx.size()))+m] == 1)
            {   if(va[m] == 1)
                    m_temp = 1;
                else
                    m_temp = 0;
            }
            else if(maximo[(k*(alx.size()))+m] == 0)
            {
                m_temp = 0;
            }   
            t_max = min(t_max,m_temp);
        }
        z.push_back(t_max);
    }
    vector<int> r_t;
    r_t.clear();
    int t_max = -1;

    for(int i = 0; i < clas; i++)
    {   
        r_t.push_back(sum_max[i]*z[i]);
        t_max = max(t_max,sum_max[i]*z[i]);
    }   
    for(int i = 0; i < clas; i++)
    {   
        if(r_t[i] != t_max)
            r_t[i] = 0;
        else
            r_t[i] = 1;
    }  
    string r_a;
    r_a.clear();
    for(int y = 0; y < clas; y++)
    {   
        r_a += r_t[y]+'0';
    }

    for(int i = 0; i < a.size(); i++)
    {
        vector<Patron> aux = a[i];
        for(int j = 0; j < aux.size(); j++)
        {
            string s_aux2;
            int temp_cont=0;
            vector<int> aly = aux[j].obtenerclase();
            string nombre = aux[j].obtenernombre();
            for(int y = 0; y < clas; y++)
            {   
                s_aux2 += aly[y]+'0';
            }
            if(!r_a.compare(s_aux2))
            {
                cout << "El patron pertence a la clase " << nombre << ".\n\n"; 
                return;
            }
        }
    }
    cout << "El patron no pertence a ninguna clase\n\n";
}


void recuperaMaxMin(vector< vector<Patron> > a)
{
    vector<int>va;
    cout << "\t\tRecuperacion de Matriz Maxima\n\n";
    string x="a"; 
    z.clear();  
    va.clear();

    if(flag == 1)
    {
        while(elem!=x.length())
        {
            cout << "Ingrese el patron a recuperar: ";
            cin >> x;
            if(elem!=x.length())
                cout << "Tamano diferente al especificado al inicio\n";
        }
        for(int i = 0; i < x.length(); i++)
        {  
            int aux = x[i] - '0';
            va.push_back(aux);
        } 
    }
    vector<Patron> aux = a[0];
    vector<int> alx = aux[0].obtenercaracteristicas();
    vector<int> aly = aux[0].obtenerclase();
    for(int k = 0; k < aly.size(); k++)
    {
        int t_max = 100;
        for(int m = 0; m < alx.size(); m++)
        {
            int m_temp;
            if(maximo[(k*(alx.size()))+m] == 2)
            {
                m_temp = 1;
            }
            else if(maximo[(k*(alx.size()))+m] == 1)
            {   if(va[m] == 1)
                    m_temp = 1;
                else
                    m_temp = 0;
            }
            else if(maximo[(k*(alx.size()))+m] == 0)
            {
                m_temp = 0;
            }   
            t_max = min(t_max,m_temp);
        }
        z.push_back(t_max);
    }
    vector<int> r_t;
    r_t.clear();
    int t_max = -1;

    for(int i = 0; i < clas; i++)
    {   
        r_t.push_back(sum_max[i]*z[i]);
        t_max = max(t_max,sum_max[i]*z[i]);
    }   
    for(int i = 0; i < clas; i++)
    {   
        if(r_t[i] != t_max)
            r_t[i] = 0;
        else
            r_t[i] = 1;
    }  
    string r_a;
    r_a.clear();
    for(int y = 0; y < clas; y++)
    {   
        r_a += r_t[y]+'0';
    }

    for(int i = 0; i < a.size(); i++)
    {
        vector<Patron> aux = a[i];
        for(int j = 0; j < aux.size(); j++)
        {
            string s_aux2;
            int temp_cont=0;
            vector<int> aly = aux[j].obtenerclase();
            string nombre = aux[j].obtenernombre();
            for(int y = 0; y < clas; y++)
            {   
                s_aux2 += aly[y]+'0';
            }
            if(!r_a.compare(s_aux2))
            {
                cout << "El patron pertence a la clase " << nombre << ".\n\n"; 
                return;
            }
        }
    }
    cout << "El patron no pertence a ninguna clase\n\n";
}

//Funcion que calcula la matriz maxima con los datos ingresados
void CalculoMaximo(vector< vector<Patron> > a)
{
    for(int i = 0; i < a.size(); i++)
    {
        vector<Patron> aux = a[i];
        for(int j = 0; j < aux.size(); j++)
        {
            vector<int> alx = aux[j].obtenercaracteristicas();
            vector<int> aly = aux[j].obtenerclase();
            for(int y = 0; y < aly.size(); y++)
            {
                for(int x = 0; x < alx.size(); x++)                
                {
                    int m_temp;
                    if(alx[x] == 1)
                    {   if(aly[y] == 1)
                            m_temp = 1;
                        else
                            m_temp = 0;
                    }
                    else if(alx[x] == 0)
                    {
                        if(aly[y] == 1)
                            m_temp = 2;
                        else
                            m_temp = 1;
                    }   
                    maximo[(y*(alx.size()))+x] = max(maximo[(y*(alx.size()))+x], m_temp);
                }
            }   
        } 
    }
}

//Funcion que imprime los patrones de las clases dadas
void imprime(vector< vector<Patron> > a)
{
    cout << "\t\tInformacion\n\n";
    for(int i = 0; i < a.size(); i++)
    {
        vector<Patron> aux = a[i];
        for(int j = 0; j < aux.size(); j++)
        {
            cout << "X" << i + 1 << " : "; 
            vector<int> als = aux[j].obtenercaracteristicas();
            vector<int> alr = aux[j].obtenerclase();
            for(int k = 0; k < als.size(); k++)
                cout << als[k] << ' ';
            cout << "\n";
            cout << "Y" << i + 1 << " : "; 
            for(int k = 0;k < alr.size(); k++)
                cout << alr[k] << ' ';
            cout << "\n\n";
        }
    }
}

//Lector de Palabras
vector<Patron> LectorPalabras()
{
    int num = 0, aux = 0;
    vector<Patron>al;

        vector<int>va;
        vector<int>vs;
        string x="a";  
        string no=""; 

        cout << "Ingrese la palabra de la clase " << cont + 1 << " : ";
        cin >> x;
        int s_tp =x.length()*8;
        elem = max(elem,s_tp);

        for(int i = 0; i < clas; i++)
        {
            if(i == cont)
                vs.push_back(1);
            else
                vs.push_back(0);
            cout << vs[i];
        }
        cout << endl;
            

        int s_acum = 0;
        for(int i = 0; i < x.length(); i++)
        {  
            int aux = (int)x[i];
            bitset<8> letra(aux);
            for(int j = 7; j >= 0; j--)
            {
                cout << letra[j];
                if(aux == 1)
                    s_acum++;
                va.push_back(letra[j]);
            }

        } 
        cout << endl;
        sum_max.push_back(s_acum);

        Patron auxs(va,vs,x);

        al.push_back(auxs);
    
    return al;
}

//Lector de Patrones
vector<Patron> LectorVectores()
{
    int num = 0, aux = 0;
    vector<Patron>al;

        vector<int>va;
        vector<int>vs;
        string x = "a";  
        string no=""; 
        while(elem!=x.length())
        {
            cout << "\n\nIngrese el patron de la clase " << cont + 1 << " : ";
            cin >> x;
            if(elem!=x.length())
                cout << "Tamano diferente al especificado al inicio\n";
        }
        int s_acum = 0;
        for(int i = 0; i < x.length(); i++)
        {  
            int aux = x[i] - '0';
            if(aux == 1)
                s_acum++;
            va.push_back(aux);
        } 

        sum_max.push_back(s_acum);

        while(clas!=x.length())
        {
            cout << "Ingrese la clase " << cont + 1 << " : ";
            cin >> x;
            if(clas!=x.length())
                cout << "Tamano diferente al especificado al inicio\n";
        }

        for(int i = 0; i < x.length(); i++)
        {  
            int aux = x[i] - '0';
            vs.push_back(aux);
        } 
        cout << "Ingrese el nombre distintivo para la clase: ";
        cin >> no;
        Patron auxs(va,vs,no);

        al.push_back(auxs);
    
    return al;
}