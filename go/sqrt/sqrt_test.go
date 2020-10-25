package sqrt

import (
	"fmt"
	"testing"
)

func TestMySqrt(t *testing.T) {
	var tests = []struct {
		x        int
		expected int
	}{
		{4, 2},
		{8, 2},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%d", test.x)
		t.Run(testname, func(t *testing.T) {
			ans := mySqrt(test.x)
			if ans != test.expected {
				t.Errorf("Expected %d, but got %d", test.x, ans)
			}
		})
	}
}
