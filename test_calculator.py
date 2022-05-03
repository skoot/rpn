import unittest



def polish_eval(expression: str) -> float:
    return 0


class TestPolish(unittest.TestCase):

    def test_addition(self):
        # assert polish_eval('2 2 +') == 4
        pass

    def test_addition_2(self):
        # assert polish_eval('2 5 +') == 7
        pass

    def test_addition_2_fail(self):
        # assert polish_eval('2 5 +') != 6
        pass

    def test_deux_additions(self):
        # assert polish_eval('2 2 1 + +') == 5
        pass

    def test_encore_deux_additions(self):
        # assert polish_eval('2 2 + 1 +') == 5
        pass

    def test_soustraction(self):
        # assert polish_eval('3 2 -') == 1
        pass

    def test_multiplication(self):
        # assert polish_eval('3 2 *') == 6
        pass

    def test_division(self):
        # assert polish_eval('6 2 /') == 3
        pass

    def test_autre_soustraction(self):
        # assert polish_eval('4 2 -') == 2
        pass

    def test_autre_addition(self):
        # assert polish_eval('3 2 +') == 5
        pass

    def test_addition_avec_espaces(self):
        # assert polish_eval('1  2    +') == 3
        pass

    def test_addition_avec_negatif(self):
        # assert polish_eval('-4 5 +') == 1
        pass

    def test_addition_et_soustraction(self):
        # assert polish_eval('3 2 1 - +') == 4
        pass

    def test_acceptance(self):
        # assert polish_eval('4 2 5 * + 1 3 2 * + /') == 2
        pass

    def test_acceptance2(self):
        # assert polish_eval('5 1 2 + 4 * 3 - +') == 14
        pass


if __name__ == '__main__':
    unittest.main()
