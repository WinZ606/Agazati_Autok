import random

def lotto():
    lista = []
    for i in range(0,5,1):
        lista.append(random.randint(0,50))
    return lista

def egyjegyuek_szama(lista):
    egyjegyuek = 0
    for i in range(0,5,1):
        if ((lista[i] / 10 ) < 1):
            egyjegyuek += 1
    return egyjegyuek

lista = lotto()

def kiir():
    print("II/A, B, C:")
    print(*lista,sep="; ")
    print("II/D, E:")
    print(f"Az egyjegyűek száma: {egyjegyuek_szama(lista)}")

def file_kiir(egyjegyuek_szama):
    f = open("szamok.txt", "w")
    f.write("II/F:\n")
    f.write(f"Az egyjegyűek száma: {egyjegyuek_szama}.")