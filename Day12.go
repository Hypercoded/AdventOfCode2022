package main

import (
	"fmt"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type Node struct {
	x, y       int
	pointingTo *Node
	value      int
	height     byte
	checked    bool
}

func (heightmap Heightmap) canStep(x, y int, dir string) bool {
	if dir == "up" {
		if y == heightmap.height-1 || heightmap.data[y+1][x].checked {
			return false
		}
	}
	if dir == "down" {
		if y == 0 || heightmap.data[y-1][x].checked {
			return false
		}
	}
	if dir == "right" {
		if x == heightmap.width-1 || heightmap.data[y][x+1].checked {
			return false
		}
	}
	if dir == "left" {
		if x == 0 || heightmap.data[y][x-1].checked {
			return false
		}
	}
	return true
}

type Heightmap struct {
	data [][]Node

	root Node
	end  Node

	startx, starty int
	endx, endy     int

	width, height int
}

func loadHeightmap(input string) *Heightmap {
	lines := strings.Split(input, "\n")

	heightmap := Heightmap{}

	for y := 0; y < len(lines); y++ {
		heightmap.data = append(heightmap.data, []Node{})
		for x := 0; x < len(lines[y]); x++ {
			elevation := lines[y][x]

			if elevation == 'S' {
				elevation = 'a'
				heightmap.startx = x
				heightmap.starty = y
			} else if elevation == 'E' {
				elevation = 'z'
				heightmap.endx = x
				heightmap.endy = y
			}

			heightmap.data[y] = append(
				heightmap.data[y],
				Node{x: x, y: y, height: elevation, checked: false})

		}

	}
	heightmap.root = heightmap.data[heightmap.starty][heightmap.startx]
	heightmap.end = heightmap.data[heightmap.endy][heightmap.endx]
	heightmap.height = len(heightmap.data)
	heightmap.width = len(heightmap.data[0])
	return &heightmap
}

func printHeightmap(heightmap *Heightmap) {
	nodes := heightmap.data
	for y := 0; y < len(nodes); y++ {
		for x := 0; x < len(nodes[y]); x++ {
			fmt.Print(string(nodes[y][x].height))
		}
		fmt.Print("\n")
	}
}

func main() {
	dat, err := os.ReadFile("Input/Day 12.txt")
	check(err)

	world := loadHeightmap(string(dat))

	printHeightmap(world)
	open := []Node{}

	open = append(open, world.root)
	for len(open) != 0 {
		grid := world.data
		cur := open[0]

		// get up down left right of cur, as long as they exist & are no more than 1 block above the current height
		// increment their values by 1, add them to open, remove the first item from open and move it to closed.
		x := cur.x
		y := cur.y

		// up
		_ = grid
		_ = x
		_ = y
		//down
		fmt.Print((cur.x), cur.y, "\n")

		if world.canStep(x, y, "up") {
			add := true
			for i := 0; i < len(open); i++ {

				if open[i].y == y+1 {
					add = false
				}
			}
			if add == true {
				open = append(open, grid[y+1][x])
			}

		}
		if world.canStep(x, y, "down") {

			add := true
			for i := 0; i < len(open); i++ {

				if open[i].y == y-1 {
					add = false
				}
			}
			if add == true {
				open = append(open, grid[y-1][x])
			}
		}
		if world.canStep(x, y, "right") {
			add := true
			for i := 0; i < len(open); i++ {

				if open[i].x == x+1 {
					add = false
				}
			}
			if add == true {
				open = append(open, grid[y][x+1])
			}
		}
		if world.canStep(x, y, "left") {
			add := true
			for i := 0; i < len(open); i++ {

				if open[i].x == x-1 {
					add = false
				}
			}
			if add == true {
				open = append(open, grid[y][x-1])
			}
		}

		cur.checked = true
		grid[y][x].checked = true
		//figured out the issue its bc everything keeps getting added to open

		open = open[1:]

	}

}
