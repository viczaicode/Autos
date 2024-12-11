import bevezetes
import sorozat
import autom

#nev, ev = bevezetes.autoadatok_bekerese()
#bevezetes.kor_kategoria(nev, ev)


#szamok = sorozat.lottoszamok()
#egyjegyuek = sorozat.egyjegyuek_szama(szamok)
#sorozat.konzol_kiir(szamok, egyjegyuek)
#sorozat.file_kiir(egyjegyuek)


autok = autom.beolvas("auto.txt")
print("III/Flotta:")
print(f"Autók száma: {autom.flotta(autok)}.")

legfiatalabb_auto = autom.legfiatalabb(autok)
print("III/Legfiatalabb:")
print(f"A legfiatalabb autó: {legfiatalabb_auto.nev} ({legfiatalabb_auto.gyartasi_ev}).")

atlag_kor = autom.atlagos_kor(autok)
print("III/Átlag kor:")
print(f"Az autók átlagos kora: {atlag_kor:.2f} év.")