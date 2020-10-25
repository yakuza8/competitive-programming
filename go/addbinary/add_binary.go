package addbinary

import (
	"math"
)

// Given two binary strings, return their sum (also a binary string).
// The input strings are both non-empty and contains only characters 1 or 0.
//
// Example 1:
// Input: a = "11", b = "1"
// Output: "100"
//
// Example 2:
// Input: a = "1010", b = "1011"
// Output: "10101"
//
// Constraints:
// 		Each string consists only of '0' or '1' characters.
// 		1 <= a.length, b.length <= 10^4
// 		Each string is either "0" or doesn't contain any leading zero.
func addBinary(a string, b string) string {
	aLen := len(a)
	bLen := len(b)
	maxLen := int(math.Max(float64(aLen), float64(bLen)))

	result := ""
	trailer := '0'

	for i := 0; i < maxLen; i++ {
		aNum := '0'
		if i < aLen {
			aNum = rune(a[aLen-1-i])
		}
		bNum := '0'
		if i < bLen {
			bNum = rune(b[bLen-1-i])
		}
		currentDigit, newTrailer := sumDigit(aNum, bNum, trailer)
		result = string(currentDigit) + result
		trailer = newTrailer
	}

	if trailer == '1' {
		result = string(trailer) + result
	}

	return result
}

func sumDigit(o1, o2, o3 rune) (rune, rune) {
	sum := convertBinaryToDecimal(o1) + convertBinaryToDecimal(o2) + convertBinaryToDecimal(o3)
	return convertDecimalToBinary(sum)
}

func convertBinaryToDecimal(digit rune) int {
	switch digit {
	case 49:
		return 1
	case 48:
		return 0
	default:
		return 0
	}
}

func convertDecimalToBinary(sum int) (rune, rune) {
	switch sum {
	case 0:
		return '0', '0'
	case 1:
		return '1', '0'
	case 2:
		return '0', '1'
	case 3:
		return '1', '1'
	default:
		return '0', '0'
	}
}
