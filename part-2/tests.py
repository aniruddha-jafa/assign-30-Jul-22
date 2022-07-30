import unittest

from main import find_ascending_num, brute_force_find_ascending_num


class Tests(unittest.TestCase):
    def setUp(self):
        self.test_cases = (
            # (num, exepected_output)
            (23245, 22999),
            (11235888, 11235888),
            (111110, 99999),
            (33245, 29999),
            (9, 9),
            (0, 0),
        )

    @unittest.skip("not implemented")
    def test_find_ascending_nums(self):
        for num, exepected_output in self.test_cases:
            output = find_ascending_num(num)
            self.assertEqual(output, exepected_output)
    
    def test_find_ascending_nums_brute_force(self):
        for num, exepected_output in self.test_cases:
            output = brute_force_find_ascending_num(num)
            self.assertEqual(output, exepected_output)

if __name__ == '__main__':
    unittest.main()