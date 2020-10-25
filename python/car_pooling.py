import unittest
from typing import List


class Solution:

    @staticmethod
    def carPooling(trips: List[List[int]], capacity: int) -> bool:
        """
        You are driving a vehicle that has capacity empty seats initially available for passengers. The vehicle only
        drives east (ie. it cannot turn around and drive west.)
        Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about
        the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them
        off.  The locations are given as the number of kilometers due east from your vehicle's initial location.
        Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

        Example 1:
        Input: trips = [[2,1,5],[3,3,7]], capacity = 4
        Output: false

        Example 2:
        Input: trips = [[2,1,5],[3,3,7]], capacity = 5
        Output: true

        Example 3:
        Input: trips = [[2,1,5],[3,5,7]], capacity = 3
        Output: true

        Example 4:
        Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
        Output: true

        Runtime: 56 ms, faster than 95.54% of Python3 online submissions for Car Pooling.
        Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Car Pooling.
        """
        max_end_location = max(map(lambda x: x[2], trips))
        trip_passenger_map = [0 for _ in range(max_end_location + 2)]
        passenger_map = [0 for _ in range(max_end_location + 2)]

        for passenger_count, start, end in trips:
            trip_passenger_map[start] += passenger_count
            trip_passenger_map[end] -= passenger_count

        for i in range(max_end_location + 2):
            passenger_map[i] += passenger_map[i - 1] + trip_passenger_map[i]
            if passenger_map[i] > capacity:
                return False
        return True


class CarPooling(unittest.TestCase):

    def test_case_1(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4
        expected_output = False
        self.assertEqual(expected_output, Solution.carPooling(trips, capacity))

    def test_case_2(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 5
        expected_output = True
        self.assertEqual(expected_output, Solution.carPooling(trips, capacity))

    def test_case_3(self):
        trips = [[2, 1, 5], [3, 5, 7]]
        capacity = 3
        expected_output = True
        self.assertEqual(expected_output, Solution.carPooling(trips, capacity))

    def test_case_4(self):
        trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
        capacity = 11
        expected_output = True
        self.assertEqual(expected_output, Solution.carPooling(trips, capacity))
