import unittest


class Solution:

    @staticmethod
    def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        """
        Find the total area covered by two rectilinear rectangles in a 2D plane.
        Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

        Example:
        Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
        Output: 45

        Note:
        Assume that the total area is never beyond the maximum possible value of int.

        Runtime: 52 ms, faster than 61.63% of Python3 online submissions for Rectangle Area.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Rectangle Area.
        """

        def find_intersection_size(x1, y1, x2, y2):
            intersect_max = min(y1, y2)
            intersect_min = max(x1, x2)
            intersect_range = intersect_max - intersect_min if intersect_max > intersect_min else 0
            return intersect_range

        def find_area(_A: int, _B: int, _C: int, _D: int) -> int:
            return (_C - _A) * (_D - _B)

        return find_area(A, B, C, D) + find_area(E, F, G, H) \
               - find_intersection_size(A, C, E, G) * find_intersection_size(B, D, F, H)


class RectangleArea(unittest.TestCase):

    def test_case_1(self):
        expected_output = 45
        self.assertEqual(expected_output, Solution.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2))
