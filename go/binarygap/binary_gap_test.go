package binarygap

import (
	"fmt"
	"reflect"
	"testing"
)

func TestBinaryGap(t *testing.T) {
	var tests = []struct {
		N        int
		expected int
	}{
		{22, 2},
		{5, 2},
		{6, 1},
		{8, 0},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.N)
		t.Run(testname, func(t *testing.T) {
			ans := binaryGap(test.N)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
