import fun



print("\n \n ======= BIENVENID@ AL CAJERO M.A.F.I.A SAVINGS =======\n \n")

user = input("Ingresa tu Usuario \n").lower()

if user in fun.cuentas:
    datos = fun.cuentas[user]   
    
    if datos and datos[0] == "default":
        print(f"\n \n Querid@ {user}, hemos detectado que no ha registrado su clave!!! \n =!=!=!=!=!=!= =!=!=!=!=!=!=")
        
        nueva_clave = fun.clave_primera_vez(user) 
        
        datos[0] = nueva_clave #Reemplazar Default en Diego
        
        print(f"\n¡Clave actualizada con éxito! Nuevo estado de la cuenta: {datos}")
    else:
        print("=== OPCIONES A ELEGIR: === \n 1. Consultar Saldo \n 2. Depositar Dinero \n 3. Retirar Dinero \n ===============")
        
        opcion = int(input(f"Querid@ {user}, por favor digite el numero de la opcion a realizar: \n"))
        
        if opcion == 1:
            saldo_usuario = fun.consulta_saldo(user)
            print(f"\n \n Su saldo es {saldo_usuario}")
            
        elif opcion == 2:
            depositado = fun.depositar_dinero(user)
            print(f"\n \n Su dinero depositado es {depositado}")
        
        elif opcion == 3:
            retirado = fun.retirar_dinero(user)
            print(f"\n \n Su dinero depositado es {retirado}")
            
else:
    print("Usuario no registrado")