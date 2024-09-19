#Crear un algoritmo, que dado N números enteros ingresados por teclado determine cuál de ellos es el menor y mayor respectivamente

n= int(input("ingrese cuantos numeros va a comparar"))


if n == 2:

    num1= int(input("ingrese un numero"))
    num2=int(input("ingrese un numero"))

    lista= list([num1,num2])

    resultado = lista.reverse()
    print(" los numeros estan ordenados de izquierda a derecha, de mayor a menor :)")

    print(lista)
else:
    print("numero equivocado")



if n == 3:
    num1= int(input(" ingrese el primer numero:  "))
    num2= int(input("ingrese el segundo numero:  "))
    num3= int(input(" ingrese el tercer numero:  "))

    lista= list([num1,num2,num3])
    resultado = lista.reverse()
    print("los numeros estan ordenados de izquierda a derecha, de mayor a menor :)")
    print(lista)



