class Spedizione:
    def __init__(self, mittente, destinatario, quantita, descrizione=""):
        self.mittente = mittente
        self.destinatario = destinatario
        self.quantita = quantita
        self.descrizione = descrizione
        self.eseguita = False
