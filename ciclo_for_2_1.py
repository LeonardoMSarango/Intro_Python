#Vamos hacer un scrip que calcule el iva de un 
#de una tienda
#se puede rellenar con 0
m1=float(input("Ingrese el monto"))
m2=float(input("Ingrese el monto"))
m3=float(input("Ingrese el monto"))
m4=float(input("Ingrese el monto"))
m5=float(input("Ingrese el monto"))
m6=float(input("Ingrese el monto"))
t_i=0.12
m=(m1,m2,m3,m4,m5,m6)
for i in m:
    w=i*t_i
    print(w)

