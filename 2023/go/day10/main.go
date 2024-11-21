package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strings"
)

func isPipe(s string) bool {
	return strings.Contains("|-LJ7F", s)
}

func idxOutOfBounds(x int, y int, xLimit int, yLimit int) bool {
	return x < 0 || x > xLimit || y < 0 || y > yLimit
}

func getAdjacentEdges(x int, y int, graph [][]string) [][]int {
	edges := make([][]int, 0)

	c := graph[y][x]
	yLimit := len(graph) - 1
	xLimit := len(graph[y]) - 1
	// wrong
	if c == "S" {
		if !idxOutOfBounds(x, y+1, xLimit, yLimit) && strings.Contains("|JL", graph[y+1][x]) {
			edges = append(edges, []int{x, y + 1})
		}

		if !idxOutOfBounds(x, y-1, xLimit, yLimit) && strings.Contains("F7|", graph[y-1][x]) {
			edges = append(edges, []int{x, y - 1})
		}

		if !idxOutOfBounds(x-1, y, xLimit, yLimit) && strings.Contains("-FL", graph[y][x-1]) {
			edges = append(edges, []int{x - 1, y})
		}

		if !idxOutOfBounds(x+1, y, xLimit, yLimit) && strings.Contains("-J7", graph[y][x+1]) {
			edges = append(edges, []int{x + 1, y})
		}
	} else if c == "|" {
		if !idxOutOfBounds(x, y+1, xLimit, yLimit) && isPipe(graph[y+1][x]) {
			edges = append(edges, []int{x, y + 1})
		}

		if !idxOutOfBounds(x, y-1, xLimit, yLimit) && isPipe(graph[y-1][x]) {
			edges = append(edges, []int{x, y - 1})
		}
	} else if c == "-" {
		if !idxOutOfBounds(x-1, y, xLimit, yLimit) && isPipe(graph[y][x-1]) {
			edges = append(edges, []int{x - 1, y})
		}

		if !idxOutOfBounds(x+1, y, xLimit, yLimit) && isPipe(graph[y][x+1]) {
			edges = append(edges, []int{x + 1, y})
		}
	} else if c == "L" {
		if !idxOutOfBounds(x, y-1, xLimit, yLimit) && isPipe(graph[y-1][x]) {
			edges = append(edges, []int{x, y - 1})
		}

		if !idxOutOfBounds(x+1, y, xLimit, yLimit) && isPipe(graph[y][x+1]) {
			edges = append(edges, []int{x + 1, y})
		}
	} else if c == "J" {
		if !idxOutOfBounds(x, y-1, xLimit, yLimit) && isPipe(graph[y-1][x]) {
			edges = append(edges, []int{x, y - 1})
		}

		if !idxOutOfBounds(x-1, y, xLimit, yLimit) && isPipe(graph[y][x-1]) {
			edges = append(edges, []int{x - 1, y})
		}

	} else if c == "7" {
		if !idxOutOfBounds(x-1, y, xLimit, yLimit) && isPipe(graph[y][x-1]) {
			edges = append(edges, []int{x - 1, y})
		}

		if !idxOutOfBounds(x, y+1, xLimit, yLimit) && isPipe(graph[y+1][x]) {
			edges = append(edges, []int{x, y + 1})
		}

	} else if c == "F" {
		if !idxOutOfBounds(x+1, y, xLimit, yLimit) && isPipe(graph[y][x+1]) {
			edges = append(edges, []int{x + 1, y})
		}

		if !idxOutOfBounds(x, y+1, xLimit, yLimit) && isPipe(graph[y+1][x]) {
			edges = append(edges, []int{x, y + 1})
		}
	}
	return edges
}

func bfs(x int, y int, graph [][]string) int {
	var longest int
	queue := make([][]int, 0)
	explored := make([][]bool, len(graph))
	for i := range explored {
		explored[i] = make([]bool, len(graph[0]))
	}

	queue = append(queue, []int{x, y, 0})
	explored[y][x] = true

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]

		if v[2] > longest {
			longest = v[2]
		}

		for _, edge := range getAdjacentEdges(v[0], v[1], graph) {
			x, y := edge[0], edge[1]
			if !explored[y][x] {
				explored[y][x] = true
				queue = append(queue, []int{x, y, v[2] + 1})
			}
		}
	}

	return longest
}

func d10p1(x int, y int, tiles [][]string) {
	ans := bfs(x, y, tiles)

	fmt.Println("problem 1: ", ans)
}

func d10p2() {
	fmt.Println("problem 2: ")
}

func main() {
	file, _ := os.Open("day10.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var tiles [][]string
	var x, y int
	for scanner.Scan() {
		s := scanner.Text()
		row := strings.Split(s, "")
		tiles = append(tiles, row)

		idx := slices.Index(row, "S")
		if idx != -1 {
			y = len(tiles) - 1
			x = idx
		}
	}

	d10p1(x, y, tiles)
	d10p2()
}
