from colorama import Fore, Back, Style
import platform
import numpy as np
import os

parametros = [0,0,0,0]
matrizP = np.zeros((5,5),dtype=float)
Pi0 = np.zeros(5, dtype=float)
pt = platform.system()
ver = 0

def ValidacionEntero(x):#______________________________________________________V1
    if x.isdigit():
        return True
    else:
        print("Debe ser un numero entero, prueba nuevamente...")
        return False
    
def ValidacionFloat(x):#______________________________________________________V2
    try:
        float(x)
        return True
    except ValueError:
        print("Caracter no valido, prueba nuevamente...")
        return False

def ValidacionVPI0():#______________________________________________________V3
    if np.sum(Pi0)!=1:
        return False
    else:
        return True
    

def LimpiarPantalla():#______________________________________________________F0
    if pt == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    
def MenuPrincipal():#______________________________________________________F1
#Funcion para imprimir el menu principal
    global ver
    LimpiarPantalla()
    print(Fore.RED +"█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.RED + "████████████████████" + Fore.RESET + Style.BRIGHT + "Menu" + Fore.RESET + Fore.RED + "█████████████████████" + Fore.RESET)
    print(Fore.GREEN + "██" + Fore.RESET +"Imprimir datos capturados ........... (0)" + Fore.GREEN + "██" + Fore.RESET)
    if ver == 0:
        print(Fore.YELLOW + "██" + Fore.RESET + "Ingresar numero de estados .......... (1)" + Fore.YELLOW + "██" + Fore.RESET)#
    else:
        print(Fore.YELLOW + "██" + Fore.RESET + "Modificar numero de estados ......... (1)" + Fore.YELLOW + "██" + Fore.RESET)#

    if ver == 1:
        print(Fore.BLUE + "██" + Fore.RESET + "Ingresar matriz de transicion ....... (2)" + Fore.BLUE + "██" + Fore.RESET)
    elif ver == 2:
        print(Fore.BLUE + "██" + Fore.RESET + "Modificar matriz de transicion ...... (2)" + Fore.BLUE + "██" + Fore.RESET)
    if ver == 2:
        print(Fore.MAGENTA + "██" + Fore.RESET + "Realizar operacion .................. (3)" + Fore.MAGENTA + "██" + Fore.RESET)#
    print(Fore.RED + "██" + Fore.RESET + "Salir ............................... (4)" + Fore.RED + "██" + Fore.RESET)#
    print(Fore.RED + "█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.RED + "█████████████████████████████████████████████" + Fore.RESET)

def ImprMatriz():
    if parametros[0]!=0:
        for i in range(parametros[0]):
            for j in range(parametros[0]):
                print("["+str(matrizP[i][j])+"]", end=" ")
            print("\n")

def ImprPI0():
    if parametros[0]!=0:
        print("[", end=" ")
        for j in range(parametros[0]):
            print(str(Pi0[j]), end=" ")
            if j < parametros[0] - 1:
                print(", ", end=" ")
        print("]")
    

def ImprimirDatos():#______________________________________________________F2
#Funcion para imprimir los datos capturados por el usuario
    LimpiarPantalla()
    print(Fore.GREEN +"█████████████████████████████████████████████" + Fore.RESET)
    print("Numero de estados: " + str(parametros[0]))
    print("Estado inicial: " + str(parametros[1]))
    print("Estado final: " + str(parametros[2]))
    print("Numero de periodos: " + str(parametros[3]))
    print(Fore.GREEN +"█████████████████████████████████████████████\n" + Fore.RESET)
    ImprMatriz()
    print(Fore.GREEN +"█████████████████████████████████████████████" + Fore.RESET)
    ImprPI0()
    print(Fore.GREEN +"█████████████████████████████████████████████" + Fore.RESET)
    input("Presiona una tecla para continuar...")

def ModMatriz(x):#______________________________________________________F3
#Funcion para modificar la matriz de transicion
    LimpiarPantalla()
    aux1 = False
    aux2 = 0
    aux3 = 0.0
    
    filas = x
    columnas = filas

    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
    print(f"La matriz actual es de {filas}x{columnas}")
    ImprMatriz()
    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
    print("Teniendo en cuenta que la matriz empieza en el 0x0 ...")
    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)

    while aux1==False:
        aux2 = input("Seleccione el número de fila que desea modificar: ").encode('utf-8')
        aux1 = ValidacionEntero(aux2)
        if aux1 == True:
            fila_mod = int(aux2)
    aux1 = False

    while fila_mod < 0 or fila_mod >= filas:
        while aux1==False:
            aux2 = input(f"Seleccione un número de fila entre 0 y {filas-1}: ").encode('utf-8')
            aux1 = ValidacionEntero(aux2)
            if aux1 == True:
                fila_mod = int(aux2)
        aux1 = False
    
    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)

    while aux1==False:
        aux2 = input("Seleccione el número de columna que desea modificar: ").encode('utf-8')
        aux1 = ValidacionEntero(aux2)
        if aux1 == True:
            col_mod = int(aux2)
    aux1 = False

    while col_mod < 0 or col_mod >= columnas:
        while aux1==False:
            aux2 = input(f"Seleccione un número de columna entre 0 y {columnas-1}: ").encode('utf-8')
            aux1 = ValidacionEntero(aux2)
            if aux1 == True:
                col_mod = int(aux2)
        aux1 = False

    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)

    while aux1==False:
        aux3 = input(f"Ingrese el valor nuevo para la posición [{fila_mod}][{col_mod}]: ").encode('utf-8')
        aux1 = ValidacionFloat(aux3)
        if aux1 == True:
            valor_nuevo = float(aux3)
    aux1 = False

    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)

    matrizP[fila_mod][col_mod] = valor_nuevo
    ImprMatriz()
    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
    input("Presiona una tecla para continuar...")

