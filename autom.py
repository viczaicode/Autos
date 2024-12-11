from auto import Auto

def beolvas(fajlnev):
    autok = []
    with open(fajlnev, "r") as fajl:
        fajl.readline() 
        for sor in fajl:
            nev, ev = sor.strip().split("$")
            autok.append(Auto(nev, ev))
    return autok

def flotta(autok):
    return len(autok)

def legfiatalabb(autok):
    legfiatalabb_auto = autok[0]
    for auto in autok:
        if auto.gyartasi_ev < legfiatalabb_auto.gyartasi_ev:
            legfiatalabb_auto = auto 
    return legfiatalabb_auto


def atlagos_kor(autok, ev=2024):
    return sum(ev - auto.gyartasi_ev for auto in autok) / len(autok)
