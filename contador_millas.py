


print "hola,soy un conversor de kilometros a millas, introduce el numero de kilometros que quires convertir"
km = 1
milla = 0.621371

salida = "y"
x = None
n = "n"


while salida != x :

    i = int(raw_input("introduce el numero de kilometros: "))


    resultado = i * milla

    print "el resultado es:", float(resultado)

    x = raw_input("quieres salir del programa: ")
    if salida == x:
        break
    if n == x:
        print "continuemos"
    elif x == None:
        print " "
    else:
        x = raw_input("solo se acepta (n , y): ")
print "fin del programa, adios"

print "buena suerte"

