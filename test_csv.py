import unittest
from main import match_plus_parie

class TestCSV(unittest.TestCase):
    def test_match_plus_parie(self):
        chemin = "20230616-top-100-rencontres-les-plus-pariees.csv"
        resultat = match_plus_parie(chemin)

        print("Match le plus parié :", resultat)

        self.assertEqual(resultat["equipe_1"], "ARGENTINE")
        self.assertEqual(resultat["equipe_2"], "FRANCE")
        self.assertEqual(resultat["n_mises"], 3834519)

if __name__ == "__main__":
    unittest.main()
