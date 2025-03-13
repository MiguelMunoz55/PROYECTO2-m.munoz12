from Heladeria import Heladeria
from Producto import Producto
from Base import Base
from Complemento import Complemento
from Malteada import Malteada

def mostrar_menu():
    print("\n--- Menú Heladería Digital ---")
    print("1. Agregar Producto")
    print("2. Agregar Ingrediente")
    print("3. Vender Producto")
    print("4. Mostrar Menú de Productos")
    print("5. Mostrar Ventas del Día")
    print("6. Salir")

def main():
    heladeria = Heladeria([], [])
    
    p1 = Producto("Samurai de fresas", 7500, 2600, 5)          
    p2 = Producto("Samurai de mandarinas", 7500, 5000, 3)
    p3 = Producto("Malteda chocoespacial", 7500, 1500, 10)
    p4 = Producto("Cupihelado", 7500, 4300, 2)
    
    heladeria._Heladeria__productos.extend([p1, p2, p3, p4])
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("\n-- Agregar Producto --")
            nombre = input("Nombre del producto: ")
            precio_publico = float(input("Precio público: "))
            costo = float(input("Costo de producción: "))
            inventario = float(input("Inventario (número de unidades): "))
            nuevo_producto = Producto(nombre, precio_publico, costo, inventario)
            heladeria._Heladeria__productos.append(nuevo_producto)
            print("Producto agregado exitosamente.")
        
        elif opcion == '2':
            print("\n-- Agregar Ingrediente --")
            tipo = input("Tipo de ingrediente (Base/Complemento): ").strip().lower()
            nombre = input("Nombre del ingrediente: ")
            precio = float(input("Precio: "))
            calorias = float(input("Calorías: "))
            inventario = float(input("Inventario: "))
            es_veg = input("¿Es vegetariano? (s/n): ").strip().lower() == 's'
            
            if tipo == "base":
                extra_sabor = input("Extra sabor: ")
                ingrediente = Base(precio, calorias, nombre, inventario, es_veg, extra_sabor)
            else:
                ingrediente = Complemento(precio, calorias, nombre, inventario, es_veg)
            
            heladeria._Heladeria__ingredientes.append(ingrediente)
            print("Ingrediente agregado exitosamente.")
        
        elif opcion == '3':
            print("\n-- Vender Producto --")
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            if heladeria.vender(nombre_producto):
                print("Producto vendido exitosamente.")
            else:
                print("No se pudo vender el producto. Verifique el inventario o que el producto exista.")
        
        elif opcion == '4':
            print("\n-- Menú de Productos --")
            for prod in heladeria._Heladeria__productos:
                print(f"Nombre: {prod.nombre}, Precio público: {prod.precio_publico}, Inventario: {prod.inventario}")
        
        elif opcion == '5':
            print(f"\nVentas totales del día: {heladeria.ventas_dia}")
        
        elif opcion == '6':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()