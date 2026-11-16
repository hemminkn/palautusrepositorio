import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()
        self.varasto_saldot = {1: 10}
        self.varaston_tuotteet = {1: Tuote(1, "maito", 5)}
        self.varasto_mock.saldo.side_effect = self.varasto_saldot.get
        self.varasto_mock.hae_tuote.side_effect = self.varaston_tuotteet.get

        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumerolla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_maksettaessa_kaksi_eri_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.varasto_saldot[2] = 8
        self.varaston_tuotteet[2] = Tuote(2, "pulla", 3)

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumerolla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_maksettaessa_kaksi_samaa_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumerolla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_maksettaessa_kaksi_tuotetta_toinen_riittaa_toinen_loppu_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.varasto_saldot[2] = 0
        self.varaston_tuotteet[2] = Tuote(2, "pulla", 3)

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumerolla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_edellisten_ostosten_tiedot(self):
        # ensimmäinen ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # uudet ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        #katsotaan ettei vanha ostos näy uuden hinnassa
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [42, 43]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(2, self.viitegeneraattori_mock.uusi.call_count)
        viitenumerot = [
            kutsu.args[1]
            for kutsu in self.pankki_mock.tilisiirto.call_args_list
        ]
        self.assertEqual([42, 43], viitenumerot)

    def test_poista_korista_varastoon_palautetaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        self.varasto_mock.palauta_varastoon.assert_called_with(Tuote(1, "maito", 5))
