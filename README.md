# REGISTRO BÁSICO DE VENTAS DIARIAS

## Descripción

Este proyecto es un programa sencillo en Python que permite registrar una venta diaria, calcular el subtotal, aplicar un descuento si el cliente tiene membresía VIP y mostrar un resumen final.

## Funcionalidades

El programa permite:

- Solicitar el nombre y apellido del cliente
- Ingresar el precio de un producto
- Ingresar la cantidad de productos
- Preguntar si el cliente tiene membresía (Si/No)
- Calcular el subtotal
- Aplicar un 10% de descuento si el cliente es VIP
- Mostrar un resumen de la compra

## Lógica del programa

- Se muestran encabezados decorativos en consola
- Se solicitan datos del cliente
- Se valida que el precio y la cantidad sean números(float)
- Se pregunta si el cliente tiene membresía:
  - Si responde "si" = Se aplica descuento
  - Si responde "no" = No hay descuento
- Se calcula:
  - subtotal = subtotal * cantidad
  -descuento = subtotal * 0.10 (si es VIP)
  -total = subtotal - descuento
-Se imprime el resumen final.

## Tecnologías usadas

- Python3
- funciones utilizadas:
 - input()
 - print()
 - float()
 - try / except
 - condicionales if / else

## Posibles mejoras

- Validar correctamente que solo se acepten "si" o "no"
- Formatear los valores monetarios a 2 decimales
- Mostrar el total final en el resumen
- Manejar mejor los errores específicos (ValueError)
- Separar la logica en funciones