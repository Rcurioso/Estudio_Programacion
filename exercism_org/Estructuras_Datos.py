#Ejercicio Listas:
personajes = ["Kakyoin", "Joseph", "Jotaro"]
personajes.remove("Kakyoin")
personajes.append("Polnareff")
resultado = personajes[1:2]
print(resultado)

#Ejercicio Tuplas:
respuesta = ("Yes", "Yes", "Yes")
resultado2 = (respuesta.count("Yes"), respuesta.index("Yes"))
print(resultado2)

#Ejercicio Conjuntos:
temporada_2 = set(["Joseph", "Caesar"])
temporada_3 = set(["Jotaro", "Joseph", "Avdol", "Kakyoin", "Polnareff"])
print(temporada_2)
resultado3 = temporada_2 & temporada_3
print(resultado3)

#Ejercicio Diccionarios:
protas = {1:"Jonnathan", 2:"Joseph", 3:"Jotaro"}
jojos = {"Jonnathan":"Phantom Blood",
         "Joseph": "Battle Tendency",
         "Jotaro":"Stardust Crusaders"}
print(protas[3])
resultado4 = jojos[protas[3]]
print(resultado4)
