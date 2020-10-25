package plusone

import (
	"fmt"
	"reflect"
	"testing"
)

func TestPlusOne(t *testing.T) {
	var tests = []struct {
		digits   []int
		expected []int
	}{
		{[]int{1, 2, 3}, []int{1, 2, 4}},
		{[]int{4, 3, 2, 1}, []int{4, 3, 2, 2}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.digits)
		t.Run(testname, func(t *testing.T) {
			ans := plusOne(test.digits)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %d, but got %d", test.expected, ans)
			}
		})
	}
}
