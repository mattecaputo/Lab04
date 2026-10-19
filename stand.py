class Stand:
# Definizione della classe Stand
    def __init__(self, id_stand, superficie, padiglione, prezzo_base):
        self.id_stand = id_stand
        self.superficie = int (superficie)
        self.padiglione = int (padiglione)
        self.prezzo_base = float(prezzo_base)
        self.espositore = None
        self.disponibile = True

    def calcola_prezzo(self) -> float:

        return self.prezzo_base


    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = " Occupato "
        # Definizione dello stato dello stand
        return f"{self.id_stand}: Standard | { self.superficie} mq - Padiglione {self.padiglione} - Prezzo base {self.calcola_prezzo():.2f}€ - {stato}"


    def __repr__(self):
        return self.__str__()





