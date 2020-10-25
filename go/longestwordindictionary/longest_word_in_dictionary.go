package longestwordindictionary

import (
	"sort"
)

type ByLexicalAndLen []string

func (a ByLexicalAndLen) Len() int {
	return len(a)
}
func (a ByLexicalAndLen) Less(i, j int) bool {
	if len(a[i]) < len(a[j]) {
		return false
	} else if len(a[i]) > len(a[j]) {
		return true
	} else {
		if a[i][0] < a[j][0] {
			return true
		} else if a[i][0] > a[j][0] {
			return false
		} else {
			return a[i] < a[j]
		}
	}
}

func (a ByLexicalAndLen) Swap(i, j int) {
	a[i], a[j] = a[j], a[i]
}

// Check all sub letters exist in dictionary
func checkElementLetterExist(word *string, dictionary map[string]bool) bool {
	for index, _ := range *word {
		if _, ok := dictionary[(*word)[:index+1]]; !ok {
			return false
		}
	}
	return true
}

// Given a list of strings words representing an English Dictionary, find the longest word in words that can be built
// one character at a time by other words in words. If there is more than one possible answer, return the longest word
// with the smallest lexicographical order.
// If there is no answer, return the empty string.
//
// Example 1:
// Input:
// words = ["w","wo","wor","worl", "world"]
// Output: "world"
// Explanation:
// The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
//
// Example 2:
// Input:
// words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
// Output: "apple"
// Explanation:
// Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller
// than "apply".
//
// Note:
// 		All the strings in the input will only contain lowercase letters.
// 		The length of words will be in the range [1, 1000].
// 		The length of words[i] will be in the range [1, 30].
func longestWord(words []string) string {
	// Sort by custom order
	sort.Sort(ByLexicalAndLen(words))

	// Create lookup table
	dictionary := make(map[string]bool)
	for _, word := range words {
		dictionary[word] = false
	}

	for _, word := range words {
		if checkElementLetterExist(&word, dictionary) {
			return word
		}
	}
	return ""
}
