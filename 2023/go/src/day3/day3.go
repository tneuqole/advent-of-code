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

type gear struct {
    ratio int
    count int
}

const size int = 140
var data [size][size]string
var gears [size][size]gear

// read file into matrix
func createMatrix() {
    file, err := os.Open("day3.txt") // update size
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    i := 0
    for scanner.Scan() {
        s := scanner.Text()
        for j, char := range s {
            data[i][j] = string(char)
        }
        i++
    }
}

func isDigit(s string) bool {
    _, err := strconv.Atoi(s)
    return err == nil
}

func findNum(s [size]string, start int) (string, int) {
    var num string
    index := -1
    for i := start; i < len(s); i++ {
        char := string(s[i])
        if isDigit(char) {
            num += char
            if index == -1 {
                index = i
            }
        } else if num != "" {
            break
        }
    }

    return num, index
}

func isSymbol(s string) bool {
    return !strings.ContainsAny(s, ".123456789")
}

func checkNum(s string, row int, column int) (bool, int, int) {
    // top
    if row > 0 {
        for i := -1; i < len(s)+1; i++ {
            y := column + i
            if y < 0 || y > size-1 {
                continue
            }
            if isSymbol(data[row-1][y]) {
                return true, row-1, y
            }
        }
    }

    // bottom
    if row < size - 1 {
        for i := -1; i < len(s)+1; i++ {
            y := column + i
            if y < 0 || y > size-1 {
                continue
            }

            if isSymbol(data[row+1][y]) {
                return true, row+1, y
            }
        }
    }

    // left
    if column > 0 && isSymbol(data[row][column-1]) {
        return true, row, column-1
    }

    // right
    y := column + len(s)
    if y < size-1 && isSymbol(data[row][y]) {
        return true, row, y
    }

    return false, -1, -1
}

func p1() {
    var sum int
    for rowNum, row := range data {
        var i int
        var num string
        for {
            num, i = findNum(row, i)
            if i == -1 {
                break
            }

            found, x, y := checkNum(num, rowNum, i)
            if found {
                n, _ := strconv.Atoi(num)
                sum += n

                gear := &gears[x][y]
                gear.count++
                if gear.ratio == 0 {
                    gear.ratio = 1
                }
                gear.ratio *= n
            }

            i += len(num)
        }
    }

    fmt.Println("problem 1: ", sum)
}

func p2() {
    var sum int 
    for i := 0; i < size; i++ {
        for j := 0; j < size; j++ {
            gear := gears[i][j]
            if gear.count > 1 {
                sum += gear.ratio
            }
        }
    }

    fmt.Println("problem 2: ", sum)
}



func main() {
    createMatrix()
    p1()
    p2()
}
