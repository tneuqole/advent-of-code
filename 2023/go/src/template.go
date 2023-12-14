package main

import (
	"bufio"
	"fmt"
	"os"
)

func dp1() {
    fmt.Println("problem 1: ")
}

func dp2() {
    fmt.Println("problem 2: ")
}


func d() {
    file, err := os.Open("test.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        s := scanner.Text()
        fmt.Println("read line: ", s)
    }
    
    dp1()
    dp2()
}
