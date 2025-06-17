import unittest
from main import lire_csv, match_plus_parie

class TestCSV(unittest.TestCase):

    def test_match_plus_parie(self):
        chemin = "20230616-top-100-rencontres-les-plus-pariees.csv"
        resultat = match_plus_parie(chemin)
        self.assertEqual(resultat["equipe_1"], "ARGENTINE")
        self.assertEqual(resultat["equipe_2"], "FRANCE")
        self.assertEqual(resultat["n_mises"], 3834519)

    def test_nombre_de_lignes(self):
        df = lire_csv("20230616-top-100-rencontres-les-plus-pariees.csv")
        self.assertEqual(len(df), 100)

    def test_aucune_valeur_manquante_n_mises(self):
        df = lire_csv("20230616-top-100-rencontres-les-plus-pariees.csv")
        self.assertFalse(df["n_mises"].isnull().any())

    def test_noms_colonnes(self):
        df = lire_csv("20230616-top-100-rencontres-les-plus-pariees.csv")
        colonnes_attendues = [
            "sport", "competition", "equipe_1", "equipe_2",
            "date_rencontre", "mises", "n_mises", "n_joueurs"
        ]
        self.assertListEqual(list(df.columns), colonnes_attendues)

    def test_nombre_joueurs_positif(self):
        df = lire_csv("20230616-top-100-rencontres-les-plus-pariees.csv")
        df["n_joueurs"] = df["n_joueurs"].astype(str).str.replace(" ", "").astype(int)
        self.assertTrue((df["n_joueurs"] > 0).all())


    def test_presence_coupe_du_monde(self):
        df = lire_csv("20230616-top-100-rencontres-les-plus-pariees.csv")
        self.assertTrue(df["competition"].str.contains("Coupe du Monde").any())

if __name__ == "__main__":
    unittest.main()
