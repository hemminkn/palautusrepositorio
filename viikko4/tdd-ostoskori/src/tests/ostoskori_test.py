import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_yksi_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_kaksi_eri_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        
        pulla = Tuote("Pulla", 2)
        self.kori.lisaa_tuote(pulla)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 5)

    
    def test_ostoskorin_hinta_ja_tavaroiden_maara_kaksi_samaa_tuotetta(self):
        pulla = Tuote("Pulla", 2)
        self.kori.lisaa_tuote(pulla)
        self.kori.lisaa_tuote(pulla)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 4)

    def test_ostoskorissa_yksi_ostos_yhden_tuotteen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_ostoskorin_ostos_sisaltaa_tuotteen_nimen_ja_lukumaara_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_ostoskorissa_kaksi_ostosta_kahden_eri_tuotteen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 3)
        pulla = Tuote("Pulla", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(pulla)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_ostoskorissa_yksi_ostos_kahden_saman_tuotteen_lisaamisen_jalkeen(self):
        pulla = Tuote("Pulla", 2)
        self.kori.lisaa_tuote(pulla)
        self.kori.lisaa_tuote(pulla)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_ostoskorin_ostos_sisaltaa_saman_tuotteen_nimen_ja_lukumaaran(self):
        pulla = Tuote("Pulla", 2)
        self.kori.lisaa_tuote(pulla)
        self.kori.lisaa_tuote(pulla)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Pulla")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_tuotteen_jota_kaksi_poistaminen_jattaa_ostosriville_yhden_kappaleen(self):
        pulla = Tuote("Pulla", 2)
        self.kori.lisaa_tuote(pulla)
        self.kori.lisaa_tuote(pulla)

        self.kori.poista_tuote(pulla)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Pulla")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_tuotteen_jota_yksi_poistaminen_tyhjentaa_korin(self):
        pulla = Tuote("Pulla", 2)
        self.kori.lisaa_tuote(pulla)

        self.kori.poista_tuote(pulla)

        self.assertEqual(self.kori.ostokset(), [])

    def test_tyhjenna_tyhjentaa_ostoskorin(self):
        pulla = Tuote("Pulla", 2)
        self.kori.lisaa_tuote(pulla)

        self.kori.tyhjenna()

        self.assertEqual(self.kori.ostokset(), [])