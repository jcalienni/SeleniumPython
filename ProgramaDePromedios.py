#Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
#Se pide imprimir el nombre, el apellido y el promedio.
#Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
#En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".


nombre = input("Ingresar nombre de alumno:")
apellido = input("Ingresar apellido de alumno:")
nota_matematica = float(input("Ingresar nota de matematica:"))
nota_literatura = float(input("Ingresar nota de literatura:"))
nota_fisica = float(input("Ingresar nota de fisica:"))

def promedio (a,b,c):
    promediof = ((a+b+c)/3)
    return promediof


print ("Nombre de alumno: " + nombre)
print ("Apellido de alumno: " + apellido)
promedio_alumno = promedio (nota_literatura, nota_fisica, nota_matematica)
print ("Promedio de alumno: " + str(promedio_alumno))

if promedio_alumno >= 6:
    print ("Aprobado")
    if promedio_alumno >= 9:
        print ("Alumno destacado")
elif promedio_alumno < 4:
    print ("Insuficiente")
else:
    print ("A recuperatorio")