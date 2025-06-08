package main

import "slices"

type MyHashSet struct {
	size   int
	bucket [][]int
}

func Constructor() MyHashSet {
	size := 100001
	bucket := make([][]int, size)
	return MyHashSet{
		size:   size,
		bucket: bucket,
	}
}

func (this *MyHashSet) hash(key int) int {
	return key % this.size
}

func (this *MyHashSet) Add(key int) {
	idx := this.hash(key)
	if !this.Contains(key) {
		this.bucket[idx] = append(this.bucket[idx], key)
	}
}

func (this *MyHashSet) Remove(key int) {
	idx := this.hash(key)
	i := slices.Index(this.bucket[idx], key)
	if i != -1 {
		this.bucket[idx] = slices.Delete(this.bucket[idx], i, i+1)
	}
}

func (this *MyHashSet) Contains(key int) bool {
	idx := this.hash(key)
	return slices.Contains(this.bucket[idx], key)
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
