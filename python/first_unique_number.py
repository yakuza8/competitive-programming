import unittest

from collections import OrderedDict
from typing import List


class FirstUnique:
    """
    You have a queue of integers, you need to retrieve the first unique integer in the queue.

    Implement the FirstUnique class:

        FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
        int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is
        no such integer.
        void add(int value) insert value to the queue.

    Example 1:
    --------------------------------------------------------------------------------------------------------------------
    Input:
    ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
    [[[2,3,5]],[],[5],[],[2],[],[3],[]]
    Output:
    [null,2,null,2,null,3,null,-1]

    Explanation:
    FirstUnique firstUnique = new FirstUnique([2,3,5]);
    firstUnique.showFirstUnique(); // return 2
    firstUnique.add(5);            // the queue is now [2,3,5,5]
    firstUnique.showFirstUnique(); // return 2
    firstUnique.add(2);            // the queue is now [2,3,5,5,2]
    firstUnique.showFirstUnique(); // return 3
    firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
    firstUnique.showFirstUnique(); // return -1

    Example 2:
    --------------------------------------------------------------------------------------------------------------------
    Input:
    ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
    [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
    Output:
    [null,-1,null,null,null,null,null,17]

    Explanation:
    FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
    firstUnique.showFirstUnique(); // return -1
    firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
    firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
    firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
    firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
    firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
    firstUnique.showFirstUnique(); // return 17

    Example 3:
    --------------------------------------------------------------------------------------------------------------------
    Input:
    ["FirstUnique","showFirstUnique","add","showFirstUnique"]
    [[[809]],[],[809],[]]
    Output:
    [null,809,null,-1]

    Explanation:
    FirstUnique firstUnique = new FirstUnique([809]);
    firstUnique.showFirstUnique(); // return 809
    firstUnique.add(809);          // the queue is now [809,809]
    firstUnique.showFirstUnique(); // return -1

    Constraints:
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^8
        1 <= value <= 10^8
        At most 50000 calls will be made to showFirstUnique and add.
    """

    def __init__(self, nums: List[int]):
        self.dict = OrderedDict()
        self.seen_set = set()
        for num in nums:
            self._add_item(num)

    def showFirstUnique(self) -> int:
        if not self.dict:
            return -1
        else:
            first_item = next(iter(self.dict))
            if self.dict[first_item] == 1:
                return first_item
            else:
                return -1

    def add(self, value: int) -> None:
        self._add_item(value)

    def _add_item(self, num):
        if num not in self.seen_set:
            self.dict[num] = 1
            self.seen_set.add(num)
        else:
            if num in self.dict:
                del self.dict[num]

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


class FirstUniqueNumber(unittest.TestCase):

    def test_case_1(self):
        firstUnique = FirstUnique([2, 3, 5])
        self.assertEqual(2, firstUnique.showFirstUnique())
        firstUnique.add(5)
        self.assertEqual(2, firstUnique.showFirstUnique())
        firstUnique.add(2)
        self.assertEqual(3, firstUnique.showFirstUnique())
        firstUnique.add(3)
        self.assertEqual(-1, firstUnique.showFirstUnique())

    def test_case_2(self):
        firstUnique = FirstUnique([7, 7, 7, 7, 7, 7])
        self.assertEqual(-1, firstUnique.showFirstUnique())
        firstUnique.add(7)
        firstUnique.add(3)
        self.assertEqual(3, firstUnique.showFirstUnique())
        firstUnique.add(3)
        firstUnique.add(7)
        firstUnique.add(17)
        self.assertEqual(17, firstUnique.showFirstUnique())

    def test_case_3(self):
        firstUnique = FirstUnique([809])
        self.assertEqual(809, firstUnique.showFirstUnique())
        firstUnique.add(809)
        self.assertEqual(-1, firstUnique.showFirstUnique())
