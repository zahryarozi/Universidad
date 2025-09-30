import funciones

cuentas = {
    "diego": ["default", 5000000],
    "gabriela": ["hola1234", 4000]
}


user = input("Ingresa tu Usuario \n").lower()

if user in cuentas:
    datos = cuentas[user]
    if datos and datos[0] == "default":
        print(f"Querido {user}, por favor digite su clave por primera vez")
        clave = clave_primera_vez()
    
else:
    print("Usuario no registrado")
