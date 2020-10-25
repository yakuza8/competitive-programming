package plusone

// Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
//
// The digits are stored such that the most significant digit is at the head of the list, and each element in the array
// contain a single digit.
//
// You may assume the integer does not contain any leading zero, except the number 0 itself.
//
// Example 1:
// Input: [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
//
// Example 2:
// Input: [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.
func plusOne(digits []int) []int {
	digitLength := len(digits)

	returnSlice := make([]int, digitLength)

	propagateNext := 1
	for i := 0; i < digitLength; i++ {
		index := digitLength - i - 1
		c := digits[index] + propagateNext

		if c <= 9 {
			returnSlice[index] = c
			propagateNext = 0
		} else {
			returnSlice[index] = 0
			propagateNext = 1
		}
	}
	if propagateNext == 1 {
		returnSlice = append([]int{1}, returnSlice...)
	}
	return returnSlice
}
