import random

def lottoszamok():
    szamok = [random.randint(1, 99) for _ in range(5)]
    return szamok

def egyjegyuek_szama(szamok):
    return sum(1 for szam in szamok if szam < 10)

def konzol_kiir(szamok, egyjegyuek):
    print("II/A, B, C:")
    print("; ".join(map(str, szamok)))
    print("II/D, E:")
    print(f"Az egyjegyűek száma: {egyjegyuek}.")

def file_kiir(egyjegyuek, fajlnev="szamok.txt"):
    with open(fajlnev, "w") as fajl:
        fajl.write(f"Az egyjegyűek száma: {egyjegyuek}.")
