# Archivo: fun.py
import re;

saldo = 4000

def validar(psswrd):
    
    # Lista para almacenar lo errores que tiene el usuario al digitar la contrasena
    errores = []
    
    
    if len(psswrd) < 8:
        errores.append(" Uh Oh!! La contraseña debe tener mínimo 8 caracteres.")
        
    if psswrd.lower() == psswrd:
        errores.append("Uh Oh!! La contraseña debe tener al menos una letra mayúscula.")

    if not any(c.isdigit() for c in psswrd):
        errores.append("Uh Oh!! La contraseña debe tener al menos un número.")
    
    if not re.search(r'[^a-zA-Z0-9]', psswrd):
        errores.append("Uh Oh!! La contraseña debe tener al menos un caracter especial.")

    valida = len(errores) == 0

    return valida, errores



def consulta_saldo ():
    return saldo



def clave_primera_vez (user):
    
    # Bucle while para que se pueda reintentar
    while True: 
        print(f"\nBienvenido {user}. Por favor ingresa tu clave de acuerdo a los siguientes parametros: ")
        print(f"- Minimo 8 caracteres \n - Minimo una mayuscula \n - Minimo un numero \n - Al menos un caracter especial")
        
        psswrd = input("Ingresa la clave: ")
        valida, mensajes_error = validar(psswrd)
        
        # Resultados
        if valida:
            print("\n✅ La contraseña es válida. Guardando clave...")
            # Devolvemos la clave válida para que cajero.py la use/guarde
            return psswrd
        else:
            # Si no es válida, imprimimos los errores y le pedimos que reintente
            print("\nUps! Contraseña no válida. Revisa los siguientes errores:")
            for error in mensajes_error:
                print(error)
            print("Por favor, inténtalo de nuevo.")