from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tuotteet = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self._tuotteet)
        # kertoo korissa olevien tavaroiden lukumäärän
        # jos koriin lisätty 2 kpl tuotetta "maito",
        #   tulee metodin palauttaa 2
        # jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto",
        #   tulee metodin palauttaa 2

    def hinta(self):
        return sum(tuote.hinta() for tuote in self._tuotteet)
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._tuotteet:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return

        self._tuotteet.append(Ostos(lisattava))
        # lisää tuotteen

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self._tuotteet:
            if ostos.tuote == poistettava:
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self._tuotteet.remove(ostos)
                return
        # poistaa tuotteen

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._tuotteet
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse
        #   JA kuinka monta kappaletta kyseistä tuotetta korissa on
