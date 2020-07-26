

def ingresar_numero():
    numero = int(input("ingrese numero: "))
    numero = numero *5
    return numero

def hacer_algo_con_numeros(a,b):
    return a + b

a=1
b=2
mi_variable = print(hacer_algo_con_numeros(a,b))
mi_numero = ingresar_numero()
print (mi_numero)
