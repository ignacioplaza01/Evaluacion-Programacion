
from Bicicleta import Bicicleta
from Consola import Consola
from Scooter import Scooter
from TV import TV




def validar_numero(texto,tipo):
    while True:
        try:
            if tipo=="int":  
                valor = int(input(f"Ingrese {texto}: "))
                return valor
                
            elif tipo=="float":
                valor = float(input(f"Ingrese {texto}: "))
                return valor
        except:
              print("Debe ser un valor numerico")
            
            

ListaBici = []
ListaConsola = []
ListaScooter = []
ListaTV = []

def registrar_bici():
    aro = validar_numero("Ingrese aro: ","float")
    peso = validar_numero("Ingrese peso: ","float")
    precio = validar_numero("Ingrese precio: ","float")
    marca = input("Ingrese marca: ")
    Bicicleta(aro,peso,precio,marca)
    ListaBici.extend([aro,peso,precio,marca])
    
    
def registrar_consola():
    voltaje = validar_numero("Ingrese voltaje: ","float")
    precio = validar_numero("Ingrese precio: ","float")
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    nombreConsola = input("Ingrese nombre de consola: ")
    versionConsola = input("Ingrese version de consola: ")
    Consola(voltaje,precio,eficiencia,marca,nombreConsola,versionConsola)
    ListaConsola.extend([voltaje,precio,eficiencia,marca,nombreConsola,versionConsola])

def registrar_scooter():
    voltaje = validar_numero("Ingrese voltaje: ","float")
    precio = validar_numero("Ingrese precio: ","float")
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    aro = validar_numero("Ingrese aro: ","float") 
    velocidad = validar_numero("Ingrese velocidad: ","float")
    peso = validar_numero("Ingrese peso: ","float")
    Scooter(voltaje,precio,eficiencia,marca,aro,velocidad,peso)
    ListaScooter.extend([voltaje,precio,eficiencia,marca,aro,velocidad,peso])

def registrar_tv():
    
    
    voltaje = validar_numero("Ingrese voltaje: ","float")
    precio = validar_numero("Ingrese precio: ","float")
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    tamano = validar_numero("Ingrese tamaño de TV: ","float")
    a = TV(voltaje,precio,eficiencia,marca,tamano)
    a.calcular_descuento()
    ListaTV.extend([voltaje,precio,eficiencia,marca,tamano])
    
    


def cotizar_tv():
    precio = validar_numero("Ingrese el precio que desea: ","float")
    eficiencia = input("Ingrese la eficiencia que busca: ")
    a = TV(None,precio,eficiencia,None,None)
    a.valor_total()
    return a

def cotizar_bici():
    precio = validar_numero("Ingrese el precio que busca: ","float")
    peso = validar_numero("Ingrese el peso: ","float")
    a = Bicicleta(None,peso,precio,None)    
    a.calcularDespacho()

def cotizar_consola():
    precio = validar_numero("Ingrese el precio que busca: ","float")
    eficiencia = input("Ingrese la eficiencia que busca: ")
    version = input("Ingrese la version que busca: ")
    a = Consola(None,precio,eficiencia,None,None,version)
    a.calcular_descuento()

def cotizar_scooter():
    
    precio = validar_numero("Ingrese el precio que busca: ","float")
    peso = validar_numero("Ingrese el peso: ","float")
    eficiencia = input("Ingrese la eficiencia que busca: ")
    a = Scooter(None,precio,eficiencia,None,None,None,peso)    
    a.calcularDespacho()



while True:

    print("1.-Registrar producto")
    print("2.-Cotizar producto")
    print("3.-Listar productos")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        print("1.-Bicicleta")
        print("2.-Consola")
        print("3.-Scooter")
        print("4.-TV")
        producto = input("Tipo de producto: ")
        if producto == "1":
            registrar_bici()

        elif producto == "2":
            registrar_consola()

        elif producto == "3":
            registrar_scooter()

        elif producto == "4":
            registrar_tv()

        else:
            print("Opcion no valida")       

    elif opcion == "2":
        print("1.-Bicicleta")
        print("2.-Consola")
        print("3.-Scooter")
        print("4.-TV")
        cot = input("¿Que producto desea cotizar? ")
        if cot == "1":
            cotizar_bici()

        elif cot == "2":
            cotizar_consola()

        elif cot == "3":
            cotizar_scooter()

        elif cot == "4":
            cotizar_tv()

        else:
            print("Producto no encontrado")    

    elif opcion == "3":
        print("1.-Bicicleta")
        print("2.-Consola")
        print("3.-Scooter")
        print("4.-TV")
        p = input("Seleccione el tipo de producto que desea ver: ")
        if p == "1":
            print(ListaBici)
        elif p== "2":
            print(ListaConsola)
        elif p == "3":
            print(ListaScooter)
        elif p == "4":
            print(ListaTV)  
        else:
            print("Opcion no valida")              

    else:
        print("Opcion no valida")                    



