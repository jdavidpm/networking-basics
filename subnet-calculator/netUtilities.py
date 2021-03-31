from os import system
import math

def byteNet (i, bitsBorrowed, ipClass, rangeI): #Regresa los bytes de red y host
	if (ipClass == 'A'):
		if (bitsBorrowed <= 8):
			return str(i << (8 - bitsBorrowed)) + '.0.' + str (0 + rangeI)
		elif (bitsBorrowed <= 16):
			aux = bin(i)[2:]
			preSeparate = ''.join([str(i - i) for i in range(0, bitsBorrowed - len(aux))]) + aux
			fByte = preSeparate[:8]
			sByte = preSeparate[8:] + ''.join([str(i - i) for i in range(0, 8 - len(preSeparate[8:]))])
			return str(int(fByte, 2)) + '.' + str(int(sByte, 2)) + '.' + str (0 + rangeI)
		else:
			aux = bin(i)[2:]
			preSeparate = ''.join([str(i - i) for i in range(0, bitsBorrowed - len(aux))]) + aux
			fByte = preSeparate[:8]
			sByte = preSeparate[8:16]
			tByte = preSeparate[16:] + ''.join([str(i - i) for i in range (0, 8 - len(preSeparate[16:]))])
			return str(int(fByte, 2)) + '.' + str(int(sByte, 2)) + '.' + str (int(tByte, 2) + rangeI)

	elif (ipClass == 'B'):
		if (bitsBorrowed <= 8):
			return str(i << (8 - bitsBorrowed)) + '.' + str (0 + rangeI)
		else:
			aux = bin(i)[2:]
			preSeparate = ''.join([str(i - i) for i in range(0, bitsBorrowed - len(aux))]) + aux
			fByte = preSeparate[:8]
			sByte = preSeparate[8:] + ''.join([str(i - i) for i in range(0, 8 - len(preSeparate[8:]))])
			return str(int(fByte, 2)) + '.' + str(int(sByte, 2) + rangeI)

	elif (ipClass == 'C'):
		return str((i << (8 - bitsBorrowed)) + rangeI)

