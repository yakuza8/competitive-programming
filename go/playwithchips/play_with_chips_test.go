package playwithchips

import (
	"fmt"
	"reflect"
	"testing"
)

func TestPlayWithChips(t *testing.T) {
	var tests = []struct {
		chips    []int
		expected int
	}{
		{[]int{1, 2, 3}, 1},
		{[]int{2, 2, 2, 3, 3}, 2},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.chips)
		t.Run(testname, func(t *testing.T) {
			ans := minCostToMoveChips(test.chips)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
