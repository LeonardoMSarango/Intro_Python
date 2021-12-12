y=0
z=10
x=int(input("Ingrese el número de la tabla que desea "))
print("Tabla del", x) 
z=(z*x)
rango = range(y,z,x)
for i in rango:
    print(i)