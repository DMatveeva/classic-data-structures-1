import unittest
from braces import are_braces_balanced
from postfix import postfix_evaluation


class MyTestCase(unittest.TestCase):

    def test_are_braces_balanced(self):
        s = '()'
        self.assertEqual(are_braces_balanced(s), True)

        s = '((()))'
        self.assertEqual(are_braces_balanced(s), True)

        s = '(()'
        self.assertEqual(are_braces_balanced(s), False)

        s = '))'
        self.assertEqual(are_braces_balanced(s), False)

        s = '(('
        self.assertEqual(are_braces_balanced(s), False)

        s = ')()('
        self.assertEqual(are_braces_balanced(s), False)

    def test_postfix(self):
        s = '8 2 + 5 * 9 + ='
        self.assertEqual(postfix_evaluation(s), 59)

        s = '1 2 + 3 * ='
        self.assertEqual(postfix_evaluation(s), 9)




if __name__ == '__main__':
    unittest.main()
