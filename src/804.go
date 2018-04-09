package main

import (
	"fmt"
)

func main() {
	words := []string{"gin", "zen", "gig", "msg"}
	var l int
	l = uniqueMorseRepresentations(words)
	fmt.Println(l)
}

func uniqueMorseRepresentations(words []string) int {
	letterMapMorse := map[rune]string{
		'a': ".-",
		'b': "-...",
		'c': "-.-.",
		'd': "-..",
		'e': ".",
		'f': "..-.",
		'g': "--.",
		'h': "....",
		'i': "..",
		'j': ".---",
		'k': "-.-",
		'l': ".-..",
		'm': "--",
		'n': "-.",
		'o': "---",
		'p': ".--.",
		'q': "--.-",
		'r': ".-.",
		's': "...",
		't': "-",
		'u': "..-",
		'v': "...-",
		'w': ".--",
		'x': "-..-",
		'y': "-.--",
		'z': "--..",
	}
	set := make(map[string]bool)
	for _, value := range words {
		var morse string
		for _, char := range value {	
			morse += letterMapMorse[char]
		}
		set[morse] = true
	}
	return len(set)
}