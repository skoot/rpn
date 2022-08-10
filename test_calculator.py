import unittest


def polish_eval(expression: str) -> float:
    stack_number, stack_operator = [], []
    split_number = expression.split()
    for number in split_number:
        print(number)
        print(stack_number)
        if number not in ["+", "/", "-", "*"]:
            stack_number.append(number)

        else:
            nb_1 = stack_number.pop()
            nb_2 = stack_number.pop()
            stack_number.append(eval(f'{nb_2} {number} {nb_1}'))


    return stack_number[0]



class TestPolish(unittest.TestCase):

    def test_addition(self):
        assert polish_eval('2 2 +') == 2 + 2
        pass

    def test_addition_larger_number(self):
        assert polish_eval('12 34 +') == 12 + 34
        pass

    def test_multiple_additions_at_the_end(self):
        assert polish_eval('2 2 1 + +') == 2 + 2 + 1
        pass

    def test_multiple_additions_as_we_go(self):
        assert polish_eval('2 2 + 1 +') == 2 + 2 + 1
        pass

    def test_subtraction(self):
        assert polish_eval('3 2 -') == 3 - 2
        pass

    def test_subtraction_negative_result(self):
        assert polish_eval('2 3 -') == 2 - 3
        pass

    def test_multiplication(self):
        assert polish_eval('3 2 *') == 3 * 2
        pass

    def test_division(self):
        assert polish_eval('6 2 /') == 6 / 2
        pass

    def test_division_float(self):
        assert polish_eval('2 6 /') == 2 / 6
        pass

    def test_multiple_spaces(self):
        assert polish_eval('1  2    +') == 1 + 2
        pass

    def test_tabulation_as_separator(self):
        assert polish_eval('1\t2\t+') == 1 + 2
        pass

    def test_negative_number(self):
        assert polish_eval('-4 5 *') == -4 * 5
        pass

    def test_add_and_sub(self):
        assert polish_eval('3 2 1 - +') == 3 + (2 - 1)
        pass

    def test_complex_1(self):
        assert polish_eval('4 2 5 * + 1 3 2 * + /') == (4 + (2 * 5)) / (1 + (3 * 2))
        pass

    def test_complex_2(self):
        assert polish_eval('5 1 2 + 4 * 3 - +') == 5 + (((1 + 2) * 4) - 3)
        pass


if __name__ == '__main__':
    unittest.main()
