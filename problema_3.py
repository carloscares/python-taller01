#Cree un programa que dado una lectura de una lista
#genere una lista con las longitudes de cada elemento
#Ejemplo de entrada
#uno dos tres cuatro cinco noventa
#salida
#[3, 3, 4, 6, 5, 7]
lista = input().split()
print([len(lista) for x in lista])