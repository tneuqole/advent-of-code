package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func p1() {
    file, err := os.Open("day4.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    var sum float64
    for scanner.Scan() {
        s := scanner.Text()
        raw := strings.Split(s, ":")
        raw = strings.Split(raw[1], "|")

        winningNums := strings.Fields(raw[0])
        card := strings.Fields(raw[1])
        
        count := -1.0
        for _, n := range winningNums {
            if slices.Contains(card, n) {
                 count++
            }
        }

        if count > -1 {
            sum += math.Pow(2, count)
        }
    }

    fmt.Println("problem 1: ", sum)
}

func main() {
    p1()
}

