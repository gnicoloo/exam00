class Magazzino:
    def __init__(self, responsabile, codice, scorta=0):
        self.responsabile = responsabile
        self.codice = codice
        self.scorta = scorta
    def __str__(self):
        return f"{self.responsabile} ({self.codice}): {self.scorta} unità"
    def carica(self, quota):
        if(quota > 0):
            self.scorta += quota
            return True
        else:
            return False
    def scarica(self, quantita):
        if(quantita > self.scorta or quantita <= 0):
            return False
        self.scorta -= quantita
        return True
