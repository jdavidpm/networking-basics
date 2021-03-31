#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void)
{
	unsigned char IP[4] = {0}; //IP
	unsigned char MS[4] = {0}; //Máscara de Red
	unsigned char flag = 1, type = -1;

	while (flag)
	{
		system("clear");
		printf("\nIngrese IP: ");
		scanf("%hhu.%hhu.%hhu.%hhu", &IP[0], &IP[1], &IP[2], &IP[3]); //Se lee la IP en el formato n.n.n.n

		system("clear");
		printf("\nLa IP: %hhu.%hhu.%hhu.%hhu", IP[0], IP[1], IP[2], IP[3]);

		if (IP[0] & 128)
		{
			if (IP[0] & 64)
			{
				if (IP[0] & 32)
				{
					if (IP[0] & 16)
					{
						if (IP[0] & 8)
						{
							printf(" es: Clase E\n");
							goto classE;
						}
						else
						{
							printf(" es: Clase E\n");
							goto classE;
						}
					}
					else
					{
						printf(" es: Clase D\n");
						goto classD;
					}
				}
				else
				{
					printf(" es: Clase C\n");
					MS[0] = MS[1] = MS[2] = ~MS[0];
					if (IP[3] == (unsigned char)0)
						type = 0;
					else if (IP[3] == (unsigned char)255)
						type = 1;
					else
						type = 2;
				}
			}
			else
			{
				printf(" es: Clase B\n");
				MS[0] = MS[1] = ~MS[0]; //Se inicializa la máscara de red
				if (IP[2] == IP[3] && IP[3] == (unsigned char)0) //Revisa que tipo de IP es
					type = 0;
				else if (IP[2] == IP[3] && IP[3] == (unsigned char)255)
					type = 1;
				else
					type = 2;
			}
		}
		else
		{
			printf(" es: Clase A\n");
			MS[0] = ~MS[0]; //Se inicializa la máscara de red
			if (IP[1] == IP[2] && IP[2] == IP[3] && IP[3] == (unsigned char)0) //Revisa que tipo de IP es
				type = 0;
			else if (IP[1] == IP[2] && IP[2] == IP[3] && IP[3] == (unsigned char)255)
				type = 1;
			else
				type = 2;


		}

		printf("-----------------------------------------------------------\n");
		printf("Mascara de Red: %d.%d.%d.%d\n", MS[0], MS[1], MS[2], MS[3]);
		printf("Tipo: ");
		if (type == (unsigned char)0) //Si es de Red
		{
			printf("Red\n");
			printf("Broadcast: %d.%d.%d.%d\n",  IP[0] | (unsigned char)~(MS[0]), IP[1] | (unsigned char)~(MS[1]), IP[2] | (unsigned char)~(MS[2]), IP[3] | (unsigned char)~(MS[3]));
		}
		if (type == (unsigned char)1)//Si es de Broadcast
		{
			printf("Broadcast\n");
			printf("Red: %d.%d.%d.%d\n", IP[0] & MS[0], IP[1] & MS[1], IP[2] & MS[2], IP[3] & MS[3]);
		}
		if (type == (unsigned char)2) //Si es de Host
		{
			printf("Host\n");
			printf("Red: %d.%d.%d.%d\n", IP[0] & MS[0], IP[1] & MS[1], IP[2] & MS[2], IP[3] & MS[3]);
			printf("Broadcast: %d.%d.%d.%d\n",  IP[0] | (unsigned char)~(MS[0]), IP[1] | (unsigned char)~(MS[1]), IP[2] | (unsigned char)~(MS[2]), IP[3] | (unsigned char)~(MS[3]));
		}
		printf("Rango: de %d.%d.%d.%d a %d.%d.%d.%d\n", IP[0] & MS[0], IP[1] & MS[1], IP[2] & MS[2], (IP[3] & MS[3]) + 1, IP[0] | (unsigned char)~(MS[0]), IP[1] | (unsigned char)~(MS[1]), IP[2] | (unsigned char)~(MS[2]), (IP[3] | (unsigned char)~(MS[3])) - 1);
		
		printf("-----------------------------------------------------------\n");


		classD:
		classE:
		memset (IP, 0, 4); //Limpia la variable de la IP
		memset (MS, 0, 4); //Limpia la variable de la mascara
		printf("\nSi desea ingresar otra presione [1] o terminar [0]: ");
		scanf("%hhu", &flag); //Lee la respuesta de repeticion
	}

	return 0;
}
