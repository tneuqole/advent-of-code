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

const maxRed int = 12
const maxGreen int = 13
const maxBlue int = 14

func p1() {
    file, err := os.Open("day2.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    var sum int
    for scanner.Scan() {
        s := scanner.Text()

        temp := strings.Split(s, ":")
        gameId, _ := strconv.Atoi(strings.Split(temp[0], " ")[1])
        valid := true

        temp = strings.Split(temp[1], ";")
        for _, round := range(temp) {
            data := strings.Split(round, ",")
            for _, dice := range(data) {
                count := strings.Split(strings.Trim(dice, " "), " ")
                red, green, blue := 0, 0, 0
                switch count[1] {
                case "red":
                    num, _ := strconv.Atoi(count[0])
                    red += num 
                case "green":
                    num, _ := strconv.Atoi(count[0])
                    green += num
                case "blue":
                    num, _ := strconv.Atoi(count[0])
                    blue += num
                }

                if red > maxRed || green > maxGreen || blue > maxBlue {
                    valid = false
                }
            }
        }

        if valid {
            sum += gameId
        }
    }

    fmt.Println("problem 1: ", sum)
}

func p2() {
    file, err := os.Open("day2.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    var sum int
    for scanner.Scan() {
        s := scanner.Text()

        temp := strings.Split(s, ":")
        // gameId, _ := strconv.Atoi(strings.Split(strings.Trim(temp[0], " "), " ")[1])

        temp = strings.Split(temp[1], ";")
        red, green, blue := 1, 1, 1
        for _, round := range(temp) {
            data := strings.Split(round, ",")
            for _, dice := range(data) {
                count := strings.Split(strings.Trim(dice, " "), " ")
                switch count[1] {
                case "red":
                    num, _ := strconv.Atoi(count[0])
                    if num > red {
                        red = num
                    }
                case "green":
                    num, _ := strconv.Atoi(count[0])
                    if num > green {
                        green = num
                    }
                case "blue":
                    num, _ := strconv.Atoi(count[0])
                    if num > blue {
                        blue = num
                    }
                }
            }
        }
        sum += red*blue*green 
    }

    fmt.Println("problem 2: ", sum)
}



func main() {
    p1()
    p2()
}
