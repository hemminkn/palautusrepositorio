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

    def _hae_ostos(self, tuote: Tuote):
        return next((ostos for ostos in self._tuotteet if ostos.tuote == tuote), None)

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = self._hae_ostos(lisattava)
        if ostos is None:
            self._tuotteet.append(Ostos(lisattava))
        else:
            ostos.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        ostos = self._hae_ostos(poistettava)
        if ostos is not None:
            ostos.muuta_lukumaaraa(-1)
            if ostos.lukumaara() == 0:
                self._tuotteet.remove(ostos)

    def tyhjenna(self):
        self._tuotteet.clear()

    def ostokset(self):
        return self._tuotteet
