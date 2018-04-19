package main

import (
    "fmt"
)
type Test struct {
    Name string
}

func main() {
    t := Test{"hei"}
    var pt *Test
    pt = &t;
    fmt.Println(pt)
}
