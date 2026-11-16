from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tuotteet = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self._tuotteet)

    def hinta(self):
        return sum(tuote.hinta() for tuote in self._tuotteet)

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._tuotteet:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return

        self._tuotteet.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self._tuotteet:
            if ostos.tuote == poistettava:
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self._tuotteet.remove(ostos)
                return

    def tyhjenna(self):
        pass

    def ostokset(self):
        return self._tuotteet
