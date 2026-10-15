class Stand:

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
            stato = " Disponibile"
        else:
            stato = " Occupato "

        return f"{self.id_stand}: Standard | { self.superficie} mq - Padiglione {self.padiglione} - Prezzo base {self.calcola_prezzo():.2f}€ - {stato}"


    def __repr__(self):
        return self.__str__()



class StandPreseExtra (Stand):

    def __init__(self, id_stand, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(id_stand,superficie, padiglione, prezzo_base)
        self.numero_prese = int(numero_prese)


    def calcola_prezzo(self) -> float:
        return self.prezzo_base * ( 1 + 0.07 * self.numero_prese)

    def __str__(self):
        if self.disponibile:
            stato = " Disponibile"
        else:
            stato = " Occupato "

        return f"{self.id_stand}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive : {self.numero_prese} - {stato}"

class StandPremium ( Stand ):
    def __init__(self, id_stand, superficie, padiglione, prezzo_base, posizione):
        super().__init__(id_stand, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self) -> float:
        return self.prezzo_base * 1.30

    def __str__(self):
        if self.disponibile:
            stato = " Disponibile"
        else:
            stato = " Occupato "

        return f" { self.id_stand}: Premium ({self.posizione}) | {self.superficie} mq - Padiglione: {self.padiglione} - Prezzo: {self.calcola_prezzo():.2f}€ - {stato} "