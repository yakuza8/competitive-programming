import unittest
from typing import List


class Solution:
    @staticmethod
    def leastInterval(tasks: List[str], n: int) -> int:
        """
        Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a
        different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time,
        the CPU could complete either one task or just be idle.

        However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same
        letter in the array), that is that there must be at least n units of time between any two same tasks.

        Return the least number of units of times that the CPU will take to finish all the given tasks.

        Example 1:
            Input: tasks = ["A","A","A","B","B","B"], n = 2
            Output: 8
            Explanation:
            A -> B -> idle -> A -> B -> idle -> A -> B
            There is at least 2 units of time between any two same tasks.

        Example 2:
            Input: tasks = ["A","A","A","B","B","B"], n = 0
            Output: 6
            Explanation: On this case any permutation of size 6 would work since n = 0.
            ["A","A","A","B","B","B"]
            ["A","B","A","B","A","B"]
            ["B","B","B","A","A","A"]
            ...
            And so on.

        Example 3:
            Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
            Output: 16
            Explanation:
            One possible solution is
            A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

        Constraints:
            1 <= task.length <= 104
            tasks[i] is upper-case English letter.
            The integer n is in the range [0, 100].
        """
        from collections import Counter

        task_length = len(tasks)
        if task_length == 0:
            return 0

        task_counts = Counter(tasks)
        most_common = task_counts.most_common(1)[0][1]
        max_count = sum(1 for count in task_counts.values() if count == most_common)

        minimum_segment = most_common - 1
        unused_capacity = (n - max_count + 1) * minimum_segment
        tasks_to_schedule = task_length - most_common * max_count
        idles = max(0, unused_capacity - tasks_to_schedule)
        return task_length + idles


class TaskScheduler(unittest.TestCase):
    def test_case_1(self):
        tasks = ['A', 'A', 'A', 'B', 'B', 'B']
        n = 2
        expected_result = 8
        self.assertEqual(str(expected_result), str(Solution.leastInterval(tasks, n)))

    def test_case_2(self):
        tasks = ['A', 'A', 'A', 'B', 'B', 'B']
        n = 0
        expected_result = 6
        self.assertEqual(str(expected_result), str(Solution.leastInterval(tasks, n)))

    def test_case_3(self):
        tasks = ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        n = 2
        expected_result = 16
        self.assertEqual(str(expected_result), str(Solution.leastInterval(tasks, n)))
