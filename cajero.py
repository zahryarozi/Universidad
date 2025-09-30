# Archivo: cajero.py
import fun

cuentas = {
    "diego": ["default", 5000000],
    "gabriela": ["hola1234", 4000]
}


user = input("Ingresa tu Usuario \n").lower()

if user in cuentas:
    datos = cuentas[user]
    
    if datos and datos[0] == "default":
        print(f"Querido {user}, por favor digite su clave por primera vez")
        
        # Llama a la función que ahora maneja los reintentos
        nueva_clave = fun.clave_primera_vez(user) 
        
        # Una vez que la función devuelve la clave (que es válida), la guardamos
        datos[0] = nueva_clave # Reemplazamos "default" con la nueva clave
        
        print(f"\n¡Clave actualizada con éxito! Nuevo estado de la cuenta: {datos}")
        
    
else:
    print("Usuario no registrado")