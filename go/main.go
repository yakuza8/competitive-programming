package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4}
	b := a[2:]

	fmt.Println(a, len(a))
	fmt.Println(b, len(b))
	fmt.Println(a[len(a)-1])

	fmt.Println((4+7)/2)
}
