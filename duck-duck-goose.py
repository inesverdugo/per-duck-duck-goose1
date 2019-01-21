

jugadores = ["ines", "Lorena", "paula", "carol", "lucas"]
numero = int(input("Introduzca un numero"))

def ddg(lista_nombres, numero):
    if len(lista_nombres) < numero:
        print("ERROR")
        return
    else:
        return print(lista_nombres[numero])

ddg(jugadores, numero)
