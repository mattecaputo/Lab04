import csv
from operator import attrgetter
from espositore import Espositore
from stand import Stand, StandPreseExtra, StandPremium
class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.stand = {}
        self.espositori = {}

    @property
    def nome(self):
        #Getter per il nome del nuovo centro fieristico
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        #Setter per aggiornare il nome del centro fieristico
        self._nome = nuovo_nome



    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for riga in reader:
                    if not riga:
                        continue
                    campi = [campo.strip() for campo in riga]
                    codice = campi[0]
                    #Riconoscimento delle righe degli stand tramite il prefisso 'ST'
                    if codice.startswith("ST"):
                        id_stand = campi[0]
                        superficie = campi[1]
                        padiglione = campi[2]
                        prezzo_base = campi[3]

                        #Riconoscimento della tipologia dello stand sulla base del numero di campi e sul tipo di dato aggiuntivo
                        if len(campi) == 4:
                            self.stand[id_stand] = Stand(id_stand,superficie,padiglione, prezzo_base)

                        elif len(campi) == 5:
                            valore_extra = campi[4]

                            if valore_extra.isdigit():
                                self.stand[id_stand] = StandPreseExtra(id_stand, superficie, padiglione, prezzo_base, valore_extra)
                            else:
                                self.stand[id_stand] = StandPremium (id_stand, superficie, padiglione, prezzo_base,valore_extra)

                    elif codice.startswith("ES"):
                        id_espositore = campi[0]
                        nome_espositore = campi[1]
                        cognome_espositore = campi[2]


                        self.espositori[id_espositore] = Espositore(id_espositore, nome_espositore, cognome_espositore)

        except FileNotFoundError:
            raise FileNotFoundError(f" Il file '{file_path}' non è stato trovato")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.stand:
            raise Exception ( f"Lo stand non esiste" )
        if codice_espositore not in self.espositori:
            raise Exception (f"L'espositore non esiste" )

        stand_selezionato = self.stand[codice_stand]
        espositore_selezionato = self.espositori[codice_espositore]

        #Controlli di integrità

        if not stand_selezionato.disponibile:
            raise Exception (f"Lo stand {stand_selezionato} è già stato assegnato" )

        if espositore_selezionato.stand_assegnato is not None:
            raise Exception ( f" Errore: All'espositore {espositore_selezionato} è già stato assegnato uno stand" )

        #Esecuzione dell'associazione
        stand_selezionato.disponibile = False
        stand_selezionato.espositore = espositore_selezionato
        espositore_selezionato.stand_assegnato = stand_selezionato


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.espositori.values():
            print (espositore)


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted( self.stand.values(), key = attrgetter('prezzo_base'))
