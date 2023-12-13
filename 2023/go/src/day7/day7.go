package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func p1(hands []hand) {
    sort.Slice(hands, func(i, j int) bool {
        h1 := hands[i]
        h2 := hands[j]
        if h1.score == h2.score {
            for idx, c1 := range h1.cards {
                c1 := string(c1)
                c2 := string(h2.cards[idx])

                if c1 == c2 {
                    continue
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
        sum += (idx+1)*h.winnings
    }
    fmt.Println("problem 1: ", sum)
}

func p2() {
    fmt.Println("problem 2: ")
}

type hand struct {
    cards string
    winnings int
    score int
}

func scoreHand(s string) int {
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
    for _, v := range m {
        if v > count {
            count = v
        }
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

func main() {
    file, err := os.Open("day7.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    var hands []hand
    for scanner.Scan() {
        s := scanner.Text()
        fields := strings.Split(s, " ")
        w, _ := strconv.Atoi(fields[1])
        h := hand {
            cards: fields[0],
            winnings: w,
            score: scoreHand(fields[0]),
        }
        hands = append(hands, h)
    }

    p1(hands)
    p2()
}
