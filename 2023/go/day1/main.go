package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func d1p1() {
	file, err := os.Open("day1.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var nums [2]int
	var sum int
	for scanner.Scan() {
		s := scanner.Text()
		c := 0
		for i := 0; i < len(s); i++ {
			n, err := strconv.Atoi(string(s[i]))
			if err != nil {
				continue
			}

			nums[c] = n
			nums[1] = n
			c = 1
		}

		sum += nums[0]*10 + nums[1]
	}

	fmt.Println("problem 1: ", sum)
}

func strtonum(s string) int {
	switch s {
	case "one":
		return 1
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	}

	return 0
}

func findMinDigit(s string) (int, int) {
	for i := 0; i < len(s); i++ {
		d, err := strconv.Atoi(string(s[i]))
		if err == nil {
			return i, d
		}
	}

	return -1, -1
}

func findMaxDigit(s string) (int, int) {
	for i := len(s) - 1; i > -1; i-- {
		d, err := strconv.Atoi(string(s[i]))
		if err == nil {
			return i, d
		}
	}

	return -1, -1
}

var nums = [9]string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

func findMinWord(s string) (int, int) {
	index := len(s)
	var res string
	for _, num := range nums {
		i := strings.Index(s, num)
		if i > -1 && i < index {
			index = i
			res = num
		}
	}
	return index, strtonum(res)
}

func findMaxWord(s string) (int, int) {
	index := -1
	var res string
	for _, num := range nums {
		i := strings.LastIndex(s, num)
		if i > -1 && i > index {
			index = i
			res = num
		}
	}
	return index, strtonum(res)
}

func d1p2() {
	file, err := os.Open("day1.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var sum int
	for scanner.Scan() {
		s := scanner.Text()
		minDigitIndex, minDigit := findMinDigit(s)
		minWordIndex, minWord := findMinWord(s)
		var num1 int
		if minDigitIndex == -1 || minWordIndex < minDigitIndex {
			num1 = minWord
		} else {
			num1 = minDigit
		}

		maxDigitIndex, maxDigit := findMaxDigit(s)
		maxWordIndex, maxWord := findMaxWord(s)
		var num2 int
		if maxDigitIndex == -1 || maxWordIndex > maxDigitIndex {
			num2 = maxWord
		} else {
			num2 = maxDigit
		}

		sum += num1*10 + num2
	}
	fmt.Println("problem 2: ", sum)
}

func main() {
	d1p1()
	d1p2()
}
