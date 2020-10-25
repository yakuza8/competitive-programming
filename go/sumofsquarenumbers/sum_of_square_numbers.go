package sumofsquarenumbers

import "math"

// Given a non-negative integer c, your task is to decide whether there're two
// integers a and b such that a2 + b2 = c.
//
// Example 1:
//
// Input: 5
// Output: True
// Explanation: 1 * 1 + 2 * 2 = 5
//
//
//
// Example 2:
//
// Input: 3
// Output: False
func judgeSquareSum(c int) bool {
	for a := 0; a*a <= c; a++ {
		b := math.Sqrt(float64(c - a*a))
		if b == math.Floor(b) {
			return true
		}
	}
	return false
}
