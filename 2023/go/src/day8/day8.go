package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func p1(lr string, m map[string][2]string) {
    var i, count int
    key := "AAA"
    for {
        if i > len(lr)-1 {
            i = 0
        }

        d := string(lr[i])
        if d == "L" {
            key = m[key][0]
        } else {
            key = m[key][1]
        }
        
        count++
        if key == "ZZZ" {
            break
        }
        i++
    }
    fmt.Println("problem 1: ", count)
}

func lcm(a int, b int) int {
    return a*b/gcd(a,b)
}

// gcd(a, b, c) = gcd(a, gcd(b, c)) = gcd(gcd(a, b), c) = gcd(gcd(a, c), b).
func gcd(a int, b int) int {
    if (a == b) {
        return a
    }

    var l, s int
    if a > b {
        l = a
        s = b
    } else {
        l = b
        s = a
    }

    if s == 0 {
        return l
    }

    return gcd(s, l % s)
}


func p2(lr string, m map[string][2]string, keys []string) {
    var counts []int
    for _, key := range keys {
        var i, count int
        for {
            if i > len(lr)-1 {
                i = 0
            }

            d := string(lr[i])
            if d == "L" {
                key = m[key][0]
            } else {
                key = m[key][1]
            }

            count++
            if string(key[2]) == "Z" {
                break
            }
            i++
        }   
        counts = append(counts, count)
    }
    fmt.Println(counts)

    res := lcm(counts[0], counts[1])
    for i := 2; i < len(counts); i++ {
        res = lcm(res, counts[i])
    }

    fmt.Println("problem 2: ", res)
}



func main() {
    file, err := os.Open("day8.txt")
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)
    scanner.Scan()
    lr := scanner.Text()
    scanner.Scan()

    var start []string
    m := make(map[string][2]string)
    for scanner.Scan() {
        s := scanner.Text()
        fields := strings.Fields(s)
        key := fields[0]
        m[key] = [2]string{strings.Trim(fields[2], "(),"), strings.Trim(fields[3], "(),")}

        if string(key[2]) == "A" {
            start = append(start, key)
        }
    }

    p1(lr, m)
    t := time.Now()
    p2(lr, m, start)
    fmt.Println("elapsed: ", time.Now().Sub(t))
}
