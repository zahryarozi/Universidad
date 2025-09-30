import fun

cuentas = {
    "diego": ["default", 5000000],
    "gabriela": ["hola1234", 4000]
}


user = input("Ingresa tu Usuario \n").lower()

if user in cuentas:
    print("======= BIENVENID@ AL CAJERO M.A.F.I.A SAVINGS =======\n \n")
    datos = cuentas[user]
    
    if datos and datos[0] == "default":
        print(f"Querid@ {user}, por favor digite su clave por primera vez")
        
        nueva_clave = fun.clave_primera_vez(user) 
        
        datos[0] = nueva_clave #Reemplazar Default en Diego
        
        print(f"\n¡Clave actualizada con éxito! Nuevo estado de la cuenta: {datos}")
    else:
        print("=== OPCIONES A ELEGIR: === \n 1. Consultar Saldo \n 2. Depositar Dinero \n 3. Retirar Dinero \n ===============")
        
        opcion = input(f"Querid@ {user}, Por favor digite el numero de la opcion a realizar: \n")
        
        
        
    
else:
    print("Usuario no registrado")