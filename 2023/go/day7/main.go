package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type hand struct {
	cards    string
	winnings int
	score    int
}

func scoreHand(s string, joker bool) int {
	m := make(map[string]int)
	for _, c := range s {
		c := string(c)
		if _, contains := m[c]; contains {
			m[c] += 1
		} else {
			m[c] = 1
		}
	}

	l := len(m)
	var count int
	for k, v := range m {
		if joker && k == "J" {
			continue
		}

		if v > count {
			count = v
		}
	}

	if v, contains := m["J"]; contains && joker {
		count += v
		l -= 1
	}

	if count == 5 {
		return 7
	} else if count == 4 {
		return 6
	} else if count == 3 && l == 2 {
		return 5
	} else if count == 3 {
		return 4
	} else if count == 2 && l == 3 {
		return 3
	} else if count == 2 {
		return 2
	}

	return 1
}

func sortHands(hands []hand, joker bool) int {
	sort.Slice(hands, func(i, j int) bool {
		h1 := hands[i]
		h2 := hands[j]

		h1.score = scoreHand(h1.cards, joker)
		h2.score = scoreHand(h2.cards, joker)

		if h1.score == h2.score {
			for idx, c1 := range h1.cards {
				c1 := string(c1)
				c2 := string(h2.cards[idx])

				if c1 == c2 {
					continue
				}

				if joker && c1 == "J" {
					return true
				} else if joker && c2 == "J" {
					return false
				}

				n1, err1 := strconv.Atoi(c1)
				n2, err2 := strconv.Atoi(c2)

				if err1 != nil && err2 != nil {
					switch c1 {
					case "A":
						return false
					case "K":
						return c2 == "A"
					case "Q":
						return c2 == "A" || c2 == "K"
					case "J":
						return c2 != "T"
					case "T":
						return true
					}
				} else if err1 != nil {
					return false
				} else if err2 != nil {
					return true
				} else {
					return n1 < n2
				}
			}
		}

		return h1.score < h2.score
	})

	var sum int
	for idx, h := range hands {
		sum += (idx + 1) * h.winnings
	}

	return sum
}

func d7p1(hands []hand) {
	sum := sortHands(hands, false)
	fmt.Println("problem 1: ", sum)
}

func d7p2(hands []hand) {
	sum := sortHands(hands, true)
	fmt.Println("problem 2: ", sum)
}

func main() {
	file, _ := os.Open("day7.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var hands []hand
	for scanner.Scan() {
		s := scanner.Text()
		fields := strings.Split(s, " ")
		w, _ := strconv.Atoi(fields[1])
		h := hand{
			cards:    fields[0],
			winnings: w,
		}
		hands = append(hands, h)
	}

	d7p1(hands)
	d7p2(hands)
}
