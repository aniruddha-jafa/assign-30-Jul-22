import unittest

from main import find_ascending_num, brute_force_find_ascending_num


class Tests(unittest.TestCase):
    def setUp(self):
        self.test_cases = (
            # (num, exepected_output)
            (9, 9),
            (10,9),
            (30,29),
            (218,199),
            (389,389),
            (5552, 4999),
            (9904,8999),
            (23245, 22999),
            (11235888, 11235888),
            (111110, 99999),
            (33245, 29999),
            (1916269294, 1899999999)
        )

   
    def test_find_ascending_nums(self):
        for num, exepected_output in self.test_cases:
            output = find_ascending_num(num)
            self.assertEqual(output, exepected_output)
    
    @unittest.skip
    def test_find_ascending_nums_brute_force(self):
        for num, exepected_output in self.test_cases:
            output = brute_force_find_ascending_num(num)
            self.assertEqual(output, exepected_output)

if __name__ == '__main__':
    unittest.main()