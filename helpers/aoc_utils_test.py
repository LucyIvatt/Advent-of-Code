import unittest

from helpers.aoc_utils import get_adjacent_and_diagonal_coords


class AocUtilsTest(unittest.TestCase):

    def test_adj_and_diag_corners_single(self):
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(0, 0)], 3, 3), [(0, 1), (1, 0), (1, 1)])
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(2, 0)], 3, 3), [(1, 0), (2, 1), (1, 1)])

        self.assertCountEqual(get_adjacent_and_diagonal_coords([(0, 2)], 3, 3), [(1, 1), (1, 2), (0, 1)])
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(2, 2)], 3, 3), [(2, 1), (1, 1), (1, 2)])
    
    def test_adj_diag_middle_single(self):
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(1, 1)], 3, 3), 
                              [(0, 0), (0,1), (0,2), (1, 0), (1, 2), (2, 0), (2, 1), (2,2)])
    
    def test_adj_diag_middle_multiple(self):
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(1, 1), (1,2)], 3, 4), 
                            [(0, 0), (1,0), (2,0), (0, 1), (0, 2), (0, 3), (1, 3), (2,3), (2, 1), (2, 2)])





if __name__ == '__main__':
    unittest.main()