#Cree un programa en python que 
#dado dos números enteros, n1 y n2 se genere una
#lista que comienza en n1 y tiene 12 elementos
#con una diferencia de n2 entre cada uno
#Ejemplo de entrada:
#3
#10
#salida
#[3, 13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113]
n1 = input()
n2 = input()
print([int(n1), int(n2)+int(n2), int(n1*3)])