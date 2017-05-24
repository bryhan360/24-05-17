#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

path_to_explore="./ejerciocio_directorios/"

#Muestra solo los Directorios

for root, dirs, files in os.walk(path_to_explore):
	for name in dirs:
		print name
		
print "------------------------------------------------"

#Muestra solo los Archivos

for root, dirs, files in os.walk(path_to_explore):
	for name in files:
		print name
		
print "------------------------------------------------"

#Muestra todo

for root, dirs, files in os.walk(path_to_explore):
	for name in files:
		print name
		
	for name in dirs:
		print name
		
print "------------------------------------------------"

#Muestra Rutas de Archivos

for root, dirs, files  in os.walk(path_to_explore):
	for name in files:
		
		name_path=os.path.join(root, name)
		print (name_path)
	
print "------------------------------------------------"

#Muestra ruta de directorios

for root, dirs, files  in os.walk(path_to_explore):
	for name in dirs:
		
		name_path=os.path.join(root, name)
print (name_path)
