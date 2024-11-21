package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type seed struct {
	num         int
	soil        int
	fertilizer  int
	water       int
	light       int
	temperature int
	humidity    int
	location    int
}

type mapping struct {
	source int
	dest   int
	len    int
}

var (
	seeds                 []seed
	seedToSoil            []mapping
	soilToFertilizer      []mapping
	fertilizerToWater     []mapping
	waterToLight          []mapping
	lightToTemperature    []mapping
	temperatureToHumidity []mapping
	humidityToLocation    []mapping
)

func readMappings(scanner *bufio.Scanner, list *[]mapping) {
	for scanner.Scan() {
		s := scanner.Text()
		if len(s) == 0 {
			break
		} else if strings.Contains(s, ":") {
			continue
		}

		nums := strings.Fields(s)
		d, _ := strconv.Atoi(nums[0])
		src, _ := strconv.Atoi(nums[1])
		l, _ := strconv.Atoi(nums[2])
		m := mapping{
			source: src,
			dest:   d,
			len:    l,
		}

		*list = append(*list, m)
	}
}

func findMapping(num int, list []mapping) int {
	for _, m := range list {
		if m.source <= num && num <= m.source+m.len-1 {
			return m.dest + num - m.source
		}
	}

	return num
}

func d5p1() {
	file, _ := os.Open("day5.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	seedsRaw := scanner.Text()
	seedNums := strings.Fields(strings.Split(seedsRaw, ":")[1])
	scanner.Scan()
	for _, n := range seedNums {
		num, _ := strconv.Atoi(n)
		seed := seed{
			num: num,
		}
		seeds = append(seeds, seed)
	}

	readMappings(scanner, &seedToSoil)
	readMappings(scanner, &soilToFertilizer)
	readMappings(scanner, &fertilizerToWater)
	readMappings(scanner, &waterToLight)
	readMappings(scanner, &lightToTemperature)
	readMappings(scanner, &temperatureToHumidity)
	readMappings(scanner, &humidityToLocation)

	lowest := -1
	for _, seed := range seeds {
		seed.soil = findMapping(seed.num, seedToSoil)
		seed.fertilizer = findMapping(seed.soil, soilToFertilizer)
		seed.water = findMapping(seed.fertilizer, fertilizerToWater)
		seed.light = findMapping(seed.water, waterToLight)
		seed.temperature = findMapping(seed.light, lightToTemperature)
		seed.humidity = findMapping(seed.temperature, temperatureToHumidity)
		seed.location = findMapping(seed.humidity, humidityToLocation)
		if lowest == -1 || seed.location < lowest {
			lowest = seed.location
		}
	}
	fmt.Println("problem 1: ", lowest)
}

func d5p2() {
	file, _ := os.Open("day5.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	seedsRaw := scanner.Text()
	seedNums := strings.Fields(strings.Split(seedsRaw, ":")[1])
	scanner.Scan()

	readMappings(scanner, &seedToSoil)
	readMappings(scanner, &soilToFertilizer)
	readMappings(scanner, &fertilizerToWater)
	readMappings(scanner, &waterToLight)
	readMappings(scanner, &lightToTemperature)
	readMappings(scanner, &temperatureToHumidity)
	readMappings(scanner, &humidityToLocation)

	lowest := -1
	for i := 0; i < len(seedNums); i += 2 {
		num, _ := strconv.Atoi(seedNums[i])
		limit, _ := strconv.Atoi(seedNums[i+1])

		for j := num; j < num+limit; j++ {
			seed := seed{
				num: j,
			}
			seed.soil = findMapping(seed.num, seedToSoil)
			seed.fertilizer = findMapping(seed.soil, soilToFertilizer)
			seed.water = findMapping(seed.fertilizer, fertilizerToWater)
			seed.light = findMapping(seed.water, waterToLight)
			seed.temperature = findMapping(seed.light, lightToTemperature)
			seed.humidity = findMapping(seed.temperature, temperatureToHumidity)
			seed.location = findMapping(seed.humidity, humidityToLocation)
			if lowest == -1 || seed.location < lowest {
				lowest = seed.location
			}
		}
	}

	fmt.Println("problem 2: ", lowest)
}

func main() {
	d5p1()

	start := time.Now()
	d5p2()
	fmt.Println("elapsed: ", time.Now().Sub(start))
}
