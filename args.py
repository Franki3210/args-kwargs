#args es convencion en python q permite pasar un numero variable de argumentos posicion a funcion
def sumar(*args):
    suma=0
    for i in args:
        suma+=i
    return suma
result=sumar(1,2,3,4,5)
print(result)