def CrearMatriz(x):#______________________________________________________F4
#Funcion para crear la matriz de transicion
    aux1 = False
    aux3 = 0.0
    LimpiarPantalla()
    global ver
    if ver == 1:
        ver = 2
    for i in range(x):
        for j in range(x):
            print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
            print(Fore.BLUE + "███████" + Fore.RESET + f"Ingrese el elemento [{i}][{j}]: " + Fore.BLUE + "███████" + Fore.RESET)
            print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
            while aux1==False:
                aux3 = input("-->").encode('utf-8')
                aux1 = ValidacionFloat(aux3)
                if aux1 == True:
                    matrizP[i][j] = float(aux3)
            aux1 = False

def CrearVectorPI0():#______________________________________________________F4_1
    global Pi0
    if parametros[1]==0:
        Pi0 = [1,0,0,0,0]
    elif parametros[1]==1:
        Pi0 = [0,1,0,0,0]
    elif parametros[1]==2:
        Pi0 = [0,0,1,0,0]
    elif parametros[1]==3:
        Pi0 = [0,0,0,1,0]
    elif parametros[1]==4:
        Pi0 = [0,0,0,0,1]

def FuncionRecursiva(vector, matriz, n):
    if n == 0:
        return vector
    else:
        vectorNuevo = vector @ matriz
        print(vectorNuevo)
        return FuncionRecursiva(vectorNuevo, matriz, n-1)


def OperacionesMatriciales():#______________________________________________________F5_1
    if parametros[0]!=0:
        matrizAux = np.zeros((parametros[0],parametros[0]),dtype=float)
        vectorAux = np.zeros(parametros[0], dtype=float)
        for i in range(parametros[0]):
            vectorAux[i] = Pi0[i]
            for j in range(parametros[0]):
                matrizAux[i][j] = matrizP[i][j]

        if parametros[3]!=0:
            print("Multiplicar el vector Pi_n por la matriz de transicion " + str(parametros[3]) + " veces: ")
            vectorResultado = FuncionRecursiva(vectorAux, matrizAux, parametros[3])
            
            if parametros[2]==0:
                print("El resultado es: " + str(vectorResultado[0]))
            elif parametros[2]==1:
                print("El resultado es: " + str(vectorResultado[1]))
            elif parametros[2]==2:
                print("El resultado es: " + str(vectorResultado[2]))
            if parametros[2]==3:
                print("El resultado es: " + str(vectorResultado[3]))
            if parametros[2]==4:
                print("El resultado es: " + str(vectorResultado[4]))
            if parametros[2]==5:
                print("El resultado es: " + str(vectorResultado[5]))

        else:
            print("Tienes que colocar un mayor a 0 para realizar las operaciones con Pi0, prueba modificando dicho valor")
        input("Preciona una tecla para continuar...")

