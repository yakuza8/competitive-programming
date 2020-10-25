package rangeadditiontwo

import (
	"fmt"
	"reflect"
	"testing"
)

func TestRangeAdditionTwo(t *testing.T) {
	var tests = []struct {
		m, n     int
		ops      [][]int
		expected int
	}{
		{3, 3, [][]int{{2, 2}, {3, 3}}, 4},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v %v %v", test.m, test.n, test.ops)
		t.Run(testname, func(t *testing.T) {
			ans := maxCount(test.m, test.n, test.ops)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
