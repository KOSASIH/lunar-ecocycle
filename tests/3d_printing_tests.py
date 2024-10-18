import unittest
from printing_module import Printer  # Assuming a Printer class exists

class Test3DPrinter(unittest.TestCase):
    def setUp(self):
        self.printer = Printer()

    def test_print_success(self):
        result = self.printer.print("object.stl")
        self.assertTrue(result)

    def test_print_failure(self):
        result = self.printer.print("invalid_file.txt")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
