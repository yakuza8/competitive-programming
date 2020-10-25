package houserobber

import "fmt"

// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
// the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
// it will automatically contact the police if two adjacent houses were broken into on the same night.
//
// Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
// money you can rob tonight without alerting the police.
//
// Example 1:
// Input: [1,2,3,1]
// Output: 4
// Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
// Total amount you can rob = 1 + 3 = 4.
//
// Example 2:
// Input: [2,7,9,3,1]
// Output: 12
// Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
// Total amount you can rob = 2 + 9 + 1 = 12.
func rob(nums []int) int {
	numLen := len(nums)

	if numLen == 1 {
		return nums[0]
	} else if numLen == 2 {
		return max(nums[0], nums[1])
	}

	// Create table and set zeroth index
	tableau := make([]int, numLen+2)
	tableau[0] = 0
	tableau[1] = 0

	for index, num := range nums {
		tableau[index+2] = max(tableau[index]+num, tableau[index+1])
	}
	return tableau[numLen+1]
}

func robRecursive(nums []int) int {
	sum := 0
	return robHelper(nums, sum)
}

func robHelper(nums []int, sumUpToNow int) int {
	fmt.Println(nums, sumUpToNow)
	if numLen := len(nums); numLen == 0 {
		return 0
	} else if numLen == 1 {
		return nums[0] + sumUpToNow
	} else {
		currentSum := nums[0] + sumUpToNow
		if numLen > 2 {
			currentSum = robHelper(nums[2:], currentSum)
		}
		otherSum := robHelper(nums[1:], sumUpToNow)
		return max(currentSum, otherSum)
	}
}

func max(sum1, sum2 int) int {
	if sum1 < sum2 {
		return sum2
	}
	return sum1
}
