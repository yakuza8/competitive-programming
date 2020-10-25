package largesttrianglearea

import (
	"fmt"
	"reflect"
	"testing"
)

func TestLargestTriangleArea(t *testing.T) {
	var tests = []struct {
		points   [][]int
		expected int
	}{
		{[][]int{{0, 0}, {0, 1}, {1, 0}, {0, 2}, {2, 0}}, 2},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.points)
		t.Run(testname, func(t *testing.T) {
			ans := largestTriangleArea(test.points)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
