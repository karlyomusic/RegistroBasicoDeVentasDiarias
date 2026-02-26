print("-"*36)
print ("    Registro de compra    ")
print("-"*36)


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
precio = float(input("Ingrese el precio: "))
productos = float(input("Ingrese la cantidad de productos: "))

cliente = input("Ingrese si tiene membresia si/no: ").lower() == "no"
subtotal = precio * productos
es_vip = True

if(es_vip):
    descuento = subtotal*0.10
    print("Tiene acceso a descuento")

