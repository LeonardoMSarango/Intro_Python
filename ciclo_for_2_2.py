#Vamos hacer un scrip que calcule el iva de un 
#de una tienda
#se puede rellenar con 0
#Pedimos los datos
m1=float(input("Ingrese el monto "))
m2=float(input("Ingrese el monto "))
m3=float(input("Ingrese el monto "))
m4=float(input("Ingrese el monto "))
m5=float(input("Ingrese el monto "))
m6=float(input("Ingrese el monto "))
#Generamos la variable del 12% del iva en ecuador
t_i=0.12
#Iniciazamos las variables auxiliares 
z=0
x=0
#Agruapmos los datos pedidos en una lista
m=(m1,m2,m3,m4,m5,m6)
#Creamos un ciclo for para poder operar con todos los datos de la lista "m"
for i in m:
    #Aqui digo que mi variable i tome los valores de m, en secuencia, del primero al ultimo. 
    x=x+1
    #Aqui estoy creando un contador, primero esta 0, pero al sumarle 1 en cada ciclo va a ir cambiando --> i++
    print("ciclo ",x )
    #Aqui estoy presentando el número del ciclo
    print("Valor anterior de z = ",z)
    #Verifico el valor anterior de z
    w=i*t_i
    #Aqui estoy calculando los impuesto, al multiplicar mi varible t_1 con el valor de cada mes
    print("Valor del iva mes ",x," = ",w)
    #Aqui presento el valor del iva cada mes 
    z=z+w
    #Aqui utilizo mi variable auxiliar z para generar una sumatoria de los valores de w, es decir de los impuestos mensuales
    print("Valor del iva actualizado en el ciclo ",x," = ",z)
    #Aqui presento el valor actual de z en el ciclo x 
print("-----------------------------------------------")     
#Separo los resultados
print("El valor total de iva es: ",z)
#Presento el valor total 
#Verificar si los ingresos del usuario sobre pasan los 2000 dolares 
#el valor del iva ya no sera el 12% sino el 24% 
#Presentar el valor total iva a pagar. 