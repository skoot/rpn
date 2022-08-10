import unittest


"""
In reverse Polish notation, the operators follow their operands.

For instance, to add 3 and 4 together, one would write "3 4 +" rather than "3 + 4".

If there are multiple operations, operators are given immediately after their
final operands; so the expression written "3 − 4 + 5" in conventional notation 
would be written "3 4 − 5 +" in reverse Polish notation: 4 is first subtracted
from 3, then 5 is added to it.
 
An advantage of reverse Polish notation is that it removes the need for 
parentheses that are required by infix notation. While "3 − 4 × 5" can also 
be written "3 − (4 × 5)", that means something quite different from "(3 − 4) × 5". 

In reverse Polish notation, the former could be written "3 4 5 × −", which 
unambiguously means "3 (4 5 ×) −" which reduces to "3 20 −" (which can further 
be reduced to -17); the latter could be written "3 4 − 5 ×" (or "5 3 4 − ×", 
if keeping similar formatting), which unambiguously means "(3 4 −) 5 ×".
"""


def polish_eval(expression: str) -> float:
    pass


class TestPolish(unittest.TestCase):

    def test_addition(self):
        # assert polish_eval('2 2 +') == 2 + 2
        pass

    def test_addition_larger_number(self):
        # assert polish_eval('12 34 +') == 12 + 34
        pass

    def test_multiple_additions_at_the_end(self):
        # assert polish_eval('2 2 1 + +') == 2 + 2 + 1
        pass

    def test_multiple_additions_as_we_go(self):
        # assert polish_eval('2 2 + 1 +') == 2 + 2 + 1
        pass

    def test_subtraction(self):
        # assert polish_eval('3 2 -') == 3 - 2
        pass

    def test_subtraction_negative_result(self):
        # assert polish_eval('2 3 -') == 2 - 3
        pass

    def test_multiplication(self):
        # assert polish_eval('3 2 *') == 3 * 2
        pass

    def test_division(self):
        # assert polish_eval('6 2 /') == 6 / 2
        pass

    def test_division_float(self):
        # assert polish_eval('2 6 /') == 2 / 6
        pass

    def test_multiple_spaces(self):
        # assert polish_eval('1  2    +') == 1 + 2
        pass

    def test_tabulation_as_separator(self):
        # assert polish_eval('1\t2\t+') == 1 + 2
        pass

    def test_negative_number(self):
        # assert polish_eval('-4 5 *') == -4 * 5
        pass

    def test_add_and_sub(self):
        # assert polish_eval('3 2 1 - +') == 3 + (2 - 1)
        pass

    def test_complex_1(self):
        # assert polish_eval('4 2 5 * + 1 3 2 * + /') == (4 + (2 * 5)) / (1 + (3 * 2))
        pass

    def test_complex_2(self):
        # assert polish_eval('5 1 2 + 4 * 3 - +') == 5 + (((1 + 2) * 4) - 3)
        pass


if __name__ == '__main__':
    unittest.main()
