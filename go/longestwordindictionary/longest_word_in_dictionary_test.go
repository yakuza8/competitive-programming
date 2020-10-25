package longestwordindictionary

import (
	"fmt"
	"reflect"
	"testing"
)

func TestLongestWordInDictionary(t *testing.T) {
	var tests = []struct {
		words    []string
		expected string
	}{
		{[]string{"w","wo","wor","worl", "world"}, "world"},
		{[]string{"a", "banana", "app", "appl", "ap", "apply", "apple"}, "apple"},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.words)
		t.Run(testname, func(t *testing.T) {
			ans := longestWord(test.words)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected %v, but got %v", test.expected, ans)
			}
		})
	}
}
