class Auto:
    def __init__(self, nev, gyartasi_ev):
        self.nev = nev
        self.gyartasi_ev = int(gyartasi_ev)


    def __str__(self):
        return f"Auto neve: {self.nev}, gyártási éve: {self.gyartasi_ev}"