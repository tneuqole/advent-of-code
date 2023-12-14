package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func p1(seqs [][]int) {
    var sum int
    for _, seq := range seqs {
        hist := make([][]int, 1)
        hist[0] = seq
        current := seq

        var zero bool
        for !zero {
            var next []int
            zero = true
            for i := 0; i < len(current)-1; i++ {
                n := current[i+1] - current[i]
                next = append(next, n)

                if n != 0 && zero {
                    zero = false
                }
            }

            hist = append(hist, next)
            current = next
        }

        hist[len(hist)-1] = append(hist[len(hist)-1], 0)
        for i := len(hist)-1; i > 0; i-- {
            a := hist[i][len(hist[i])-1] + hist[i-1][len(hist[i-1])-1]
            hist[i-1] = append(hist[i-1], a)
        }

        sum += hist[0][len(hist[0])-1]
    }
    fmt.Println("problem 1: ", sum)
}

func p2(seqs [][]int) {
    var sum int
    for _, seq := range seqs {
        hist := make([][]int, 1)
        hist[0] = seq
        current := seq

        var zero bool
        for !zero {
            var next []int
            zero = true
            for i := 0; i < len(current)-1; i++ {
                n := current[i+1] - current[i]
                next = append(next, n)

                if n != 0 && zero {
                    zero = false
                }
            }

            hist = append(hist, next)
            current = next
        }

        hist[len(hist)-1] = append([]int{0}, hist[len(hist)-1]...)
        for i := len(hist)-1; i > 0; i-- {
            a := hist[i-1][0] - hist[i][0]
            hist[i-1] = append([]int{a}, hist[i-1]...)
        }

        sum += hist[0][0]
    }
    fmt.Println("problem 2: ", sum)
}

func main() {
    file, err := os.Open("day9.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    var seqs [][]int
    for scanner.Scan() {
        s := scanner.Text()
        raw := strings.Fields(s)
        seq := make([]int, len(raw))
        for idx, x := range raw {
            y, _ := strconv.Atoi(x)
            seq[idx] = y
        }
        seqs = append(seqs, seq)
    }

    p1(seqs)
    p2(seqs)
}