def FuncionVectorPI():#______________________________________________________F5_2
#Funcion encargada de realizar las operaciones matriciales
    aux1 = False
    aux2 = 0
    decUsr = 0

    LimpiarPantalla()
    print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.MAGENTA + "███ ¿Deseas modificar el estado inicial? ████" + Fore.RESET)
    print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)

    while aux1==False:
        aux2 = input("(presiona 1 para si, otro numero para no)-->").encode('utf-8')
        aux1 = ValidacionEntero(aux2)
        if aux1 == True:
            decUsr = int(aux2)
    aux1 = False

    if decUsr == 1:
        LimpiarPantalla()
        print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
        print(Fore.MAGENTA + "████████" + Fore.RESET + " Ingresa el estado inicial... " + Fore.MAGENTA + "███████" + Fore.RESET)
        print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
        while aux1==False:
            aux2 = input("-->").encode('utf-8')
            aux1 = ValidacionEntero(aux2)
            if aux1 == True:
                parametros[1] = int(aux2)
        aux1 = False
    LimpiarPantalla()

    print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.MAGENTA + "███ ¿Deseas modificar el estado final? ██████" + Fore.RESET)
    print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)

    while aux1==False:
        aux2 = input("(presiona 1 para si, otro numero para no)-->").encode('utf-8')
        aux1 = ValidacionEntero(aux2)
        if aux1 == True:
            decUsr = int(aux2)
    aux1 = False

    if decUsr == 1:
        LimpiarPantalla()
        print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
        print(Fore.MAGENTA + "████████" + Fore.RESET + " Ingresa el estado final... " + Fore.MAGENTA + "█████████" + Fore.RESET)
        print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
        while aux1==False:
            aux2 = input("-->").encode('utf-8')
            aux1 = ValidacionEntero(aux2)
            if aux1 == True:
                parametros[2] = int(aux2)
        aux1 = False
    LimpiarPantalla()

    print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.MAGENTA + "██ ¿Deseas modificar el numero de periodos? █" + Fore.RESET)
    print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)

    while aux1==False:
        aux2 = input("(presiona 1 para si, otro numero para no)-->").encode('utf-8')
        aux1 = ValidacionEntero(aux2)
        if aux1 == True:
            decUsr = int(aux2)
    aux1 = False

    if decUsr == 1:
        LimpiarPantalla()
        print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
        print(Fore.MAGENTA + "██████" + Fore.RESET + " Ingresa el numero de periodos... " + Fore.MAGENTA + "█████" + Fore.RESET)
        print(Fore.MAGENTA + "█████████████████████████████████████████████" + Fore.RESET)
        while aux1==False:
            aux2 = input("-->").encode('utf-8')
            aux1 = ValidacionEntero(aux2)
            if aux1 == True:
                parametros[3] = int(aux2)
        aux1 = False
    LimpiarPantalla()

    CrearVectorPI0()

    OperacionesMatriciales()



#________________________________________________________________________________MAIN

usuarioMenu = 0
aux1 = False
aux2 = 0

while usuarioMenu != 4:
    MenuPrincipal()
    
    while aux1==False:
        usuarioMenu = input("-->").encode('utf-8')
        aux1 = ValidacionEntero(usuarioMenu)
        if aux1 == True:
            usuarioMenu = int(usuarioMenu)
    
    aux1 = False

    if usuarioMenu==1:
        LimpiarPantalla()
        if ver == 0:
            ver = 1
        print(Fore.YELLOW +"█████████████████████████████████████████████" + Fore.RESET)
        print(Fore.YELLOW + "███████" + Fore.RESET + "Ingresa el numero de estados..." + Fore.YELLOW + "███████" + Fore.RESET)
        print(Fore.YELLOW +"█████████████████████████████████████████████" + Fore.RESET)

        while aux1==False:
            aux2 = input("-->")
            aux1 = ValidacionEntero(aux2)
            if aux1 == True:
                parametros[0] = int(aux2)
                
        aux1 = False
    
    elif usuarioMenu==2:
        if ver == 1:
            CrearMatriz(parametros[0])
        elif ver == 2:
            ModMatriz(parametros[0])
    elif usuarioMenu==0:
        ImprimirDatos()
    elif usuarioMenu==3:
        if ver != 0:
            FuncionVectorPI()

#________________________________________________________________________________MAIN