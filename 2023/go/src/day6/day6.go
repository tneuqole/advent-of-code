package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func p1(times []string, dist[]string) {
    sum := 1
    for idx, time := range times {
        t, _ := strconv.Atoi(time)
        d, _ := strconv.Atoi(dist[idx])
        var count int
        for j := 1; j < t; j++ {
            if j * (t-j) > d {
                count++
            }
        }

        if count > 0 {
            sum *= count
        }
    }
    fmt.Println("problem 1: ", sum)
}

func getNum(nums []string) int {
    var result int
    for _, n := range nums {
        result *= int(math.Pow(10, float64(len(n))))
        num, _ := strconv.Atoi(n)
        result += num
    }

    return result
}

func p2(times []string, dist []string) {
    t := getNum(times)
    d := getNum(dist)
    var count int
    for i := 1; i < t; i++ {
        if i * (t-i) > d {
            count++
        }
    }
    fmt.Println("problem 2: ", count)
}


func main() {
    file, err := os.Open("day6.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    scanner.Scan()
    times := strings.Fields(strings.Split(scanner.Text(), ":")[1])
    scanner.Scan()
    distances := strings.Fields(strings.Split(scanner.Text(), ":")[1])
    
    p1(times, distances)
    p2(times, distances)
}
