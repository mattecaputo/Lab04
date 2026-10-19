from stand import Stand

class StandPreseExtra (Stand):

    def __init__(self, id_stand, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(id_stand,superficie, padiglione, prezzo_base)
        self.numero_prese = int(numero_prese)  #Aggiunta del parametro


    def calcola_prezzo(self) -> float:
        #Calcolo del nuovo prezzo
        return self.prezzo_base * ( 1 + 0.07 * self.numero_prese)

    def __str__(self):
        if self.disponibile:
            stato = " Disponibile"
        else:
            stato = " Occupato "

        return f"{self.id_stand}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive : {self.numero_prese} - {stato}"