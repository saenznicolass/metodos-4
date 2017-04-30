#include <stdio.h>
#include <stdlib.h>
#include <math.h>

# include <stdio.h>
# include <math.h>

#define b 100

//punteros no, listas 
//alpha, v, dt y dx double
double estoy[b][b];
double pasado[b][b];
int i;
int j;
int k;
int l;
int it;
double dx;
double alpha;
double v;
double dt;

//hacer alpha= 0.25

//en posicion i, j= 50, 
int condicion1()
{
    for(i = 0;i<b;i++)
	{
      for(j = 0;j<b;j++)
	  {
            estoy[i][j] = 50;
            estoy[i][j] = 50;
            estoy[i][j] = 50;
            }
    }

 for(i = 44;i<54;i++)
 {
      for(j = 19; j<39;j++)
	  {
            estoy[i][j] = 100;        
            }
      }   
      return 1;
}



//usar mismo arreglo para todaslas condiciones
int texto(char s[])
{
    
    FILE *tex =fopen(s,"w+");    
    for(i = 0;i<b;i++)
	{
      for(j = 0;j<b;j++)
	  {
            fprintf(tex,"%f ",estoy[i][j]);
            }
            fprintf(tex,"\n");
    }

    
    
}


//poner ecuacion hoja 5, sumarle dimension en y. carpeta 2, preguntar si si da eso. pag 400 landau
//resuelve ecuacion para condicion fija caso 1
//dividir tmax sobre dt
int condicion1c1(int t)
{
it = t/dt;
for(k = 0 ; k<it;k++)
{
      for(i = 1;i<b-1;i++)
	  {
            for(j = 1;j<b-1;j++)
			{
                  pasado[i][j]=estoy[i][j];
                  estoy[i][j]= estoy[i][j] - 4*alpha*estoy[i][j] + alpha*(estoy[i-1][j]+estoy[i+1][j]+estoy[i][j-1]+estoy[i][j+1]);
                  }
            }
      }
    
    return 1;  
}

//condicion de frontera fija caso 2.
int condicion1c2(int t)
{
it = t/dt;
for(k = 0 ; k<it;k++)
{
      for(i = 1;i<b-1;i++)
	  {
            for(j = 1;j<b-1;j++)
			{
                  pasado[i][j]=estoy[i][j];
                  if( estoy[i][j] != 100)
				  {
                      
                  estoy[i][j]= estoy[i][j] - 4*alpha*estoy[i][j] + alpha*(estoy[i-1][j]+estoy[i+1][j]+estoy[i][j-1]+estoy[i][j+1]);
                  }
                  }
            }
      }
    
    return 1;
    
}

//hacer modulo para cada i,j despues del igual
//condicion de frontera periodica caso 1
int condicion2c1(int t)
{
it = t/dt;
for(k = 0 ; k<it;k++)
{
      for(i = 0;i<b;i++)
	  {
            for(j = 0;j<b;j++)
			{
                  pasado[i][j]=estoy[i][j];
                  estoy[i][j]= estoy[i%100][j%100] - 4*alpha*estoy[i%100][j%100] + alpha*(estoy[(i-1)%100][j%100]+estoy[(i+1)%100][j%100]+estoy[i%100][(j-1)%100]+estoy[i%100][(j+1)%100]);
                  }
            }
      }
    
    return 1;  
}

//condicion de frontera periodica caso 2
int condicion2c2(int t)
{
it = t/dt;
for(k = 0 ; k<it;k++)
{
      for(i = 0;i<b;i++)
	  {
            for(j = 0;j<b;j++)
			{
                  pasado[i][j]=estoy[i][j];
                  if( estoy[i][j] != 100)
				  {
                  	estoy[i][j]= estoy[i%100][j%100] - 4*alpha*estoy[i%100][j%100] + alpha*(estoy[(i-1)%100][j%100]+estoy[(i+1)%100][j%100]+estoy[i%100][(j-1)%100]+estoy[i%100][(j+1)%100]);
                  
				  }
              
                  
                  }
            }
      }
    
    return 1;  
}


//condicion abierta, como es?



int main ()
{



//condicion fija, caso 1 t = 0
condicion1();
texto("t0fC1.txt");

//condicion fija, caso 2 t = 0
condicion1();
texto("t0fC2.txt");


//condicion fija, caso 1 t = 100
condicion1();
condicion1c1(100);
texto("t100fC1.txt");


//condicion fija, caso 2 t = 100
condicion1();
condicion1c2(100);
texto("t100fC2.txt");

//condicion fija, caso 1 t = 2500
condicion1();
condicion1c1(2500);
texto("t2500fC1.txt");

//condicion fija, caso 2 t = 2500
condicion1();
condicion1c2(2500);
texto("t2500fC2.txt");


//condicion periodica, caso 1 t = 0
condicion1();
texto("t0pC1.txt");

//condicion periodica, caso 2 t = 0
condicion1();
texto("t0pC2.txt");


//condicion periodica, caso 1 t = 100
condicion1();
condicion2c1(100);
texto("t100pC1.txt");

//condicion periodica, caso 2 t = 100
condicion1();
condicion2c2(100);
texto("t100pC2.txt");


//condicion periodica, caso 1 t = 2500
condicion1();
condicion2c1(2500);
texto("t2500pC1.txt"); 

//condicion periodica, caso 2 t = 2500
condicion1();
condicion2c2(2500);
texto("t2500pC2.txt");


dt = 0.25;
dx = 0.01;
alpha = 0.25;
v = 0.0001;












}










