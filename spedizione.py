class Spedizione:
    def __init__(self, mittente, destinatario, quantita, descrizione=""):
        self.mittente = mittente
        self.destinatario = destinatario
        self.quantita = quantita
        self.descrizione = descrizione
        self.eseguita = False

    def __str__(self):
        stato = "eseguita" if self.eseguita else "in attesa"
        return (
            f"{self.quantita:.2f} unità "
            f"da {self.mittente.responsabile} "
            f"a {self.destinatario.responsabile} "
            f"({stato})"
        )
