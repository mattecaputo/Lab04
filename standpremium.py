from stand import Stand
class StandPremium ( Stand ):
    def __init__(self, id_stand, superficie, padiglione, prezzo_base, posizione):
        super().__init__(id_stand, superficie, padiglione, prezzo_base)
        self.posizione = posizione  #Aggiunta del parametro

    def calcola_prezzo(self) -> float:
        #Calcolo del nuovo prezzo
        return self.prezzo_base * 1.30

    def __str__(self):
        if self.disponibile:
            stato = " Disponibile"
        else:
            stato = " Occupato "

        return f" { self.id_stand}: Premium ({self.posizione}) | {self.superficie} mq - Padiglione: {self.padiglione} - Prezzo: {self.calcola_prezzo():.2f}€ - {stato} "