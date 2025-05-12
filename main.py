import os
import random
from ruleta import apostar_color, apostar_paridad, apostar_por_numeros, apostar_docena
from blackjack import blackjack




class Usuario:
    def __init__(self, dni, nickname, contraseña, disponible = 0):
        self.dni = dni
        self.nickname = nickname
        self.contraseña =contraseña
        self.disponible = disponible

    def mostrar_informacion(self):
        print("SU CUENTA:")
        print(f"DNI - {self.dni}")
        print(f"Nombre de Usuario - {self.nickname}")
        print(f"Dinero Disponible - {self.disponible}")
        print("")
        input("Pulse ENTER para continuar")
        os.system("cls")

    def añadir_dinero(self, dinero):
        self.disponible += dinero
        print("")
        print(f"Se han añadido {dinero}€ correctamente.")
        print("")
        input("Pulse ENTER para continuar")
        os.system("cls")

    def retirar_dinero(self, dinero):
        if self.disponible > dinero:
            self.disponible -= dinero
            print("")
            print(f"Se han retirado {dinero}€ correctamente.")
            input()
            os.system("cls")
        else:
            print("No tienes suficiente cantidad de dinero.")
            input()
            os.system("cls")

        print("")
        input("Pulse ENTER para continuar")
        os.system("cls")


class Casino:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, dni, nickname, contraseña):
        if dni not in self.usuarios:
            self.usuarios[dni] = Usuario(dni, nickname, contraseña)
            print("Tu cuenta ha sido creada con éxito.")
        else:
            print("Este DNI tiene una cuenta ya creada.")
        print("")
        input("Pulse ENTER para continuar")
        os.system("cls")

    def verificar_dni(self, dni):
        
        while True:
            if len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha():
                return dni
            else:
                print("Introduce el DNI correctamente (8 números seguidos de una letra).")
                dni = input("Introduzca su DNI por favor: ")


    def menu(self):
       
        print("LA GLOTONA")
        print("")
        print("Bienvenido a la mejor casa de apuestas online.")
        print("Primeramente, deberá registrarse.")
        print("")
        dni = input("Introduzca su DNI por favor: ")
        dni = self.verificar_dni(dni)
        nickname = input("Crea un nombre de usuario: ")
        contraseña = input("Crea una contraseña: ")
        self.registrar_usuario(dni, nickname, contraseña)


        while True:
            print("LA GLOTONA - Menú Principal")
            print("1. RULETA")
            print("2. BLACKJACK")
            print("3. CUENTA")
            print("0. SALIR")

            opcion_menu = int(input("Seleccione una opción: "))
            os.system("cls")
            
            if opcion_menu == 1:
                
                while True:
                    print("--- RULETA ---")
                    print("1. Apostar por color")
                    print("2. Apostar por paridad")
                    print("3. Apostar por número")
                    print("4. Apostar por docena")
                    print("5. Volver al menú principal")
                    opcion_ruleta = input("Elige una opción: ")
                    os.system("cls")

                    # Dentro de la opción RULETA:
                    if opcion_ruleta == "1":
                        apostar_color(self.usuarios[dni])
                    elif opcion_ruleta == "2":
                        apostar_paridad(self.usuarios[dni])
                    elif opcion_ruleta == "3":
                        apostar_por_numeros(self.usuarios[dni])
                    elif opcion_ruleta == "4":
                        apostar_docena(self.usuarios[dni])

                    elif opcion_ruleta == "5":
                        break
                    else:
                        print("Opción inválida.")
                        input()
                        os.system("cls")

                
            if opcion_menu == 2:
                print("BLACKJACK")
                blackjack(self.usuarios[dni])
                
            if opcion_menu == 3:
                print("Introduzca su contraseña para continuar, por favor: ")
                contraseña_verificacion = input()
                print("")
                
                if contraseña_verificacion == self.usuarios[dni].contraseña:
                    input("Contraseña correcta, pulse ENTER.")
                    os.system("cls")
                    print("1. Ver información de la cuenta")
                    print("2. Añadir dinero")
                    print("3. Retirar dinero")
                    print("4. Salir")
                    opcion = int(input("Seleccione una opción: "))
                    
                    os.system("cls")
                    if opcion == 1:
                        self.usuarios[dni].mostrar_informacion()

                    elif opcion == 2:
                    
                        try:
                            cantidad = float(input("¿Cuánto desea añadir? "))
                            self.usuarios[dni].añadir_dinero(cantidad)
                        except ValueError:
                            print("Error: debe ingresar un número válido.")
                            input("Pulse ENTER para continuar")
                            os.system("cls")
                    

                    elif opcion == 3:
                        try:
                            cantidad = float(input("¿Cuánto desea retirar? "))
                            self.usuarios[dni].retirar_dinero(cantidad)

                        except ValueError:
                            print("Error: debe ingresar un número válido.")
                            input("Pulse ENTER para continuar")
                            os.system("cls")
                else:
                    print("Credenciales erróneas, inténtelo de nuevo.")
                    input()
                    os.system("cls")

            elif opcion_menu == 0:
                        print("Gracias por visitar LA GLOTONA. ¡Hasta pronto!")
                        input()
                        break

            else:
                print("Opción inválida.")
                input("Pulse ENTER para continuar")
                os.system("cls")



    
casinote = Casino()
casinote.menu()
