from components import Menu,Valida
from utilities import borrarPantalla,gotoxy,dibujar_cuadro
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient,VipClient
from sales import Sale,SaleDetail
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion

class CrudClients(ICrud):
    def create(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print( green_color+ "=" * 180 +reset_color )
        gotoxy(80, 2)
        print("REGISTRAR DE CLIENTE")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(75, 5)
        print(purple_color + "Seleccione el tipo de cliente:" + reset_color)
        gotoxy(80, 6)
        print("1) Cliente Regular")
        gotoxy(80, 7)
        print("2) Cliente VIP")
        gotoxy(2, 8)
        print( green_color+ "=" * 180 +reset_color )
        gotoxy(2,9)
        costumer_type = input(blue_color +"Seleccione una opción: "+ reset_color)

        if costumer_type == "1":
            gotoxy(2,11)
            print("CLIENTE REGULAR")
            gotoxy(2,12)
            name = Valida.validar_letras2( "Ingrese el nombre del cliente:")
            # gotoxy(2,13)
            last_name = Valida.validar_letras2(" Ingrese el apellido del cliente:")
            # gotoxy(2,14)
            dni = Valida.validar_dni(" Ingrese el DNI del cliente:")
            # gotoxy(2,15)
            card = Valida.validar_letras2(" Cliente tiene tarjeta de descuento? (s/n): ").lower() == "s"
            new_client = RegularClient(name, last_name, dni, card)
        elif costumer_type == "2":
            gotoxy(2,11)
            print("CLIENTE VIP")
            gotoxy(2,12)
            name = Valida.validar_letras2(" Ingrese el nombre del cliente:")
            # gotoxy(2,13)
            last_name = Valida.validar_letras2(" Ingrese el apellido del cliente:")
            # gotoxy(2,14)
            dni = Valida.validar_dni(' Ingrese el DNI del cliente:')
            new_client = VipClient(name, last_name, dni)
        else:
            # gotoxy(25,9)
            print(red_color + " Opción inválida")
            return

        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.read() #1. Los carga para poder maqnipularlos"
        clients.append(new_client.getJson()) #Luego se agrega a la lista de diccionarios como un dicionario con getJson
        json_file.save(clients) #Finalmente se guarda como Save
        gotoxy(75,17)
        print("Cliente registrado exitosamente!")
        time.sleep(5)

    def update(self):  # hecho
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print(green_color + "=" * 180 + reset_color)
        gotoxy(80, 2)
        print("ACTUALIZAR CLIENTE")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print(green_color + "=" * 180 + reset_color)
        gotoxy(2, 6)
        dni = Valida.validar_dni("Ingrese el DNI del cliente que desea actualizar:")
        gotoxy(2, 8)
        print(green_color + "=" * 180 + reset_color)

        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.read()

        found = False
        updated_clients = []

        def handle_option():
            nonlocal found
            nonlocal client

            #MÉTODO RECURSIVO
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                new_nombre = Valida.validar_letras2(purple_color + " Ingrese el nuevo nombre del cliente: " + blue_color)
                if new_nombre.strip():
                    client['nombre'] = new_nombre.strip()
            elif opcion == "2":
                new_apellido = Valida.validar_letras2(purple_color + " Ingrese el nuevo apellido del cliente: " + blue_color)
                if new_apellido.strip():
                    client['apellido'] = new_apellido.strip()
            elif opcion == "3":
                gotoxy(80,15)
                print("Ha decidido salir, bye")
                return  # Salir de la función handle_option
            else:
                print(" Opción inválida.")
                handle_option()  # Llamada recursiva

        for client in clients:
            if client['dni'] == dni:
                found = True
                gotoxy(2, 10)
                print("CLIENTE ENCONTRADO:")
                gotoxy(2, 12)
                print(blue_color + "Nombre        Apellido        DNI")
                gotoxy(2, 13)
                print(purple_color + f"{client['nombre']}")
                gotoxy(16, 13)
                print(purple_color + f"{client['apellido']}")
                gotoxy(32, 13)
                print(purple_color + f"{client['dni']}")
                gotoxy(2, 15)
                print(green_color + "=" * 180 + reset_color)
                gotoxy(2, 17)
                print("Opciones:")
                gotoxy(2, 18)
                print('1) Cambiar nombre')
                gotoxy(2, 19)
                print('2) Cambiar apellido')
                gotoxy(2, 20)

                gotoxy(2, 22)
                handle_option()  # Llamada inicial a la función recursiva

            updated_clients.append(client)

        if found:
            json_file.save(updated_clients)
            gotoxy(70, 26)
            print("Cliente actualizado exitosamente!")
        else:
            gotoxy(80, 6)
            print("Cliente no encontrado.")
        time.sleep(5)

    def delete(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print( green_color+ "=" * 180 +reset_color )
        gotoxy(80, 2)
        print("ELIMINAR CLIENTE")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print( green_color+ "=" * 180 +reset_color )
        gotoxy(2, 6)
        dni = Valida.validar_dni('Ingrese el DNI del cliente que desea eliminar:')
        gotoxy(2, 8)
        print( green_color+ "=" * 180 +reset_color )
        
        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.read()
        
        for client in clients:
            if client['dni'] == dni:
                gotoxy(2,11)
                print(blue_color + "Nombre        Apellido        DNI")
                gotoxy(2, 12)
                print(purple_color + f"{client['nombre']}")
                gotoxy(16, 12)
                print(purple_color + f"{client['apellido']}")
                gotoxy(32, 12)
                print(purple_color + f"{client['dni']}")
                gotoxy(2, 14)
                print( green_color+ "=" * 180 +reset_color )
                
        
        filtered_clients = [client for client in clients if client['dni'] != dni]

        if len(filtered_clients) < len(clients):
            json_file.save(filtered_clients)
            gotoxy(73,20)
            print("Cliente eliminado exitosamente!")
        else:
            print("Cliente no encontrado.")
        time.sleep(5)

    def consult(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print(green_color + "=" * 180 + reset_color)
        gotoxy(80, 2)
        print("CONSULTAR CLIENTE")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print(green_color + "=" * 180 + reset_color)
        
        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.read()
   
        gotoxy(70, 6)
        print(blue_color + "Nombre       Apellido     DNI")
        
       
        for i, client in enumerate(clients):
            gotoxy(70, 7 + i)
            print(purple_color + f"{client['nombre']: <12} {client['apellido']: <12} {client['dni']}")
        
        
        gotoxy(2, 8 + len(clients))
        print(green_color + "=" * 180 + reset_color)

        gotoxy(2, 10 + len(clients))
        dni = Valida.validar_dni('Ingrese el DNI del cliente que desea consultar:')
        
        gotoxy(70, 26)
        print(blue_color + "Nombre       Apellido     DNI")
        
        for client in clients:
            if client['dni'] == dni:
                gotoxy(70, 27)
                print(purple_color + f"{client['nombre']}")
                gotoxy(83, 27)
                print(purple_color + f"{client['apellido']}")
                gotoxy(96, 27)
                print(purple_color + f"{client['dni']}")
                
            
        if client['dni'] is None:
            gotoxy(32, 29)
            print('Cliente no encontrado') 
     
        
class CrudProducts(ICrud):
    def create(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print(green_color + "=" * 180 + reset_color)
        gotoxy(80, 2)
        print("REGISTRAR PRODUCTO")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print(green_color + "=" * 180 + reset_color)
        
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()
        
        # gotoxy(2, 6)
        descrip = Valida.validar_letras2("  Ingrese la descripción del producto: ")
        # gotoxy(2, 8)
        # print(green_color + "=" * 180 + reset_color)
        
        existing_product = next((product for product in products if product['descripcion'].lower() == descrip.lower()), None)

        if existing_product:
            gotoxy(80, 15)
            print(red_color + "¡EL PRODUCTO YA EXISTE!")
            gotoxy(65, 17)
            print(blue_color + "ID          Descripción          Precio          Stock")
            gotoxy(65, 18); print(purple_color + str(existing_product['id']))
            gotoxy(79, 18); print(purple_color + existing_product['descripcion'])
            gotoxy(98, 18); print(purple_color + str(existing_product['precio']))
            gotoxy(114, 18); print(purple_color + str(existing_product['stock']) + reset_color)
        else:
            # gotoxy(2, 10)
            preci = Valida.validar_numeros_decimales("  Ingrese el precio del producto: ")
            # gotoxy(2, 11)
            stock = int(Valida.validar_numeros("  Ingrese el stock del producto: "))
            gotoxy(2, 12)
            new_product = Product(descrip=descrip, preci=preci, stock=stock)
            products.append(new_product.getJson())
            json_file.save(products)
            
            # Actualizar el contador de IDs
            Product.update_next_id(products)

            gotoxy(75, 17)
            print(reset_color + "Producto registrado exitosamente!")
        
        time.sleep(2)

    def update(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print( green_color + "=" * 180 + reset_color )
        gotoxy(80, 2)
        print("ACTUALIZAR PRODUCTO")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print( green_color + "=" * 180 + reset_color )
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()
        
        if products:
            gotoxy(2, 6)
            search_term = Valida.validar_letras2("Ingrese la descripción del producto que desea actualizar: ").strip()
            found_product = None
            for product in products:
                if search_term.lower() in product['descripcion'].lower():
                    found_product = product
                    break
                
        gotoxy(2, 8)
        print( green_color + "=" * 180 + reset_color )
        

        if found_product:
            gotoxy(2,10)
            print("Producto encontrado:")
            gotoxy(2,12)
            print(blue_color + "ID         Descripción         Precio         Stock" + reset_color)
            gotoxy(2,13);print(purple_color + str(found_product['id']))
            gotoxy(13,13);print(purple_color + found_product['descripcion'])
            gotoxy(34,13);print(purple_color + str(found_product['precio']))
            gotoxy(50,13);print(purple_color + str(found_product['stock']) + reset_color)      
            gotoxy(2, 15)
            print("Opciones:" )
            gotoxy(2, 16) 
            print('1) Cambiar Descripción' )
            gotoxy(2, 17) 
            print('2) Cambiar Precio ')
            gotoxy(2, 18)  
            print('3) Cambiar y Stock')
            gotoxy(2, 19) 
            print('4) Guardar y salir')            
            while True:
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    new_descripcion = Valida.validar_letras2("Ingrese la nueva descripción: ")
                    if new_descripcion.strip():
                        found_product['descripcion'] = new_descripcion.strip()
                elif opcion == "2":
                    new_precio = Valida.validar_letras2("Ingresa el nuevo precio: ")
                    if new_precio.strip():
                        found_product['precio'] = new_precio.strip()
                elif opcion == "3":
                    new_stock = Valida.validar_numeros("Ingresa el nuevo stock: ")
                    if new_stock.strip():
                        found_product['stock'] = new_stock.strip() 
                elif opcion == "4":
                    json_file.save(products)
                    break  # Salir del bucle interno
                else:
                    print("Opción inválida.")

            else:  # Se ejecuta si el bucle interno termina sin break
                print("Producto no encontrado.")

        # Para indicar cuando no hay productos registrados.
        if not products:
            print("No hay productos registrados.")
    
    def delete(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print(green_color + "=" * 180 + reset_color)
        gotoxy(80, 2)
        print("ELIMINAR PRODUCTO")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print(green_color + "=" * 180 + reset_color)
        gotoxy(2, 6)
        descripcion = Valida.validar_letras2('Ingrese el producto que desea eliminar:').lower()
        gotoxy(2, 8)
        print(green_color + "=" * 180 + reset_color)
        
        
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()

        found_product = None
        for product in products:
            if product['descripcion'].lower() == descripcion:
                found_product = product
                break

        if found_product:
            gotoxy(2, 8)
            print(green_color + "=" * 90)
            gotoxy(2, 9)
            print(blue_color + "Producto a eliminar:")
            gotoxy(2, 10)
            print(blue_color + f"ID: {purple_color}{found_product['id']}{blue_color}, Descripción: {purple_color}{found_product['descripcion']}{blue_color}, Precio: {purple_color}{found_product['precio']}{blue_color}, Stock: {purple_color}{found_product['stock']}")
            confirmacion = Valida.validar_letras2(purple_color + "¿Está seguro de que desea eliminar este producto? (s/n): ").lower()
            if confirmacion == 's':
                products.remove(found_product)  # Eliminar el producto de la lista
                json_file.save(products)  # Guardar la lista actualizada en el archivo JSON
                gotoxy(2, 12)
                print(green_color + "=" * 180 + reset_color)
                gotoxy(2, 13)
                print(blue_color + "Producto eliminado exitosamente!")
            else:
                gotoxy(2, 12)
                print(green_color + "=" * 90)
                gotoxy(2, 13)
                print(blue_color + "Eliminación cancelada.")
        else:
            gotoxy(2, 8)
            print(green_color + "=" * 90)
            gotoxy(2, 9)
            print(blue_color + "Producto no encontrado.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print(green_color + "=" * 180 + reset_color)
        gotoxy(80, 2)
        print("CONSULTA DE PRODUCTO")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print(green_color + "=" * 180 + reset_color)

        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()

        gotoxy(70, 6)
        print(blue_color + "ID         Descripción     Precio       Stock")

        if products:
            precios = [product['precio'] for product in products]

            # Calcular el producto con el mayor y menor costo
            mayor_costo = max(products, key=lambda x: x['precio'])
            menor_costo = min(products, key=lambda x: x['precio'])
            costo_total = sum(precios)

            for i, product in enumerate(products):
                gotoxy(70, 7 + i)
                print(purple_color + f"{product['id']}")
                gotoxy(83, 7 + i)
                print(purple_color + f"{product['descripcion']}")
                gotoxy(98, 7 + i)
                print(purple_color + f"{product['precio']}")
                gotoxy(110, 7 + i)
                print(purple_color + f"{product['stock']}")

            search_term = Valida.validar_letras2("\nIngrese la descripción del producto que desea buscar: ").strip()

            found_products = [product for product in products if search_term.lower() in product['descripcion'].lower()]

            if found_products:
                # posiciones de impresión cada producto encontrado 
                for i, product in enumerate(found_products):
                    gotoxy(70, 8 + len(products) + i)
                    print(reset_color + f"{product['id']}")
                    gotoxy(83, 8 + len(products) + i)
                    print(reset_color +  f"{product['descripcion']}")
                    gotoxy(98, 8 + len(products) + i)
                    print(reset_color +  f"{product['precio']}")
                    gotoxy(110, 8 + len(products) + i)
                    print(reset_color + f"{product['stock']}")
            else:
                gotoxy(70, 8 + len(products))
                print("Producto no encontrado.")
        else:
            gotoxy(70, 7)
            print("No hay productos registrados.")

        # Imprimir información sobre el producto con mayor costo, menor costo y costo total debajo de la lista de productos
        gotoxy(70, 10 + len(products) + len(found_products))
        print(red_color + f"Producto con mayor costo: {mayor_costo['descripcion']} / Precio: {mayor_costo['precio']}")
        gotoxy(70, 12 + len(products) + len(found_products))
        print(red_color + f"Producto con menor costo: {menor_costo['descripcion']} / Precio: {menor_costo['precio']}")
        gotoxy(70, 14 + len(products) + len(found_products))
        print(red_color + f"Costo total de todos los productos: {costo_total}")

        # Imprimir línea de separación al final
        # gotoxy(2, 16 + len(products) + len(found_products))
        print(green_color + "=" * 180 + reset_color)
        input("Presione una tecla para continuar...")

      
class CrudSales(ICrud):#hecho
    def create(self):#hecho
        validar = Valida()
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        gotoxy(23,6)
        dni=validar.solo_numeros("Error: Solo numeros")
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe");time.sleep(5)
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True)
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(green_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line);
            id=int(validar.solo_numeros("Error: Solo numeros"))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print("Producto no existe")
                time.sleep(5)
                gotoxy(24,9+line);print(" "*20)
            else:
                prods = prods[0]
                product = Product(descrip=prods["descripcion"], preci=prods["precio"], stock=prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros"))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ult_invoices = invoices[-1]["factura"]+1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print("🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(2)    
    
    def consult(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        
        gotoxy(130,2);print(blue_color+"REGISTRO DE VENTAS")
        gotoxy(115,3);print(blue_color+Company.get_business_name())
        
        gotoxy(30,2);print(blue_color+"CONSULTA DE FACTURAS POR NÚMERO")
        print()
        
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoices = json_file.read()

        # Imprimir todas las facturas en el lado derecho
        gotoxy(135,4)
        print(reset_color + "FACTURAS")
        inicio_fila = 6
        for invoice in invoices:
            gotoxy(130, inicio_fila); print(reset_color + "Factura:", invoice["factura"])
            gotoxy(130, inicio_fila+1); print(reset_color +"Fecha:", invoice["Fecha"])
            gotoxy(130, inicio_fila+2); print(reset_color +"Cliente:",invoice["cliente"])
            inicio_fila += 4

        # Calculo de factura con el mayor total, la factura con el menor total y la suma de todos los totales
        mayor_total = menor_total = None
        total_sum = 0  # Inicializar total_sum como 0
        for invoice in invoices:
            total = invoice["total"]
            total_sum += total
            if mayor_total is None or total > mayor_total["total"]:
                mayor_total = invoice
            if menor_total is None or total < menor_total["total"]:
                menor_total = invoice

        gotoxy(115, inicio_fila - 1)  # Posicionarse antes de las facturas
        print("=" * 50) 

        # Mostrar la facturamayor total
        gotoxy(130, inicio_fila+4)
        print(red_color + "Factura con mayor total:")
        gotoxy(130, inicio_fila+5)
        print(red_color + "Número de Factura:", mayor_total["factura"])
        gotoxy(130, inicio_fila+6)
        print("Total:", mayor_total["total"])

        # Mostrar la factura menor total
        gotoxy(130, inicio_fila+8)
        print(red_color + "Factura con menor total:")
        gotoxy(130, inicio_fila+9)
        print(red_color + "Número de Factura:", menor_total["factura"])
        gotoxy(130, inicio_fila+10)
        print("Total:", menor_total["total"])

        # Mostrar la suma de todos los totales
        gotoxy(130, inicio_fila+12)
        print(red_color + "Suma de todos los totales:", total_sum)

        gotoxy(20,4)
        factura_num = int(input("Ingrese el número de factura para ver el detalle: "))

        gotoxy(19,5)
        print(reset_color+ "=" * 52) 

        found_invoice = None
        for invoice in invoices:
            if invoice["factura"] == factura_num:
                found_invoice = invoice
                break

        if found_invoice:            
            # Factura en el lado izquierdo
            gotoxy(20,7)
            print("Detalle de la factura")
            gotoxy(20, 8); print(purple_color + "Número de Factura:" + reset_color, found_invoice["factura"])
            gotoxy(20, 9); print(purple_color + "Fecha:" + reset_color, found_invoice["Fecha"])
            gotoxy(20, 10); print(purple_color + "Cliente:" + reset_color, found_invoice["cliente"])
            gotoxy(20, 11); print(purple_color + "Subtotal:" + reset_color, found_invoice["subtotal"])
            gotoxy(20, 12); print(purple_color + "Descuento:" + reset_color, found_invoice["descuento"])
            gotoxy(20, 13); print(purple_color + "IVA:" + reset_color, found_invoice["iva"])
            gotoxy(20, 14); print(purple_color + "Total:" + reset_color, found_invoice["total"])
            gotoxy(20, 15); print(purple_color + "Detalle:" + reset_color)
            detalle_linea = 14
            for detalle in found_invoice["detalle"]:
                gotoxy(23, detalle_linea+2); print("  " + purple_color + "Producto:" + reset_color, detalle["producto"])
                gotoxy(23, detalle_linea+3); print("  " + purple_color + "Precio:" + reset_color, detalle["precio"])
                gotoxy(23, detalle_linea+4); print("  " + purple_color + "Cantidad:" + reset_color, detalle["cantidad"])
                detalle_linea += 4
        else:
            print("No se encontró la factura con el número proporcionado.")

        input("Presione enter para continuar...")

    def update(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        
        gotoxy(2, 1)
        print( green_color + "=" * 180 + reset_color )
        gotoxy(80, 2)
        print("ACTUALIZAR FACTURA")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print( green_color + "=" * 180 + reset_color )
        gotoxy(2, 5)
        factura_numero = int(Valida.validar_numeros("Ingrese el número de factura que desea actualizar: "))

        json_file_invoices = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file_invoices.read()

        json_file_products = JsonFile(path + '/archivos/products.json')
        products = json_file_products.read()
        gotoxy(2, 6)
        for factura in invoices:
            if factura["factura"] == factura_numero:
                gotoxy(5, 7)
                print(red_color + "Factura encontrada")
                gotoxy(5, 8)
                print(purple_color + "Número de Factura:" + blue_color, factura["factura"] )
                gotoxy(5, 9)
                print(purple_color + "Fecha:"+ blue_color, factura["Fecha"])
                gotoxy(5, 10)
                print(purple_color + "Cliente:"+ blue_color, factura["cliente"])
                gotoxy(5, 11)
                print(purple_color + "Subtotal:"+ blue_color, factura["subtotal"])
                gotoxy(5, 12)
                print(purple_color + "Descuento:"+ blue_color, factura["descuento"])
                gotoxy(5, 13)
                print(purple_color + "IVA:"+ blue_color, factura["iva"])
                gotoxy(5, 14)
                print(purple_color + "Total:"+ blue_color, factura["total"])
                gotoxy(5, 15)
                print(purple_color + "Detalle:")

                detalle_linea = 14
                for detalle in factura["detalle"]:
                    gotoxy(8, detalle_linea+2)
                    print("  Producto:", detalle["producto"])
                    gotoxy(8, detalle_linea + 3)
                    print("  Precio:", detalle["precio"])
                    gotoxy(8, detalle_linea + 4)
                    print("  Cantidad:", detalle["cantidad"])
                    detalle_linea += 4  
                
                print(reset_color + "\n¿Qué desea hacer?")
                print("1) Agregar    2) Eliminar    3) Actualizar    4) Salir")
                
                while True:

                    opcion = str(Valida.validar_numeros("Ingrese el número de la opción que desea realizar: "))

                    if opcion == "1":
                        producto = Valida.validar_letras2("Ingrese el nombre del producto que desea agregar: ")
                        precio_producto = None
                        for prod in products:
                            if prod["descripcion"] == producto:
                                precio_producto = prod["precio"]
                                break
                        if precio_producto is not None:
                            cantidad =int(Valida.validar_numeros("Ingrese la cantidad del producto que desea agregar: "))
                            factura["detalle"].append({"producto": producto, "precio": precio_producto, "cantidad": cantidad})
                            factura["subtotal"] += precio_producto * cantidad
                            factura["total"] = factura["subtotal"] - factura["descuento"] + factura["iva"]
                            
                            print("Detalle actualizado.")
                        else:
                            
                            print("El producto no está en la lista de productos.")
                    elif opcion == "2":
                        producto = Valida.validar_letras2("Ingrese el nombre del producto que desea eliminar: ")
                        for item in factura["detalle"]:
                            if item["producto"] == producto:
                                factura["subtotal"] -= item["precio"] * item["cantidad"]
                                factura["total"] = factura["subtotal"] - factura["descuento"] + factura["iva"]
                                factura["detalle"].remove(item)
                                
                                print("Detalle actualizado.")
                                break
                        else:
                           
                            print("El producto no está en la factura.")
                    elif opcion == "3":
                        producto = Valida.validar_letras2("Ingrese el nombre del producto que desea actualizar: ")
                        cantidad_nueva = int(Valida.validar_numeros("Ingrese la nueva cantidad del producto: "))
                        for item in factura["detalle"]:
                            if item["producto"] == producto:
                                factura["subtotal"] -= item["precio"] * item["cantidad"]
                                item["cantidad"] = cantidad_nueva
                                factura["subtotal"] += item["precio"] * cantidad_nueva
                                factura["total"] = factura["subtotal"] - factura["descuento"] + factura["iva"]
                                
                                print("Detalle actualizado.")
                                break
                        else:
                            
                            print("El producto no está en la factura.")
                    elif opcion == "4":
                        # Salir del menú
                        break
                    else:
                        print("Opción no válida. Por favor, ingrese un número válido.")

                json_file_invoices.save(invoices)
                print("¡Factura actualizada exitosamente!")
                return

        print("Factura no encontrada.")

    def delete(self):#hecho
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(2, 1)
        print( green_color + "=" * 180 + reset_color )
        gotoxy(30, 2)
        print(blue_color + "ELIMINAR VENTA")
        gotoxy(65, 3)
        print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        gotoxy(2, 4)
        print( green_color + "=" * 180 + reset_color )
        gotoxy(17, 5)
        print(blue_color + Company.get_business_name())
        invoice_number = Valida.validar_numeros("Ingrese el número de factura que desea eliminar: ")
        json_file = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file.read()

        # Buscar la factura específica
        found = False
        updated_invoices = []
        for invoice in invoices:
            if invoice["factura"] == int(invoice_number):
                found = True
                # Mostrar la factura antes de eliminarla
                print(f"Factura encontrada:")
                print(f"Número de Factura: {invoice['factura']}")
                print(f"Fecha: {invoice['Fecha']}")
                print(f"Cliente: {invoice['cliente']}")
                print(f"Total: {invoice['total']}")
                print("\nDetalle de la Venta:")
                for detalle in invoice['detalle']:
                    print(f"{detalle['producto']}: {detalle['cantidad']} x {detalle['precio']}")
                print(green_color + "=" * 90 + reset_color)

                # Confirmar la eliminación
                confirmacion = Valida.validar_letras2("¿Está seguro que desea eliminar esta factura? (s/n): ").lower()
                if confirmacion == "s":
                    print("Factura eliminada exitosamente.")
                else:
                    print("Eliminación cancelada.")
            else:
                updated_invoices.append(invoice)

        if found:
            # Guardar las facturas actualizadas en el archivo JSON
            json_file.save(updated_invoices)
        else:
            print("Factura no encontrada.")


       
    #Menu Proceso Principal

opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu(red_color + "Menu Facturacion" + reset_color,["1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()    
            menu_clients = Menu(blue_color + "Menu Cientes" + reset_color,["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                crud_clients = CrudClients()
                crud_clients.create()
            elif opc1 == "2":
                crud_clients = CrudClients()
                crud_clients.update()
            elif opc1 == "3":
                crud_clients = CrudClients()
                crud_clients.delete()
            elif opc1 == "4":
                crud_clients = CrudClients()
                crud_clients.consult()
            print("  Regresando al menu Clientes...")
            time.sleep(5)       
                 
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()    
            menu_products = Menu(blue_color + "Menu Productos"+ reset_color,["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                crud_products = CrudProducts()
                crud_products.create()
                pass
            elif opc2 == "2":
                crud_products = CrudProducts()
                crud_products.update()
                
            elif opc2 == "3":
                crud_products = CrudProducts()
                crud_products.delete()
                
            elif opc2 == "4":
                crud_products = CrudProducts()
                crud_products.consult()
                
                
            print("  Regresando al menu Clientes...")
            time.sleep(5)           
            
    elif opc == "3":
        opc3 = ''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu(blue_color+"Menu Ventas"+ reset_color,["1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
                
            elif opc3 == "2":
                sales.consult()
                
            elif opc3 == "3":
                sales.update()
                
            elif opc3 == "4":
                sales.delete()
                
            print("  Regresando al menu Clientes...")
            time.sleep(3)     

    
                
     
    print("Regresando al menu Principal...")
    # time.sleep(2)            

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()
