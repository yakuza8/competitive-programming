package findpivotindex

import (
	"fmt"
	"reflect"
	"testing"
)

func TestFindPivotIndex(t *testing.T) {
	var tests = []struct {
		nums     []int
		expected int
	}{
		{[]int{1, 7, 3, 6, 5, 6}, 3},
		{[]int{1, 2, 3}, -1},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.nums)
		t.Run(testname, func(t *testing.T) {
			ans := pivotIndex(test.nums)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
