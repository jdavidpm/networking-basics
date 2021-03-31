#!/usr/bin/env python3
from prettytable import PrettyTable
from netUtilities import *

if __name__ == '__main__':
	rep = 1
	while (rep):
		ipClass = -1
		while (ipClass == -1 or classIP(ipAddress[1]) == -1 or classIP(ipAddress[2]) == -1 or classIP(ipAddress[3]) == -1):
			system('cls')
			print ("\t\t\tSubnetting\n")
			if (rep == 1):
				print("Ingrese direccion IP: ", end = '')
				auxIP = input()

			ipAddress = [int(i) for i in ((auxIP).split('.'))]
			ipClass = classIP(ipAddress[0])

		if (ipClass != 'D' and ipClass != 'E'):
			print("\nElige la opcion deseada:\n\n1) No. de Subredes\n2) No. de Host/Subred\n3) Máscara de Subred")
			opt = -1
			while (opt < 1 or opt > 3):
				print ("-> ", end ='')	
				opt = int(input())

			maxSub = asBigS(ipClass)
			maxHost = asBigH(ipClass)
			numBits = howBit(ipClass)
			staticByte = howByte(ipClass)

			table = PrettyTable(['#SR', 'IP Red', 'Rango', 'IP Broadcast']) #Se crea una tabla

			if (opt == 1):
				numSub = maxSub + 1
				while (numSub > maxSub): #Verifica que no ingrese un número más grande que el máximo
					print("\nIngresa el No. de Subredes: ", end = '')
					numSub = int(input())
				bitsBorrowed = nearPower(numSub)
				show(auxIP, ipClass, typeIP(ipAddress, ipClass), bitsBorrowed, numBits - bitsBorrowed, ((2 ** (numBits - bitsBorrowed)) - 2), (2 ** bitsBorrowed))
				for i in range (0, (2 ** bitsBorrowed)): #Por cada subred se iran agregando las filas con: #SB, IP Red, Rango e IP Broadcast
					table.add_row([i, '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteNet(i, bitsBorrowed, ipClass, 0), '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteNet(i, bitsBorrowed, ipClass, 1) + ' a ' + '.'.join([str(i) for i in ipAddress[:staticByte]])+ '.' + byteBro(i, bitsBorrowed, ipClass, 1), '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteBro(i, bitsBorrowed, ipClass, 0)])
		
			elif (opt == 2):
				numHost = -1
				while (numHost > maxHost or numHost < 2): #Verifica que no se ingrese ni más ni menos host por subred
					print("\nIngresa el No. de Host/Subred: ", end = '')
					numHost = int(input())
				bitsHots = nearPower(numHost + 2)
				numSub = 2 ** (numBits - bitsHots)
				show(auxIP, ipClass, typeIP(ipAddress, ipClass), numBits - bitsHots, bitsHots, ((2 ** bitsHots) - 2), numSub)
				for i in range (0, numSub): #Por cada subred se iran agregando las filas con: #SB, IP Red, Rango e IP Broadcast
					table.add_row([i, '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteNet(i, numBits - bitsHots, ipClass, 0), '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteNet(i, numBits - bitsHots, ipClass, 1) + ' a ' + '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteBro(i, numBits - bitsHots, ipClass, 1), '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteBro(i, numBits - bitsHots, ipClass, 0)])
		
			elif (opt == 3):
				minMask = asShort(ipClass)
				maskSR = -1
				while (maskSR > 30 or maskSR < minMask): #Verifica que la máscara ingresada este dentro de los limites
					print ("\nIngresa la Máscara de Subred: ", end = '')
					aux = input()
					maskSR = int(aux[1:])
				bitsBorrowed = maskSR - minMask
				numSub = 2 ** bitsBorrowed
				show(auxIP, ipClass, typeIP(ipAddress, ipClass), bitsBorrowed, numBits - bitsBorrowed, ((2 ** (numBits - bitsBorrowed)) - 2), (2 ** bitsBorrowed))
				for i in range (0, numSub): #Por cada subred se iran agregando las filas con: #SB, IP Red, Rango e IP Broadcast
					table.add_row([i, '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteNet(i, bitsBorrowed, ipClass, 0), '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteNet(i, bitsBorrowed, ipClass, 1) + ' a ' + '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteBro(i, bitsBorrowed, ipClass, 1), '.'.join([str(i) for i in ipAddress[:staticByte]]) + '.' + byteBro(i, bitsBorrowed, ipClass, 0)])

			print ("\nPresione [Enter] para mostra tabla...", end = '')
			input()
			print ("\n")
			print (table) #Muestra tabla

		else:
			system('cls')
			print ("\n===============================================================")
			print ("\t\tIP dada: %s" % ('.'.join([str(i) for i in ipAddress])))
			print ("\t\tClase: %s" % (ipClass))
			print ("===============================================================\n")
	
		print ("\n[2] Usar misma IP\n[1] Ingresar otra IP\n[0] Salir del programa\n-> ", end = '')
		rep = int(input())