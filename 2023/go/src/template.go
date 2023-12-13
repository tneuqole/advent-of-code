package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func p1() {
    fmt.Println("problem 1: ")
}

func p2() {
    fmt.Println("problem 2: ")
}


func main() {
    file, err := os.Open("test.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        s := scanner.Text()
        fmt.Println("read line: ", s)
    }
    
    p1()
    p2()
}
