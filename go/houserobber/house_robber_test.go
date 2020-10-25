package houserobber

import (
	"fmt"
	"testing"
)

func TestHouseRobber(t *testing.T) {
	var tests = []struct {
		nums     []int
		expected int
	}{
		{[]int{1, 2, 3, 1}, 4},
		{[]int{2, 7, 9, 3, 1}, 12},
		// {[]int{1, 5, 1, 1, 9, 1}, 14},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.nums)
		t.Run(testname, func(t *testing.T) {
			ans := rob(test.nums)
			if ans != test.expected {
				t.Errorf("Expected %d, but got %d", test.expected, ans)
			}
		})
	}
}
