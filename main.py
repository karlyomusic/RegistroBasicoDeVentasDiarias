print("-"*36)
print ("    Registro de compra    ")
print("-"*36)

try:

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
except:
    print("Error: Ingrese su nombre y apellido")
try:
    precio = float(input("Ingrese el precio: "))
    productos = float(input("Ingrese la cantidad de productos: "))
except:
    print("Ingrese un número")

try:
    cliente = input("Ingrese si tiene membresia si/no: ").lower() == "no"
except:
    print("Error: Ingrese un si o un no")



es_vip = bool()

if cliente == "si":
    es_vip=True
else:
    es_vip=False    


subtotal = precio * productos

if(es_vip):
    descuento = subtotal*0.10
    print("Tiene acceso a descuento") 
else:
    descuento = 0
    print("No tiene acceso a descuento")

total = subtotal - descuento

print("-"*36)
print("    Resumen de la compra   ")
print("-"*36)

print(nombre, apellido)
print(subtotal)
if(cliente == "si"):
    print(descuento)
print(total)
