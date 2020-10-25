package longpressedname

import (
	"fmt"
	"testing"
)

func TestLongPressedName(t *testing.T) {
	var tests = []struct {
		name, typed string
		expected    bool
	}{
		{"alex", "aaleex", true},
		{"saeed", "ssaaedd", false},
		{"leelee", "lleeelee", true},
		{"laiden", "laiden", true},
		{"pyplrz", "ppyypllr", false},
		{"kikcxmvzi", "kiikcxxmmvvzz", false},
		{"alex", "alexxr", false},
		{"vtkgn", "vttkgnn", true},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v %v", test.name, test.typed)
		t.Run(testname, func(t *testing.T) {
			ans := isLongPressedName(test.name, test.typed)
			if ans != test.expected {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
