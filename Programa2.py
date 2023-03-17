from colorama import Fore, Back, Style
import platform
import numpy as np
import os

NumeroDeEstados = 0
EstadoInicial = -1
EstadoFinal = -1
NumeroDePeriodos = 0
matrizP = np.zeros((5,5),dtype=float)
pt = platform.system()
ver = 0

def ValidacionEntero(x):#______________________________________________________F_Validacion1
    if x.isdigit():
        return True
    else:
        print("Debe ser un numero entero, prueba nuevamente...")
        return False
    
def ValidacionFloat(x):#______________________________________________________F_Validacion2
    try:
        float(x)
        return True
    except ValueError:
        print("Caracter no valido, prueba nuevamente...")
        return False

def LimpiarPantalla():#______________________________________________________F_IMPR1
    if pt == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    
def MenuPrincipal():#______________________________________________________F_IMPR2
#Funcion para imprimir el menu principal
    global ver
    LimpiarPantalla()
    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.BLUE + "████████████████████" + Fore.RESET + Style.BRIGHT + "Menu" + Fore.RESET + Fore.BLUE + "█████████████████████" + Fore.RESET)
    print(Fore.BLUE + "██" + Fore.RESET +"Imprimir datos capturados ........... (0)" + Fore.BLUE + "██" + Fore.RESET)
    
    if ver == 0:
        print(Fore.RED + "██" + Fore.RESET + "Ingresar numero de estados .......... (1)" + Fore.RED + "██" + Fore.RESET)
    else:
        print(Fore.BLUE + "██" + Fore.RESET + "Modificar numero de estados ......... (1)" + Fore.BLUE + "██" + Fore.RESET)

    if ver == 1:
        print(Fore.RED + "██" + Fore.RESET + "Ingresar matriz de transicion ....... (2)" + Fore.RED + "██" + Fore.RESET)
    elif ver == 2:
        print(Fore.BLUE + "██" + Fore.RESET + "Modificar matriz de transicion ...... (2)" + Fore.BLUE + "██" + Fore.RESET)

    if ver != 0:
        if EstadoInicial==-1:
            print(Fore.RED + "██" + Fore.RESET + "Ingresar estado inicial ............. (3)" + Fore.RED + "██" + Fore.RESET)
        else:
            print(Fore.BLUE + "██" + Fore.RESET + "Modificar estado inicial ............ (3)" + Fore.BLUE + "██" + Fore.RESET)
        
        if EstadoFinal==-1:
            print(Fore.RED + "██" + Fore.RESET + "Ingresar estado final ............... (4)" + Fore.RED + "██" + Fore.RESET)
        else:
            print(Fore.BLUE + "██" + Fore.RESET + "Ingresar estado final ............... (4)" + Fore.BLUE + "██" + Fore.RESET)

        if NumeroDePeriodos==0:
            print(Fore.RED + "██" + Fore.RESET + "Ingresar numero de periodos ......... (5)" + Fore.RED + "██" + Fore.RESET)
        else:
            print(Fore.BLUE + "██" + Fore.RESET + "Modificar numero de periodos ........ (5)" + Fore.BLUE + "██" + Fore.RESET)

    if ver == 2:
        if EstadoInicial!=-1 and EstadoFinal!=-1 and NumeroDePeriodos!=0:
            print(Fore.BLUE + "██" + Fore.RESET + Fore.RED + "Probabilidad de primera vez ......... (6)" + Style.RESET_ALL + Fore.BLUE + "██" + Fore.RESET)#
    print(Fore.BLUE + "██" + Fore.RESET + "Salir ............................... (7)" + Fore.BLUE + "██" + Fore.RESET)#
    print(Fore.BLUE + "█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.BLUE + "█████████████████████████████████████████████" + Fore.RESET)

def ImprMatriz():#______________________________________________________F_IMPR13
    if NumeroDeEstados!=0:
        for i in range(NumeroDeEstados):
            for j in range(NumeroDeEstados):
                print("["+str(matrizP[i][j])+"]", end=" ")
            print("\n")

def ImprPI0():#______________________________________________________F_IMPR4
    if NumeroDeEstados!=0:
        if EstadoInicial!=-1:
            if EstadoInicial==0:
                print("[1,0,0,0]")
            elif EstadoInicial==0:
                print("[0,1,0,0]")
            elif EstadoInicial==0:
                print("[0,0,1,0]")
            elif EstadoInicial==0:
                print("[0,0,0,1]")
    else:
        print("No se ha ingresado el estado inicial, por lo tanto no existe el vector PI0...")
    
def ImprimirDatos():#______________________________________________________F_IMPR5
#Funcion para imprimir los datos capturados por el usuario
    LimpiarPantalla()
    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
    print("Numero de estados: " + str(NumeroDeEstados))
    print("Estado inicial: " + str(EstadoInicial))
    print("Estado final: " + str(EstadoFinal))
    print("Numero de periodos: " + str(NumeroDePeriodos))
    print(Fore.BLUE +"█████████████████████████████████████████████\n" + Fore.RESET)
    ImprMatriz()
    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
    ImprPI0()
    print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
    input("Presiona una tecla para continuar...")

def ModMatriz(x):#______________________________________________________F_Matrix3
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

def CrearMatriz(x):#______________________________________________________F_Matrix4
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

def FuncionRecursiva(vector, matriz, nperiodos):#______________________________________________________F_Vector2
    if nperiodos == 0:
        return vector
    else:
        vectorNuevo = vector @ matriz
        return FuncionRecursiva(vectorNuevo, matriz, nperiodos-1)

def ObtenerProbabilidadDeNperidodos(Estinicial, EstFinal, periodos):#______________________________________________________F5_1
    global matrizP
    vectorPi0 = [1,0,0,0,0]

    if Estinicial==0:
        vectorPi0 = [1,0,0,0,0]
    elif Estinicial==1:
        vectorPi0 = [0,1,0,0,0]
    elif Estinicial==2:
        vectorPi0 = [0,0,1,0,0]
    elif Estinicial==3:
        vectorPi0 = [0,0,0,1,0]
    elif Estinicial==4:
        vectorPi0 = [0,0,0,0,1]

    if periodos!=0:
        vectorResultado = FuncionRecursiva(vectorPi0, matrizP, periodos)
        
        if EstFinal==0:
            return vectorResultado[0]
        elif EstFinal==1:
            return vectorResultado[1]
        elif EstFinal==2:
            return vectorResultado[2]
        elif EstFinal==3:
            return vectorResultado[3]
        elif EstFinal==4:
            return vectorResultado[4]
        elif EstFinal==5:
            return vectorResultado[5]
        else:
            return 0

def ModEstadoInicial():
    global EstadoInicial
    aux1 = False
    aux2 = 0

    LimpiarPantalla()
    print(Fore.BLUE + "█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.BLUE + "████████" + Fore.RESET + " Ingresa el estado inicial... " + Fore.BLUE + "███████" + Fore.RESET)
    print(Fore.BLUE + "█████████████████████████████████████████████" + Fore.RESET)
    while aux1==False:
        aux2 = input("-->").encode('utf-8')
        aux1 = ValidacionEntero(aux2)
        if aux1 == True:
            EstadoInicial = int(aux2)
    aux1 = False

def ModEstadoFinal():
    global EstadoFinal
    aux1 = False
    aux2 = 0

    LimpiarPantalla()
    print(Fore.BLUE + "█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.BLUE + "████████" + Fore.RESET + " Ingresa el estado final... " + Fore.BLUE + "█████████" + Fore.RESET)
    print(Fore.BLUE + "█████████████████████████████████████████████" + Fore.RESET)
    while aux1==False:
        aux2 = input("-->").encode('utf-8')
        aux1 = ValidacionEntero(aux2)
        if aux1 == True:
            EstadoFinal = int(aux2)
    aux1 = False

def ModNumeroDePeriodos():
    global NumeroDePeriodos
    aux1 = False
    aux2 = 0

    LimpiarPantalla()
    print(Fore.BLUE + "█████████████████████████████████████████████" + Fore.RESET)
    print(Fore.BLUE + "██████" + Fore.RESET + " Ingresa el numero de periodos... " + Fore.BLUE + "█████" + Fore.RESET)
    print(Fore.BLUE + "█████████████████████████████████████████████" + Fore.RESET)
    while aux1==False:
        aux2 = input("-->").encode('utf-8')
        aux1 = ValidacionEntero(aux2)
        if aux1 == True:
            NumeroDePeriodos = int(aux2)
    aux1 = False

def ProbabilidadDePrimeraVez(): #Crear la funcion que haga las operaciones
    print("holA")

#________________________________________________________________________________MAIN

usuarioMenu = 0
aux1 = False
aux2 = 0

while usuarioMenu != 7:
    MenuPrincipal()
    
    while aux1==False:
        usuarioMenu = input("-->").encode('utf-8')
        aux1 = ValidacionEntero(usuarioMenu)
        if aux1 == True:
            usuarioMenu = int(usuarioMenu)
    
    aux1 = False

    if usuarioMenu==0:
        ImprimirDatos()
    elif usuarioMenu==1:
        LimpiarPantalla()
        if ver == 0:
            ver = 1
        print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)
        print(Fore.BLUE + "███████" + Fore.RESET + "Ingresa el numero de estados..." + Fore.BLUE + "███████" + Fore.RESET)
        print(Fore.BLUE +"█████████████████████████████████████████████" + Fore.RESET)

        while aux1==False:
            aux2 = input("-->")
            aux1 = ValidacionEntero(aux2)
            if aux1 == True:
                NumeroDeEstados = int(aux2)
                
        aux1 = False
    
    elif usuarioMenu==2:
        if ver == 1:
            CrearMatriz(NumeroDeEstados)
        elif ver == 2:
            ModMatriz(NumeroDeEstados)
    elif usuarioMenu==3:
        ModEstadoInicial()
    elif usuarioMenu==4:
        ModEstadoFinal()
    elif usuarioMenu==5:
        ModNumeroDePeriodos()
    elif usuarioMenu==6:
        if EstadoInicial!=-1 and EstadoFinal!=-1 and NumeroDeEstados!=0:
            print(ObtenerProbabilidadDeNperidodos(EstadoInicial, EstadoFinal,NumeroDePeriodos)) #Imprime la probabilidad de ir del EstadoInicial al EstadoFinal en NumeroDePeridos periodos de tiempo (Por lo mientras, luego se colocara la funcion de primera vez)
            input("Presiona un boton para continuar...")

#________________________________________________________________________________MAIN