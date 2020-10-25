package longpressedname

// Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed,
// and the character will be typed 1 or more times.
//
// You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with
// some characters (possibly none) being long pressed.
//
// Example 1:
// Input: name = "alex", typed = "aaleex"
// Output: true
// Explanation: 'a' and 'e' in 'alex' were long pressed.
//
// Example 2:
// Input: name = "saeed", typed = "ssaaedd"
// Output: false
// Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
//
// Example 3:
// Input: name = "leelee", typed = "lleeelee"
// Output: true
//
// Example 4:
// Input: name = "laiden", typed = "laiden"
// Output: true
// Explanation: It's not necessary to long press any character.
//
// Constraints:
// 		1 <= name.length <= 1000
// 		1 <= typed.length <= 1000
//The characters of name and typed are lowercase letters.
func isLongPressedName(name string, typed string) bool {
	typedIndex := 0
	var previousChar, currentChar uint8 = 0, 0
	charChanged := false

	for _, char := range name {
		if typedIndex >= len(typed) {
			return false
		}

		previousChar, currentChar = currentChar, uint8(char)
		// Check any change happened so that we can consume rest of previousChar
		charChanged = previousChar != currentChar

		if charChanged {
			for previousChar == typed[typedIndex] {
				typedIndex += 1
				if typedIndex >= len(typed) {
					return false
				}
			}
		}
		if currentChar != typed[typedIndex] {
			return false
		}
		typedIndex += 1
	}
	return typedIndex >= len(typed)-1
}
