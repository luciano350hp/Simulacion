#!/usr/bin/python

import re
import collections
from Funciones import textoSinPalabrasProhibidas

# EJERCICIO 2
# EJERCICIO 2.2	
#	PALABRAS PROHIBIDAS

archivo = open("king_lear.txt", 'r')
archivo2 = open("prohibidas.txt", 'r')
textoV1 = archivo.read()
listaProhibidas = archivo2.readlines()


print ('*********')
texto, listaProhibidas = textoSinPalabrasProhibidas(textoV1,listaProhibidas)
print ("Prohibidas:", listaProhibidas)
print ('*********')
print (texto)
