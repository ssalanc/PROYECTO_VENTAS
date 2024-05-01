[
  { "id": 1, "descripcion": "mortadela", "precio": 0.6, "stock": 100 },
  { "id": 2, "descripcion": "aceite", "precio": 2.0, "stock": 300 },
  { "id": 3, "descripcion": "Coca Cola", "precio": 1.5, "stock": 60 },
  { "id": 1, "descripcion": "tomates", "precio": 2.0, "stock": 400 },
  { "id": 1, "descripcion": "zandia", "precio": 10.0, "stock": 40 }
]

# #ESTA ES LA VALIDACION DE JORDY DEL DNI
# def validar_dni(mensaje):
#     while True:
#         print(blue_color + f"{mensaje}")
#         cedula = input(purple_color)
        
#         if len(cedula) == 10 and cedula.isdigit():
#             coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
#             suma = 0
            
#             for i in range(9):
#                 digito = int(cedula[i]) * coeficientes[i]
#                 if digito > 9:
#                     digito -= 9
#                 suma += digito
            
#             total = suma % 10
#             if total != 0:
#                 total = 10 - total
            
#             # Verifica si el dígito de control es igual al último dígito del DNI
#             if total == int(cedula[9]):
#                 return cedula
        
#         print(purple_color + "El formato del DNI es incorrecto.")
      








        
    #LO QUE HICE ARRIBA PENSANDO QUE ERA CREATE PERO HICE UPDATE
        # borrarPantalla()
        # dibujar_cuadro()
        # gotoxy(2, 1)
        # print(green_color + "=" * 180 + reset_color)
        # gotoxy(80, 2)
        # print("CONSULTAR CLIENTE")
        # gotoxy(65, 3)
        # print(blue_color + "Empresa: Corporación el Rosado    RUC: 0876543294001")
        # gotoxy(2, 4)
        # print(green_color + "=" * 180 + reset_color)
        # gotoxy(2, 6)
        # descrip = Valida.validar_letras2("Ingrese la descripción del producto: ")
        
        # json_file = JsonFile(path + '/archivos/clients.json')
        # products = json_file.read()
        
        # existing_product = next((product for product in products if product['descripcion'] == descrip), None)
        
        # if existing_product:
        #     print(red_color + "El producto ya existe:")
        #     gotoxy(1,9)
        #     print(blue_color + "ID          Descripción          Precio          Stock")
        #     gotoxy(1,10);print(existing_product['id'])
        #     gotoxy(13,10);print(purple_color + existing_product['descripcion'])
        #     gotoxy(34,10);print(purple_color + str(existing_product['precio']))
        #     gotoxy(50,10);print(purple_color + str(existing_product['stock']) + reset_color)              
            
        # else:
        #     preci = Valida.validar_numeros_decimales(" Ingrese el precio del producto: ")
        #     stock = int(Valida.validar_numeros(" Ingrese el stock del producto: "))
        #     new_product = Product(descrip=descrip, preci=preci, stock=stock)
        #     products.append(new_product.getJson())
        #     json_file.save(products)
        #     gotoxy(32,15 )
        #     print("Producto registrado exitosamente!")
        
        # time.sleep(2) 
        
        
#tenerlos pra registrarlo con la validcion del dni
        
#   {
#     "dni": "0914192144",
#     "nombre": "Dayanna",
#     "apellido": "Vera",
#     "valor": 10000
#   },
#   {
#     "dni": "0939833680",
#     "nombre": "Sandra",
#     "apellido": "Salan",
#     "valor": 10000
#   },
#   {
#     "dni": "0920689302",
#     "nombre": "Sandra ",
#     "apellido": "Calderon",
#     "valor": 0.1
#   },
#   {
#     "dni": "0978945612",
#     "nombre": "Mayra",
#     "apellido": "Tomala",
#     "valor": 0.1
#   },
#   {
#     "dni": "0955578494",
#     "nombre": "Ariana",
#     "apellido": "Aguilar",
#     "valor": 0.1
#   },
#   {
#     "dni": "0930210578",
#     "nombre": "Cesar",
#     "apellido": "Calderon",
#     "valor": 0.1
#   },
#   {
#     "dni": "0973916482",
#     "nombre": "Pilar",
#     "apellido": "Calderonn",
#     "valor": 10000
#   },
#   {
#     "dni": "0955573000",
#     "nombre": "Nayeli",
#     "apellido": "Alvarado",
#     "valor": 0
#   },
#   {
#     "dni": "0989562321",
#     "nombre": "Willian",
#     "apellido": "Naranjo",
#     "valor": 0.1
#   }
#   { "dni": "0913204781", "nombre": "Luis", "apellido": "Salan", "valor": 0.1 },
#   { "dni": "0987451234", "nombre": "ecc", "apellido": "efrvae", "valor": 0.1 },
#   {
#     "dni": "0955571542",
#     "nombre": "Leonelita",
#     "apellido": "Calderon",
#     "valor": 0.1
#   },
        



