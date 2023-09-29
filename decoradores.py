def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return funcion_modificada

def saludo():
    print("Hola mundo!")

saludo_modificado =decorador(saludo)
saludo_modificado()
