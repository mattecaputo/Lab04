class Espositore:
#Definizione della classe Espositore
    def __init__(self, id_espositore,nome,cognome):
        self.id_espositore = id_espositore
        self.nome = nome
        self.cognome = cognome
        self.stand_assegnato = None


    def __str__(self):
        if self.stand_assegnato:
            stato_stand = f" Stand assegnato: {self.stand_assegnato.id_stand}"
        else:
            stato_stand = "Nessuno stand assegnato"

        return f"{self.id_espositore} {self.nome} {self.cognome} {stato_stand}"

    def __repr__(self):
        return self.__str__()