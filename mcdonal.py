Inventario = [{"nombre":"Mcflyrry", "precio":2.50, "stock":10}]

def menu_principal():
    """
    Muestra el menu principal
    """
    while True:
        print("Menu principal")
        print("1.Agregar producto")
        print("2.Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario() 
        elif opcion == "3":   
            vender_producto() 
        elif opcion == "4":
            break
        else:
            print("opcion no validad. porfavor intente de nuevo")  

def agregar_producto():
    """
    Agregar un nuevo producto al inventario
    """

    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre != "":
            break

    precio = float(input("Ingrese el precio del producto: "))  
    cantidad = int(input("Ingrese la cantidad del producto: "))    

    producto = {"nombre": nombre, "precio": precio, "stock" : cantidad}        

    Inventario.append(producto)

    print("Producto {Nombre} agregado al inventario")
    print(Inventario)

def mostrar_inventario():

    """
    Muestra todos los procutos del inventario
    """

    if len(Inventario) == 0:
        print("El inventario esta vacio")
    else:
        print("Presentando Inventario")
    for producto in Inventario:
        print(f"Nombre:{producto['nombre']}, Precio: {producto['precio']:.2f}, Cantidad: {producto['stock']}")

def vender_producto():
    """
    Vende un producto, actualiza el inventario y muestra el total de la venta
    """    

    nombre = input("Ingrese el nombre del producto que desea vender: ")
    for producto in Inventario:
        if producto["nombre"].lower() ==nombre.lower():
            cantidad = int(input(f"¿Cuantas unidades de {nombre} desea vender?: "))
            if cantidad <= producto["stock"]:
                producto["stock"] -= cantidad
                total = cantidad * producto["precio"]
                print(f"Venta realizada.Total: ${total:.2f}")

                if producto["stock"] == 0:
                    print(f"El producto {nombre} se ha agotado.")

                return
            else:
                print("No hay suficiente Stock en el Inventario")    
                return
    print("Producto no encontrado en el Inventario")      

menu_principal()