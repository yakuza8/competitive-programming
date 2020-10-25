package sumofsquarenumbers

import (
	"fmt"
	"reflect"
	"testing"
)

func TestSumOfSquareNumbers(t *testing.T) {
	var tests = []struct {
		c        int
		expected bool
	}{
		{5, true},
		{3, false},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.c)
		t.Run(testname, func(t *testing.T) {
			ans := judgeSquareSum(test.c)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
