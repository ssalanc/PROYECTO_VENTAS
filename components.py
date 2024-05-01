from utilities import borrarPantalla, gotoxy
from utilities import reset_color, red_color, green_color, yellow_color, blue_color, purple_color, cyan_color
import time

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil)
            print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input(f"Elija opcion[1...{len(self.opciones)}]: ") 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError):
        while True:           
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                print(mensajeError)
                time.sleep(1)
                
        return valor

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    
    def validar_letras(frase):
        while True:
            print(f"{frase}")
            nombre = input(blue_color)
            if nombre.isalpha():
                return nombre.capitalize()
            else:
                print(red_color+ "El campo solo puede contener letras.")
                time.sleep(1)
                print(" "*40)
        
        
                
    def validar_dni(mensaje):
        while True:
            dni = input(purple_color + f"{mensaje}" + blue_color)
            if len(dni) < 10:
                print(purple_color + " El DNI debe tener al menos 10 caracteres.")
                dni = input(purple_color + " Ingrese el DNI del cliente: " + blue_color)
            else:
                if dni.isdigit():
                    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
                    suma = 0
                    for i in range(9):
                        digito = int(dni[i]) * coeficientes[i]
                        if digito > 9:
                            digito -= 9
                        suma += digito
                    total = suma % 10
                    if total != 0:
                        total = 10 - total
                    else:
                        total = 0  # Valor predeterminado si total == 0
                    if total == int(dni[9]):
                        return dni
                print(red_color + " El formato del DNI es incorrecto.")
                dni = input(purple_color + " Ingrese el DNI del cliente: "+ blue_color)
                
                
                
    def validar_letras2(frase):
        while True:
            nombre = input(purple_color + f"{frase}" + blue_color)
            if nombre.replace(' ', '').isalpha() or nombre.strip() == "":
                return nombre
            else:
                print(red_color + "El campo solo puede contener letras.")

    
    def validar_numeros(frase):
        while True:
            numero = input(purple_color + f"{frase}" + blue_color)
            if numero.isdigit():
                return numero
            else:
                print(red_color + " El campo solo puede contener números.")
    
    
    def validar_numeros_decimales(frase):
        while True:
            numero = input(purple_color + f"{frase}" + blue_color)
            try:
                numero = float(numero)
                return numero
            except ValueError:
                print(red_color+"El campo debe ser un número decimal.")


