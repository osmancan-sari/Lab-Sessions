import unittest
from decryption import decrypt_sentence

class TestDecryption(unittest.TestCase):

    def test_decrypt_sentence(self):
        test_cases = [
            ("GRAADHADMEAPF COCBATSCB ISG MAN AAANNGOYEIGMNAG VIBLLIAACFANAR FROMFCCC THEEA CFBOAOK ADNQGAANSAIA BOYGSSAA",
             "GRAHAME COATS IS AN ANNOYING VILLIAN FROM THE BOOK ANANSI BOYS"),
            ("HISFG CATCHPHCRASCANEFGDBSAA ABSATIVEELBCYTHJAKAA LFIS COBNEE EMOF THEBAC AICGDGGCRHAINGIEST CLHWHORD EI HBTAAVEG EVEHRCKA JCSDEPEN",
             "HIS CATCHPHRASE ABSATIVELY IS ONE OF THE CRINGIEST WORD I HAVE EVER SEEN"),
            ("IE MDEAACNB DIDF YORUBI REALLYGEABB RCEMJUST COMBINEBLBALBB ABSOLUTELYIBAHJAEAA ANDHA POSCITHIAAVEDLCEYMAA",
             "I MEAN IF YOU REALLY MUST COMBINE ABSOLUTELY AND POSITIVELY"),
            ("MADKEAK LIT GBAAEBFSSOKTBIAVAELY NMOMTH WEBABIBGSAFTIVAAELY",
             "MAKE IT ABSOTIVELY NOT ABSATIVELY"),
            ("EDBABSIABTIAVOAAELY ISQE AWRANONJVG AGIN ALHLDA GFOESCORTS DJOF WNAYASU",
             "ABSATIVELY IS WRONG IN ALL SORTS OF WAYS")
        ]

        points_per_case = 100 // len(test_cases)
        total_points = 0

        for encrypted, expected in test_cases:
            actual_output = decrypt_sentence(encrypted)
            try:
                self.assertEqual(actual_output, expected)
                total_points += points_per_case
                print(f"✅ Passed! | Points: {points_per_case}\nEncrypted: '{encrypted}'\nExpected : '{expected}'\n")
            except AssertionError:
                print(f"❌ Failed!\nEncrypted: '{encrypted}'\nExpected: '{expected}'\nGot:      '{actual_output}'\n")

        print(f"\n🎯 Total Points: {total_points}/100")

if __name__ == '__main__':
    unittest.main()

