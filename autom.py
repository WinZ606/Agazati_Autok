class Auto:
    def __init__(self,nev,evjarat):
        self.nev = nev
        self.evjarat = int(evjarat)
        self.kor = 2024 - self.evjarat
        self.autok = []

    def beolvas(self):
        f = open("auto.txt", 'r', encoding='utf-8')
        for line in f:
            adatok = line.strip().split(";")
            nev, evjarat = adatok
            self.autok.append({'nev': nev, 'evjarat': int(evjarat)})

    def flotta(autok):
        return len(autok)