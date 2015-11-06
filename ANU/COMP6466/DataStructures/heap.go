package main

import "math"
import "fmt"
import "errors"

type intHeap struct {
	nodes     []int
	heap_size int
}

func left(i int) int {
	return 2*i + 1
}

func right(i int) int {
	return 2*i + 2
}

func parent(i int) int {
	return int(math.Floor(float64((i - 1) / 2)))
}

func (A *intHeap) MAX_HEAPIFY(i int) {
	l := left(i)
	r := right(i)
	largest := i
	if l < A.heap_size && A.nodes[l] > A.nodes[i] {
		largest = l
	}
	if r < A.heap_size && A.nodes[r] > A.nodes[largest] {
		largest = r
	}
	if largest != i {
		A.nodes[i], A.nodes[largest] = A.nodes[largest], A.nodes[i]
		A.MAX_HEAPIFY(largest)
	}
}

func BUILD_MAX_HEAP(A []int) intHeap {
	ih := intHeap{A, len(A)}
	for i := int(math.Floor(float64(len(A) / 2))); i >= 0; i-- {
		ih.MAX_HEAPIFY(i)
	}
	return ih
}

func (ih *intHeap) HEAP_MAXIMUM() int {
	return ih.nodes[0]
}

func (ih *intHeap) HEAP_EXTRACT_MAX() (int, error) {
	if ih.heap_size < 1 {
		err := errors.New("Heap Underflow")
		return -1, err
	}
	max := ih.nodes[0]
	ih.nodes[0] = ih.nodes[ih.heap_size-1]
	ih.heap_size -= 1
	ih.MAX_HEAPIFY(0)
	return max, nil
}

func (ih *intHeap) HEAP_INCREASE_KEY(i int, key int) error {
	if ih.nodes[i] > key {
		return errors.New("New Key is smaller than current Key")
	}
	ih.nodes[i] = key
	for ih.nodes[parent(i)] < ih.nodes[i] {
		ih.nodes[parent(i)], ih.nodes[i] = ih.nodes[i], ih.nodes[parent(i)]
		i = parent(i)
	}
	return nil
}

func (ih *intHeap) MAX_HEAP_INSERT(key int) {
	ih.heap_size += 1
	ih.nodes = append(ih.nodes, int(math.Inf(-1)))
	ih.HEAP_INCREASE_KEY(ih.heap_size-1, key)
}

func main() {
	A := []int{4, 1, 3, 2, 16, 9, 10, 14, 8, 7}
	ih := BUILD_MAX_HEAP(A)
	fmt.Println(ih)
	fmt.Println(ih.HEAP_INCREASE_KEY(8, 15))
	fmt.Println(ih)
	ih.MAX_HEAP_INSERT(11)
	fmt.Println(ih)
}
