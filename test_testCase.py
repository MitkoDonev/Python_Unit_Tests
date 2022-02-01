import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isUpper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        text = "Hello World"
        self.assertEqual(text.split(), ["Hello", "World"])

        try:
            number = 2
            self.assertEqual(number.split(), ["Hello", "World"])
        except TypeError:
            self.assertRaises(TypeError)


if __name__ == "__main__":
    unittest.main()
