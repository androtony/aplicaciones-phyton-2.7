# -*- coding: utf-8 -*-

print "hola bienvenido al restaurante"

no_salir = True
dict = {}

while no_salir:

    plato = raw_input("introduzca nuevo plato al menu: ")
    precio = float(raw_input("introduzca precio del plato: "))

    print "tu nuevo plato es: {} ; {}$".format(plato,precio)

    dict[plato] = precio

    salir = raw_input("desea salir del menu (y/n):  ")
    if salir == "y":
        no_salir = False
    
print "numero de platos del menu: {}".format(len(dict))
print "elementos del menu:"
for key in dict.iteritems():
    print "- {}".format(key),

print "fin del programa menu "