def byteBro (i, bitsBorrowed, ipClass, rangeS): #Regresa los bytes de broadcast y host
	if (ipClass == 'A'):
		if (bitsBorrowed <= 8):
			return str(((i << (8 - bitsBorrowed)) + ((2 ** (8 - bitsBorrowed)) - 1))) + '.255.' + str (255 - rangeS)
		elif (bitsBorrowed <= 16):
			aux = bin(i)[2:]
			preSeparate = ''.join([str(i - i) for i in range(0, bitsBorrowed - len(aux))]) + aux
			fByte = preSeparate[:8]
			sByte = preSeparate[8:] + ''.join([str(i//i) for i in range(1, 9 - len(preSeparate[8:]))])
			return str(int(fByte, 2)) + '.' + str(int(sByte, 2)) + '.' + str (255 - rangeS)
		else:
			aux = bin(i)[2:]
			preSeparate = ''.join([str(i - i) for i in range(0, bitsBorrowed - len(aux))]) + aux
			fByte = preSeparate[:8]
			sByte = preSeparate[8:16]
			tByte = preSeparate[16:] + ''.join([str(i//i) for i in range (1, 9 - len(preSeparate[16:]))])
			return str(int(fByte, 2)) + '.' + str(int(sByte, 2)) + '.' + str (int(tByte, 2) - rangeS)

	elif (ipClass == 'B'):
		if (bitsBorrowed <= 8):
			return str((i << (8 - bitsBorrowed)) + ((2 ** (8 - bitsBorrowed)) - 1)) + '.' + str (255 - rangeS)
		else:
			aux = bin(i)[2:]
			preSeparate = ''.join([str(i - i) for i in range(0, bitsBorrowed - len(aux))]) + aux
			fByte = preSeparate[:8]
			sByte = preSeparate[8:] + ''.join([str(i//i) for i in range(1, 9 - len(preSeparate[8:]))])
			return str(int(fByte, 2)) + '.' + str(int(sByte, 2) - rangeS)

	elif (ipClass == 'C'):
		return str(((i << (8 - bitsBorrowed)) + ((2 ** (8 - bitsBorrowed)) - 1)) - rangeS)

def howBit (ipClass): #Regresa que tantos bits de host por default tiene una IP
	return (24 if (ipClass == 'A') else (16 if (ipClass == 'B') else 8))

def howByte (ipClass): #Regresa que tantos bytes de red por default tiene una IP
	return (1 if (ipClass == 'A') else (2 if (ipClass == 'B') else 3))

def nearPower(numSH): #Dado un No de subredes o No de Host/Red deseados, regresa la expotente tal que 2^n = No cubre alguno de los dos.
	return math.ceil(math.log(numSH, 2))

def asBigS(ipClass): #Regresa el número máximo de subredes dada una IP
	return (((2 ** 22) - 2) if (ipClass == 'A') else (((2 ** 14) - 2) if (ipClass == 'B') else ((2 ** 6) - 2)))

def asBigH(ipClass): #Regresa el número máximo de host/subred dada una IP
	return (((2 ** 24) - 2) if (ipClass == 'A') else (((2 ** 16) - 2) if (ipClass == 'B') else ((2 ** 8) - 2)))

def asShort(ipClass): #Regresa un número tal que sea el minimo para mostrar una máscara de subred en el formato /N
	return ((8) if (ipClass == 'A') else ((8 * 2) if (ipClass == 'B') else (8 * 3)))

def maskDefault(ipClass): #Regresa la máscara de red que tiene por default cada ip dependiendo su clase
	return ("255.0.0.0" if (ipClass == 'A') else ("255.255.0.0" if (ipClass == 'B') else "255.255.255.0"))

def maskSubnet(ipClass, bitsBorrowed): #Regresa la máscara de subred
	if(ipClass == 'A'):
		if (bitsBorrowed <=8):
			return "255." + str (((2 ** bitsBorrowed) - 1) << (8 - bitsBorrowed)) + '.0.0'
		elif (bitsBorrowed <= 16):
			return "255.255." + str (((2 ** (8 - (16 - bitsBorrowed))) - 1) << (8 - (8 - (16 - bitsBorrowed)))) + '.0'
		else:
			return "255.255.255." + str (((2 ** (8 - (24  - bitsBorrowed))) - 1) << (8 - (8 - (24 - bitsBorrowed))))

	elif(ipClass == 'B'):
		if(bitsBorrowed <= 8):
			return "255.255." + str (((2 ** bitsBorrowed) - 1) << (8 - bitsBorrowed)) + '.0'
		else:
			return "255.255.255." + str (((2 ** (8 - (16 - bitsBorrowed))) - 1) << (8 - (8 - (16 - bitsBorrowed))))

	elif(ipClass == 'C'):
		return "255.255.255." + str (((2 ** bitsBorrowed) - 1) << (8 - bitsBorrowed))

def typeIP(ipAddress, ipClass):
	if (ipClass == 'A'):
		fByte = bin(ipAddress[1])[2:]
		sByte = bin(ipAddress[2])[2:]
		tByte = bin(ipAddress[3])[2:]
		if (fByte == (len(sByte) * fByte[0]) and sByte == (len(sByte) * sByte[0]) and tByte == (len(tByte) * tByte[0]) and sByte[0] == tByte[0]):
			if (sByte[0] == '0'):
				return "Red"
			else:
				return "Broadcast"
		else:
			return "Host"

	elif (ipClass == 'B'):
		sByte = bin(ipAddress[2])[2:]
		tByte = bin(ipAddress[3])[2:]
		if (sByte == (len(sByte) * sByte[0]) and tByte == (len(tByte) * tByte[0]) and sByte[0] == tByte[0]):
			if (sByte[0] == '0'):
				return "Red"
			else:
				return "Broadcast"
		else:
			return "Host"

	elif (ipClass == 'C'):
		tByte = bin(ipAddress[3])[2:]
		if (tByte == (len(tByte) * tByte[0])):
			if (tByte[0] == '0'):
				return "Red"
			else:
				return "Broadcast"
		else:
			return "Host"

def classIP(IP): #Regresa la clase dada una IP
	if (IP & 256):
		return -1
	if (IP & 128):
		if (IP & 64):
			if (IP & 32):
				if (IP & 16):
					if (IP & 8):
						if (IP & 4):
							if (IP & 2):
								if (IP & 1):
									return "E"
								else:
									return -1
							else:
								return "E"
						else:
							return "E"
					else:
						return "E"
				else:
					return "D"
			else:
				return "C"
		else:
			return "B"
	else:
		return "A"

def show(ipAddress, ipClass, ipType, bitsBorrowed, bitsHost, numHost, numSubn): #Muestra todo los argumentos dados
	system('cls')
	print ("\n===============================================================")
	print ("\t\tIP dada: %s" % (ipAddress))
	print ("\t\tClase: %s" % (ipClass))
	print ("\t\tTipo: %s" % (ipType))
	print ("\t\tBits Prestados: %s" % (bitsBorrowed))
	print ("\t\tBits de Host: %s" % (bitsHost))
	print ("\t\tNo. de Host/Subred: %d" % (numHost))
	print ("\t\tNo. de Subredes: %d" % (numSubn))
	print ("\t\tMáscara de Red: %s" % (maskDefault(ipClass)))
	print ("\t\tMáscara de Subred: %s" % (maskSubnet(ipClass, bitsBorrowed)))
	print ("===============================================================\n")