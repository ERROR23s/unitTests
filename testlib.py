from main import reverse
import unittest


class TestReverse(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(reverse(""), "")

    def testCorrect(self):
        self.assertEqual(reverse("abc"), "cba")

    def testSingle(self):
        self.assertEqual(reverse("a"), "a")

    def testPolidrom(self):
        self.assertEqual(reverse("aba"), "aba")

    def testWrongType(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def testList(self):
        with self.assertRaises(TypeError):
            reverse(['a','b','c'])

if __name__ == '__main__' :
    unittest.main()