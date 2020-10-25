package nextgreaterelementone

import (
	"fmt"
	"reflect"
	"testing"
)

func TestNextGreaterElementOne(t *testing.T) {
	var tests = []struct {
		nums1, nums2 []int
		expected     []int
	}{
		{[]int{4, 1, 2}, []int{1, 3, 4, 2}, []int{-1, 3, -1}},
		{[]int{2, 4}, []int{1, 2, 3, 4}, []int{3, -1}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v %v", test.nums1, test.nums2)
		t.Run(testname, func(t *testing.T) {
			ans := nextGreaterElement(test.nums1, test.nums2)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
