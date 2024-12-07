#Tickets
import pickle, sys, os, random

archivo="tickets.pkl"

def limpiar_terminal():
    os.system("cls" if os.name=="nt" else"clear")

def guardar_ticket(ticket, archivo):
    tickets=[]
    if os.path.isfile(archivo):
        with open(archivo, "rb") as f:
            tickets=pickle.load(f)
    tickets.append(ticket)
    with open(archivo, "wb") as f:
        pickle.dump(tickets, f)

def cargar_ticket(archivo):
    if os.path.isfile(archivo):
        with open(archivo, "rb") as f:
            return pickle.load(f)
    return[]
    
def generar_ticket(archivo):
    limpiar_terminal()
    print("Ingrese los datos para generar un nuevo ticket:")
    nombre=input("Ingrese su nombre: ")
    sector=input("Ingrese su sector: ")
    asunto=input("Ingrese el asunto: ")
    mensaje=input("Ingrese un mensaje: ")
    numero_ticket = random.randrange(1000, 9999)
    ticket={
        "N° ticket":numero_ticket,
        "Nombre":nombre,
        "Sector":sector,
        "Asunto":asunto, 
        "Mensaje":mensaje,
    }
    guardar_ticket(ticket, archivo)
    limpiar_terminal()
    print("------------------------------")
    print("Se generó el siguiente ticket")
    print("------------------------------")
    print(f"N° ticket: {numero_ticket}")
    print(f"Su nombre: {nombre}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")
    print("Recordar su número de ticket para posterior consulta")
    

    nuevo_ticket=input("¿Desea generar un nuevo ticket? (s/n)").lower()
    if nuevo_ticket=="s":
        generar_ticket(archivo)
    elif nuevo_ticket=="n":
        limpiar_terminal()
        menu()
    else:
        print("Ingresar una opción válida")
        print(nuevo_ticket)


def leer_ticket(archivo):
    limpiar_terminal()
    tickets = cargar_ticket(archivo)
    if not tickets:
        print("No hay tickets guardados.")
        return menu()
    try:
        numero_ticket = int(input("Ingrese su número de ticket: "))
    except ValueError:
        print("Ingrese un número válido")
        return menu()
    
    encontrado = False
    for ticket in tickets:
        if ticket["N° ticket"] == numero_ticket:
            print("Ticket cargado:")
            print("------------------------------")
            for clave, valor in ticket.items():
                print(f"{clave}: {valor}")
            print("------------------------------")
            encontrado=True
            break
     
    if not encontrado:
        print("El número de ticket no existe.")
    post_lectura=input("¿Desea leer otro ticket? (s/n)").lower()
    if post_lectura=="s":
        leer_ticket(archivo)
    elif post_lectura=="n":
        limpiar_terminal()
        menu()
    else:
        print("Ingrese una opción válida")
        limpiar_terminal()
        menu()

def menu():
    print("Hola bienvenido al sistema de Tickets") 
    print("1. Generar un nuevo ticket")
    print("2. Leer un ticket")
    print("3. Salir")
    opcion=input("Seleccione: ")
    if opcion=="1":
        generar_ticket(archivo)
    elif opcion=="2":
        leer_ticket(archivo)
    elif opcion=="3":
        limpiar_terminal()
        print("Saliendo del sistema")
        sys.exit()
    else: 
        print("Ingresar una opción válida")
        limpiar_terminal()
        menu()

limpiar_terminal()
menu()