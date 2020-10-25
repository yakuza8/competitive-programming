package setmismatch

import (
	"fmt"
	"reflect"
	"testing"
)

func TestSetMismatch(t *testing.T) {
	var tests = []struct {
		nums     []int
		expected []int
	}{
		{[]int{1, 2, 2, 4}, []int{2, 3}},
		{[]int{1, 1}, []int{1, 2}},
		{[]int{2, 2}, []int{2, 1}},
		{[]int{3, 2, 2}, []int{2, 1}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.nums)
		t.Run(testname, func(t *testing.T) {
			ans := findErrorNums(test.nums)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
