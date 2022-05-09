import unittest
from braces import are_braces_balanced


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


if __name__ == '__main__':
    unittest.main()
