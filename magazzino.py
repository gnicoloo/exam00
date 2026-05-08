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
