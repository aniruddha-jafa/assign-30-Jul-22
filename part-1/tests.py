import unittest 

from main import evaluate

class Tests(unittest.TestCase):
    
    def setUp(self):
        self.test_cases = (
            ("5",5),
            ("1+2*2",5),
            ("6/2",3),
            ("5+4/2",7),
            ("2 + 8/4 + 9/3", 7),
            ("1-1-1", -1),
            ("(5+8)*3/8+3", 7.875),
        )

    def test_all(self):
        for str_input, expected_output in self.test_cases:
            self.assertEqual(evaluate(str_input), expected_output)

if __name__ == "__main__":
    unittest.main()