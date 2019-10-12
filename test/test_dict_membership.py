import unittest
from more_fun_with_collections import dict_membership as dm


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        my_dict = {'LV1': 0, 'LV2': 25, 'LV3': 50, 'LV4': 75, 'LV5': 100}
        my_value = 'LV2'
        self.assertEqual(dm.in_dict(my_dict, my_value), True)

    def test_in_dict_false(self):
        my_dict = {'Mario': 1, 'Luigi': 2, 'Bowser': 3, 'Toad': 4}
        my_value = 'Yoshi'
        self.assertEqual(dm.in_dict(my_dict, my_value), False)


if __name__ == '__main__':
    unittest.main()
