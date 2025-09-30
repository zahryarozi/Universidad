# Archivo: fun.py
import re; # 'collections' ya no es necesario, lo quité.

saldo = 4000

def validar(psswrd):
    
    # Lista para almacenar lo errores que tiene el usuario al digitar la contrasena
    errores = []
    
    # ¡CORRECCIÓN! Usar 'psswrd' en lugar de 'password'
    if len(psswrd) < 8:
        errores.append("❌ La contraseña debe tener mínimo 8 caracteres.")
        
    # ¡CORRECCIÓN! Usar 'psswrd' en lugar de 'password'
    if psswrd.lower() == psswrd:
        errores.append("❌ La contraseña debe tener al menos una letra mayúscula.")

    # ¡CORRECCIÓN! Usar 'psswrd' en lugar de 'password'
    if not any(c.isdigit() for c in psswrd):
        errores.append("❌ La contraseña debe tener al menos un número.")

    # ¡CORRECCIÓN! Usar 'psswrd' en lugar de 'password'
    if not re.search(r'[^a-zA-Z0-9]', psswrd):
        errores.append("❌ La contraseña debe tener al menos un caracter especial.")

    valida = len(errores) == 0

    return valida, errores

def consulta_saldo ():
    return saldo

def clave_primera_vez (user):
    
    # Usaremos un bucle while para que el usuario pueda reintentar
    while True: 
        print(f"\nBienvenido {user}. Por favor ingresa tu clave de acuerdo a los siguientes parametros: ")
        print(f"- Minimo 8 caracteres \n - Minimo una mayuscula \n - Minimo un numero \n - Al menos un caracter especial")
        
        psswrd = input("Ingresa la clave: ")
        valida, mensajes_error = validar(psswrd)
        
        # Paso 3: Impresión de resultados
        if valida:
            print("\n✅ La contraseña es válida. Guardando clave...")
            # Devolvemos la clave válida para que cajero.py la use/guarde
            return psswrd
        else:
            # Si no es válida, imprimimos los errores y le pedimos que reintente
            print("\n🚨 Contraseña no válida. Revisa los siguientes errores:")
            for error in mensajes_error:
                print(error)
            print("Por favor, inténtalo de nuevo.")